# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

import argparse
import os

print("In evaluate.py")
print("As a data scientist, this is where I use my evaluate code.")

parser = argparse.ArgumentParser("evaluate")
parser.add_argument("--existing_model", type=str, help="existing model")
parser.add_argument("--model_dir", type=str, help="model dir")
parser.add_argument("--evaluate_result", type=str, help="evaluate result")

args = parser.parse_args()

print("Argument 1: %s" % args.existing_model)
print("Argument 2: %s" % args.model_dir)
print("Argument 3: %s" % args.evaluate_result)

if not (args.evaluate_result is None):
    os.makedirs(args.evaluate_result, exist_ok=True)
    print("%s created" % args.evaluate_result)
