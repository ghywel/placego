#!/usr/bin/env python3
"""L1385 (Local, 2026-11-03): independent exact check (Python Fractions) of GC2475's nested plateaus.
Run: python3 tests/probes/mahler/nested_plateau_check.py SAMPLES

N1 the midpoint control: c = (a - B)/r^26 = 1/6 + S_5/2 at a = (T_5 + S_5)/2, 11/30 < c < 443/1200, v_5 = 275/729 > c,
   v_7 = 2315/6561 < c; the full words (4,11,6,5,5) and (4,11,6,5,7) fail and pass at a.
N2 for (f, h) in f = 5..8, h = 5..9: T_f < V_(f,h) < R_(f,h) < V_(f,h-1) < S_f; fixed points 81/211, 177147/443105,
   12550483683/31376865305 and S_(f+1) below T_f; the width V_(f,h-1) - R_(f,h) = p(1 - 2T_f - p)/(2(1 - p));
   the upper witness (4,11,6,f,h-1) has max tail V_(f,h-1); the periodic word's root (geometric series) is R_(f,h).
N3 Q = 97/243 = 2/5 - 1/1215.
N4 a finite sanity test (support, not proof): random finite gap words, (f, h) in {(5,5), (5,7), (6,5), (6,8)}, at the
   midpoint of (R_(f,h), V_(f,h-1)] and at V_(f,h-1): membership in W_(f,h) equals "max tail < a".
N5 the h = 4 control: the periodic word (4,11,6,f,4) violates "after 4, next >= 11" at its repeat boundary.
"""
import random
import sys
from fractions import Fraction as F

r = F(2, 3); third = F(1, 3)
B = (1 + r ** 4 + r ** 15 + r ** 21) / 3
T = lambda f: B + r ** (21 + f) / 3
S = lambda f: B / (1 - r ** (21 + f))
V = lambda f, h: T(f) + r ** (21 + f + h) / 3
R = lambda f, h: T(f) / (1 - r ** (21 + f + h))


def ones_of(gaps):
    pos = [0]
    for g in gaps:
        pos.append(pos[-1] + g)
    return pos


def maxtail(ones):
    return max(third * sum(r ** (k - j) for k in ones if k >= j) for j in ones)


a = (T(5) + S(5)) / 2
c = (a - B) / r ** 26
v5, v7 = (1 + r ** 5) / 3, (1 + r ** 7) / 3
print('N1 c = 1/6 + S_5/2: %s; 11/30 < c < 443/1200: %s; v_5 = 275/729 > c: %s; v_7 = 2315/6561 < c: %s; '
      '(4,11,6,5,5) max tail < a: %s; (4,11,6,5,7) max tail < a: %s' % (
          c == third / 2 + S(5) / 2, F(11, 30) < c < F(443, 1200), v5 == F(275, 729) and v5 > c, v7 == F(2315, 6561) and v7 < c,
          maxtail(ones_of([4, 11, 6, 5, 5])) < a, maxtail(ones_of([4, 11, 6, 5, 7])) < a))
fps = [third / (1 - r ** 5), (1 + r ** 4) / 3 / (1 - r ** 16), (1 + r ** 4 + r ** 15) / 3 / (1 - r ** 22)]
ok = True
for f in range(5, 9):
    for h in range(5, 10):
        p = r ** (21 + f + h)
        o = T(f) < V(f, h) < R(f, h) < V(f, h - 1) < S(f)
        o &= all(x < T(f) for x in fps) and S(f + 1) < T(f)
        o &= V(f, h - 1) - R(f, h) == p * (1 - 2 * T(f) - p) / (2 * (1 - p))
        o &= maxtail(ones_of([4, 11, 6, f, h - 1])) == V(f, h - 1)
        per = (1 + r ** 4 + r ** 15 + r ** 21 + r ** (21 + f)) / 3 / (1 - p)
        o &= per == R(f, h)
        ok &= o
print('N2 order, dominance, width, upper witness, periodic root for f = 5..8, h = 5..9: %s' % ok)
print('N3 Q = 97/243 = 2/5 - 1/1215: %s' % ((1 + r ** 4) / 3 == F(97, 243) == F(2, 5) - F(1, 1215)))


def in_W(gaps, f, h):
    for i, g in enumerate(gaps):
        if g <= 3:
            return False
        if i >= 1 and gaps[i - 1] == 4 and g <= 10:
            return False
        if i >= 2 and gaps[i - 2:i] == [4, 11] and g <= 5:
            return False
        if i >= 3 and gaps[i - 3:i] == [4, 11, 6] and g <= f - 1:
            return False
        if i >= 4 and gaps[i - 4:i] == [4, 11, 6, f] and g <= h - 1:
            return False
    return True


rng = random.Random(2475)
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
bad = tested = members = 0
for f, h in ((5, 5), (5, 7), (6, 5), (6, 8)):
    pool = [3, 4, 4, 4, 5, 6, 7, 11, 12, f - 1, f, f + 1, h - 1, h, h + 1, 15]
    for a in ((R(f, h) + V(f, h - 1)) / 2, V(f, h - 1)):
        for _ in range(NS):
            gaps = []
            for _ in range(rng.randint(1, 10)):
                if gaps and gaps[-1] == 4 and rng.random() < 0.7:
                    gaps.append(11)
                elif len(gaps) >= 2 and gaps[-2:] == [4, 11] and rng.random() < 0.7:
                    gaps.append(6)
                elif len(gaps) >= 3 and gaps[-3:] == [4, 11, 6] and rng.random() < 0.7:
                    gaps.append(f)
                else:
                    gaps.append(rng.choice(pool))
            m = in_W(gaps, f, h)
            members += m
            bad += m != (maxtail(ones_of(gaps)) < a)
            tested += 1
print('N4 random finite gap words: %d tested (%d in W), mismatches %d' % (tested, members, bad))
print('N5 h = 4: periodic (4,11,6,5,4) repeated twice is in L_5: %s (must be False)' % in_W([4, 11, 6, 5, 4, 4, 11, 6, 5, 4], 5, 0))
print('NESTED_DONE')
