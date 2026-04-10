# Experiment Text — All Participant-Facing Content
# For translation. Conditions in [brackets]. Variables in {{curly braces}}.

---

## PAGE: Field ID Entry

**Title:** Participant Check-In
**Subtitle:** Please enter the ID given to you by the research team.
**Field label:** Field ID
**Field hint:** Enter the 4-digit code from your participant card (e.g. 1011, 2154, 3023).
**Button:** Next

---

## PAGE: Informed Consent

**Title:** Informed Consent

**Purpose of the study**
We invite you to take part in a research study on decision-making and cognitive tasks. The study is conducted by researchers from the Massachusetts Institute of Technology, the University of California Berkeley, the University of Zurich. The study involves responding quickly and correctly to images on your screen. Participation is voluntary. You must be over the age of 18.

**What you will do**
[IF no_break]:
You will complete a symbol-matching task: the session lasts 90 minutes, with no break.

[IF forced_break]:
You will complete a symbol-matching task in two sessions of {{task_minutes}} minutes each, separated by a required {{break_minutes}}-minute break.

[IF choice]:
You will complete a symbol-matching task in two sessions of {{task_minutes}} minutes each, with an optional {{break_minutes}}-minute break in between.

[ALL CONDITIONS]:
During a given round, you will see a target symbol and must select all matching symbols from a grid of 100.

**Payment**
You will receive a participation payment of Ksh 350 for completing the full study. We also cover your transport for Ksh 200. In addition, you could earn additional bonus payments based on task accuracy and speed. In total, you can expect to earn around Ksh 600–700. You can earn Shillings for every correct task. Your total earnings will be paid via MPesa. We will calculate earnings immediately, but it may take a day or two for the payments to arrive because of administrative reasons.

**Risks and benefits**
There are no known risks beyond those of everyday computer use. There is no direct personal benefit beyond the payment described above, but your responses will contribute to scientific research.

**Confidentiality**
Identifying information will be kept strictly confidential and will not be shared outside the research team. All data are stored securely and will only be reported in anonymized, aggregated form. Your name will never be linked to your responses in any publication. Your participant ID (not your name) will be used to identify your data.

**Voluntary participation**
Participation is entirely voluntary. You may stop at any time without penalty, though you will only receive the full payment if you complete the study. If you have questions, please ask the research team before proceeding.

**Checkbox label:** I have read and understood the information above and I agree to participate.
**Button:** Next

---

## PAGE: Welcome

**Title:** Welcome to your work task!

Next we will explain your work task to you. Then you will have an opportunity to try it. Then we will explain how you will get paid.

**Your work today will have the following structure:**

[IF no_break]:
You will work on this task for 90 minutes without a break.

[IF forced_break]:
You will work on this task for {{task_minutes}} minutes. Then you will take a short {{break_minutes}} minute break. Then you will work for another {{task_minutes}} minutes.

[IF choice]:
You will work on this task for {{task_minutes}} minutes. Then you can choose if you would like to take a break or keep working for {{break_minutes}} minutes. Then you will work for another {{task_minutes}} minutes.

**Button:** Next

---

## PAGE: Tutorial (MatrixInstructions) — 7 steps

**Title:** Tutorial

**Study structure reminder (top of page):**
[IF no_break]: Study structure: 90 minutes of work without a break
[IF forced_break]: Study structure: {{task_minutes}} min work → {{break_minutes}} min break → {{task_minutes}} min work
[IF choice]: Study structure: {{task_minutes}} min work → choice to take a {{break_minutes}} min break or to keep working during that time → {{task_minutes}} min work

**Step 0 — What you will do**
Banner: 📋 What you will do
- You will see a large grid.
- Your job is to find a specific symbol in each grid, and tap on it as quickly and accurately as possible.
- We will now walk through the steps and task together.
- Your payment for the task will depend on speed and accuracy.
Button: Next →

**Step 1 — Target symbol**
Banner: 👁 Highlighted in blue, just below, is the symbol you need to find in the grid. Click on NEXT to continue with the instructions.
Prompt: Find this symbol in the grid:
Button: Next →

**Step 2 — Select a symbol**
Banner: 👆 Look for this symbol in the grid. For simplicity, we have highlighted it in orange. Select it by tapping on the screen.
Button: ✓ Confirm Selection (disabled until selected)

**Step 3 — Deselect a symbol**
Banner: 👆 Great job! What if you selected the wrong symbol by mistake? Tap on it again to remove it. Give it a try below.

**Step 4 — Find all matching symbols**
Banner: ✋ Now find ALL matching symbols and select them in the grid below by tapping on them. To make it simple, they are highlighted in orange for this demonstration.

**Step 5 — Confirm your selection**
Banner: ✅ When you are working on this task, the page will NOT change automatically. Once you believe you have selected all symbols, you will need to hit CONFIRM at the bottom. Tap on Confirm Selection now.

**Step 6 — Free practice round**
Banner: 🎯 Now try a full round by yourself: find and tap on all matching symbols. Then tap on Confirm Selection once you are done.
Button: ✓ Confirm Selection

---

## PAGE: Payment Info (PaymentInfo)

**Title:** How you will get paid

- 💰 You will receive a fixed participation payment of Ksh 350 if you complete the entire task until the end.
- ✅ You can earn bonus payments that will depend on your speed and accuracy. For each correctly completed grid, you can earn Ksh 1.
- 📱 Your earnings will be paid via M-PESA.
- 🕐 Payments will arrive within the next 2 days.
- 💼 We will tell you about possibilities of being rehired on the next page.

**Button:** Next →

---

## PAGE: Future Work (FutureWork)

**Title:** Possibilities for future work

[IF treat]:
👔 Some workers will be selected by a hiring manager, who is also present today, to be invited back for a separate session tomorrow.

[IF no_treat]:
📋 Some workers will be selected to be invited back for a separate session tomorrow.

[ALL CONDITIONS]:
- 💬 The future task tomorrow will be different from today, easier and more fun.
- ⏱ The future task will take at most 30 minutes.
- 💰 Workers selected can earn Ksh 350 for that short 30-minute session.

**Button:** Next →

---

## PAGE: Ready to Begin (MatrixStartScreen)

**Title:** Ready? Let's review and then begin!

- ⏱ You will now do the task for {{task_minutes}} minutes.
- 💰 The more tasks you finish correctly, the higher your payoff.
- ➡️ Don't forget to hit Confirm Selection to keep moving from grid to grid.
- 🔇 No feedback is given after each grid — do your best, and move on. Remember that speed and accuracy matter.

[IF no_break]:
➡️ After {{task_minutes}} minutes you will continue working for {{break_minutes}} more minute(s), then do the final {{task_minutes}}-minute session.

[IF forced_break]:
☕ After {{task_minutes}} minutes you will take a required {{break_minutes}}-minute break before the final session.

[IF choice]:
☕ After {{task_minutes}} minutes you can choose to take a {{break_minutes}}-minute break or continue working.

**Button:** ▶ Start task

---

## PAGE: Task Screen (MatrixTask) — shown during all work segments

**Timer label (session 1):** Session 1 of 2
**Timer label (bridge):** Continue working
**Timer label (session 2):** Session 2 of 2
**Task prompt:** Find all matching symbols in the grid:
**Button:** ✓ Confirm Selection

---

## PAGE: Break Choice (BreakChoice) — choice condition only

**Title:** End of Session 1

**Heading:** Session 1 complete!
You have completed the first part of your work session. Please choose what you would like to happen next.
Please note that which option you choose will be shared with the hiring manager in charge of deciding who is invited back for another task.

**Card 1 — Take a break:**
😴 Take a 10-minute break
The screen will lock for {{break_minutes}} min and you won't be able to work and earn money during this time. You can use this time to get up and rest and relax in the break room.

**Card 2 — Keep working:**
💪 Work an extra 10 minutes
You will keep working and earning money during the {{break_minutes}} min. You will not have a break during the work period.

**Button:** Confirm my choice →

---

## PAGE: Break Wait (BreakWait) — when break is taken

**Title:** Break in Progress
**Card header:** Break in progress — Work task is locked
**Timer label:** Time remaining in break
**Message:** You are now in your 10-minute break. You may get up and go to the break room to rest and recharge during this time. Do make sure you return on time as the next session will start automatically.

---

## PAGE: Demographics Survey

**Title:** Almost done — a few quick questions
**Subtitle:** These questions take about 5 minutes. Your answers are kept strictly confidential.

**Question 1:** What is your age (in years)? [18–50]
**Question 2:** What is your gender? [Male / Female / Non-binary / gender diverse / Prefer not to say]
**Question 3:** What is the highest level of education you have completed?
  - No formal education
  - Some primary school (not completed)
  - Primary school completed (Standard 8 / KCPE)
  - Some secondary school (not completed)
  - Secondary school completed (Form 4 / KCSE)
  - Post-secondary certificate or diploma (TVET / college)
  - University degree (Bachelor's or equivalent)
  - Postgraduate degree (Master's or PhD)
  - Prefer not to say

**Question 4:** What is your current main occupation?
  - Farmer / agricultural worker
  - Casual / manual labourer
  - Trader / market vendor / petty business
  - Artisan / skilled tradesperson (e.g. mechanic, tailor, carpenter)
  - Teacher / education professional
  - Healthcare worker
  - Domestic worker
  - Professional / office worker
  - Student
  - Unemployed / not currently working
  - Other

**Question 4b (shown if "Other" selected):** Please describe your occupation: [free text]

**Question 5:** In your usual work, do you choose freely when to take a break, or is it fixed?
  - I can always choose freely when to take a break
  - I can usually choose, but with some restrictions
  - My break times are mostly set by my work or employer
  - My break times are always fixed — I have no choice
  - Not applicable / I do not currently work

**Question 6:** Do you have a salaried job or do you do casual work?
  - Salaried / permanent employee
  - Casual / day labourer
  - Self-employed / own business
  - Unpaid family worker
  - I do not currently work
  - Other

**Question 7:** What is your approximate monthly household income?
  - Less than KES 5,000
  - KES 5,000 – 14,999
  - KES 15,000 – 29,999
  - KES 30,000 – 59,999
  - KES 60,000 – 99,999
  - KES 100,000 or more
  - Prefer not to say

**Question 8:** How many hours did you sleep last night? [0–12]
**Question 9:** What did you have for breakfast today? (write "nothing" if you skipped it) [free text]

**Button:** Next

---

## PAGE: Goodbye / Payoff Summary

**Title:** Thank you for your participation!
**Message:** You have completed the task. Here is a summary of your earnings.

**Earnings table:**
| | |
|---|---|
| Participation fee | Ksh 350 |
| Transportation fee | Ksh 200 |
| Session 1 (N correct × Ksh 1) | Ksh N |
[IF no_break OR choice-kept-working]:
| Continue working (N correct × Ksh 1) | Ksh N |
[IF took break]:
| Session 2 (N correct × Ksh 1) | Ksh N |
[IF no_break OR choice-kept-working]:
| Final session (N correct × Ksh 1) | Ksh N |
| **Total earnings** | **Ksh X** |

**Task summary:** Grids attempted: N | Correct: N

**Footer:** Your responses have been recorded. Your payment will arrive within the next 2 days via M-PESA. You may now close this browser window.
