#!/usr/bin/env python3
"""rule30_all_s_future.py: ASF, does a long enough all-S past force the 84-ring's sixth column (and beyond)? The S twin
of ALF (rule30_all_l_future.py, L387). Local's run (chat L393), claimed in CLOUD-LOCAL.md with predictions pushed first.

RUN-ON:     cpu (Python 3 and kissat, NL's encoder); a few minutes
COMMAND:    python3 tests/probes/lexicon/rule30_all_s_future.py

GPT's GC688 proves that every marker-aligned all-S trace carries the ring's five columns next to the wall at every loop
with a following S, whatever lies further out; GC689 gives only gates for site 6, and L369's samples saw several site-6
histories. Here, as in ALX/ALF, each query is NL's exact mode-A cone (the clamped wall white at even times; any right
exterior) with the visible word S^K and its closing 1, GC606's entrance 11101 on sites 1 .. 5 at time 0, and one clause
saying that some cell of the named sites at loop k (times 6k .. 6k + 5) differs from GC686's 84-cell ring. UNSAT at K is
UNSAT at every longer K (an extension of a witness is a witness for the prefix), and a later loop with a following S
restarts in 11101 at an even time (GC606/GC626), so a forced cell at loop k0 with future f is forced at every later
loop with future f.

PREDICTIONS (Local's, published before the run):
  ASF-C1 (control): sites 1 .. 5 at loop 0 of S^2 are UNSAT (GC688's slab).
  ASF-C2 (control): UNSAT is monotone in K wherever it appears.
  ASF-P1 (blind, confidence 0.5): some loop k0 <= 8 has site 6 forced with one following S (F6(k0) = 1).
  ASF-P2 (blind, confidence 0.4): site 7 is forced at some loop k <= 8 with future <= 8.
  ASF-D1 (descriptive): for k = 0 .. 8, the least future (following S's, K up to k + 14) forcing site 6, and sites 6 .. 7,
         or "SAT up to K = k + 14".
Counterfactual: site 6 deviating at every loop with every future tried would mean the all-S slab is five columns for
good, unlike all-L's six.
OUTCOME, 2026-10-09 10:56 BST (M5, 12 s, run at commit 470c3d9a; raw strings are K = k+2 .. k+15, S = SAT, U = UNSAT):
  ASF-C1 PASS. ASF-C2 PASS (UNSAT monotone in K everywhere).
  D1: sites 6, 7 and 6..7 all need future 5 at loops 0 .. 4 and future 4 at loops 5 .. 8 (SSSSU.., SSSU..).
  ASF-P1 REFUTED: no loop forces site 6 with only one following S. ASF-P2 HELD: site 7 is forced with future <= 5.
  So for S the gate is a short future and no past, where for L (ALF) it was five L's behind and one ahead.
  Exploratory, after the run (no predictions): widest run of forced sites, one site per query:
    loop 0, futures 5 .. 17: sites 1 .. 7 (site 8 free). Future 12: loop 1 gives 1 .. 9, and loops 2 .. 8 give 1 .. 13
    (site 14 free). Loop 4, futures 8, 12, 16, 20, 24: 1 .. 13 each time.
    Sites 6 .. 13 jointly: loop 2 needs future 7, loop 3 needs future 6.
  Certificate: word S^10, loop 2, sites 6 .. 13 is UNSAT with a DRAT proof verified by drat-trim (CNF sha256 prefix
  eccb9f681ba207bb, proof 1,291,148 bytes, kept in ~/np-scratch-int/rule30-al outside git). UNSAT stays UNSAT for longer
  words, and a later loop with a following S restarts in 11101 (GC606, GC626), so:
  in every actual clamped-wall trace, a loop with at least two completed S gaps behind it and at least seven
  following S gaps carries the 84-ring's columns 1 .. 13 (columns 1 .. 5 at every loop by GC688). In particular,
  every infinite all-S trace has the ring's thirteen near-wall columns from time 12 on. Site 14 is free in every finite
  word tried, which says nothing yet about infinite futures.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule30_neutral_concat as nl                                    # noqa: E402

RING = 0x688eb74a45efb082671ee
N, LOOP = 84, 6
ENTRANCE = (1, 1, 0, 1)            # sites 2 .. 5 at time 0 (site 1's 1 comes from the visible word): 11101
LOOPS = range(0, 9)
FUT = 14


def ring_cols(maxsite):
    row = [(RING >> i) & 1 for i in range(N)]
    hist = [row]
    for _ in range(LOOP - 1):
        row = [row[(i - 1) % N] ^ (row[i] | row[(i + 1) % N]) for i in range(N)]
        hist.append(row)
    return {(t, i): hist[t][i] for t in range(LOOP) for i in range(1, maxsite + 1)}


def query(K, k, sites, ref):
    cons, Tend = nl.targets('S' * K, 'A', 0)
    cons = cons + [(0, i, v) for i, v in zip(range(2, 6), ENTRANCE)]
    body, ncl, nv, off, width = nl.base(Tend, max(max(sites), 5, max(i for _, i, _ in cons)))
    lits = []
    for s in range(LOOP):
        t = LOOP * k + s
        for i in sites:
            assert t <= Tend and i <= width[t]
            lits.append(-(off[t] + i) if ref[(s, i)] else off[t] + i)
    units = ['%d 0' % (off[t] + i if v else -(off[t] + i)) for t, i, v in cons] + [' '.join(map(str, lits)) + ' 0']
    r = nl.kissat('p cnf %d %d\n' % (nv, ncl + len(units)) + body + '\n'.join(units) + '\n', 600)
    return {20: 'UNSAT', 10: 'SAT'}.get(r.returncode, 'UNKNOWN')


def least_future(k, sites, ref):
    v = {K: query(K, k, sites, ref) for K in range(k + 2, k + 2 + FUT)}
    mono = all(not (v[K] == 'UNSAT' and v[K + 1] != 'UNSAT') for K in list(v)[:-1])
    first = next((K for K in sorted(v) if all(v[K2] == 'UNSAT' for K2 in v if K2 >= K)), None)
    return (first - k - 1 if first is not None else None), mono, ''.join(x[0] for x in (v[K] for K in sorted(v)))


def main():
    ref = ring_cols(8)
    assert [ref[(0, i)] for i in range(1, 6)] == [1, 1, 1, 0, 1]
    c1 = query(2, 0, (1, 2, 3, 4, 5), ref) == 'UNSAT'
    print('ASF-C1', 'PASS' if c1 else 'FAIL', flush=True)
    allmono, f6, f67, f7 = True, {}, {}, {}
    for k in LOOPS:
        a, m1, r1 = least_future(k, (6,), ref)
        b, m2, r2 = least_future(k, (6, 7), ref)
        c, m3, r3 = least_future(k, (7,), ref)
        allmono &= m1 and m2 and m3
        f6[k], f67[k], f7[k] = a, b, c
        show = lambda x: x if x is not None else 'SAT to K=%d' % (k + 1 + FUT)
        print('loop %d: site 6 %s (%s); sites 6..7 %s (%s); site 7 %s (%s)' % (k, show(a), r1, show(b), r2, show(c), r3),
              flush=True)
    print('ASF-C2', 'PASS' if allmono else 'FAIL')
    print('ASF-P1', 'HELD' if any(f6[k] == 1 for k in LOOPS) else 'REFUTED')
    print('ASF-P2', 'HELD' if any(f7[k] is not None and f7[k] <= 8 for k in LOOPS) else 'REFUTED')
    print('COMPLETE')


if __name__ == '__main__':
    main()
