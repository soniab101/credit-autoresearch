import numpy as np
import pandas as pd

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


RANDOM_SEED = 42
TARGET = "SeriousDlqin2yrs"


def load_full_training_data():
    df = pd.read_csv("data/cs-training.csv")

    unnamed_cols = [col for col in df.columns if "Unnamed" in col]
    if unnamed_cols:
        df = df.drop(columns=unnamed_cols)

    X = df.drop(TARGET, axis=1)
    y = df[TARGET]

    return X, y


def main():
    X, y = load_full_training_data()

    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=RANDOM_SEED
    )

    models = {
        "Logistic baseline": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=RANDOM_SEED
            ))
        ]),

        "Final HGB pipeline": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("model", HistGradientBoostingClassifier(
                learning_rate=0.03,
                max_iter=200,
                max_leaf_nodes=31,
                l2_regularization=0.05,
                random_state=RANDOM_SEED
            ))
        ])
    }

    print("5-Fold Stratified Cross-Validation Stability Check")
    print("Metric: ROC AUC")
    print("-" * 60)

    for name, model in models.items():
        scores = cross_val_score(
            model,
            X,
            y,
            cv=cv,
            scoring="roc_auc",
            n_jobs=-1
        )

        print(f"\n{name}")
        print(f"Fold AUCs: {np.round(scores, 6)}")
        print(f"Mean AUC:  {scores.mean():.6f}")
        print(f"Std AUC:   {scores.std():.6f}")


if __name__ == "__main__":
    main()