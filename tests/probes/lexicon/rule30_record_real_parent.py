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

OUTCOME: (filled in after the run, below this line)
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


if __name__ == '__main__':
    main()
