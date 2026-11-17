#!/usr/bin/env python3
"""Local, 2026-10-28 (L1066): literal-rule check of a pair-graph witness seed.

Evolves the finite seed with the literal Rule 30 update new(i) = old(i-1) XOR (old(i) OR old(i+1)) on big integers,
reads right diagonal d as D_d(t) = x_t(t - d), and reports each diagonal's least dyadic period (tested over 4 * PMAX
ticks after the first 2 * PMAX, which covers two full periods of any period <= 2 * PMAX).
Usage: plateau_witness_check.py SEED_BITS_FROM_EDGE PMAX DMAX
"""
import sys
bits, PMAX, DMAX = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
T = 8 * PMAX + DMAX; OFF = T + len(bits) + 4
x = sum(int(b) << (OFF - i) for i, b in enumerate(bits))
rows = []
for t in range(T + 1): rows.append(x); x = (x << 1) ^ (x | (x >> 1))
D = lambda d, t: (rows[t] >> (t - d + OFF)) & 1
def per(d):
    p = 1
    while p <= 2 * PMAX:
        if all(D(d, t) == D(d, t + p) for t in range(0, T - p - 0)) : return p
        p *= 2
    return None
ps = [per(d) for d in range(DMAX + 1)]
j = next(d for d, p in enumerate(ps) if p and p > 2)
first_big = next((d for d, p in enumerate(ps) if p is None or p > PMAX), None)
print("periods:", ps)
print(f"first period > 2 at d = {j}; first period > {PMAX} at d = {first_big}; stretch from j: {first_big - j} diagonals")
print("monotone:", all((ps[i] or 10**9) >= (ps[i-1] or 0) for i in range(1, len(ps)) if ps[i-1]))
