#!/usr/bin/env python3
"""What the smallest windows already force on the gaps of column 1, for every right half, with no target removed.

Prediction, written before the run. At some W <= 16 every cycle of the physical double-step graph has all its gaps in
{2, 3, 4, 5} and no all-white cycle (0.6). Then every right half, finite or infinite, has only boundedly many gaps
outside {2, 3, 4, 5}, by a small finite certificate, with no entry hypothesis. That would give CQ01 from Q01 restricted to
those gaps, where the kit's not_finSupp_Psi_of_Q01Gap needs the window to enter the trap.
Counterfactual: a cycle with gap 1 or gap at least 6, or an all-white cycle, at every W <= 22: some right half keeps such
gaps at that width, and a wider or different statement is needed.
Control: W = 16 restricted to the kit's complement must give R-02's 3,483-window core in lift.c.
"""
import sys, collections
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
def moves(c, W):
    mask = np.int64((1 << W) - 1); out = []
    for x in range(4):
        b = c | (np.int64(x) << np.int64(W))
        b = (b << 1) ^ (b | (b >> 1))
        b = ((b << 1) | 1) ^ (b | (b >> 1))
        out.append(b & mask)
    return out
for W in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    n = 1 << W
    c = np.arange(n, dtype=np.int64)
    mv = moves(c, W)
    S = np.concatenate([c] * 4); D = np.concatenate(mv)
    key = np.unique(S * n + D); S = key // n; D = key % n
    g = csr_matrix((np.ones(len(S), dtype=np.int8), (S, D)), shape=(n, n))
    nc, lab = connected_components(g, directed=True, connection='strong')
    size = np.bincount(lab, minlength=nc)
    loop = np.zeros(nc, bool); loop[lab[S[S == D]]] = True
    cyc = np.nonzero((size > 1) | loop)[0]
    black = (c & 1).astype(bool)
    allg = collections.Counter(); rows = []
    for k in cyc:
        v = np.nonzero(lab == k)[0]
        sub = g[v][:, v].astype(np.int32).tocsr()
        A = sub.T.tocsr()
        b = black[v]
        cur = b.copy(); gaps = []
        for gp in range(1, 40):
            if not cur.any(): break
            nx = (A @ cur.astype(np.int32)) > 0
            if (nx & b).any(): gaps.append(gp)
            cur = nx & ~b
        white = bool(cur.any()) or not b.any()
        rows.append((len(v), gaps, white))
        for x in gaps: allg[x] += 1
    rows.sort(key=lambda r: -r[0])
    print('W', W, 'cyclic components', len(cyc), 'gaps over all', sorted(allg), 'white cycle', any(r[2] for r in rows), 'largest', rows[:4], flush=True)
