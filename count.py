#!/usr/bin/env python

import itertools

hat = [
    "blue",
    "blue",
    "blue",
    "green",
    "green",
    "green",
    "green",
    "green",
    "green",
    "red",
    "red",
]

combos = list(itertools.combinations(hat, 4))
good = 0

for combo in combos:
    if (combo.count("blue") >= 2) and (combo.count("green") >= 1):
        good += 1

print(f"g: {good} b: {len(combos) - good} n: {len(combos)} p: {good/len(combos)}")
