# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area            | A question it could answer                                    |
| --------------- | ------------------------------------------------------------- |
| False positives | How often may a human's writing get called AI?                |
| Score spread    | How far apart should clearly-AI and clearly-human text score? |
| Label coverage  | Is every one of your three labels actually reachable?         |
| The appeal path | Does an appeal always change status and always get recorded?  |
| Bad input       | What happens when `text` is missing, empty, or enormous?      |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

# Acceptance Criteria — Provenance Guard

### 1. False Positives

**Target:** Of 100 human-written samples, no more than 1 may be labeled high-confidence AI.

**Reason:** False positives can seriously damage a writer's credibility and reputation. I believe protecting genuine human writers from false accusations is more important than detecting every AI-generated text. Therefore, my goal is to avoid any high-confidence AI classifications for human-written samples in this test set.

### 2. Score Spread

**Target:** The average AI-likelihood score of 20 AI-generated samples must exceed the average score of 20 human-written samples by at least 0.20.

**Reason:** The system should demonstrate a measurable difference between human-written and AI-generated text. I chose a minimum difference of 0.20 because I want the combined signals to provide meaningful separation rather than producing nearly identical scores for both groups.

### 3. Label Coverage

**Target:** All three labels and their exact boundary values must be tested successfully.

**Reason:** The system should not force every piece of writing into either human or AI classification. The unsure label is especially important because both detection signals have limitations. Testing all three labels and their boundaries ensures that uncertain cases can be handled appropriately.

### 4. Appeal Path

**Target:** At least 100% of 20 valid appeals must update the status to `under_review` and create an audit record.

**Reason:** Writers should always have a reliable way to challenge incorrect classifications. Since the detection system cannot guarantee perfect accuracy, every valid appeal must be recorded and acknowledged. I chose 100% because losing an appeal could prevent a falsely accused writer from receiving a review.

### 5. Bad Input

**Target:** Missing or empty text, and text longer than 20,000 characters, must return HTTP 400 in all tested cases.

**Reason:** Input validation is necessary to prevent invalid requests from reaching the detection pipeline. I chose a 20,000-character limit to establish a clear maximum input size and reduce unnecessary processing of excessively long submissions. Invalid input should receive a predictable error response rather than causing the service to fail.
---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
