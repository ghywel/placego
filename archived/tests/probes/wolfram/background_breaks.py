#!/usr/bin/env python3
"""bg_breaks.py: (12, 68), all 816 alignments to T=1700: do the laws detected on t <= 700 survive to 1700? W(k) to 300 by direct hits only.
Control: alignment (0, 51) recomputed at a different depth J to confirm the break at t=1590."""
import numpy as np
from collections import Counter
STATE0 = '100100000000'; s0 = tuple(int(c) for c in STATE0); p = len(s0)
def ring_step(st): return tuple(st[j] ^ (st[(j-1) % p] | st[(j-2) % p]) for j in range(p))
orbit = [s0]; cur = ring_step(s0)
while cur != s0: orbit.append(cur); cur = ring_step(cur)
q = len(orbit)
def fronts(r, s, T, J, margin=60):
    X = np.zeros(J+1, dtype=np.uint8); X[0] = 1; st = orbit[s % q]
    for j in range(1, J+1): X[j] = st[(j+r) % p]
    Erows = {}
    R = np.full(T+1, -1, dtype=np.int64)
    for t in range(T+1):
        lim = J+1-2*t
        st = orbit[(t+s) % q]; E = np.array([st[(j+r) % p] for j in range(lim)], dtype=np.uint8)
        Dm = np.flatnonzero(X[:lim] ^ E); R[t] = Dm.max() if Dm.size else -1
        assert R[t] + margin < lim, f"trusted range at t={t}"
        Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
    return R
Rc = fronts(0, 51, 1600, 6000)
print("control (0,51) at J=6000: R[1584..1598] =", list(map(int, Rc[1584:1599])), "(expected 1896 1897 1899 1901 1901 1903 1905 1903 1905 1904 1904 1906 1908 1910 1910)")
def law(inc, upto):
    seg = inc[:upto]; n = len(seg)
    for per in range(1, 301):
        if n < 3*per: break
        if np.array_equal(seg[n-2*per:n-per], seg[n-per:]):
            t0 = n - 2*per
            while t0 > 0 and seg[t0-1] == seg[t0-1+per]: t0 -= 1
            return t0, per, int(seg[t0:t0+per].sum())
    return None
T, J = 1700, 6000
KMAX = 300
Wd = np.zeros(KMAX+1, dtype=np.int64); nohit = Counter(); breaks_at = {}; laws700 = {}; laws1700 = {}
for r in range(p):
    for s in range(q):
        R = fronts(r, s, T, J); inc = np.diff(R)
        for k in range(1, KMAX+1):
            hit = np.flatnonzero(R >= k)
            if hit.size: Wd[k] = max(Wd[k], hit[0])
            else: nohit[k] += 1
        l7 = law(inc, 700); laws700[(r, s)] = l7
        if l7:
            t0, per, sh = l7
            b = [t for t in range(t0 + per, T) if inc[t] != inc[t - per]]
            breaks_at[(r, s)] = b[0] if b else None
        laws1700[(r, s)] = law(inc, T)
W12 = [int(x) for x in open('background_witness_law_s12_68.out').read().split('W(1..300) = ')[1].split('\n')[0].split()]
print(f"W_direct(1..300) equals the CL673 W(1..300): {all(int(Wd[k]) == W12[k-1] for k in range(1, 301))}; alignments not reaching k by T=1700: {dict(nohit) if nohit else 'none'}")
diff = [(k, int(Wd[k]), W12[k-1]) for k in range(1, 301) if int(Wd[k]) != W12[k-1]]
print("  differences (k, direct, CL673):", diff[:20])
withlaw = [a for a in laws700 if laws700[a]]
broken = {a: b for a, b in breaks_at.items() if b is not None}
print(f"alignments with a law by t=700: {len(withlaw)}; of these, laws broken by t=1700: {len(broken)}")
cls = Counter((laws700[a][1], laws700[a][2]) for a in broken)
print("  broken by (period, shift) class:", dict(cls), "| class sizes at 700:", dict(Counter((l[1], l[2]) for l in laws700.values() if l)))
print("  break times (first 40 sorted):", sorted(broken.values())[:40])
print("  break-time distribution per 200 ticks:", {a: sum(1 for b in broken.values() if a <= b < a+200) for a in range(700, 1700, 200)})
print("laws at 1700 (period, shift) classes:", sorted(Counter((l[1], l[2]) for l in laws1700.values() if l).items(), key=lambda x: -x[1])[:10], "| without a law at 1700:", sum(1 for l in laws1700.values() if l is None))
print("BG_BREAKS_DONE")
