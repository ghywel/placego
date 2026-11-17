"""GC1068: the first potentially unmasked post-merger input has two origins.
Missing inference: GC1067's actual lift ends after future update6. Can
the actual exterior at future time6 match either requested seventh input?
Record searched:110100|six input|time6 + carrier|origin|image|constant1
->43 hits in19 files; black boundary|constant1 + six|seven + exterior|
origin|image ->31 hits in15 files. GC1067's exact collar reused.
P1 BEFORE controls: the rewritten child's boundary is black at times
0..5, so all those inputs are irrelevant to its interior. Original
sites j..j+6=0000000 force its exterior at future6 to0; 0000111 force1.
The first constructor has child R,S=10. Under constant black R, S0
forces S(t+2)=0 while the black driver continues, hence S6=0.
The second has child R,S,T,U,V=11101. Its right prefixes at successive
times are 1101,0001,1011,001,111,00,1; so S6=1 for every farther tail.
P2: retained original prefix ending010101, j>=7, child Q0, then candidate
R0 with inputs0100xyz has an actual original nine-tick cone: ten
observations, complete interior equality from future4 through7.
Counterfactual: GC1067's fixed0000001 constructor always suffices at
the seventh update. It must fail when the common boundary is white
and the requested seventh input is1, because its actual input is0.
Unexpected guard: in selected j=8 contexts that boundary at future6
is the retained earlier child bit p; p1 masks the wrong seventh input.
Retained hand correction: a first noncanonical S1 construction used
V2 where the six-step readout requires V3. Correct the indexing before
controls; the present explicit 11101 shield is independent of farther bits.
Independent literal/packed actual cones, decimal-table strips, both
phases and selected arbitrary earlier/farther bits. No solver, language
membership, NFA, return-word or strip-width census. Later inputs and
all-context repair remain missing; this is one specific closure step.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_trace_prefix_repair import strip, trace


def main():
    lifts = failed_fixed = masked_fixed = 0
    for p, phase, x, y, G, h, k in product((0, 1), repeat=7):
        prefix = (p,) + bits('010101')
        ref = run(prefix + bits('001110') + (0, 0, 0), 2, phase)
        child = ref[2][:9]
        assert child[-6:] == bits('010100')
        wanted = strip(child, bits('0100') + (x, y, G), phase)
        tail = bits('0000111' if G else '0000000')
        far = (h, k, 1-h, 1-k)
        actual = run(prefix + tail + far, 9, phase)
        assert actual[2][:8] == child[:8]
        assert actual[2][8] == 1
        assert all(actual[t+2][8] == 1 for t in range(6))
        if G:
            assert actual[2][8:13] == bits('11101')
        else:
            assert actual[2][8:10] == (1, 0)
        assert actual[8][9] == G  # Actual seventh exterior sample.
        assert all(actual[t+2][:9] == wanted[t] for t in range(4, 8))
        assert trace(actual) == trace(ref[:2]) + trace(wanted)
        assert actual[8][8] == p
        if G:
            fixed = run(prefix + bits('0000001') + far, 9, phase)
            assert fixed[8][9] == 0
            assert fixed[9][:8] == wanted[7][:8]
            if p == 0:
                assert fixed[9][8] != wanted[7][8]
                failed_fixed += 1
            else:
                assert fixed[9][:9] == wanted[7]
                masked_fixed += 1
        lifts += 1
    print({'actual_seventh_input_lifts': lifts,
           'fixed_origin_failures': failed_fixed,
           'fixed_origin_masked_mismatches': masked_fixed,
           'literal_packed': 'PASS', 'past_and_trace': 'PASS',
           'all_farther_shield_controls': 'PASS'})


if __name__ == '__main__':
    main()
