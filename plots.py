"""
Create a presentation-ready validation AUC over experiment-run plot.

Usage:
    .venv/bin/python plots.py
    .venv/bin/python plots.py results.tsv auc_over_time_annotated.png
"""

from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt


DEFAULT_RESULTS_FILE = "results.tsv"
DEFAULT_OUTPUT_FILE = "auc_over_time_annotated.png"
DEFAULT_DATA_FILE = "data/cs-training.csv"
DEFAULT_CLASS_IMBALANCE_FILE = "class_imbalance.png"
TARGET_COLUMN = "SeriousDlqin2yrs"


@dataclass(frozen=True)
class Experiment:
    auc: float
    status: str
    description: str


def parse_float(value: str) -> float | None:
    """Return a float from a TSV cell, ignoring trailing comments if present."""
    token = value.split("#", 1)[0].strip().split()
    if not token:
        return None

    try:
        return float(token[0])
    except ValueError:
        return None


def load_experiments(path: Path) -> list[Experiment]:
    """Load validation experiments from results.tsv in experiment order."""
    if not path.exists():
        raise FileNotFoundError(f"Results file not found: {path}")

    experiments = []
    with path.open(newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        for line_number, row in enumerate(reader, start=1):
            if not row:
                continue

            # Supports normal rows:
            #   <experiment> <val_auc> <status> <description>
            # and the older irregular baseline row:
            #   baseline <description> <val_auc> # old
            if len(row) >= 4 and (auc := parse_float(row[1])) is not None:
                status = row[2].strip()
                description = row[3].strip()
            else:
                auc = next((value for cell in row if (value := parse_float(cell)) is not None), None)
                status = "baseline"
                description = row[1].strip() if len(row) > 1 else f"experiment {line_number}"

            if auc is None:
                raise ValueError(f"No numeric AUC found on line {line_number}: {row}")

            experiments.append(Experiment(auc=auc, status=status, description=description))

    if not experiments:
        raise ValueError(f"No experiment AUC values found in {path}")

    return experiments


def best_so_far(values: list[float]) -> list[float]:
    best_values = []
    best = -float("inf")
    for value in values:
        best = max(best, value)
        best_values.append(best)
    return best_values


def find_run(experiments: list[Experiment], description: str) -> int:
    for index, experiment in enumerate(experiments, start=1):
        if experiment.description == description:
            return index
    raise ValueError(f"Required experiment not found: {description}")


def annotate_phase(ax, run: int, auc: float, text: str, xytext: tuple[int, int]) -> None:
    ax.annotate(
        text,
        xy=(run, auc),
        xytext=xytext,
        textcoords="offset points",
        ha="center",
        va="center",
        fontsize=9,
        fontweight="bold",
        color="#202124",
        bbox={
            "boxstyle": "round,pad=0.35",
            "facecolor": "white",
            "edgecolor": "#9aa0a6",
            "linewidth": 0.8,
            "alpha": 0.95,
        },
        arrowprops={
            "arrowstyle": "->",
            "color": "#5f6368",
            "linewidth": 1.1,
            "shrinkA": 4,
            "shrinkB": 4,
        },
    )


def plot_auc_over_time(experiments: list[Experiment], output_path: Path) -> None:
    aucs = [experiment.auc for experiment in experiments]
    best_values = best_so_far(aucs)
    runs = list(range(1, len(aucs) + 1))

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(12, 6.6))

    status_colors = {
        "baseline": "#5f6368",
        "keep": "#188038",
        "discard": "#d93025",
        "crash": "#9334e6",
    }
    colors = [status_colors.get(experiment.status, "#5f6368") for experiment in experiments]

    ax.plot(
        runs,
        aucs,
        color="#1a73e8",
        linewidth=1.5,
        alpha=0.55,
        label="Validation AUC",
        zorder=2,
    )
    ax.scatter(
        runs,
        aucs,
        c=colors,
        edgecolor="white",
        linewidth=0.9,
        s=58,
        zorder=3,
    )
    ax.plot(
        runs,
        best_values,
        color="#202124",
        linewidth=2.4,
        label="Best so far",
        zorder=4,
    )

    phase_runs = {
        "stable_logistic": find_run(experiments, "debug run"),
        "hgb_jump": find_run(experiments, "hist gradient boosting"),
        "median_gain": find_run(experiments, "median imputer hgb"),
        "plateau": find_run(experiments, "hgb l2_regularization 0.05 with imputer"),
    }

    annotate_phase(
        ax,
        phase_runs["stable_logistic"],
        aucs[phase_runs["stable_logistic"] - 1],
        "Stable logistic\nbaseline",
        (20, -44),
    )
    annotate_phase(
        ax,
        phase_runs["hgb_jump"],
        aucs[phase_runs["hgb_jump"] - 1],
        "HGB jump",
        (18, 42),
    )
    annotate_phase(
        ax,
        phase_runs["median_gain"],
        aucs[phase_runs["median_gain"] - 1],
        "Median imputation\ngain",
        (10, 30),
    )
    annotate_phase(
        ax,
        phase_runs["plateau"],
        best_values[phase_runs["plateau"] - 1],
        "Late-stage\nplateau",
        (76, 26),
    )

    ax.set_title("Validation AUC Over AutoResearch Experiments", fontsize=16, pad=30)
    ax.set_xlabel("Experiment Run Number", fontsize=11)
    ax.set_ylabel("Validation ROC AUC", fontsize=11)
    ax.set_xlim(0.5, len(runs) + 0.8)
    ax.set_ylim(min(aucs) - 0.012, max(aucs) + 0.012)
    ax.set_xticks(runs)
    ax.tick_params(axis="x", labelsize=8)
    ax.tick_params(axis="y", labelsize=9)
    ax.grid(True, axis="y", alpha=0.28)
    ax.grid(False, axis="x")

    legend_handles = [
        plt.Line2D([0], [0], color="#1a73e8", linewidth=1.5, alpha=0.65, label="Validation AUC"),
        plt.Line2D([0], [0], color="#202124", linewidth=2.4, label="Best so far"),
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#188038", markersize=8, label="Kept"),
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#d93025", markersize=8, label="Discarded"),
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#5f6368", markersize=8, label="Baseline"),
    ]
    ax.legend(handles=legend_handles, loc="lower right", frameon=True, framealpha=0.95)

    plt.tight_layout()
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close()


def load_class_counts(path: Path) -> dict[int, int]:
    """Load target-class counts from the raw training CSV."""
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    counts = {0: 0, 1: 0}
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        if TARGET_COLUMN not in reader.fieldnames:
            raise ValueError(f"Target column not found in {path}: {TARGET_COLUMN}")

        for row in reader:
            label = int(row[TARGET_COLUMN])
            counts[label] = counts.get(label, 0) + 1

    return counts


def plot_class_imbalance(counts: dict[int, int], output_path: Path) -> None:
    labels = ["No serious delinquency", "Serious delinquency"]
    values = [counts.get(0, 0), counts.get(1, 0)]
    total = sum(values)
    percentages = [(value / total) * 100 for value in values]

    fig, ax = plt.subplots(figsize=(7.5, 5))
    bars = ax.bar(labels, values, color=["#1a73e8", "#d93025"], width=0.55)

    for bar, value, percentage in zip(bars, values, percentages):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{value:,}\n{percentage:.2f}%",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    ax.set_title("Class Imbalance in Credit Default Dataset", fontsize=14, pad=14)
    ax.set_ylabel("Rows")
    ax.set_xlabel("Target class")
    ax.set_ylim(0, max(values) * 1.14)
    ax.grid(True, axis="y", alpha=0.25)
    ax.grid(False, axis="x")
    plt.tight_layout()
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close()


def main() -> None:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(DEFAULT_RESULTS_FILE)
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(DEFAULT_OUTPUT_FILE)
    class_imbalance_path = (
        Path(sys.argv[3]) if len(sys.argv) > 3 else Path(DEFAULT_CLASS_IMBALANCE_FILE)
    )

    experiments = load_experiments(input_path)
    plot_auc_over_time(experiments, output_path)
    print(f"Saved {output_path} from {input_path} ({len(experiments)} experiments)")

    class_counts = load_class_counts(Path(DEFAULT_DATA_FILE))
    plot_class_imbalance(class_counts, class_imbalance_path)
    print(f"Saved {class_imbalance_path} from {DEFAULT_DATA_FILE}")


if __name__ == "__main__":
    main()
