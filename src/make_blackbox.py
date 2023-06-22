import os

from sklearn.ensemble import RandomForestClassifier as RFC
import pandas as pd
import pickle


def main():
    data_path = "../data/processed/blackbox"
    train_csv = os.path.join(data_path, "train.csv")
    test_csv = os.path.join(data_path, "test.csv")

    train_df = pd.read_csv(train_csv, header=None)
    test_df = pd.read_csv(test_csv, header=None)

    clf = RFC(n_jobs=-1)

    clf.fit(train_df.iloc[:, :-1], train_df.iloc[:, -1])
    print(clf.score(test_df.iloc[:, :-1], test_df.iloc[:, -1]))
    with open("../models/blackbox.pkl", "wb") as f:
        pickle.dump(clf, f)

    del clf

    with open("../models/blackbox.pkl", "rb") as f:
        clf = pickle.load(f)

    print(clf.score(test_df.iloc[:, :-1], test_df.iloc[:, -1]))

    pass


if __name__ == "__main__":
    main()
