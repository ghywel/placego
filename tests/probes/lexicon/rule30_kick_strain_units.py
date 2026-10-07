#!/usr/bin/env python3
"""rule30_kick_strain_units.py: KT2b, KT2's instances (rule30_kick_strain_kissat.py) with implied unit clauses from
LK (rule30_locked_core_lock.py), to make the N = 560 instances tractable (row 6.1, drawn under draw-and-work on
2026-10-07 22:46; Local's claim in CLOUD-LOCAL.md with these predictions pushed before the run).

RUN-ON:     cpu, one kissat process (RK and KT2 hold the other nine cores)
COMMAND:    python3 tests/probes/lexicon/rule30_kick_strain_units.py
COST:       to be recorded; each solve is capped at 1,800 s.

Why the units are implied, not assumed. In a kick instance, column 1 follows the wheel at even phase d on rows t0 ..
s - 1, so those rows of columns 0 .. 15 form a walk in the complete width-15 graph (the configuration's own column 16
is the free input). A row with r edges of that walk on each side survives r rounds of the in/out trimming. At width
15, column x is single-valued at every phase among the r_x-round survivors, with r_x = 3, 25, 25, 96 and 102 for
x = 2 .. 6 (computed here). So every satisfying row of the instance already has column x equal to the forced word on
rows t0 + r_x .. s - 1 - r_x, and adding those values as unit clauses removes no solution.

PREDICTIONS (Local's, published before the run):
  KT2b-C0 (control, the words): the forced words and round counts recomputed here are LK's (columns 2 .. 6; r_x =
          3, 25, 25, 96, 102).
  KT2b-C1 (control, soundness on a real configuration): instance (N = 252, class 32, t0 0, d 0) solved WITHOUT the
          units is SAT, replays, and its model obeys every unit KT2b would add (columns 2 .. 6 on the rows above).
          If it is SAT and disobeys one, LK is wrong.
  KT2b-C2 (control): every SAT model with the units replays by direct simulation.
  KT2b-P1 (blind, confidence 0.5): with the units, (N = 560, class 32, t0 0, d 0) is solved within 600 s.
  KT2b-P2 (blind): wherever KT2 and KT2b both finish an instance, they agree.
OUTCOME: not yet run.
"""
import os
import subprocess
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_kick_bite_kissat as kk
sys.argv = _argv
import rule30_locked_core_review as rv
import rule30_locked_core_lock as lk

SCRATCH = '/Volumes/extnvme/nframe-project/np-scratch/rule30-kt2b'
CAP = 1800
P = kk.P
U = kk.U


def forced_words():
    src, dst, n = rv.graph(15, rv.wheel())
    alive = np.ones(n, dtype=bool)
    need, r = {}, 0
    while len(need) < 5:
        w = lk.words(alive, 15, (2, 3, 4, 5, 6))
        for x in (2, 3, 4, 5, 6):
            if x not in need and '*' not in w[x]:
                need[x] = (r, w[x])
        alive = rv.trim_once(src, dst, alive)
        r += 1
    return need


def instance_vars(t0, d, a, N):
    """KK's instance, with its variable map exposed (the clause list is KK's, built by the same code)"""
    s = t0 + N
    while (s - d) % P != a:
        s += 1
    E = s + 20
    var, nv = {}, [0]

    def v(t, i):
        if (t, i) not in var:
            nv[0] += 1
            var[(t, i)] = nv[0]
        return var[(t, i)]

    clauses = []
    for t in range(t0 + 1, E + 1):
        for i in range(1, 1 + (E - t) + 1):
            y, b, c = v(t, i), v(t - 1, i), v(t - 1, i + 1)
            nv[0] += 1
            o = nv[0]
            clauses += [[-b, o], [-c, o], [b, c, -o]]
            if i == 1:
                if (t - 1) % 2 == 0:
                    clauses += [[-y, o], [y, -o]]
                else:
                    clauses += [[y, o], [-y, -o]]
            else:
                l = v(t - 1, i - 1)
                clauses += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]
    for t in range(t0, s):
        clauses.append([v(t, 1) if U[(t - d) % P] else -v(t, 1)])
    sels = []
    for dn in range(0, P, 2):
        if U[(s - dn) % P] == U[(s - d) % P]:
            continue
        nv[0] += 1
        sel = nv[0]
        sels.append(sel)
        for t in range(s, E + 1):
            clauses.append([-sel, v(t, 1) if U[(t - dn) % P] else -v(t, 1)])
    clauses.append(sels)
    row = [v(t0, i) for i in range(1, 1 + (E - t0) + 1)]
    return nv[0], clauses, row, s, E, var


def units(t0, d, s, var, need):
    out = []
    for x, (r, word) in need.items():
        for t in range(t0 + r, s - r):
            bit = int(word[(t - d) % P])
            out.append([var[(t, x)] if bit else -var[(t, x)]])
    return out


def solve(t0, d, a, N, need, with_units):
    nv, clauses, row, s, E, var = instance_vars(t0, d, a, N)
    extra = units(t0, d, s, var, need)
    if with_units:
        clauses = clauses + extra
    os.makedirs(SCRATCH, exist_ok=True)
    path = os.path.join(SCRATCH, 'u_%d_%d_%d_%d_%d.cnf' % (N, a, t0, d, with_units))
    with open(path, 'w') as f:
        f.write('p cnf %d %d\n' % (nv, len(clauses)))
        for c in clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')
    t = time.time()
    r = subprocess.run(['kissat', '-q', '--time=%d' % CAP, path], capture_output=True, text=True)
    secs = time.time() - t
    os.unlink(path)
    if r.returncode == 20:
        return 'UNSAT', secs, None, len(extra)
    if r.returncode != 10:
        return 'UNKNOWN', secs, None, len(extra)
    val = set()
    for line in r.stdout.splitlines():
        if line.startswith('v '):
            val.update(int(x) for x in line[2:].split())
    ok = kk.replay(t0, d, s, E, [1 if x in val else 0 for x in row])
    obeys = all((u[0] in val) for u in extra)
    return 'SAT', secs, (ok, obeys), len(extra)


def main():
    need = forced_words()
    for x in sorted(need):
        print('column %d: single-valued among the %d-round survivors' % (x, need[x][0]), flush=True)
    c0 = [need[x][0] for x in (2, 3, 4, 5, 6)] == [3, 25, 25, 96, 102] and \
        need[5][1] == '10000001011000000101100000010110000001011010101110000101'
    v1, s1, m1, n1 = solve(0, 0, 32, 252, need, False)
    print('N 252 class 32 (0, 0), no units: %s in %.0f s, replay and obeys %d implied units: %s' % (v1, s1, n1, m1),
          flush=True)
    c1 = v1 == 'SAT' and m1 == (True, True)
    v2, s2, m2, n2 = solve(0, 0, 32, 560, need, True)
    print('N 560 class 32 (0, 0), %d units: %s in %.0f s, replay %s' % (n2, v2, s2, m2), flush=True)
    c2 = v2 != 'SAT' or m2[0]
    print('KT2b-C0', 'PASS' if c0 else 'FAIL')
    print('KT2b-C1', 'PASS' if c1 else ('FAIL' if v1 == 'SAT' else 'VOID (%s)' % v1))
    print('KT2b-C2', 'PASS' if c2 else 'FAIL')
    print('KT2b-P1', 'HELD' if v2 in ('SAT', 'UNSAT') and s2 <= 600 else 'REFUTED')
    print('KT2b-P2: compare with KT2 checkpoint line "560 32 0 0" when it lands')


if __name__ == '__main__':
    main()
