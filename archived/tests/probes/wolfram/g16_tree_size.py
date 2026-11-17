#!/usr/bin/env python3
"""g16_tree_size.py K...: the size of a top-bits tree certificate for M_G16(k) < horizon (Cloud, CL706).
Locality: bit j of the edge code at tick s depends on initial bits j-2s..j, so an episode of length >= t at depths k, k+1
depends only on the top 2t bits of the (k+2)-bit prefix (the pair at tick s reads bits k-2s..k+1) (bits 0..k+1, bit 0 = 1). The certificate explores top words
two bits per tick and prunes at the first mismatch; its node count is sum over ticks t >= 1 and alignments (i, a) of the
number of distinct top-2t-bit words among prefixes with episode >= t. CHECK (G25): for every (i, a, t) with 2t <= k+1,
#survivors == #distinct top words x 2^(k+1-2t), asserted (survival is a function of the top word)."""
import sys, numpy as np
from pysat.solvers import Solver
N, r, H = 128, 72, 64
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
orbit = [ring]; cur = cstep(ring)
while cur != ring: orbit.append(cur); cur = cstep(cur)
q = len(orbit); assert q == 16; orb = np.array(orbit, dtype=np.uint8)
def traces(k):
    n = 1 << (k+1); rr = np.arange(n, dtype=np.int64)
    X = np.zeros((k+2, n), dtype=np.uint8); X[0] = 1
    for j in range(1, k+2): X[j] = (rr >> (j-1)) & 1
    A = np.empty((H, n), dtype=np.uint8); B = np.empty_like(A)
    for t in range(H):
        A[t], B[t] = X[k], X[k+1]
        Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
    return A, B
for k in map(int, sys.argv[1:]):
    n = 1 << (k+1); A, B = traces(k); rr = np.arange(n, dtype=np.int64); nb = k + 2   # bits 0..k+1; rr encodes bits 1..k+1
    nodes = np.zeros(H + 1, dtype=np.int64); maxw = np.zeros(H + 1, dtype=np.int64); checks = 0; M = 0
    for i in range(N):
        for a in range(q):
            tt = (np.arange(H) + a) % q
            Ek = orb[tt, (k + i) % N]; Ek1 = orb[tt, (k + 1 + i) % N]
            match = (A == Ek[:, None]) & (B == Ek1[:, None])
            alive = np.ones(n, dtype=bool); L = np.zeros(n, dtype=np.int64)
            for t in range(H):
                alive &= match[t]
                if not alive.any(): break
                L[alive] = t + 1
            assert not alive.any()
            Lm = int(L.max()); M = max(M, Lm)
            for t in range(1, Lm + 1):
                S = rr[L >= t]; w = min(2 * t, nb - 1)            # top w of the k+1 free bits (bit 0 is the fixed black edge)
                shift = (nb - 1) - w                               # rr holds bits 1..k+1, i.e. nb-1 free bits
                tops = S >> shift
                nd = np.unique(tops).size
                nodes[t] += nd; maxw[t] = max(maxw[t], nd)
                if True:
                    assert S.size == nd * (1 << shift), (k, i, a, t, S.size, nd, shift)   # survival depends on the top word only
                    checks += 1
    tot = int(nodes.sum())
    print(f"k={k:2d} M={M:2d} tree nodes (all 2048 alignments) = {tot:,}; per alignment {tot/2048:.0f}; "
          f"per-pair steps {int(((1<<(k+1))*2048)*(M+1)):,}; locality checks passed {checks:,}")
    print("   t  nodes[t]  max per alignment")
    for t in range(1, M + 1): print(f"  {t:2d} {nodes[t]:9,d} {maxw[t]:8d}")
    sys.stdout.flush()
print("G16_TREE_SIZE_DONE")
