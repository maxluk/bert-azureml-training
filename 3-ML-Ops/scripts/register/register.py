# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

import argparse
import os

print("In register.py")
print("As a data scientist, this is where I register my model.")

parser = argparse.ArgumentParser("register")
parser.add_argument("--eval_result", type=str, help="model result")

args = parser.parse_args()

print("Argument 1: %s" % args.eval_result)
