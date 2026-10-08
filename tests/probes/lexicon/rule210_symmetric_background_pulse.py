#!/usr/bin/env python3
"""rule210_symmetric_background_pulse.py: SB, the first route of L280 as assigned in GPT's GC472 coordination: on
ACTUAL symmetric backgrounds, how long can a near-wall first deviation live? Local's claimed bounded exploration
toward the uniform near-wall obligation for Rule 210 question B (GC471, GC472; entries 29 and 31). Research, not a
claim that this route works. Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule210_symmetric_background_pulse.py
COST:       to be recorded (expected a few minutes).

Backgrounds are actual, not relaxed windows: for an odd-supported left row L in [-R, -1], y is G65's realization,
left row L and right seed R_0 XOR mirror(L) (R_0 = sites coprime to 6), evolved by literal Rule 210. Every window this
probe reads comes from such a y; no arbitrary window is used, so nothing here over-relaxes the target (GPT's caution).
Rows: all 63 odd-supported rows with R <= 12, and 150 random odd-supported rows at each of R = 20, 30, 40 (seeded).
For each row and each even first-deviation site e = 2 .. R + 20: x agrees with y on sites 1 .. e-1, has x_0(e) = 1
(y_0(e) = 0 at even e), and EVERY choice of the next K = 8 sites is enumerated by depth-first search (a branch is
kept while the clock holds through its depth). Odd first deviations are not run: GC472 kills them at their own clock.

PREDICTIONS (Local's, published before the run):
  SB-C0 (control, GC472): every (L, e) keeps the clock at depth e (the pulse dies before its own clock).
  SB-C1 (control, L281's proposed lemma): survivors exist at depth e + 1 exactly when y's cell D_(e+1)(tau) is
         white, tau being the first black time of y's diagonal e - 1.
  SB-P1 (blind, confidence 0.6): every first deviation dies by depth e + 3, for every tail choice, every row and
         every even e <= R + 20 (the far field's three-diagonal life holds near the wall too).
  SB-P2 (blind, confidence 0.5): no (L, e) has a survivor at depth e + 8. Any survivor there is reported as the
         failure witness (row, e, surviving tails), a candidate second realization to chase.
  D1 (descriptive): the distribution of the deviation's life (last surviving depth minus e) by e - R and by tau.
OUTCOME: not yet run.
"""
import os
import random
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule210_two_step_review as ts

K = 8


def R0(i):
    return 1 if i >= 1 and i % 6 in (1, 5) else 0


def setup(maxsite):
    ts.B, ts.OFF = 2 * maxsite + 40, maxsite + 20
    ts.MASK = (1 << (ts.B + 1)) - 1


def background(L, n):
    right = [i for i in range(1, n + 1) if R0(i) ^ (1 if -i in L else 0)]
    return right


def clock_ok(sites, d):
    rs = ts.rows_of(sites, d)
    return all(ts.bit(rs[t], 0) == t % 2 for t in range(d + 1)), rs


def study(L, R):
    out = []
    ybits = background(L, R + 20 + K + 2)
    yset = set(ybits)
    rsy = ts.rows_of(L + ybits, R + 20 + K + 2)
    D = lambda c, s: ts.bit(rsy[s], c - s)
    for e in range(2, R + 21, 2):
        base = [i for i in ybits if i < e] + [e]
        tau = next(s for s in range(0, e) if D(e - 1, s) == 1)
        predict1 = D(e + 1, tau) == 0
        alive = [base]
        life = 0
        ok_e, _ = clock_ok(L + base, e)
        for k in range(1, K + 1):
            d = e + k
            nxt = []
            for pre in alive:
                for v in (0, 1):
                    cand = pre + ([d] if v else [])
                    if clock_ok(L + cand, d)[0]:
                        nxt.append(cand)
            alive = nxt
            if k == 1:
                surv1 = bool(alive)
            if not alive:
                break
            life = k
        out.append((e, tau, ok_e, predict1, surv1, life, alive))
    return out


def main():
    t0 = time.time()
    setup(40 + 20 + K + 10)
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
    c0 = c1 = p1 = p2 = True
    lifes = Counter()
    by_tau = Counter()
    witness = []
    n = 0
    for R, L in rows:
        for e, tau, ok_e, predict1, surv1, life, alive in study(L, R):
            n += 1
            c0 &= ok_e
            c1 &= (predict1 == surv1)
            if life > 3:
                p1 = False
            if life >= K and alive:
                p2 = False
                witness.append((L, e, [sorted(set(a) - set(range(e))) for a in alive][:3]))
            lifes[life] += 1
            by_tau[(min(tau, 4), life)] += 1
    print('cases (row, e): %d over %d rows' % (n, len(rows)))
    print('life distribution:', dict(sorted(lifes.items())))
    print('by (min(tau,4), life):', dict(sorted(by_tau.items())))
    print('SB-C0', 'PASS' if c0 else 'FAIL')
    print('SB-C1', 'PASS' if c1 else 'FAIL')
    print('SB-P1', 'HELD' if p1 else 'REFUTED')
    print('SB-P2', 'HELD' if p2 else 'REFUTED', witness[:3])
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
