#!/usr/bin/env python3
"""rule210_census_lag.py: CL, how the empty-left full 0101 Rule 210 census decides each initial site. Local's lane
(GPT's GC461: "leave its actual-prefix census to Local"); follows TS (rule210_two_step_review.py) and L270-L272.
Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule210_census_lag.py
COST:       to be recorded (expected well under a minute).

Why. TS found the survivor count by depth periodic (1, 2, 3, 6, 1, 2 by depth mod 6, from depth 1) and the unique
survivors equal to G60's seed R (sites coprime to 6) through depth 240. A uniqueness proof (no mixed-parity member)
would follow if every block of undecided sites is always settled within a bounded lag by a uniform mechanism. This
probe measures the lag and the killing structure, deeper, before any attempt at that proof.

A site e is decided at depth d when every survivor at depth d has the same value at e (and so does every later
survivor, since survivors at later depths extend survivors at earlier ones).

PREDICTIONS (Local's, published before the run):
  CL-P1 (blind, confidence 0.9): to depth 1200 the count pattern by depth mod 6 (1:1, 2:2, 3:3, 4:6, 5:1, 0:2) holds
         and every unique survivor is R restricted to sites 1 .. d.
  CL-P2 (blind, confidence 0.6): site e is decided exactly at the first depth d >= e with d = 1 or 5 (mod 6): sites
         6k+2 .. 6k+5 at 6k+5 and sites 6k+6, 6k+7 at 6k+7 (k >= 0); no site is decided earlier.
  CL-P3 (blind, confidence 0.6): at every depth d = 4 (mod 6) the six survivors' trailing triples (sites d-2, d-1, d)
         are the same six triples for every k, and so are the three pairs (d-1, d) at d = 3 (mod 6) and the two
         singles at d = 0, 2 (mod 6): the census is a periodic machine, not just periodic counts.
  CL-C0 (control): the census to depth 240 reproduces TS's counts exactly.
OUTCOME: not yet run.
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule210_two_step_review as ts

D = 1200


def main():
    t0 = time.time()
    ts.B, ts.OFF = 2 * D + 40, D + 20
    ts.MASK = (1 << (ts.B + 1)) - 1
    R = set(i for i in range(1, D + 1) if i % 6 in (1, 5))
    alive, counts, decided, tails = [[]], {}, {}, {}
    uniq_ok = True
    for d in range(1, D + 1):
        nxt = []
        for pre in alive:
            for v in (0, 1):
                sites = [i + 1 for i, b in enumerate(pre + [v]) if b]
                rs = ts.rows_of(sites, d)
                if all(ts.bit(rs[t], 0) == t % 2 for t in range(d + 1)):
                    nxt.append(pre + [v])
        alive = nxt
        counts[d] = len(alive)
        if d % 6 in (1, 5):
            uniq_ok &= len(alive) == 1 and [i + 1 for i, b in enumerate(alive[0]) if b] == sorted(i for i in R if i <= d)
        for e in range(1, d + 1):
            if e not in decided and len(set(p[e - 1] for p in alive)) == 1:
                decided[e] = d
        w = {4: 3, 3: 2, 0: 1, 2: 1}.get(d % 6)
        if w and d > 6:
            tails.setdefault(d % 6, set()).add(frozenset(tuple(p[d - w:]) for p in alive))
    want = {1: 1, 2: 2, 3: 3, 4: 6, 5: 1, 0: 2}
    pattern = all(counts[d] == want[d % 6] for d in counts)
    first = lambda e: next(d for d in range(e, e + 7) if d % 6 in (1, 5))
    p2 = all(decided.get(e) == first(e) for e in range(1, D - 6))
    lagbad = [(e, decided.get(e), first(e)) for e in range(1, D - 6) if decided.get(e) != first(e)][:8]
    p3 = all(len(v) == 1 for v in tails.values())
    c0 = [counts[d] for d in range(1, 241)] == [1, 2, 3, 6, 1, 2] * 40
    print('count pattern held:', pattern, '; every unique survivor is R:', uniq_ok)
    print('CL-P1', 'HELD' if pattern and uniq_ok else 'REFUTED')
    print('CL-P2', 'HELD' if p2 else 'REFUTED', lagbad)
    print('CL-P3', 'HELD' if p3 else 'REFUTED')
    for m in sorted(tails):
        print('  depth = %d mod 6: %d distinct tail sets; first: %s' % (m, len(tails[m]),
              sorted(sorted(s) for s in tails[m])[0]))
    print('CL-C0', 'PASS' if c0 else 'FAIL')
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    main()
