# AutoResearch Agent Instructions

## Objective
Maximize validation AUC on the credit default prediction task.

The target is `SeriousDlqin2yrs`, where 1 indicates serious delinquency within 2 years.

## Rules
- You may ONLY modify `model.py`.
- `prepare.py` and `run.py` are FROZEN — do not touch them.
- `build_model()` must return an sklearn-compatible estimator or Pipeline.
- Training + evaluation must complete in under 60 seconds on CPU.
- No additional data sources or external downloads.
- Do not use the locked test set during dry-run experiments.
- Run at most 3 experiments before stopping for human review.
- After 3 experiments, summarize:
   - best result
   - trends observed
   - whether performance appears to plateau
   - suggested next direction

## Evaluation
- Primary metric: validation AUC.
- Higher AUC is better.
- The validation split is fixed in `prepare.py`.
- The test set is locked and should only be used once at the end for final evaluation.

## Workflow
1. Read current `model.py`.
2. Propose one modification.
3. Edit `model.py`.
4. Run:

   ```bash
   .venv/bin/python run.py "description of change"
   ```
5. Check val_auc in the output.
6. If improved: keep the change and run: git add model.py && git commit -m "feat: <description>"

7. If lower than or equal to the best prior AUC: mark the result as discard and revert: git checkout model.py
8. If the run crashes: log the crash reason and revert.
9. Repeat from step 1.

## Keep / Discard / Crash Rule:
Original run: status = baseline
Improved validation AUC versus the best prior result: status = keep
Lower or equal validation AUC versus the best prior result: status = discard
Runtime error or invalid model: status = crash

## Locked Search Priorities
Domain-Informed Search Priorities:

The project uses the Kaggle “Give Me Some Credit” dataset, a tabular binary credit-default prediction problem with substantial class imbalance and missing-value structure.

Based on prior credit-risk modeling literature and Kaggle solution patterns, the following directions are prioritized:

- Gradient-boosted tree models are prioritized over deep learning or highly complex architectures because they consistently perform strongly on structured tabular credit data.
- Missing-value handling and preprocessing are treated as high-impact variables because the dataset contains substantial missingness, especially in MonthlyIncome and NumberOfDependents.
- Controlled feature engineering and preprocessing changes are prioritized over broad architecture exploration.
- Class imbalance awareness remains important because SeriousDlqin2yrs is highly imbalanced.
- Small hyperparameter changes with repeatedly negligible gains should not dominate the remaining search budget.

Relevant findings from prior work:
- Credit-risk studies frequently report that preprocessing and feature engineering contribute substantially to AUC improvements.
- Recent tabular credit-risk work suggests that data representation and sampling strategies often matter more than architecture choice.
- Kaggle credit-scoring solutions commonly rely on boosting-based methods such as Gradient Boosting, LightGBM, or HistGradientBoosting-style approaches.


## Dropped Directions

The following directions are no longer being actively pursued:
- Deep learning architectures
- Large-scale model-family exploration
- Uncontrolled multi-variable experiments
- Extensive local hyperparameter sweeps with diminishing returns
- Expansion beyond tabular credit-risk prediction

## What NOT to do
- Do not modify prepare.py.
- Do not modify run.py.
- Do not modify the train/validation/test split.
- Do not evaluate on the test set during dry runs.
- Do not add new files unless explicitly asked.
- Do not add new dependencies.
- Do not hard-code validation labels, validation predictions, or dataset-specific outputs.
- Do not change the function signature of build_model()

## Comparison Policy
- Treat the first recorded run's AUC as the baseline.
- After the baseline, compare every experiment against the best validation AUC recorded so far.
- Keep a change only when it improves on the best prior AUC.
- Discard a change when it is lower than or equal to the best prior AUC.
