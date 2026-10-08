#!/usr/bin/env python3
"""rule210_left_rows_census.py: LB, the real-orbit census beyond the empty left row: for every nonempty initial left
row supported on sites -6 .. -1 (63 rows), enumerate every right prefix that keeps the 0101 clock through depth 300.
A cheap step toward question B with a nonempty finite left row (entry 29 settled the empty one). Local's census lane.
Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule210_left_rows_census.py
COST:       to be recorded (expected a minute or two).

With the left row fixed and every other left site white, the centre at time t depends on initial sites -t .. t, so
the census adds right site d at depth d exactly as in TS and CL, with the left row included in every evolution. A
left row with no survivor at some depth admits no full 0101 orbit at all: a finite certificate. "Odd-supported" left
rows (black only at odd sites) have a parity-sparse right realization by G65, a control.

PREDICTIONS (Local's, published before the run):
  LB-C0 (control, G65): every odd-supported left row (7 of the 63) has at least one survivor at depth 300.
  LB-P1 (blind, confidence 0.5): at least one of the 63 left rows has no survivor at some depth <= 300 (some
         nonempty left rows admit no 0101 orbit at all).
  LB-P2 (blind, confidence 0.7): no survivor at depth 300, for any left row, has its last 60 right sites all white
         (no finite-looking right seed).
  LB-P3 (blind, confidence 0.6): for every left row with survivors at 300, the survivor count stays at most 6 at
         every depth from 30 on (the census stays a small machine, as for the empty row).
  D1 (descriptive): per left row, the first dying depth or the survivor counts at 295 .. 300, and whether the unique
         survivors (where unique) are eventually periodic with period 6 over sites 200 .. 300.
OUTCOME: not yet run.
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule210_two_step_review as ts

D = 300
CAP = 5000


def census(left):
    alive, counts, died = [[]], {}, None
    for d in range(1, D + 1):
        nxt = []
        for pre in alive:
            for v in (0, 1):
                sites = left + [i + 1 for i, b in enumerate(pre + [v]) if b]
                rs = ts.rows_of(sites, d)
                if all(ts.bit(rs[t], 0) == t % 2 for t in range(d + 1)):
                    nxt.append(pre + [v])
        alive = nxt
        counts[d] = len(alive)
        if not alive:
            died = d
            break
        if len(alive) > CAP:
            return alive, counts, 'CAP'
    return alive, counts, died


def main():
    t0 = time.time()
    ts.B, ts.OFF = 2 * D + 60, D + 30
    ts.MASK = (1 << (ts.B + 1)) - 1
    rows = []
    for m in range(1, 64):
        rows.append([-(k + 1) for k in range(6) if (m >> k) & 1])
    c0 = p1 = False
    c0 = True
    p2 = p3 = True
    report = []
    for left in rows:
        odd = all(i % 2 for i in left)
        alive, counts, died = census(left)
        if died == 'CAP':
            report.append((left, 'CAP at depth %d' % max(counts)))
            p3 = False
            continue
        if died is not None:
            p1 = True
            if odd:
                c0 = False
            report.append((left, 'dies at %d' % died))
            continue
        if any(counts[d] > 6 for d in range(30, D + 1)):
            p3 = False
        for p in alive:
            if not any(p[-60:]):
                p2 = False
        per = None
        if len(alive) == 1:
            s = alive[0]
            per = all(s[i] == s[i + 6] for i in range(199, D - 6))
        report.append((left, 'alive: counts 295..300 %s; period-6 tail %s' %
                       ([counts[d] for d in range(295, D + 1)], per)))
    for left, msg in report:
        print('left %s: %s' % (left, msg))
    print('LB-C0', 'PASS' if c0 else 'FAIL')
    print('LB-P1', 'HELD' if p1 else 'REFUTED')
    print('LB-P2', 'HELD' if p2 else 'REFUTED')
    print('LB-P3', 'HELD' if p3 else 'REFUTED')
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
