#!/usr/bin/env python3
"""band_edge.py LOG2T LOG2P: the single seed's band edge B(t) (8.74) on the autonomous left-frame system; its step distribution.
Cloud, Block 21(a)."""
import sys, numpy as np
L2T, L2P = int(sys.argv[1]), int(sys.argv[2]); T = 1 << L2T; P = 1 << L2P; K = T + P + 8; MASK = (1 << K) - 1
def stp(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
rows = []
V = 1
for t in range(T + P + 1):
    rows.append(V); V = stp(V)
B = np.zeros(T + 1, dtype=np.int64)
for t in range(T + 1):
    x = rows[t] ^ rows[t + P]
    B[t] = (x & -x).bit_length() - 1 if x else K
assert np.all(np.diff(B) >= 0), "B decreased"
d = np.diff(B[T//4:]); h = np.bincount(d, minlength=8)
print(f"band edge to T=2^{L2T}, P=2^{L2P}: B(T)={B[T]}, x/t at T = {(-T + B[T])/T:.4f}; mean step over [T/4, T] = {d.mean():.4f}")
print("step distribution (0..7 and beyond):", np.round(h[:8]/len(d), 4).tolist(), "max step", int(d.max()), "P(step>=8)", round(float((d >= 8).mean()), 5))
ac = [float(np.corrcoef(d[:-l], d[l:])[0, 1]) for l in range(1, 6)]
print("step autocorrelation lags 1..5:", np.round(ac, 4).tolist())
adv = d > 0
print(f"P(advance)={adv.mean():.4f}; P(advance | prev advance)={adv[1:][adv[:-1]].mean():.4f}; P(advance | prev none)={adv[1:][~adv[:-1]].mean():.4f}")
print("BAND_EDGE_DONE")
