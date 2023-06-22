import os
import pickle
import pandas as pd

with open("../models/blackbox.pkl", "rb") as f:
    model = pickle.load(f)

data_path = "../data/processed/blackbox"
test_csv = os.path.join(data_path, "test.csv")
test_df = pd.read_csv(test_csv, header=None)

sample = test_df.sample(1)

pred = model.predict(sample.iloc[:, :-1])[0]
actual = sample.iloc[:, -1].values[0]

print(
    pred,
    "should be",
    actual,
)

print(pred == actual)
