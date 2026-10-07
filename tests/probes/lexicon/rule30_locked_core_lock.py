#!/usr/bin/env python3
"""rule30_locked_core_lock.py: LK, Local's check of RV2's unexpected outcome: the complete width-15 graph's core forces
columns 2 .. 6 next to the wheel, so column 5 is no longer ambiguous (RV2-P1 refuted; rule30_locked_core_review.py).
Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one core; numpy
COMMAND:    python3 tests/probes/lexicon/rule30_locked_core_lock.py   (from the repository root; GPT's branch fetched)
COST:       to be recorded.

The setting is GC373's: column 0 is t mod 2, column 1 runs the wheel U, a vertex is (phase, columns 2 .. m), an edge
needs some free column m + 1, and the core is the simultaneous in/out trimming. A forward-infinite wheel strip ends
inside one strongly connected component, hence inside the core, so a column forced in the core is eventually
forced in every configuration whose column 1 follows the wheel for ever. A wider core projects into a narrower one,
so a column forced at width m stays forced at every larger width where the core is not empty.

PREDICTIONS (Local's, published before the run):
  LK-C0 (control, a second route): GPT's lift (rule30_locked_lift.py, from GPT's branch), chained 12 -> 13 -> 14 ->
        15 from GPT's own width-12 core, gives exactly the direct cores' vertex and edge sets at widths 14 and 15.
  LK-C1 (control, projection): wherever the core is non-empty at widths 16, 17 and 18, columns 2 .. 6 are forced,
        with the width-15 words.
  LK-P1 (blind, confidence 0.85): the core is non-empty at widths 16, 17 and 18.
  LK-P2 (blind, confidence 0.5): at width 18 at least one column beyond 6 is forced.
  LK-P3 (blind, confidence 0.5): at width 15, column 5 is already single-valued at every phase among the r-round
        survivors of the complete graph for some r <= 60, so a wheel strip of 2r + 1 <= 121 observations forces
        column 5 at its centre.
OUTCOME: not yet run.
"""
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule30_locked_core_review as rv

P = rv.P


def words(alive, m, cols):
    S = 1 << (m - 1)
    ids = np.nonzero(alive)[0]
    ph, st = ids // S, ids % S
    out = {}
    for x in cols:
        vals = [sorted(set(((st[ph == p] >> (x - 2)) & 1).tolist())) for p in range(P)]
        out[x] = ''.join(str(v[0]) if len(v) == 1 else '*' for v in vals)
    return out


def lift_chain(U, top):
    """GPT's width-12 core lifted by GPT's lift to width top; returns {m: (vertex ids, edge id pairs)}"""
    rv.gpt_lift(13, U)                                   # writes GPT's three modules to scratch and imports them
    import rule30_locked_core as gc
    import rule30_locked_lift as gl
    _, a, o = gc.core(12, U, details=True)
    res = {}
    for m in range(12, top):
        a, o, _ = gl.lift(m, U, a, o)
        S = 1 << m
        res[m + 1] = ({p * S + s for p, s in a}, {(p * S + s, q * S + t) for (p, s), vs in o.items() for q, t in vs})
    return res


def main():
    U = rv.wheel()
    direct = {}
    for m in range(14, 19):
        t = time.time()
        src, dst, n = rv.graph(m, U)
        alive, rounds = rv.trim(src, dst, n)
        f = rv.forced(alive, m)
        direct[m] = (src, dst, alive, f)
        print('width %d: core %d vertices after %d rounds, forced columns %s (%.1f s)'
              % (m, int(alive.sum()), rounds, f, time.time() - t), flush=True)
    w15 = words(direct[15][2], 15, (5, 6))
    print('width 15 words from phase 0: column 5 %s, column 6 %s' % (w15[5], w15[6]))
    chain = lift_chain(U, 15)
    c0 = True
    for m in (14, 15):
        src, dst, alive, _ = direct[m]
        live = alive[src] & alive[dst]
        v = set(np.nonzero(alive)[0].tolist())
        e = set(zip(src[live].tolist(), dst[live].tolist()))
        same = v == chain[m][0] and e == chain[m][1]
        c0 &= same
        print('width %d: direct core vs GPT lift chain: %s (%d and %d vertices, %d and %d edges)'
              % (m, same, len(v), len(chain[m][0]), len(e), len(chain[m][1])))
    c1, p1 = True, True
    for m in (16, 17, 18):
        alive = direct[m][2]
        if alive.any():
            c1 &= all(x in direct[m][3] for x in range(2, 7)) and words(alive, m, (5, 6)) == w15
        else:
            p1 = False
    p2 = direct[18][2].any() and any(x > 6 for x in direct[18][3])
    src, dst, _, _ = direct[15]
    alive = np.ones(P << 14, dtype=bool)
    r = 0
    while '*' in words(alive, 15, (5,))[5]:
        alive = rv.trim_once(src, dst, alive)
        r += 1
    print('width 15: column 5 is single-valued at every phase among the %d-round survivors (strip of %d)' % (r, 2 * r + 1))
    print('LK-C0', 'PASS' if c0 else 'FAIL')
    print('LK-C1', 'PASS' if c1 else 'FAIL')
    print('LK-P1', 'HELD' if p1 else 'REFUTED')
    print('LK-P2', 'HELD' if p2 else 'REFUTED')
    print('LK-P3', 'HELD' if r <= 60 else 'REFUTED')


if __name__ == '__main__':
    main()
