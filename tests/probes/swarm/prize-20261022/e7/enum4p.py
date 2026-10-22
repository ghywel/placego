#!/usr/bin/env python3
"""Re-enumerate all nontrivial odd prime sets with |S| <= 4 (primes < 400) using the product certificate;
then scan {3,5,7,11,s} and {3,5,7,13,s} for 5-prime boundary."""
import itertools, time
from fractions import Fraction as F
t0 = time.time()
pr = [p for p in range(3, 400) if all(p % k for k in range(2, int(p**.5) + 1))]
def pcert(P):
    best = None
    for ts in itertools.product(range(0, 5), repeat=len(P)):
        if any(t >= p - 1 for t, p in zip(ts, P)): continue
        u = [1 / ((p - 1) * (1 - F(t, p - 1))) for t, p in zip(ts, P)]
        prod = F(1)
        for uu in u: prod *= (1 + uu)
        E = sum(F(3, 2) / 3**t * uu for t, uu in zip(ts, u)) + F(3, 2) * (prod - 1 - sum(u))
        if best is None or E < best: best = E
    return best
cnt = 0; fails = []
for k in (1, 2, 3, 4):
    for S in itertools.combinations(pr, k):
        Pi = F(1)
        for p in S: Pi *= F(p, p - 1)
        if Pi <= 2: continue
        cnt += 1
        if 3 not in S: fails.append(S); continue
        if pcert([p for p in S if p != 3]) > F(1, 2): fails.append(S)
print(f"|S|<=4 nontrivial: {cnt}; failing product certificate: {fails}  ({time.time()-t0:.0f}s)")
for base in ([5, 7, 11], [5, 7, 13]):
    ok = [s for s in pr if s > base[-1] and s < 200 and pcert(base + [s]) <= F(1, 2)]
    print(f"{{3,{','.join(map(str, base))},s}} certified for s in {ok[:5]}... first={ok[0] if ok else None}")
