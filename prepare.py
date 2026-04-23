print("hi")
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def load_data():
    df = pd.read_csv("data/cs-training.csv")
    df = df.dropna()

    X = df.drop("SeriousDlqin2yrs", axis=1)
    y = df["SeriousDlqin2yrs"]

    # deterministic split
    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=0.15, random_state=42, stratify=y
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=0.176, random_state=42, stratify=y_temp
    )

    return X_train, X_val, X_test, y_train, y_val, y_test