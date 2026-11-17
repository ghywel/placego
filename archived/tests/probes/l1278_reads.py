#!/usr/bin/env python3
"""L1278 (Local, 2026-11-01): independent replays behind two second reads, and how far from a cell
its parents are written.

Run: python3 tests/probes/l1278_reads.py   (about ten seconds; no solver, no files written)

(A) CL674's masking-envelope lemma, in Local's own code (Cloud's probe not imported). Frame: depth j
    reads j-1 and j-2, X_j' = X_j ^ (X_{j-1} | X_{j-2}), depth 0 held black, depth -1 white. For every
    alignment of the five backgrounds: R(t) <= U(t); R' <= R + 2; D_{R+2}(t+1) = NOT E_{R+1}(t) when
    R >= 0; and R' <= R + 1 when E_{R+1}(t) = 1. Then the envelope speeds and L_env(1..20).
(B) Convention: the witness's first disagreement time on the pair (k, k+1), maximised over alignments,
    reproduces CL673's W(1..18) for (12, 68), and T_env(k) <= that time at every alignment. PR69's
    L_env(k) = ceil(2(k+1)/3) for 2 <= k <= 40.
(C) GC2351 against G13. The right-to-left predecessor reader of Rule 30 (state = the two parent cells
    to the right; input = the child) is derived here from the rule. Its reset words, by brute force
    for every word up to length 14, are exactly those containing 0 1^(3k+1) 0 z (G13.2, PROOFS.md E.1).
    A white child run keeps {white parents, black parents} both possible: GPT's 00000/11111 collision.
(D) How far to the right of a cell its parents are written, on the single-seed orbit. d(i, t) is the
    least w such that the row at time t on [i, i+w] fixes the parent triple of (i, t) over every
    completion (the reader resets inside y[i+1..i+w]). Rows 1000..2000, cells i in [-t+2, t-2].

Prediction for (D), written before the first run: the median of d is at most 8 and the mean at most 12;
fewer than 1% of cells need d > 50. Counterfactual: if more than 10% need d > 50, Rule 30's own record of
parentage is effectively non-local and the owner's labels add substantial local information.
Record searched: record_find 'preimage', 'synchroniz', 'predecessor', 'ancestry', 'Garden of Eden',
'Welch', 'Hedlund'; known index kit f1cb20be (no hit for the joint terms). G13.1-G13.2 (the four-state
inverse-row reader and its reset language), G121 (full-line finite injectivity), the zero-wall
predecessor count at PROOFS.md GC2218 and the kit's Preimages module are the known tools.
"""
import re
from fractions import Fraction
from itertools import product

import numpy as np

# ---------- (A) the envelope lemma ----------
SEEDS = {'e4_8': '1000', 'c7_28': '1000000', 's7_63': '1010000', 's9_57': '100100000', 's12_68': '100100000000'}


def ring_orbit(w):
    s = [int(c) for c in w]
    p = len(s)
    orb = [tuple(s)]
    while True:
        s = [s[j] ^ (s[j - 1] | s[j - 2]) for j in range(p)]
        if tuple(s) == orb[0]:
            return p, orb
        orb.append(tuple(s))


def step(X):
    return [1, X[1] ^ X[0]] + [X[j] ^ (X[j - 1] | X[j - 2]) for j in range(2, len(X))]


def envelope_check(name, T):
    p, orb = ring_orbit(SEEDS[name])
    q = len(orb)
    J = 2 * T + 6
    viol = checks = 0
    Lenv = {}
    speeds = set()
    for r, s in product(range(p), range(q)):
        def E(j, t):
            return orb[(t + s) % q][(j + r) % p]

        def front(X, t):
            return max((j for j in range(J) if X[j] != E(j, t)), default=-1)

        X = [E(j, 0) for j in range(J)]
        X[0] = 1
        R, U = front(X, 0), 0
        for t in range(T):
            if R > U:
                viol += 1
            Y = step(X)
            R2 = front(Y, t + 1)
            if R2 > R + 2:
                viol += 1
            if R >= 0:
                checks += 1
                if (Y[R + 2] ^ E(R + 2, t + 1)) != 1 - E(R + 1, t):
                    viol += 1
                if E(R + 1, t) == 1 and R2 > R + 1:
                    viol += 1
            U = U + 2 if E(U + 1, t) == 0 else U + 1
            X, R = Y, R2
        U, t, seen, arr = 0, 0, {}, {}
        while (U % p, t % q) not in seen or len(arr) < 20:
            seen.setdefault((U % p, t % q), (U, t))
            U = U + 2 if E(U + 1, t) == 0 else U + 1
            t += 1
            for k in range(1, 21):
                if k not in arr and U >= k:
                    arr[k] = t
        U0, t0 = seen[(U % p, t % q)]
        speeds.add(Fraction(U - U0, t - t0))
        for k, v in arr.items():
            Lenv[k] = max(Lenv.get(k, 0), v)
    return viol, checks, speeds, [Lenv[k] for k in range(1, 21)]


CL674 = {'e4_8': '1 2 3 4 4 5 6 6 7 8 8 9 10 10 11 12 12 13 14 14',
         'c7_28': '1 2 3 4 4 5 6 6 7 8 9 9 10 10 11 12 12 13 13 14',
         's7_63': '1 2 3 4 5 6 7 8 8 9 10 11 11 12 13 14 15 16 17 17',
         's9_57': '1 2 3 4 5 6 6 7 8 9 9 10 11 11 12 13 14 14 15 16',
         's12_68': '1 2 3 4 5 6 7 8 9 10 11 12 12 13 14 15 16 17 17 18'}
print('(A) masking envelope, every alignment')
for nm in SEEDS:
    v, n, sp, L = envelope_check(nm, 60 if nm != 's12_68' else 40)
    same = ' '.join(map(str, L)) == CL674[nm]
    print(f'  {nm}: violations {v} over {n} front steps; envelope speed {sorted(map(str, sp))}; '
          f'L_env(1..20) equals CL674: {same}')
    assert v == 0 and same and len(sp) == 1

# ---------- (B) the time convention and PR69's closed form ----------
p, orb = ring_orbit(SEEDS['s12_68'])
q = len(orb)
T, J = 80, 166
W = [0] * 19
for r, s in product(range(p), range(q)):
    def E(j, t):
        return orb[(t + s) % q][(j + r) % p]
    X = [E(j, 0) for j in range(J)]
    X[0] = 1
    tau, tenv, U = {}, {}, 0
    for t in range(T + 1):
        for k in range(1, 19):
            if k not in tau and (X[k] != E(k, t) or X[k + 1] != E(k + 1, t)):
                tau[k] = t
            if k not in tenv and U >= k:
                tenv[k] = t
        X = step(X)
        U = U + 2 if E(U + 1, t) == 0 else U + 1
    for k in range(1, 19):
        assert tenv[k] <= tau[k]
        W[k] = max(W[k], tau[k])
assert W[1:] == [23, 24, 24, 26, 26, 28, 28, 32, 32, 35, 36, 36, 38, 38, 40, 40, 43, 45]
L69 = [int(x) for x in CL674['e4_8'].split()]
assert all(L69[k - 1] == -(-2 * (k + 1) // 3) for k in range(2, 21))
excess = sorted({(k % 3, L69[k - 1] + (2 * k // -3)) for k in range(3, 21)})
print('(B) W(1..18) for (12, 68) replayed as the first disagreement time of the pair (k, k+1): equals CL673;')
print(f'    T_env <= witness time at all 816 alignments; PR69 L_env = ceil(2(k+1)/3) for k >= 2; '
      f'excess over ceil(2k/3) by k mod 3: {excess}')

# ---------- (C) the predecessor reader and the parent labels ----------


def rule(a, b, c):
    return a ^ (b | c)


def reader(state, y):
    """state = (x_i, x_{i+1}) of the parent row; y = child at i; returns (x_{i-1}, x_i)."""
    a, b = state
    xm = [u for u in (0, 1) if rule(u, a, b) == y]
    assert len(xm) == 1          # left permutivity: exactly one left parent
    return (xm[0], a)


STATES = list(product((0, 1), repeat=2))


def image(S, word):
    for y in word:
        S = {reader(st, y) for st in S}
    return S


reset_re = re.compile(r'0(111)*10[01]')
for n in range(1, 15):
    for w in product((0, 1), repeat=n):
        resets = len(image(set(STATES), w)) == 1
        assert resets == bool(reset_re.search(''.join(map(str, w)))), w
assert image({(0, 0), (1, 1)}, (0,) * 40) == {(0, 0), (1, 1)}
assert {rule(0, 0, 0), rule(1, 1, 1)} == {0}
print('(C) reader derived from Rule 30; reset words = words containing 0 1^(3k+1) 0 z, every word to length 14;')
print('    a white child run leaves {white parents, black parents} open for its whole length (GC2351 collision)')

# ---------- (D) where the parents are written, single-seed orbit ----------
TMAX = 2000
N = 2 * TMAX + 5
row = np.zeros(N, dtype=np.uint8)
c0 = TMAX + 2
row[c0] = 1
ds, edge_only, rows_done = [], 0, 0
for t in range(1, TMAX + 1):
    prev = row
    row = np.zeros_like(prev)
    row[1:-1] = prev[:-2] ^ (prev[1:-1] | prev[2:])
    if t < 1000:
        continue
    y = row
    lo, hi = c0 - t + 2, c0 + t - 2           # interior cells
    # occurrences (row order) z,0,1^L,0 starting at p with L = 1 mod 3: end(p) = p + 2 + L
    ends = np.full(N + 1, 10 ** 9, dtype=np.int64)
    ones_run = np.zeros(N + 1, dtype=np.int64)
    for j in range(N - 1, -1, -1):
        ones_run[j] = ones_run[j + 1] + 1 if y[j] == 1 else 0
    for pp in range(lo, c0 + t + 1):
        if pp + 2 < N and y[pp + 1] == 0:
            L = ones_run[pp + 2]
            if L >= 1 and L % 3 == 1 and pp + 2 + L < N and y[pp + 2 + L] == 0 and pp + 2 + L <= c0 + t:
                ends[pp] = pp + 2 + L
    sufmin = np.minimum.accumulate(ends[::-1])[::-1]
    for i in range(lo, hi + 1):
        e = sufmin[i + 1]
        if e >= 10 ** 9:
            edge_only += 1
        else:
            ds.append(e - i)
    # independent spot check: the reader itself at 40 cells of this row
    if t % 250 == 0:
        for i in np.linspace(lo, hi, 40).astype(int):
            d = next((w for w in range(1, c0 + t - i + 1)
                      if len(image(set(STATES), [int(v) for v in y[i + w:i:-1]])) == 1), None)
            assert (d is None) == (sufmin[i + 1] >= 10 ** 9), (t, i)
            if d is not None:
                assert d == sufmin[i + 1] - i, (t, i)
    rows_done += 1
ds = np.array(ds)
print(f'(D) rows 1000..{TMAX}, {len(ds) + edge_only} interior cells: parents fixed by the row to the right within d cells')
print(f'    median {np.median(ds):.0f}, mean {ds.mean():.2f}, 90% {np.percentile(ds, 90):.0f}, 99% {np.percentile(ds, 99):.0f}, '
      f'99.9% {np.percentile(ds, 99.9):.0f}, max {ds.max()}; share d > 50: {(ds > 50).mean():.5f}; '
      f'no reset before the edge: {edge_only}')
for w in (4, 6, 8, 12, 20):
    print(f'    share of cells fixed within {w:2d} cells: {(ds <= w).mean():.4f}')
# control: independent fair coin rows of the same widths (seeded), same statistic
rng = np.random.default_rng(1278)
dc = []
for t in range(1000, TMAX + 1, 10):
    y = rng.integers(0, 2, size=2 * t + 1).astype(np.uint8)
    n = len(y)
    ones_run = np.zeros(n + 1, dtype=np.int64)
    for j in range(n - 1, -1, -1):
        ones_run[j] = ones_run[j + 1] + 1 if y[j] == 1 else 0
    ends = np.full(n + 1, 10 ** 9, dtype=np.int64)
    for pp in range(n - 2):
        if y[pp + 1] == 0:
            L = ones_run[pp + 2]
            if L >= 1 and L % 3 == 1 and pp + 2 + L < n and y[pp + 2 + L] == 0:
                ends[pp] = pp + 2 + L
    sufmin = np.minimum.accumulate(ends[::-1])[::-1]
    dc.extend(int(sufmin[i + 1] - i) for i in range(1, n - 100) if sufmin[i + 1] < 10 ** 9)
dc = np.array(dc)
print(f'    control, fair coin rows (every tenth width, {len(dc)} cells): median {np.median(dc):.0f}, mean {dc.mean():.2f}, '
      f'90% {np.percentile(dc, 90):.0f}, 99% {np.percentile(dc, 99):.0f}, max {dc.max()}; within 8: {(dc <= 8).mean():.4f}')
print('L1278_READS_DONE')
