#!/usr/bin/env python

import math

# Arrays of b, g, r possibilities.
possibilities = [
    "0 4 0",
    "0 3 1",
    "0 2 2",
    "1 3 0",
    "1 2 1",
    "1 1 2",
    "2 2 0",
    "2 1 1",
    "2 0 2",
    "3 1 0",
    "3 0 1",
]

desired = [
    "2 2 0",
    "2 1 1",
    "3 1 0",
]

blues = 3
greens = 6
reds = 2

# Combinations.
good = 0
total = 0
for draw in possibilities:
    (b, g, r) = draw.split(" ")
    total += (
        math.comb(blues, int(b)) * math.comb(greens, int(g)) * math.comb(reds, int(r))
    )
for draw in desired:
    (b, g, r) = draw.split(" ")
    good += (
        math.comb(blues, int(b)) * math.comb(greens, int(g)) * math.comb(reds, int(r))
    )

print(f"g: {good} b: {total - good} n: {total} p: {good/total}")
