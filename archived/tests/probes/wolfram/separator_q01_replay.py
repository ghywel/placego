#!/usr/bin/env python3
"""separator_q01_replay.py (Local, Block 7, S-04): the plain-Python replay of the essay's worked-numbers cell.
Prints the list the notebook's first Output cell must equal:
  [death tick of 272125, death tick of 11083, number of (d, t) with t + d <= 15 checked for the peel chart on 11083,
   whether all of them agree, number of distinct layer words of length k = 1..6].
Conventions are the kit's: bit i of a natural is depth i + 1, F Y = (Y >> 1) ^ (Y | (Y << 1)); encodePair (a, b) = 2a + b;
phi and boundary as in Rule30WedgeBridge; the alternating column is black at the even ticks."""
from functools import lru_cache

def F(y): return (y >> 1) ^ (y | (y << 1))

def death(y, cap=400):
    t = 0
    while t <= cap:
        if y & 1 == 0: return t
        y = F(F(y)); t += 2
    return None

def phi(a, b):
    if a == 0: return {0: 0, 1: 1, 2: 3, 3: 2}[b]
    if a == 2: return {0: 3, 1: 2, 2: 0, 3: 1}[b]
    return {0: 3, 1: 2, 2: 1, 3: 0}[b]

def boundary(q): return 3 - q

def chart_check(y, S):
    rows = [y]
    for _ in range(2 * S + 2 * S + 8): rows.append(F(rows[-1]))
    def zrow(t, k): return 0 if k == 0 else (rows[t] >> (k - 1)) & 1
    def zpair(t, k): return 2 * zrow(t, k) + zrow(t, k + 1)
    def e(j): return zpair(2 * j + 1, 1)
    @lru_cache(maxsize=None)
    def cone(t, j):
        if t == 0: return boundary(e(j))
        if t == 1: return phi(e(j), boundary(e(j + 1)))
        return phi(cone(t - 2, j + 1), cone(t - 1, j + 1))
    @lru_cache(maxsize=None)
    def peelpow(d, t):
        if d == 0: return cone(t, 0)
        return phi(peelpow(d - 1, t), peelpow(d - 1, t + 1))
    pairs = [(d, t) for d in range(S + 1) for t in range(S + 1 - d)]
    return len(pairs), all(peelpow(d, t) == zpair(t, 2 * d + t + 2) for d, t in pairs)

def layer_words(k):
    words = set()
    for x0 in (0, 1):
        for r in range(1 << (2 * k)):
            col, w = x0, []
            for t in range(2 * k):
                col = (1 if t % 2 == 0 else 0) ^ (col | ((r >> t) & 1))
                if t % 2 == 0: w.append(col)  # col is now the value at tick t + 1, odd: a white tick
            words.add(tuple(w))
    return len(words)

n, ok = chart_check(11083, 15)
print([death(272125), death(11083), n, ok, [layer_words(k) for k in range(1, 7)]])
