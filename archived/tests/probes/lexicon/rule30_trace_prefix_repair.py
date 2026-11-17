"""GC1057: test the frozen-initial-row premise of trace halfwidth repair.
Missing inference (CL222): can correlated right extension preserve the
initial strip row? A concrete refutation would force trace-preserving
repair to alter an interior initial bit, instead of appending columns.
Record searched: halfwidth|trace.form|repair with fixed initial/prefix,
initial preservation, outermost, boundary initial ->30 hits; GC1042/1044/
1045 read, no frozen-initial-row counterexample at the halfwidth horizon.
No Local solver, cut-membership, trace census or width sweep duplicated.
P1 registered before controls: at W=3, five samples, strip initial010
with exterior samples10 then zeros yields trace01000, whereas every
actual initial010 row yields01001. Actual initial0111 plus zeros yields
01000. Thus the correct unrestricted trace can require changing site3.
Counterfactual: appending arbitrary actual right cells suffices while
preserving all W initial strip cells. P1 must refute this.
P2 (single bounded stronger-invariant diagnostic): at W=4, seven samples,
all strip traces can be realized keeping its first W-1 initial cells.
Confidence0.6; if false, retain the first literal counterexample and stop.
Independent controls: literal Wolfram-table strip versus packed updates;
actual shrinking cones with every relevant initial suffix at this ONE
width, grouped by the frozen prefix, not unconditioned language size.
Unexpected check: wrong strip boundary11 repairs P1's initial010 trace;
actual matched trace comes from changing site3, not changing site1/2.
Neither a finite success nor failure settles all-length trace exactness.
Informed P3 registered after P1/P2, before its separate controls: every
actual initial01cDE row has five-sample trace0100 followed by
NOT[c AND(D OR E)]; trace01000 iff initial011 and D OR E=1.
Hand algebra, all32 five-input cones, and both farther extremes.
Unexpected P3 check:01101 is positive although site4 is white, so the
origin guard must retain D OR E, not replace it by D.
Informed P4 before local checks: initial strip rows differing only at
last cell coalesce after one update when its left neighbor and first
exterior sample are black. Either wall phase, every strip width>=2.
This local primitive repairs the P1 case; it is not a general repair.
Countercontrol with white exterior must fail coalescence.
OUTCOME:P1 HELD, frozen-W-initial-row repair REFUTED. P2 HELD on
1,024 conditioned width4 strip cases against128 actual initial cones;
this is evidence for retaining W-1 initial cells, not a uniform proof.
P3 controls and independent engines PASS on32 five-input cones.
P4 local merger and white-exterior countercontrols PASS in both phases.
"""
from itertools import product
from rule30_sl_no_refork import bits, run


def strip(start, exterior, phase=0):
    W = len(start)
    rows = [tuple(start)]
    word = sum(b << j for j, b in enumerate(start))
    for t, e in enumerate(exterior):
        old = (((t + phase) & 1),) + rows[-1] + (e,)
        child = tuple((30 >> (4*old[j] + 2*old[j+1] + old[j+2])) & 1
                      for j in range(W))
        word = (((word << 1) | ((t + phase) & 1)) ^
                (word | (word >> 1) | (e << (W-1)))) & ((1 << W)-1)
        assert child == tuple((word >> j) & 1 for j in range(W))
        rows.append(child)
    return rows


def trace(rows):
    return tuple(r[0] for r in rows)


def main():
    s = strip(bits('010'), bits('1000'))
    assert trace(s) == bits('01000')
    for tail in product((0, 1), repeat=2):
        assert trace(run(bits('010') + tail, 4)) == bits('01001')
    assert trace(run(bits('0111') + (0,)*5, 4)) == bits('01000')
    assert trace(strip(bits('010'), bits('1100'))) == bits('01001')
    W, T = 4, 6
    actual = {}
    for initial in product((0, 1), repeat=T+1):
        p = initial[:W-1]
        actual.setdefault(p, set()).add(trace(run(initial, T)))
    checked = 0
    failure = None
    for initial in product((0, 1), repeat=W):
        for ext in product((0, 1), repeat=T):
            tr = trace(strip(initial, ext))
            checked += 1
            if tr not in actual[initial[:W-1]]:
                failure = (initial, ext, tr)
                break
        if failure:
            break
    fibres = 0
    for initial in product((0, 1), repeat=5):
        rows = run(initial, 4)
        tr = trace(rows)
        a, b, c, D, E = initial
        target = (a, b, c) == (0, 1, 1) and bool(D | E)
        assert (tr == bits('01000')) == target
        if (a, b) == (0, 1):
            assert tr[:4] == bits('0100')
            assert tr[4] == 1-(c & (D | E))
        fibres += 1
    for farther in (0, 1):
        assert trace(run(bits('01101') + (farther,)*7, 4)) == bits('01000')
    for phase in (0, 1):
        for first in (0, 1):
            row0, row1 = (first, 1, 0), (first, 1, 1)
            assert strip(row0, (1,), phase)[1] == strip(row1, (1,), phase)[1]
            assert strip(row0, (0,), phase)[1] != strip(row1, (0,), phase)[1]
    assert strip(bits('010'), (1,))[1] == strip(bits('011'), (1,))[1] == bits('110')
    print({'P1': 'HELD'  , 'actual_010_cones': 4,
           'counterfactual': 'REFUTED', 'changed_site3': 'PASS',
           'P2': 'REFUTED' if failure else 'HELD',
           'conditional_strip_cases': checked, 'first_failure': failure,
           'P3_fibre_cones': fibres, 'P3': 'HELD',
           'P4_merger_both_phases': 'PASS', 'OR_not_site4': 'PASS', 'independent_engines': 'PASS'})


if __name__ == '__main__':
    main()
