#!/usr/bin/env python3
"""separator_q01_margins.py (Local, Block 7, S-04): the BWH horizons M(n, c) read through the death-time dictionary of
Rule30SeparatorQ01 (bwh_iff_deathBounds): M(n, 2) = max over starts of exact width 2n + 2 of death/2 - 1 - n, and M(n, 3)
the same over exact width 2n + 3 with the top two cells black. BWH at n says M(n, c) <= n + 1. Exhaustive, n = 5 to 9."""
def F(y): return (y >> 1) ^ (y | (y << 1))
def death(y):
    t = 0
    while y & 1:
        y = F(F(y)); t += 2
    return t
def M(n, c):
    W = 2 * n + 2 if c == 2 else 2 * n + 3
    lo = (1 << (W - 1)) | ((1 << (W - 2)) if c == 3 else 0)
    hi = 1 << W
    step_ok = (lambda y: True) if c == 3 else (lambda y: True)
    best = -1
    for y in range(lo | 1, hi, 2):
        if c == 3 and not (y >> (W - 2)) & 1: continue
        d = death(y)
        if d > best: best = d
    return best // 2 - 1 - n
for n in range(5, 10):
    print(n, M(n, 2), M(n, 3))
