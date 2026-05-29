import os
from datasets import load_dataset

print("1. Loading raw dataset...")
raw_dataset = load_dataset("yairschiff/qm9", split="train")

print("2. Splitting into Train (80%), Val (10%), and Test (10%)...")
# Split 1: Train and a temporary test/val block
train_valtest = raw_dataset.train_test_split(test_size=0.2, seed=42)
# Split 2: Divide that 20% right down the middle
val_test = train_valtest["test"].train_test_split(test_size=0.5, seed=42)

# Define our explicit splits
train_data = train_valtest["train"]
val_data = val_test["train"]
test_data = val_test["test"]

print("3. Saving to explicit folders...")
# This forces them into clear, separated directories
train_data.save_to_disk("./qm9_split_train")
val_data.save_to_disk("./qm9_split_val")
test_data.save_to_disk("./qm9_split_test")

print("\nDone! Run 'ls' in your terminal now.")