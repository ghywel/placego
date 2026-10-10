"""GC1064: releasing one origin cell removes white forced-zero carriers.
Missing inference: GC1063's Q0,R0 readout does not translate to arbitrary j.
Use the actual two-tick origin instead: retain initial prefix through j,
not j+1, and retain the COMPLETE time2 child prefix through j, j>=3.
Record searched: two.tick|two.step|halfwidth|child.*prefix with
one.*(cell|bit)|releas|relax|shorter and lift|boundary|origin|freedom
->30 hits in13 files. GC1060's equations reused; no released-cell
whole-child-prefix criterion found. No solver/word/width census.
P1 before controls: put u,a,b at initial j-2..j. For any feasible
child Q=time2 j=0, BOTH values R=time2 j+1 lift, except uab=011,
which forces R=1. Every forced-zero Q0 obstruction is removed.
P2: if Q1, both lift except uab=000 (R=1-c),110,c1 (R1),111 (R1).
P3: initial c=j+1 may change without changing child j-1 iff
b=1 OR P=1, P=u XOR(a OR b). Otherwise child j-1 pins c.
The listed constructions preserve the full child prefix, any farther
tail, and the original first two trace observations for j>=3.
Counterfactual: changing c silently damages a preceding child cell,
so the union of GC1060 pair tables is not a valid lift. Test that guard.
Independent controls: all256 seven-cell cones in both wall phases;
literal truth table and packed updates; construct every allowed R.
Unexpected: 0001 with Q1 permits R1 if only Q is retained, but the
preceding child cell flips. Retaining the whole prefix forbids it.
This releases an INITIAL cell, not a future observation; arbitrary
later child tails and the halfwidth induction remain unproved.
First constructor check FAILED at uab=111,Q1: d was written1 instead
of0. The mixed-pair equation Q=NOT P XOR d gives d0. This executable
witness was corrected; the fibre criterion itself passed that control.
"""
from itertools import product
from rule30_sl_no_refork import bits, run


def allowed(u, a, b, c, Q):
    key = (u, a, b)
    if Q == 0:
        return (1,) if key == (0, 1, 1) else (0, 1)
    if key == (0, 0, 0):
        return (1-c,)
    if key == (1, 1, 1) or (key == (1, 1, 0) and c == 1):
        return (1,)
    return (0, 1)


def extension(u, a, b, c, Q, R):
    key = (u, a, b)
    if key == (0, 0, 0):
        return (0, 0, R) if Q == 0 else ((0, 1, 0) if c == 0 else (1, 0, 0))
    if key == (0, 0, 1) or key == (1, 0, 1):
        return (1, 0, R)
    if key == (0, 1, 0):
        return (0, 0, 1-R)
    if key == (0, 1, 1):
        return (0, 0, 0) if Q == 0 else (1, 0, 1-R)
    if key == (1, 0, 0):
        return (0, 0, R) if Q == 1 else ((1, 0, 0) if R == 0 else (0, 1, 0))
    if key == (1, 1, 0):
        return (0, 0, 1-R) if c == 0 else (1, 0, 0)
    assert key == (1, 1, 1)
    return (1, 0, 1-R) if Q == 0 else (0, 0, 0)


def main():
    cones = lifts = changed = 0
    for row, phase in product(product((0, 1), repeat=7), (0, 1)):
        v, u, a, b, c, d, e = row
        original = run(row, 2, phase)
        target = original[2][:4]
        Q = target[-1]
        predicted = allowed(u, a, b, c, Q)
        seen = set()
        # One local origin fibre, not a width/trace-language census.
        for tail in product((0, 1), repeat=3):
            child = run((v, u, a, b)+tail, 2, phase)[2]
            if child[:4] == target:
                seen.add(child[4])
        assert seen == set(predicted)
        for R in predicted:
            tail = extension(u, a, b, c, Q, R)
            for farther in (0, 1):
                repaired = run((v, u, a, b)+tail+(farther,)*3, 2, phase)
                assert repaired[2][:4] == target
                assert repaired[2][4] == R
                assert tuple(r[0] for r in repaired[:2]) == tuple(r[0] for r in original[:2])
            P = u ^ (a | b)
            if tail[0] != c:
                assert b == 1 or P == 1
                changed += 1
            lifts += 1
        cones += 1
    # A tempting unguarded union preserves Q but damages the child prefix.
    for phase in (0, 1):
        old = run(bits('00001')+(0, 0), 2, phase)[2]
        bad = run(bits('00000')+(1, 0), 2, phase)[2]
        assert old[3:5] == (1, 0) and bad[3:5] == (1, 1)
        assert old[2] != bad[2]
    print({'local_origin_cones': cones, 'constructed_lifts': lifts,
           'released_cell_changes': changed, 'whole_prefix_guard_controls': 2,
           'literal_packed': 'PASS', 'white_forced_zero_release': 'PASS',
           'remaining_011_guard': 'PASS'})


if __name__ == '__main__':
    main()
