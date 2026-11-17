#!/usr/bin/env python3
"""ether_cut_edge_replay.py (Local, 10 November 2026; S-11): the plain-Python replay of the worked-numbers cell of the
cut-ether essay. Usage: python3 ether_cut_edge_replay.py

Prediction (written before the first run): the nine-bit cycle of the single cell's edge code has 32 values without 129,
the thirteen-bit one 64; the cuts c7cut N for N = 0..5 all begin with the code 129; on actual rule 30 rows of c7cut N
(N = 0, 1, 2) for t <= 32, the edge code agrees with the single cell's at time 16 + t below bit 8 and differs at 8;
over the single cell's rows s <= 300, the longest flush agreement with the ether at any phase and position is 12 cells,
first at s = 55; and at s = 204 the cells at distances 7..19 are the ether at phase 2, position 1. Counterfactual: any
mismatch means the module's finite certificates or the edge reading are misread.

Rows are rule 30 on the whole line, new_p = x_(p-1) xor (x_p or x_(p+1)), computed on finite windows. It prints
{cycle 9, 129 in it, cycle 13, cut prefixes, frozen check, longest flush agreement, first time, row 204 check}."""


def T(c, nb):
    return (c ^ ((c << 1) | (c << 2))) & ((1 << nb) - 1)


def cycle(nb):
    seen, c = [], 1
    while True:
        seen.append(c)
        c = T(c, nb)
        if c == 1:
            return seen


def step(row):  # row: dict position -> 1 for black cells
    ps = set()
    for p in row:
        ps.update((p - 1, p, p + 1))
    g = lambda p: row.get(p, 0)
    return {p: 1 for p in ps if g(p - 1) ^ (g(p) | g(p + 1))}


def c7(p):
    return 1 if (p + 1) % 7 == 0 else 0


def cut(N):
    return {p: 1 for p in range(-(7 * N + 1), 7 * N + 7) if c7(p)}


def code(row, e, n):
    return sum(row.get(e - k, 0) << k for k in range(n))


c9, c13 = cycle(9), cycle(13)
prefixes = [code(cut(N), 7 * N + 6, 9) for N in range(6)]
seeds = [{0: 1}]
for _ in range(320):
    seeds.append(step(seeds[-1]))
frozen = True
for N in (0, 1, 2):
    row = cut(N)
    for t in range(33):
        a, b = code(row, 7 * N + 6 + t, 9), code(seeds[16 + t], 16 + t, 9)
        frozen = frozen and (a % 256 == b % 256) and ((a >> 8) & 1) != ((b >> 8) & 1)
        row = step(row)
ether = [{p: c7(p) for p in range(7)}]
for _ in range(3):
    r = ether[-1]
    ether.append({p: r[(p - 1) % 7] ^ (r[p] | r[(p + 1) % 7]) for p in range(7)})
best, first = 0, -1
for s in range(301):
    cs = [seeds[s].get(s - j, 0) for j in range(13)]
    for a in range(4):
        for p in range(7):
            L = 0
            while L < 13 and cs[L] == ether[a][(p - L) % 7]:
                L += 1
            if L > best:
                best, first = L, s
row204 = all(seeds[204].get(204 - 7 - j, 0) == ether[2][(1 - j) % 7] for j in range(13))
out = [len(c9), 129 in c9, len(c13), prefixes, frozen, best, first, row204]


def wl(x):
    if isinstance(x, list):
        return '{' + ', '.join(wl(y) for y in x) + '}'
    return ('True' if x else 'False') if isinstance(x, bool) else str(x)


print(wl(out))
assert out == [32, False, 64, [129] * 6, True, 12, 55, True], out
