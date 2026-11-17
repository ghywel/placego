#!/usr/bin/env python3
"""rule30_jen_pow2.py: JP, the left diagonals' eventual periods divide 2^(k-2), checked on every small seed.

RUN-ON:     cpu (Python 3, numpy); seconds
COMMAND:    python3 tests/probes/lexicon/rule30_jen_pow2.py [S=12] [J=14] [T=65536]

Why. The record map lists "left diagonals eventually periodic, power-of-2 periods (known: Jen 1986, Rowland §5)" as
COMPUTED. Jen's paper is still unread (paywalled), and §8.27's proof covers the right diagonals (running XORs) only.
The left diagonals D_k(t) = cell e - t + k satisfy D_k(t + 1) = D_(k-2)(t) xor (D_(k-1)(t) or D_k(t)), a recurrence
closed on the left. Local's proof, for JenPow2.lean:
  - D_0 is black, D_1 is black from t = 1, and D_2 is white from t = 2. So every k <= 2 has period 1 from t = 2.
  - Let a = D_(k-2) and b = D_(k-1) both have period p from T. Then x = D_k obeys x(t + 1) = a(t) xor (b(t) or x(t)).
  - Two of the bits x(T), x(T + p), x(T + 2p) are equal. Equal states with equal inputs have equal futures, so in
    each of the three cases x(T + 3p) = x(T + p). From T + p on, x then has period 2p.
  - By induction every diagonal k <= j + 2 has period 2^j from some time.
This scan computes the diagonals by that recurrence for every seed with leftmost black cell 0 and support inside cells
0 .. S - 1 (2^(S-1) seeds, bit-packed), for k <= J and T steps. In the last 3 * 2^(J-2) steps it finds each diagonal's
least power-of-2 period. The least period divides every period, so if 2^(k-2) is a period the least period is the
least power of 2 that is one.

PREDICTIONS (Local's, written before the Lean run and before this scan; the time is in the ledger entry L540):
  JP-C1 (control): D_0 is black at every step, and in every seed D_1 is black from t = 1 and D_2 white from t = 2.
  JP-P1 (0.8): Lean accepts `jen_pow2` (for every j there is a T after which every diagonal k <= j + 2 has period 2^j)
         and the corollary `run_bound` (from some time on, a white run in diagonals <= j + 2 has length at most
         2^(j+1) - 1), with no sorryAx.
  JP-P2 (0.85): every (seed, k) pair with 3 <= k <= J is periodic with period 2^(k-2) over the window (settled within
         T steps). A failure here counts as unsettled within T, not as a counterexample.
  JP-P3 (the unexpected check, 0.5): for every k = 3 .. J some seed's least period is exactly 2^(k-2), so the bound
         is attained at every depth.
OUTCOME, 2026-10-10 05:21 BST (M5; the scan about 20 s; Lean about 40 s): C1 PASS; P1 and P2 HELD; P3 REFUTED.
  - P1: JenPow2.lean compiles after two fixes. A rewrite order in `det` was wrong, and omega needed 1 <= 2^j given
    explicitly. Axioms: forced_periodic uses propext and Quot.sound; jen_pow2 and run_bound use propext,
    Classical.choice and Quot.sound. No sorryAx.
  - C1 and P2: all 2,048 seeds settle within 65,536 steps, with D_1 black from t = 1 and D_2 white from t = 2.
  - P3 REFUTED: 2^(k-2) is attained only at k = 3. Every seed has the same least periods, 2, 1, 2, 2, 1, 4, 1, 4,
    4, 4, 4, 4 for k = 3 .. 14 (with 1, 1, 1 for k = 0 .. 2). So the proved bound is far from tight beyond k = 3, and
    the periods are seed-independent here.
  - Instrument check (after the run, before believing P3): for 6 random seeds a full Rule 30 simulation (T = 3,000)
    matches the closed recurrence exactly and gives the same periods. Across those seeds the last 8 steps show only
    4 distinct patterns, which are phase shifts.
  - This fits §8.31's "generic rows share one left side". The proof explains only the power of 2; why the
    sequence of periods is seed-independent is not proved here.
  - Correction (Cloud CL171): P3 was already against the record when I registered it. UB (L383,
    rule30_edge_period_universal.py) measured the universal left-edge staircase on 21 rows: P_e = 4 for 8 <= e < 29.
    My record search missed it, because UB says "staircase" and "P_e", not "period"; `record_find.py staircase`
    finds it. Cloud's 300-seed replay gives the same periods out to k = 16.
"""
import sys

import numpy as np

S = int(sys.argv[1]) if len(sys.argv) > 1 else 12
J = int(sys.argv[2]) if len(sys.argv) > 2 else 14
T = int(sys.argv[3]) if len(sys.argv) > 3 else 65536


def main():
    n = 1 << (S - 1)
    words = (n + 63) // 64
    seeds = np.arange(n, dtype=np.uint64)
    bits = [np.ones(n, np.uint64)] + [((seeds >> np.uint64(i - 1)) & np.uint64(1)) for i in range(1, S)]

    def pack(v):
        out = np.zeros(words, np.uint64)
        for s in np.flatnonzero(v):
            out[s // 64] |= np.uint64(1) << np.uint64(s % 64)
        return out

    full = pack(np.ones(n, np.uint64))
    d = [pack(bits[k]) if k < S else np.zeros(words, np.uint64) for k in range(J + 1)]
    W = 3 << (J - 2)
    tail = np.zeros((W, J + 1, words), np.uint64)
    c1 = True
    zero = np.zeros(words, np.uint64)
    for t in range(T):
        if not (d[0] == full).all():
            c1 = False
        if t >= 1 and not (d[1] == full).all():
            c1 = False
        if t >= 2 and not (d[2] == 0).all():
            c1 = False
        if t >= T - W:
            tail[t - (T - W)] = np.array(d)
        nd = []
        for k in range(J + 1):
            a = d[k - 2] if k >= 2 else zero
            b = d[k - 1] if k >= 1 else zero
            nd.append(a ^ (b | d[k]))
        d = nd

    def unpack(v):
        return np.array([(int(v[s // 64]) >> (s % 64)) & 1 for s in range(n)], np.uint8)

    p2_fail = 0
    attained = {}
    hist = {}
    for k in range(3, J + 1):
        least = np.full(n, -1)
        for m in range(0, k - 1):
            p = 1 << m
            mis = np.bitwise_or.reduce(tail[:W - p, k] ^ tail[p:, k], axis=0)
            ok = unpack(~mis & full)
            newly = (least < 0) & (ok == 1)
            least[newly] = m
        bad = int((least < 0).sum())
        p2_fail += bad
        attained[k] = int((least == k - 2).sum())
        hist[k] = {int(m): int((least == m).sum()) for m in np.unique(least)}
        print('k=%2d  unsettled %d  least period 2^m counts %s  attaining 2^(k-2): %d' % (k, bad, hist[k], attained[k]))
    print('S=%d J=%d T=%d: %d seeds' % (S, J, T, n))
    print('JP-C1', 'PASS' if c1 else 'FAIL')
    print('JP-P2', 'HELD' if p2_fail == 0 else 'REFUTED (%d unsettled pairs)' % p2_fail)
    print('JP-P3', 'HELD' if all(attained[k] for k in range(3, J + 1)) else
          'REFUTED (not attained at k = %s)' % [k for k in range(3, J + 1) if not attained[k]])


if __name__ == '__main__':
    main()
