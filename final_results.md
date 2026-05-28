# Final Results

## Final Candidate Method

The final retained model is a median-imputed HistGradientBoostingClassifier pipeline:

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

| Model              |              Evaluation |  ROC AUC |
| ------------------ | ----------------------: | -------: |
| Logistic baseline  |          5-fold CV mean | 0.790524 |
| Final HGB pipeline |          5-fold CV mean | 0.865310 |
| Final HGB pipeline | locked validation split | 0.870970 |
| Final HGB pipeline |         locked test set | 0.871004 |

| Model              | Fold AUCs                                        | Mean AUC |  Std AUC |
| ------------------ | ------------------------------------------------ | -------: | -------: |
| Logistic baseline  | 0.788839, 0.794961, 0.787630, 0.785874, 0.795313 | 0.790524 | 0.003885 |
| Final HGB pipeline | 0.864182, 0.864288, 0.869611, 0.859331, 0.869136 | 0.865310 | 0.003774 |
