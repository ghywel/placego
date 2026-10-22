#!/usr/bin/env python3
"""Finite-m certificate: no distinct covering with lcm | q^a * m for ANY a (m fixed, gcd(m, q) = 1).
Per-divisor avoidance t_d (avoid top t_d residues of family d), y uniform on Z/m:
  PA = prod_p (1 - sum_{j: p^j | m} t_{p^j}/p^j) - sum_{mixed d | m} t_d/d
  E[S|A] <= (c/PA) * sum_{d | m, d > 1} q^-t_d / d ,  c = q/(q-1);   certificate iff PA > 0 and E <= (q-2)/(q-1).
Coordinate descent in floats, final check in exact rationals.  Usage: finite_cert.py q p1^e1,p2^e2,...
"""
import sys
from fractions import Fraction as Fr
q = int(sys.argv[1]); fac = []
for part in sys.argv[2].split(','):
    p, e = (part.split('^') + ['1'])[:2]; fac.append((int(p), int(e)))
divs = [1]
for p, e in fac: divs = [d * p**k for d in divs for k in range(e + 1)]
divs = sorted(d for d in divs if d > 1)
primes = [p for p, _ in fac]
def pp(d):
    return [p for p in primes if d % p == 0]
def evalf(t, exact=False):
    one = Fr(1) if exact else 1.0
    PA = one
    for p in primes:
        s = sum(Fr(t[d], d) if exact else t[d] / d for d in divs if pp(d) == [p])
        if s > 1: return None, None
        PA *= (1 - s)
    PA -= sum(Fr(t[d], d) if exact else t[d] / d for d in divs if len(pp(d)) > 1)
    if PA <= 0: return None, None
    c = Fr(q, q - 1) if exact else q / (q - 1)
    E = c / PA * sum((Fr(1, q**t[d] * d) if exact else 1.0 / (q**t[d] * d)) for d in divs)
    return E, PA
need = (q - 2) / (q - 1)
best = None
import itertools, random
random.seed(7)
starts = [(a, b) for a in range(0, 4) for b in range(0, 4)]
for (t0, t1) in starts:
    t = {d: min(t0 if len(pp(d)) == 1 else t1, d - 1) for d in divs}
    cur, _ = evalf(t)
    if cur is None: cur = 1e9
    changed = True
    while changed:
        changed = False
        for d in divs:
            for dl in (1, -1):
                k = t[d] + dl
                if k < 0 or k > min(d - 1, 12): continue
                old = t[d]; t[d] = k
                v, _ = evalf(t)
                if v is not None and v < cur - 1e-13: cur = v; changed = True
                else: t[d] = old
    if best is None or cur < best[0]: best = (cur, dict(t))
E, PA = evalf(best[1], exact=True)
print(f"q={q} m={sys.argv[2]} divisors>1={len(divs)}: E[S|A] <= {float(E):.5f} (exact {E}) P(A) >= {float(PA):.4f} "
      f"need <= {need:.4f} -> {'CERTIFICATE' if E <= Fr(q-2, q-1) else 'no certificate'}; t = {best[1] if len(divs) <= 16 else '...'}")
