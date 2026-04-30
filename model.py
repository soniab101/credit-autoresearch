"""
EDITABLE -- The agent may modify this file.
Define the model pipeline for credit default prediction.

The function build_model() must return an sklearn-compatible estimator
that can be fit on X_train, y_train and evaluated using validation AUC.
"""

from sklearn.ensemble import HistGradientBoostingClassifier


def build_model():
    """Return an sklearn-compatible model."""
    return HistGradientBoostingClassifier(
        learning_rate=0.05,
        max_iter=200,
        max_leaf_nodes=15,
        l2_regularization=0.1,
        random_state=42
    )
