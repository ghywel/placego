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
OUTCOME, 2026-10-08 05:44 (M5, one run; transcript outside Git; 0.8 s). PROCEDURE NOTE: the predictions were
committed locally (82543a2, 05:44:09) before the run (05:44:11) and are unchanged, but the push of that commit was
rejected (non-fast-forward) and the run started in the same step, so they reached origin only after the run. Scored
as written. LB-C0 PASS: all 7 odd-supported left rows survive to depth 300. LB-P1 HELD: every one of the 56 rows with
a black even site dies, at depth equal to its nearest even black site (2, 4 or 6); this is G27's known
classification (compatible left halves are parity-sparse), seen at the first possible depth, not news. LB-P2 HELD:
no survivor ends in 60 white sites. LB-P3 HELD: the odd-supported rows keep exactly the empty row's count pattern
1, 2, 3, 6, 1, 2 (D1's period-6 tail check did not run: depth 300 has two survivors; a fault in the probe, not data).
So B with a finite left row reduces to the 7 odd-supported rows here, whose census looks like a unique realization
(G65's infinite parity-sparse seed). If that holds for every finite odd-supported left row, no finite seed realizes
0101 at all. Entry 29's automaton does not apply as it stands: these seeds are not periodic far from the wall.
ISO MODE (python3 tests/probes/lexicon/rule210_left_rows_census.py iso), predictions published before its run:
  Exploration after LB (descriptive, recorded here before any claim): for each odd-supported left row L, G65's seed
  is R with the mirror sites -i (i in L) flipped, so beyond max|L| it is R and the far field is R's periodic field.
  LB-I1 (blind, confidence 0.5): for each of the 7 odd-supported rows L and every depth d = 1 .. 300, the survivor
         set for L is exactly {u XOR mirror(L)} over the survivors u of the empty row (the census commutes with the
         reflection), so a base certificate for the empty row would serve every odd-supported L in this range.
  LB-I2 (control): the unique survivor at depth 299 for each L equals R XOR mirror(L) on sites 1 .. 299.
ISO OUTCOME, 2026-10-08 05:47 (M5, one run at commit bd96d6f; 1.1 s). LB-I1 REFUTED: the census does not commute
with the reflection; the survivor sets first differ at depth |l| for the nearest left site l whenever l != -1 (row
[-1] agrees at every depth), so frontier survivors are not mirrored and no uniform base follows. LB-I2 PASS: for
every odd-supported row the unique survivor at depth 299 is R XOR mirror(L), so each of the 7 rows is forced
through site 299 to G65's seed.
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


def iso():
    t0 = time.time()
    ts.B, ts.OFF = 2 * D + 60, D + 30
    ts.MASK = (1 << (ts.B + 1)) - 1

    def sets(left):
        alive, out = [[]], {}
        for d in range(1, D + 1):
            nxt = []
            for pre in alive:
                for v in (0, 1):
                    sites = left + [i + 1 for i, b in enumerate(pre + [v]) if b]
                    rs = ts.rows_of(sites, d)
                    if all(ts.bit(rs[t], 0) == t % 2 for t in range(d + 1)):
                        nxt.append(pre + [v])
            alive = nxt
            out[d] = set(tuple(p) for p in alive)
        return out

    base = sets([])
    i1 = i2 = True
    bad = []
    R = [1 if i % 6 in (1, 5) else 0 for i in range(1, D + 1)]
    for k in range(1, 8):
        left = [-(2 * j + 1) for j in range(3) if (k >> j) & 1]
        mine = sets(left)
        for d in range(1, D + 1):
            flip = lambda u: tuple(b ^ (1 if -(i + 1) in left else 0) for i, b in enumerate(u))
            if mine[d] != set(flip(u) for u in base[d]):
                i1 = False
                bad.append((left, d))
                break
        u299 = list(mine[299])
        want = tuple(R[i] ^ (1 if -(i + 1) in left else 0) for i in range(299))
        i2 &= len(u299) == 1 and u299[0] == want
    print('LB-I1', 'HELD' if i1 else 'REFUTED', bad[:7])
    print('LB-I2', 'PASS' if i2 else 'FAIL')
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    iso() if sys.argv[1:] == ['iso'] else main()
