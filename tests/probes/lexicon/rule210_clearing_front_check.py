#!/usr/bin/env python3
"""rule210_clearing_front_check.py: FR, Local's independent actual-orbit check of GC478's clearing-front statement
(GPT's proposed hand proof of the 2w life law, closing Rule 210 question B for the full 0101 clock), run before the
second reading is filed. Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule210_clearing_front_check.py
COST:       to be recorded (expected under a minute).

GC478's statement, in its notation: P_j = D_(e+2j)(x), Q_j = D_(e+2j+1)(x), A_j = D_(e+2j+1)(y), T_j = tau + j + 1. For
every j <= w and every choice of later initial sites, the candidate pair (P_j, Q_j) is (0, 1) at T_j, and for every
s >= T_j, P_j(s) = 0 and Q_j(s) XOR A_j(s) = A_j(0). This is sharper than FV's settling time tau + 1 + 2j. Cases and
tails exactly as FV (all 63 odd rows R <= 12; 150 random rows at each of R = 20, 30, 40; every even e <= R + 20;
every tail of sites e + 1 .. e + 2w + 1 when 2w + 1 <= 9, else 16 seeded random tails), with the window s <= the
clock e + 2j + 1 of each pair. Local's own coding: literal Rule 210 orbits from ts.rows_of, not GPT's coordinates.

PREDICTIONS (Local's, published before the run):
  FR-P1 (confidence 0.95, from the hand reading): for every case, tail and j <= w, (P_j, Q_j)(T_j) = (0, 1).
  FR-P2 (confidence 0.95): for every case, tail, j <= w and T_j <= s <= e + 2j + 1, P_j(s) = 0 and
         Q_j(s) XOR A_j(s) = A_j(0).
  FR-C0 (control, can say no): replacing T_j by T_j - 1 makes FR-P2 fail somewhere (the settling time is sharp).
OUTCOME: not yet run.
"""
import os
import random
import sys
import time
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule210_two_step_review as ts


def R0(i):
    return 1 if i >= 1 and i % 6 in (1, 5) else 0


def rows_list():
    rows = []
    for m in range(1, 64):
        L = [-(2 * j + 1) for j in range(6) if (m >> j) & 1]
        rows.append((max(-x for x in L), L))
    rng = random.Random(20261008)
    for R in (20, 30, 40):
        for _ in range(150):
            while True:
                L = [-i for i in range(1, R + 1, 2) if rng.random() < 0.5]
                if L and max(-x for x in L) == R - (1 - R % 2):
                    break
            rows.append((R, L))
    return rows


def main():
    t0 = time.time()
    nmax = 40 + 20 + 24
    ts.B, ts.OFF = 2 * nmax + 60, nmax + 30
    ts.MASK = (1 << (ts.B + 1)) - 1
    p1 = p2 = True
    sharp_fail = False
    bad = []
    cases = 0
    for R, L in rows_list():
        n = R + 20 + 24
        y = [i for i in range(1, n + 1) if R0(i) ^ (1 if -i in L else 0)]
        yset = set(y)
        rsy = ts.rows_of(L + y, n)
        Dy = lambda c, s: ts.bit(rsy[s], c - s)
        for e in range(2, R + 21, 2):
            tau = next(s for s in range(e) if Dy(e - 1, s) == 1)
            w = 0
            while ts.bit(rsy[tau], e + 1 - tau + 2 * w) == 0 and w < 10:
                w += 1
            span = 2 * w + 1
            if span <= 9:
                tails = list(product((0, 1), repeat=span))
            else:
                rng = random.Random(e * 7919 + R)
                tails = [tuple(rng.randint(0, 1) for _ in range(span)) for _ in range(16)]
            T = e + span
            for tail in tails:
                cases += 1
                sites = [i for i in y if i < e] + [e]
                for k, bit in enumerate(tail):
                    site = e + 1 + k
                    if (site in yset) ^ bit:
                        sites.append(site)
                rsx = ts.rows_of(L + sites, T)
                Dx = lambda c, s: ts.bit(rsx[s], c - s)
                for j in range(0, w + 1):
                    Tj = tau + j + 1
                    cP, cQ = e + 2 * j, e + 2 * j + 1
                    A0 = Dy(cQ, 0)
                    if (Dx(cP, Tj), Dx(cQ, Tj)) != (0, 1):
                        p1 = False
                        bad.append(('P1', L, e, tau, w, j, tail))
                    for s in range(Tj, cQ + 1):
                        if Dx(cP, s) != 0 or (Dx(cQ, s) ^ Dy(cQ, s)) != A0:
                            p2 = False
                            bad.append(('P2', L, e, tau, w, j, s, tail))
                            break
                    s = Tj - 1
                    if s >= 0 and (Dx(cP, s) != 0 or (Dx(cQ, s) ^ Dy(cQ, s)) != A0):
                        sharp_fail = True
    print('tail cases %d' % cases)
    print('FR-P1', 'HELD' if p1 else 'REFUTED', bad[:3])
    print('FR-P2', 'HELD' if p2 else 'REFUTED')
    print('FR-C0', 'PASS' if sharp_fail else 'FAIL')
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
