#!/usr/bin/env python3
"""g16_survival.py KMAX: the survival profile of G16 episodes (Cloud, CL705; A5's sequel, feasibility).

For the phase G16 (the 128-cell ring y with c(y) = rho^72 y, time period 16; CL676's g16_episode.py) and each depth k <= KMAX:
over all 2^(k+1) black-edge prefixes (bit 0 = 1, bits 1..k+1 free) and all 128 x 16 alignments (i, a), the episode length L is
the number of ticks t = 0, 1, ... for which bits k, k+1 of the code equal E_k(t+a), E_{k+1}(t+a), E_j(t) = orbit[t mod 16][(j+i) mod 128].
Reported per k: M(k) = max L (control against CL676's table), surv[t] = #{(prefix, i, a): L >= t}, the certificate size
sum_t surv[t] (steps a first-mismatch certificate must simulate), and the family structure: per (i, a) and t, the number of
distinct values of the top min(2t, k+1) bits among survivors with L >= t (max and mean over (i, a)); bit k at tick t depends on
initial bits k-2t..k, so matching for t ticks constrains the top 2t bits.
Trusted window (G25): depths 1..KMAX, horizon H = 64 ticks per prefix; every prefix must mismatch before H (asserted)."""
import sys, numpy as np
from pysat.solvers import Solver
KMAX = int(sys.argv[1]); H = 64
N, r = 128, 72
y = lambda i: (i % N) + 1
cl = []; nv = N
for n in range(N):
    nv += 1; o = nv; a_, b_ = y(n-1), y(n-2)
    cl += [[-a_, o], [-b_, o], [a_, b_, -o]]
    x, z = y(n-r), y(n)
    cl += [[-x, z, o], [-x, -z, -o], [x, -z, o], [x, z, -o]]
ds = []
for i in range(N // 2):
    nv += 1; d = nv; a_, b_ = y(i), y(i + N // 2); ds.append(d); cl += [[-d, a_, b_], [-d, -a_, -b_]]
cl.append(ds)
with Solver(name='cadical195', bootstrap_with=cl) as s:
    assert s.solve(); m = s.get_model(); ring = tuple(1 if m[i] > 0 else 0 for i in range(N))
def cstep(st): return tuple(st[j] ^ (st[(j-1) % N] | st[(j-2) % N]) for j in range(N))
assert cstep(ring) == tuple(ring[(j - r) % N] for j in range(N)), "c(y) = rho^72 y"
orbit = [ring]; cur = cstep(ring)
while cur != ring: orbit.append(cur); cur = cstep(cur)
q = len(orbit); assert q == 16, q
orb = np.array(orbit, dtype=np.uint8)
print(f"G16 ring: N={N}, time period {q}, weight {sum(ring)}; horizon H={H}; depths 1..{KMAX}", flush=True)
KNOWN = {1:8,2:8,3:9,4:11,5:12,6:13,7:13,8:16,9:17,10:19,11:19,12:21,13:21,14:22}
def traces(k):
    n = 1 << (k+1); rr = np.arange(n, dtype=np.int64)
    X = np.zeros((k+2, n), dtype=np.uint8); X[0] = 1
    for j in range(1, k+2): X[j] = (rr >> (j-1)) & 1
    A = np.empty((H, n), dtype=np.uint8); B = np.empty_like(A)
    for t in range(H):
        A[t], B[t] = X[k], X[k+1]
        Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
    return A, B
for k in range(1, KMAX + 1):
    n = 1 << (k+1); A, B = traces(k); rr = np.arange(n, dtype=np.int64)
    surv = np.zeros(H + 1, dtype=np.int64); M = 0
    fam_max = np.zeros(H + 1, dtype=np.int64); fam_sum = np.zeros(H + 1, dtype=np.float64); fam_cnt = np.zeros(H + 1, dtype=np.int64)
    top_pairs = 0
    for i in range(N):
        for a in range(q):
            tt = (np.arange(H) + a) % q
            Ek = orb[tt, (k + i) % N]; Ek1 = orb[tt, (k + 1 + i) % N]
            match = (A == Ek[:, None]) & (B == Ek1[:, None])          # H x n
            alive = np.ones(n, dtype=bool); L = np.zeros(n, dtype=np.int64)   # L = ticks matched; 0 if the first tick fails
            for t in range(H):
                alive &= match[t]
                if not alive.any():
                    break
                L[alive] = t + 1
            assert not alive.any(), f"prefix alive at horizon: k={k} i={i} a={a}"
            Lm = int(L.max()); M = max(M, Lm)
            # survivors with L >= t, t = 0..Lm
            for t in range(0, Lm + 1):
                S = rr[L >= t]; surv[t] += S.size
                w = min(2 * t, k + 1)
                if t >= 1 and S.size:
                    tops = (S >> max(0, k + 1 - w)) if w else np.zeros_like(S)
                    nd = np.unique(tops).size
                    fam_max[t] = max(fam_max[t], nd); fam_sum[t] += nd; fam_cnt[t] += 1
    assert M == KNOWN[k], (k, M, KNOWN[k])
    size = int(surv.sum())
    print(f"k={k:2d} M={M:2d} (control ok)  certificate steps sum_t surv[t] = {size:,}")
    print("   t    surv[t]      ratio   fam_max  fam_mean")
    for t in range(0, M + 1):
        ratio = (surv[t] / surv[t-1]) if t >= 1 and surv[t-1] else float('nan')
        fm = (fam_sum[t] / fam_cnt[t]) if fam_cnt[t] else float('nan')
        print(f"  {t:2d} {surv[t]:11,d} {ratio:9.3f} {fam_max[t]:8d} {fm:9.2f}")
    sys.stdout.flush()
print("G16_SURVIVAL_DONE")
