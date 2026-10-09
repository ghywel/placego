#!/usr/bin/env python3
"""rule30_isolated_zero_pairs.py: SGP, does a failing black-end strip component force some OTHER adjacent pair of
columns? Jen's theorem with a clock (PROOFS.md entry 5) forbids any two adjacent eventually periodic columns from a
finite nonzero seed, not only pairs that contain column 0. SG and SGW (rule30_isolated_zero_strip.py and _wide.py)
tested only columns -1 and +1 beside the wall. Local's own-lane step (chat L437), predictions pushed before the run.

RUN-ON:     cpu (Python 3, standard library); a few minutes
COMMAND:    python3 tests/probes/lexicon/rule30_isolated_zero_pairs.py

For each open wall q in {2, 3, 4, 5, 6, 8} and radius R = 6, 7, 8, take every cyclic component (SGW's graph and
period), and list the columns c in -(R - 1) .. R - 1 that take one value on each time class. If some component forces
no adjacent pair (c, c + 1) at all (column 0 counts as forced), that component escapes this test, and the wall stays
open by this method. A wall all of whose components force an adjacent pair is excluded for finite seeds, by the same
argument as entry 38. (The outer cells -R and R are free inputs, so they are never counted.)

PREDICTIONS (Local's, published before the run):
  SGP-C1 (control): q = 7 at R = 6 has its component force the pair (-1, 0), as SG found.
  SGP-P1 (blind, confidence 0.7): no open wall is excluded this way at R <= 8 (each keeps a component forcing no
         adjacent pair).
  SGP-D1 (descriptive): for each failing component, its forced columns.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule30_isolated_zero_wide as sgw                               # noqa: E402
from math import gcd                                                  # noqa: E402


def components(R, q):
    verts, succ, C = sgw.build(R, q)
    out = []
    for comp in sgw.sccs(len(verts), succ):
        cs = set(comp)
        level, queue = {comp[0]: 0}, [comp[0]]
        for v in queue:
            for w in succ[v]:
                if w in cs and w not in level:
                    level[w] = level[v] + 1
                    queue.append(w)
        P = 0
        for v in comp:
            for w in succ[v]:
                if w in cs:
                    P = gcd(P, level[v] + 1 - level[w])
        P = abs(P)
        forced = []
        for c in range(-(R - 1), R):
            b = C + c
            vals, ok = {}, True
            for v in comp:
                x = (verts[v][0] >> b) & 1
                if vals.setdefault(level[v] % P, x) != x:
                    ok = False
                    break
            if ok:
                forced.append(c)
        pair = any(c in forced and c + 1 in forced for c in range(-(R - 1), R - 1))
        out.append((len(comp), P, forced, pair))
    return out


def main():
    c1 = any(p and -1 in f and 0 in f for _, _, f, p in components(6, 7))
    print('SGP-C1', 'PASS' if c1 else 'FAIL')
    excluded = []
    for q in (2, 3, 4, 5, 6, 8):
        for R in (6, 7, 8):
            comps = components(R, q)
            ok = bool(comps) and all(p for _, _, _, p in comps)
            if ok:
                excluded.append((q, R))
            desc = '; '.join('%d P%d forced %s%s' % (n, P, f, ' PAIR' if p else '') for n, P, f, p in
                             sorted(comps, key=lambda c: -c[0]))
            print('q = %d, R = %d: %s; %s' % (q, R, 'EXCLUDED' if ok else 'open', desc), flush=True)
    print('SGP-P1', 'HELD' if not excluded else 'REFUTED: excluded %s' % excluded)
    print('COMPLETE')


if __name__ == '__main__':
    main()
