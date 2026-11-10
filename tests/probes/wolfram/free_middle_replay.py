#!/usr/bin/env python3
"""free_middle_replay.py (Local, 10 November 2026; S-13): the plain-Python replay of the worked-numbers cell of the
free-middle essay. Usage: python3 free_middle_replay.py

Prediction (written before the first run): (a) the four-step rise summed over all cyclic words is 0 for popcount at
N = 9 and for the count of 11 at N = 10 (balance, `wsum_rho`); (b) in a row with the stripe on 12 depths, mu + 2
periods of a best popcount word d of length 9 and a black top cell, the four-step popcount change grows by exactly
the cyclic rise of d read from its deep end at each step of mu (`rise_mkRow`'s slope). Counterfactual: a nonzero
total, or increments that differ from that rise, means the orientation or the balance argument is misread.

Cyclic words are read left to right, rule 30 is new_i = x_(i-1) xor (x_i or x_(i+1)) on the cycle. A row is listed by
depth 1..W (depth 0 is the white wall); it evolves by new_k = old_(k+1) xor (old_k or old_(k-1)). It prints
{{total, max, positive, negative} for popcount at 9, the same for the count of 11 at 10, the best popcount word, its
rise read from the deep end, the four-step popcount changes for mu = 0..6}. The notebook's first Output cell must
equal this list."""
from itertools import product


def cstep(x):
    n = len(x)
    return [x[(i - 1) % n] ^ (x[i] | x[(i + 1) % n]) for i in range(n)]


def rise(x, h, m):
    n, y = len(x), list(x)
    for _ in range(4):
        y = cstep(y)
    win = lambda z, i: tuple(z[(i + j) % n] for j in range(m))
    return sum(h(win(y, i)) for i in range(n)) - sum(h(win(list(x), i)) for i in range(n))


def stats(N, h, m):
    r = [rise(list(x), h, m) for x in product((0, 1), repeat=N)]
    return [sum(r), max(r), sum(1 for v in r if v > 0), sum(1 for v in r if v < 0)]


pop = lambda w: w[0]
c11 = lambda w: 1 if w == (1, 1) else 0
A, B = stats(9, pop, 1), stats(10, c11, 2)
# the best popcount word, as a depth word d: depth k carries d[k mod 9]; read from the deep end it is reversed
words = [list(x) for x in product((0, 1), repeat=9)]
best = max(words, key=lambda d: (rise(d[::-1], pop, 1), d))
rho = rise(best[::-1], pop, 1)


def zstep(s):
    # s[0] is the wall; s has room for one more depth
    s = s + [0]
    return [0] + [s[k + 1] ^ (s[k] | s[k - 1]) for k in range(1, len(s) - 1)] + [s[-1] ^ (s[-1] | s[-2])]


def row(D, mu, d):
    N = len(d)
    Q = (mu + 2) * N
    W = D + Q + 1
    s = [0] * (W + 1)
    for k in range(1, W + 1):
        s[k] = (k % 2) if k <= D else (d[k % N] if k <= D + Q else 1)
    return s


def zstep2(s):
    t = s + [0, 0]
    return [0] + [t[k + 1] ^ (t[k] | t[k - 1]) for k in range(1, len(t) - 1)]


changes = []
for mu in range(7):
    s = row(12, mu, best)
    t = s
    for _ in range(4):
        t = zstep2(t)
    changes.append(sum(t[1:]) - sum(s[1:]))
out = [A, B, best, rho, changes]


def wl(x):
    return '{' + ', '.join(wl(y) for y in x) + '}' if isinstance(x, list) else str(x)


print(wl(out))
assert A[0] == 0 and B[0] == 0
assert all(changes[i + 1] - changes[i] == rho for i in range(6)), (rho, changes)
