from prepare import load_data
import pandas as pd
import matplotlib.pyplot as plt

# Load split data
X_train, y_train, X_val, y_val, X_test, y_test, feature_names = load_data()

# Recombine features + target for visualization
train_df = X_train.copy()
train_df["SeriousDlqin2yrs"] = y_train

print(train_df.head())
print(train_df.describe())

# Example visualization
train_df.hist(figsize=(12, 10))
plt.tight_layout()
plt.show()