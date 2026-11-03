#!/usr/bin/env python3
"""L1362 T54 (Local, 2026-11-03): random right tails at the four entries where the rooted-front observer stalls above
its single-flip witnesses ((0, 3), (1, 0), (4, 1), (5, 1)). For each cut b from 40 to the rooted cut minus one, 400
tails (E on x <= b, random beyond) are run to the entry time; a tail that changes a cell x <= xB + 13 is a witness
that cut b does not suffice. reports/rule30-genealogy.md section 58. Run: python3 tests/probes/rooted_front_gaps.py
"""
import random

TAB = [[0,0,1,1],[0,1,1,0],[1,1,0,1],[0,1,0,1],[0,0,1,1],[0,0,0,1],[0,0,0,1]]
ENTRY = {(0,3): (186,-26,83), (1,0): (185,-27,81), (4,1): (148,-23,66), (5,1): (148,-24,61)}
LO, HI = -700, 700; n = HI - LO + 1; mask = (1 << n) - 1
rng = random.Random(541)
def ev(a, T):
    for _ in range(T):
        a = ((a << 1) ^ (a | (a >> 1))) & mask
    return a
for (c0, c1), (T, xB, rooted) in sorted(ENTRY.items()):
    Q = xB + 13
    E0 = lambda x: TAB[(x + c0) % 7][c1] if x < 0 else int(x == 0)
    base = sum(E0(x) << (x - LO) for x in range(LO, HI + 1))
    ref = ev(base, T); win = sum(1 << (x - LO) for x in range(LO + T + 1, Q + 1))
    out = []
    for b in range(40, rooted):
        hits = 0
        keep = base & ((1 << (b + 1 - LO)) - 1)
        for _ in range(400):
            a = keep | (rng.getrandbits(HI - b) << (b + 1 - LO))
            hits += bool((ev(a, T) ^ ref) & win)
        out.append('%d:%d' % (b, hits))
    print('(%d,%d) rooted %d; random tails (of 400) hitting the target, by cut: %s' % (c0, c1, rooted, ' '.join(out)), flush=True)
