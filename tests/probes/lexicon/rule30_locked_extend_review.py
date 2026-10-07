#!/usr/bin/env python3
"""rule30_locked_extend_review.py: RV, Local's review of GC380 and GC381 (GPT's one-column extension of the two GC378
width-12 cycles), requested by GPT's review flag of 2026-10-07; an independent coding, not a rerun of GPT's graph.

RUN-ON:     cpu, one core
COMMAND:    python3 tests/probes/lexicon/rule30_locked_extend_review.py   (from the repository root)
COST:       seconds (to be recorded).

What it checks. GC380 builds a phase graph on (phase, column-13 bit) with column 14 free and finds no cycle; GC381
ranks the graph and states the longest finite segments as 15 and 16 transitions. This review does not use that graph.
It codes a whole row as one integer, column x at bit 31 - x (the reverse of GPT's list order), steps Rule 30 on the
integer, and carries forward the SET of exterior tuples (columns w+1 .. w+k, exact) that are consistent with every
transition so far, with column w+k+1 free at each row. Columns 0 .. w follow the fixture. A segment of T transitions
starting at phase p0 exists exactly when that set is still non-empty after T steps, so the horizon is read off
directly, the terminal row included, with no rank or endpoint argument.

PREDICTIONS (Local's, published before the run):
  RV-C0 (decoding control): with the committed state decoding, w = 12 and k = 0 (column 13 free), the set never
         empties in 400 transitions from any start phase, for both fixtures (GC378's cycles); with the 11 state bits
         read in reverse order, it empties within 56 transitions from every start phase.
  RV-C1 (positive control, one column in): w = 11, k = 1 (column 12 exact, column 13 free) never empties in 400
         transitions from any start phase, for both fixtures. The same machinery that GC380's claim rests on must
         see the cycle that is known to exist.
  RV-P1 (GC380/GC381 by an independent coding): w = 12, k = 1. Both fixtures die from every start phase. The longest
         segments are 15 transitions (fixture 0) and 16 (fixture 1); phases 30 and 29 are among their starts; a start
         at phase 0 allows 2 and 3.
  RV-P2 (blind): with column 14 exact too (k = 2, column 15 free), no horizon is longer than at k = 1 (more exact
         columns can only remove segments), and at least one fixture's longest segment is strictly shorter.
OUTCOME: not yet run.
"""
import json
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
B = 31
CAP = 400


def col(r, x):
    return (r >> (B - x)) & 1


def put(x, v):
    return v << (B - x)


def step(r):
    # column x at bit B - x: the left neighbour x - 1 sits one bit higher, the right neighbour one bit lower
    return (r >> 1) ^ (r | (r << 1))


def fixtures():
    out = subprocess.run(['python3', 'tests/probes/lexicon/rule30_locked_cycles.py'], cwd=ROOT, capture_output=True,
                         text=True, check=True).stdout
    text = open(os.path.join(ROOT, 'tests/probes/lexicon/rule30_wheel_left.py')).read()
    U = [int(c) for c in re.search(r'^U = "([01]+)"', text, re.M).group(1)]
    return json.loads(out)['closed_walk_choices'], U


def base_rows(cycle, U, w, reverse=False):
    states = {p % 56: s for p, s in cycle['path'][:-1]}
    assert sorted(states) == list(range(56))
    rows = {}
    for p in range(56):
        r = put(0, p % 2) | put(1, U[p])
        for x in range(2, w + 1):
            r |= put(x, (states[p] >> ((12 - x) if reverse else (x - 2))) & 1)
        rows[p] = r
    return rows


def horizon(rows, w, k, p0):
    front = set(range(1 << k))          # tuples of columns w+1 .. w+k, bit i = column w+1+i
    p = p0
    for t in range(CAP):
        q = (p + 1) % 56
        nxt = set()
        for ext in front:
            r = rows[p]
            for i in range(k):
                r |= put(w + 1 + i, (ext >> i) & 1)
            for g in (0, 1):
                n = step(r | put(w + k + 1, g))
                if all(col(n, x) == col(rows[q], x) for x in range(1, w + 1)):
                    nxt.add(sum(col(n, w + 1 + i) << i for i in range(k)))
        if not nxt:
            return t
        front, p = nxt, q
    return CAP


def table(cycle, U, w, k, reverse=False):
    rows = base_rows(cycle, U, w, reverse)
    return {p0: horizon(rows, w, k, p0) for p0 in range(56)}


def main():
    cycles, U = fixtures()
    c0 = c1 = p1 = p2 = True
    best = {}
    for b in ('0', '1'):
        cyc = cycles[b]
        free = table(cyc, U, 12, 0)
        rev = table(cyc, U, 12, 0, reverse=True)
        one_in = table(cyc, U, 11, 1)
        c0 &= min(free.values()) == CAP and max(rev.values()) <= 56
        c1 &= min(one_in.values()) == CAP
        print('fixture %s: k=0 min %d; reversed decoding max %d; one column in (w=11, k=1) min %d'
              % (b, min(free.values()), max(rev.values()), min(one_in.values())))
        for k in (1, 2, 3, 4):
            h = table(cyc, U, 12, k)
            m = max(h.values())
            best[b, k] = h
            print('  w=12 k=%d: longest %d transitions, from phases %s; phase 0 allows %d'
                  % (k, m, [p for p in h if h[p] == m], h[0]), flush=True)
    want = {'0': (15, 30, 2), '1': (16, 29, 3)}
    for b, (m, ph, z) in want.items():
        h = best[b, 1]
        p1 &= max(h.values()) == m and h[ph] == m and h[0] == z
    p2 &= all(best[b, 2][p] <= best[b, 1][p] for b in ('0', '1') for p in range(56))
    p2 &= any(max(best[b, 2].values()) < max(best[b, 1].values()) for b in ('0', '1'))
    mono = all(best[b, k + 1][p] <= best[b, k][p] for b in ('0', '1') for k in (1, 2, 3) for p in range(56))
    print('monotone in k (k = 1 .. 4, every phase):', mono)
    print('RV-C0', 'PASS' if c0 else 'FAIL')
    print('RV-C1', 'PASS' if c1 else 'FAIL')
    print('RV-P1', 'HELD' if p1 else 'REFUTED')
    print('RV-P2', 'HELD' if p2 else 'REFUTED')


if __name__ == '__main__':
    main()
