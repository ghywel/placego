#!/usr/bin/env python3
"""L1312 T35 (Local, 2026-11-02): the drawdown of the mismatch front against a phase, from prepared mismatch regions.
reports/rule30-genealogy.md section 40 (predictions written first). Run: python3 tests/probes/drawdown.py PHASE R [R ...]

No edge. E = the phase (G8 or G16), two-sided, at every alignment class (cosets of its twist lattice). The initial
mismatch D(0) is supported on depths 0 .. r-1 with both ends 1, over all 2^(r-2) interiors. D evolves exactly:
D_n(t+1) = D_n xor [((E_(n-1) xor D_(n-1)) | (E_(n-2) xor D_(n-2))) xor (E_(n-1) | E_(n-2))]. The top (depth 0) is
pinned (section 40.1). The front R(t) is the deepest mismatch; the drawdown is max over t <= 3r + 30 of
(max_(s<=t) R(s)) - R(t). Reported per r: the largest drawdown, and how many cells above the top the front came at its
lowest, for the extreme pattern.
"""
import os
import sys
import runpy
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
name = sys.argv[1]; p, cols, _ = g['phases']()[name]; NC = len(cols)
classes = [(0, q) for q in range(8)] if name == 'G8' else [(a, q) for a in range(8) for q in range(16)]
OFF = 4
for r in [int(x) for x in sys.argv[2:]]:
    T = 3 * r + 30; Dm = OFF + r + 2 * T + 4; P = 1 << (r - 2)
    best = (-1, None)
    inter = ((np.arange(P)[:, None] >> np.arange(r - 2)[None, :]) & 1).astype(np.uint8)
    for (a, q) in classes:
        def erow(t):
            return np.array([(cols[(j - OFF + a) % NC] >> ((t + q) % p)) & 1 for j in range(-2, Dm)], dtype=np.uint8)
        Er = [erow(t) for t in range(p)]
        D = np.zeros((P, Dm), dtype=np.uint8)
        D[:, OFF] = 1; D[:, OFF + r - 1] = 1; D[:, OFF + 1:OFF + r - 1] = inter
        def front(D):
            return Dm - 1 - np.argmax(D[:, ::-1], axis=1)
        R = front(D); M = R.copy(); dd = np.zeros(P, dtype=np.int64); low = R.copy()
        for t in range(T):
            e = Er[t % p]                       # length Dm + 2; e[j + 2] is depth index j
            X = np.zeros((P, Dm + 2), dtype=np.uint8); X[:, 2:] = D ^ e[None, 2:]; X[:, :2] = e[None, :2]
            orX = X[:, 1:-1] | X[:, :-2]        # X_(n-1) | X_(n-2) for depth index j (columns j+1, j)
            orE = e[1:-1] | e[:-2]
            D = D ^ (orX ^ orE[None, :])
            R = front(D); M = np.maximum(M, R); dd = np.maximum(dd, M - R); low = np.minimum(low, R)
        i = int(np.argmax(dd))
        if dd[i] > best[0]:
            best = (int(dd[i]), (a, q, format(i, '0%db' % (r - 2)) if r > 2 else '', int(low[i] - OFF)))
    a, q, pat, lowest = best[1]
    print('%s r=%2d: patterns %d x %d alignment classes, %d ticks: largest drawdown %d (alignment a=%d q=%d, interior %s, '
          'front came to %d cells below the pinned top)' % (name, r, P, len(classes), T, best[0], a, q, pat, lowest), flush=True)
