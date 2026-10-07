#!/usr/bin/env python3
"""rule30_class12_gate_check.py: GW, a second witness for GC390's class-12 gate (GPT asked for its forced timestamps
to be checked against a witness; Cloud holds CL031's saved one, and this is an independent one). Claimed in
CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one kissat process (seconds)
COMMAND:    python3 tests/probes/lexicon/rule30_class12_gate_check.py
COST:       to be recorded.

The witness: KK's instance (rule30_kick_bite_kissat.py) for class 12 after N = 126 steps, at the one case alive there
(t0 = 0, phase d = 2; L231, CL031), solved by kissat and replayed. Its columns 1 .. 6 over the last turn before the
kick are compared with the reference words of the locked strip (LK, rule30_locked_core_lock.py: columns 2 .. 6 at
width 15; columns 2 .. 4 are G205's words), read at phase (t - d) mod 56. GC390's gate: where the left and centre
inputs of an update agree between the witness and the reference, the output difference is (1 - b)(r XOR r'), with
b the common centre bit and r, r' the right inputs.

PREDICTIONS (Local's, published before the run):
  GW-C0 (control): the model replays (KK's direct simulation: the wheel for 126 steps, a class-12 departure, 21
        observations of a new phase), and columns 1 .. 4 agree with the reference words on the first turn of the
        witness's last 112 wheel rows, away from the kick.
  GW-C1 (control, an identity): at every update in the last turn where the left and centre inputs agree, the
        output difference equals (1 - b)(r XOR r').
  GW-P1: column 2 first disagrees with its reference in the last turn at s - 1 (as CL031's witness does).
  GW-P2 (GC390's forced consequence): column 3 disagrees at s - 2.
  GW-P3 (GC390, conditional): if column 3 disagrees at s - 4, column 4 disagrees at s - 5; if column 3 disagrees at
        s - 2 while column 2 agrees at s - 3 and column 3's reference at s - 3 is 0, column 4 disagrees at s - 3.
OUTCOME: not yet run.
"""
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_kick_bite_kissat as kk
sys.argv = _argv
import rule30_locked_core_review as rv
import rule30_locked_core_lock as lk

P = kk.P
SCRATCH = '/Volumes/extnvme/nframe-project/np-scratch/rule30-gw'


def witness(t0, d, a, N):
    nv, clauses, row, s, E = kk.instance(t0, d, a, N)
    os.makedirs(SCRATCH, exist_ok=True)
    path = os.path.join(SCRATCH, 'w.cnf')
    with open(path, 'w') as f:
        f.write('p cnf %d %d\n' % (nv, len(clauses)))
        for c in clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')
    r = subprocess.run(['kissat', '-q', path], capture_output=True, text=True)
    os.unlink(path)
    assert r.returncode == 10, 'not SAT: %d' % r.returncode
    val = set()
    for line in r.stdout.splitlines():
        if line.startswith('v '):
            val.update(int(x) for x in line[2:].split())
    bits = [1 if x in val else 0 for x in row]
    return bits, s, E


def columns(t0, bits, E, width=8):
    """columns 0 .. width at every time t0 .. E, by direct simulation (column 0 = t mod 2)"""
    cur = [t0 % 2] + list(bits) + [0]
    cols = {t0: cur[:width + 1]}
    for t in range(t0 + 1, E + 1):
        cur = [t % 2] + [cur[i - 1] ^ (cur[i] | cur[i + 1]) for i in range(1, len(cur) - 1)] + [0]
        cols[t] = cur[:width + 1]
    return cols


def main():
    t0, d, a, N = 0, 2, 12, 126
    bits, s, E = witness(t0, d, a, N)
    ok = kk.replay(t0, d, s, E, bits)
    cols = columns(t0, bits, E)
    src, dst, n = rv.graph(15, rv.wheel())
    alive, _ = rv.trim(src, dst, n)
    words = lk.words(alive, 15, (2, 3, 4, 5, 6))
    ref = lambda x, t: (t % 2) if x == 0 else (kk.U[(t - d) % P] if x == 1 else int(words[x][(t - d) % P]))
    diff = {(x, t): cols[t][x] ^ ref(x, t) for x in range(1, 7) for t in range(s - 56, s)}
    early = all(cols[t][x] == ref(x, t) for x in range(1, 5) for t in range(s - 112, s - 56) if t >= t0)
    print('witness: s = %d (class %d after %d steps, t0 %d, phase %d); replay %s' % (s, a, N, t0, d, ok))
    for x in range(1, 7):
        print('column %d: differences in the last turn at s - %s' % (x, sorted(s - t for t in range(s - 56, s)
                                                                              if diff[x, t])))
    gate_ok = True
    for x in range(1, 6):
        for t in range(s - 56, s - 1):
            if cols[t][x - 1] == ref(x - 1, t) and cols[t][x] == ref(x, t):
                b = cols[t][x]
                want = (1 - b) * (cols[t][x + 1] ^ ref(x + 1, t))
                gate_ok &= (cols[t + 1][x] ^ ref(x, t + 1)) == want
    first2 = next((s - t for t in range(s - 56, s) if diff[2, t]), None)
    p1 = first2 == 1
    p2 = bool(diff[3, s - 2])
    p3 = True
    if diff[3, s - 4]:
        p3 &= bool(diff[4, s - 5])
    if diff[3, s - 2] and not diff[2, s - 3] and ref(3, s - 3) == 0:
        p3 &= bool(diff[4, s - 3])
    print('GW-C0', 'PASS' if ok and early else 'FAIL')
    print('GW-C1', 'PASS' if gate_ok else 'FAIL')
    print('GW-P1', 'HELD' if p1 else 'REFUTED (column 2 first differs at s - %s)' % first2)
    print('GW-P2', 'HELD' if p2 else 'REFUTED')
    print('GW-P3', 'HELD' if p3 else 'REFUTED')


if __name__ == '__main__':
    main()
