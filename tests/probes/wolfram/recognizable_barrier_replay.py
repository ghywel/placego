#!/usr/bin/env python3
"""recognizable_barrier_replay.py (Local, 10 November 2026; S-19, Cloud's K-06 with K-01): the plain-Python replay of
the worked-numbers cell of the recognizable-barrier essay. Usage: python3 recognizable_barrier_replay.py

The zero-boundary left half: depth k >= 1, a white wall at depth 0, and one tick
x(k, t+1) = x(k+1, t) xor (x(k, t) or x(k-1, t)). A finite row is the natural number Y with bit i at depth i + 1,
so one tick is F(Y) = (Y >> 1) xor (Y | (Y << 1)) and a double step is G = F o F. Written independently of the
Lean module (no shared code).

Prediction (written before the first run, from the S-19 build report): the rows 1493 and 1507 first reach an even
value at the fifteenth iterate of G; among odd rows of bit length L = 1..12 the largest first-even index is
1, 3, 2, 3, 4, 5, 6, 5, 9, 7, 15, 8, attained at L = 11 by 1493 and 1507 only; and for every odd n from 5 to 41
and every j with 1 <= j and 4 j <= n, the row trunc n after j double steps has width n + 2 j and, read from its
edge, is a word of length 4 j - 1 that depends only on j, followed by (01)^k with k = (n + 1 - 2 j) / 2.
Counterfactual: a mismatch refutes the rider's computation or the essay's description of the decomposition.
It prints {first even index of 1493, of 1507, the maxima by bit length, the maximizers at length 11,
the decomposition holds}."""


def F(y):
    return (y >> 1) ^ (y | (y << 1))


def first_even(y, cap=400):
    for s in range(cap):
        if y % 2 == 0:
            return s
        y = F(F(y))
    raise SystemExit('no even iterate within the cap')


def tick(row):
    """row[k] is depth k; row[0] is the wall, always white."""
    ext = row + [0, 0]
    return [0] + [ext[k + 1] ^ (ext[k] | ext[k - 1]) for k in range(1, len(row) + 1)]


def iterate(n, j):
    row = [0] + [k % 2 for k in range(1, n + 1)] + [0] * (2 * j + 2)
    for _ in range(2 * j):
        row = tick(row)
    return row


maxima, arg11 = [], []
for L in range(1, 13):
    vals = {y: first_even(y) for y in range(1 << (L - 1), 1 << L) if y % 2 == 1}
    m = max(vals.values())
    maxima.append(m)
    if L == 11:
        arg11 = sorted(y for y, v in vals.items() if v == m)

ok, prefix = True, {}
for n in range(5, 42, 2):
    for j in range(1, n // 4 + 1):
        row = iterate(n, j)
        W = n + 2 * j
        ok &= row[W] == 1 and not any(row[W + 1:])
        edge = [row[W - i] for i in range(W)]
        k = (n + 1 - 2 * j) // 2
        ok &= edge[len(edge) - 2 * k:] == [0, 1] * k and len(edge) - 2 * k == 4 * j - 1
        ok &= prefix.setdefault(j, edge[:4 * j - 1]) == edge[:4 * j - 1]
print('{%d, %d, {%s}, {%s}, %s}' % (first_even(1493), first_even(1507), ', '.join(map(str, maxima)),
                                    ', '.join(map(str, arg11)), ok))
