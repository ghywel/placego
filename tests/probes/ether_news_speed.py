#!/usr/bin/env python3
"""L1364 T55 (Local, 2026-11-03): how fast can any disturbance's left front invade the classic ether?
reports/rule30-genealogy.md section 59 (predictions written first). Run: python3 tests/probes/ether_news_speed.py W [W ...]

Upper bound: T54's rooted observer over the periodic background E(t, x) = ether(x mod 7, t mod 4) (every alignment is a
node), as a finite graph on (t mod 4, L mod 7, ternary window w of width W). One tick evaluates delta' by the exact
mismatch identity with E's values, three-valued, and branches on unknown cells from L - 1 to the new front; a scan past
the window gives edges to (L + W + 1 + i, unknown word), i = 0..6 (a larger jump of the same residue adds 7 and is
dominated). Edge weight: L' - L. Karp's minimum cycle mean mu_W bounds every actual front: L(t) - L(0) >= mu_W t - C,
so the leftward speed is at most max(0, -mu_W). A2's 7/12 is the control ceiling (v_W must not exceed it).
Lower end: actual fronts of random right halves (ether on x < 0 at each of the 28 alignments, random on 0 .. 3000,
white beyond) over 2000 ticks, and the inserted black edge (A1: speed 0) as a control.
"""
import random
import sys
from fractions import Fraction

import numpy as np

Ws = [int(a) for a in sys.argv[1:]] or [0, 1, 2, 3, 4]
TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
X = 2


def E(t, x):
    return TAB[x % 7][t % 4]


assert all(E(t + 1, x) == E(t, x - 1) ^ (E(t, x) | E(t, x + 1)) for t in range(4) for x in range(7))

TERN = {}
for dl in (0, 1, X):
    for dc in (0, 1, X):
        for dr in (0, 1, X):
            for c in (0, 1):
                for r in (0, 1):
                    vals = {a ^ ((1 - r) & b) ^ ((1 - c) & d) ^ (b & d)
                            for a in ((0, 1) if dl == X else (dl,))
                            for b in ((0, 1) if dc == X else (dc,))
                            for d in ((0, 1) if dr == X else (dr,))}
                    TERN[dl, dc, dr, c, r] = vals.pop() if len(vals) == 1 else X


def successors(t, L, w, W):
    """(L', w') successors of rooted (L, w) at time t, as in rooted_front.py, with the half-line exit unrolled."""
    d = {L - 2: 0, L - 1: 0, L: 1}
    for i, v in enumerate(w):
        d[L + 1 + i] = v
    get = lambda x: d.get(x, X)
    nd = {x: TERN[get(x - 1), get(x), get(x + 1), E(t, x), E(t, x + 1)] for x in range(L - 1, L + W + 1)}
    nget = lambda x: nd.get(x, X)
    out = []
    p = L - 1
    while True:
        if p > L + W:
            out += [(L + W + 1 + i, (X,) * W) for i in range(7)]
            return out
        v = nget(p)
        if v != 0:
            out.append((p, tuple(nget(p + 1 + i) for i in range(W))))
        if v == 1:
            return out
        p += 1


def words(W):
    if W == 0:
        return [()]
    return [w + (v,) for w in words(W - 1) for v in (0, 1, X)]


def min_cycle_mean(W):
    ws = words(W)
    idx = {(ph, j, w): k for k, (ph, j, w) in enumerate((ph, j, w) for ph in range(4) for j in range(7) for w in ws)}
    src, dst, wt = [], [], []
    for (ph, j, w), k in idx.items():
        for L2, w2 in successors(ph, j, w, W):
            src.append(k); dst.append(idx[(ph + 1) % 4, L2 % 7, w2]); wt.append(L2 - j)
    n = len(idx)
    src, dst, wt = np.array(src), np.array(dst), np.array(wt, dtype=np.int64)
    INF = 10 ** 15
    D = np.zeros((n + 1, n), dtype=np.int64)
    for k in range(1, n + 1):
        cand = D[k - 1][src] + wt
        row = np.full(n, INF, dtype=np.int64)
        np.minimum.at(row, dst, cand)
        D[k] = row
    best = None
    for v in range(n):
        if D[n][v] >= INF // 2:
            continue
        ks = [k for k in range(n) if D[k][v] < INF // 2]
        m = max(((D[n][v] - D[k][v]) / (n - k), k) for k in ks)
        if best is None or m[0] < best[0]:
            best = (m[0], v, m[1])
    _, v, k = best
    mu = Fraction(int(D[n][v] - D[k][v]), n - k)
    return mu, n, len(src)


for W in Ws:
    mu, n, m = min_cycle_mean(W)
    v = max(Fraction(0), -mu)
    print('W=%d: %d nodes, %d edges; minimum cycle mean %s; leftward speed bound %s (%.4f); A2 7/12 = 0.5833' % (
        W, n, m, mu, v, float(v)), flush=True)
    assert v <= Fraction(7, 12), 'bound above A2: bug alarm'

# Lower end: actual fronts.
rng = random.Random(55)
LO, HI, T = -4000, 3000, 2000
N = HI - LO + 1
mask = (1 << N) - 1


def ev_front(row_bits, ref_bits, c1):
    a, r = row_bits, ref_bits
    out = []
    for t in range(1, T + 1):
        a = ((a << 1) ^ (a | (a >> 1))) & mask
        r = ((r << 1) ^ (r | (r >> 1))) & mask
        if t % 500 == 0:
            d = (a ^ r) >> (t + 1) << (t + 1)           # drop the left-boundary garbage
            out.append((d & -d).bit_length() - 1 + LO if d else None)
    return out


speeds = []
for c0 in range(7):
    for c1 in range(4):
        ref = sum(TAB[(x + c0) % 7][c1] << (x - LO) for x in range(LO, HI + 1))
        edge = sum((TAB[(x + c0) % 7][c1] if x < 0 else int(x == 0)) << (x - LO) for x in range(LO, HI + 1))
        fe = ev_front(edge, ref, c1)
        rnd = sum((TAB[(x + c0) % 7][c1] if x < 0 else rng.getrandbits(1)) << (x - LO) for x in range(LO, HI + 1))
        fr = ev_front(rnd, ref, c1)
        speeds.append((-(fr[-1] - fr[0]) / (T - 500) if fr[-1] is not None and fr[0] is not None else None, c0, c1))
        print('(%d,%d) inserted edge fronts at t=500..2000: %s; random right half: %s' % (c0, c1, fe, fr), flush=True)
ok = [s for s in speeds if s[0] is not None]
print('random right halves: leftward speed over t = 500..2000: max %.4f, median %.4f' % (
    max(s[0] for s in ok), sorted(s[0] for s in ok)[len(ok) // 2]))
print('ETHER_NEWS_SPEED_DONE')
