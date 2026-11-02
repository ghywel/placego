#!/usr/bin/env python3
"""long_zero.py T: the classic ether's (8,8) front law to time T at four alignments (G26: run well beyond the first window)."""
import sys, numpy as np
T = int(sys.argv[1]); y = np.array([1,0,0,1,0,0,0,0,0], dtype=np.uint8); N = 9
def cst(s): return s ^ (np.roll(s, 1) | np.roll(s, 2))
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y): orb.append(cur.copy()); cur = cst(cur)
orb = np.array(orb); q = len(orb)
def step(rw):
    n = np.zeros_like(rw); n[1:-1] = rw[:-2] ^ (rw[1:-1] | rw[2:]); return n
WL = 2*T + 100; WR = T + 60; W = WL + WR; c = WL
for (r, s) in [(0, 0), (3, 11), (5, 40), (8, 50)]:
    bg = np.array([orb[s % q][((0 - x) + r) % N] for x in range(-WL, WR)], dtype=np.uint8)
    pert = bg.copy(); pert[c] = 1; pert[c+1:] = 0
    a, b = bg.copy(), pert.copy(); km = np.zeros(T + 1, dtype=np.int64)
    for t in range(T + 1):
        d = np.flatnonzero(a ^ b); km[t] = int(d.min()) - c + t
        if t < T: a, b = step(a), step(b)
    inc = np.diff(km); breaks = [t for t in range(200 + 8, T) if inc[t] != inc[t - 19]]
    print(f"alignment ({r},{s}): x_min range over [200, {T}]: [{int((km - np.arange(T+1))[200:].min())}, {int((km - np.arange(T+1))[200:].max())}]; breaks of the 19-law after t=200: {len(breaks)} (first {breaks[:5]})", flush=True)
print("LONG_ZERO_DONE")
