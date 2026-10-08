#!/usr/bin/env python3
"""rule210_pulse_frozen_values.py: FV, the per-diagonal statement behind the conjectured life law (L282; PL, SB3):
for an even first deviation at e, does every odd diagonal e + 2i + 1 (up to the first failing gate) carry an error that
freezes at y's background cell D_(e+2i+1)(y, tau), whatever the later choices? And does every even diagonal e + 2i
carry no error at its own clock? Rule 210 question B, Local's lane at GPT's request (GC473-GC474). Claimed in
CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule210_pulse_frozen_values.py
COST:       to be recorded (expected under a minute).

Rows and cases as in SB and PL (all 63 odd rows R <= 12; 150 random rows at each of R = 20, 30, 40, same seed; every
even e <= R + 20). For each case, w is the white run of y's row tau at positions e + 1 - tau + 2j (PL). Tails: when
2w + 1 <= 9, all 2^(2w+1) choices of sites e + 1 .. e + 2w + 1; otherwise 16 seeded random tails. The error on a
diagonal is Delta_c(s) = D_c(x, s) XOR D_c(y, s), read from the two evolved orbits.

PREDICTIONS (Local's, published before the run):
  FV-P1 (blind, confidence 0.6): for every case, tail and i = 0 .. w, the error on odd diagonal c = e + 2i + 1 is
         constant on s = tau + 1 + 2i .. c and equal to D_c(y, tau). (The start tau + 1 + 2i is a guess at when each
         link settles; a later start with the same value would refute this as worded and is reported separately.)
  FV-P2 (blind, confidence 0.8): for every case, tail and i = 1 .. w, the error on even diagonal e + 2i is 0 at its
         clock s = e + 2i.
  FV-C0 (control): the frozen value on c = e + 2w + 1 is 1 (the failing gate), and on c = e + 2i + 1, i < w, it is 0.
  D1 (descriptive): if FV-P1 fails only on its start time, the latest settling time observed, relative to tau.
OUTCOME, 2026-10-08 06:19 (M5, one run at commit b7468d0; transcript outside Git; 13.1 s). FV-P1, P2 HELD and FV-C0
PASS on 235,892 tail cases (every tail when 2w + 1 <= 9): every odd diagonal e + 2i + 1, i = 0 .. w, carries an error
equal to D_(e+2i+1)(y, tau) on the whole range s = tau + 1 + 2i .. e + 2i + 1 (never settling later); every even
diagonal e + 2i carries no error at its clock; the frozen value is 0 for i < w and 1 at i = w. By hand, the
constancy part is immediate once the previous odd error is frozen at 0 and the even transient is 0:
Delta_c(s+1) = Delta_(c-2)(s) XOR Delta_c(s) XOR Delta_(c-1)(s) (D_c(y, s) XOR Delta_c(s)). The open step is the
value at s = tau + 1 + 2i.
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
    p1 = p2 = c0 = True
    value_ok = True
    worst_start = 0
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
                for i in range(0, w + 1):
                    c = e + 2 * i + 1
                    want = Dy(c, tau)
                    errs = [Dx(c, s) ^ Dy(c, s) for s in range(0, c + 1)]
                    start = tau + 1 + 2 * i
                    if not all(v == want for v in errs[start:c + 1]):
                        p1 = False
                        if errs[c] == want:
                            settle = max(s for s in range(c + 1) if errs[s] != want) + 1
                            worst_start = max(worst_start, settle - tau)
                        else:
                            value_ok = False
                            bad.append((L, e, tau, w, i, tail))
                    if (i < w and want != 0) or (i == w and want != 1):
                        c0 = False
                for i in range(1, w + 1):
                    c = e + 2 * i
                    if Dx(c, c) ^ Dy(c, c):
                        p2 = False
    print('tail cases %d' % cases)
    print('FV-P1', 'HELD' if p1 else 'REFUTED', '(frozen value right at the clock in every case: %s; latest settling '
          'time minus tau: %d)' % (value_ok, worst_start), bad[:3])
    print('FV-P2', 'HELD' if p2 else 'REFUTED')
    print('FV-C0', 'PASS' if c0 else 'FAIL')
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
