#!/usr/bin/env python3
"""Local, 2026-10-28 (L1064): exact right-diagonal periods of the single seed from the 8.27 recurrence, and the
plateau lengths L(v) = w(v) - w(v-1) of Proposition 23's edge-triangle widths.

D_0 = 1, D_-1 = 0, D_d(0) = 0 and D_d(t+1) = D_d(t) XOR (D_(d-1)(t) OR D_(d-2)(t)). Each D_d is built over one exact
period (doubling when the forcing's period holds an odd number of 1s) and reduced to its least dyadic period.
Prints per diagonal: d, log2 p_d, forcing parity bits. Usage: diagonal_plateaus.py [MAXLOG]   (default 22)
"""
import sys, json
import numpy as np
MAXLOG = int(sys.argv[1]) if len(sys.argv) > 1 else 22
def least(a):
    while len(a) > 1 and len(a) % 2 == 0 and np.array_equal(a[:len(a)//2], a[len(a)//2:]): a = a[:len(a)//2]
    return a
def tile(a, n): return np.tile(a, n // len(a))
prev2, prev1 = np.zeros(1, np.uint8), np.ones(1, np.uint8)   # D_-1, D_0
out = [{"d": 0, "e": 0}]
d = 0
while True:
    d += 1
    q = max(len(prev1), len(prev2))
    g = tile(prev1, q) | tile(prev2, q)
    D = np.concatenate(([0], np.bitwise_xor.accumulate(g)[:-1])).astype(np.uint8)
    odd = int(g.sum() & 1)
    if odd: D = np.concatenate((D, 1 - D))
    D = least(D)
    e = len(D).bit_length() - 1
    out.append({"d": d, "e": e, "odd": odd, "wt": int(D.sum() & 1),
                "ev": int(D[0::2].sum() & 1) if len(D) > 1 else None})
    if e > MAXLOG: break
    prev2, prev1 = prev1, D
E = [r["e"] for r in out]
Q = np.maximum.accumulate(E)
w = {}
for v in range(1, MAXLOG + 1):
    w[v] = next(j for j in range(len(Q)) if Q[j] > v) - 1
L = {v: w[v] - w[v-1] for v in range(2, MAXLOG + 1)}
x = "".join(str(int(Q[j] > Q[j-1])) for j in range(1, len(Q)))
print("periods log2:", E)
print("w(v):", [w[v] for v in range(1, MAXLOG + 1)])
print("plateau L(v):", [L[v] for v in range(2, MAXLOG + 1)])
print("increment word:", x)
json.dump({"e": E, "w": w, "x": x, "rows": out}, open(sys.argv[2], "w")) if len(sys.argv) > 2 else None
