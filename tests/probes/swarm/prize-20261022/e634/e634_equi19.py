#!/usr/bin/env python3
"""Equilateral ABC, 120-degree tile with commensurable sides (primitive Eisenstein triple a,b,c), prime N:
L^2 = N*a*b with L integer forces {a,b} = {N x^2, y^2}.  Search primitive triples with a*b = N*square.
Prediction: none for N = 19 (quartic y^4 + 19x^2y^2 + 361x^4 = c^2 looks like a rank-0 curve).
Counterfactual: any triple found means the commensurable equilateral case for 19 needs more than arithmetic."""
import math, time
T0 = time.time()
MMAX = 2500
found = {}
primes = [p for p in range(7, 200) if all(p % q for q in range(2, int(p**0.5) + 1)) and p % 4 == 3]
for m in range(2, MMAX):
    if time.time() - T0 > 480: print("time limit at m =", m); break
    for n in range(1, m):
        if (m - n) % 3 == 0 or math.gcd(m, n) != 1: continue
        a, b = m * m - n * n, 2 * m * n + n * n
        ab = a * b
        for p in primes:
            if ab % p == 0:
                q = ab // p
                r = math.isqrt(q)
                if r * r == q:
                    found.setdefault(p, []).append((a, b, m * m + m * n + n * n))
print(f"searched m < {MMAX} (c up to ~{MMAX*MMAX*3//2}) in {time.time()-T0:.1f}s")
for p in primes:
    print(f"  N={p}: {len(found.get(p, []))} triples with ab = N*square; first: {found.get(p, [])[:3]}")
