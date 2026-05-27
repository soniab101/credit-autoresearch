| Model                       | Purpose                       | Validation AUC |
| --------------------------- | ----------------------------- | -------------: |
| Initial Logistic Regression | early exploratory baseline    |         0.6833 |
| Stable Logistic Baseline    | frozen reproducible benchmark |         0.7913 |


| Model              | Mean CV AUC |    Std |
| ------------------ | ----------: | -----: |
| Logistic baseline  |      0.7905 | 0.0039 |
| Final HGB pipeline |      0.8653 | 0.0038 |
