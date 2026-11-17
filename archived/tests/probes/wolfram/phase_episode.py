#!/usr/bin/env python3
"""phase_episode.py NAME KMAX: exact episode law M_E(k) for a phase E given as a ring in the light-speed frame (c = frame rule), over all
2^(k+1) prefixes behind a black edge and all distinct alignments (collapsed by the rotator symmetry: E(j,t) = y(j - r t + a), one parameter a
when c = rho^r). Reports whether any prefix agrees to the horizon. Cloud, Block 25 (A)."""
import sys, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); PROBES = os.path.join(HERE, '..') if HERE.endswith('wolfram') else HERE
name, KMAX = sys.argv[1], int(sys.argv[2])
if name == 'P1024':
    ring = tuple(int(c) for c in open(os.path.join(PROBES, 'phase1024_ring.txt')).read().strip()); lag = 21
elif name == 'G16':
    from pysat.solvers import Solver
    N, r = 128, 72; yv = lambda i: (i % N) + 1; cl = []; nv = N
    for n in range(N):
        nv += 1; o = nv; a, b = yv(n-1), yv(n-2); cl += [[-a, o], [-b, o], [a, b, -o]]
        x, z = yv(n-r), yv(n); cl += [[-x, z, o], [-x, -z, -o], [x, -z, o], [x, z, -o]]
    ds = []
    for i in range(N // 2):
        nv += 1; d = nv; a, b = yv(i), yv(i + N // 2); ds.append(d); cl += [[-d, a, b], [-d, -a, -b]]
    cl.append(ds)
    with Solver(name='cadical195', bootstrap_with=cl) as s_:
        assert s_.solve(); m = s_.get_model(); ring = tuple(1 if m[i] > 0 else 0 for i in range(N))
    lag = 72
elif name == 'G8':
    ring = (1, 0, 0, 0); lag = None
elif name == 'P480':
    rows = [l.split() for l in open(os.path.join(PROBES, 'phase480_p32.txt')) if l.strip() and not l.startswith('#')]
    ring = tuple(int(v, 16) & 1 for u, v in rows); lag = None   # bit 0 of each state's newer column = the ring at time 0
N = len(ring); y = np.array(ring, dtype=np.uint8)
def cst(s): return s ^ (np.roll(s, 1) | np.roll(s, 2))
if lag is not None:
    assert np.array_equal(cst(y), np.roll(y, lag)), "c(y) = rho^lag y"
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y): orb.append(cur.copy()); cur = cst(cur)
orb = np.array(orb); q = len(orb)
# alignments: E(j, t) = orb[(t+s) % q][(j + r) % N]; with c = rho^lag, orb[t][i] = y[i - lag t], so E depends on (r - lag s) mod N only
als = [(a, 0) for a in range(N)] if lag is not None else ([(a, s) for a in range(N) for s in (0, 1)] if name == 'P480' else [(r, s) for r in range(N) for s in range(q)])
print(f"{name}: ring {N}, frame period {q}, alignments used {len(als)}", flush=True)
def traces(k, H):
    n = 1 << (k+1); rr = np.arange(n, dtype=np.int64)
    X = np.zeros((k+2, n), dtype=np.uint8); X[0] = 1
    for j in range(1, k+2): X[j] = (rr >> (j-1)) & 1
    a = np.empty((H, n), dtype=np.uint8); b = np.empty_like(a)
    for t in range(H):
        a[t], b[t] = X[k], X[k+1]
        Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
    return a, b
Ms = []
for k in range(1, KMAX + 1):
    H = 3*k + 3*q + 24
    a, b = traces(k, H); best = 0; athor = 0
    for (r, s) in als:
        ek = orb[(np.arange(H) + s) % q, (k + r) % N]; ek1 = orb[(np.arange(H) + s) % q, (k + 1 + r) % N]
        agree = (a == ek[:, None]) & (b == ek1[:, None])
        first_false = np.where(agree.all(axis=0), H, agree.argmin(axis=0))
        best = max(best, int(first_false.max())); athor += int((first_false >= H).sum())
    Ms.append(best)
    print(f"k={k:2d} M={best:4d} (horizon {H}) prefixes agreeing to the horizon: {athor}", flush=True)
print(f"M_{name}(1..{KMAX}) = {' '.join(map(str, Ms))}")
print("PHASE_EPISODE_DONE")
