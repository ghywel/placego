"""GC1089: a last black-marker SS can force A and the low001 reset.

Missing inference: does the last black SS enforce core admission?
Record searched: black.*short|black.*marker|sixth.marker with
001|111010001|core|admission ->22 hits in11 files; GC1054/55/56 read.
ASF's existing finite future forcing is reused, not rerun or reproved.
P1 BEFORE controls: a mature black S cannot give white S-A with10=1.
REFUTED:12/384 local cones, all with initial6..9=1111.
P2 BEFORE controls, after hand derivation: S-A iff black origin is
111011111 and10..14=11100 or1101*. Then A10=A12=1 and next SL is
low001. HELD by scalar elimination and an all-tail prefix shield.
P3 BEFORE controls: GC1088's fixed44-bit source reaches that gate by
54 or60. REFUTED: its retained prefixes are111011110001101 and
1110111100011, still with black marker. Do not extend that origin.
Counterfactual: every S-A returns001. White sourceA0000100 returns
C instead. The black SS past is an essential theorem hypothesis.
REFUTED-BY: any failed selector or shield implication invalidates P2.
Independent controls:1536 complete six-tick literal/packed cones;
local scalar bands and both fresh exterior choices in each shield;
64 selected composed histories, including both selector cylinders.
Unexpected: white A can enter C; marker monotonicity alone does not
prevent its last black SS predecessor from preparing dangerous A.
No solver, CUT, membership or record run. Eventual admission OPEN.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_core_short_bridge import update, propagate, S

SS = bits('111010')


def main():
    cones = resets = 0
    for pre in ('111011101', '111011110', '111011111'):
        for far in product((0, 1), repeat=9):
            rows = run(bits(pre) + far, 6)
            gate = pre == '111011111' and (
                far[:5] == bits('11100') or far[:4] == bits('1101'))
            assert (rows[6][:9] == bits('111010001')) == gate
            if gate:
                assert rows[1][9:13] == bits('0001')
                assert rows[3][9:13] == bits('0110')
                assert rows[4][9:12] == bits('110')
                assert rows[6][9] == rows[6][11] == 1
                resets += 1
            cones += 1
    scalar = 0
    for tail in product((0, 1), repeat=8):
        # At time1, sites6..9=0000. Eliminate the A-image target.
        rows = propagate(bits('0000') + tail, SS[1:])
        assert (rows[5][:4] == bits('0001')) == (tail[:4] == bits('0001'))
        scalar += 1
    # Actual time1 packet00000001 at6..13 gives the finite shield.
    old = bits('00000001')
    for t, expected in ((1, '10000011'), (2, '01000110'), (3, '1110110')):
        new = bits(expected)
        for exterior in (0, 1):
            assert update((SS[t],) + old + (exterior,))[:len(new)] == new
        old = new
    for u, v in product((0, 1), repeat=2):
        row5 = update((SS[4],) + old + (u, v))
        assert row5 == bits('000010') + (1-u, u | v)
        assert update((SS[5],) + row5) == bits('00011') + (u, 1)
    composed = 0
    for source in ('11101111111100', '1110111111101'):
        for far in product((0, 1), repeat=5):
            rows = run(bits(source) + far + tuple(1-x for x in far)*6, 12)
            assert rows[6][:10] == bits('1110100011')
            assert rows[6][11] == 1
            assert rows[12][:9] == bits('111001001')
            composed += 1
    free_a = run(bits('1110100010000100') + (0,)*12, 6)
    assert free_a[6][6:9] == bits('010')
    print(dict(cones=cones, A_resets=resets, scalar=scalar,
               composed=composed, literal_packed='PASS',
               black_SS_A_001='ALL-TAIL HAND SELECTOR',
               eventual_admission='OPEN', all_depth_bound='OPEN'))


if __name__ == '__main__':
    main()
