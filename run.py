from prepare import load_data
from model import build_model, train_model
from sklearn.metrics import roc_auc_score
import time


start = time.time()


# load data
X_train, X_val, X_test, y_train, y_val, y_test = load_data()


# build model
model = build_model()


# train
model = train_model(model, X_train, y_train)


# evaluate
preds = model.predict_proba(X_val)[:, 1]
auc = roc_auc_score(y_val, preds)


print(f"Validation AUC: {auc:.4f}")


# runtime
end = time.time()
print(f"Runtime: {end - start:.2f} seconds")


# log result
with open("results.tsv", "a") as f:
   f.write(f"baseline\tlogreg\t{auc:.4f}\n")



