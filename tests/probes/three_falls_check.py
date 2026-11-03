#!/usr/bin/env python3
"""L1379 (Local, 2026-11-03): independent replay of GC2460's three-fast-fall witness and carrying check of GC2461's
finite-prefix family. Run: python3 tests/probes/three_falls_check.py SAMPLES

Normalized frame (GC2454): E(t, x) = ether((x + 2) mod 7, (t + 3) mod 4); anchor 0 is a B3 column at phase 3. Initial
row: E on x <= 0, core word 1951 on 1..13 (bit i - 1 is cell i), the witness's 111 bits on 14..124 (GC2460), and a
continuation beyond. The anchor starts at 0 and falls by 7 whenever its cell leaves the ether; per fall the time, the
new anchor and the new 13-cell core word are recorded, through t = 140.
W1 the witness with white beyond 124: falls at 44, 88, 132; cores 1951, 1951, 4767 (GC2460).
W2 cells beyond 118 random (SAMPLES rows): falls at 44, 88, 132 (GC2461's cutoff 118).
W3 cells beyond 124 random: also core 4767 at 132 (the cutoff 124).
W4 the 48-bit word on 14..61 and black everywhere from 62 (GC2461's simple member).
"""
import random
import sys

TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
WIT = ('100101000011011100011100110011111001111100001100111111111111111111111111111111111111111111111111111111111111111')
assert len(WIT) == 111
E = lambda t, x: TAB[(x + 2) % 7][(t + 3) % 4]
CORE = 1951
TMAX = 140
LO, HI = -400, 700


def falls(tail):
    """tail(x) for x >= 14; returns the list of (time, new anchor, new core word)."""
    g = [E(0, x) if x <= 0 else (((CORE >> (x - 1)) & 1) if x <= 13 else tail(x)) for x in range(LO, HI + 1)]
    lo = LO; a = 0; out = []
    for t in range(1, TMAX + 1):
        g = [g[i - 1] ^ (g[i] | g[i + 1]) for i in range(1, len(g) - 1)]
        lo += 1
        assert all(g[x - lo] == E(t, x) for x in range(lo + 1, a))      # the half-line left of the anchor stays clean
        while g[a - lo] != E(t, a):
            a -= 7
            out.append((t, a, sum(g[a + i - lo] << (i - 1) for i in range(1, 14))))
    return out


wit = lambda x: int(WIT[x - 14]) if 14 <= x <= 124 else 0
print('W1 witness, white beyond 124: falls %s' % falls(wit))
rng = random.Random(2461)
NS = int(sys.argv[1])
ok2 = 0; ok3 = 0
for k in range(NS):
    r = {x: rng.getrandbits(1) for x in range(119, HI + 1)}
    f2 = falls(lambda x, r=r: int(WIT[x - 14]) if x <= 118 else r[x])
    ok2 += [t for t, _, _ in f2][:3] == [44, 88, 132]
    r3 = {x: rng.getrandbits(1) for x in range(125, HI + 1)}
    f3 = falls(lambda x, r3=r3: int(WIT[x - 14]) if x <= 124 else r3[x])
    ok3 += [(t, c) for t, _, c in f3][:3] == [(44, 1951), (88, 1951), (132, 4767)]
print('W2 cells beyond 118 random: %d of %d give first falls exactly 44, 88, 132' % (ok2, NS))
print('W3 cells beyond 124 random: %d of %d give falls 44, 88, 132 with cores 1951, 1951, 4767' % (ok3, NS))
print('W4 the word on 14..61, black from 62: falls %s' % falls(lambda x: int(WIT[x - 14]) if x <= 61 else 1))
print('THREE_FALLS_DONE')
