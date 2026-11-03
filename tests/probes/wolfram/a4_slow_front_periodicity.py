#!/usr/bin/env python3
"""L1437 (Local, 2026-11-03): are the slow left fronts on 1010000 exact periodic walls? Reads a4_perturbation_census.py's
saved F(t) (SAVE.npz, outside git). Run: python3 tests/probes/wolfram/a4_slow_front_periodicity.py SAVE.npz P S [T1 LMAX]
For every pattern: the late slope over [T1, TMAX]; the least lag L <= LMAX with F(t + L) - F(t) constant for every t in
[T1, TMAX - L] (an exact periodic motion over that range), and its displacement m; and, for fronts fast at the end, the
last time the front is more than 20 cells off its final 2/9 line (the conversion time; the theorem's band is 17 cells).
"""
import sys
from collections import Counter
from fractions import Fraction

import numpy as np

z = np.load(sys.argv[1]); F = z['F'].astype(np.int64); pats = z['pats']
P, S = int(sys.argv[2]), int(sys.argv[3])
T1 = int(sys.argv[4]) if len(sys.argv) > 4 else 2000; LMAX = int(sys.argv[5]) if len(sys.argv) > 5 else 1260
TMAX = F.shape[0] - 1; NP = F.shape[1]; q = 63
fast = -(P - S) / P
sl = (F[TMAX] - F[T1]) / (TMAX - T1)
slow = np.flatnonzero(np.abs(sl - fast) >= 0.01)
print('patterns %d, TMAX %d, late window [%d, %d]: fast (within 0.01 of %.4f) %d, slow %d' % (
    NP, TMAX, T1, TMAX, fast, NP - len(slow), len(slow)))
per = Counter(); nonper = 0; examples = []
for k in slow:
    f = F[T1:, k]; found = None
    for L in range(1, LMAX + 1):
        d = f[L:] - f[:-L]
        if (d == d[0]).all():
            found = (L, int(d[0])); break
    if found is None:
        nonper += 1
    else:
        per[(found[0], found[1], str(Fraction(-found[1], found[0])))] += 1
        if len(examples) < 5:
            examples.append((int(pats[k]), found))
print('slow fronts exactly periodic in [%d, %d] with lag <= %d: %d; not: %d' % (T1, TMAX, LMAX, sum(per.values()), nonper))
print('  (least lag, displacement, speed): count -- %s' % sorted(per.items(), key=lambda kv: -kv[1])[:10])
print('  examples (pattern, (lag, displacement)): %s' % examples)
# conversion times: last t with F(t + q) - F(t) != the fast wall's q-tick displacement, for fronts fast at the end
dq_fast = Counter((F[TMAX] - F[TMAX - q])[np.abs(sl - fast) < 0.01].tolist()).most_common(3)
print('fast fronts: their last %d-tick displacement: %s' % (q, dq_fast))
fastk = np.flatnonzero(np.abs(sl - fast) < 0.01); conv = []
tt = np.arange(TMAX + 1)
for k in fastk:
    dev = np.abs(F[:, k] - F[TMAX, k] - fast * (tt - TMAX)); bad = np.flatnonzero(dev > 20)
    conv.append(int(bad[-1]) + 1 if len(bad) else 0)
conv = np.array(conv)
print('fast-at-end fronts: time from which the front stays within 20 cells of its final 2/9 line: '
      'quantiles 50/90/99/max = %s; later than %d: %d' % (np.percentile(conv, [50, 90, 99, 100]).astype(int).tolist(), T1,
                                                           int((conv > T1).sum())))
# slow speeds as exact rationals over the late window
print('slow late displacements over %d ticks: %s' % (TMAX - T1, Counter((F[TMAX, slow] - F[T1, slow]).tolist()).most_common(8)))
