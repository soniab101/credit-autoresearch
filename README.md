# Credit Default AutoResearch

This project runs controlled experiments for a credit default prediction task.
The target is `SeriousDlqin2yrs`, where `1` means a borrower became seriously
delinquent within two years.

## Evaluation

The objective is to maximize validation ROC AUC. Higher is better.

The validation split is fixed in `prepare.py`, and dry-run experiments evaluate
only on the validation set. The locked test set is loaded but not evaluated
during these experiments.

## Experiment Rules

- Only `model.py` is editable during model experiments.
- `prepare.py` and `run.py` are frozen.
- `build_model()` must return an sklearn-compatible estimator.
- Training and validation evaluation must complete in under 60 seconds on CPU.
- No external data sources, downloads, new dependencies, or test-set evaluation
  are used during autoresearch loops.

## Current Best Model

The best retained model is a `HistGradientBoostingClassifier`:

```python
HistGradientBoostingClassifier(
    learning_rate=0.05,
    max_iter=200,
    max_leaf_nodes=15,
    l2_regularization=0.1,
    random_state=42
)
```

Current best validation AUC:

```text
0.849862
```

## Experiment Results

| Description | Status | Validation AUC | Notes |
| --- | --- | ---: | --- |
| `debug run` | baseline | 0.791284 | Established baseline before boosting experiments. |
| `hist gradient boosting` | keep | 0.848813 | Large improvement over logistic-regression baseline. |
| `hgb max_iter 400` | logged keep | 0.848813 | Matched the best at the time but did not improve; change was not retained. |
| `hgb max_leaf_nodes 15` | keep | 0.849862 | Improved the best result and is the current retained model. |

An older pre-baseline result, `logreg` with AUC `0.6833`, is present in
`results.tsv` but is not used as the established baseline.

## Running an Experiment

Use the project virtual environment:

```bash
.venv/bin/python run.py "short experiment description"
```

`run.py` trains the estimator returned by `build_model()`, evaluates validation
AUC, and appends the result to `results.tsv`.
