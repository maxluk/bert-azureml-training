import argparse
import os

print("In train.py: as a data scientist, this is where you should fill in your training code.")

parser = argparse.ArgumentParser("train")

parser.add_argument("--input_data", type=str, help="input data")
parser.add_argument("--model_dir", type=str, help="model directory")

args = parser.parse_args()

print(f"Argument 1: {args.input_data}")
print(f"Argument 2: {args.model_dir}")

if not (args.model_dir is None):
	os.makedirs(args.model_dir, exist_ok=True)
	print(f"{args.model_dir} created")
