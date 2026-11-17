#!/usr/bin/env python3
"""L1409 (Local, 2026-11-03): exact checks for the carrying read of GC2507 (finite bounds on the six R1 window
omissions). Run: python3 tests/probes/mahler/window_omission_check.py

For each listed word w: the strict suffix predicate and S_w < 1/2 (class membership), S_w and T_w against the table,
P_w(g) > 0 at the rational g (so gamma_w < g), Q_n = 1 - 60/n <= 2 T_w and n >= L, and the exact rational comparison
n g^L (2g/3)^n < ceiling. Also the true root gamma_w by Fraction bisection, and the bound with it.
"""
from fractions import Fraction as Fr

r = Fr(2, 3)
rows = [('10000', 100, Fr(4, 3), Fr(1, 250), Fr(81, 211), Fr(97, 243)),
        ('1000', 200, Fr(7, 5), Fr(1, 1000), Fr(27, 65), Fr(35, 81)),
        ('1001000', 400, Fr(29, 20), Fr(1, 125), Fr(945, 2059), Fr(1009, 2187)),
        ('100', 800, Fr(22, 15), Fr(1, 20000), Fr(9, 19), Fr(13, 27)),
        ('100', 1600, Fr(22, 15), Fr(1, 500000000000), Fr(9, 19), Fr(13, 27)),
        ('101000000', 3200, Fr(373, 250), Fr(1, 200), Fr(9477, 19171), Fr(9733, 19683))]


def P(w, t):
    L = len(w)
    return t ** L - sum(t ** (L - j - 1) for j in range(L) if w[j]) - 1


allok = True
for ws, n, g, ceil, S_tab, T_tab in rows:
    w = [int(c) for c in ws]
    L = len(w)
    strict = all(w[i:] < w[:L - i] for i in range(1, L))
    A = sum(r ** j for j in range(L) if w[j]) / 3
    S = A / (1 - r ** L); T = A + r ** (L - 1) / 3
    lo, hi = Fr(1), Fr(3, 2)
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if P(w, mid) < 0 else (lo, mid)
    Q = 1 - Fr(60, n)
    bound_g = n * g ** L * (2 * g / 3) ** n
    bound_gamma = n * hi ** L * (2 * hi / 3) ** n
    ok = strict and S < Fr(1, 2) and S == S_tab and T == T_tab and P(w, g) > 0 and Q <= 2 * T and n >= L and bound_g < ceil
    allok &= ok
    print('%-9s n=%4d: strict %s, S<1/2 %s, S,T match %s, P(g)=%s>0 %s, gamma in (%.6f, %.6f) < g=%s, Q=%s <= 2T=%s %s; '
          'n g^L (2g/3)^n = %.3e < %s %s; with gamma: %.3e' % (
              ws, n, strict, S < Fr(1, 2), S == S_tab and T == T_tab, P(w, g), P(w, g) > 0, float(lo), float(hi), g, Q,
              2 * T, Q <= 2 * T, float(bound_g), ceil, bound_g < ceil, float(bound_gamma)))
print('ALL SIX CASES PASS' if allok else 'A CASE FAILS')
print('cutoff margin at n = 1600: 2T - Q = %s' % (Fr(26, 27) - Fr(77, 80)))
print('WINDOW_OMISSION_DONE')
