#!/usr/bin/env python3
"""Exact closed-form certificate (all exponents at once) for: no distinct covering with lcm | q^a * prod_{p in P} p^(b_p).
Avoid the top t_p residues of every pure p-power family and the top t_M residues of every mixed family.
  PA = prod_p (1 - t_p/(p-1)) - t_M * Mix,   Mix = prod_p p/(p-1) - 1 - sum_p 1/(p-1)
  E[S|A] <= (c/PA) * ( sum_p q^-t_p/(p-1) + q^-t_M * Mix ),   c = q/(q-1)
Certificate if PA > 0 and E[S|A] <= (q-2)/(q-1).  Exact rational arithmetic.  Usage: closedform.py q p1,p2,...
"""
import sys, itertools
from fractions import Fraction as F
q = int(sys.argv[1]); P = [int(x) for x in sys.argv[2].split(',')]
c = F(q, q - 1); need = F(q - 2, q - 1)
Pi = F(1)
for p in P: Pi *= F(p, p - 1)
Mix = Pi - 1 - sum(F(1, p - 1) for p in P)
best = None
for ts in itertools.product(range(0, 6), repeat=len(P)):
    if any(t > p - 1 for t, p in zip(ts, P)):
        continue
    for tM in range(0, 5):
        PA = F(1)
        for t, p in zip(ts, P): PA *= (1 - F(t, p - 1))
        PA -= tM * Mix
        if PA <= 0: continue
        E = c / PA * (sum(F(1, q**t * (p - 1)) for t, p in zip(ts, P)) + Mix / q**tM)
        if best is None or E < best[0]:
            best = (E, ts, tM, PA)
E, ts, tM, PA = best
print(f"q={q} P={P}: best t_p={dict(zip(P, ts))} t_M={tM}: P(A)>={PA} E[S|A]<={E} = {float(E):.5f} "
      f"need<={need} -> {'CERTIFICATE' if E <= need else 'no certificate'}")
