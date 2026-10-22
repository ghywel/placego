#!/usr/bin/env python3
"""Numeric test of Lemma A and its quantitative form on the five known unitary perfect numbers.
For every subset S of the odd components: E(S) = prod_{q in S} q^(e_q - c_q(S)) where c_q(S) = sum_{r in S} v_q(r^e_r+1).
Claim: E(S) > 2^(|S|-1), with exact rational arithmetic, and seed reachability holds."""
from fractions import Fraction
from itertools import combinations
known = {6: (1, {3: 1}), 60: (2, {3: 1, 5: 1}), 90: (1, {3: 2, 5: 1}), 87360: (6, {3: 1, 5: 1, 7: 1, 13: 1}),
         146361946186458562560000: (18, {3: 1, 5: 4, 7: 1, 11: 1, 13: 1, 19: 1, 37: 1, 79: 1, 109: 1, 157: 1, 313: 1})}
def v(q, n):
    c = 0
    while n % q == 0:
        n //= q; c += 1
    return c
allok = True
for N, (a, P) in known.items():
    # sigma* check
    s = 2 ** a + 1
    for p, e in P.items():
        s *= p ** e + 1
    assert s == 2 * N, N
    # reachability from seed
    reach = {q for q in P if (2 ** a + 1) % q == 0}
    changed = True
    while changed:
        changed = False
        for r in list(reach):
            for q in P:
                if q not in reach and (r ** P[r] + 1) % q == 0:
                    reach.add(q); changed = True
    primes = list(P)
    worst = None
    cnt = 0
    for k in range(1, len(primes) + 1):
        for S in combinations(primes, k):
            E = Fraction(1)
            for q in S:
                cq = sum(v(q, r ** P[r] + 1) for r in S)
                E *= Fraction(q) ** (P[q] - cq)
            ratio = E / Fraction(2) ** (k - 1)
            cnt += 1
            if worst is None or ratio < worst[0]:
                worst = (ratio, S)
            if not ratio > 1:
                allok = False
                print("VIOLATION", N, S, E)
    print(f"N={N}: a={a}, seed-reachable={reach == set(P)}, subsets={cnt}, min E(S)/2^(|S|-1) = {float(worst[0]):.4f} at S={worst[1]}")
print("all subsets satisfy E(S) > 2^(|S|-1):", allok)
