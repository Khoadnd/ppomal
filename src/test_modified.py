import pathlib
import pickle
from malware_gym.envs.feature_extractor import pefeature
from malware_gym.envs.utils import read_file, predict

modified_sample_path = "../data/evaded/modified"
modified_samples = [
    sample for sample in pathlib.Path(modified_sample_path).glob("**/*")
]
original_sample_path = "../data/evaded/original"
original_samples = [
    sample for sample in pathlib.Path(original_sample_path).glob("**/*")
]

blackbox = pickle.load(open("../models/blackbox.pkl", "rb"))
feature_extractor = pefeature.PEFeatureExtractor2()

print("-" * 20)
print("Modifed: ")
for file in modified_samples:
    sample = read_file(file)
    print(predict(sample), end="\t")
print("\n")
print("-" * 20)
print("Original: ")
for file in original_samples:
    sample = read_file(file)
    print(predict(sample), end="\t")
