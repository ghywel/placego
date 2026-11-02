#!/usr/bin/env python3
"""L1308 T30 (Local, 2026-11-02): replay of the period-1024 light-speed phase that refutes the cycle lemma.
reports/rule30-genealogy.md section 35. Run: python3 tests/probes/phase1024.py

The ring (phase1024_ring.txt, 1024 cells, cell i = character i) was found by rotators_g.c as a cycle of the forward
register y_n = y_(n-21) ^ (y_(n-1) | y_(n-2)). Checked here, independently of how it was found:
- c(y)_i = y_i ^ (y_(i-1) | y_(i-2)) equals y_(i-21) for every i (c is rotation by 21 on this ring);
- the ring is primitive, and its least period under c is 1024;
- every column (time series of one cell over one period) has least period 1024 and odd weight, so tau-adic valuation 0;
  the cycle lemma needs a column of valuation L/2 - 1 = 255 (P = 2L = 1024);
- its twisted depth period: C_(K+1)(t) = C_K(t + s) for the s printed.
"""
import os
here = os.path.dirname(os.path.abspath(__file__))
ring = [int(ch) for ch in open(os.path.join(here, 'phase1024_ring.txt')).read().strip()]
N = len(ring)
step = lambda z: [z[i] ^ (z[i - 1] | z[i - 2]) for i in range(N)]
cy = step(ring)
print('cells %d, weight %d' % (N, sum(ring)))
print('c(y)_i = y_(i-21) for every i:', all(cy[i] == ring[(i - 21) % N] for i in range(N)))
print('primitive (no rotation k < N fixes the ring):', all(ring != ring[k:] + ring[:k] for k in range(1, N) if N % k == 0))
z = ring[:]; hist = [z]; P = 0
for t in range(1, 2 * N + 1):
    z = step(z)
    if z == ring:
        P = t; break
    hist.append(z)
print('least period under c:', P)
M = (1 << P) - 1


def integ(d):
    y, s = d, 1
    while s < P:
        y ^= (y << s) & M; s <<= 1
    return (y << 1) & M


def val(c):
    k = 0
    while c:
        if bin(c).count('1') & 1:
            return k
        c = integ(c); k += 1
    return P


def lp(x):
    q = 1
    while q < P and (((x >> q) | (x << (P - q))) & M) != x:
        q *= 2
    return q


cols = [sum(hist[t][i] << t for t in range(P)) for i in range(N)]
vals = set(val(c) for c in cols); lps = set(lp(c) for c in cols); wts = set(bin(c).count('1') % 2 for c in cols)
print('column valuations %s, column least periods %s, column weight parities %s' % (sorted(vals), sorted(lps), sorted(wts)))
print('cycle lemma (some column of valuation %d): %s' % (P // 4 - 1, 'holds' if (P // 4 - 1) in vals else 'FAILS'))
rot = lambda c, s: ((c >> s) | (c << (P - s))) & M
ss = [s for s in range(P) if all(cols[(k + 1) % N] == rot(cols[k], s) for k in range(N))]
print('twisted depth period 1: C_(K+1)(t) = C_K(t + s) for s =', ss)
