#!/usr/bin/env python3
"""gate_trap_lift_replay.py (Local, 9 November 2026; S-16): the plain-Python replay of the worked-numbers cell of the
gate-trap lift essay. Usage: python3 gate_trap_lift_replay.py KIT_DIR

From the kit's 829 trap codes (lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean): the 18-column lift
(every trap window with every value of columns 17 and 18), the number of its double steps (both values of column 19
at both steps) that stay inside; the layer sizes of the gap word 3535353 from every black window, in the 16-column
trap and in the 18-column lift; and the minimal forbidden gap words over 3 and 5 of up to eight gaps from every black
window, at 16 and at 18 columns (sorted by length, then lexicographically). It prints
{lift size, closed edges, sizes at 16, sizes at 18, minimal at 16, minimal at 18}.
The notebook's first Output cell must equal this list."""
import re
import sys
from pathlib import Path

src = (Path(sys.argv[1]) / 'lean/Ruliology/CellularAutomata/Rule30Certificates/GateTrap.lean').read_text()
trap = [int(x) for x in re.findall(r'\d+', re.search(r'def trapCodes : List Nat := \[(.*?)\]', src, re.S).group(1))]
lift = [t | (h << 16) for t in trap for h in range(4)]


def step(s, c, x, W):
    e = s | (x << W)
    return (((e << 1) | c) ^ (e | (e >> 1))) & ((1 << W) - 1)


def succ(s, W):
    return {step(step(s, 0, a, W), 1, b, W) for a in (0, 1) for b in (0, 1)}


L = set(lift)
closed = sum(1 for w in lift for a in (0, 1) for b in (0, 1) if step(step(w, 0, a, 18), 1, b, 18) in L)


def bits(g):
    b = [1]
    for x in g:
        b += [0] * (x - 1) + [1]
    return b


def sizes(start, W, w):
    S = {x for x in start if (x & 1) == w[0]}
    out = [len(S)]
    for y in w[1:]:
        S = {v for x in S for v in succ(x, W) if (v & 1) == y}
        out.append(len(S))
    return out


def minimal(start, W, nmax):
    def gap(S, g):
        for k in range(1, g + 1):
            S = {v for x in S for v in succ(x, W) if (v & 1) == (1 if k == g else 0)}
        return frozenset(S)
    allowed = {(): frozenset(x for x in start if x & 1)}
    forb = []
    for n in range(1, nmax + 1):
        for w in [k for k in allowed if len(k) == n - 1]:
            for g in (3, 5):
                S = gap(allowed[w], g)
                if S:
                    allowed[w + (g,)] = S
                else:
                    forb.append(w + (g,))
    return sorted((list(v) for v in forb if v[1:] in allowed), key=lambda v: (len(v), v))


w = bits([3, 5, 3, 5, 3, 5, 3])
out = [len(lift), closed, sizes(trap, 16, w), sizes(lift, 18, w), minimal(trap, 16, 8), minimal(lift, 18, 8)]


def wl(x):
    return '{' + ', '.join(wl(y) for y in x) + '}' if isinstance(x, list) else str(x)


print(wl(out))
assert out[0] == 3316 and out[1] == 4 * 3316 and out[3][-1] == 0 and out[2][-1] > 0
