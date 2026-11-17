#!/usr/bin/env python3
"""L1371 (Local, 2026-11-03): carrying check of GC2444's two-tick boundary-history law and GC2445's envelope.
Run: python3 tests/probes/two_tick_history.py

A0, A1: the left neighbour (column p - 1) at times 0, 1; U0, U1, U2: the boundary cell (column p) at times 0, 1, 2.
The image of all 32 initial rows on p - 2 .. p + 2 is compared with the histories meeting GC2444's conditions
(1) U0 = 1 => U1 = 1 - A0; (2) U1 = 1 => U2 = 1 - A1; (3) U0 = U1 = 0 and A0 = 1 => U2 = 1 - A1.
GC2445's envelope: with potentials pi (max - min = 385) for w = 44 * drift + 7 on the S = 13 strip graph, a path of t
ticks with r re-anchorings has 7t - 308r >= pi(end) - pi(start) >= -385, so r <= floor((t + 55) / 44) and
L(t) >= a0 + 1 - 7 floor((t + 55) / 44); tabulated, and the invader specimen (a0 = -5 at alignment (0, 0)) compared.
"""
rule = lambda l, c, r: l ^ (c | r)
image = set()
for v in range(32):
    z, a0, u0, v0, w0 = [(v >> i) & 1 for i in range(5)]
    a1 = rule(z, a0, u0); u1 = rule(a0, u0, v0); v1 = rule(u0, v0, w0); u2 = rule(a1, u1, v1)
    image.add((a0, a1, u0, u1, u2))
cond = {h for h in [tuple((x >> i) & 1 for i in range(5)) for x in range(32)]
        if (h[2] == 0 or h[3] == 1 - h[0]) and (h[3] == 0 or h[4] == 1 - h[1])
        and not (h[2] == 0 and h[3] == 0 and h[0] == 1 and h[4] != 1 - h[1])}
print('two-tick law: image of the 32 rows has %d histories; conditions admit %d; equal: %s' % (
    len(image), len(cond), image == cond))
spec = {150: -21, 300: -43, 450: -62, 600: -80}
for t in (44, 150, 300, 450, 600, 1200):
    r = (t + 55) // 44
    print('t=%4d: at most %2d re-anchorings; envelope L(t) >= %4d for a0 = -5%s' % (
        t, r, -5 + 1 - 7 * r, '; specimen front %d' % spec[t] if t in spec else ''))
print('TWO_TICK_HISTORY_DONE')
