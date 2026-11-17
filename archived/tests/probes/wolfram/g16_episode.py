#!/usr/bin/env python3
"""g16_episode.py KMAX: exact episode law M_E(k) for the phase G16 (128-cell ring y with c(y) = rho^72 y, time period 16),
over all 2^(k+1) prefixes behind a black edge and all 128 x 16 alignments. Cloud, Block 17."""
import sys, math, numpy as np
from pysat.solvers import Solver
KMAX = int(sys.argv[1])
N, r = 128, 72
y = lambda i: (i % N) + 1
cl = []; nv = N
for n in range(N):
    nv += 1; o = nv; a, b = y(n-1), y(n-2)
    cl += [[-a, o], [-b, o], [a, b, -o]]
    x, z = y(n-r), y(n)
    cl += [[-x, z, o], [-x, -z, -o], [x, -z, o], [x, z, -o]]
ds = []
for i in range(N // 2):
    nv += 1; d = nv; a, b = y(i), y(i + N // 2); ds.append(d); cl += [[-d, a, b], [-d, -a, -b]]
cl.append(ds)
with Solver(name='cadical195', bootstrap_with=cl) as s:
    assert s.solve(); m = s.get_model(); ring = tuple(1 if m[i] > 0 else 0 for i in range(N))
def cstep(st): return tuple(st[j] ^ (st[(j-1) % N] | st[(j-2) % N]) for j in range(N))
assert cstep(ring) == tuple(ring[(j - r) % N] for j in range(N)), "c(y) = rho^72 y"
orbit = [ring]; cur = cstep(ring)
while cur != ring: orbit.append(cur); cur = cstep(cur)
q = len(orbit); print(f"G16 ring: N={N}, time period q={q}, weight {sum(ring)}", flush=True)
orb = np.array(orbit, dtype=np.uint8)
def traces(k, H):
    n = 1 << (k+1); rr = np.arange(n, dtype=np.int64)
    X = np.zeros((k+2, n), dtype=np.uint8); X[0] = 1
    for j in range(1, k+2): X[j] = (rr >> (j-1)) & 1
    a = np.empty((H, n), dtype=np.uint8); b = np.empty_like(a)
    for t in range(H):
        a[t], b[t] = X[k], X[k+1]
        Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
    return a, b
def inserted_prefix(k, rr, s):
    st = orbit[s % q]; v = 0
    for j in range(1, k+2): v |= int(st[(j + rr) % N]) << (j-1)
    return v
Ms = []
for k in range(1, KMAX+1):
    H = 3*k + 3*q + 24
    a, b = traces(k, H)
    best = 0; argmax = []
    for rr in range(N):
        for s in range(q):
            ek = orb[(np.arange(H) + s) % q, (k + rr) % N]; ek1 = orb[(np.arange(H) + s) % q, (k + 1 + rr) % N]
            agree = (a == ek[:, None]) & (b == ek1[:, None])
            # run length = number of leading True in each column
            first_false = np.where(agree.all(axis=0), H, agree.argmin(axis=0))
            rm = int(first_false.max())
            if rm > best: best, argmax = rm, [(rr, s, int(x)) for x in np.flatnonzero(first_false == rm)[:20]]
            elif rm == best: argmax += [(rr, s, int(x)) for x in np.flatnonzero(first_false == rm)[:20]]
    nwit = sum(1 for (rr, s, x) in argmax if x == inserted_prefix(k, rr, s))
    Ms.append(best)
    print(f"k={k:2d} M={best:3d} (horizon {H}) maximizers listed {len(argmax)}, inserted-edge witnesses among them {nwit}; at horizon: {best >= H}", flush=True)
print("M_G16(1..%d) = %s" % (KMAX, ' '.join(map(str, Ms))))
print("G16_EPISODE_DONE")
