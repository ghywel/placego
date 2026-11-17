#!/usr/bin/env python3
"""news_frame_rows.py [NROWS] [LOG2T]: is the boundary dipole universal? CL719's news-frame measurements repeated on NROWS random
left-finite rows (CL696's construction: random odd seeds of random width 1..64 bits, rng 606) and the single seed as control
(Cloud, CL720, Part B). For each row to T = 2^LOG2T (default 2^16), trusted window [T/8, T/2] with the certified prefix check:
the band edge's mean step, P(heal), E[jump|heal]; the mismatch density rho(1), rho(2) above the edge; the row's black density at
h = -1, 0, 1 (the dipole) and on the settled side h in [-16, -1] and the news side h in [16, 64]."""
import sys, time, numpy as np
from collections import deque
NROWS = int(sys.argv[1]) if len(sys.argv) > 1 else 20
L2T = int(sys.argv[2]) if len(sys.argv) > 2 else 16
T = 1 << L2T; P = 16; W = min(8192, T // 8); T0 = T // 8; TH = T // 2; K = 2 * T + 104; MASK = (1 << K) - 1
def measure(seed):
    V = seed; rows = deque([V], maxlen=P + 1); keepA = keepB = None
    stats = dict(n=0, sumD=0, heals=0, sumJ=0, rho1=0, rho2=0, dm1=0, d0=0, d1=0, settled=0, news=0, viol=0)
    Bprev = None
    for t in range(0, T - W + P + 1):
        if t >= P:
            s = t - P
            if s <= TH + 1:
                r0 = rows[0]; x = r0 ^ rows[-1]; b = (x & -x).bit_length() - 1
                if Bprev is not None and T0 <= s - 1 <= TH:
                    d = b - Bprev; stats['n'] += 1; stats['sumD'] += d
                    if d > 0: stats['heals'] += 1; stats['sumJ'] += d
                    if (d == 0) != (decprev == 0): stats['viol'] += 1
                if T0 <= s <= TH:
                    stats['rho1'] += (x >> (b + 1)) & 1; stats['rho2'] += (x >> (b + 2)) & 1
                    stats['dm1'] += (r0 >> (b - 1)) & 1; stats['d0'] += (r0 >> b) & 1; stats['d1'] += (r0 >> (b + 1)) & 1
                    stats['settled'] += bin((r0 >> (b - 16)) & 0xFFFF).count('1') / 16
                    stats['news'] += bin((r0 >> (b + 16)) & ((1 << 49) - 1)).count('1') / 49
                Bprev = b; decprev = (r0 >> (b - 1)) & 1 if b >= 1 else 0
        if t == T - W: keepA = V
        if t == T - W + P: keepB = V; break
        V = ((V << 2) ^ ((V << 1) | V)) & MASK; rows.append(V)
    d = keepA ^ keepB; Kc = (d & -d).bit_length() - 1 if d else K
    m = TH - T0 + 1
    return dict(Kc=Kc, mean=stats['sumD'] / stats['n'], pheal=stats['heals'] / stats['n'], ejump=stats['sumJ'] / max(1, stats['heals']),
                rho1=stats['rho1'] / m, rho2=stats['rho2'] / m, dm1=stats['dm1'] / m, d0=stats['d0'] / m, d1=stats['d1'] / m,
                settled=stats['settled'] / m, news=stats['news'] / m, viol=stats['viol'], Bend=Bprev)
t0 = time.time()
print(f"T=2^{L2T}, window [{T0}, {TH}]; rows: the single seed and {NROWS} random left-finite rows (CL696's construction)")
print("  row                      width  Kc     B(TH)   mean   P(heal) E[jump]  rho1   rho2   d(-1)  d(0)   d(1)  settled  news  viol")
res = []
r = measure(1); res.append(('seed', 1, r))
print(f"  {'single seed':24s} {1:5d} {r['Kc']:6d} {r['Bend']:7d} {r['mean']:6.4f} {r['pheal']:7.4f} {r['ejump']:7.3f} {r['rho1']:6.3f} {r['rho2']:6.3f} {r['dm1']:6.3f} {r['d0']:6.3f} {r['d1']:6.3f} {r['settled']:7.3f} {r['news']:6.3f} {r['viol']:4d}", flush=True)
rng = np.random.default_rng(606)
for i in range(NROWS):
    wb = int(rng.integers(1, 65)); seed = ((int(rng.integers(0, 1 << 32)) << 32) | int(rng.integers(0, 1 << 32))) & ((1 << wb) - 1) | 1
    r = measure(seed); res.append((f"0x{seed:x}", wb, r))
    assert r['Bend'] + 8 < r['Kc'], "window edge beyond the certified prefix"
    print(f"  {('0x%x' % seed)[:24]:24s} {wb:5d} {r['Kc']:6d} {r['Bend']:7d} {r['mean']:6.4f} {r['pheal']:7.4f} {r['ejump']:7.3f} {r['rho1']:6.3f} {r['rho2']:6.3f} {r['dm1']:6.3f} {r['d0']:6.3f} {r['d1']:6.3f} {r['settled']:7.3f} {r['news']:6.3f} {r['viol']:4d}", flush=True)
import statistics as st
for key, name in [('mean', 'mean step'), ('pheal', 'P(heal)'), ('ejump', 'E[jump|heal]'), ('rho1', 'rho(1)'), ('rho2', 'rho(2)'), ('dm1', 'density h=-1'), ('d0', 'density h=0'), ('d1', 'density h=1')]:
    vals = [r[key] for _, _, r in res[1:]]
    print(f"random rows, {name:13s}: min {min(vals):.4f} max {max(vals):.4f} mean {st.mean(vals):.4f}; seed {res[0][2][key]:.4f}; max |row - seed| {max(abs(v - res[0][2][key]) for v in vals):.4f}")
print(f"total {time.time()-t0:.1f} s")
print("NEWS_FRAME_ROWS_DONE")
