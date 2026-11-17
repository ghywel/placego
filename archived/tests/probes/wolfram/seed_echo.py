#!/usr/bin/env python3
"""Local, 2026-10-28 (L1064): the seed echo at the right edge, checked by direct simulation.

Claim (hand, Proposition 23's argument with arbitrary start bits): for a finite seed with rightmost black cell at 0,
at every time t >= 1 the cells t-1, t-2, ... just inside the black right edge copy the seed cells -1, -2, ... for
exactly B(t) - 1 cells, where B(t) = min{i >= 1 : p_i does not divide t}, and cell t - B(t) is the complement of seed
cell -B(t). (p_i: least period of right diagonal i, from the 8.27 recurrence.) Usage: seed_echo.py SEEDS T RNGSEED
"""
import sys, random
import numpy as np
NS, T, R = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
random.seed(R)
def least(a):
    while len(a) > 1 and len(a) % 2 == 0 and np.array_equal(a[:len(a)//2], a[len(a)//2:]): a = a[:len(a)//2]
    return a
def periods(seed, need):
    prev2, prev1 = np.zeros(1, np.uint8), np.ones(1, np.uint8); per = [1]
    for d in range(1, need + 1):
        q = max(len(prev1), len(prev2)); g = np.tile(prev1, q // len(prev1)) | np.tile(prev2, q // len(prev2))
        s0 = seed[d] if d < len(seed) else 0
        D = (np.concatenate(([0], np.bitwise_xor.accumulate(g)[:-1])) ^ s0).astype(np.uint8)
        if g.sum() & 1: D = np.concatenate((D, 1 - D))
        D = least(D); per.append(len(D)); prev2, prev1 = prev1, D
    return per
checks = fails = 0
for _ in range(NS):
    seed = [1] + [random.randint(0, 1) for _ in range(random.randint(0, 30))]
    per = periods(seed, 60)
    OFF = T + len(seed) + 4
    x = sum(b << (OFF - i) for i, b in enumerate(seed))
    sb = lambda i: seed[i] if i < len(seed) else 0
    for t in range(1, T + 1):
        x = (x << 1) ^ (x | (x >> 1))
        cell = lambda pos: (x >> (pos + OFF)) & 1
        B = next(i for i in range(1, len(per)) if t % per[i])
        ok = all(cell(t - i) == sb(i) for i in range(1, B)) and cell(t - B) != sb(B)
        checks += 1; fails += not ok
print(f"seeds {NS}, times 1..{T}: {checks} checks, {fails} failures")
