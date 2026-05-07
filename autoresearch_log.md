# AutoResearch Experiment Journal

Human-readable journal for credit default validation experiments.

`results.tsv` remains the compact machine-readable table. This journal records richer context, interpretation, and failure notes for every experiment, including discarded and crashed runs.

## Current Best

- Best validation AUC: `0.849862`
- Best retained model: `HistGradientBoostingClassifier(learning_rate=0.05, max_iter=200, max_leaf_nodes=15, l2_regularization=0.1, random_state=42)`

## Experiment Rules

- Modify only `model.py`.
- Do not modify `prepare.py` or `run.py`.
- Do not use the locked test set during dry-run experiments.
- Keep experiments controlled: change one major variable at a time.
- Log every experiment: baseline, keep, discard, and crash.
- Training plus validation evaluation must complete in under 60 seconds on CPU.

## Experiment Entries

### Historical - logreg

- Status: `baseline`
- Validation AUC: `0.6833`
- Runtime: `not recorded`
- Previous best: `none recorded`
- Comparison to previous best: `not applicable`
- Model / parameter change:
  ```python
  Logistic regression experiment; exact parameters not recorded in current project files.
  ```
- Interpretation:
  Older pre-baseline result. It is present in `results.tsv`, but `README.md` notes that it is not used as the established baseline.
- Warnings / errors / failure modes:
  Historical entry is incomplete: exact runtime and model parameters were not recorded.

### Historical - debug run

- Status: `baseline`
- Validation AUC: `0.791284`
- Runtime: `not recorded`
- Previous best: `none established`
- Comparison to previous best: `established baseline`
- Model / parameter change:
  ```python
  Baseline model used for the debug run; exact parameters not recorded in README.md or results.tsv.
  ```
- Interpretation:
  Established the controlled validation baseline before the boosting experiments.
- Warnings / errors / failure modes:
  Historical runtime and exact model parameters were not recorded.

### Historical - hist gradient boosting

- Status: `keep`
- Validation AUC: `0.848813`
- Runtime: `not recorded`
- Previous best: `0.791284`
- Comparison to previous best: `+0.057529`
- Model / parameter change:
  ```python
  HistGradientBoostingClassifier(
      learning_rate=0.05,
      max_iter=200,
      l2_regularization=0.1,
      random_state=42
  )
  ```
- Interpretation:
  Switching from the baseline approach to histogram gradient boosting produced a large validation AUC improvement.
- Warnings / errors / failure modes:
  Historical runtime was not recorded. No crash or warning was noted.

### 2026-05-07 17:02 - hgb max_leaf_nodes 10

- Status: `discard`
- Validation AUC: `0.849096`
- Runtime: `2.82 s training time`
- Previous best: `0.849862`
- Comparison to previous best: `-0.000766`
- Model / parameter change:
  ```python
  HistGradientBoostingClassifier(
      learning_rate=0.05,
      max_iter=200,
      max_leaf_nodes=10,
      l2_regularization=0.1,
      random_state=42
  )
  ```
- Interpretation:
  Reducing `max_leaf_nodes` from 15 to 10 made the trees more constrained, but validation AUC decreased. This suggests the current retained `max_leaf_nodes=15` setting preserves useful split complexity that is lost at 10.
- Warnings / errors / failure modes:
  The run completed successfully. Environment warnings appeared for a non-writable Matplotlib cache directory and joblib physical-core detection; neither affected validation evaluation. The result was initially appended by `run.py` as `keep` and was corrected to `discard` because it did not beat the previous best.

### 2026-05-07 17:04 - hgb l2_regularization 0.2

- Status: `discard`
- Validation AUC: `0.849466`
- Runtime: `1.83 s training time`
- Previous best: `0.849862`
- Comparison to previous best: `-0.000396`
- Model / parameter change:
  ```python
  HistGradientBoostingClassifier(
      learning_rate=0.05,
      max_iter=200,
      max_leaf_nodes=15,
      l2_regularization=0.2,
      random_state=42
  )
  ```
- Interpretation:
  Increasing L2 regularization from 0.1 to 0.2 reduced validation AUC. Together with the 0.05 result, this supports keeping `l2_regularization=0.1` for now.
- Warnings / errors / failure modes:
  The run completed successfully. Environment warnings appeared for a non-writable Matplotlib cache directory and joblib physical-core detection; neither affected validation evaluation. The result was initially appended by `run.py` as `keep` and was corrected to `discard` because it did not beat the previous best.

### 2026-05-07 17:03 - hgb l2_regularization 0.05

- Status: `discard`
- Validation AUC: `0.849262`
- Runtime: `2.22 s training time`
- Previous best: `0.849862`
- Comparison to previous best: `-0.000600`
- Model / parameter change:
  ```python
  HistGradientBoostingClassifier(
      learning_rate=0.05,
      max_iter=200,
      max_leaf_nodes=15,
      l2_regularization=0.05,
      random_state=42
  )
  ```
- Interpretation:
  Lowering L2 regularization from 0.1 to 0.05 reduced validation AUC. The current model appears to benefit from the stronger regularization already retained.
- Warnings / errors / failure modes:
  The run completed successfully. Environment warnings appeared for a non-writable Matplotlib cache directory and joblib physical-core detection; neither affected validation evaluation. The result was initially appended by `run.py` as `keep` and was corrected to `discard` because it did not beat the previous best.

### 2026-05-07 17:03 - hgb max_leaf_nodes 20

- Status: `discard`
- Validation AUC: `0.848987`
- Runtime: `2.51 s training time`
- Previous best: `0.849862`
- Comparison to previous best: `-0.000875`
- Model / parameter change:
  ```python
  HistGradientBoostingClassifier(
      learning_rate=0.05,
      max_iter=200,
      max_leaf_nodes=20,
      l2_regularization=0.1,
      random_state=42
  )
  ```
- Interpretation:
  Increasing `max_leaf_nodes` from 15 to 20 reduced validation AUC, so additional leaf capacity appears to overfit or otherwise weaken generalization on the fixed validation split.
- Warnings / errors / failure modes:
  The run completed successfully. Environment warnings appeared for a non-writable Matplotlib cache directory and joblib physical-core detection; neither affected validation evaluation. The result was initially appended by `run.py` as `keep` and was corrected to `discard` because it did not beat the previous best.

### Historical - hgb max_iter 400

- Status: `keep` in `results.tsv`; not retained according to `README.md`
- Validation AUC: `0.848813`
- Runtime: `not recorded`
- Previous best: `0.848813`
- Comparison to previous best: `no change`
- Model / parameter change:
  ```python
  HistGradientBoostingClassifier(
      learning_rate=0.05,
      max_iter=400,
      l2_regularization=0.1,
      random_state=42
  )
  ```
- Interpretation:
  Increasing `max_iter` to 400 matched the previous best but did not improve validation AUC. Because it changed a single major parameter and produced no gain, the README says the change was not retained.
- Warnings / errors / failure modes:
  Historical runtime was not recorded. The status in `results.tsv` is `keep`, but the README clarifies that the model change was not retained because it did not improve.

### Historical - hgb max_leaf_nodes 15

- Status: `keep`
- Validation AUC: `0.849862`
- Runtime: `not recorded`
- Previous best: `0.848813`
- Comparison to previous best: `+0.001049`
- Model / parameter change:
  ```python
  HistGradientBoostingClassifier(
      learning_rate=0.05,
      max_iter=200,
      max_leaf_nodes=15,
      l2_regularization=0.1,
      random_state=42
  )
  ```
- Interpretation:
  Reducing tree complexity with `max_leaf_nodes=15` produced a small validation AUC improvement and became the current retained model.
- Warnings / errors / failure modes:
  Historical runtime was not recorded. No crash or warning was noted.
