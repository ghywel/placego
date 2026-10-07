#!/usr/bin/env python3
"""rule30_kick_bite_kissat.py: KK, Local's second reading of Cloud's KS (rule30_kick_bite_sat.py), asked for in CL028:
an independent CNF encoding of the same question, solved with a different solver (kissat), every model replayed.
Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu; needs the kissat binary on the PATH (no Python packages)
COMMAND:    python3 tests/probes/lexicon/rule30_kick_bite_kissat.py [JOBS=8]
COST:       minutes to an hour (to be recorded); one kissat process per instance, JOBS at a time.

The question, as KS states it (written here from its header, not from its code): column 0 is t mod 2; column 1
follows the wheel U of rule30_walls.py at an even phase d, x_t(1) = U((t - d) mod 56), for t0 <= t < s, where s is the
least time >= t0 + N with (s - d) mod 56 = a (the class); at s it departs, and on s .. s + 20 it follows U at some even
phase d' with U((s - d') mod 56) != U((s - d) mod 56). The row at t0 is free, which covers every history, and t0 in
{0, 1} with the 28 even phases covers every case. Is there a row that makes this happen?

Encoding (Local's own): variables x_t(i) for t0 <= t <= E = s + 20 and 1 <= i <= 1 + (E - t), column 1's light cone;
for t > t0, x_t(i) = x_(t-1)(i-1) XOR (x_(t-1)(i) OR x_(t-1)(i+1)) with x_(t-1)(0) = (t - 1) mod 2 a constant, by
Tseitin clauses through an auxiliary OR variable; unit clauses fix column 1 on [t0, s); one selector per eligible d',
their disjunction, and selector -> unit literals on [s, E]. Written as DIMACS, solved by kissat; a SAT model's row at
t0 is replayed by direct simulation and must reproduce the event.

PREDICTIONS (Local's, published before the run; they are KS's reported outcome, to be reproduced):
  KK-C1 (control): class 32 and class 42 are satisfiable at N = 168 for some (t0, d).
  KK-C2 (control, negative): class 22 is unsatisfiable at all 56 (t0, d) at N = 168.
  KK-C3 (control, positive for class 12 itself): class 12 at N = 112 is satisfiable at exactly 15 of the 56 cases,
         as CL028's table says.
  KK-C4: every SAT model replays by direct simulation.
  KK-P1 (the second reading): class 12 is unsatisfiable at all 56 cases at N = 140 and at N = 168.
OUTCOME: not yet run.
"""
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_walls as wl
sys.argv = _argv

U = [int(c) for c in wl.U]
P = len(U)
JOBS = int(sys.argv[1]) if len(sys.argv) > 1 else 8


def instance(t0, d, a, N):
    s = t0 + N
    while (s - d) % P != a:
        s += 1
    E = s + 20
    var = {}
    nv = [0]

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
            o = nv[0]                                   # o = b OR c
            clauses += [[-b, o], [-c, o], [b, c, -o]]
            if i == 1:                                  # left input is column 0, a constant
                if (t - 1) % 2 == 0:
                    clauses += [[-y, o], [y, -o]]       # y = o
                else:
                    clauses += [[y, o], [-y, -o]]       # y = NOT o
            else:
                l = v(t - 1, i - 1)                     # y = l XOR o
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
            lit = v(t, 1) if U[(t - dn) % P] else -v(t, 1)
            clauses.append([-sel, lit])
    clauses.append(sels)
    row = [v(t0, i) for i in range(1, 1 + (E - t0) + 1)]
    return nv[0], clauses, row, s, E


def replay(t0, d, s, E, rowbits):
    """simulate the row at t0 (cells 1 ..) with column 0 = t mod 2; check the event."""
    width = len(rowbits)
    cur = [t0 % 2] + list(rowbits) + [0]
    col1 = {t0: cur[1]}
    for t in range(t0 + 1, E + 1):
        nxt = [t % 2] + [cur[i - 1] ^ (cur[i] | cur[i + 1]) for i in range(1, len(cur) - 1)] + [0]
        cur = nxt
        col1[t] = cur[1]
    if any(col1[t] != U[(t - d) % P] for t in range(t0, s)) or col1[s] == U[(s - d) % P]:
        return False
    return any(all(col1[t] == U[(t - dn) % P] for t in range(s, E + 1)) for dn in range(0, P, 2)
               if U[(s - dn) % P] != U[(s - d) % P])


def solve(args):
    t0, d, a, N = args
    nv, clauses, row, s, E = instance(t0, d, a, N)
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', delete=False) as f:
        f.write('p cnf %d %d\n' % (nv, len(clauses)))
        for c in clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')
        path = f.name
    r = subprocess.run(['kissat', '-q', path], capture_output=True, text=True)
    os.unlink(path)
    if r.returncode == 20:
        return (t0, d, a, N, 'UNSAT', None)
    if r.returncode != 10:
        return (t0, d, a, N, 'ERROR %d' % r.returncode, None)
    val = set()
    for line in r.stdout.splitlines():
        if line.startswith('v '):
            val.update(int(x) for x in line[2:].split())
    bits = [1 if x in val else 0 for x in row]
    return (t0, d, a, N, 'SAT', replay(t0, d, s, E, bits))


def run(a, N):
    cases = [(t0, d, a, N) for t0 in (0, 1) for d in range(0, P, 2)]
    with ThreadPoolExecutor(JOBS) as ex:
        res = list(ex.map(solve, cases))
    sat = sum(1 for r in res if r[4] == 'SAT')
    err = [r for r in res if r[4].startswith('ERROR')]
    replay_ok = all(r[5] for r in res if r[4] == 'SAT')
    print('class %d, N %d: SAT %d of %d, errors %d, replays %s' % (a, N, sat, len(res), len(err),
          'all PASS' if replay_ok else 'FAIL'), flush=True)
    return sat, err, replay_ok


def main():
    r32 = run(32, 168)
    r42 = run(42, 168)
    r22 = run(22, 168)
    r12_112 = run(12, 112)
    r12_140 = run(12, 140)
    r12_168 = run(12, 168)
    allr = [r32, r42, r22, r12_112, r12_140, r12_168]
    print('KK-C1', 'PASS' if r32[0] > 0 and r42[0] > 0 else 'FAIL')
    print('KK-C2', 'PASS' if r22[0] == 0 and not r22[1] else 'FAIL')
    print('KK-C3', 'PASS' if r12_112[0] == 15 else 'FAIL (%d)' % r12_112[0])
    print('KK-C4', 'PASS' if all(r[2] for r in allr) else 'FAIL')
    print('KK-P1', 'HELD' if r12_140[0] == 0 and r12_168[0] == 0 and not r12_140[1] and not r12_168[1]
          else 'REFUTED')


if __name__ == '__main__':
    main()
