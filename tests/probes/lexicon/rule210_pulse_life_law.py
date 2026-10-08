#!/usr/bin/env python3
"""rule210_pulse_life_law.py: PL, a conjectured law for the life of a near-wall first deviation (Rule 210 question B),
from E3 (rule210_pulse_e3_gate.py) and GC472-GC473. Local's lane at GPT's request. Claimed in CLOUD-LOCAL.md with
these predictions pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule210_pulse_life_law.py
COST:       to be recorded (expected a few minutes).

Where it comes from. With an even first difference e and tau the first black time of y's diagonal e - 1, the e + 1
gate is D_(e+1)(y, tau) = 0 (L281, GC473), and E3's derivation gives the e + 3 gate as Q_final = D_(e+3)(y, tau) by
hand: c(s_d) = c(tau) because y's diagonal e + 3 accumulates a, which is white on [tau, s_d), and the other branch
Z(tau + 1) = 0 forces a(tau - 1) = 0, so O(tau) XOR c(tau) = c(tau). E3 also found every (d, f) choice surviving
together. Both gates read y's row tau at the visible positions e + 1 - tau, e + 3 - tau.

CONJECTURE (the life law). The deviation keeps the clock through depth e + 2w and fails at e + 2w + 1, for every
choice of every later site, where w is the length of the run of white cells of y's row tau at the positions
e + 1 - tau + 2j, j = 0, 1, 2, .... Far from the wall that row is black at two of every three such positions, so w is
finite and every first deviation dies: if the law holds for every finite odd left row, each has a unique 0101
realization (with GC471), and no finite seed with a finite left row realizes 0101. This probe tests the law; it
proves nothing.

PREDICTIONS (Local's, published before the run), on SB's rows (all 63 odd rows R <= 12; 150 random rows at each of
R = 20, 30, 40, same seed) and every even e <= R + 20:
  PL-P1 (blind, confidence 0.6): the life (last depth that keeps the clock, minus e) equals 2w exactly. Tested on
         three tails (y's own bits, their complement, and a seeded random tail); all tails are enumerated only
         through depth e + 10, by PL-P2.
  PL-P2 (blind, confidence 0.6): every tail choice survives until the death: at depth e + k, 1 <= k <= min(2w, 10),
         exactly 2^k of the 2^k tails keep the clock.
  PL-C0 (control): w = 0 exactly when the e + 1 gate fails, and w >= 1 with D_(e+3)(y, tau) = 1 exactly when E3's
         gate kills at e + 3.
OUTCOME, 2026-10-08 06:16 (M5, one run at commit fb97412; transcript outside Git; 8.8 s). PL-P1, P2 HELD and PL-C0
PASS on all 12,138 cases: the life equals 2w on all three tails tested; all 2^k tails keep the clock at every depth
e + k <= min(e + 2w, e + 10); w = 0 and w = 1 match the e + 1 and e + 3 gates. w histogram: 0: 6,938, 1: 3,476,
2: 921, 3: 435, 4: 208, 5: 89, 6: 37, 7: 19, 8: 8, 9: 5, 10: 2 (SB's life distribution is exactly 2w). With SB3's
368 all-tail deep cases this is strong evidence for the life law; it is not a proof.
"""
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule210_two_step_review as ts

KCOUNT = 10
CAP = 120


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


def ok_through(L, sites, d):
    rs = ts.rows_of(L + sites, d)
    return all(ts.bit(rs[t], 0) == t % 2 for t in range(d + 1))


def main():
    t0 = time.time()
    n_max = 40 + 20 + CAP + 4
    ts.B, ts.OFF = 2 * n_max + 60, n_max + 30
    ts.MASK = (1 << (ts.B + 1)) - 1
    p1 = p2 = c0 = True
    bad1, bad2 = [], []
    hist = {}
    cases = 0
    for R, L in rows_list():
        n = R + 20 + CAP + 4
        y = [i for i in range(1, n + 1) if R0(i) ^ (1 if -i in L else 0)]
        yset = set(y)
        rsy = ts.rows_of(L + y, n)
        D = lambda c, s: ts.bit(rsy[s], c - s)
        for e in range(2, R + 21, 2):
            cases += 1
            tau = next(s for s in range(e) if D(e - 1, s) == 1)
            w = 0
            while ts.bit(rsy[tau], e + 1 - tau + 2 * w) == 0 and w < CAP:
                w += 1
            hist[w] = hist.get(w, 0) + 1
            gate1 = D(e + 1, tau) == 0
            gate3 = D(e + 3, tau) == 0
            c0 &= ((w == 0) == (not gate1)) and ((w == 1) == (gate1 and not gate3))
            base = [i for i in y if i < e] + [e]
            # full-tail counts for the first KCOUNT sites
            alive = [base]
            for k in range(1, min(2 * w, KCOUNT) + 1):
                d = e + k
                nxt = []
                for pre in alive:
                    for v in (0, 1):
                        cand = pre + ([d] if v else [])
                        if ok_through(L, cand, d):
                            nxt.append(cand)
                alive = nxt
                if len(alive) != 2 ** k:
                    p2 = False
                    bad2.append((L, e, k, len(alive)))
                    break
            # exact life: the law says every tail behaves alike, so follow two extreme tails and one random tail
            rng = random.Random(e * 1000 + R)
            tails = [lambda i: (i in yset), lambda i: not (i in yset), lambda i: rng.random() < 0.5]
            lives = []
            for tf in tails:
                sites = list(base)
                life = 0
                for k in range(1, 2 * w + 3):
                    d = e + k
                    if tf(d):
                        sites.append(d)
                    if ok_through(L, sites, d):
                        life = k
                    else:
                        break
                lives.append(life)
            if any(l != 2 * w for l in lives):
                p1 = False
                bad1.append((L, e, tau, w, lives))
    print('cases %d; w histogram %s' % (cases, dict(sorted(hist.items()))))
    print('PL-P1', 'HELD' if p1 else 'REFUTED', bad1[:4])
    print('PL-P2', 'HELD' if p2 else 'REFUTED', bad2[:4])
    print('PL-C0', 'PASS' if c0 else 'FAIL')
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
