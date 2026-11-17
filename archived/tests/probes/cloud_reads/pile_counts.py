#!/usr/bin/env python3
"""How many towns the peeling reduction leaves to check, for n streets with threshold L.

Usage:  python3 pile_counts.py [n L] ...     (default: n = 5..12 with Tan-Teh's values 36, 46, 56 and the predicted 68..110)

A town at level m is n street lengths, each in [L, 2m + L - 2], summing to m^2 (sorted). Subtracting L from each length
turns these into partitions of m^2 - nL into at most n parts, each at most 2m - 2, counted by the recurrence
R(k, b, r) = R(k, b - 1, r) + R(k - 1, b, r - b). For n = 8, L = 68 it gives the table of the note (64,787,844 towns on
levels 24..32), the same counts as the q-binomial generating function (DLMF 26.9).
"""
import sys
from functools import lru_cache
sys.setrecursionlimit(100000)

def level_count(n, L, m):
    b, r = 2 * m - 2, m * m - n * L
    if r < 0: return 0
    @lru_cache(None)
    def R(k, bb, rr):
        if rr == 0: return 1
        if k == 0 or bb == 0 or rr < 0: return 0
        return R(k, bb - 1, rr) + (R(k - 1, bb, rr - bb) if rr >= bb else 0)
    return R(n, b, r)

def pile(n, L):
    out, m = {}, 1
    while m * m <= n * (2 * m + L - 2) or not out:   # beyond this the levels are empty
        c = level_count(n, L, m)
        if c: out[m] = c
        m += 1
    return out

if __name__ == '__main__':
    a = [int(x) for x in sys.argv[1:]]
    cases = list(zip(a[::2], a[1::2])) or [(5, 36), (6, 46), (7, 56), (8, 68), (9, 78), (10, 88), (11, 98), (12, 110)]
    for n, L in cases:
        p = pile(n, L)
        print(f"n={n} L={L}: levels {min(p)}..{max(p)}, towns {sum(p.values()):,}")
