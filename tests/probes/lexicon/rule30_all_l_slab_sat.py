#!/usr/bin/env python3
"""rule30_all_l_slab_sat.py: ALX, exact light-cone checks of the all-L slab (GPT's GC744 four columns and the start-up
gate; Local's ALS, L381). Local's run (chat L384), claimed in CLOUD-LOCAL.md with these predictions pushed before it.

RUN-ON:     cpu (Python 3 and kissat, NL's encoder); seconds
COMMAND:    python3 tests/probes/lexicon/rule30_all_l_slab_sat.py

ALS sampled finite rows; this asks the exact question over the whole light cone, so any right exterior is covered.
Each query is NL's mode-A cone (rule30_neutral_concat.py: the clamped wall white at even times, the visible word and
its closing 1 on site 1) plus GC623's long entrance 111001 on sites 1 .. 6 at time 0, plus one clause saying that at
loop k (times 10k .. 10k + 9) some cell of the named sites differs from the 155-ring's (rule30_all_l_period10.py).
UNSAT means every actual row with that word has the ring's columns there; SAT gives a replayed witness that differs.

PREDICTIONS (Local's, published before the run):
  ALX-Q1 (blind, confidence 0.9; GC744): word LL, loop 0, sites 2 .. 4: UNSAT (the four-column slab is forced).
  ALX-Q2 (control, confidence 0.95): word LL, loop 0, site 5: SAT (ALS saw the alternative 0101101010 at loop 0).
  ALX-Q3 (control, confidence 0.8): word LLL, loop 1, site 5: SAT (ALS saw it once at loop 1).
  ALX-Q4 (blind, confidence 0.6): word LLLL, loop 2, sites 5 .. 6: UNSAT (six columns after two loops, as ALS saw).
  ALX-Q5 (blind, confidence 0.6): word LLLLL, loop 3, sites 5 .. 6: UNSAT.
  ALX-Q6 (blind, confidence 0.8): word LLLLL, loop 3, site 7: SAT (ALS's width saturates at exactly 6).
  ALX-C1 (control): every SAT witness replays its targets and really differs from the ring at the named sites.
Counterfactual: Q1 SAT would refute GC744; Q4 or Q5 SAT would show the six-column slab is not forced by two loops.
OUTCOME, 2026-10-09 10:12 BST (M5, 0.2 s, run at commit b9c3cab1): ALX-C1 PASS (every witness replays and differs).
  ALX-Q1 HELD: UNSAT, so GPT's GC744 four columns are forced over the whole cone (word LL, loop 0, sites 2 .. 4).
  ALX-Q2 HELD and ALX-Q3 HELD: site 5 can differ at loops 0 and 1 (witness 0101100101 against the ring's 0101100000).
  ALX-Q4 REFUTED: word LLLL, loop 2, sites 5 .. 6 is SAT (site 5 0101100101, site 6 1100100100).
  ALX-Q5 REFUTED: word LLLLL, loop 3, sites 5 .. 6 is SAT (site 6 1100101111 against the ring's 1100001111).
  ALX-Q6 HELD: site 7 can differ at loop 3.
  So ALS's six columns after two loops (L381) do not hold for short words: the samples never hit these rows.
  Exploratory follow-up, the same query at every loop of longer words (no predictions; site 5 / sites 5..6 / site 7):
    K = 6:  every loop allows a deviation at 5 and at 5..6.
    K = 8:  site 5 forced from loop 4, sites 5..6 from loop 5.
    K = 10 and K = 12: site 5 forced from loop 2, sites 5..6 from loop 3, through the last loop.
    K = 14: the same (site 5 from loop 2, sites 5..6 from loop 3), and site 7 can differ at every loop.
  Reading: an early deviation at sites 5 and 6 is possible only in a row whose L run ends soon. With at least about
  eight more L's to come, a loop from the third on has the ring's six columns, and the seventh is never forced.
  Exact for each finite word; not yet a statement for infinite all-L.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule30_neutral_concat as nl                                    # noqa: E402

RING = 0x35409b1caa645d715104db5291a2fe8415260ce
N = 155


def ring_cols(maxsite):
    row = [(RING >> i) & 1 for i in range(N)]
    hist = [row]
    for _ in range(9):
        row = [row[(i - 1) % N] ^ (row[i] | row[(i + 1) % N]) for i in range(N)]
        hist.append(row)
    return {(t, i): hist[t][i] for t in range(10) for i in range(1, maxsite + 1)}


def query(word, k, sites, ref):
    cons, Tend = nl.targets(word, 'A', 0)
    cons = cons + [(0, i, v) for i, v in zip(range(2, 7), (1, 1, 0, 0, 1))]
    # make the cone reach the named sites over the loop: give the encoder its widest site
    width_site = max(max(sites), 6)
    body, ncl, nv, off, width = nl.base(Tend, max(width_site, max(i for _, i, _ in cons)))
    lits = []
    for s in range(10):
        t = 10 * k + s
        for i in sites:
            assert t <= Tend and i <= width[t], (t, i)
            v = off[t] + i
            lits.append(-v if ref[(s, i)] else v)          # "this cell differs from the ring"
    clause = ' '.join(map(str, lits)) + ' 0'
    units = ['%d 0' % (off[t] + i if v else -(off[t] + i)) for t, i, v in cons] + [clause]
    text = 'p cnf %d %d\n' % (nv, ncl + len(units)) + body + '\n'.join(units) + '\n'
    r = nl.kissat(text, 600)
    if r.returncode == 20:
        return 'UNSAT', None
    if r.returncode != 10:
        return 'UNKNOWN', None
    init = nl.model(r.stdout, width[0])
    ok = nl.replay(cons, Tend, init)
    rows = nl.rows_from(sum(v << j for j, v in enumerate(init)), Tend + 1)
    differs = any(nl.site(rows[10 * k + s], i) != ref[(s, i)] for s in range(10) for i in sites)
    hist = {i: ''.join(str(nl.site(rows[10 * k + s], i)) for s in range(10)) for i in sites}
    return 'SAT', (ok and differs, hist)


def main():
    ref = ring_cols(8)
    plan = [('ALX-Q1', 'LL', 0, (2, 3, 4), 'UNSAT'), ('ALX-Q2', 'LL', 0, (5,), 'SAT'), ('ALX-Q3', 'LLL', 1, (5,), 'SAT'),
            ('ALX-Q4', 'LLLL', 2, (5, 6), 'UNSAT'), ('ALX-Q5', 'LLLLL', 3, (5, 6), 'UNSAT'),
            ('ALX-Q6', 'LLLLL', 3, (7,), 'SAT')]
    c1 = True
    for name, word, k, sites, want in plan:
        verdict, w = query(word, k, sites, ref)
        if w is not None:
            c1 &= w[0]
        print('%s %s: word %s, loop %d, sites %s: %s%s' % (name, 'HELD' if verdict == want else 'REFUTED', word, k,
              sites, verdict, ('; witness %s (replays and differs: %s)' % (w[1], w[0])) if w else ''), flush=True)
    print('ALX-C1', 'PASS' if c1 else 'FAIL')
    print('ring columns at sites 5, 6, 7 (t = 0 .. 9):', {i: ''.join(str(ref[(s, i)]) for s in range(10)) for i in (5, 6, 7)})
    print('COMPLETE')


if __name__ == '__main__':
    main()
