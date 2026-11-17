#!/usr/bin/env python3
"""crystal_shadow.py TABLE T: the crystal's shadow on the centre (inquisition round 14, fourth block; Cloud, CL694). c(t) = D_t(t)
is the birth value of wheel t; C_t its eventual cycle from the certificate table (F's). Agreement P(c(t) = C_t(t mod p)) over
400 <= t < K, and the same for the cells at lab x = -2..3 at time t (wheels t + x). Prediction (tracker): 1/2 +- 0.02."""
import sys, numpy as np
table, T = sys.argv[1], int(sys.argv[2])
C = [tuple(int(ch) for ch in l.strip()) for l in open(table) if l and not l.startswith('#')]
K = len(C); T = min(T, K + 8)
MASK = (1 << (T + 80)) - 1
def stp(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
rows = []; V = 1
for t in range(T + 1): rows.append(V); V = stp(V)
def bit(t, k): return (rows[t] >> k) & 1 if 0 <= k else 0
def period(c):
    for p in (1, 2, 4, 8, 16):
        if all(c[i] == c[(i + p) % 16] for i in range(16)): return p
for x in (-2, -1, 0, 1, 2, 3):
    agree = n = 0
    for t in range(400, K - 4):
        k = t + x
        if k < 0 or k >= K: continue
        c = C[k]; n += 1; agree += int(bit(t, k) == c[t % 16])
    print(f"lab x = {x:2d} (wheel t + x at time t): P(cell = its wheel's eventual cycle value) = {agree / n:.4f} over {n} times (binomial se {0.5 / n ** 0.5:.4f})")
# the defect's lifetime: time from the parents' settling to the wheel's own, from the writing-law data if present
print("CRYSTAL_SHADOW_DONE")
