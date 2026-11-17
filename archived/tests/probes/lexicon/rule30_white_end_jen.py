#!/usr/bin/env python3
"""rule30_white_end_jen.py: WJ, the Condrey white end 1 0^q excluded for finite seeds by a one-sided relaxation and
Theorem A (Jen's theorem with a clock, PROOFS.md entry 5). Local, chat L498. The finding was exploratory (scratch,
2026-10-09 22:27 BST, while extending L497's black-end route); this probe REPLICATES it with an implementation written
separately from rule30_one_hole_widths.py's `jen` mode, and adds blind questions. Predictions pushed before the run.

RUN-ON:     cpu (Python 3); a minute
COMMAND:    python3 tests/probes/lexicon/rule30_white_end_jen.py

The relaxation: k cells x1 .. xk right of column 0, an arbitrary outside bit beyond xk at every step, one Rule 30 step
x'(j) = x(j - 1) xor (x(j) or x(j + 1)) with x(0) the wall. The wall reads the word w periodically.
The stable set: apply the macro (one period of w, every outside bit) to all 2^k states until the image stops
changing. Every actual right half's k-cell state lies in it after finitely many periods.
Column +1 is determined if, from the stable set, x1 takes a single value at every tick of the period. Then x1 is
eventually periodic with the wall's period, on every actual right half, whatever lies further right.
Theorem A: two adjacent columns that are P-periodic for ever are impossible in a configuration with a leftmost black
cell. So a determined word is excluded as an eventual column of any finite nonzero seed.

This implementation keeps relations as lists of image sets, given by literal row tuples and the Rule 30 table, not
bitmasks. The eventual periods of the white and black relations are computed by exact equality of whole relations.

PREDICTIONS (Local's, published before the run):
  WJ-C1 (control): the black end 0 1^(p-1) is determined at width 8 exactly for p = 15 .. 40, and at width 6 for none
        (L497).
  WJ-R1 (replication of the exploratory finding, not blind): the white end 1 0^q is determined at width 8 for every
        q = 10 .. 40, and the white relation at width 8 has W^(n+4) = W^n for n >= 22.
  WJ-P1 (blind, confidence 0.5): at width 12, some white-end q in 2 .. 9 is also determined.
  WJ-P2 (blind, confidence 0.5): the white end is determined at width 6 for some q in 10 .. 40.
  WJ-D1 (descriptive): column +1's determined word for a few q, and the stable-set sizes.
OUTCOME, 2026-10-09 22:27 BST (M5, 2.3 s, run at commit b78b52f4): WJ-C1 PASS, WJ-R1 HELD, WJ-P1 REFUTED, WJ-P2 REFUTED.
  - The black end reproduces L497: determined at width 8 for p = 15 .. 40, and at width 6 for none.
  - The white end, width 8: determined for every q = 10 .. 40. Column +1 reads 1 0 0 1^(q-2), with period q + 1. The
    stable sets have 31 states at q = 10, 21 at q = 12 and 7 at q = 20.
  - W^(n+4) = W^n for n >= 22, so the macros 1 0^q repeat with period 4 in q from q = 22 on, and q = 10 .. 40 covers
    every q >= 10.
  - Neither width 12 (q = 2 .. 9) nor width 6 (q = 10 .. 40) determines column +1.
  - Claim, for a second reader: no finite nonzero seed has a column that eventually reads 1 0^q for any q >= 10.
    - Every actual right half's 8-cell state lies in the stable set after finitely many periods, so column +1 is
      eventually periodic with period q + 1.
    - Column 0 is periodic too, and Theorem A (PROOFS.md entry 5) forbids two adjacent columns periodic for ever when
      there is a leftmost black cell.
  - EXPLORATORY consistency check (scratch, 22:31 BST, after the run; no predictions). Plain forward simulation of the true
    half-line, with 200 random initial right halves of width 300 run for 60 periods each:
    - walls 1 0^10, 1 0^12 and 1 0^20, the black end 0 1^14 and the slow wall 0^2 1^8;
    - in all 1,000 runs, column +1 ends in exactly the word the width-8 stable set predicts (for 0^2 1^8: 0110000000).
    This is consistent with the transfer step; it is not a proof.
"""
from itertools import product

R30 = {(a, b, c): a ^ (b | c) for a in (0, 1) for b in (0, 1) for c in (0, 1)}


def states(k):
    return list(product((0, 1), repeat=k))


def step(x, wall, u):
    row = (wall,) + x + (u,)
    return tuple(R30[row[j:j + 3]] for j in range(len(x)))


def image(S, wall):
    return frozenset(step(x, wall, u) for x in S for u in (0, 1))


def eventual(k, wall):
    """exact eventual period of the one-step relation with a fixed wall bit, as whole relations"""
    sts = states(k)
    cur = tuple(frozenset([s]) for s in sts)
    seen, m = {}, 0
    while cur not in seen:
        seen[cur] = m
        cur = tuple(image(S, wall) for S in cur)
        m += 1
    return seen[cur], m - seen[cur]


def determined(k, word):
    wall = [int(c) for c in word]
    S = frozenset(states(k))
    for _ in range(200):
        T = S
        for w in wall:
            T = image(T, w)
        if T == S:
            break
        S = T
    ticks, T = [], S
    for w in wall:
        ticks.append({x[0] for x in T})
        T = image(T, w)
    col = ''.join(str(next(iter(v))) if len(v) == 1 else '*' for v in ticks)
    return '*' not in col, col, len(S)


def main():
    blk8 = [p for p in range(8, 41) if determined(8, '0' + '1' * (p - 1))[0]]
    blk6 = [p for p in range(8, 41) if determined(6, '0' + '1' * (p - 1))[0]]
    print('black end, width 8: determined at p = %s' % blk8)
    print('black end, width 6: determined at p = %s' % (blk6 or 'none'))
    print('WJ-C1', 'PASS' if blk8 == list(range(15, 41)) and not blk6 else 'FAIL')
    n0, P = eventual(8, 0)
    wh8 = [q for q in range(2, 41) if determined(8, '1' + '0' * q)[0]]
    print('white relation, width 8: W^(n+%d) = W^n for n >= %d' % (P, n0))
    print('white end, width 8: determined at q = %s' % wh8)
    print('WJ-R1', 'HELD' if all(q in wh8 for q in range(10, 41)) and (n0, P) == (22, 4) else 'REFUTED')
    wh12 = [q for q in range(2, 10) if determined(12, '1' + '0' * q)[0]]
    print('white end, width 12, q = 2 .. 9: determined at %s' % (wh12 or 'none'))
    print('WJ-P1', ('HELD %s' % wh12) if wh12 else 'REFUTED')
    wh6 = [q for q in range(10, 41) if determined(6, '1' + '0' * q)[0]]
    print('WJ-P2', ('HELD %s' % wh6) if wh6 else 'REFUTED (none at width 6)')
    for q in (10, 12, 20):
        ok, col, m = determined(8, '1' + '0' * q)
        print('  q = %d, width 8: stable set %d states; column +1 = %s' % (q, m, col))
    print('COMPLETE')


if __name__ == '__main__':
    main()
