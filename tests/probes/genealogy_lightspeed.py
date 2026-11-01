#!/usr/bin/env python3
"""L1283 T5c (Local, 2026-11-01): forced deep words of light-speed (r, L) patterns, and whether the seed's left band
can host them. Prediction in reports/rule30-genealogy.md section 15, written first. Run: python3 tests/probes/genealogy_lightspeed.py
"""
from itertools import product
import numpy as np

N = 60


def Phi(w):
    w1 = np.concatenate(([0, 1], w))
    return w ^ (w1[1:-1] | w1[:-2])


def reads(w, pattern, nreads):
    """the global read sequence of deep word w under the periodic (r, L) pattern (deep-side law), first nreads."""
    out = []
    k = 0
    while len(out) < nreads and len(w) > 0:
        r, L = pattern[k % len(pattern)]
        u = w.copy()
        for _ in range(r):
            u = Phi(u)
        for j in range(min(L, len(u))):
            out.append(int(u[j]))
        w = Phi(u)[L:]
        k += 1
    return out[:nreads]


def target(pattern, n):
    y = []
    k = 0
    while len(y) < n:
        r, L = pattern[k % len(pattern)]
        y += [1] * (L - 1) + [0]
        k += 1
    return y[:n]


def forced(pattern):
    y = target(pattern, N)
    w = np.zeros(N + 2 * 64, dtype=np.uint8)     # spare digits so reads up to N are exact
    for j in range(N):
        got = reads(w, pattern, j + 1)
        if got[j] != y[j]:
            w[j] ^= 1
            assert reads(w, pattern, j + 1)[j] == y[j]
    return w[:N]


pats = []
for r, L in product(range(3), range(1, 7)):
    if L == 2 * (r + 1):
        pats.append(((r, L),))
for (r1, L1), (r2, L2) in product(product(range(3), range(1, 7)), repeat=2):
    if L1 + L2 == 2 * (r1 + r2 + 2) and (r1, L1) != (r2, L2):
        pats.append(((r1, L1), (r2, L2)))
# the seed's left band at late times: deep word behind a front at offset D from the left edge
T = 6100
W = 2 * T + 9
C = T + 4
row = np.zeros(W, dtype=np.uint8)
row[C] = 1
band = {}
for t in range(T):
    row = np.concatenate(([0], row[:-2] ^ (row[1:-1] | row[2:]), [0])).astype(np.uint8)
    if t + 1 >= T - 64:
        band[t + 1] = row[C - (t + 1): C - (t + 1) + 80].copy()   # offsets 0..79 from the left edge
results = []
for pat in pats:
    w = forced(pat)
    nz = np.flatnonzero(w)
    finite = nz.size == 0 or nz.max() < N - 20
    D0 = int(nz.max()) + 1 if nz.size else 0
    match = []
    if finite and D0 > 0:
        for t, b in band.items():
            # front at offset D0 must be black; digits w_j = band[D0 - j], j = 1..D0, top digit D0 = the edge
            if b[D0] == 1 and all(b[D0 - j] == w[j - 1] for j in range(1, D0 + 1)):
                match.append(t)
    results.append((pat, finite, D0, ''.join(map(str, w[:24])), len(match)))
for pat, finite, D0, head, m in results:
    print(f'pattern {pat}: forced word {head}... {"finite, length " + str(D0) if finite else "infinite (non-zero tail)"}'
          + (f'; matches the seed band (front black at offset {D0}) in {m} of {len(band)} late rows' if finite and D0 else ''))
print(f'{len(results)} light-speed patterns; finite forced words {sum(1 for x in results if x[1])}; '
      f'finite and matching the band in some late row {sum(1 for x in results if x[1] and x[4] > 0)}')
print('GENEALOGY_LIGHTSPEED_DONE')
