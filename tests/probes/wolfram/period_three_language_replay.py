#!/usr/bin/env python3
"""period_three_language_replay.py (Local, S-14): the plain-Python replay of the essay's worked-numbers cell.

For the center words 011 (strip width 7, reading phase 0) and 001 (width 10, phase 1) it builds the strip graph (phase,
columns 1..B, one edge per value of column B + 1), finds its cyclic strongly connected components, and inside the largest
one (the bad class of the module's certificates) asks, for each listed word, whether some path reads it in column 1 at
the reading phase of consecutive periods. It prints, for each word in turn, [sorted sizes of the cyclic components,
size of the largest, the occurrence flags]: the forbidden words first (all False), then the control words (all True).
The notebook's first Output cell must equal this list."""
import sys

CASES = [('011', 7, 0, ['00', '011110', '111010', '0101010', '0101110', '01011010', '11101110', '111011010'], ['11', '0110111']),
         ('001', 10, 1, ['010', '101', '11111', '000000', '100111', '111001', '00000111', '01110001', '10011001', '11100000'],
          ['11', '0011', '110011'])]

def run(word, B, R, words):
    w = [int(c) for c in word]; n = 1 << B; N = 3 * n
    def nxt(v, x):
        ph, s = divmod(v, n); e = s | (x << B)
        return ((ph + 1) % 3) * n + ((((e << 1) | w[ph]) ^ (e | (e >> 1))) & (n - 1))
    # Kosaraju, iterative
    order = []; seen = [False] * N
    for r in range(N):
        if seen[r]: continue
        seen[r] = True; stack = [(r, 0)]
        while stack:
            v, i = stack[-1]
            if i < 2:
                stack[-1] = (v, i + 1); u = nxt(v, i)
                if not seen[u]: seen[u] = True; stack.append((u, 0))
            else:
                stack.pop(); order.append(v)
    rev = [[] for _ in range(N)]
    for v in range(N):
        for x in (0, 1): rev[nxt(v, x)].append(v)
    comp = [-1] * N; comps = []
    for r in reversed(order):
        if comp[r] != -1: continue
        c = len(comps); comps.append([r]); comp[r] = c; todo = [r]
        while todo:
            v = todo.pop()
            for u in rev[v]:
                if comp[u] == -1: comp[u] = c; comps[c].append(u); todo.append(u)
    cyc = [c for c in comps if len(c) > 1]
    big = set(max(cyc, key=len))
    def steps(v):
        out = []
        for a in (0, 1):
            v1 = nxt(v, a)
            if v1 not in big: continue
            for b in (0, 1):
                v2 = nxt(v1, b)
                if v2 not in big: continue
                for c in (0, 1): out.append(nxt(v2, c))
        return out
    def occ(word_):
        S = {v for v in big if v // n == R and (v & 1) == int(word_[0])}
        for y in word_[1:]:
            S = {u for v in S for u in steps(v) if u in big and (u & 1) == int(y)}
        return len(S) > 0
    return [sorted(len(c) for c in cyc), len(big), [occ(x) for x in words]]

out = [run(word, B, R, forb + ctrl) for word, B, R, forb, ctrl in CASES]
def wl(x):
    if isinstance(x, bool): return 'True' if x else 'False'
    if isinstance(x, list): return '{' + ', '.join(wl(y) for y in x) + '}'
    return str(x)
print(wl(out))
assert all(not f for f in out[0][2][:8]) and all(out[0][2][8:]) and all(not f for f in out[1][2][:10]) and all(out[1][2][10:])
