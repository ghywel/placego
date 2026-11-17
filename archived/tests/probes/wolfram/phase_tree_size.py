#!/usr/bin/env python3
"""L1485 (Local, 2026-11-03): the size of Cloud's top-word tree certificate (CL706; L1484's `layer`, generalised to depth k)
for the phases P1024 and P480, over phase_episode.py's alignment representatives.
Run: python3 tests/probes/wolfram/phase_tree_size.py NAME KMAX        (NAME = P1024, P480 or G16)

Phase E(j, t) = orb[(t + s) % q][(j + r) % N], with orb the ring's orbit under the frame rule c(y)_n = y_n xor (y_(n-1) or y_(n-2)).
Representatives: (r, 0) for every r when c is a rotation (G16, P1024); (r, s), s in {0, 1}, for P480 after checking that c^2 is a
rotation (the reduction phase_episode.py uses). Depth k: wd(t) = min(2t, k + 1); a word of width wd(t + 1) is completed with bit 0
black and unread bits white, run t steps of the edge map, and kept iff bits k, k + 1 match E(k, t), E(k + 1, t).
Per k: retained nodes (sum of layers 1, 2, ...), candidate tests (every extension tried, including the empty layer's), the deepest
nonempty layer (must equal phase_episode's M(k)), and the largest per-representative node count. Prints counts only.
"""
import os
import sys
import time

import numpy as np

name, KMAX = sys.argv[1], int(sys.argv[2])
HERE = os.path.dirname(os.path.abspath(__file__)); PROBES = os.path.join(HERE, '..')
if name == 'P1024':
    y = np.array([int(c) for c in open(os.path.join(PROBES, 'phase1024_ring.txt')).read().strip()], dtype=np.uint8); lag = 21
    MREC = [19, 19, 20, 21, 22, 23, 24, 24]
elif name == 'P480':
    rows = [l.split() for l in open(os.path.join(PROBES, 'phase480_p32.txt')) if l.strip() and not l.startswith('#')]
    y = np.array([int(v, 16) & 1 for u, v in rows], dtype=np.uint8); lag = None
    MREC = [15, 15, 16, 17, 20, 21, 21, 23, 23, 24]
elif name == 'G16':
    src = open(os.path.join(PROBES, 'upward_rigid.py')).read()
    lit = src.split('RING16 = (', 1)[1].split(')', 1)[0]
    y = np.array([1 if ch == '#' else 0 for ch in ''.join(p.strip().strip("'") for p in lit.split('\n'))], dtype=np.uint8); lag = 72
    MREC = [8, 8, 9, 11, 12, 13, 13, 16, 17, 19, 19, 21, 21, 22]
N = len(y)
cst = lambda s: s ^ (np.roll(s, 1) | np.roll(s, 2))
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y):
    orb.append(cur.copy()); cur = cst(cur)
orb = np.array(orb); q = len(orb)
if lag is not None:
    assert np.array_equal(cst(y), np.roll(y, lag)), 'c(y) = rho^lag y'
    reps = [(r, 0) for r in range(N)]
else:
    m2 = [m for m in range(N) if np.array_equal(orb[2 % q], np.roll(y, m))]
    assert m2, 'c^2 is not a rotation of the ring'
    reps = [(r, s) for r in range(N) for s in (0, 1)]
    print('%s: c^2 = rho^%d on the ring' % (name, m2[0]))
print('%s: ring %d, frame period %d, representatives %d' % (name, N, q, len(reps)), flush=True)


def tree(k, r, s):
    E = lambda j, t: int(orb[(t + s) % q][(j + r) % N])
    wd = lambda t: min(2 * t, k + 1)
    S = [0]; nodes = 0; tests = 0; t = 0
    while S:
        d = wd(t + 1) - wd(t); W = wd(t + 1); e14, e15 = E(k, t), E(k + 1, t); nxt = []
        for w in S:
            for e in range(1 << d):
                w2 = (w << d) | e; c = (w2 << (k + 2 - W)) | 1; tests += 1
                for _ in range(t):
                    c ^= (c << 1) | (c << 2)
                if (c >> k) & 1 == e14 and (c >> (k + 1)) & 1 == e15:
                    nxt.append(w2)
        nodes += len(nxt); S = nxt; t += 1
        assert t < 4000, 'no extinction'
    return nodes, tests, t - 1   # t - 1: the deepest nonempty layer


Ms = []
for k in range(1, KMAX + 1):
    t0 = time.time(); tot_n = tot_t = 0; M = 0; maxn = 0
    for (r, s) in reps:
        n, ts, m = tree(k, r, s)
        tot_n += n; tot_t += ts; M = max(M, m); maxn = max(maxn, n)
    Ms.append(M)
    print('k=%2d: nodes %9d, tests %9d, deepest layer %3d (record M %s), max per representative %6d, %.1f s' % (
        k, tot_n, tot_t, M, MREC[k - 1] if k <= len(MREC) else '-', maxn, time.time() - t0), flush=True)
print('deepest layers equal the record\'s M(k): %s' % (Ms == MREC[:KMAX]))
print('PHASE_TREE_SIZE_DONE')
