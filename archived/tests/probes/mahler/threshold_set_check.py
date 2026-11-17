#!/usr/bin/env python3
"""L1392 (Local, 2026-11-03): exact checks of GC2485/GC2487 (threshold criterion controls, spacing counts, the periodic
limit example). Run: python3 tests/probes/mahler/threshold_set_check.py

T1 the controls: a = 5/12 (X = 5/6) first escapes at n = 4 with v = 1/96; delta = 1/1200 satisfies (beta^4 + 1) delta < v
   and keeps the first four branches; flat interval [333/800, 1001/2400] inside the gap-4 band (27/65, 35/81];
   a = 1/3 and a = 13/27 never escape (in E), with 13/27's greedy code 101000...
T2 N_n (one-gaps >= g) satisfies N_n = N_(n-1) + N_(n-g) and N_n <= g lambda_g^n, n <= 40, g = 3..6, by direct count for
   n <= 20; lambda_g in (1, 3/2); beta_3 = 13/27.
T3 the GC2487 periodic-limit example: gap histories 3^n,4 (n = 1..12, finite) have every tail < 9/19, the supremum
   over n tends to 9/19, and 9/19 is the root of the periodic word 100.
"""
from fractions import Fraction as F
import itertools
import math

beta = F(3, 2); r = F(2, 3); third = F(1, 3)


def G(x):
    y = beta * x
    return y - math.floor(y)


def escape(X, n_max=200):
    x = X
    for n in range(1, n_max + 1):
        x = G(x)
        if x > X:
            return n, x - X
        if x == 0:
            return None
    return None


X = F(5, 6)
n, v = escape(X)
d = F(1, 1200)
orbit = [X]
for _ in range(4):
    orbit.append(G(orbit[-1]))
margins = all(abs(orbit[k] - F(2, 3)) > beta ** k * d and orbit[k] - beta ** k * d > 0 for k in range(4))
band = (third / (1 - r ** 4), (1 + r ** 3) / 3)
print('T1 a = 5/12: first escape n = %s, v = %s; (beta^4 + 1) delta < v: %s; branch margins: %s; flat [%s, %s]; gap-4 band (%s, %s]; inside: %s' % (
    n, v, (beta ** 4 + 1) * d < v, margins, F(5, 12) - d / 2, F(5, 12) + d / 2, band[0], band[1],
    band[0] < F(5, 12) - d / 2 and F(5, 12) + d / 2 <= band[1]))


def greedy(X, k):
    out, x = [], X
    for _ in range(k):
        dgt = 1 if beta * x >= 1 else 0
        out.append(dgt); x = beta * x - dgt
    return out


print('T1 a = 1/3: escape %s; a = 13/27: escape %s, greedy code %s' % (escape(F(2, 3)), escape(F(26, 27)), greedy(F(26, 27), 8)))
ok = True
for g in range(3, 7):
    lam_lo, lam_hi = 1.0, 1.5
    f = lambda x: x ** g - x ** (g - 1) - 1
    for _ in range(200):
        mid = (lam_lo + lam_hi) / 2
        lam_lo, lam_hi = (mid, lam_hi) if f(mid) < 0 else (lam_lo, mid)
    lam = lam_hi
    N = [n + 1 for n in range(g)]
    for n in range(g, 41):
        N.append(N[n - 1] + N[n - g])
    direct = [sum(1 for w in itertools.product((0, 1), repeat=n)
                  if all(j - i >= g for i, j in zip([p for p in range(n) if w[p]], [p for p in range(n) if w[p]][1:])))
              for n in range(0, 17)]
    ok &= direct == N[:17] and all(N[n] <= g * lam ** n + 1e-9 for n in range(41)) and 1 < lam < 1.5
print('T2 counts (direct to n = 16), bound N_n <= g lambda_g^n (to 40), 1 < lambda_g < 3/2, g = 3..6: %s; beta_3 = 13/27: %s' % (
    ok, (1 + r ** 2) / 3 == F(13, 27)))


def tails(gaps):
    pos = [0]
    for gp in gaps:
        pos.append(pos[-1] + gp)
    return [third * sum(r ** (k - j) for k in pos if k >= j) for j in pos]


hist = []
for n in range(1, 13):
    hist += [3] * n + [4]
t = tails(hist)
print('T3 gaps 3^n,4 (n = 1..12): max tail %.12f < 9/19 = %.12f: %s; periodic 100 root = 9/19: %s' % (
    float(max(t)), float(F(9, 19)), max(t) < F(9, 19), third / (1 - r ** 3) == F(9, 19)))
print('THRESHOLD_DONE')
