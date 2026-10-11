"""GC1097: four-step black-A ancestry bars its S-D-H-A restart.

Missing inference: complete101-toA selector, beyond GC1096's packet.
Record searched: black.eleventh|GC1096 with101|guard|restart ->16hits
8files; GC1083/91/96 read. No solver, CUT, visible membership or record job.
P1: D8prefix1111 and101-toA requires000001 nextsix. HELD.
P2: D8packet1111000001 with low100100 has short common antecedent.
HELD:1282 eight-step parents,248 qualified, all begin10010001.
P3: low10010001 gives blackA suffix000001 or another branch.
Corrected result: eight qualified packets, suffix000***; no full guard.
P4: actualSS time3prefix01000110 excludes A14..18fivewhites. HELD.
P5: full D8packet transported through blackA's S6 shields forces those
five whites. HELD stronger:384 parents all begin000111110000011.
P6: complete101-toA selector always gives D8prefix1111. REFUTED:
11100 has no two-step past;1101 has four packets, three begin1110.
P7: those three1110 alternatives have no low100100 D past. HELD:
in fact they die after one, two, one backward D updates respectively.
Counterfactual: equalA11=A13black without mature past bars restart.
KnownGC1096 fresh all-tail counter restarts; keep maturity premise.
Unexpected: P6's three alternative packets explain why the first-four
prefix cannot be assumed; they need earlier D past to be excluded.
Independent controls: every inverse edge scalar-forward checked;
all384 final packets forward through S6+D8;64 nonvacuous actualSS
histories literal/packed checked, plus the known fresh counter.
Conclusion: any blackA at even clamped age>=4, followed by S,D and
return101, cannot returnA through its H. ActualSS blackA at6 qualifies.
This local all-tail macro exclusion is not an all-depth record bound.
PROVED: independent Cloud full-row route confirms it, CL274 atc4744f11.
"""
from itertools import product
from rule30_black_A_ancestry_guard import inverse, SOURCE
from rule30_core_short_bridge import bits, propagate, S, D
from rule30_sl_no_refork import run

H = bits('0101101010')
SHIELDS = ('00011111', '10110000', '0010100',
           '111011', '100010', '11011')
PACKET = bits('1111000001')
ACTUAL = bits('111011111111000010000000000000000000')


def lift(rows, track, shields=None):
    counts = []
    for t in range(len(track)-1, -1, -1):
        rows = {x for y in rows for x in inverse(y, track[t])}
        if shields is not None:
            rows = {x for x in rows if x[:len(shields[t])] == bits(shields[t])}
        counts.append(len(rows))
    return rows, counts


def main():
    # Full clamped preimages of both complete A selector alternatives.
    first, _ = lift({bits('11100110111100')}, (0, 1))
    assert not first
    second, _ = lift({bits('1110011011101')}, (0, 1))
    assert len(second) == 4
    packets = {x[5:15] for x in second}
    assert packets == {PACKET, bits('1110111010'),
                       bits('1110111011'), bits('1110111100')}
    failures = []
    for text, depth in (('1110111010', 1), ('1110111011', 2),
                        ('1110111100', 1)):
        rows = {bits(text)}
        for t in range(7, 7-depth, -1):
            rows = {x for y in rows for x in inverse(y, D[t])}
        assert not rows
        failures.append(depth)
    low, low_counts = lift({PACKET}, D[:8])
    assert low_counts == [3, 5, 8, 32, 74, 114, 372, 1282]
    low = {x for x in low if x[:6] == bits('100100')}
    assert len(low) == 248
    assert all(x[:8] == bits('10010001') for x in low)
    origins, origin_counts = lift(low, S, SHIELDS)
    assert origin_counts == [788, 522, 1680, 838, 608, 384]
    assert all(x[:15] == bits('000111110000011') for x in origins)
    for x in origins:
        rows = propagate(x, S+D[:8])
        assert rows[6][:6] == bits('100100')
        assert rows[14] == PACKET
    # The short-packet intermediate claim, separately controlled.
    short, _ = lift({bits('10010001')}, S)
    short = {x for x in short if x[:8] == bits(SHIELDS[0])}
    assert len(short) == 8
    assert all(x[8:11] == (0, 0, 0) for x in short)
    # Actual SS time3 has a stronger guard than is needed by the proof.
    ss_parent, _ = lift({bits('0001111100000')}, bits('010'))
    assert not {x for x in ss_parent if x[:8] == bits('01000110')}
    actual = 0
    for tail in product((0, 1), repeat=5):
        for far in (0, 1):
            rows = run(ACTUAL+tail+(far,)*32, 32)
            assert rows[6][:13] == bits('1110100011111')
            assert rows[12][:11] == bits('11100100100')
            assert rows[22][:9] == bits('111001101')
            assert tuple(r[4] for r in rows[6:32]) == S+D+H
            assert rows[32][:9] == bits('111010011')
            actual += 1
    fresh = run(SOURCE+(0,)*24, 26)
    assert fresh[26][:9] == bits('111010001')
    print(dict(full_selector_parents=4, excluded_D8_depths=failures,
               low_parents=248, black_A_parents=384,
               forward_packet_controls=384, short_packet_controls=8,
               actual_SS_histories=actual, literal_packed='PASS',
               P6='REFUTED; three alternatives require earlier D past',
               mature_S_D_H_A='EXCLUDED AT EVERY EVEN AGE >=4',
               following_B_guard='OPEN', all_depth_bound='OPEN'))


if __name__ == '__main__':
    main()
