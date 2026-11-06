#!/usr/bin/env python3
"""S-03's numbers, replayed by brute force before any Lean is trusted.

Prediction, written before the run: for every n in range, with P(n) = #{f in F_2^n : Theta f (2n + 1) = 1}:
(a) #{f : C_n(f) != C_(n-1)(shift f)} = 2^(n-2) + P(n-2), for n >= 2;
(b) the number of rows of width at most 2n black at every even tick through 2n is 2^n - P(n), counted over all rows;
(c) 4 E(n) + 24 E(n-2) >= 2^(n-2) for n >= 4, with E(n) = min(P(n), 2^n - P(n));
(d) in every triple from n >= 2 at least two have 2^n <= 40 E(n).
Counterfactual: any failure means the carried statement and the code read the definitions differently. Stop before Lean.
"""
import sys
sys.path.insert(0, sys.argv[1]); import ref
NMAX = int(sys.argv[2])
def theta_all(f, k):
    return ref.theta(f, k)
def C(bits, n):
    """Theta f (2n + 1) for the word bits, white past its end"""
    f = lambda s: bits[s] if s < len(bits) else 0
    return (ref.theta(f, 2 * n + 1) >> (2 * n)) & 1
P = {}
Q = {}
for n in range(0, NMAX + 1):
    p = q = 0
    for v in range(1 << n):
        b = [(v >> i) & 1 for i in range(n)]
        c = C(b, n); p += c
        if n >= 1: q += c ^ C(b[1:], n - 1)
    P[n] = p; Q[n] = q
    print('n', n, 'P', p, 'Q', q, flush=True)
bad = 0
for n in range(2, NMAX + 1):
    if Q[n] != 2 ** (n - 2) + P[n - 2]: bad += 1; print('pair law fails at', n)
def F(y): return (y >> 1) ^ (y | (y << 1))
for n in range(1, min(NMAX, 11) + 1):
    W = 2 * n; cnt = 0
    for y in range(1 << W):
        z = y; ok = True
        for t in range(0, 2 * n + 1):
            if t % 2 == 0 and not z & 1: ok = False; break
            z = F(z)
        cnt += ok
    if cnt != 2 ** n - P[n]: bad += 1; print('count fails at', n, cnt)
E = {n: min(P[n], 2 ** n - P[n]) for n in P}
for n in range(4, NMAX + 1):
    if 4 * E[n] + 24 * E[n - 2] < 2 ** (n - 2): bad += 1; print('distance two fails', n)
for n in range(2, NMAX - 1):
    good = sum(2 ** k <= 40 * E[k] for k in (n, n + 1, n + 2))
    if good < 2: bad += 1; print('triple fails', n)
print('E/2^n', [round(E[n] / 2 ** n, 4) for n in sorted(E)])
print('failures', bad)
