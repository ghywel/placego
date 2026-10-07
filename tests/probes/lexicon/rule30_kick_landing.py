#!/usr/bin/env python3
"""rule30_kick_landing.py: LW, CL031's second question, "is the landing window a lemma of the thin lock?", answered in
KL's relaxed model width by width (row 6.1, Local's draw; claimed in CLOUD-LOCAL.md with these predictions pushed
before the run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_kick_landing.py
COST:       to be recorded (KL's settled tables to m = 16 took about 20 s).

KL (rule30_kick_layers.py, entry 26) runs the m-layer automaton: columns 2 .. m exact, column m + 1 free at every
step, so every real right side is one input sequence and anything it rules out is ruled out for every right side. Its
settled table lists, after column 1 has followed the wheel long enough, the departure classes a and the kick sizes k
that survive 21 observations of a new phase. Cloud's KA (CL031) reads a kick as a landing: the take-off angle is
17 a mod 56 and the landing angle is 17 a + 2 k mod 56. Forward kicks from entry 26's classes land in 44 .. 52.
CL031 asks whether that window already follows from the thin lock: columns 2 to 4 or 5 pinned, the rest free. In KL's
model that is a small m. So this script lists the landing angles of the settled table at every m from 2 to 16.

PREDICTIONS (Local's, published before the run):
  LW-C0 (control): at m = 16 the settled table is entry 26's (classes 12, 32, 42, 52 with sizes +4 .. +8, +2 .. +6,
        +1 .. +5, -6 .. -1); its forward landings are exactly 44 .. 52 and class 52's backward landings 32 .. 42.
  LW-C1 (control, soundness): the set of (class, size) pairs never grows with m (a wider layer only removes input
        sequences).
  LW-P1 (blind, confidence 0.5): every forward landing already lies in 44 .. 54 at m = 5.
  LW-P2 (blind, confidence 0.6): at m = 2 some forward landing lies outside 44 .. 54.
OUTCOME: not yet run.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_kick_layers as kl
sys.argv = _argv


def landings(table):
    fwd, back = set(), set()
    for a, ks in table.items():
        for k in ks:
            ang = (17 * a + 2 * k) % 56
            (fwd if k > 0 else back).add(ang)
    return sorted(fwd), sorted(back)


def main():
    t0 = time.time()
    rows = {}
    for m in range(2, 17):
        rows[m] = kl.kicks_from(kl.settled(m, kl.step_row), m, kl.step_row)
        fwd, back = landings(rows[m])
        pairs = sum(len(v) for v in rows[m].values())
        print('m %2d: %2d classes, %3d (class, size) pairs; forward landings %s; backward landings %s'
              % (m, len(rows[m]), pairs, fwd, back), flush=True)
    t16 = rows[16]
    want = {12: [4, 5, 6, 7, 8], 32: [2, 3, 4, 5, 6], 42: [1, 2, 3, 4, 5], 52: [-6, -5, -4, -3, -2, -1]}
    f16, b16 = landings(t16)
    c0 = {a: v for a, v in t16.items() if v} == want and f16 == list(range(44, 53)) and b16 == list(range(32, 43))
    pairs = {m: {(a, k) for a, ks in rows[m].items() for k in ks} for m in rows}
    c1 = all(pairs[m + 1] <= pairs[m] for m in range(2, 16))
    first = next((m for m in range(2, 17) if all(44 <= x <= 54 for x in landings(rows[m])[0])), None)
    print('first m whose forward landings all lie in 44 .. 54:', first, '(%.0f s)' % (time.time() - t0))
    print('LW-C0', 'PASS' if c0 else 'FAIL')
    print('LW-C1', 'PASS' if c1 else 'FAIL')
    print('LW-P1', 'HELD' if first is not None and first <= 5 else 'REFUTED')
    print('LW-P2', 'HELD' if any(not 44 <= x <= 54 for x in landings(rows[2])[0]) else 'REFUTED')


if __name__ == '__main__':
    main()
