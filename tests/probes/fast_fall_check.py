#!/usr/bin/env python3
"""L1377 (Local, 2026-11-03): carrying checks of GC2454's fast-reset lemma and its cone counts.
Run: python3 tests/probes/fast_fall_check.py POTENTIALS.json

F1 M = phase-3 words with low byte 159 and the global minimum potential h = -385 (GC2454: {671, 1951, 4767, 6047, 6815}).
F2 inside the S = 13 strip model (independent step): from each start in M, the earliest first fall (a path of
   non-re-anchoring edges ended by one re-anchoring edge) and the set of endpoints of falls at exactly 44 ticks; the
   lemma predicts earliest >= 44 and 44-tick endpoints inside M.
F3 GC2454's cone for three falls: T = 132, initial [-152, 124]: variables, gates, fixed and free initial bits.
"""
import json
import sys

TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
S = 13


def step(ph, s, u):
    cells = [TAB[(2 + i) % 7][ph] for i in (-1, 0)] + [(s >> j) & 1 for j in range(S)] + [u]
    new = [cells[i - 1] ^ (cells[i] | cells[i + 1]) for i in range(1, len(cells) - 1)]
    ph2 = (ph + 1) % 4
    if new[0] != TAB[2][ph2]:
        strip = [TAB[(2 + i) % 7][ph2] for i in range(-6, 0)] + new[0:S - 6]
        return ph2, sum(b << j for j, b in enumerate(strip)), -7
    return ph2, sum(b << j for j, b in enumerate(new[1:])), 0


h = json.load(open(sys.argv[1]))['pi']
node = lambda ph, s: ph * (1 << S) + s
hmin = min(h)
M = sorted(w for w in range(1 << S) if w & 255 == 159 and h[node(3, w)] == hmin)
print('F1 global minimum h = %d; phase-3 low-byte-159 words at the minimum: %s' % (hmin, M))
for w0 in M:
    layer = {(3, w0)}; first = None; ends44 = set()
    for k in range(1, 61):
        nxt = set()
        for ph, s in layer:
            for u in (0, 1):
                ph2, s2, d = step(ph, s, u)
                if d < 0:
                    first = k if first is None else first
                    if k == 44:
                        ends44.add(s2)
                else:
                    nxt.add((ph2, s2))
        layer = nxt
    print('F2 start %d: earliest first fall at tick %s; endpoints of 44-tick falls %s (inside M: %s)' % (
        w0, first, sorted(ends44), set(ends44) <= set(M)))
T, lo, hi = 132, -152, 124
cells = sum((hi - t) - (lo + t) + 1 for t in range(T + 1))
print('F3 cone: %d variables, %d gates, fixed initial bits %d (x <= 13), free %d (14..124)' % (
    cells, cells - (hi - lo + 1), 13 - lo + 1, hi - 14 + 1))
print('FAST_FALL_DONE')
