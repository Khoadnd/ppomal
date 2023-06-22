import os
import pathlib

import numpy as np
from malware_gym.envs.feature_extractor import pefeature
from malware_gym.envs.utils import read_file
from tqdm import tqdm
import pandas as pd


def interim(
    path, train_files, test_files, extractor, save_path="../data/interim/blackbox"
):
    print("Extracting train feature")
    for file in tqdm(train_files):
        if os.path.exists(
            os.path.join(save_path, "train", file.parent.name, file.name)
        ):
            continue
        temp = extractor.extract(read_file(file))
        if temp is None:
            continue

        with open(
            os.path.join(save_path, "train", file.parent.name, file.name), "w"
        ) as f:
            f.write(",".join([str(x) for x in temp]))

    print("Extracting test feature")
    for file in tqdm(test_files):
        if os.path.exists(os.path.join(save_path, "test", file.parent.name, file.name)):
            continue
        temp = extractor.extract(read_file(file))
        if temp is None:
            continue

        with open(
            os.path.join(save_path, "test", file.parent.name, file.name), "w"
        ) as f:
            f.write(",".join([str(x) for x in temp]))

    pass


def validate(train_files, test_files, interim_path="../data/interim/blackbox"):
    print("Validating feature")
    train_count = 0
    test_count = 0
    for file in tqdm(train_files):
        with open(
            os.path.join(interim_path, "train", file.parent.name, file.name), "r"
        ) as f:
            data = f.read().split(",")

        if len(data) != 2350:
            train_count += 1

    for file in tqdm(test_files):
        with open(
            os.path.join(interim_path, "test", file.parent.name, file.name), "r"
        ) as f:
            data = f.read().split(",")

        if len(data) != 2350:
            test_count += 1

    if test_count != 0 and train_count != 0:
        print("Validation failed")
        print(f"Train: {train_count}")
        print(f"Test: {test_count}")
        exit(1)

    print("Validation passed")

    pass


def process(
    train_files,
    test_files,
    interim_path="../data/interim/blackbox",
    processed_path="../data/processed/blackbox",
):
    with open(os.path.join(processed_path, "train.csv"), "w") as train_csv:
        for file in tqdm(train_files):
            with open(
                os.path.join(interim_path, "train", file.parent.name, file.name), "r"
            ) as f:
                data = f.read()

            train_csv.write(data + "," + file.parent.name + "\n")

    with open(os.path.join(processed_path, "test.csv"), "w") as test_csv:
        for file in tqdm(test_files):
            with open(
                os.path.join(interim_path, "test", file.parent.name, file.name), "r"
            ) as f:
                data = f.read()

            test_csv.write(data + "," + file.parent.name + "\n")

    pass


def main():
    raw_data_path = "../data/raw/blackbox"
    train_files = [
        sample
        for sample in pathlib.Path(os.path.join(raw_data_path, "train")).glob("**/*")
        if sample.is_file()
    ]
    test_files = [
        sample
        for sample in pathlib.Path(os.path.join(raw_data_path, "test")).glob("**/*")
        if sample.is_file()
    ]

    feature_extractor = pefeature.PEFeatureExtractor2()

    interim(raw_data_path, train_files, test_files, feature_extractor)
    validate(train_files, test_files)
    process(train_files, test_files)
    pass


if __name__ == "__main__":
    main()
