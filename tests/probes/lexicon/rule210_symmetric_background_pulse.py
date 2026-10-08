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
OUTCOME, 2026-10-08 06:09 (M5, one run at commit 8b0f1af; transcript outside Git; 5.2 s). 12,138 (row, e) cases
over 513 rows. SB-C0 PASS and SB-C1 PASS: L281's next-diagonal test predicts survival at e + 1 in every case.
SB-P1 REFUTED and SB-P2 REFUTED: lives are 0, 2, 4, 6 and 8 (6,938, 3,476, 921, 435, 368 cases), and 368 deviations
are still alive at the cap e + 8. First witness: L = {-5, -7}, e = 2. Mirroring L removes sites 5 and 7 from R_0, so
y is white on sites 2 .. 10 and the deviation lives in that local white stretch. Every witness row has radius >= 7,
outside entry 31. Whether such a deviation lives for ever (a second realization) is the next question.
CHASE MODE (python3 tests/probes/lexicon/rule210_symmetric_background_pulse.py chase), predictions published before
its run, for the three first witness rows {-5,-7}, {-1,-5,-7}, {-5,-7,-11}: full census of right prefixes to 300.
  SB2-P1 (blind, confidence 0.5): at least one of the three has two or more survivors at depth 299 (a second
         realization is likely, so uniqueness fails beyond radius 6).
  SB2-P2 (blind, confidence 0.2): some survivor at depth 299 ends in 60 white sites (a finite-seed candidate for B).
  SB2-C0 (control): G65's background y is among the survivors at depth 299 for each row.
CHASE OUTCOME, 2026-10-08 06:10 (M5, one run at commit 9f33f10; 0.4 s). SB2-P1 REFUTED, SB2-P2 REFUTED, SB2-C0
PASS: each of the three witness rows keeps the 1, 2, 3, 6, 1, 2 pattern and has exactly one survivor at depth 299, y
itself (the other depth-300 survivor differs only at the frontier site 300). The long-lived deviations die later.
LIFE MODE (python3 tests/probes/lexicon/rule210_symmetric_background_pulse.py life), predictions published before
its run: every SB case still alive at e + 8 (368 cases) is followed by depth-first search to e + 200, and its exact
life is compared with w, the number of consecutive odd sites e+1, e+3, ... at which y_0 is white.
  SB3-P1 (blind, confidence 0.8): every one of the 368 deviations dies by e + 200.
  SB3-P2 (blind, confidence 0.5): the exact life is a nondecreasing function of w alone (equal w, equal life).
  D2 (descriptive): the table of (w, life) pairs and the longest life found.
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


def chase():
    t0 = time.time()
    Dd = 300
    setup(Dd + 40)
    out = []
    p1 = p2 = False
    c0 = True
    for L in ([-5, -7], [-1, -5, -7], [-5, -7, -11]):
        alive, counts = [[]], {}
        for d in range(1, Dd + 1):
            nxt = []
            for pre in alive:
                for v in (0, 1):
                    cand = pre + [v]
                    sites = L + [i + 1 for i, b in enumerate(cand) if b]
                    if clock_ok(sites, d)[0]:
                        nxt.append(cand)
            alive = nxt
            counts[d] = len(alive)
            if len(alive) > 20000:
                break
        y = [R0(i) ^ (1 if -i in L else 0) for i in range(1, Dd + 1)]
        at = counts.get(299)
        surv = alive if max(counts) >= 299 else []
        if at is not None and at >= 2:
            p1 = True
        if any(not any(p[-60:]) for p in surv):
            p2 = True
        c0 &= any(p[:299] == y[:299] for p in surv)
        diffs = [[i + 1 for i in range(len(p)) if p[i] != y[i]][:12] for p in surv[:4]]
        out.append((L, [counts[d] for d in sorted(counts)[-6:]], max(counts), diffs))
    for L, tail, last, diffs in out:
        print('L %s: counts at last depths %s (deepest %d); first differences from y of up to 4 survivors: %s'
              % (L, tail, last, diffs))
    print('SB2-P1', 'HELD' if p1 else 'REFUTED')
    print('SB2-P2', 'HELD' if p2 else 'REFUTED')
    print('SB2-C0', 'PASS' if c0 else 'FAIL')
    print('%.1f s' % (time.time() - t0))


def life_mode():
    t0 = time.time()
    KK = 200
    setup(40 + 20 + KK + 10)
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
    table = Counter()
    by_w = {}
    longest = None
    died = True
    n = 0
    for R, L in rows:
        for e, tau, ok_e, predict1, surv1, life, alive in study(L, R):
            if life < K:
                continue
            n += 1
            ybits = set(background(L, e + KK + 2))
            w = 0
            while (e + 1 + 2 * w) not in ybits and w < 100:
                w += 1
            alive2 = [[i for i in ybits if i < e] + [e]]
            ex = 0
            for k in range(1, KK + 1):
                d = e + k
                nxt = []
                for pre in alive2:
                    for v in (0, 1):
                        cand = pre + ([d] if v else [])
                        if clock_ok(L + cand, d)[0]:
                            nxt.append(cand)
                alive2 = nxt
                if not alive2:
                    break
                ex = k
            if alive2:
                died = False
            table[(w, ex)] += 1
            by_w.setdefault(w, set()).add(ex)
            if longest is None or ex > longest[0]:
                longest = (ex, L, e, w)
    p2 = all(len(v) == 1 for v in by_w.values())
    ws = sorted(by_w)
    p2 = p2 and all(max(by_w[a]) <= min(by_w[b]) for a, b in zip(ws, ws[1:]))
    print('cases followed: %d' % n)
    print('(w, life) table:', dict(sorted(table.items())))
    print('longest life:', longest)
    print('SB3-P1', 'HELD' if died else 'REFUTED')
    print('SB3-P2', 'HELD' if p2 else 'REFUTED')
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    m = sys.argv[1:]
    chase() if m == ['chase'] else life_mode() if m == ['life'] else main()
