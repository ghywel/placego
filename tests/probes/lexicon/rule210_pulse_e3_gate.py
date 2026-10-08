#!/usr/bin/env python3
"""rule210_pulse_e3_gate.py: E3, the e + 3 link of the near-wall pulse chain (Rule 210 question B), taken by Local at
GPT's request (GC473; GPT takes the e + 2 transient). Hand derivation below, checked here per choice against direct
simulation on actual G65 backgrounds. Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule210_pulse_e3_gate.py
COST:       to be recorded (expected under a minute).

THE DERIVATION (hand). Background y (G65, odd left row L), even first difference e, diagonals D_c(s) = x_s(c - s).
Write b = D_(e-1)(y), a = D_(e+1)(y), c = D_(e+3)(y); y's diagonals e and e + 2 are white. tau = first s with
b(s) = 1. The pulse on diagonal e is E(s) = [s <= tau] (GC472). On diagonal e + 1, O(0) = d (choice at site e + 1),
O(s) = a(s - 1) for 1 <= s <= tau + 1 and O(s) = a(tau) after (GC473, L281); assume the gate a(tau) = 0.
Diagonal e + 2 (choice f = x_0(e + 2)): Z(0) = f, Z(s+1) = E(s) XOR (1 XOR a(s) XOR O(s)) Z(s). For s >= tau + 1 this
is (1 XOR a(s)) Z(s), so Z keeps its value Z(tau + 1) until s_d = first s >= tau + 1 with a(s) = 1 (s_d <= e + 1 by
y's clock) and is 0 afterwards: the e + 2 clock passes automatically (GPT's transient).
Diagonal e + 3 (choice g): Q(0) = g, Q(s+1) = O(s) XOR (1 - Z(s)) Q(s) XOR Z(s) c(s). Z(0) = 1 or Z(1) = 1 always
(Z(1) = 1 XOR (1 XOR a(0) XOR d) f), so g is erased. After s_d, Z = O = 0 and Q is frozen, so the e + 3 clock
holds exactly when Q_final = 0, where:
  if Z(tau + 1) = 1:  Q_final = c(s_d);
  otherwise, with s* the last s <= tau with Z(s) = 1:  Q_final = O(s*) XOR c(s*) XOR (XOR of O(s), s* < s <= tau).
Far field, e = 2 (mod 6): tau = 0, a(0) = 0, a(1) = 1 (s_d = 1), c(0) = c(1) = 1, so every (d, f) gives Q_final = 1:
killed at e + 3, as in CL's census.

PREDICTIONS (Local's, published before the run), on the rows of SB (all 63 odd rows R <= 12; 150 random rows at each
of R = 20, 30, 40, same seed) and every even e <= R + 20 whose e + 1 gate passes:
  E3-C0 (control): for every case and every choice (d, f, g), the direct simulation keeps the clock through e + 3
         exactly when the formula gives Q_final = 0.
  E3-C1 (control): the choice g never changes the outcome (erasure).
  E3-P1 (blind, confidence 0.7): in the far field (e >= R + 4, so the cells read sit beyond the mirrored region),
         every gate-passing deviation is killed at e + 3 for every (d, f).
  D1 (descriptive): how many near-wall gate-passing cases survive e + 3, and for which (d, f).
OUTCOME: not yet run.
"""
import os
import random
import sys
import time

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
    ts.B, ts.OFF = 2 * 80 + 40, 100
    ts.MASK = (1 << (ts.B + 1)) - 1
    c0 = c1 = p1 = True
    cases = passed = near_surv = 0
    surv_choices = {}
    for R, L in rows_list():
        n = R + 24
        y = [i for i in range(1, n + 1) if R0(i) ^ (1 if -i in L else 0)]
        rsy = ts.rows_of(L + y, n)
        D = lambda c, s: ts.bit(rsy[s], c - s)
        yset = set(y)
        for e in range(2, R + 21, 2):
            cases += 1
            b = lambda s: D(e - 1, s)
            a = lambda s: D(e + 1, s)
            c = lambda s: D(e + 3, s)
            tau = next(s for s in range(e) if b(s) == 1)
            if a(tau) == 1:
                continue
            passed += 1
            sd = next(s for s in range(tau + 1, e + 2) if a(s) == 1)
            outcomes = {}
            for d in (0, 1):
                for f in (0, 1):
                    O = lambda s: d if s == 0 else (a(s - 1) if s <= tau + 1 else a(tau))
                    Z = [f]
                    for s in range(0, tau + 1):
                        E = 1
                        Z.append(E ^ ((1 ^ a(s) ^ O(s)) & Z[s]))
                    if Z[tau + 1] == 1:
                        qf = c(sd)
                    else:
                        sstar = max(s for s in range(0, tau + 1) if Z[s] == 1)
                        qf = O(sstar) ^ c(sstar)
                        for s in range(sstar + 1, tau + 1):
                            qf ^= O(s)
                    for g in (0, 1):
                        sites = [i for i in y if i < e] + [e]
                        if (e + 1 in yset) ^ d:
                            sites.append(e + 1)
                        if f:
                            sites.append(e + 2)
                        if (e + 3 in yset) ^ g:
                            sites.append(e + 3)
                        rs = ts.rows_of(L + sites, e + 3)
                        ok = all(ts.bit(rs[t], 0) == t % 2 for t in range(e + 4))
                        c0 &= (ok == (qf == 0))
                        outcomes.setdefault((d, f), set()).add(ok)
            c1 &= all(len(v) == 1 for v in outcomes.values())
            alive = [k for k, v in outcomes.items() if True in v]
            if e >= R + 4 and alive:
                p1 = False
            if e < R + 4 and alive:
                near_surv += 1
                for k in alive:
                    surv_choices[k] = surv_choices.get(k, 0) + 1
    print('cases %d, gate passed %d, near-wall survivors of e + 3: %d, by (d, f): %s'
          % (cases, passed, near_surv, surv_choices))
    print('E3-C0', 'PASS' if c0 else 'FAIL')
    print('E3-C1', 'PASS' if c1 else 'FAIL')
    print('E3-P1', 'HELD' if p1 else 'REFUTED')
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
