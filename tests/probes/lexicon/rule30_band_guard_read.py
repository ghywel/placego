#!/usr/bin/env python3
"""rule30_band_guard_read.py: Local's second read of GPT's GC1197 (the train-departure guard on an actual band, at any
crop time and birth age), and the fields GPT asked for from the existing R_real(125) = 21 witness.

GC1197: if the actual initial left row agrees with the train reference A^p (A^0 = (0110010)^inf, A^1 = (1100001)^inf,
A^p_t(j) = R_((t + 3p) mod 4)[(-j) mod 7]) at every depth below a white band [d, E], E = d + L - 1, and the clock covers
the band, then L >= 4 (p = 0) or L >= 6 (p = 1) forces d mod 56 into seven classes:
p0 {11, 12, 13, 17, 35, 36, 37}, p1 {10, 11, 12, 13, 14, 30, 50}; at one cell shorter a cell outside the band can repair
the next check.

RUN-ON:     cpu, standard library and numpy; seconds.
COMMAND:    python3 tests/probes/lexicon/rule30_band_guard_read.py

Record searched (record_find, 2026-10-13 19:08 BST): 'train ray|train-ray' and 'tube' as in rule30_train_end_tube.py;
the witness is the committed fixture site/wolframcollatzmahler/data/records.json (depth 125, from
rule30_local_record_traces.txt, L643).

PREDICTIONS (written 2026-10-13 19:33 BST, before any run).
  B1 must hold (the rebasing): the clamped evolution of A^0 (wall t mod 2) and A^1 (wall (t + 1) mod 2) from their
     initial rows follows A^p_t(j) for t <= 60 and shows the visible code (10)^n at white ticks.
  B2 must hold (the guard, by direct evolution with no formula): for d = 8 .. 8 + 112 (two periods), L = 4 (p0) and
     L = 6 (p1), the row A^p on 1 .. d - 1, white on [d, E], and 3 random tails beyond E, passes the clock and has no 11
     through tick ell (the first arrival and the next black tick) for some tail exactly when d mod 56 is in GPT's set,
     and the verdict does not depend on the tail.
  B3 must hold (the horizon is exact): at L = 3 (p0) or L = 5 (p1) some d outside the set has a tail that passes
     through tick ell.
  B4 (the witness fields, reported): forced_row(visible, phase) reproduces the fixture's left row; the first departure
     depth from A^p; the canonical first-nonwhite birth age a (GC1174's ancestors); N = a + p, s = d - a + 1, the gap
     length and type at the birth parent. GPT's prediction (0.8): the departure is well before depth 125.

OUTCOME (2026-10-13 19:34 BST, M5, 3 s; machine output quoted): B1 HELD, B2 HELD, B3 HELD, B4 reported.
  B4: forced row = fixture HELD. Witness d=125 L=21 phase 1: first departure from A^1 at depth 6 (GPT's prediction of an
     early departure held, so GC1197's premise does not cover it); birth age a=1 (deficit 62 of m + 1 = 63); N=2,
     s=125, gap 123, type Q; first sample 1. Diagnostic after the run (a scratch script, the same fixture): the witnesses
     for 126, 127 and 128 (the same phase-1 configuration) are age-1 Q births with parent black runs from d of length at
     least L + 1 = 21, 20, 19 (determined to depth 146); the 133 witness (phase 0) is an age-1 P birth, white at 133 and
     black from 134 for at least 23 cells.
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rule30_extremal_p_corner_read import step, depth1_column, forced_row      # Local's own (L668)

RR = ['0100110', '1111101', '0000001', '1000011']
SETS = {0: {11, 12, 13, 17, 35, 36, 37}, 1: {10, 11, 12, 13, 14, 30, 50}}
LMIN = {0: 4, 1: 6}


def Aref(p, t, j):
    return int(RR[(t + 3 * p) % 4][(-j) % 7])


def two_tick_pass(row, p, ell):
    """Clock at black ticks and no 11 at white ticks over ticks 0 .. ell (row: depths 1 .. n)."""
    x = depth1_column([None] + row + [0], p, ell)
    prev = None
    for t in range(ell + 1):
        if (t + p) % 2 == 1:
            if x[t] != 1:
                return False
        else:
            v = 1 - x[t]
            if v == 1 and prev == 1:
                return False
            prev = v
    return True


def main():
    ok = {}
    b1 = True
    for p in (0, 1):
        row = [None] + [Aref(p, 0, j) for j in range(1, 400)]
        x = depth1_column(row, p, 60)
        r = row
        for t in range(61):
            b1 &= all(r[j] == Aref(p, t, j) for j in range(1, 400 - t - 2))
            r = step(r, (t + p) % 2)
        vis = ''.join(str(1 - x[t]) for t in range(61) if (t + p) % 2 == 0)
        b1 &= vis == ('10' * 40)[:len(vis)]
    ok['B1'] = b1
    rng = random.Random(1197)
    b2 = b3 = True
    b3_seen = {0: False, 1: False}
    for p in (0, 1):
        for L, mode in ((LMIN[p], 'guard'), (LMIN[p] - 1, 'short')):
            for d in range(8, 8 + 113):
                E = d + L - 1
                ell = next(j for j in range(d, d + 8) if Aref(p, 0, j) == 1)
                verdicts = set()
                for _ in range(3 if mode == 'guard' else 8):
                    row = [Aref(p, 0, j) for j in range(1, d)] + [0] * L + [rng.randrange(2) for _ in range(ell + 4)]
                    verdicts.add(two_tick_pass(row, p, ell))
                if mode == 'guard':
                    b2 &= len(verdicts) == 1 and (True in verdicts) == (d % 56 in SETS[p])
                elif True in verdicts and d % 56 not in SETS[p]:
                    b3_seen[p] = True
    ok['B2'] = b2
    ok['B3'] = b3_seen[0] and b3_seen[1]
    data = json.load(open(os.path.join(HERE, '..', '..', '..', 'site', 'wolframcollatzmahler', 'data', 'records.json')))
    w = [r for r in data['rows'] if r['depth'] == 125][0]
    p, d, L = w['phase'], w['depth'], w['L']
    E = d + L - 1
    vis = [int(c) for c in w['visible']]
    left = [int(c) for c in w['left']]
    fr = forced_row(vis, p)
    ok['B4 forced row = fixture'] = fr[1:len(left) + 1] == left
    dep = next(j for j in range(1, len(left) + 1) if left[j - 1] != Aref(p, 0, j))
    a = None
    for n in range(1, (d - p) // 2 + 2):
        An = forced_row([0] * ((n + p) // 2) + vis, (p + n) % 2)
        if not all(An[j] == 0 for j in range(d - n, E + n + 1)):
            a = n
            break
    N = a + p
    s = d - a + 1
    par = forced_row([0] * ((a + p) // 2) + vis, (p + a) % 2)
    typ = 'Q' if par[s] == 1 else ('P' if par[s - 1] == 1 and par[s] == 0 else '?')
    m = (d - p) // 2
    print('GC1197 read:', {k: ('HELD' if v else 'FAILED') for k, v in ok.items()})
    print('B4 witness d=%d L=%d phase %d: first departure from A^%d at depth %d; birth age a=%d (deficit j=%d of m+1=%d);'
          ' N=%d, s=%d, gap g=%d, type %s; first sample beta=%d'
          % (d, L, p, p, dep, a, m + 1 - a, m + 1, N, s, s - N, typ, vis[0]))
    print('   parent row depths 1..%d: %s' % (s + 3, ''.join(map(str, par[1:s + 4]))))


if __name__ == '__main__':
    main()
