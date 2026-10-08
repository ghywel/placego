#!/usr/bin/env python3
"""rule210_prefix_review.py: PX, Local's independent reading of GC454 (GPT's finite certificate that the initial
column-3 product V_1(3) vanishes in every empty-left full 0101 Rule 210 orbit), requested by GPT's review flag of
2026-10-08. Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule210_prefix_review.py
COST:       to be recorded (well under a second).

Why seven bits suffice. With every cell left of the centre white at time 0, the centre at time t depends only on
sites 1 .. t at time 0 (radius one), so the centre through time 7 depends on sites 1 .. 7 only, and V_1(3) =
x_1(3) x_1(4) on sites 2 .. 5. So an enumeration of the 128 seven-bit seeds is an exact certificate for all tails.

Own coding: a row is an integer with site i at bit 20 - i (sites -12 .. 20, so the cone never reaches the ends),
stepped as Rule 210 by left XOR ((NOT centre) AND right): new = (row >> 1) ^ (~row & (row << 1)), masked.

PREDICTIONS (GC454's reported outcome, to be reproduced):
  PX-P1: exactly one seed survives the centre prefix 01010101 (times 0 .. 7): {1, 5, 7}.
  PX-P2: that seed has V_1(3) = 0.
  PX-P3: without the prefix condition, 32 seeds have V_1(3) = 1 and 96 have 0.
  PX-C0 (control): an independent scalar truth-table evolution gives the same centre prefix for every seed.
OUTCOME: not yet run.
"""
B = 32
MASK = (1 << (B + 1)) - 1
OFF = 12                                   # site i lives at bit B - (i + OFF)


def bit(row, i):
    return (row >> (B - (i + OFF))) & 1


def step(row):
    return ((row >> 1) ^ (~row & (row << 1))) & MASK


def scalar_centre(seed_sites, T):
    cells = {i: 0 for i in range(-T - 2, T + 10)}
    for i in seed_sites:
        cells[i] = 1
    out = [cells[0]]
    rule = {(l, c, r): (210 >> (4 * l + 2 * c + r)) & 1 for l in (0, 1) for c in (0, 1) for r in (0, 1)}
    lo, hi = min(cells), max(cells)
    for t in range(1, T + 1):
        cells = {i: rule[cells.get(i - 1, 0), cells[i], cells.get(i + 1, 0)] for i in range(lo, hi + 1)}
        out.append(cells[0])
    return out


def main():
    survivors, prod1, ok = [], 0, True
    for seed in range(1 << 7):
        sites = [i for i in range(1, 8) if (seed >> (i - 1)) & 1]
        row = sum(1 << (B - (i + OFF)) for i in sites)
        rows = [row]
        for _ in range(7):
            rows.append(step(rows[-1]))
        centre = [bit(r, 0) for r in rows]
        v13 = bit(rows[1], 3) & bit(rows[1], 4)
        prod1 += v13
        ok &= centre == scalar_centre(sites, 7)
        if centre == [t % 2 for t in range(8)]:
            survivors.append((sites, v13))
    print('survivors of 01010101: %s' % survivors)
    print('V_1(3) = 1 for %d of 128 seeds' % prod1)
    print('PX-P1', 'HELD' if [s for s, _ in survivors] == [[1, 5, 7]] else 'REFUTED')
    print('PX-P2', 'HELD' if survivors and all(v == 0 for _, v in survivors) else 'REFUTED')
    print('PX-P3', 'HELD' if prod1 == 32 else 'REFUTED')
    print('PX-C0', 'PASS' if ok else 'FAIL')


if __name__ == '__main__':
    main()
