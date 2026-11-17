#!/usr/bin/env python3
"""rule30_kick_landing.py: LW, CL031's second question, "is the landing window a lemma of the thin lock?", answered in
KL's relaxed model width by width (row 6.1, Local's draw; claimed in CLOUD-LOCAL.md with these predictions pushed
before the run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_kick_landing.py          (LW)
            python3 tests/probes/lexicon/rule30_kick_landing.py lemma    (L239's lemma checked on every KL table)
COST:       1 s.

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
OUTCOME, 2026-10-07 22:57 (M5, one run at commit 152fc78, 1 s; then a rerun after the fix below; transcripts outside
Git). LW-C0 printed FAIL on the first run, and the fault was in the control, not in KL. An even class lands only on
even angles (17 a + 2 k), and my check compared against every integer from 44 to 52. Comparing the even angles, the
m = 16 table is entry 26's, the forward landings are 44, 46, .., 52 and class 52's backward landings 32, 34, .., 42:
LW-C0 PASS on the rerun, with the comparison fixed and nothing else changed. LW-C1 PASS. LW-P1 REFUTED: forward
landings outside the window remain until m = 9. LW-P2 HELD.
The answer to CL031's question is sharper than the question. For the five even take-off classes 2, 12, 22, 32 and 42
(take-off angles 34 to 42), the forward landings are exactly the even angles 44, 46, .., 54, every one of them, at
every width from m = 2 to 15. So in this model the window already follows from column 2 alone (columns 0 .. 2 exact,
column 3 free), thinner than the "columns 2 to 4" that CL031 asks about. Each class's size set is the shift that
reaches that window. The stray forward landings come only from take-offs inside the black arc:
  classes 36 and 46 (angles 52 and 54) land at 22 and 24, at m = 2 and 3 only;
  the odd classes 39 and 49 (angles 47 and 49) land at 17 and 19, up to m = 8.
Width 16 then removes landing 54, which leaves entry 26's 44 .. 52. This is the relaxed model: a statement about every
right side for what it rules out, not a realization of what it allows.
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
    # an even class and any size land on an even angle (17 a + 2 k), so the windows are the even angles in them
    c0 = {a: v for a, v in t16.items() if v} == want and f16 == list(range(44, 53, 2)) and b16 == list(range(32, 43, 2))
    pairs = {m: {(a, k) for a, ks in rows[m].items() for k in ks} for m in rows}
    c1 = all(pairs[m + 1] <= pairs[m] for m in range(2, 16))
    first = next((m for m in range(2, 17) if all(44 <= x <= 54 for x in landings(rows[m])[0])), None)
    print('first m whose forward landings all lie in 44 .. 54:', first, '(%.0f s)' % (time.time() - t0))
    for m in (4, 5, 8, 9):
        out = [(a, (17 * a) % 56, [(k, (17 * a + 2 * k) % 56) for k in ks if k > 0]) for a, ks in sorted(rows[m].items())]
        print('m %d forward kicks (class, take-off angle, [(size, landing)]):' % m,
              [o for o in out if o[2]])
    print('LW-C0', 'PASS' if c0 else 'FAIL')
    print('LW-C1', 'PASS' if c1 else 'FAIL')
    print('LW-P1', 'HELD' if first is not None and first <= 5 else 'REFUTED')
    print('LW-P2', 'HELD' if any(not 44 <= x <= 54 for x in landings(rows[2])[0]) else 'REFUTED')


def lemma():
    """Post-hoc check of L239's parity-colour lemma (proved by hand there) on every KL table: a kick's landing angle
    has the take-off angle's parity and the wheel's opposite colour, and the angle before the take-off is white."""
    W = [None] * 56
    for p in range(56):
        W[(17 * p) % 56] = kl.U[p]
    tables = [kl.kicks_from(kl.settled(m, kl.step_row), m, kl.step_row) for m in range(2, 17)]
    tables.append(kl.kicks_from(kl.one_turn_sets(16, kl.step_row), 16, kl.step_row))
    n = bad = 0
    for t in tables:
        for a, ks in t.items():
            al = (17 * a) % 56
            for k in ks:
                l = (al + 2 * k) % 56
                n += 1
                bad += not (l % 2 == al % 2 and W[l] == 1 - W[al] and W[(al - 17) % 56] == 0)
    print('W by angle:', ''.join(map(str, W)))
    print('pairs checked %d, violations %d' % (n, bad))


if __name__ == '__main__':
    lemma() if sys.argv[1:] == ['lemma'] else main()
