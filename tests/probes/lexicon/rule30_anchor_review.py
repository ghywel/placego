#!/usr/bin/env python3
"""rule30_anchor_review.py: RW, Local's review of GC397 and GC399 (GPT's anchored implication in the class-12 tail:
with the wall at phase 0 and initial columns 2 .. 6 = 1, 1, 1, 0, 0, column 6 at time 8 being 1 forces column 5 at
time 12 to be 1), requested by GPT's review flag of 2026-10-07. Claimed in CLOUD-LOCAL.md with these predictions
pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule30_anchor_review.py
COST:       0.6 seconds.

Independent coding: rows are integers in the reverse bit order (column x at bit 17 - x), stepped by one shift-and-OR
expression, and column 0 is overwritten by the supplied wall value after every step. Column 5 at time 12 depends
on initial columns 1 .. 17 and wall values at times 0 .. 7 only (a wall value at time t first reaches column 1 at
t + 1 and column 5 at t + 5); column 6 at time 8 on initial columns 1 .. 14 and wall times 0 .. 2. So initial
columns 1 .. 17 and wall times 0 .. 11 cover the question exactly.

PREDICTIONS (Local's, published before the run; GC397's and GC399's reported numbers, to be reproduced):
  RW-P1: with the wall t mod 2 and initial columns 2 .. 6 = 11100, none of the 4,096 assignments to initial column 1
        and columns 7 .. 17 violates the implication.
  RW-P2: the anchor is inclusion-minimal: freeing any one of its five bits (the other four kept) admits a violation.
  RW-P3: flipping the wall at a single time t gives 2444, 864, 240, 976, 848, 812, 1340 and 1504 violations among
        the 4,096 for t = 0 .. 7, and none for t = 8 .. 11.
  RW-P4: with the full original prefix (initial columns 1 .. 6 = 011100), 1,376 of the 2,048 assignments to columns
        7 .. 17 make the antecedent true.
  RW-P5: with the opposite wall phase at every time and the original prefix, some assignment violates the implication
        (GC397 reports 544 of 2,048).
GC401 SECOND READING (added 2026-10-08, predictions before its run; mode `gc401`). GC401 proves by hand that after
four updates position 5 is 1 if positions 1 .. 7 are 0101110 (A) or positions 1, 2, 3, 4, 6 are 1, 1, 1, 0, 1 (B). I
checked both case analyses line by line. This mode checks the lemma and its bridge to GC397 directly, without
GC400's seven clauses:
  RW-L1 (the lemma, computed): all 20 assignments to the free cells of A and B give 1 at position 5 after 4 updates.
  RW-L2 (the bridge): under GC397's anchor and the baseline wall, every one of the 4,096 runs with column 6 = 1 at
        time 8 has columns 1 .. 9 at time 8 matching A or B. With RW-L1 that proves GC397's implication from the
        census of reached time-8 rows, and needs nothing else.
  OUTCOME of mode gc401, 2026-10-08 00:08 (M5, at commit 5798d4f, under a second): RW-L1 HELD (all 20 give 1).
  RW-L2 HELD: 1,504 of the 4,096 runs have column 6 = 1 at time 8, and all 1,504 match A or B in columns 1 .. 9.
OUTCOME, 2026-10-07 23:57 (M5, at commit 2ac668d; transcript outside Git). The first run crashed before printing
anything (a Python slip: dict(anchor, **{1: 0}) needs string keys); fixed to orig[1] = 0 and run again, nothing
else changed. All five HELD, reproducing GPT's numbers exactly: 0 violations among 4,096 at baseline; freeing anchor
columns 2, 3, 4, 5 or 6 gives 1616, 1600, 1260, 1000 and 1360 violations; single wall flips give 2444, 864, 240, 976,
848, 812, 1340, 1504 at t = 0 .. 7 and 0 at t = 8 .. 11; the original prefix has 1,376 antecedent-positive rows of
2,048; the opposite phase gives 544 violations (GC397's number).
"""
B = 17
MASK = (1 << (B + 1)) - 1


def run(init, wall):
    """init: dict column -> bit for columns 1 .. 17; wall: list of 13 wall bits for times 0 .. 12.
    Returns (column 6 at time 8, column 5 at time 12)."""
    row = (wall[0] << B) | sum(b << (B - x) for x, b in init.items())
    c6 = None
    for t in range(1, 13):
        nxt = ((row >> 1) ^ (row | (row << 1))) & MASK
        row = (nxt & ~(1 << B)) | (wall[t] << B)
        if t == 8:
            c6 = (row >> (B - 6)) & 1
    return c6, (row >> (B - 5)) & 1


def violations(anchor, free_cols, wall):
    v = pos = 0
    for seed in range(1 << len(free_cols)):
        init = dict(anchor)
        for i, x in enumerate(free_cols):
            init[x] = (seed >> i) & 1
        a, c = run(init, wall)
        pos += a
        v += a == 1 and c == 0
    return v, pos


def main():
    base_wall = [t % 2 for t in range(13)]
    anchor = {2: 1, 3: 1, 4: 1, 5: 0, 6: 0}
    free = [1] + list(range(7, 18))
    v0, _ = violations(anchor, free, base_wall)
    p1 = v0 == 0
    minimal = {}
    for x in anchor:
        sub = {y: b for y, b in anchor.items() if y != x}
        minimal[x] = violations(sub, sorted(free + [x]), base_wall)[0]
    p2 = all(n > 0 for n in minimal.values())
    flips = []
    for t in range(12):
        w = list(base_wall)
        w[t] ^= 1
        flips.append(violations(anchor, free, w)[0])
    p3 = flips[:8] == [2444, 864, 240, 976, 848, 812, 1340, 1504] and flips[8:] == [0, 0, 0, 0]
    orig = dict(anchor)
    orig[1] = 0
    _, pos = violations(orig, list(range(7, 18)), base_wall)
    p4 = pos == 1376
    v5, _ = violations(orig, list(range(7, 18)), [1 - b for b in base_wall])
    p5 = v5 > 0
    print('baseline violations %d of 4096; freeing each anchor bit gives %s' % (v0, minimal))
    print('single wall flips t = 0 .. 11: %s' % flips)
    print('original prefix: antecedent true for %d of 2048; opposite phase: %d violations' % (pos, v5))
    for name, ok in (('RW-P1', p1), ('RW-P2', p2), ('RW-P3', p3), ('RW-P4', p4), ('RW-P5', p5)):
        print(name, 'HELD' if ok else 'REFUTED')


def gc401():
    def evolve(cells, steps):
        cur = list(cells)
        for _ in range(steps):
            cur = [cur[i - 1] ^ (cur[i] | cur[i + 1]) for i in range(1, len(cur) - 1)]
        return cur
    ok = True
    for d in (0, 1):
        for e in (0, 1):
            ok &= evolve([0, 1, 0, 1, 1, 1, 0, d, e], 4) == [1]
    for b in (0, 1):
        for x7 in (0, 1):
            for x8 in (0, 1):
                for x9 in (0, 1):
                    ok &= evolve([1, 1, 1, 0, b, 1, x7, x8, x9], 4) == [1]
    print('RW-L1', 'HELD' if ok else 'REFUTED')
    wall = [t % 2 for t in range(13)]
    anchor = {2: 1, 3: 1, 4: 1, 5: 0, 6: 0}
    free = [1] + list(range(7, 18))
    pos = good = 0
    for seed in range(1 << len(free)):
        init = dict(anchor)
        for i, x in enumerate(free):
            init[x] = (seed >> i) & 1
        row = (wall[0] << B) | sum(b << (B - x) for x, b in init.items())
        for t in range(1, 9):
            nxt = ((row >> 1) ^ (row | (row << 1))) & MASK
            row = (nxt & ~(1 << B)) | (wall[t] << B)
        c = [(row >> (B - x)) & 1 for x in range(0, 10)]
        if c[6]:
            pos += 1
            a = c[1:8] == [0, 1, 0, 1, 1, 1, 0]
            bb = [c[1], c[2], c[3], c[4], c[6]] == [1, 1, 1, 0, 1]
            good += a or bb
    print('runs with column 6 = 1 at time 8: %d; matching A or B: %d' % (pos, good))
    print('RW-L2', 'HELD' if pos and good == pos else 'REFUTED')


if __name__ == '__main__':
    import sys
    gc401() if sys.argv[1:] == ['gc401'] else main()
