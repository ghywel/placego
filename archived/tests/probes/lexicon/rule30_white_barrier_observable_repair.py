"""GC1067: a specific third-row barrier has an observable four-tick repair.
Missing inference: GC1066's feasible 10001 child with free inputs010
cannot keep three full rows. Can a changed child representative heal
before its discrepancy reaches column1? Test the alternating collar.
Record searched:010100|010101 + merge|coalesce|repair|rewrite|four tick
->13 hits in8 files;01100|010100 + origin|third|halfwidth|boundary
->44 hits in19 files. GC1057/1059's masks and GC1065's actual origin
retention reused. No matching four-tick coupled construction found.
P1 BEFORE execution: for every W>=6, every earlier prefix and wall
phase, initial last6=010100 with input0100 and last6=010101 with
input0101 differ only at the last two cells, then coalesce at tick4.
Copying ANY subsequent controlled inputs retains all future rows and
the complete column1 trace. This is a controlled equivalence first.
P2: retained original prefix through j-1 ending010101, j>=7, has a
time2 child suffix01010 through j whenever Q0. Replace original
sites j..j+6 by0000001: child next4=1001, hence actual future inputs
0101. This gives an actual ORIGINAL cone for the repaired four ticks.
Counterfactual: the stricter GC1066 row-retention failure forbids even
this changed-representative trace repair. Actual controls must refute it.
Retained hand failure: collar01100 was first considered; its first
updated inner neighbour is white, so the second row gains an inward
discrepancy. The asserted outward-only transfer there is false.
Unexpected guard: replacing target input0100 by0101 prevents tick4
coalescence, despite the valid new actual origin. Do not drop last0.
Controls: independent literal/packed original cones, decimal-table
strips, both phases, arbitrary earlier/farther bits. No solver, width,
visible-language, NFA or return-word census. Later ACTUAL exterior
compatibility remains missing; controlled copying is not actualization.
P3 informed AFTER the first passing run, before extended controls:
the common tick4 row ends01. Its last bit remains1 on tick5; these
two black centres mask arbitrary target inputs at ticks4,5. The same
original cone therefore lifts SIX future updates after target0100,
with any two next samples. This is another application of the mask,
not a claimed lift of arbitrary later inputs or an iterated invariant.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_trace_prefix_repair import strip, trace


def main():
    mergers = guarded_failures = 0
    for p, q, phase, x, y in product((0, 1), repeat=5):
        old = (p, q) + bits('010100')
        new = (p, q) + bits('010101')
        left = strip(old, bits('0100') + (x, y), phase)
        right = strip(new, bits('0101') + (x, y), phase)
        W = len(old)
        expected = [{W-1}, {W-2, W-1}, {W-1}, {W-2, W-1}, set()]
        for t in range(5):
            diff = {i for i in range(W) if left[t][i] != right[t][i]}
            assert diff == expected[t]
        assert left[4:] == right[4:]
        assert trace(left) == trace(right)
        bad = strip(old, bits('0101'), phase)
        assert bad[4][:-1] == right[4][:-1]
        assert bad[4][-1] != right[4][-1]
        mergers += 1
        guarded_failures += 1
    lifts = 0
    for p, phase, h, k, x, y in product((0, 1), repeat=6):
        prefix = (p,) + bits('010101')
        # j=8, W=9; the earlier bit p is arbitrary.
        ref = run(prefix + bits('001110') + (0, 0, 0), 2, phase)
        child = ref[2][:9]
        assert child[-6:] == bits('010100')
        actual = run(prefix + bits('0000001') + (h, k, 1-h, 1-k), 8, phase)
        assert actual[2][:8] == child[:8]
        assert actual[2][8:12] == bits('1001')
        wanted = strip(child, bits('0100') + (x, y), phase)
        new = strip(child[:-1] + (1,), bits('0101'), phase)
        assert tuple(actual[t+2][9] for t in range(4)) == bits('0101')
        assert all(actual[t+2][:9] == new[t] for t in range(5))
        assert wanted[4][-2:] == (0, 1)
        assert wanted[5][-1] == 1
        assert all(actual[t+2][:9] == wanted[t] for t in range(4, 7))
        assert trace(actual) == trace(ref[:2]) + trace(wanted)
        lifts += 1
    for phase in (0, 1):
        a = strip(bits('01100'), bits('0100'), phase)
        b = strip(bits('01101'), bits('0101'), phase)
        assert a[2][-3] != b[2][-3]  # Discharges retained hand failure.
    print({'controlled_mergers': mergers, 'actual_origin_lifts': lifts,
           'terminal_sample_guards': guarded_failures,
           'discarded_collar_controls': 2, 'literal_packed': 'PASS',
           'full_prefix_at_tick4': 'PASS', 'six_future_updates': 'PASS',
           'observable_repair': 'PASS'})


if __name__ == '__main__':
    main()
