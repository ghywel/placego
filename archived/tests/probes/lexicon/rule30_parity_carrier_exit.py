"""GC1095: a static third-image carrier loses a valid recurrent orbit.

Missing inference: phase persistence needs a carrier preserved under F.
Record searched: parity.phase|white.parity|parity.origin|OR3|
phase.distinction with persist|invariant|merger|nilpotent ->15 hits in8
files; third.image|white.parity|parity.origin with forward.closed|
forward.invariant|carrier ->one unrelated board paragraph. GC1094 read.

P1 before controls: U=F^3(A_even) union F^3(A_odd) is not forward closed.
OR3 formulas predict U forbids0010: output pair00 forces four hidden
zeros; its next pair is00/11 on one origin parity and00/01 on the other.
The named1000 period4 row has the eight-cycle recorded below. Its third
image1011 is in U, its fourth0010 is not. This refutes only the static
carrier shortcut, not every phase invariant or finite-type route.
Counterfactual: the recurrent cycle is not nilpotent or a wall witness.
Unexpected check: every spatial column must fail temporal period2.
Initial six-cycle prediction REFUTED:0111 maps0100, not1000; scalar and
packed updates agreed. The unchanged fourth-step carrier exit remains.
Controls:64 literal/packed OR3 packets,256 arbitrary-exterior cylinders
and the exact eight-cycle. No new fixed-time graph, solver or record run.
"""
from itertools import product

from rule30_forced_odd_period_bridge import evolve
from rule30_two_step_parity_bridge import ring


ORBIT = ('1000', '1101', '0001', '1011', '0010', '0111', '0100', '1110')


def bits(s):
    return tuple(map(int, s))


def even_pair(a, b, c, g):
    return a ^ b ^ ((1-c) & g), b | c | g


def odd_pair(a, b, c, g):
    return a | b | c, a ^ b ^ ((1-c) & g)


def main():
    packets = zero_pairs = 0
    for white_even in (True, False):
        formula = even_pair if white_even else odd_pair
        for a, b, c, g, h in product((0, 1), repeat=5):
            row = tuple(v for z in (a, b, c, g, h)
                        for v in ((z, 0) if white_even else (0, z)))
            actual = evolve(row, 3)[3]
            expected = formula(a, b, c, g)+formula(b, c, g, h)
            assert actual == expected and actual != (0, 0, 1, 0)
            if actual[:2] == (0, 0):
                assert (a, b, c, g) == (0, 0, 0, 0)
                assert actual[2:] in (((0, 0), (1, 1)) if white_even
                                     else ((0, 0), (0, 1)))
                zero_pairs += 1
            packets += 1
    rows = tuple(map(bits, ORBIT))
    assert len(set(rows)) == 8
    for t, row in enumerate(rows):
        assert ring(row) == rows[(t+1) % 8]
    assert all(rows[0][i] == 0 for i in (1, 3))
    traces = tuple(tuple(row[i] for row in rows) for i in range(4))
    assert all(any(trace[t] != trace[(t+2) % 8] for t in range(8))
               for trace in traces)
    cylinders = 0
    fixed = bits('100010001000')
    assert evolve(fixed, 4)[4] == bits('0010')
    for exterior in product((0, 1), repeat=8):
        row = exterior[:4]+fixed+exterior[4:]
        assert evolve(row, 4)[4][4:8] == bits('0010')
        cylinders += 1
    print(dict(OR3_packets=packets, zero_pair_packets=zero_pairs,
               all_tail_cylinders=cylinders, recurrent_cycle=8,
               temporal_traces=[''.join(map(str, t)) for t in traces],
               third_image_forbids='0010 PROOF-SKETCH',
               static_carrier_forward_closure='REFUTED',
               alternating_wall_counterexample='NO',
               general_phase_invariants='OPEN', prize_bound='OPEN'))


if __name__ == '__main__':
    main()
