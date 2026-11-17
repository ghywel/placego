#!/usr/bin/env python3
"""trim.py (Local, L1519): what does V == 1 force locally, with NO black edge? State: D bits below the alternating diagonal,
b1 (nearest it), b2, ..., bD; the two bits below bD are free inputs at every tick. Constraint: b1 OR b2 = 1 at every tick (V == 1), plus
optionally b0: a second alternating diagonal above, which forces b1 black on a parity class. Keep the states lying on a bi-infinite
constrained path (trim both ways). The growth of the trimmed set says how strong the local constraint is."""
import numpy as np, sys, time
def trim(D, two_alt=False):
    # state index: bit (i-1) holds b_i, i = 1..D; with two_alt, one more bit (bit D) is the tick parity
    n = 1 << D
    S = n * (2 if two_alt else 1)
    idx = np.arange(S, dtype=np.int64)
    b = (idx & (n - 1))
    par = (idx >> D) & 1
    ok = ((b & 1) | ((b >> 1) & 1)) == 1 if D >= 2 else (b >= 0)
    if two_alt:
        # b1 black at even parity
        ok = ok & ((par == 1) | ((b & 1) == 1))
    alive = ok.copy()
    # successors with free inputs z1 (below bD), z2
    def nxt(st, z1, z2):
        bb = st & (n - 1); p = (st >> D) & 1
        x = bb | (z1 << D) | (z2 << (D + 1))
        y = (x ^ ((x >> 1) | (x >> 2))) & (n - 1)
        return y | ((p ^ 1) << D) if two_alt else y
    succ = [nxt(idx, z1, z2) for z1 in (0, 1) for z2 in (0, 1)]
    while True:
        hs = np.zeros(S, dtype=bool)
        for s in succ: hs |= alive[s]
        hp = np.zeros(S, dtype=bool)
        for s in succ:
            hp[s[alive]] = True
        new = alive & hs & hp
        if (new == alive).all(): break
        alive = new
    return alive
for two in (False, True):
    print('two adjacent alternating' if two else 'single V == 1')
    prev = None
    for D in range(2, 23):
        t0 = time.time()
        a = trim(D, two)
        c = int(a.sum())
        print(f'  D={D:2d} states {c:8d} of {a.size:8d}  growth {None if not prev else round(c / prev, 3)}  ({time.time() - t0:.1f}s)', flush=True)
        prev = c
        if time.time() - t0 > 30: break
