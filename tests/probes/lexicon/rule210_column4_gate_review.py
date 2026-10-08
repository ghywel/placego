#!/usr/bin/env python3
"""rule210_column4_gate_review.py: GG, Local's independent reading of GC462 (GPT's column-4 gate: under b = 0 and
h z = 0 the next even column-4 bit is H = (1 - q)(1 - z) w; with GC461's q and z and G26's stream, an even column-4
bit could be black only at n = 4^r, where z_n = 1 forbids it), requested by GPT's review flag of 2026-10-08.
Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule210_column4_gate_review.py
COST:       to be recorded (expected seconds).

The hand reading is in L273. This probe checks the local identity under Local's own integer coding and the switch
arithmetic on G26's closed form over a long range, independently of GPT's twelve patches.

PREDICTIONS (Local's, published before the run):
  GG-P1: all 12 inputs (0, q, h, z, w) with h z = 0 give the two-step column-4 bit H = (1 - q)(1 - z) w under the
         integer Rule 210 step; exactly 2 of them have H = 1 (q = z = 0, w = 1).
  GG-P2: with s_0 = 1, s_n = floor(log2 n) mod 2 (G26), q_m = 1 XOR s_m XOR s_(m+1) and z_m = 1 XOR s_m XOR s_(m+1)
         XOR s_(m+2) (GC461), the indices 0 <= m < 2^20 with q_m = z_m = 0 are exactly 4^r - 1, r >= 1.
  GG-P3: z_n = 1 at every n = 4^r, r >= 1, below 2^20.
  GG-C0 (control): the four inputs with h = z = 1 are not all fitted by the same formula (the product premise
         matters).
OUTCOME: not yet run.
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule210_two_step_review as ts


def two_step_col4(patch):
    row = 0
    for k, v in enumerate(patch):                 # patch at sites 2 .. 6
        if v:
            row |= 1 << (ts.B - (2 + k + ts.OFF))
    return ts.bit(ts.step(ts.step(row)), 4)


def main():
    t0 = time.time()
    ins = [(0, q, h, z, w) for q in (0, 1) for h in (0, 1) for z in (0, 1) for w in (0, 1)]
    free = [p for p in ins if p[2] * p[3] == 0]
    f = lambda p: (1 - p[1]) * (1 - p[3]) * p[4]
    p1 = len(free) == 12 and all(two_step_col4(p) == f(p) for p in free)
    ones = [p for p in free if two_step_col4(p)]
    p1 = p1 and sorted(ones) == [(0, 0, 0, 0, 1), (0, 0, 1, 0, 1)]
    c0 = any(two_step_col4(p) != f(p) for p in ins if p[2] * p[3] == 1)
    M = 1 << 20
    s = [1] + [(n.bit_length() - 1) % 2 for n in range(1, M + 3)]
    q = lambda m: 1 ^ s[m] ^ s[m + 1]
    z = lambda m: 1 ^ s[m] ^ s[m + 1] ^ s[m + 2]
    hit = [m for m in range(M) if q(m) == 0 and z(m) == 0]
    fours = [4 ** r - 1 for r in range(1, 11) if 4 ** r - 1 < M]
    p2 = hit == fours
    p3 = all(z(4 ** r) == 1 for r in range(1, 11) if 4 ** r < M)
    print('GG-P1', 'HELD' if p1 else 'REFUTED', '(H = 1 at %s)' % ones)
    print('GG-P2', 'HELD' if p2 else 'REFUTED', '(first hits %s)' % hit[:8])
    print('GG-P3', 'HELD' if p3 else 'REFUTED')
    print('GG-C0', 'PASS' if c0 else 'FAIL')
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
