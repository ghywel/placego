#!/usr/bin/env python3
"""L1381 (Local, 2026-11-03): carrying checks of GC2463 (the seven-cell pre-return packet) and GC2464 (applications).
Run: python3 tests/probes/packet_check.py HEXBITS

P1 exhaustive in the S = 13 strip step (my own): at phase 2, over all 2^13 strips and both inputs, "re-anchors and the
   new core is 1951" holds iff the first seven strip cells (little-endian) are 57, 89 or 121 (10011pq, p or q = 1).
P2 the GC2460 witness (normalised frame, core 1951, its 111 bits): the packets at times 43, 87, 131 on columns
   1 - 7j .. 7 - 7j (GC2463: 121, 89, then 45, which fails at physical -11 and -9 although it still falls).
P3 the retained specimen B: packets at t = 474 (anchor -68) and t = 518 (anchor -75) (GC2464: 89 and 121), and the
   pre-fall cores there (1369 and 4857).
"""
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


bad = 0; packets = set()
for s in range(1 << S):
    for u in (0, 1):
        ph2, s2, d = step(2, s, u)
        hit = d < 0 and s2 == 1951
        if hit:
            packets.add(s & 127)
        if hit != ((s & 127) in (57, 89, 121)):
            bad += 1
print('P1 phase-2 strips x inputs: mismatches with the packet rule %d; packets that reset to 1951: %s' % (bad, sorted(packets)))
WIT = '100101000011011100011100110011111001111100001100111111111111111111111111111111111111111111111111111111111111111'
E = lambda t, x: TAB[(x + 2) % 7][(t + 3) % 4]
LO, HI = -400, 700
g = [E(0, x) if x <= 0 else (((1951 >> (x - 1)) & 1) if x <= 13 else (int(WIT[x - 14]) if x <= 124 else 0))
     for x in range(LO, HI + 1)]
lo = LO
for t in range(1, 132):
    g = [g[i - 1] ^ (g[i] | g[i + 1]) for i in range(1, len(g) - 1)]; lo += 1
    if t in (43, 87, 131):
        a = -7 * ((t - 43) // 44)
        pk = sum(g[a + i - lo] << (i - 1) for i in range(1, 8))
        print('P2 witness t=%d anchor %d: packet %d (cells %s), phase %d' % (
            t, a, pk, ''.join(str(g[a + i - lo]) for i in range(1, 8)), (t + 3) % 4))
bits = int(sys.argv[1], 16)
LO, HI = -900, 1300
g = [TAB[x % 7][0] if x < 0 else ((bits >> x) & 1 if x < 1200 else 0) for x in range(LO, HI + 1)]
lo = LO
for t in range(1, 519):
    g = [g[i - 1] ^ (g[i] | g[i + 1]) for i in range(1, len(g) - 1)]; lo += 1
    if t in (474, 518):
        a = {474: -68, 518: -75}[t]
        pk = sum(g[a + i - lo] << (i - 1) for i in range(1, 8))
        core = sum(g[a + i - lo] << (i - 1) for i in range(1, 14))
        print('P3 specimen t=%d anchor %d: packet %d, pre-fall core %d, phase %d' % (t, a, pk, core, t % 4))
print('PACKET_DONE')
