"""GC1061: the delayed packet selects a prefix-compatible lift bit.
Missing inference: enforce GC1060's forced next-child bit when choosing
a future trace representative; use GC1030, not another width census.
Record searched:1001000|0011111 with ancestr|preimage|past|two.tick|time.?2
->22 hits, including GC1004/1005 and GC1030; no complete packet origin.
P1 before controls: at black start, time2 prefix1001000 iff initial
prefix0011111 and initial c=x8,d=x9 satisfy c OR d=1.
Then R=time2 x8=c XOR(d OR e), e=initial x10. At white start the
packet cannot occur at time2 (GC1004's black-image obstruction).
P2: existing GC1030 gives x1(15)=NOT R. Initial x8=0 locks R=1;
any future representative preserving packet and its 14-symbol trace
has that same R. Initial x8=1 permits either R, explicitly.
Counterfactual: the packet branch is vacuous even at black start.
Nonvacuity:001111101 produces packet with R=1, any farther tail.
Independent controls: literal/packed cones for the eight c,d,e cases,
plus two farther-tail extremes; no solver, word or width census.
Unexpected check:0011111100 produces R=1,0011111110 R=0:
packet ancestry alone does NOT force R=1. No old transport rerun.
The proof uses local equations; these selected controls are evidence.
No whole-tail lift, general representative selection or prize claim.
"""
from itertools import product
from rule30_sl_no_refork import bits, run


def main():
    cases = endpoint_checks = 0
    for c, d, e in product((0, 1), repeat=3):
        source = bits('0011111') + (c, d, e)
        child = run(source, 2, 1)[2]
        assert (child[:7] == bits('1001000')) == bool(c | d)
        if c | d:
            R = c ^ (d | e)
            assert child[7] == R
            # Compose the reviewed transport on two selected actual tails.
            # This does not rerun its exhaustive arbitrary-input proof.
            for farther in (0, 1):
                actual = run(source + (farther,)*6, 15, 1)
                assert actual[2][:8] == bits('1001000') + (R,)
                assert actual[15][0] == 1-R
                endpoint_checks += 1
        cases += 1
    assert run(bits('0011111010'), 2, 1)[2] == bits('10010001')
    assert run(bits('0011111100'), 2, 1)[2] == bits('10010001')
    assert run(bits('0011111110'), 2, 1)[2] == bits('10010000')
    # Independent short negative control behind the white-phase exclusion.
    for tail in product((0, 1), repeat=6):
        assert run(tail, 1, 1)[1] != bits('10010')
    print({'local_cases': cases, 'actual_endpoint_controls': endpoint_checks,
           'black_image_negative_controls': 64,
           'literal_packed': 'PASS', 'nonvacuity': 'PASS',
           'ancestry_alone_R1': 'REFUTED as predicted'})


if __name__ == '__main__':
    main()
