# Credit Default AutoResearch

This project runs controlled experiments for a credit default prediction task.
The target is `SeriousDlqin2yrs`, where `1` means a borrower became seriously
delinquent within two years.

## Evaluation

The objective is to maximize validation ROC AUC. Higher is better.

The validation split is fixed in `prepare.py`, and dry-run experiments evaluate
only on the validation set. The locked test set is loaded but not evaluated
during these experiments.

Early experiments used complete-case analysis with rows containing missing
values dropped. Later experiments retain rows with missing values and handle
missingness inside `model.py` pipelines. Treat the missing-value/imputation
change as a documented preprocessing and feature-engineering experiment rather
than a directly identical evaluation setup.

## Experiment Rules

- Only `model.py` is editable during model experiments.
- `prepare.py` and `run.py` are frozen.
- `build_model()` must return an sklearn-compatible estimator.
- Training and validation evaluation must complete in under 60 seconds on CPU.
- No external data sources, downloads, new dependencies, or test-set evaluation
  are used during autoresearch loops.

## Current Best Model

The current best retained model is a pipeline with median imputation followed
by a `HistGradientBoostingClassifier`:

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

Current best validation AUC:

```text
0.870970
```

## Experiment Results

`results.tsv` is the single structured experiment log. Richer notes,
interpretation, runtime, and warning details are tracked in
`autoresearch_log.md`.

### Metric Over Time

The plot below shows validation AUC by experiment run number using the rows in
`results.tsv`.

![Validation AUC over experiment runs](auc_over_time.png)

Regenerate the plot with:

```bash
.venv/bin/python plots.py
```

### Experiments

| Description | Status | Validation AUC | Notes |
| --- | --- | ---: | --- |
| `logreg` | original baseline | 0.6833 | First recorded logistic regression result. Older run with incomplete metadata. |
| `debug run` | baseline | 0.791284 | Early baseline/debug validation run; exact model parameters are not recorded in the current files. |
| `hist gradient boosting` | keep | 0.848813 | Large improvement over logistic-regression baseline. |
| `hgb max_iter 400` | logged keep | 0.848813 | Matched the best at the time but did not improve; change was not retained. |
| `hgb max_leaf_nodes 15` | keep | 0.849862 | Improved the complete-case boosting result. |
| `hgb max_leaf_nodes 10` | discard | 0.849096 | More constrained trees underperformed the complete-case best. |
| `hgb max_leaf_nodes 20` | discard | 0.848987 | Additional leaf capacity underperformed the complete-case best. |
| `hgb l2_regularization 0.05` | discard | 0.849262 | Weaker L2 regularization underperformed the complete-case best. |
| `hgb l2_regularization 0.2` | discard | 0.849466 | Stronger L2 regularization underperformed the complete-case best. |
| `hgb learning_rate 0.03` | keep | 0.849493 | Lower learning rate experiment from the complete-case stage; did not exceed the complete-case best in the current log. |
| `v2 baseline median imputer hgb` | baseline | 0.870665 | Preprocessing/feature-engineering experiment retaining missing-value rows with median imputation inside the pipeline. |
| `v2 hgb max_leaf_nodes 15` | discard | 0.870596 | Reduced tree capacity from 31 to 15 after adding median imputation; slightly worse than the imputed-data baseline. |
| `v2 hgb learning_rate 0.05` | discard | 0.870643 | Increased learning rate from 0.03 to 0.05 after adding median imputation; nearly tied but did not improve. |
| `v2 hgb l2_regularization 0.05` | keep | 0.870970 | Reduced L2 regularization from 0.1 to 0.05 after adding median imputation; current best retained model. |

## Running an Experiment

Use the project virtual environment:

```bash
.venv/bin/python run.py "short experiment description"
```

`run.py` trains the estimator returned by `build_model()`, evaluates validation
AUC, and appends the result to `results.tsv`.

After each run, update `autoresearch_log.md` with the richer human-readable
experiment notes, including interpretation, runtime, and any warnings or
failure modes.
