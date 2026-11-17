#!/usr/bin/env python3
"""L1448 (Local, 2026-11-03): P-m. Does an inserted edge's front move along a minimal-time symmetry vector of its ring
background? Run: python3 tests/probes/wolfram/glide_census.py WORD BOUND_NUM BOUND_DEN [TMAX [LMAX2]]
The background is closed_set.py's: the ring orbit of WORD, E(t, x) = orb[(t + s) mod q][(t - x + r) mod N], alignment (r, s).
1. The symmetry lattice: every (T, d), 1 <= T <= q, |d| < N, with E(t + T, x + d) = E(t, x) everywhere (one alignment
   suffices: alignments are translates). Its minimal time T_min, and P-m's prediction: the largest leftward speed -d/T_min
   (d < 0 or d = 0) not above e660e4's bound BOUND_NUM/BOUND_DEN.
2. The inserted edge (background on x < 0, black at 0, white on x > 0) at every alignment, evolved together to TMAX. The
   left front F(t); its least lag L <= 2q with F(t + L) - F(t) constant over [TMAX/2, TMAX]; the speed -m/L.
"""
import sys
from collections import Counter
from fractions import Fraction

import numpy as np

WORD = sys.argv[1]; BOUND = Fraction(int(sys.argv[2]), int(sys.argv[3])); TMAX = int(sys.argv[4]) if len(sys.argv) > 4 else 3000
y = np.array([int(ch) for ch in WORD], dtype=np.uint8); N = len(y)
cst = lambda s: s ^ (np.roll(s, 1) | np.roll(s, 2))
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y):
    orb.append(cur.copy()); cur = cst(cur)
orb = np.array(orb); q = len(orb)
E = lambda x, t, r, s: orb[(t + s) % q][((t - x) + r) % N]
# 1. the lattice, from alignment (0, 0)
grid = lambda T, d: all(E(x + d, t + T, 0, 0) == E(x, t, 0, 0) for t in range(q) for x in range(N))
sym = [(T, d) for T in range(1, q + 1) for d in range(-(N - 1), N) if grid(T, d)]
Tmin = min(T for T, d in sym); dmin = sorted(d for T, d in sym if T == Tmin)
cands = sorted({Fraction(-d, Tmin) for d in range(-4 * N, N) if (d - dmin[0]) % N == 0 and Fraction(-d, Tmin) >= 0})
allowed = [v for v in cands if v <= BOUND]
pred = max(allowed) if allowed else None
print('%s: N=%d, q=%d; minimal-time symmetry T_min=%d with d = %s (mod %d); leftward minimal-time speeds <= 1: %s; bound %s; '
      'P-m predicts %s' % (WORD, N, q, Tmin, dmin, N, [str(v) for v in cands if v <= 1], BOUND, pred))
# 2. the inserted edge at every alignment
als = [(r, s) for r in range(N) for s in range(q)]
lo = -2 * TMAX - 10; hi = TMAX + 10; L = hi - lo; c = -lo  # exact on (lo + t + 1, hi - t - 1) at time t
X = np.zeros((len(als), L), dtype=np.uint8); Bg = np.zeros_like(X)
xs = np.arange(lo, hi)
for k, (r, s) in enumerate(als):
    Bg[k] = orb[s % q][((0 - xs) + r) % N]
    X[k] = Bg[k]; X[k, c] = 1; X[k, c + 1:] = 0
Fs = np.zeros((TMAX + 1, len(als)), dtype=np.int32)
for t in range(TMAX + 1):
    if t:
        n = np.zeros_like(X); n[:, 1:-1] = X[:, :-2] ^ (X[:, 1:-1] | X[:, 2:]); X = n
        m = np.zeros_like(Bg); m[:, 1:-1] = Bg[:, :-2] ^ (Bg[:, 1:-1] | Bg[:, 2:]); Bg = m
    D = X ^ Bg
    assert D.any(axis=1).all()
    Fs[t] = D.argmax(axis=1) - c
    assert (Fs[t] < hi - t - 1).all(), 'the front is outside the exact range'
assert Fs[TMAX].min() > lo + TMAX + 1, 'truncation reached the front'
# background row check where exact (x from lo + TMAX + 2 to -1)
for k in (0, len(als) - 1):
    r, s = als[k]
    assert all(int(Bg[k, c + x]) == int(E(x, TMAX, r, s)) for x in range(lo + TMAX + 2, 0)), 'background row drifted'
res = Counter(); nonper = 0
h = TMAX // 2
for k in range(len(als)):
    f = Fs[h:, k].astype(np.int64); found = None
    for Lg in range(1, 2 * q + 1):
        d = f[Lg:] - f[:-Lg]
        if (d == d[0]).all():
            found = (Lg, int(d[0])); break
    if found is None:
        nonper += 1
    else:
        Lg, m_ = found; res[(str(Fraction(-m_, Lg)), (Lg, m_))] += 1
print('inserted edge at all %d alignments, TMAX=%d: exactly periodic over [%d, %d] with lag <= %d: %d; not: %d' % (
    len(als), TMAX, h, TMAX, 2 * q, len(als) - nonper, nonper))
print('  (speed, (least lag, displacement)): count -- %s' % sorted(res.items(), key=lambda kv: -kv[1])[:10])
LMAX2 = int(sys.argv[5]) if len(sys.argv) > 5 else 0
if nonper and LMAX2:
    res2 = Counter(); still = []
    for k in range(len(als)):
        f = Fs[h:, k].astype(np.int64)
        if any((f[Lg:] - f[:-Lg] == (f[Lg:] - f[:-Lg])[0]).all() for Lg in range(1, 2 * q + 1)):
            continue
        found = None
        for Lg in range(2 * q + 1, LMAX2 + 1):
            d = f[Lg:] - f[:-Lg]
            if (d == d[0]).all():
                found = (Lg, int(d[0])); break
        if found:
            res2[(str(Fraction(-found[1], found[0])), found)] += 1
        else:
            still.append(k)
    print('  the not-periodic ones, lags up to %d: %s; still not periodic: %d' % (LMAX2, sorted(res2.items(), key=lambda kv: -kv[1])[:8], len(still)))
    sl = (Fs[TMAX, still].astype(np.int64) - Fs[h, still]) / (TMAX - h)
    print('  their late slopes (rounded): %s' % Counter(np.round(sl, 3).tolist()).most_common(8))
# alignment classes by speed: is the speed a function of the insertion's background phase?
cls = {}
for k, (r, s) in enumerate(als):
    f = Fs[h:, k].astype(np.int64); sp = None
    for Lg in range(1, 2 * q + 1):
        d = f[Lg:] - f[:-Lg]
        if (d == d[0]).all():
            sp = str(Fraction(-int(d[0]), Lg)); break
    key = tuple(int(E(x, 0, r, s)) for x in range(-6, 1))  # the background cells x = -6 .. 0 at insertion
    cls.setdefault(key, Counter())[sp] += 1
mixed = sum(1 for v in cls.values() if len(v) > 1)
print('  background word on [-6, 0] at insertion: %d distinct; words whose alignments all share one outcome: %d; mixed: %d' % (
    len(cls), len(cls) - mixed, mixed))
ok = all(Fraction(sp) == pred for (sp, _), n in res.items()) and nonper == 0
print('P-m (every alignment at the predicted speed %s): %s' % (pred, 'HELD' if ok else 'FAILED'))
print('GLIDE_CENSUS_DONE')
