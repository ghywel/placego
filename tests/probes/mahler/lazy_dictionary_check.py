#!/usr/bin/env python3
"""L1386 (Local, 2026-11-03): exact spot checks of GC2476's reflected dictionary. Run: python3 lazy_dictionary_check.py

D1 H(G(x)) = L(H(x)) for all x = k/N in [0, 1) with N = 2310 (includes x = 0 and x = 2/3), with G(x) = 3x/2 - floor(3x/2),
   H(x) = 1 - x, L(y) = (3y + 1)/2 on (0, 1/3], (3y - 1)/2 on (1/3, 1]; the reflected digit is 1 - floor(3x/2).
D2 the beta' forced by the all-ones itinerary of 1: sum_k beta'^(-k) = 1 gives beta' = 2.
D3 the sign symmetry F(-1 - n) = -1 - F(n) for F(n) = ceil(3n/2), n in [-500, 500], with complementary parities.
D4 on finite gap words of L_5 (GC2473 examples), the strict ceiling translates: every U_j < a iff every L^j(1 - 2U_0) > 1 - 2a,
   at a = midpoint of (S_5, T_4].
"""
import math
from fractions import Fraction as F

N = 2310
G = lambda x: F(3, 2) * x - math.floor(F(3, 2) * x)
H = lambda x: 1 - x
L = lambda y: (3 * y + 1) / 2 if y <= F(1, 3) else (3 * y - 1) / 2
ok1 = all(H(G(F(k, N))) == L(H(F(k, N))) and (0 if H(F(k, N)) <= F(1, 3) else 1) == 1 - math.floor(F(3, 2) * F(k, N))
          for k in range(N))
print('D1 H(G(x)) = L(H(x)) and digit complement on %d rationals in [0, 1): %s' % (N, ok1))
print('D2 all-ones itinerary: 1/(beta - 1) = 1 at beta = 2: %s' % (F(1, 2 - 1) == 1))
Fn = lambda n: -((-3 * n) // 2)                      # ceil(3n/2)
print('D3 F(-1-n) = -1-F(n) and parity complement on [-500, 500]: %s' % all(
    Fn(-1 - n) == -1 - Fn(n) and (-1 - n) % 2 == 1 - n % 2 for n in range(-500, 501)))
r = F(2, 3); third = F(1, 3)
B = (1 + r ** 4 + r ** 15 + r ** 21) / 3
T = lambda f: B + r ** (21 + f) / 3
S = lambda f: B / (1 - r ** (21 + f))
a = (S(5) + T(4)) / 2


def tails(gaps, extra=60):
    pos = [0]
    for g in gaps:
        pos.append(pos[-1] + g)
    n = pos[-1] + 1
    return [third * sum(r ** (k - j) for k in pos if k >= j) for j in range(n)]


bad = 0
for gaps in ([4, 11, 6, 5], [4, 11, 6, 4], [5, 4, 11, 6, 5, 4, 12], [4, 11, 7, 4, 11, 6, 5], [3, 5], [4, 10, 6]):
    U = tails(gaps)
    y = 1 - 2 * U[0]
    ys = [y]
    for _ in range(len(U) - 1):
        ys.append(L(ys[-1]))
    lhs = all(u < a for u in U)
    rhs = all(v > 1 - 2 * a for v in ys)
    bad += (lhs != rhs) or any(ys[j] != 1 - 2 * U[j] for j in range(len(U)))
print('D4 reflected orbit equals 1 - 2U_j and the strict ceiling translates on 6 words: mismatches %d' % bad)
print('LAZY_DONE')
