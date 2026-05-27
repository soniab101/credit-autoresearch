# Training Split EDA Report: cs-training.csv

**Generated:** 2026-05-21 18:16:56

## Metadata

- **Raw file:** `data/cs-training.csv`
- **File size:** 7,564,965 bytes (7.21 MB)
- **Raw rows:** 150,000
- **Columns in raw file:** 12 including `Unnamed: 0` index column
- **Modeling rows after ID drop:** 150,000
- **Feature columns:** 10
- **Target:** `SeriousDlqin2yrs`
- **Split logic:** `test_size=0.15`, then validation fraction `0.2` of remaining rows, stratified with `random_state=42`

## File Type Details

CSV is plain text tabular data. Appropriate EDA includes row and column counts, data type inference, missing value patterns, numeric statistics, duplicate row checks, outlier detection, and correlation analysis. This report focuses on the actual training split used by `prepare.py`, because model experiments fit only that split.

## Split And Target Balance

| index | rows | positive_count | positive_rate_pct |
| --- | --- | --- | --- |
| train | 102000 | 6818 | 6.684 |
| validation | 25500 | 1704 | 6.682 |
| locked_test | 22500 | 1504 | 6.684 |
| raw_after_id_drop | 150000 | 10026 | 6.684 |

The training split preserves the raw target balance: approximately 6.684% positive delinquency cases. This is a strongly imbalanced binary classification task.

## Raw Missingness After ID Drop

| index | missing | missing_pct |
| --- | --- | --- |
| SeriousDlqin2yrs | 0 | 0 |
| RevolvingUtilizationOfUnsecuredLines | 0 | 0 |
| age | 0 | 0 |
| NumberOfTime30-59DaysPastDueNotWorse | 0 | 0 |
| DebtRatio | 0 | 0 |
| MonthlyIncome | 29731 | 19.82 |
| NumberOfOpenCreditLinesAndLoans | 0 | 0 |
| NumberOfTimes90DaysLate | 0 | 0 |
| NumberRealEstateLoansOrLines | 0 | 0 |
| NumberOfTime60-89DaysPastDueNotWorse | 0 | 0 |
| NumberOfDependents | 3924 | 2.62 |

## Training Missingness

| index | missing | missing_pct |
| --- | --- | --- |
| RevolvingUtilizationOfUnsecuredLines | 0 | 0 |
| age | 0 | 0 |
| NumberOfTime30-59DaysPastDueNotWorse | 0 | 0 |
| DebtRatio | 0 | 0 |
| MonthlyIncome | 20128 | 19.73 |
| NumberOfOpenCreditLinesAndLoans | 0 | 0 |
| NumberOfTimes90DaysLate | 0 | 0 |
| NumberRealEstateLoansOrLines | 0 | 0 |
| NumberOfTime60-89DaysPastDueNotWorse | 0 | 0 |
| NumberOfDependents | 2710 | 2.66 |

Missing values are concentrated in `MonthlyIncome` and `NumberOfDependents`. The current best model's median imputer is appropriate for keeping these rows instead of dropping roughly one fifth of the data.

### Missingness By Target In Training Split

| feature | target_0_missing_pct | target_1_missing_pct |
| --- | --- | --- |
| MonthlyIncome | 19.97 | 16.4 |
| NumberOfDependents | 2.71 | 1.91 |

## Training Summary Statistics

| index | count | mean | std | min | 1% | 5% | 25% | 50% | 75% | 95% | 99% | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RevolvingUtilizationOfUnsecuredLines | 102000.000 | 6.47632 | 275.136 | 0 | 0 | 0 | 0.0294845 | 0.153781 | 0.557823 | 1 | 1.08921 | 50708.000 |
| age | 102000.000 | 52.2843 | 14.7949 | 0 | 24 | 29 | 41 | 52 | 63 | 78 | 87 | 109 |
| NumberOfTime30-59DaysPastDueNotWorse | 102000.000 | 0.416108 | 4.13846 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 98 |
| DebtRatio | 102000.000 | 352.103 | 1980.804 | 0 | 0 | 0.00438911 | 0.175363 | 0.366069 | 0.864501 | 2439.000 | 4972.020 | 326442.000 |
| MonthlyIncome | 81872.000 | 6628.469 | 13994.017 | 0 | 0 | 1280.000 | 3400.000 | 5400.000 | 8208.000 | 14582.450 | 25000.000 | 3008750.000 |
| NumberOfOpenCreditLinesAndLoans | 102000.000 | 8.46336 | 5.15266 | 0 | 0 | 2 | 5 | 8 | 11 | 18 | 25 | 57 |
| NumberOfTimes90DaysLate | 102000.000 | 0.260304 | 4.11374 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 98 |
| NumberRealEstateLoansOrLines | 102000.000 | 1.01664 | 1.12102 | 0 | 0 | 0 | 0 | 1 | 2 | 3 | 4 | 32 |
| NumberOfTime60-89DaysPastDueNotWorse | 102000.000 | 0.235529 | 4.10042 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 98 |
| NumberOfDependents | 99290.000 | 0.756934 | 1.1138 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 4 | 20 |

## Heavy Tails And Outliers

| feature | gt_p99_count | p99 | max | max_to_p99 |
| --- | --- | --- | --- | --- |
| RevolvingUtilizationOfUnsecuredLines | 1020 | 1.08921 | 50708.000 | 46554.651 |
| DebtRatio | 1020 | 4972.020 | 326442.000 | 65.6558 |
| MonthlyIncome | 772 | 25000.000 | 3008750.000 | 120.35 |

`RevolvingUtilizationOfUnsecuredLines`, `DebtRatio`, and `MonthlyIncome` have extreme right tails. Tree-based models can often tolerate this better than linear models, but clipping or log transforms are reasonable experiments if done inside a pipeline.

## Delinquency Sentinel Values

| index | value_96_count | value_98_count |
| --- | --- | --- |
| NumberOfTime30-59DaysPastDueNotWorse | 1 | 177 |
| NumberOfTimes90DaysLate | 1 | 177 |
| NumberOfTime60-89DaysPastDueNotWorse | 1 | 177 |

The three past-due count features contain repeated high values, especially `98`, that likely encode exceptional or missing-like states rather than literal counts. Treating these consistently across related columns may be worth testing.

## Target Correlation Ranking

| index | pearson_corr_with_target |
| --- | --- |
| NumberOfTime30-59DaysPastDueNotWorse | 0.125663 |
| NumberOfTimes90DaysLate | 0.117174 |
| age | -0.112519 |
| NumberOfTime60-89DaysPastDueNotWorse | 0.102916 |
| NumberOfDependents | 0.0463098 |
| NumberOfOpenCreditLinesAndLoans | -0.0341702 |
| MonthlyIncome | -0.0186273 |
| NumberRealEstateLoansOrLines | -0.0100301 |
| DebtRatio | -0.00938614 |
| RevolvingUtilizationOfUnsecuredLines | -0.00090277 |

Simple linear correlation is limited for this nonlinear task, but the past-due count features and `age` are the strongest one-feature signals by absolute correlation.

## Median Feature Values By Target

| index | target_0_median | target_1_median | delta_1_minus_0 |
| --- | --- | --- | --- |
| RevolvingUtilizationOfUnsecuredLines | 0.132408 | 0.829758 | 0.69735 |
| age | 52 | 46 | -6 |
| NumberOfTime30-59DaysPastDueNotWorse | 0 | 0 | 0 |
| DebtRatio | 0.362409 | 0.424899 | 0.0624907 |
| MonthlyIncome | 5446.000 | 4500.000 | -946 |
| NumberOfOpenCreditLinesAndLoans | 8 | 7 | -1 |
| NumberOfTimes90DaysLate | 0 | 0 | 0 |
| NumberRealEstateLoansOrLines | 1 | 1 | 0 |
| NumberOfTime60-89DaysPastDueNotWorse | 0 | 0 | 0 |
| NumberOfDependents | 0 | 0 | 0 |

## Duplicate And Integrity Checks

- **Duplicate training rows including target:** 329
- **Constant feature columns:** none
- **Unexpected target labels:** none
- **Age minimum in training split:** 0 (`0` appears in the full dataset and may need domain-specific handling if it lands in a future split)

## Sample Raw Rows

| index | Unnamed: 0 | SeriousDlqin2yrs | RevolvingUtilizationOfUnsecuredLines | age | NumberOfTime30-59DaysPastDueNotWorse | DebtRatio | MonthlyIncome | NumberOfOpenCreditLinesAndLoans | NumberOfTimes90DaysLate | NumberRealEstateLoansOrLines | NumberOfTime60-89DaysPastDueNotWorse | NumberOfDependents |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 0.766127 | 45 | 2 | 0.802982 | 9120.000 | 13 | 0 | 6 | 0 | 2 |
| 1 | 2 | 0 | 0.957151 | 40 | 0 | 0.121876 | 2600.000 | 4 | 0 | 0 | 0 | 1 |
| 2 | 3 | 0 | 0.65818 | 38 | 1 | 0.0851134 | 3042.000 | 2 | 1 | 0 | 0 | 0 |

## Key Findings

- The train split has 102,000 rows, 10 features, and 6,818 positive cases.
- The target is imbalanced at 6.684% positive cases, so ROC AUC is a sensible ranking metric, though PR AUC would also be useful for diagnostics.
- `MonthlyIncome` is missing for 20,128 training rows (19.73%). `NumberOfDependents` is missing for 2,710 rows (2.66%).
- Several features are highly skewed, with maxima far beyond the 99th percentile.
- The current retained median-imputation plus histogram gradient boosting approach aligns with the data shape: numeric features, missingness, nonlinear interactions, and heavy tails.

## Recommendations

- Keep imputation inside the sklearn pipeline so validation/test transformations are learned only from training data.
- Test missingness indicator features for `MonthlyIncome` and `NumberOfDependents`; missingness rates differ slightly by target.
- Consider capped versions of `RevolvingUtilizationOfUnsecuredLines`, `DebtRatio`, and `MonthlyIncome` as controlled experiments.
- Consider special handling for the `96`/`98` values in the past-due count columns, either as categorical sentinel indicators or clipped counts plus sentinel flags.
- For reporting beyond the current loop, add PR AUC and calibration diagnostics, but continue using validation ROC AUC as the optimization metric because that is the project objective.

---
*Generated with the exploratory-data-analysis workflow plus project-specific split analysis.*
