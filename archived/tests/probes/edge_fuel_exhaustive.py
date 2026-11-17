#!/usr/bin/env python3
"""L1313 T36 (c) (Local, 2026-11-02): exhaustive prepared prefixes under the black edge, against G16.
reports/rule30-genealogy.md section 41 (P36c written first). Run: python3 tests/probes/edge_fuel_exhaustive.py K [K ...]

All 2^K prefixes (digits at depths 0 .. K-1) above the clean G16 tail, at all 128 alignment classes, evolved by the edge
map (black cell at depth -1, white above) for 6K + 60 ticks with numpy, all prefixes at once. Front R(t) = deepest depth
>= 0 where the row differs from G16 (-1 if none). Reported: largest total drawdown, largest late drawdown (after the
front first reaches depth 2K), runs that never reach depth 2K, and the slowest speed.
"""
import os
import sys
import runpy
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
p, cols, _ = g['phases']()['G16']; NC = len(cols)
for K in [int(x) for x in sys.argv[1:]]:
    T = 6 * K + 60; Dm = K + 2 * T + 8; P = 1 << K
    pref = ((np.arange(P)[:, None] >> np.arange(K)[None, :]) & 1).astype(np.uint8)
    tot_dd = 0; late_dd = 0; never = 0; slow = 9.0; worst = None
    for a in range(8):
        for q in range(16):
            Er = [np.array([(cols[(n + a) % NC] >> ((t + q) % p)) & 1 for n in range(Dm)], dtype=np.uint8) for t in range(p)]
            X = np.tile(Er[0], (P, 1)); X[:, :K] = pref
            best = np.full(P, -2, dtype=np.int64); dd = np.zeros(P, dtype=np.int64); ddl = np.zeros(P, dtype=np.int64)
            passed = np.zeros(P, dtype=bool)
            for t in range(T + 1):
                Dd = X ^ Er[t % p][None, :]
                anyd = Dd.any(axis=1)
                R = np.where(anyd, Dm - 1 - np.argmax(Dd[:, ::-1], axis=1), -1)
                best = np.maximum(best, R); cur = best - R
                dd = np.maximum(dd, cur)
                passed |= R >= 2 * K
                ddl = np.where(passed, np.maximum(ddl, cur), ddl)
                # edge map: x_n <- x_n ^ (x_(n-1) | x_(n-2)), with x_(-1) = 1, x_(-2) = 0
                sh1 = np.empty_like(X); sh1[:, 1:] = X[:, :-1]; sh1[:, 0] = 1
                sh2 = np.empty_like(X); sh2[:, 2:] = X[:, :-2]; sh2[:, 1] = 1; sh2[:, 0] = 0
                X = X ^ (sh1 | sh2)
            i = int(np.argmax(dd))
            if dd[i] > tot_dd:
                tot_dd = int(dd[i]); worst = (a, q, format(i, '0%db' % K))
            late_dd = max(late_dd, int(ddl.max())); never += int((~passed).sum())
            slow = min(slow, float(R.min()) / T)
    print('K=%2d: %d prefixes x 128 classes, %d ticks: largest total drawdown %d (K + %d; alignment %s, prefix %s); '
          'largest late drawdown %d; never reached depth 2K: %d; slowest R(T)/T %.3f' % (
              K, P, T, tot_dd, tot_dd - K, worst[:2], worst[2], late_dd, never, slow), flush=True)
