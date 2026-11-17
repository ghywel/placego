#!/usr/bin/env python3
"""L1482 (Local, 2026-11-03): carrying checks for GC2596's alignment contract on the pinned G16 literal.
Run: python3 tests/probes/wolfram/g16_alignment_check.py KMAX KALL
1. The literal RING16 of upward_rigid.py (128 cells) satisfies c(y) = rho^72 y for the frame rule
   c(y)_n = y_n xor (y_(n-1) or y_(n-2)), and returns after 16 steps (and not before); it is not 64-periodic.
2. The alignment identity on the literal: E_(i,a)(j, t) = orb[(t + a) % 16][(j + i) % 128] equals E_(i - 72a, 0)(j, t)
   for all 128 x 16 alignments, all j < 128 and t < 16.
3. The episode law M(k), k = 1 .. KMAX, by phase_episode.py's exact method (all 2^(k+1) prefixes behind the black edge,
   horizon 3k + 72), over the 128 representatives at a = 0 for k <= KMAX, and over all 2,048 (i, a) for k <= KALL, where
   every alignment's longest episode must equal its representative's; the maxima equal CL676's table 8 8 9 11 12 13 13 16 17 19 19 21 21 22. A literal-pinned replay, not a new census.
Prints counts only.
"""
import os
import sys

import numpy as np

KMAX = int(sys.argv[1]); KALL = int(sys.argv[2])
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, '..', 'upward_rigid.py')).read()
lit = src.split('RING16 = (', 1)[1].split(')', 1)[0]
ring = ''.join(part.strip().strip("'") for part in lit.split('\n'))
y = np.array([1 if ch == '#' else 0 for ch in ring], dtype=np.uint8)
N = len(y); ok = True


def report(name, cond):
    global ok
    ok &= bool(cond)
    print('%s: %s' % (name, 'PASS' if cond else 'FAIL'))


cst = lambda s: s ^ (np.roll(s, 1) | np.roll(s, 2))
report('1. literal: %d cells, c(y) = rho^72 y' % N, N == 128 and np.array_equal(cst(y), np.roll(y, 72)))
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y):
    orb.append(cur.copy()); cur = cst(cur)
orb = np.array(orb)
report('1. frame period %d (16 expected); not 64-periodic' % len(orb), len(orb) == 16 and not np.array_equal(y, np.roll(y, 64)))
q = 16
E = lambda i, a: orb[((np.arange(q) + a) % q)[:, None], ((np.arange(N) + i) % N)[None, :]]
report('2. E_(i,a) = E_(i - 72a, 0) for all 2,048 alignments', all(np.array_equal(E(i, a), E((i - 72 * a) % N, 0))
                                                                  for i in range(N) for a in range(q)))
CL676 = [8, 8, 9, 11, 12, 13, 13, 16, 17, 19, 19, 21, 21, 22]


def traces(k, H):
    n = 1 << (k + 1); rr = np.arange(n, dtype=np.int64)
    X = np.zeros((k + 2, n), dtype=np.uint8); X[0] = 1
    for j in range(1, k + 2):
        X[j] = (rr >> (j - 1)) & 1
    a = np.empty((H, n), dtype=np.uint8); b = np.empty_like(a)
    for t in range(H):
        a[t], b[t] = X[k], X[k + 1]
        Y = X.copy(); Y[1] = X[1] ^ X[0]; Y[2:] = X[2:] ^ (X[1:-1] | X[:-2]); X = Y
    return a, b


Ms0, Msall = [], []
for k in range(1, KMAX + 1):
    H = 3 * k + 3 * q + 24
    a, b = traces(k, H)
    best = {}
    for (i, s) in [(i, s) for i in range(N) for s in (range(q) if k <= KALL else (0,))]:
        ek = orb[(np.arange(H) + s) % q, (k + i) % N]; ek1 = orb[(np.arange(H) + s) % q, (k + 1 + i) % N]
        agree = (a == ek[:, None]) & (b == ek1[:, None])
        ff = np.where(agree.all(axis=0), H, agree.argmin(axis=0))
        best[(i, s)] = int(ff.max())
    Ms0.append(max(best[(i, 0)] for i in range(N)))
    if k <= KALL:
        Msall.append(max(best.values()))
        ok &= all(best[(i, s)] == best[((i - 72 * s) % N, 0)] for i in range(N) for s in range(q))
print('3. M(k) over the 128 representatives at a = 0: %s' % ' '.join(map(str, Ms0)))
print('   M(k) over all 2,048 alignments (k <= %d):     %s' % (KALL, ' '.join(map(str, Msall))))
report('3. per-alignment longest episodes equal their representative\'s, and both maxima equal CL676\'s table',
       Ms0 == CL676[:KMAX] and Msall == CL676[:KALL])
print('ALL PASS' if ok else 'SOME FAIL')
