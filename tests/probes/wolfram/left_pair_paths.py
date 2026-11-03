#!/usr/bin/env python3
"""L1480/L1481 (Local, 2026-11-03): the F2 pair map on P-periodic words, and rule 30's left diagonals as its paths.
Run: python3 tests/probes/wolfram/left_pair_paths.py PMAX [T]

Words are P-periodic functions of t mod P, packed as ints (bit k = the value at t = k mod P). For b != 0 the recurrence
x(t + 1) = a(t) xor (b(t) or x(t)) has exactly one P-periodic solution x = child(a, b) (start at a black r of b:
x(r + 1) = not a(r)), and T(a, b) = (b, child(a, b)) is a bijection from {b != 0} onto {a != 0} (a = x(t+1) xor (b or x)).
So its components are exactly 2^P - 1 paths, from the starts (0, y) to the ends (a, 0), and cycles; 4^P - 1 states.

1. For P = 1 .. PMAX: the exact decomposition, the path lengths in states (mean, coefficient of variation, min, max),
   and the cycle states.
2. Rule 30's left diagonals D j (t) = cell (t, j - t) of the single seed, to T ticks, by the kit's D_step in closed form,
   checked against a direct simulation for small T. Their eventual periods on [T/2, T) are compared with OEIS A363345.
3. After each eventually white diagonal w, the actual tails (D j, D (j + 1)), j = w ... the next white, are checked to be
   exactly the T_P path from (0, tail of D (w + 1)), and its length (states) is compared with the gap.
Prints counts only.
"""
import sys
from statistics import mean, pstdev

import numpy as np

PMAX = int(sys.argv[1]); TT = int(sys.argv[2]) if len(sys.argv) > 2 else 1 << 16


def child(a, b, P):
    r = next(k for k in range(P) if b >> k & 1)
    x = {}
    x[(r + 1) % P] = 1 - (a >> r & 1)
    for i in range(1, P):
        k = (r + i) % P
        x[(k + 1) % P] = (a >> k & 1) ^ ((b >> k & 1) | x[k])
    assert x[(r + 1) % P] == 1 - (a >> r & 1)
    return sum(x[k] << k for k in range(P))


def decompose(P):
    N = 1 << P; seen = set(); lengths = []; ends = {}
    for y in range(1, N):
        st = (0, y); n = 1; seen.add(st)
        while st[1] != 0:
            st = (st[1], child(st[0], st[1], P)); n += 1
            assert st not in seen, 'a path revisits a state'
            seen.add(st)
        lengths.append(n); ends[y] = (n, st)
    total = N * N - 1
    return lengths, total - len(seen), ends


print('== 1. the pair map T_P: exact path/cycle decomposition')
summary = {}
for P in range(1, PMAX + 1):
    L, cyc, ends = decompose(P)
    assert len(L) == (1 << P) - 1
    mu = mean(L); cv = pstdev(L) / mu
    summary[P] = (L, ends)
    print('P=%2d: states %d, paths %d, cycle states %d (%.1f%%), path states: mean %.1f (bound 2^P+1 = %d), cv %.3f, min %d, max %d'
          % (P, (1 << 2 * P) - 1, len(L), cyc, 100.0 * cyc / ((1 << 2 * P) - 1), mu, (1 << P) + 1, cv, min(L), max(L)))


# 2. the left diagonals by D_step in closed form
def next_diag(a, b):
    """x(0) = 0, x(t+1) = a(t) xor (b(t) or x(t)), vectorized: x(t) = 1 xor par(a[r..t-1]) after the last black r < t."""
    T = len(a)
    par = np.zeros(T + 1, dtype=np.uint8); par[1:] = np.cumsum(a, dtype=np.int64) % 2
    idx = np.where(b == 1, np.arange(T), -1); last = np.maximum.accumulate(idx)
    x = np.zeros(T, dtype=np.uint8)
    rt = last[:-1]; t = np.arange(1, T)
    x[1:] = np.where(rt >= 0, 1 ^ par[t] ^ par[np.clip(rt, 0, None)], par[t])
    return x


def diagonals(J, T):
    D = [np.ones(T, dtype=np.uint8), np.ones(T, dtype=np.uint8)]
    D[1][0] = 0
    for j in range(J - 1):
        D.append(next_diag(D[j], D[j + 1]))
    return D


# check against a direct simulation of rule 30 for small T
Ts = 300; ca = np.zeros((Ts, 2 * Ts + 1), dtype=np.uint8); ca[0, Ts] = 1
for t in range(1, Ts):
    p = ca[t - 1]; ca[t, 1:-1] = p[:-2] ^ (p[1:-1] | p[2:])
Dsmall = diagonals(120, Ts)
assert all(int(Dsmall[j][t]) == int(ca[t, Ts + j - t]) for j in range(120) for t in range(Ts)), 'closed form differs'
print('== 2. D_step closed form equals direct simulation on j < 120, t < %d' % Ts)

J = 402; T = TT
D = diagonals(J, T)
lo = T // 2


def evper(v):
    for p in (1, 2, 4, 8, 16, 32):
        if np.array_equal(v[lo + p:], v[lo:T - p]):
            return p
    return None


per = [evper(D[j]) for j in range(J)]
assert all(p is not None for p in per), 'a diagonal is not periodic on [T/2, T) with period <= 32'
A363345 = [1, 1, 1, 2, 1, 2, 2, 1, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 1, 8, 1, 8, 8, 8, 8, 8, 8, 8, 8, 8,
           8, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4, 8, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
           8, 4, 8, 8, 8, 8, 8]
print('eventual periods on [T/2, T), T = %d: equal to OEIS A363345 (offset 1) for its %d listed terms: %s' % (
    T, len(A363345), per[:len(A363345)] == A363345))
white = [j for j in range(J) if per[j] == 1 and not D[j][lo:].any()]
black = [j for j in range(J) if per[j] == 1 and D[j][lo:].all()]
print('eventually white, j < %d: %s; eventually black: %s' % (J, white, black))
first = {}
for j, p in enumerate(per):
    first.setdefault(p, j)
print('first diagonal of each period: %s (A364239 offset 1: 1, 4, 9, 30, 401)' % sorted(first.items()))

print('== 3. the left side between whites as T_P paths')
tail = lambda v, P: sum(int(v[lo + k]) << ((lo + k) % P) for k in range(P))
for w, w2 in zip(white, white[1:]):
    P = per[w + 1]
    st = (tail(D[w], P), tail(D[w + 1], P)); n = 1; j = w; match = True
    while st[1] != 0:
        st = (st[1], child(st[0], st[1], P)); n += 1; j += 1
        match &= st == (tail(D[j], P), tail(D[j + 1], P)) and all(per[i] <= P for i in (j, j + 1))
    pct = ''
    if P in summary:
        L = summary[P][0]; pct = '; its rank among the %d paths: %.1f%% are shorter' % (len(L), 100.0 * sum(x < n for x in L) / len(L))
    print('white %d -> %d: P = %d, path states %d, gap %d, tails match the path: %s; mean path %.1f, bound %d%s' % (
        w, w2, P, n, w2 - w, match, mean(summary[P][0]) if P in summary else float('nan'), (1 << P) + 1, pct))
# after the last white below J, follow the path at its period to its end (the next white), without diagonals
w = white[-1]; P = per[w + 1]
st = (tail(D[w], P), tail(D[w + 1], P)); n = 1
while st[1] != 0 and n < 10 ** 7:
    st = (st[1], child(st[0], st[1], P)); n += 1
print('white %d: P = %d, the path from (0, tail D(%d)) has %d states, so the next white is j = %d (A364239: first period %d at offset-1 index 87868)'
      % (w, P, w + 1, n, w + n, 2 * P))
print('LEFT_PAIR_PATHS_DONE')
