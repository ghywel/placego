#!/usr/bin/env python3
"""gate_trap_words_replay.py (Local, 9 November 2026): the plain-Python replay of the worked-numbers cell of the
gate-trap gap-word essay. Usage: python3 gate_trap_words_replay.py KIT_DIR

It reads the 829 codes of the kit's gate trap (lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean),
counts the double steps (both values of column 17 at both steps) that stay inside, computes the layer sizes of the
gap words 333, 3353, 3533, 3553 and 5533 (the windows of the trap that can have read each prefix of their samples),
and lists the minimal forbidden gap words over 3 and 5 of up to eight gaps (forbidden, while the word without its
first gap is allowed), with the number of distinct path sets among the allowed words. It prints
{829, closed edges, layer sizes, minimal forbidden words sorted by length then lexicographically, distinct path sets}.
The notebook's first Output cell must equal this list."""
import re
import sys
from pathlib import Path

src = (Path(sys.argv[1]) / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
trap = [int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))]
T = set(trap)


def step(s, c, x):
    e = s | (x << 16)
    return (((e << 1) | c) ^ (e | (e >> 1))) & 65535


def succ(s):
    return sorted({step(step(s, 0, a), 1, b) for a in (0, 1) for b in (0, 1)})


closed = sum(1 for w in trap for v in [step(step(w, 0, a), 1, b) for a in (0, 1) for b in (0, 1)] if v in T)


def bits(g):
    b = [1]
    for x in g:
        b += [0] * (x - 1) + [1]
    return b


def sizes(w):
    S = {x for x in trap if (x & 1) == w[0]}
    out = [len(S)]
    for y in w[1:]:
        S = {v for x in S for v in succ(x) if (v & 1) == y}
        out.append(len(S))
    return out


words = [[3, 3, 3], [3, 3, 5, 3], [3, 5, 3, 3], [3, 5, 5, 3], [5, 5, 3, 3]]


def gap(S, g):
    for k in range(1, g + 1):
        S = {v for x in S for v in succ(x) if (v & 1) == (1 if k == g else 0)}
    return frozenset(S)


allowed = {(): frozenset(x for x in trap if x & 1)}
forb = []
for n in range(1, 9):
    for w in [k for k in allowed if len(k) == n - 1]:
        for g in (3, 5):
            S = gap(allowed[w], g)
            if S:
                allowed[w + (g,)] = S
            else:
                forb.append(w + (g,))
minimal = sorted((v for v in forb if v[1:] in allowed), key=lambda v: (len(v), v))
out = [len(trap), closed, [sizes(bits(w)) for w in words], [list(v) for v in minimal], len(set(allowed.values()))]


def wl(x):
    return '{' + ', '.join(wl(y) for y in x) + '}' if isinstance(x, list) else str(x)


print(wl(out))
assert out[0] == 829 and out[1] == 3316 and [list(v) for v in minimal] == words
