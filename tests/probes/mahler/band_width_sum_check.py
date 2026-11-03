#!/usr/bin/env python3
"""L1398 (Local, 2026-11-03): numerical support for GC2496's total band width 1/6, and the Parry density bounds.
Run: python3 tests/probes/mahler/band_width_sum_check.py LMAX

W1 partial sums of T_w - S_w over all words w in W (start 1, end 0, strict suffix predicate on the complement, S_w < 1/2)
   of length L <= LMAX, in floating point; the sum must stay below 1/6 and approach it. W1x is a heuristic tail only:
   it fits the last length's contribution to c / L^2 and adds c * (sum over L > LMAX of 1 / L^2). It is not evidence for
   the identity, whose proof is GC2496's.
W2 Parry density of the greedy beta = 3/2 map: h(x) = sum over n >= 0 of beta^(-n) [x < T^n(1)], with T^0(1) = 1,
   T^1(1) = 1/2, ...: 1 <= h <= 3 everywhere (checked on a grid with 60 exact orbit terms).
W3 direct sampling of the null-set claim: 20,000 random ceilings a in (1/3, 1/2) (exact rationals with denominator 2^40):
   the fraction whose G-orbit of X = 2a escapes above X within 200 steps (outside E by the carried criterion), and the
   escape-time quantiles. Leb(E) = 0 predicts a fraction tending to 1.
"""
import random
from fractions import Fraction as Fr
import sys

LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 16
r = 2 / 3
total = 0.0
rows = []
for L in range(2, LMAX + 1):
    sub = 0.0; count = 0
    for v in range(1 << (L - 2)):
        w = [1] + [(v >> i) & 1 for i in range(L - 2)] + [0]
        s = [1 - x for x in w]
        ok = True
        for i in range(1, L):
            if not s[i:] > s[:L - i]:
                ok = False; break
        if not ok:
            continue
        A = sum(r ** j for j in range(L) if w[j]) / 3
        S = A / (1 - r ** L); T = A + r ** (L - 1) / 3
        if S < 0.5:
            sub += T - S; count += 1
    total += sub
    rows.append((L, count, sub, total))
for L, c, sub, tot in rows:
    if L <= 6 or L % 2 == 0:
        print('W1 L=%2d: %5d words, widths %.3e, cumulative %.10f (1/6 - cumulative = %.3e)' % (L, c, sub, tot, 1 / 6 - tot))
for L, c, sub, tot in rows[-3:]:
    print('W1x L=%2d: L^2 * widths = %.4f' % (L, L * L * sub))
cfit = LMAX * LMAX * rows[-1][2]
tail = cfit * sum(1 / (L * L) for L in range(LMAX + 1, 10 ** 6))
print('W1x heuristic c/L^2 tail beyond L=%d: %.4f; cumulative + tail = %.4f (1/6 = %.4f)' % (LMAX, tail, total + tail, 1 / 6))
orbit = [Fr(1)]
x = Fr(1)
for _ in range(60):
    y = 3 * x / 2; x = y - (y.numerator // y.denominator); orbit.append(x)
assert all(t > 0 for t in orbit), 'the orbit of 1 reached 0'
hmin, hmax = 10.0, 0.0
for k in range(1, 2000):
    h = sum((1.5 ** -n) for n, t in enumerate(orbit) if Fr(k, 2000) < t)
    hmin, hmax = min(hmin, h), max(hmax, h)
print('W2 Parry density on a grid: min %.4f, max %.4f (bounds 1 and 3)' % (hmin, hmax))
rng = random.Random(2496)
esc = 0; times = []
for _ in range(20000):
    a = Fr(1, 3) + Fr(rng.getrandbits(40), 2 ** 40) * (Fr(1, 2) - Fr(1, 3))
    X = 2 * a; x = X
    for n in range(1, 201):
        y = 3 * x / 2; x = y - (y.numerator // y.denominator)
        if x > X:
            esc += 1; times.append(n); break
times.sort()
print('W3 random ceilings in (1/3, 1/2): escaped within 200 steps %d of 20000 (%.4f); escape time median %d, 99%% %d, max %d' % (
    esc, esc / 20000, times[len(times) // 2], times[int(0.99 * len(times))], times[-1]))
print('BAND_SUM_DONE')
