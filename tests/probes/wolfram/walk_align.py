#!/usr/bin/env python3
"""walk_align.py [NROWS] [LOG2T]: is the band edge's walk literally the same for every left-finite row? (Cloud, CL720 P-F7.)
For the single seed and NROWS random left-finite rows (CL696's construction, rng 606, the same rows as news_frame_rows.py),
the lag-16 band edge B(t) on [T/8, T/2]; for each row the time shift s in [-400, 400] maximizing the agreement of the step
sequences Delta_row(t + s) = Delta_seed(t) over the overlap, the agreement fraction at that shift, and whether B_row(t + s) -
B_seed(t) is constant over the window (its min and max)."""
import sys, time, numpy as np
from collections import deque
NROWS = int(sys.argv[1]) if len(sys.argv) > 1 else 20
L2T = int(sys.argv[2]) if len(sys.argv) > 2 else 16
T = 1 << L2T; P = 16; T0 = T // 8; TH = T // 2; K = 2 * T + 104; MASK = (1 << K) - 1; SMAX = 400
def band_edge(seed):
    V = seed; rows = deque([V], maxlen=P + 1); B = []
    for t in range(0, TH + P + 2):
        if t >= P and t - P <= TH + 1:
            x = rows[0] ^ rows[-1]; B.append((x & -x).bit_length() - 1)
        V = ((V << 2) ^ ((V << 1) | V)) & MASK; rows.append(V)
    return np.array(B, dtype=np.int64)
t0 = time.time()
Bseed = band_edge(1); Dseed = np.diff(Bseed)
rng = np.random.default_rng(606)
print(f"T=2^{L2T}, window [{T0}, {TH}]; shifts up to {SMAX}")
print("  row                      width   best s  agreement   B_row(t+s)-B_seed(t): min  max")
aggs = []
for i in range(NROWS):
    wb = int(rng.integers(1, 65)); seed = ((int(rng.integers(0, 1 << 32)) << 32) | int(rng.integers(0, 1 << 32))) & ((1 << wb) - 1) | 1
    Brow = band_edge(seed); Drow = np.diff(Brow)
    best = (-1.0, 0)
    for s in range(-SMAX, SMAX + 1):
        lo = T0 + max(0, -s); hi = TH - max(0, s)
        a = Dseed[lo:hi]; b = Drow[lo + s:hi + s]
        if len(a) < 1000: continue
        f = float(np.mean(a == b))
        if f > best[0]: best = (f, s)
    f, s = best
    lo = T0 + max(0, -s); hi = TH - max(0, s)
    off = Brow[lo + s:hi + s] - Bseed[lo:hi]
    aggs.append(f)
    print(f"  {('0x%x' % seed)[:24]:24s} {wb:5d} {s:8d} {f:10.4f}   {int(off.min()):6d} {int(off.max()):5d}", flush=True)
print(f"agreement at the best shift: min {min(aggs):.4f}, max {max(aggs):.4f}, rows with agreement >= 0.99: {sum(a >= 0.99 for a in aggs)} of {NROWS}")
print(f"total {time.time()-t0:.1f} s")
print("WALK_ALIGN_DONE")
