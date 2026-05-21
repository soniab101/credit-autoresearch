"""
EDITABLE -- The agent may modify this file.
Define the model pipeline for credit default prediction.

The function build_model() must return an sklearn-compatible estimator
that can be fit on X_train, y_train and evaluated using validation AUC.
"""

from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

def build_model():
    return Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("model", HistGradientBoostingClassifier(
            learning_rate=0.03,
            max_iter=200,
            max_leaf_nodes=31,
            l2_regularization=0.05,
            random_state=42
        ))
    ])
