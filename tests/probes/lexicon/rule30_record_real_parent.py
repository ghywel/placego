#!/usr/bin/env python3
"""rule30_record_real_parent.py: do the record witnesses' formal parents exist in reality? Local's first block as the
maths lead (AGENTS.md item 19), on door 1 (the black-run side) after loop check 1.

Background. Tonight's B4 (rule30_band_guard_read.py) found the depth-125 record and its neighbours born at the youngest
age: the white band [d, E] of the phase-p child is a Q or P birth from a black run in the age-1 canonical (formal)
parent. That parent is C_1(w) for p = 0 and C_0(0w) for p = 1, where w is the child's visible word (GC1170). It is a
real configuration's forced row exactly when its root is a real visible word of its phase: w in L_1 (p = 0), or 0w in
L_0 (p = 1). GC1169 gave one real phase-1 word with no real phase-0 prepend. If record bands always have real parents,
the real white record at depth d is tied to the real black-run record of the other phase at depth d (a forward
inequality holds anyway: a real black run of length K at depth s becomes, one tick later, a real white band of length
K - 1 at depth s). If they often do not, long bands need roots whose prepends are not real, and that is a candidate
source of the missing price.

RUN-ON:     cpu, kissat for RLK's membership (in_language_phase); minutes.
COMMAND:    KISSAT=kissat python3 tests/probes/lexicon/rule30_record_real_parent.py

Record searched (record_find, 2026-10-13 22:50 BST): 'real parent|real prepend|prepend' -> 48 hits in 13 files (GC1169's
example, G141/G149's wall predecessors and free prepends of compatible rows, other objects); 'formal parent.*real|
non-real parent' -> 4 hits in 2 files (GC1170's origin guard). The witnesses are the committed fixture
site/wolframcollatzmahler/data/records.json (141 rows, depths 20 .. 160, 74 in phase 0 and 67 in phase 1).

PREDICTIONS (written 2026-10-13 22:50 BST, before the run).
  P1 must hold (the instrument): for every row, forced_row(visible, phase) reproduces the fixture's left row, and the
     canonical first-nonwhite birth age is found within GC1174's budget.
  P2 blind (0.7): both outcomes occur in each phase: some witnesses have a real age-1 parent and some do not.
  P3 blind (0.5): every witness at depth >= 100 is an age-1 birth.
  P4 (reported, no prediction): the parent black run's length against L + 1, and the real-parent fraction by depth.

OUTCOME (2026-10-13 22:52 BST, M5; machine output quoted): P1 HELD, P2 HELD, P3 REFUTED.
  P1: forced rows reproduce the fixture and births are found for all 141 rows.
  Birth ages: 140 rows at age 1 (93 Q, 47 P) and one at age 2 (d = 152, p = 0, L = 18, Q). So P3 is refuted, narrowly.
  P2: phase 0: 73 age-1 births, 66 with a real parent, 7 without; phase 1: 67, 49 real, 18 without. By depth:
     20 .. 59: 36 real, 4 not; 60 .. 99: 30 and 10; 100 .. 160: 49 and 11. The rows come in runs served by one
     configuration: 125 .. 128 (the R_real(125) = 21 witness) has no real canonical parent; 129 .. 139, including the
     largest record (133, L = 23, a P birth with a black run of at least 23 from 134), has a real one.
  P4: every age-1 parent run is exactly at least L + 1 (Q) or L (P), the minimum, determined to the horizon.

ADDENDUM PREDICTION (2026-10-13 22:54 BST, before the run): a phase-1 child has two formal parents, C_0(0w) and C_0(1w)
  (the parent's first white sample is free, and both advance to C_1(w), GC1170); the census tested only the canonical 0.
  P5 blind (0.5): some of the 18 phase-1 rows without a real canonical parent have a real 1w parent; for those the
     forward image is the same child, and the parent's own birth shape is reported.
  P5 HELD (2026-10-13 22:53 BST): 9 of the 18 rows have a real 1w parent (37, 67 .. 69, 87 .. 91). No real age-1 parent
     at all for 16 of the 140 age-1 rows: phase 0 at 41, 43, 44, 80, 86, 122, 147, and phase 1 at 112 .. 114, 125 .. 128,
     151, 153. The R_real(125) = 21 witness is one of them: that configuration has no real wall-keeping past at all.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rule30_relaxed_records_k as rlk                                  # noqa: E402
from rule30_extremal_p_corner_read import forced_row                    # noqa: E402


def birth(vis, p, d, E):
    for n in range(1, (d - p) // 2 + 2):
        A = forced_row([0] * ((n + p) // 2) + vis, (p + n) % 2)
        if not all(A[j] == 0 for j in range(d - n, E + n + 1)):
            return n, A
    return None, None


def main():
    rows = json.load(open(os.path.join(HERE, '..', '..', '..', 'site', 'wolframcollatzmahler', 'data', 'records.json')))['rows']
    ok1, stats = True, []
    for r in rows:
        p, d, L = r['phase'], r['depth'], r['L']
        E = d + L - 1
        vis = [int(c) for c in r['visible']]
        left = [int(c) for c in r['left']]
        fr = forced_row(vis, p)
        ok1 &= fr[1:len(left) + 1] == left
        a, A = birth(vis, p, d, E)
        ok1 &= a is not None
        s = d - a + 1
        typ = 'Q' if A[s] == 1 else ('P' if A[s - 1] == 1 and A[s] == 0 else '?')
        start = s if typ == 'Q' else s + 1
        run = 0
        while start + run < len(A) and A[start + run] == 1:
            run += 1
        root = r['visible'] if p == 0 else '0' + r['visible']
        real = rlk.in_language_phase(root, 1 if p == 0 else 0) if a == 1 else None
        stats.append((d, p, L, a, typ, run, real))
        print('d=%3d p=%d L=%2d: birth age %d %s, parent run >= %d (L+1 = %d)%s' % (
            d, p, L, a, typ, run, L + 1, '' if real is None else ', formal parent REAL' if real else ', formal parent NOT REAL'),
            flush=True)
    print('P1 forced rows reproduce the fixture and births found:', 'HELD' if ok1 else 'FAILED')
    for p in (0, 1):
        rr = [s for s in stats if s[1] == p and s[3] == 1]
        print('phase %d: %d age-1 births, %d with a real parent, %d without' % (
            p, len(rr), sum(1 for s in rr if s[6]), sum(1 for s in rr if s[6] is False)))
    both = all(any(s[1] == p and s[6] is True for s in stats) and any(s[1] == p and s[6] is False for s in stats)
               for p in (0, 1))
    print('P2 both outcomes in each phase:', 'HELD' if both else 'REFUTED')
    deep = [s for s in stats if s[0] >= 100]
    print('P3 every witness at depth >= 100 is an age-1 birth:', 'HELD' if all(s[3] == 1 for s in deep) else 'REFUTED',
          '| ages there:', sorted({s[3] for s in deep}))


def p5():
    rows = json.load(open(os.path.join(HERE, '..', '..', '..', 'site', 'wolframcollatzmahler', 'data', 'records.json')))['rows']
    found = 0
    for r in rows:
        if r['phase'] != 1:
            continue
        p, d, L = 1, r['depth'], r['L']
        if rlk.in_language_phase('0' + r['visible'], 0):
            continue
        real1 = rlk.in_language_phase('1' + r['visible'], 0)
        A = forced_row([1] + [int(c) for c in r['visible']], 0)
        run = 0
        while d - 1 + run < len(A) and A[d - 1 + run] == 1:
            run += 1
        white = all(A[j] == 0 for j in range(d - 1, d + L + 1))
        found += real1
        print('d=%3d p=1 L=%2d: 0w not real; 1w %s; 1w-parent cells from d-1: %s' % (
            d, L, 'REAL' if real1 else 'not real', 'white band (inherits)' if white else 'black run %d' % run), flush=True)
    print('P5 some phase-1 row has a real 1w parent:', 'HELD' if found else 'REFUTED', '(%d rows)' % found)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'p5':
        p5()
    else:
        main()
