# ICT304 Tutorial 3 — Group 4

ICT304 AI System Design (TSA 2026), Murdoch University.
Topics: sampling, imbalanced data, batch vs stream processing, feature importance/selection/extraction, data leakage
(lecture Topics 5 and 6).

**Due:** Week 8 tutorial session (Moodle: Friday 30 Oct 2026, 11:59 PM). Marked live by the tutor, not via upload.

## Files

| Folder | File | Purpose |
|---|---|---|
| Presentation | ICT304_Tutorial3_Group4_DRAFT.pptx | Draft slides for Q1–Q5 (to be finalised) |
| Notebook | ICT304_Tut3_Q2_Imbalanced_Abalone.ipynb | Q2: steps + code, before/after comparison |
| Datasets | abalone.data | UCI Abalone dataset (Nash et al., 1994) |
| Results | fig*.png, q2_*.csv | Charts and result tables written by the notebook |
| Scripts | make_figs.py | Q1 sampling simulation chart |
| Notes | Tutorial3_questions.md | Question summary + checklist |

## Questions

1. Types of sampling — advantages and disadvantages, with examples.
2. Abalone imbalanced data — steps and code, model performance before vs after.
3. Batch vs stream processing — examples, two ML techniques for streams.
4. 10-min presentation — feature importance vs feature selection; feature extraction approaches.
5. 5-min presentation — Kaggle data-leakage tutorial and what we learned.

## Running the Q2 notebook

1. Open this folder in VS Code.
2. Open `Notebook/ICT304_Tut3_Q2_Imbalanced_Abalone.ipynb` and pick the Python kernel
   (the unit's `.venv` in `ICT 304/` works).
3. **Run All.** The first cell installs `imbalanced-learn` if it is missing.
   Charts and CSV tables are saved to `Results/`.

Random seed = 42, so results repeat exactly.

## AI declaration

Drafted with help from Claude (Anthropic). Prompts and screenshots go on the last slide of the deck.
