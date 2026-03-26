import csv
import json
import os
import random
import time

from otree.api import *

doc = """
Image Labelling Task.

Participants view images one at a time and provide free-text answers to
image-specific questions. The experiment has two 90-minute task blocks
separated by an optional 15-minute break.

Session config keys:
  task_minutes  (int, default 90)  — duration of each task block in minutes
  break_minutes (int, default 15)  — duration of the break in minutes
"""


# ---------------------------------------------------------------------------
# Load image data at module import time
# ---------------------------------------------------------------------------

def _load_image_data():
    csv_path = os.path.join(os.path.dirname(__file__), 'images_data.csv')
    images = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            images.append({
                'filename': row['filename'].strip(),
                'question': row['question'].strip(),
            })
    return images


IMAGE_DATA = _load_image_data()


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

class C(BaseConstants):
    NAME_IN_URL = 'image_labelling'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    TASK_MINUTES_DEFAULT = 90
    BREAK_MINUTES_DEFAULT = 15

    TRAINING_IMAGE = 'training_example.svg'
    TRAINING_QUESTION = (
        'This is a practice trial to familiarise you with the task. '
        'Describe what you see in this image in one or two sentences. '
        'Your answer here will not be recorded.'
    )


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

class Subsession(BaseSubsession):
    def creating_session(self):
        """Assign a shuffled image order to every player when the session is created."""
        for player in self.get_players():
            order = list(range(len(IMAGE_DATA)))
            random.shuffle(order)
            player.image_order = json.dumps(order)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Shuffled list of IMAGE_DATA indices, serialised as JSON
    image_order = models.LongStringField()
    # Points to the next image to show (incremented after each submission)
    current_image_index = models.IntegerField(initial=0)

    # Break decision (set on BreakChoice page)
    break_choice = models.BooleanField(
        label='Would you like to take a 15-minute break before continuing?',
        choices=[
            [True,  'Yes, I would like to take a 15-minute break'],
            [False, 'No, I will continue working'],
        ],
        widget=widgets.RadioSelect,
    )

    # Training answer — stored for completeness but not analysed
    training_answer = models.LongStringField(
        label='Your answer (practice)',
        blank=True,
    )

    # Server-side timestamps (Unix epoch, seconds)
    task1_start_time = models.FloatField(null=True)
    task2_start_time = models.FloatField(null=True)


class Answer(ExtraModel):
    """One row per image-labelling response."""
    player = models.Link(Player)

    # 1 = first 90-min block
    # 2 = 15-min bridge (no-break participants only)
    # 3 = second 90-min block
    block = models.IntegerField()

    image_index    = models.IntegerField()   # position in the shuffled order
    image_filename = models.StringField()
    question       = models.StringField()
    answer_text    = models.LongStringField()
    response_time_ms = models.FloatField()   # ms from image display to submission
    timestamp      = models.FloatField()     # Unix epoch


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _get_image_payload(player):
    """Return the next image dict for a player, or None if pool exhausted."""
    # Initialise image_order here as a fallback in case creating_session was
    # not called (e.g. when reusing an existing session / stale database).
    if player.field_maybe_none('image_order') is None:
        order = list(range(len(IMAGE_DATA)))
        random.shuffle(order)
        player.image_order = json.dumps(order)
    order = json.loads(player.image_order)
    idx = player.current_image_index
    if idx >= len(order):
        return None
    img = IMAGE_DATA[order[idx]]
    return {
        'filename': img['filename'],
        'question':  img['question'],
        'index':     idx,
        'total':     len(order),
    }


def _task_live_method(player, data, block):
    """
    Handles two message types from the client:
      'request_image'  — send the current image to the participant
      'submit_answer'  — save the answer, advance index, send next image
    """
    if data.get('type') == 'request_image':
        payload = _get_image_payload(player)
        if payload:
            return {player.id_in_group: {'type': 'image', **payload}}
        return {player.id_in_group: {'type': 'pool_exhausted'}}

    if data.get('type') == 'submit_answer':
        order = json.loads(player.image_order)
        idx   = player.current_image_index
        img   = IMAGE_DATA[order[idx]] if idx < len(order) else {}

        Answer.create(
            player=player,
            block=block,
            image_index=idx,
            image_filename=img.get('filename', ''),
            question=img.get('question', ''),
            answer_text=data.get('answer', ''),
            response_time_ms=data.get('response_time_ms', 0),
            timestamp=time.time(),
        )
        player.current_image_index += 1

        payload = _get_image_payload(player)
        if payload:
            return {player.id_in_group: {'type': 'image', **payload}}
        return {player.id_in_group: {'type': 'pool_exhausted'}}

    return {}


def _task_duration(player):
    return int(player.session.config.get('task_minutes',  C.TASK_MINUTES_DEFAULT)  * 60)


def _break_duration(player):
    return int(player.session.config.get('break_minutes', C.BREAK_MINUTES_DEFAULT) * 60)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

class Welcome(Page):
    pass


class Instructions(Page):
    pass


class TrainingExample(Page):
    form_model  = 'player'
    form_fields = ['training_answer']

    @staticmethod
    def vars_for_template(player):
        return {
            'training_image':    C.TRAINING_IMAGE,
            'training_question': C.TRAINING_QUESTION,
        }


class Task1(Page):
    template_name = 'image_labelling/TaskPage.html'

    @staticmethod
    def get_timeout_seconds(player):
        return _task_duration(player)

    @staticmethod
    def js_vars(player):
        return dict(first_image=_get_image_payload(player) or {})

    @staticmethod
    def vars_for_template(player):
        player.task1_start_time = time.time()
        return {
            'duration_seconds': _task_duration(player),
            'block_label': 'Session 1 of 2',
        }

    @staticmethod
    def live_method(player, data):
        return _task_live_method(player, data, block=1)


class BreakChoice(Page):
    form_model  = 'player'
    form_fields = ['break_choice']


class BreakWait(Page):
    """Locked break screen for participants who chose to take a break."""

    @staticmethod
    def is_displayed(player):
        return player.break_choice == True

    @staticmethod
    def get_timeout_seconds(player):
        return _break_duration(player)

    @staticmethod
    def vars_for_template(player):
        return {'duration_seconds': _break_duration(player)}


class BridgeTask(Page):
    """15-minute task continuation for participants who chose NOT to take a break."""
    template_name = 'image_labelling/TaskPage.html'

    @staticmethod
    def is_displayed(player):
        return player.break_choice == False

    @staticmethod
    def get_timeout_seconds(player):
        return _break_duration(player)

    @staticmethod
    def js_vars(player):
        return dict(first_image=_get_image_payload(player) or {})

    @staticmethod
    def vars_for_template(player):
        return {
            'duration_seconds': _break_duration(player),
            'block_label': 'Session 1 of 2 (continuing through break)',
        }

    @staticmethod
    def live_method(player, data):
        return _task_live_method(player, data, block=2)


class Task2(Page):
    template_name = 'image_labelling/TaskPage.html'

    @staticmethod
    def get_timeout_seconds(player):
        return _task_duration(player)

    @staticmethod
    def js_vars(player):
        return dict(first_image=_get_image_payload(player) or {})

    @staticmethod
    def vars_for_template(player):
        player.task2_start_time = time.time()
        return {
            'duration_seconds': _task_duration(player),
            'block_label': 'Session 2 of 2',
        }

    @staticmethod
    def live_method(player, data):
        return _task_live_method(player, data, block=3)


class Goodbye(Page):
    pass


page_sequence = [
    Welcome,
    Instructions,
    TrainingExample,
    Task1,
    BreakChoice,
    BreakWait,
    BridgeTask,
    Task2,
    Goodbye,
]
