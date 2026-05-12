"""
FROZEN -- Do not modify this file.
Data loading, train/val split, evaluation metric, and plotting
"""

import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

# ── Constants ──────────────────────────────────────────────
RANDOM_SEED = 42
VAL_FRACTION = 0.2
RESULTS_FILE = "results.tsv"


def load_data():
    df = pd.read_csv("data/cs-training.csv")
     # Drop unnamed ID column if present
    unnamed_cols = [col for col in df.columns if "Unnamed" in col]
    if unnamed_cols:
        df = df.drop(columns=unnamed_cols)

    print(df.shape)
    print(df.isnull().sum())
    print(df["SeriousDlqin2yrs"].value_counts(normalize=True))

    # v2 loop, commented out df.dropna()
    #df = df.dropna()

    X = df.drop("SeriousDlqin2yrs", axis=1)
    y = df["SeriousDlqin2yrs"]

    # deterministic split
    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=0.15, random_state=RANDOM_SEED, stratify=y
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=0.2, random_state=RANDOM_SEED, stratify=y_temp
    )

    feature_names = list(X.columns)

    return X_train, y_train, X_val, y_val, X_test, y_test, feature_names

def evaluate(model, X_val, y_val):
    if hasattr(model, "predict_proba"):
        y_score = model.predict_proba(X_val)[:, 1]
    else:
        y_score = model.decision_function(X_val)

    val_auc = float(roc_auc_score(y_val, y_score))
    return val_auc

def log_result(experiment_id, val_auc, status, description):
    file_exists = os.path.exists(RESULTS_FILE)

    with open(RESULTS_FILE, "a", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        if not file_exists:
            writer.writerow(["experiment", "val_auc", "status", "description"])
        writer.writerow([experiment_id, f"{val_auc:.6f}", status, description])

def plot_results(save_path="performance.png"):
    if not os.path.exists(RESULTS_FILE):
        print("No results.tsv found. Run experiments first.")
        return

    experiments, aucs, statuses, descriptions = [], [], [], []

    with open(RESULTS_FILE) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            experiments.append(row["experiment"])
            aucs.append(float(row["val_auc"]))
            statuses.append(row["status"])
            descriptions.append(row["description"])

    color_map = {
        "baseline": "#3498db",
        "keep": "#2ecc71",
        "discard": "#e74c3c"
    }
    colors = [color_map.get(s, "#95a5a6") for s in statuses]

    plt.figure(figsize=(11, 5))
    plt.scatter(range(len(aucs)), aucs, c=colors, s=80)
    plt.plot(range(len(aucs)), aucs, "k--", alpha=0.3)

    best_so_far = []
    current_best = -float("inf")
    for auc in aucs:
        current_best = max(current_best, auc)
        best_so_far.append(current_best)

    plt.plot(range(len(aucs)), best_so_far, linewidth=2.5, label="Best so far")

    short_labels = [d[:22] + ".." if len(d) > 24 else d for d in descriptions]
    plt.xticks(range(len(aucs)), short_labels, rotation=45, ha="right", fontsize=8)

    plt.ylabel("Validation AUC (higher is better)")
    plt.title("AutoResearch: Credit Default Prediction")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    print(f"Saved {save_path}")


if __name__ == "__main__":
    plot_results()