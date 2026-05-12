"""
Create a simple validation AUC over experiment-run plot.

Usage:
    .venv/bin/python plots.py
    .venv/bin/python plots.py results.tsv auc_over_time.png
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt


DEFAULT_RESULTS_FILE = "results.tsv"
DEFAULT_OUTPUT_FILE = "auc_over_time.png"


def parse_float(value: str) -> float | None:
    """Return a float from a TSV cell, ignoring trailing comments if present."""
    token = value.split("#", 1)[0].strip().split()
    if not token:
        return None

    try:
        return float(token[0])
    except ValueError:
        return None


def load_auc_values(path: Path) -> list[float]:
    """Load validation AUC values from results.tsv in experiment order."""
    if not path.exists():
        raise FileNotFoundError(f"Results file not found: {path}")

    aucs = []
    with path.open(newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        for line_number, row in enumerate(reader, start=1):
            if not row:
                continue

            # Supports both normal rows like:
            #   <experiment> <val_auc> <status> <description>
            # and the older irregular row:
            #   baseline <description> <val_auc> # old
            auc = next((value for cell in row if (value := parse_float(cell)) is not None), None)
            if auc is None:
                raise ValueError(f"No numeric AUC found on line {line_number}: {row}")

            aucs.append(auc)

    if not aucs:
        raise ValueError(f"No experiment AUC values found in {path}")

    return aucs


def plot_auc_over_time(aucs: list[float], output_path: Path) -> None:
    runs = list(range(1, len(aucs) + 1))

    plt.figure(figsize=(9, 5))
    plt.plot(runs, aucs, marker="o", linewidth=1.8)
    plt.xlabel("Experiment Run Number")
    plt.ylabel("Validation AUC")
    plt.title("Validation AUC Over Experiment Runs")
    plt.xticks(runs)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close()


def main() -> None:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(DEFAULT_RESULTS_FILE)
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(DEFAULT_OUTPUT_FILE)

    aucs = load_auc_values(input_path)
    plot_auc_over_time(aucs, output_path)
    print(f"Saved {output_path} from {input_path} ({len(aucs)} experiments)")


if __name__ == "__main__":
    main()
