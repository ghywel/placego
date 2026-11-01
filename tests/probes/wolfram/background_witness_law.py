#!/usr/bin/env python3
"""bg_law3.py NAME T J KMAX: witness fronts on the trusted range (front + 40 < J+1-2t), exact eventual periodicity of the increments
(period <= 300) on that range, the per-alignment arrival law and W(k)."""
import sys, numpy as np
from collections import Counter
name = sys.argv[1]; T, J, KMAX = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
STATE0 = {'c7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000', 's12_68': '100100000000', 'e4_8': '1000'}[name]
p = len(STATE0); s0 = tuple(int(c) for c in STATE0)
def ring_step(s): return tuple(s[j] ^ (s[(j-1) % p] | s[(j-2) % p]) for j in range(p))
orbit = [s0]; cur = ring_step(s0)
while cur != s0: orbit.append(cur); cur = ring_step(cur)
q = len(orbit)
fronts = {}
for r in range(p):
    for s in range(q):
        X = np.zeros(J+1, dtype=np.uint8); X[0] = 1
        st = orbit[s % q]
        for j in range(1, J+1): X[j] = st[(j+r) % p]
        R = np.full(T+1, -2, dtype=np.int64)
        for t in range(T+1):
            lim = J+1-2*t
            E = np.array([orbit[(t+s) % q][(j+r) % p] for j in range(lim)], dtype=np.uint8)
            Dm = np.flatnonzero(X[:lim] ^ E); R[t] = Dm.max() if Dm.size else -1
            if R[t] + 40 >= lim: R = R[:t]; break       # beyond the trusted range
            Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
        fronts[(r, s)] = R
def law(R):
    inc = np.diff(R); n = len(inc)
    for per in range(1, 301):
        if n < 3*per: break
        if not np.all(inc[n-2*per:n-per] == inc[n-per:]): continue
        t0 = n - 2*per
        while t0 > 0 and inc[t0-1] == inc[t0-1+per]: t0 -= 1
        return t0, per, int(inc[t0:t0+per].sum())
    return None
laws = {a: law(R) for a, R in fronts.items()}
print(f"{name}: p={p} q={q}; trusted front length min/max {min(len(R) for R in fronts.values())}/{max(len(R) for R in fronts.values())}; alignments without a law: {sum(1 for l in laws.values() if l is None)}")
print("  (period, shift, speed) classes:", sorted(Counter((l[1], l[2], round(l[2]/l[1], 3)) for l in laws.values() if l).items(), key=lambda x: -x[1])[:12])
print("  earliest-start t0 distribution (max):", max(l[0] for l in laws.values() if l))
def arrival(a, k):
    R = fronts[a]; hit = np.flatnonzero(R >= k)
    if hit.size: return int(hit[0])
    l = laws[a]
    if l is None or l[2] <= 0: return None
    t0, per, sh = l; best = None
    for t in range(t0, min(t0 + per, len(R))):
        m = max(0, -(-(k - R[t]) // sh)); cand = t + m*per
        if R[t] + m*sh >= k and (best is None or cand < best): best = cand
    return best
W = []; att = []
for k in range(1, KMAX+1):
    arrs = {a: arrival(a, k) for a in fronts}
    w = max(v for v in arrs.values() if v is not None); W.append(w); att.append([a for a, v in arrs.items() if v == w][:4])
print("W(1..%d) = %s" % (KMAX, ' '.join(map(str, W))))
for k in (20, 40, 60, 100, 150, 200, 300):
    if k <= KMAX: print(f"  k={k}: W={W[k-1]} attained by {att[k-1]} with laws {[laws[a] for a in att[k-1]]}")
# the slowest classes: min speed
sp = sorted(set(round(l[2]/l[1], 4) for l in laws.values() if l))
print("  distinct asymptotic speeds:", sp[:8], "...", sp[-4:])
print("BG_LAW3_DONE")
