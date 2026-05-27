import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score

from prepare import load_data


RANDOM_SEED = 42


def build_final_model():
    return Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("model", HistGradientBoostingClassifier(
            learning_rate=0.03,
            max_iter=200,
            max_leaf_nodes=31,
            l2_regularization=0.05,
            random_state=RANDOM_SEED
        ))
    ])


def main():
    # load frozen split
    X_train, y_train, X_val, y_val, X_test, y_test, feature_names = load_data()

    # combine train + validation for final training
    X_final_train = pd.concat([X_train, X_val], axis=0)
    y_final_train = pd.concat([y_train, y_val], axis=0)

    print(f"Final training rows: {len(X_final_train)}")
    print(f"Locked test rows: {len(X_test)}")

    model = build_final_model()

    print("\nTraining final locked pipeline...")
    model.fit(X_final_train, y_final_train)

    print("Evaluating on LOCKED TEST SET...")

    y_score = model.predict_proba(X_test)[:, 1]

    test_auc = roc_auc_score(y_test, y_score)

    print("\n==============================")
    print(f"FINAL TEST ROC AUC: {test_auc:.6f}")
    print("==============================")


if __name__ == "__main__":
    main()