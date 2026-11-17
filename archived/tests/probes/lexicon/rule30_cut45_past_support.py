"""GC1038: does the origin guard use CL198's distant common pins?

Missing inference: explain GC1037's dependence on pins17,18,19,23,
rather than treat the common19 premise as one opaque conjunction.
Record searched: (origin|cut45) + (prefix15|width20|first15|first 15)
-> no hit, including ledgers.
P1: fixing only sites1..15 to CL198's prefix still excludes x16=x20=1
under the leading0 entry. Confidence 0.4. One width20 past relation;
this is a weakening of pin hypotheses, not a larger-window sweep.
Counterfactual: a surviving relaxed past refutes this weakened guard,
not the original GC1037 guard or the actual cut.
Controls: GC1037's independent parent and nonvacuous forward controls;
every retained counterexample is replayed with the literal rule.
Unexpected check: a refuting path must violate one of the discarded
common pins17..19, or else it needs a continuation at21..24 incompatible
with pin23; distinguish these alternatives explicitly.
Caps: 20000 rows, 30 seconds; no SAT or actual-language membership run.
First outcome: P1 REFUTED; 42 leading0 initial rows, peak743.
Unexpected: the first literal counterexample obeys pins17..19 too.
Thus the projection alone does not implicate those three pins. BEFORE
the adaptive check: P2, releasing only pin23 in width24 admits a
leading0 past (confidence0.7). Check the original pin23=1 as a negative
control, and replay any pin23=0 path. If P2 fails, the width20 path may
be unextendible; do not claim pin23 necessary on projected evidence.
Implementation repair before publication: the first P2 call mistakenly
ORed released bits into PIN without clearing site23's original1. It
repeated the original premise and gave a false deletion conclusion.
Assert the eight values of each pin23 branch at the source; clear the
released bit before filling. No original-P2 verdict is retained as valid.
OUTCOME after repair: P2 REFUTED. All16 source fillings now represented,
eight for each pin23 value; no leading0 past, peak310. Thus pin23 is
dispensable for the backward implication; common18 suffice there.
GC1036's forward guard still uses common19.
The projected counterexample has illegal exterior-column updates at
6,12,20,25: x20=0, x21=1, x21(next)=0. Rule30 forces that next bit1
regardless of x22. This is the known GC1022 type of boundary defect,
now localized in this origin test, not a new general method.
Stop premise deletions: the common-pin forcing lemma remains open.
"""

import signal
from rule30_cut45_origin_past import ENTRY, PIN, controls, literal, parents


def main():
    controls()
    width = 20
    prefix = sum(int(c) << i for i, c in enumerate(PIN[:15]))
    rows = {}
    for middle in range(8):
        origin = prefix | (1 << 15) | (middle << 16) | (1 << 19)
        rows[origin] = (0, origin)
    peak = len(rows)
    for t in range(29, -1, -1):
        nxt = {}
        for child, (inputs, origin) in rows.items():
            for parent, exterior in parents(child, t % 2, width):
                if t % 2 == 0 and parent & 1 != int(ENTRY[t // 2]):
                    continue
                nxt.setdefault(parent, (inputs | (exterior << t), origin))
        rows = nxt
        peak = max(peak, len(rows))
        if len(rows) > 20000:
            raise RuntimeError('row cap; no conclusion')
    print('P1', not rows, 'initial_rows', len(rows), 'peak', peak)
    if rows:
        initial, (inputs, origin) = next(iter(rows.items()))
        row = initial
        boundary_failures = []
        for t in range(30):
            if t % 2 == 0:
                assert row & 1 == int(ENTRY[t // 2])
            if t < 29 and (inputs >> t) & 1:
                inside = (row >> 19) & 1
                if ((inputs >> (t+1)) & 1) != 1-inside:
                    boundary_failures.append(t)
            row = literal(row, t % 2, (inputs >> t) & 1, width)
        assert row == origin
        assert format(origin, '020b')[::-1][:15] == PIN[:15]
        assert all(origin & (1 << (i-1)) for i in (16,20))
        mismatches = [i for i in (17,18,19)
                      if ((origin >> (i-1)) & 1) != int(PIN[i-1])]
        print('initial', format(initial, '020b')[::-1],
              'inputs', format(inputs, '030b')[::-1],
              'origin30', format(origin, '020b')[::-1],
              'discarded_pin_mismatches', mismatches,
              'boundary_update_failures',boundary_failures,
              'literal replay PASS')
        assert boundary_failures == [6,12,20,25]
    single_pin_check()
    single_pin_check(1)


def single_pin_check(lead=0):
    width = 24
    assert PIN[22] == '1'
    fixed = sum(int(c) << i for i,c in enumerate(PIN)) & ~(1 << 22)
    origins = {}
    for label in range(16):
        origin = fixed | (1 << 15) | (1 << 19)
        for j,i in enumerate((21,22,23,24)):
            origin |= ((label >> j) & 1) << (i-1)
        origins[origin] = (1 << label, 0, origin)
    assert len(origins) == 16
    assert sum(bool(row & (1 << 22)) for row in origins) == 8
    rows = origins
    peak = len(rows)
    for t in range(29,-1,-1):
        nxt = {}
        for child, (labels, inputs, origin) in rows.items():
            for parent, exterior in parents(child,t % 2,width):
                sample = lead if t == 0 else int(ENTRY[t // 2])
                if t % 2 == 0 and parent & 1 != sample:
                    continue
                if parent in nxt:
                    oldlabels, oldinputs, oldorigin = nxt[parent]
                    nxt[parent] = (oldlabels | labels, oldinputs, oldorigin)
                else:
                    nxt[parent] = (labels, inputs | (exterior << t),origin)
        rows = nxt
        peak = max(peak,len(rows))
        if len(rows) > 20000:
            raise RuntimeError('single-pin row cap; no conclusion')
    mask = 0
    for labels, _, _ in rows.values():
        mask |= labels
    labels = [k for k in range(16) if mask & (1 << k)]
    if lead:
        assert rows and any(k & 4 for k in labels)
        print('leading1 positive countercontrol PASS',len(rows),'initial rows')
        return
    assert all(not (k & 4) for k in labels), 'original pin23=1 guard must survive'
    print('P2', bool(rows), 'pin23=1 control PASS', 'labels', labels,
          'initial_rows', len(rows), 'peak', peak)
    if rows:
        initial, (_, inputs, origin) = next(iter(rows.items()))
        row = initial
        for t in range(30):
            if t % 2 == 0:
                assert row & 1 == int(ENTRY[t // 2])
            row = literal(row,t % 2,(inputs >> t)&1,width)
        assert row == origin
        mismatches = [i for i in range(1,25) if i not in (16,20,21,22,24)
                      and ((origin >> (i-1))&1) != int(PIN[i-1])]
        assert mismatches == [23]
        print('single_pin_initial',format(initial,'024b')[::-1],
              'inputs',format(inputs,'030b')[::-1],
              'origin30',format(origin,'024b')[::-1],
              'common_pin_mismatches',mismatches,'literal replay PASS')


if __name__ == '__main__':
    signal.signal(signal.SIGALRM,
                  lambda *_: (_ for _ in ()).throw(RuntimeError('time cap')))
    signal.alarm(30)
    try:
        main()
    finally:
        signal.alarm(0)
