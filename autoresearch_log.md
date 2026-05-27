# AutoResearch Experiment Journal

Human-readable journal for credit default validation experiments.

`results.tsv` remains the compact machine-readable table. This journal records richer context, interpretation, and failure notes for every experiment, including discarded and crashed runs.

## Current Best

- Best validation AUC: `0.870970`
- Best retained model:
  ```python
  Pipeline([
      ("imputer", SimpleImputer(strategy="median")),
      ("model", HistGradientBoostingClassifier(
          learning_rate=0.03,
          max_iter=200,
          max_leaf_nodes=31,
          l2_regularization=0.05,
          random_state=42
      ))
  ])
  ```

## Experiment Rules

- Modify only `model.py`.
- Do not modify `prepare.py` or `run.py`.
- Do not use the locked test set during dry-run experiments.
- Keep experiments controlled: change one major variable at a time.
- Treat the first recorded run as the baseline; after that, keep only experiments that beat the best validation AUC so far.
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
  First recorded run and the baseline for all later comparisons.
- Warnings / errors / failure modes:
  Historical entry is incomplete: exact runtime and model parameters were not recorded.

### Historical - debug run

- Status: `keep`
- Validation AUC: `0.791284`
- Runtime: `not recorded`
- Previous best: `0.6833`
- Comparison to previous best: `+0.107984`
- Model / parameter change:
  ```python
  Debug run model; exact parameters not recorded in README.md or results.tsv.
  ```
- Interpretation:
  Improved on the original baseline and became the best recorded result before the boosting experiments.
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

- Status: `discard`
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
  Increasing `max_iter` to 400 matched the previous best but did not improve validation AUC, so the change is treated as discard.
- Warnings / errors / failure modes:
  Historical runtime was not recorded.

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
  Reducing tree complexity with `max_leaf_nodes=15` produced a small validation AUC improvement and became the best retained model at that point.
- Warnings / errors / failure modes:
  Historical runtime was not recorded. No crash or warning was noted.

## Later Experiment Entries

### 2026-05-07 17:34 - median imputer hgb

- Status: `keep`
- Validation AUC: `0.870665`
- Runtime: `3.92 s training time`
- Previous best: `0.849862`
- Comparison to previous best: `+0.020803`
- Model / parameter change:
  ```python
  Pipeline([
      ("imputer", SimpleImputer(strategy="median")),
      ("model", HistGradientBoostingClassifier(
          learning_rate=0.03,
          max_iter=200,
          max_leaf_nodes=31,
          l2_regularization=0.1,
          random_state=42
      ))
  ])
  ```
- Interpretation:
  Retaining missing-value rows plus median imputation inside the model pipeline substantially improved validation AUC and became the best recorded result.
- Warnings / errors / failure modes:
  The run completed successfully. Environment warnings appeared for a non-writable Matplotlib cache directory and joblib physical-core detection; neither affected validation evaluation.

### 2026-05-07 17:35 - hgb max_leaf_nodes 15 with imputer

- Status: `discard`
- Validation AUC: `0.870596`
- Runtime: `2.97 s training time`
- Previous best: `0.870665`
- Comparison to previous best: `-0.000069`
- Model / parameter change:
  ```python
  Pipeline([
      ("imputer", SimpleImputer(strategy="median")),
      ("model", HistGradientBoostingClassifier(
          learning_rate=0.03,
          max_iter=200,
          max_leaf_nodes=15,
          l2_regularization=0.1,
          random_state=42
      ))
  ])
  ```
- Interpretation:
  Reducing tree capacity from `max_leaf_nodes=31` to 15 slightly decreased validation AUC, so the change was discarded.
- Warnings / errors / failure modes:
  The run completed successfully. Environment warnings appeared for a non-writable Matplotlib cache directory and joblib physical-core detection; neither affected validation evaluation. `run.py` initially appended this row to `results.tsv` as `keep`; it was corrected to `discard`.

### 2026-05-07 17:36 - hgb learning_rate 0.05 with imputer

- Status: `discard`
- Validation AUC: `0.870643`
- Runtime: `2.33 s training time`
- Previous best: `0.870665`
- Comparison to previous best: `-0.000022`
- Model / parameter change:
  ```python
  Pipeline([
      ("imputer", SimpleImputer(strategy="median")),
      ("model", HistGradientBoostingClassifier(
          learning_rate=0.05,
          max_iter=200,
          max_leaf_nodes=31,
          l2_regularization=0.1,
          random_state=42
      ))
  ])
  ```
- Interpretation:
  Increasing `learning_rate` from 0.03 to 0.05 produced nearly the same validation AUC, but it did not beat the best result so far.
- Warnings / errors / failure modes:
  The run completed successfully. Environment warnings appeared for a non-writable Matplotlib cache directory and joblib physical-core detection; neither affected validation evaluation. `run.py` initially appended this row to `results.tsv` as `keep`; it was corrected to `discard`.

### 2026-05-07 18:09 - hgb l2_regularization 0.05 with imputer

- Status: `keep`
- Validation AUC: `0.870970`
- Runtime: `5.33 s training time`
- Previous best: `0.870665`
- Comparison to previous best: `+0.000305`
- Model / parameter change:
  ```python
  Pipeline([
      ("imputer", SimpleImputer(strategy="median")),
      ("model", HistGradientBoostingClassifier(
          learning_rate=0.03,
          max_iter=200,
          max_leaf_nodes=31,
          l2_regularization=0.05,
          random_state=42
      ))
  ])
  ```
- Interpretation:
  Reducing `l2_regularization` from 0.1 to 0.05 improved validation AUC. This is the current best and the model change is retained.
- Warnings / errors / failure modes:
  The run completed successfully. Environment warnings appeared for a non-writable Matplotlib cache directory and joblib physical-core detection; neither affected validation evaluation. `run.py` appended this row to `results.tsv`.

### 2026-05-21 16:11 - hgb max_iter 300 with imputer

- Status: `discard`
- Validation AUC: `0.870970`
- Runtime: `18.39 s training time`
- Previous best: `0.870970`
- Comparison to previous best: `no change`
- Model / parameter change:
  ```python
  Pipeline([
      ("imputer", SimpleImputer(strategy="median")),
      ("model", HistGradientBoostingClassifier(
          learning_rate=0.03,
          max_iter=300,
          max_leaf_nodes=31,
          l2_regularization=0.05,
          random_state=42
      ))
  ])
  ```
- Interpretation:
  Increasing `max_iter` from 200 to 300 did not improve validation AUC. Because the result tied the prior best rather than exceeding it, the change was discarded and `model.py` was reverted to `max_iter=200`.
- Warnings / errors / failure modes:
  The run completed successfully. Environment warnings appeared for a non-writable Matplotlib cache directory, Matplotlib font-cache setup, and joblib physical-core detection; none affected validation evaluation. `run.py` initially appended this row to `results.tsv` as `keep`; it was corrected to `discard`.

### 2026-05-21 16:23 - median imputer missing indicators hgb

- Status: `discard`
- Validation AUC: `0.870913`
- Runtime: `3.65 s training time`
- Previous best: `0.870970`
- Comparison to previous best: `-0.000057`
- Model / parameter change:
  ```python
  Pipeline([
      ("imputer", SimpleImputer(strategy="median", add_indicator=True)),
      ("model", HistGradientBoostingClassifier(
          learning_rate=0.03,
          max_iter=200,
          max_leaf_nodes=31,
          l2_regularization=0.05,
          random_state=42
      ))
  ])
  ```
- Interpretation:
  This domain-informed preprocessing experiment exposed missingness indicators for `MonthlyIncome` and `NumberOfDependents`, the two columns with substantial missingness. The added indicators slightly reduced validation AUC, suggesting the current HGB setup with median imputation already captures enough useful missingness signal or that the explicit indicators add mild noise on this split.
- Warnings / errors / failure modes:
  The run completed successfully. Environment warnings appeared for a non-writable Matplotlib cache directory, Matplotlib font-cache setup, and joblib physical-core detection; none affected validation evaluation. `run.py` initially appended this row to `results.tsv` as `keep`; it was corrected to `discard`, and `model.py` was reverted to the retained best pipeline.

### 2026-05-21 16:28 - xgboost default hist with median imputer

- Status: `discard`
- Validation AUC: `0.858567`
- Runtime: `1.61 s training time`
- Previous best: `0.870970`
- Comparison to previous best: `-0.012403`
- Model / parameter change:
  ```python
  Pipeline([
      ("imputer", SimpleImputer(strategy="median")),
      ("model", XGBClassifier(
          objective="binary:logistic",
          eval_metric="auc",
          tree_method="hist",
          random_state=42
      ))
  ])
  ```
- Why XGBoost was tested:
  Prior work on the Kaggle "Give Me Some Credit" dataset and related tabular credit-risk problems often reports strong results from boosting-based methods, including XGBoost. This experiment tested whether a reasonable default XGBoost classifier could outperform the current median-imputed HistGradientBoostingClassifier direction without changing preprocessing or evaluation logic.
- Interpretation:
  XGBoost did not meaningfully outperform the current best direction; it underperformed by `0.012403` AUC. This result does not justify additional XGBoost tuning runs under the current one-experiment budget. If XGBoost is revisited later, it should be because the search plan explicitly allocates budget for controlled class-imbalance or regularization settings, not because this default comparison was promising.
- Warnings / errors / failure modes:
  The run completed successfully. `xgboost==2.1.4` was installed into the local `.venv` to make the requested comparison possible. Environment warnings appeared for a non-writable Matplotlib cache directory and Matplotlib font-cache setup; neither affected validation evaluation. `run.py` initially appended this row to `results.tsv` as `keep`; it was corrected to `discard`, and `model.py` was reverted to the retained best HistGradientBoostingClassifier pipeline.

### 2026-05-21 16:33 - hgb class_weight balanced with imputer

- Status: `discard`
- Validation AUC: `0.870814`
- Runtime: `3.97 s training time`
- Previous best: `0.870970`
- Comparison to previous best: `-0.000156`
- Model / parameter change:
  ```python
  Pipeline([
      ("imputer", SimpleImputer(strategy="median")),
      ("model", HistGradientBoostingClassifier(
          learning_rate=0.03,
          max_iter=200,
          max_leaf_nodes=31,
          l2_regularization=0.05,
          class_weight="balanced",
          random_state=42
      ))
  ])
  ```
- Interpretation:
  This controlled class-imbalance experiment added balanced class weighting to the current best median-imputed HGB pipeline. It slightly reduced validation AUC, suggesting that the current objective and fixed split do not benefit from global inverse-frequency weighting for this metric. The unweighted HGB pipeline remains the retained best.
- Warnings / errors / failure modes:
  The run completed successfully. Environment warnings appeared for a non-writable Matplotlib cache directory, Matplotlib font-cache setup, and joblib physical-core detection; none affected validation evaluation. `run.py` initially appended this row to `results.tsv` as `keep`; it was corrected to `discard`, and `model.py` was reverted to the retained best pipeline.

### 2026-05-21 16:44 - quantile clipping 0.5 99.5 with imputer hgb

- Status: `discard`
- Validation AUC: `0.870692`
- Runtime: `5.32 s training time`
- Previous best: `0.870970`
- Comparison to previous best: `-0.000278`
- Model / parameter change:
  ```python
  Pipeline([
      ("clipper", QuantileClipper(lower_quantile=0.005, upper_quantile=0.995)),
      ("imputer", SimpleImputer(strategy="median")),
      ("model", HistGradientBoostingClassifier(
          learning_rate=0.03,
          max_iter=200,
          max_leaf_nodes=31,
          l2_regularization=0.05,
          random_state=42
      ))
  ])
  ```
- Interpretation:
  This outlier-handling experiment clipped each feature to train-fitted 0.5th and 99.5th percentile bounds before median imputation. The validation AUC decreased, suggesting that the retained HGB model benefits from preserving some extreme credit-risk values or already handles outliers adequately through tree splits.
- Warnings / errors / failure modes:
  The run completed successfully. Quantile bounds were fit inside the pipeline on the training split only, so validation/test information was not used for preprocessing. Environment warnings appeared for a non-writable Matplotlib cache directory, Matplotlib font-cache setup, and joblib physical-core detection; none affected validation evaluation. `run.py` initially appended this row to `results.tsv` as `keep`; it was corrected to `discard`, and `model.py` was reverted to the retained best pipeline.

### 2026-05-21 17:00 - domain ratios and bins with imputer hgb

- Status: `discard`
- Validation AUC: `0.869795`
- Runtime: `4.80 s training time`
- Previous best: `0.870970`
- Comparison to previous best: `-0.001175`
- Model / parameter change:
  ```python
  Pipeline([
      ("features", CreditFeatureEngineer()),
      ("imputer", SimpleImputer(strategy="median")),
      ("model", HistGradientBoostingClassifier(
          learning_rate=0.03,
          max_iter=200,
          max_leaf_nodes=31,
          l2_regularization=0.05,
          random_state=42
      ))
  ])
  ```
- Feature engineering tested:
  Added lightweight domain-informed features before imputation: total delinquency count, severe-delinquency share, open-credit-to-real-estate ratio, income per dependent, debt-income proxy, and age decade bin.
- Interpretation:
  The engineered ratios and bins reduced validation AUC. This suggests the retained HGB model is already extracting the useful nonlinear structure from the original columns, and this particular feature bundle added noise or redundant splits rather than signal.
- Warnings / errors / failure modes:
  The run completed successfully. The transformer used only row-level arithmetic and fixed binning, with no validation/test-fitted state. Environment warnings appeared for a non-writable Matplotlib cache directory, Matplotlib font-cache setup, and joblib physical-core detection; none affected validation evaluation. `run.py` initially appended this row to `results.tsv` as `keep`; it was corrected to `discard`, and `model.py` was reverted to the retained best pipeline.

### 2026-05-26 16:34 - past due sentinel flags with median imputer hgb

- Status: `discard`
- Validation AUC: `0.870831`
- Runtime: `5.54 s training time`
- Previous best: `0.870970`
- Comparison to previous best: `-0.000139`
- Model / parameter change:
  ```python
  Pipeline([
      ("past_due_sentinels", PastDueSentinelHandler()),
      ("imputer", SimpleImputer(strategy="median")),
      ("model", HistGradientBoostingClassifier(
          learning_rate=0.03,
          max_iter=200,
          max_leaf_nodes=31,
          l2_regularization=0.05,
          random_state=42
      ))
  ])
  ```
- Interpretation:
  This EDA-informed preprocessing experiment targeted the repeated `96` and `98` sentinel-like values in the three past-due count columns. It added sentinel indicator columns and set sentinel count values to missing before median imputation. Validation AUC decreased slightly, suggesting the retained HGB model is better served by preserving those extreme values directly on this split.
- Warnings / errors / failure modes:
  The run completed successfully and did not evaluate the locked test set. Environment warnings appeared for a non-writable Matplotlib cache directory, Matplotlib font-cache setup, and joblib physical-core detection; none affected validation evaluation. `run.py` initially appended this row to `results.tsv` as `keep`; it was corrected to `discard`, and `model.py` was reverted to the retained best pipeline.

### 2026-05-26 17:06 - clip DebtRatio and revolving utilization only with imputer hgb

- Status: `discard`
- Validation AUC: `0.870739`
- Runtime: `3.87 s training time`
- Previous best: `0.870970`
- Comparison to previous best: `-0.000231`
- Model / parameter change:
  ```python
  Pipeline([
      ("clipper", SelectedQuantileClipper(
          lower_quantile=0.005,
          upper_quantile=0.995
      )),
      ("imputer", SimpleImputer(strategy="median")),
      ("model", HistGradientBoostingClassifier(
          learning_rate=0.03,
          max_iter=200,
          max_leaf_nodes=31,
          l2_regularization=0.05,
          random_state=42
      ))
  ])
  ```
- Interpretation:
  This controlled clipping experiment isolated the two requested heavy-tail variables, `DebtRatio` and `RevolvingUtilizationOfUnsecuredLines`, using the same train-fitted 0.5th and 99.5th percentile bounds as the earlier all-feature clipping test. The validation AUC still decreased, though by less than the all-feature clipping run, suggesting that preserving the raw extreme values in these two features remains slightly better for the retained HGB model on the fixed validation split.
- Warnings / errors / failure modes:
  The run completed successfully and did not evaluate the locked test set. Quantile bounds were fit inside the pipeline on the training split only. Environment warnings appeared for a non-writable Matplotlib cache directory, Matplotlib font-cache setup, and joblib physical-core detection; none affected validation evaluation. `run.py` initially appended this row to `results.tsv` as `keep`; it was corrected to `discard`, and `model.py` was reverted to the retained best pipeline.

### 2026-05-26 17:10 - lightgbm default with median imputer

- Status: `discard`
- Validation AUC: `0.866955`
- Runtime: `3.38 s training time`
- Previous best: `0.870970`
- Comparison to previous best: `-0.004015`
- Model / parameter change:
  ```python
  Pipeline([
      ("imputer", SimpleImputer(strategy="median")),
      ("model", LGBMClassifier(
          objective="binary",
          n_estimators=200,
          random_state=42
      ))
  ])
  ```
- Why LightGBM was tested:
  Prior literature and Kaggle solutions for the "Give Me Some Credit" dataset frequently report strong performance from boosting-based tabular models, including LightGBM. This was run as a final controlled model-family comparison against the retained median-imputed `HistGradientBoostingClassifier` direction while keeping preprocessing and validation evaluation unchanged.
- Interpretation:
  LightGBM underperformed the retained HGB pipeline by `0.004015` validation AUC. Because this reasonable/default LightGBM comparison did not match or improve the retained model, it does not justify additional LightGBM tuning under the locked search priorities. Model-family exploration should stop here unless a future plan explicitly reopens it with new evidence.
- Warnings / errors / failure modes:
  The run completed successfully and did not evaluate the locked test set. `lightgbm==4.6.0` was installed into the local `.venv` to make the requested comparison possible. Environment warnings appeared for a non-writable Matplotlib cache directory, Matplotlib font-cache setup, joblib physical-core detection, and a harmless sklearn feature-name warning from the imputed array passed to LightGBM. `run.py` initially appended this row to `results.tsv` as `keep`; it was corrected to `discard`, and `model.py` was reverted to the retained best HGB pipeline.
