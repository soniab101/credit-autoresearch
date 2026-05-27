# Exploratory Data Analysis Report: cs-training.csv

**Generated:** 2026-05-21 18:14:30

---

## Basic Information

- **Filename:** `cs-training.csv`
- **Full Path:** `/Users/sonia/Desktop/credit-autoresearch/data/cs-training.csv`
- **File Size:** 7.21 MB (7,564,965 bytes)
- **Last Modified:** 2019-12-11T04:01:24
- **Extension:** `.csv`

## File Type

- **Category:** General Scientific
- **Description:** Comma-Separated Values

## Format Reference

### .csv - Comma-Separated Values
**Description:** Plain text tabular data
**Typical Data:** Experimental measurements, results tables
**Use Cases:** Universal data exchange, spreadsheet export
**Python Libraries:**
- `pandas`: `pd.read_csv('file.csv')`
- `csv`: Built-in module
- `polars`: High-performance CSV reading
- `numpy`: `np.loadtxt()` or `np.genfromtxt()`
**EDA Approach:**
- Row and column counts
- Data type inference
- Missing value patterns and frequency
- Column statistics (numeric: mean, std; categorical: frequencies)
- Outlier detection
- Correlation matrix
- Duplicate row detection
- Header and index validation
- Encoding issues detection



*Reference: general_scientific_formats.md*

## Data Analysis

### Summary Statistics

```json
{
  "shape": [
    10000,
    12
  ],
  "columns": [
    "Unnamed: 0",
    "SeriousDlqin2yrs",
    "RevolvingUtilizationOfUnsecuredLines",
    "age",
    "NumberOfTime30-59DaysPastDueNotWorse",
    "DebtRatio",
    "MonthlyIncome",
    "NumberOfOpenCreditLinesAndLoans",
    "NumberOfTimes90DaysLate",
    "NumberRealEstateLoansOrLines",
    "NumberOfTime60-89DaysPastDueNotWorse",
    "NumberOfDependents"
  ],
  "dtypes": {
    "Unnamed: 0": "int64",
    "SeriousDlqin2yrs": "int64",
    "RevolvingUtilizationOfUnsecuredLines": "float64",
    "age": "int64",
    "NumberOfTime30-59DaysPastDueNotWorse": "int64",
    "DebtRatio": "float64",
    "MonthlyIncome": "float64",
    "NumberOfOpenCreditLinesAndLoans": "int64",
    "NumberOfTimes90DaysLate": "int64",
    "NumberRealEstateLoansOrLines": "int64",
    "NumberOfTime60-89DaysPastDueNotWorse": "int64",
    "NumberOfDependents": "float64"
  },
  "missing_values": {
    "Unnamed: 0": 0,
    "SeriousDlqin2yrs": 0,
    "RevolvingUtilizationOfUnsecuredLines": 0,
    "age": 0,
    "NumberOfTime30-59DaysPastDueNotWorse": 0,
    "DebtRatio": 0,
    "MonthlyIncome": 1974,
    "NumberOfOpenCreditLinesAndLoans": 0,
    "NumberOfTimes90DaysLate": 0,
    "NumberRealEstateLoansOrLines": 0,
    "NumberOfTime60-89DaysPastDueNotWorse": 0,
    "NumberOfDependents": 284
  },
  "summary_statistics": {
    "Unnamed: 0": {
      "count": 10000.0,
      "mean": 5000.5,
      "std": 2886.8956799071675,
      "min": 1.0,
      "25%": 2500.75,
      "50%": 5000.5,
      "75%": 7500.25,
      "max": 10000.0
    },
    "SeriousDlqin2yrs": {
      "count": 10000.0,
      "mean": 0.064,
      "std": 0.2447651752171863,
      "min": 0.0,
      "25%": 0.0,
      "50%": 0.0,
      "75%": 0.0,
      "max": 1.0
    },
    "RevolvingUtilizationOfUnsecuredLines": {
      "count": 10000.0,
      "mean": 4.9312058070099,
      "std": 160.47967396529165,
      "min": 0.0,
      "25%": 0.031134953,
      "50%": 0.1653283055,
      "75%": 0.5717455865,
      "max": 9340.0
    },
    "age": {
      "count": 10000.0,
      "mean": 52.1642,
      "std": 14.778791548295239,
      "min": 21.0,
      "25%": 41.0,
      "50%": 52.0,
      "75%": 62.0,
      "max": 101.0
    },
    "NumberOfTime30-59DaysPastDueNotWorse": {
      "count": 10000.0,
      "mean": 0.3851,
      "std": 3.7237326177453784,
      "min": 0.0,
      "25%": 0.0,
      "50%": 0.0,
      "75%": 0.0,
      "max": 98.0
    },
    "DebtRatio": {
      "count": 10000.0,
      "mean": 350.4572484980129,
      "std": 2243.9839025032384,
      "min": 0.0,
      "25%": 0.17360532574999998,
      "50%": 0.367082637,
      "75%": 0.84725680425,
      "max": 168835.0
    },
    "MonthlyIncome": {
      "count": 8026.0,
      "mean": 6606.379142785946,
      "std": 6787.373041181549,
      "min": 0.0,
      "25%": 3400.0,
      "50%": 5400.0,
      "75%": 8200.0,
      "max": 208333.0
    },
    "NumberOfOpenCreditLinesAndLoans": {
      "count": 10000.0,
      "mean": 8.345,
      "std": 5.0673802733052735,
      "min": 0.0,
      "25%": 5.0,
      "50%": 8.0,
      "75%": 11.0,
      "max": 46.0
    },
    "NumberOfTimes90DaysLate": {
      "count": 10000.0,
      "mean": 0.2315,
      "std": 3.691540396237011,
      "min": 0.0,
      "25%": 0.0,
      "50%": 0.0,
      "75%": 0.0,
      "max": 98.0
    },
    "NumberRealEstateLoansOrLines": {
      "count": 10000.0,
      "mean": 1.008,
      "std": 1.0844600524503132,
      "min": 0.0,
      "25%": 0.0,
      "50%": 1.0,
      "75%": 2.0,
      "max": 17.0
    },
    "NumberOfTime60-89DaysPastDueNotWorse": {
      "count": 10000.0,
      "mean": 0.2022,
      "std": 3.675985098806123,
      "min": 0.0,
      "25%": 0.0,
      "50%": 0.0,
      "75%": 0.0,
      "max": 98.0
    },
    "NumberOfDependents": {
      "count": 9716.0,
      "mean": 0.7488678468505557,
      "std": 1.1267229636338114,
      "min": 0.0,
      "25%": 0.0,
      "50%": 0.0,
      "75%": 1.0,
      "max": 20.0
    }
  }
}
```

## Recommendations for Further Analysis

Based on the file type (`.csv`), consider the following analyses:

- Statistical distribution analysis
- Missing value imputation strategies
- Correlation analysis between variables
- Outlier detection and handling
- Dimensionality reduction (PCA, t-SNE)

---
*This report was generated by the exploratory-data-analysis skill.*