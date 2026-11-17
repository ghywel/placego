#!/usr/bin/env python3
"""L1313 T36 (Local, 2026-11-02): does the black edge supply retreat fuel against G16?
reports/rule30-genealogy.md section 41 (predictions written first). Run: python3 tests/probes/edge_fuel.py [a|b]

Edge frame: digits at depths 0, 1, ... below a black cell at depth -1 and white above; the edge map is
Phi(x) = x ^ ((x << 1) | (x << 2) | 3). E = G16, two-sided, at alignment (a, q): E_n(t) = column (n + a) mod 128 at time
(t + q) mod 16. Mismatch D(t) = Phi^t(X) xor E(t) on depths >= 0; the front R(t) is its deepest 1 (-1 if none: the front
is then in the edge region). Drawdown = max_t (max_(s<=t) R(s) - R(t)); stall = longest run of ticks without a new
maximum of R.
(a) clean starts: X(0) = E(0) on depths >= 0, all 128 alignment classes (a in 0..7, q in 0..15), 20,000 ticks.
(b) prepared prefixes: random digits at depths 0 .. K-1 above the clean tail, K = 20, 40, 80, 160, 300 runs each at random
    alignments, 8K + 200 ticks; drawdown split at the first time R >= 2K.
"""
import os
import random
import sys
import runpy
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')
p, cols, _ = g['phases']()['G16']; NC = len(cols)


def erows(a, q, depth):
    return [sum(((cols[(n + a) % NC] >> ((t + q) % p)) & 1) << n for n in range(depth)) for t in range(p)]


def run(x, E, T, mask, split=None):
    best = -2; dd = 0; dd_early = 0; dd_late = 0; stall = 0; smax = 0; passed = False; R = -1
    for t in range(T + 1):
        d = (x ^ E[t % p]) & mask
        R = d.bit_length() - 1
        if R > best:
            best = R; stall = 0
        else:
            stall += 1; smax = max(smax, stall)
        cur = best - R; dd = max(dd, cur)
        if split is not None:
            if not passed and R >= split:
                passed = True
            if passed:
                dd_late = max(dd_late, cur)
            else:
                dd_early = max(dd_early, cur)
        x = (x ^ ((x << 1) | (x << 2) | 3)) & mask
    return R, dd, smax, dd_early, dd_late, passed


mode = sys.argv[1] if len(sys.argv) > 1 else 'ab'
if 'a' in mode:
    T = 20000; depth = 2 * T + 16; mask = (1 << depth) - 1
    sp, dds, sts = [], [], []
    for a in range(8):
        for q in range(16):
            E = erows(a, q, depth)
            R, dd, smax, *_ = run(E[0], E, T, mask)
            sp.append(R / T); dds.append(dd); sts.append(smax)
    print('(a) clean starts, 128 alignment classes, %d ticks: speed min %.3f median %.3f max %.3f; largest drawdown %d; '
          'longest stall %d' % (T, min(sp), sorted(sp)[64], max(sp), max(dds), max(sts)), flush=True)
if 'b' in mode:
    rng = random.Random(36)
    for K in (20, 40, 80, 160):
        T = 8 * K + 200; depth = 2 * T + K + 16; mask = (1 << depth) - 1
        early, late, notpassed, sp = [], [], 0, []
        for it in range(300):
            a, q = rng.randrange(8), rng.randrange(16)
            E = erows(a, q, depth)
            x = rng.getrandbits(K) | (E[0] >> K << K)
            R, dd, smax, de, dl, passed = run(x, E, T, mask, split=2 * K)
            early.append(de); late.append(dl); notpassed += not passed; sp.append(R / T)
        print('(b) K=%3d, 300 runs, %d ticks: early drawdown max %d (median %d); late drawdown max %d (median %d); '
              'runs not past depth 2K: %d; speed min %.3f' % (K, T, max(early), sorted(early)[150], max(late),
              sorted(late)[150], notpassed, min(sp)), flush=True)
