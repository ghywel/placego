#!/usr/bin/env python3
"""L1373 (Local, 2026-11-03): independent carrying check of GC2448 (prefix-490 capture of the invader specimen).
Run: python3 tests/probes/prefix490_check.py HEXBITS SAMPLES

The specimen B: the classic ether at alignment (0, 0) on x < 0, its retained bits on x = 0 .. 1199 (hex, little-endian,
from ether_invasion_climb.out), white beyond. Checks, by a list oracle written here:
  P1 the first time t at which, for some B3 column xB (x = 2 mod 7), B equals the ether on every x <= xB (within the
     light-cone-valid window) and B's 13 cells xB+1 .. xB+13 form one of the kit's 109 wall states at phase t mod 4
     (GC2448: t = 558, xB = -82); and the minimum front over t <= that time (GC2448: -81, first at 527);
  P2 the quantifier: SAMPLES rows agreeing with B on x <= 489 (the cone right edge Q + 558 = -69 + 558) and random
     beyond (up to 3000), run to 1200: each must show the same entry at 558 and an all-time minimum front of -81;
  P3 a negative control: changing bit 489 alone must leave the entry at 558 unchanged only if it is masked; changing
     a bit inside the prefix near the cone's edge is reported (no expectation; GC2448 claims no shortest prefix).
"""
import ast
import os
import random
import sys

TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
src = open(os.path.expanduser('~/.cache/placego-known/kit/lean/Ruliology/CellularAutomata/Rule30Ether.lean')).read()
body = src[src.index('def wallStates'):]
body = body[body.index(':=') + 2:body.index('/-- Closure under')]
WALL = {(ph, tuple(s)) for ph, s in ast.literal_eval(body.replace('true', '1').replace('false', '0').strip())}
assert len(WALL) == 109
bits = int(sys.argv[1], 16)
NS = int(sys.argv[2])
T = 1200
LO, HI = -T - 200, 3000


def run(row_fn):
    """Front path and first wall entry for the row x -> row_fn(x)."""
    g = [row_fn(x) for x in range(LO, HI + 1)]
    lo = LO
    entry = None; fronts = []
    for t in range(T + 1):
        valid_lo = lo + 1                                   # cells are exact from lo + 1 on after t ticks (list shrinks)
        ether = lambda x: TAB[x % 7][t % 4]
        L = next((x for x in range(valid_lo, valid_lo + len(g) - 2) if g[x - lo] != ether(x)), None)
        fronts.append(L)
        if entry is None and L is not None:
            # largest B3 column xB < L with ether up to it, and a wall right of it
            xB = L - 1 - ((L - 1 - 2) % 7)
            if xB >= valid_lo:
                strip = tuple(g[x - lo] for x in range(xB + 1, xB + 14))
                if (t % 4, strip) in WALL:
                    entry = (t, xB)
        if t < T:
            g = [g[i - 1] ^ (g[i] | g[i + 1]) for i in range(1, len(g) - 1)]
            lo += 1
    return entry, fronts


B = lambda x: TAB[x % 7][0] if x < 0 else ((bits >> x) & 1 if x < 1200 else 0)
entry, fr = run(B)
mins = min(f for f in fr if f is not None)
first_min = next(t for t, f in enumerate(fr) if f == mins)
print('P1 specimen: first wall entry (t, xB) = %s; minimum front %d first at t = %d; front at 558, 600, 1200: %s %s %s' % (
    entry, mins, first_min, fr[558], fr[600], fr[1200]))
rng = random.Random(2448)
ok = 0
for k in range(NS):
    tail = {x: rng.getrandbits(1) for x in range(490, HI + 1)}
    H = lambda x, tail=tail: TAB[x % 7][0] if x < 0 else ((bits >> x) & 1 if x < 490 else tail[x])
    e2, f2 = run(H)
    m2 = min(f for f in f2 if f is not None)
    ok += (e2 == entry and m2 == mins)
    if e2 != entry or m2 != mins:
        print('   P2 MISMATCH sample %d: entry %s, min front %d' % (k, e2, m2))
print('P2 quantifier: %d of %d random continuations beyond 489 give entry %s and all-time minimum front %d' % (
    ok, NS, entry, mins))
for x in (489, 470, 450):
    H = lambda y, x=x: B(y) ^ (y == x)
    e3, f3 = run(H)
    print('P3 flip bit %d: entry %s, minimum front %d' % (x, e3, min(f for f in f3 if f is not None)))
print('PREFIX490_DONE')
