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
5. Check val_auc in the output.
6. If improved: keep the change and run: git add model.py && git commit -m "feat: <description>"

7. If worse: mark the result as discard and revert: git checkout model.py
8. If the run crashes: log the crash reason and revert.
9. Repeat from step 1.

## Keep / Discard / Crash Rule:
Baseline run: status = baseline
Improved validation AUC: status = keep
Lower or equal validation AUC: status = discard
Runtime error or invalid model: status = crash

## Ideas to explore
- LogisticRegression with class weighting
- Ridge-style regularization through LogisticRegression C
- RandomForestClassifier
- GradientBoostingClassifier
- HistGradientBoostingClassifier
- Feature scaling: StandardScaler, RobustScaler
- Imputation strategies for missing values
- Simple feature engineering inside Pipeline
- Hyperparameter tuning within model.py

## What NOT to do
- Do not modify prepare.py.
- Do not modify run.py.
- Do not modify the train/validation/test split.
- Do not evaluate on the test set during dry runs.
- Do not add new files unless explicitly asked.
- Do not add new dependencies.
- Do not hard-code validation labels, validation predictions, or dataset-specific outputs.
- Do not change the function signature of build_model()