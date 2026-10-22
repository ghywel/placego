#!/usr/bin/env python3
"""Per-family refinement of the closed-form certificate (all exponents).  Families d' <= D get individual t;
families d' > D keep the closed-form type rule (pure t_p / mixed t_M), their sums taken over smooth d' <= 1e13
plus a 1e-9 margin.  Bound per family: min(c q^-t, c q^-t/(d' PA)) (both valid).  q = 3."""
import sys, itertools
from fractions import Fraction as Fr
P = [int(x) for x in sys.argv[1].split(',')]; D = int(sys.argv[2]); tp0 = [int(x) for x in sys.argv[3].split(',')]; tM0 = int(sys.argv[4])
q = 3; c = 1.5
def smooth(lim):
    out = [1]
    for p in P:
        new = []
        for d in out:
            x = d
            while x <= lim: new.append(x); x *= p
        out = new
    return sorted(d for d in out if d > 1)
def kind(d):
    ps = [p for p in P if d % p == 0]
    return ps[0] if len(ps) == 1 else 'M'
fam = smooth(D); big = [d for d in smooth(10**13) if d > D]
tdef = {p: t for p, t in zip(P, tp0)}; tdef['M'] = tM0
tail_cost = {k: 0.0 for k in list(P) + ['M']}; tail_inv = {k: 0.0 for k in list(P) + ['M']}
for d in big:
    k = kind(d); tail_cost[k] += tdef[k] / d; tail_inv[k] += 1.0 / d
t = {d: min(tdef[kind(d)], d - 1) for d in fam}
def score(t):
    pure = {p: tail_cost[p] for p in P}; mixed = tail_cost['M']
    for d in fam:
        k = kind(d)
        if k == 'M': mixed += t[d] / d
        else: pure[k] += t[d] / d
    PA = 1.0
    for p in P:
        if pure[p] >= 1: return None
        PA *= 1 - pure[p]
    PA -= mixed
    if PA <= 0: return None
    E = 0.0
    for d in fam:
        b = c * q ** (-t[d]); E += min(b, b / (d * PA))
    for k in list(P) + ['M']:
        E += c * q ** (-tdef[k]) * tail_inv[k] / PA
    return E + 1e-9
cur = score(t); start = cur
improved = True
while improved:
    improved = False
    for d in fam:
        for dl in (1, -1):
            k2 = t[d] + dl
            if k2 < 0 or k2 > min(d - 1, 15): continue
            old = t[d]; t[d] = k2; s = score(t)
            if s is not None and s < cur - 1e-12: cur = s; improved = True
            else: t[d] = old
print(f"P={P} D={D} start(closed-form t)={start:.5f} refined E[S|A] <= {cur:.5f} -> {'CERTIFICATE' if cur <= 0.5 else 'no'}; "
      f"t for d'<=200: { {d: t[d] for d in fam if d <= 200} }")
