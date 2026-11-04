#!/usr/bin/env python3
"""walk_merge.py [NROWS] [LOG2T]: after the time shift that aligns a left-finite row's band-edge walk with the seed's (walk_align.py,
P-F7), do the two orbits themselves coincide, and how far beyond the band edge? (Cloud, CL721 P-F8.)
Wall frame (bit 0 the left edge; bit j at tick t + 1 reads bits j - 2, j - 1, j at tick t, so a prefix's future is its own).
For the single seed and NROWS random left-finite rows (CL696's construction, rng 606, the same rows as walk_align.py): the shift
s from the alignment pass (best agreement of the step sequences, |s| <= 400); then, stepping the seed at tick t and the row at
tick t + s together, the lag-16 band edges B_seed(t), B_row(t + s) and the merge front J(t) = the lowest bit where the seed's
row t and the row's row t + s differ (K, beyond the pattern, if they are equal). Reported per row: the last tick at which the
band edges differ (the end of the transient), the last tick at which J <= B_seed, and over the window [T/8, T/2] the margin
J - B_seed: min, median, mean, 99th percentile, max, the means on the two halves of the window, and the fraction of ticks with
the margin below 8 (CL719's determination horizon)."""
import sys, time, numpy as np
from collections import deque
NROWS = int(sys.argv[1]) if len(sys.argv) > 1 else 20
L2T = int(sys.argv[2]) if len(sys.argv) > 2 else 16
T = 1 << L2T; P = 16; T0 = T // 8; TH = T // 2; K = 2 * T + 104; MASK = (1 << K) - 1; SMAX = 400
def step(V): return ((V << 2) ^ ((V << 1) | V)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
def band_edge(seed):
    V = seed; rows = deque([V], maxlen=P + 1); B = []
    for t in range(0, TH + P + 2):
        if t >= P and t - P <= TH + 1:
            B.append(lowbit(rows[0] ^ rows[-1]))
        V = step(V); rows.append(V)
    return np.array(B, dtype=np.int64)
def align(Dseed, Drow):
    best = (-1.0, 0)
    for s in range(-SMAX, SMAX + 1):
        lo = T0 + max(0, -s); hi = TH - max(0, s)
        a = Dseed[lo:hi]; b = Drow[lo + s:hi + s]
        if len(a) < 1000: continue
        f = float(np.mean(a == b))
        if f > best[0]: best = (f, s)
    return best[1], best[0]
def merge_pass(seed_r, s):
    t_start = max(0, -s)
    Vs = 1; Vr = seed_r
    for _ in range(t_start): Vs = step(Vs)
    for _ in range(t_start + s): Vr = step(Vr)
    ds = deque([Vs], maxlen=P + 1); dr = deque([Vr], maxlen=P + 1)
    tt, Bs, Br, J = [], [], [], []
    for t in range(t_start + 1, TH + P + 2):
        Vs = step(Vs); Vr = step(Vr); ds.append(Vs); dr.append(Vr)
        if len(ds) == P + 1:
            tt.append(t - P); Bs.append(lowbit(ds[0] ^ ds[-1])); Br.append(lowbit(dr[0] ^ dr[-1])); J.append(lowbit(ds[0] ^ dr[0]))
    return (np.array(tt), np.array(Bs, dtype=np.int64), np.array(Br, dtype=np.int64), np.array(J, dtype=np.int64))
t0 = time.time()
Bseed = band_edge(1); Dseed = np.diff(Bseed)
rng = np.random.default_rng(606)
print(f"T=2^{L2T}, window [{T0}, {TH}]; shifts up to {SMAX}; K={K} marks identical rows")
print("  row                      width  s     agree  lastB!=  lastJ<=B   margin J-B on the window: min  med   mean   p99   max   half1  half2  frac<8")
summ = []
for i in range(NROWS):
    wb = int(rng.integers(1, 65)); seed = ((int(rng.integers(0, 1 << 32)) << 32) | int(rng.integers(0, 1 << 32))) & ((1 << wb) - 1) | 1
    Brow = band_edge(seed); s, f = align(Dseed, np.diff(Brow))
    tt, Bs, Br, J = merge_pass(seed, s)
    neq = tt[Bs != Br]; lastB = int(neq.max()) if len(neq) else -1
    le = tt[J <= Bs]; lastJ = int(le.max()) if len(le) else -1
    w = (tt >= T0) & (tt <= TH); m = (J - Bs)[w]; tw = tt[w]
    identical = bool(np.all(J[w] == K))
    if identical:
        print(f"  {('0x%x' % seed)[:24]:24s} {wb:5d} {s:4d} {f:7.4f} {lastB:8d} {lastJ:9d}   rows identical on the window (J = K)")
        summ.append((wb, s, lastB, lastJ, None)); continue
    h1 = m[tw < (T0 + TH) // 2].mean(); h2 = m[tw >= (T0 + TH) // 2].mean()
    print(f"  {('0x%x' % seed)[:24]:24s} {wb:5d} {s:4d} {f:7.4f} {lastB:8d} {lastJ:9d}   {int(m.min()):6d} {int(np.median(m)):4d} {m.mean():7.1f} {int(np.percentile(m, 99)):5d} {int(m.max()):5d}   {h1:6.1f} {h2:6.1f} {float(np.mean(m < 8)):7.4f}", flush=True)
    summ.append((wb, s, lastB, lastJ, (int(m.min()), m.mean(), h1, h2, float(np.mean(m < 8)))))
rows = [x for x in summ if x[4] is not None]
print(f"rows compared: {len(rows)} (rows identical to the seed on the window: {len(summ) - len(rows)})")
print(f"last tick with B_row(t+s) != B_seed(t): max over rows {max(x[2] for x in summ)}; last tick with J <= B_seed: max over rows {max(x[3] for x in summ)}")
if rows:
    print(f"margin J - B_seed on the window: min over rows {min(x[4][0] for x in rows)}; mean over rows {np.mean([x[4][1] for x in rows]):.1f} (range {min(x[4][1] for x in rows):.1f} .. {max(x[4][1] for x in rows):.1f})")
    print(f"half-window means: first {np.mean([x[4][2] for x in rows]):.1f}, second {np.mean([x[4][3] for x in rows]):.1f}; rows with second/first > 1.5: {sum(x[4][3] > 1.5 * x[4][2] for x in rows)} of {len(rows)}")
    print(f"fraction of ticks with margin < 8: max over rows {max(x[4][4] for x in rows):.4f}")
print(f"total {time.time()-t0:.1f} s")
print("WALK_MERGE_DONE")
