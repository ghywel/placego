#!/usr/bin/env python3
"""L1384 (Local, 2026-11-03): independent exact check (Python Fractions) of GC2473's plateau cascade.
Run: python3 tests/probes/mahler/plateau_cascade_check.py SAMPLES

C1 forbidden costs above T_4: 35/81, (1 + r^4 + r^14)/3, (1 + r^4 + r^15 + r^20)/3, and the two factored differences.
C2 fixed points 81/211, Q/(1 - r^16), P/(1 - r^22) as stated and below 2/5; S_f above B.
C3 the width T_(f-1) - S_f = q (1 - 2B - q) / (2 (1 - q)) for f = 5..12.
C4 a finite sanity test (support, not proof): random finite gap words (gaps from a pool rich in 4, 11, 6, f - 1, f, f + 1)
   at ceilings a = the midpoint of (S_f, T_(f-1)] and a = T_(f-1), f = 5, 6, 7: membership in L_f equals "max tail < a".
C5 the right limit: a terminal 4,11,6 word has max tail exactly B; an L_old word sample stays below 2/5.
"""
import random
import sys
from fractions import Fraction as F

r = F(2, 3); third = F(1, 3)
B = (1 + r ** 4 + r ** 15 + r ** 21) / 3
T = lambda f: B + r ** (21 + f) / 3
S = lambda f: B / (1 - r ** (21 + f))
Q = (1 + r ** 4) / 3; P = (1 + r ** 4 + r ** 15) / 3
c1 = [F(35, 81), (1 + r ** 4 + r ** 14) / 3, (1 + r ** 4 + r ** 15 + r ** 20) / 3]
print('C1 costs above T_4: %s; differences factor: %s %s' % (
    [c > T(4) for c in c1], c1[1] - T(4) == (r ** 14 / 3) * (1 - r - r ** 7 - r ** 11),
    c1[2] - T(4) == (r ** 20 / 3) * (1 - r - r ** 5)))
fps = [third / (1 - r ** 5), Q / (1 - r ** 16), P / (1 - r ** 22)]
print('C2 fixed points %s; equal to stated %s; below 2/5: %s; S_5..S_12 above B: %s' % (
    [str(x) for x in fps], fps == [F(81, 211), F(177147, 443105), F(12550483683, 31376865305)],
    [x < F(2, 5) for x in fps], all(S(f) > B for f in range(5, 13))))
print('C3 width formula f = 5..12: %s' % all(
    T(f - 1) - S(f) == r ** (21 + f) * (1 - 2 * B - r ** (21 + f)) / (2 * (1 - r ** (21 + f))) for f in range(5, 13)))


def ones_of(gaps):
    pos = [0]
    for g in gaps:
        pos.append(pos[-1] + g)
    return pos


def maxtail(ones):
    return max(third * sum(r ** (k - j) for k in ones if k >= j) for j in ones)


def in_L(gaps, f):
    for i, g in enumerate(gaps):
        if g <= 3:
            return False
        if i >= 1 and gaps[i - 1] == 4 and g <= 10:
            return False
        if i >= 2 and gaps[i - 2:i] == [4, 11] and g <= 5:
            return False
        if i >= 3 and gaps[i - 3:i] == [4, 11, 6] and g <= f - 1:
            return False
    return True


rng = random.Random(2473)
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
bad = 0; tested = 0; members = 0
for f in (5, 6, 7):
    pool = [1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 10, 11, 11, 11, 12, f - 1, f, f, f + 1, 15, 20]
    for a in ((S(f) + T(f - 1)) / 2, T(f - 1)):
        for _ in range(NS):
            k = rng.randint(1, 9)
            gaps = []
            for _ in range(k):                          # bias towards the trigger chain 4, 11, 6, ...
                if gaps and gaps[-1] == 4 and rng.random() < 0.6:
                    gaps.append(11)
                elif len(gaps) >= 2 and gaps[-2:] == [4, 11] and rng.random() < 0.6:
                    gaps.append(6)
                else:
                    gaps.append(rng.choice(pool))
            mem = in_L(gaps, f)
            members += mem
            bad += mem != (maxtail(ones_of(gaps)) < a)
            tested += 1
print('C4 random finite gap words: %d tested (%d in L_f), mismatches between L_f and max tail < a: %d' % (tested, members, bad))
print('C5 terminal 4,11,6 word max tail equals B: %s; sample L_old words below 2/5: %s' % (
    maxtail(ones_of([4, 11, 6])) == B,
    all(maxtail(ones_of(g)) < F(2, 5) for g in ([4, 11, 7], [4, 12], [5, 4, 11, 7, 4, 11, 7], [4, 11, 7] * 3))))
print('PLATEAU_DONE')
