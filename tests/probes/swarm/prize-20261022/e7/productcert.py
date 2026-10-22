#!/usr/bin/env python3
"""Product-structured certificate (q=3, all exponents).  A = prod_p A_p, A_p = y_p avoids the top t_p residues of
every pure p-power family (depends on y mod p^b only); mixed families are not avoided.  Because A is a product
event and a family depends only on its own primes' coordinates:
  E[F_e | A] <= E[F_e] / prod_{p | e} P(A_p),  P(A_p) >= P_p := 1 - t_p/(p-1).
Pure p-family (Lemma 2):  sum_j (3/2) 3^-t_p / p^j / P_p = (3/2) 3^-t_p / ((p-1) P_p).
Mixed: (3/2) * [prod_p (1 + u_p) - 1 - sum_p u_p],  u_p = 1/((p-1) P_p).
Certificate iff E[S|A] <= 1/2.  Exact rationals.  Usage: productcert.py p1,p2,...
"""
import sys, itertools
from fractions import Fraction as F
P = [int(x) for x in sys.argv[1].split(',')]
best = None
for ts in itertools.product(range(0, 6), repeat=len(P)):
    if any(t >= p - 1 for t, p in zip(ts, P)): continue
    Pp = [1 - F(t, p - 1) for t, p in zip(ts, P)]
    u = [1 / ((p - 1) * pp) for p, pp in zip(P, Pp)]
    pure = sum(F(3, 2) / 3**t * uu for t, uu in zip(ts, u))
    prod = F(1)
    for uu in u: prod *= (1 + uu)
    mixed = F(3, 2) * (prod - 1 - sum(u))
    E = pure + mixed
    if best is None or E < best[0]: best = (E, ts, Pp)
E, ts, Pp = best
print(f"P={P}: t_p={dict(zip(P, ts))} E[S|A] <= {E} = {float(E):.5f} -> {'CERTIFICATE' if E <= F(1,2) else 'no certificate'}")
