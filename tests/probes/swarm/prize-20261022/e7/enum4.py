#!/usr/bin/env python3
"""Enumerate every set S of odd primes (|S| <= 4, primes < 400) with prod p/(p-1) > 2 (otherwise the union bound
already rules out a covering) and test the exact closed-form certificate with q = 3 (3 in S) ."""
import itertools, time
from fractions import Fraction as F
t0 = time.time()
pr = [p for p in range(3, 400) if all(p % k for k in range(2, int(p**.5) + 1))]
def cert(P):
    q = 3; c = F(3, 2)
    Pi = F(1)
    for p in P: Pi *= F(p, p - 1)
    Mix = Pi - 1 - sum(F(1, p - 1) for p in P)
    best = None
    for ts in itertools.product(range(0, 5), repeat=len(P)):
        if any(t > p - 1 for t, p in zip(ts, P)): continue
        base = F(1)
        for t, p in zip(ts, P): base *= (1 - F(t, p - 1))
        for tM in range(0, 4):
            PA = base - tM * Mix
            if PA <= 0: continue
            E = c / PA * (sum(F(1, 3**t * (p - 1)) for t, p in zip(ts, P)) + Mix / 3**tM)
            if best is None or E < best: best = E
    return best
nontriv = []; fails = []
for k in (1, 2, 3, 4):
    for S in itertools.combinations(pr, k):
        Pi = F(1)
        for p in S: Pi *= F(p, p - 1)
        if Pi <= 2: continue
        nontriv.append(S)
        if 3 not in S:
            fails.append((S, 'no 3 in S')); continue
        E = cert([p for p in S if p != 3])
        if E is None or E > F(1, 2): fails.append((S, float(E) if E else None))
    if time.time() - t0 > 400: print("time cap"); break
print(f"nontrivial sets (|S|<=4, primes<400): {len(nontriv)}; without certificate: {len(fails)}")
for f in fails: print("  ", f)
