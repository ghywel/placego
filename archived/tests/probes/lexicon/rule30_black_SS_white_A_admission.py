"""GC1090: the white-eleventh last-black SS reset enters the mixed core.

Missing inference: GC1089's low001 return with its black-SS past.
Record searched: black.SS|111011111|last black with001|gate|past|inherited
->25 hits in9 files; GC1080/89 read. Failed generic A pair guards closed.
P1 BEFORE controls: A10=A12=1 gives low10=0, hence always D, never X.
P2 BEFORE controls: actual A11=0 forces A13=0; this gives low10,11=01,
whose D admits C. HELD by complementary-pair ancestry and prefix proof.
P2b predicted time5prefix0101 and next100/101. REFUTED: incorrect
fifth-track phase in the hand calculation. Complete controls give010.
P2c before causal controls predicted exact010. The prefix certificate
retains only11100101, sufficient for C={010,011}; exact010 is not used.
Countercontrol: a fresh white-eleventh A with black13 can renew111.
First17-bit diagnostic returned C: concatenation of the retained tuple
was wrong. Correct12-bit A packet plus8-bit tail yields111 at16;
both diagnostics are retained, no source search or new sweep.
Unexpected: black-eleventh A remains outside the admission theorem;
do not strengthen it by the already-failed low pair inequalities.
REFUTED-BY: any failed actual A13=A11 guard, low01 shield or C prefix
implication invalidates the theorem. Scalar fresh-right controls and
literal/packed actual histories are independent checks.
No solver, CUT, membership or record run. All-depth bound OPEN.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_core_short_bridge import update, propagate, S, D, CORE

SS = bits('111010')
LOW_SHIELD = (
    '11100100101', '10011111101', '01110000001', '11001000011',
    '00111100110', '0110001110', '010101100', '11010101',
    '00010101', '00110101', '11100101',
)


def main():
    ancestry = short = white = composed = qualified = 0
    # Actual SS time3packet, including the missing ancestor of the
    # sparse complementary pair at time4sites13,14.
    for far in product((0, 1), repeat=7):
        rows = propagate(bits('01000110') + far, SS[3:])
        out = rows[3]
        assert out[:5] == bits('00011')
        assert out[6] == 1
        assert out[7] == out[5]  # S-A sites13 and11 agree.
        ancestry += 1
    for u in (0, 1):
        for far in product((0, 1), repeat=7):
            out = propagate(bits('00011') + (u, 1) + far, S)[6]
            assert out[:5] == bits('10010')
            short += 1
    for far in product((0, 1), repeat=7):
        rows = propagate(bits('00011010') + far, S)
        assert rows[2][7] == 0  # site13 at short time2.
        assert rows[4][7] == 1  # site13 at short time4.
        assert rows[6][:6] == bits('100101')
        white += 1
    implications = 0
    for t, (old, new) in enumerate(zip(LOW_SHIELD, LOW_SHIELD[1:])):
        for exterior in (0, 1):
            assert update((t % 2,) + bits(old) + (exterior,))[:len(new)] == bits(new)
            implications += 1
    for source in ('11101111111100', '1110111111101'):
        for far in product((0, 1), repeat=5):
            rows = run(bits(source) + far + tuple(1-x for x in far)*8, 22)
            assert rows[6][10] == rows[6][12]
            assert rows[12][9] == 0
            assert tuple(row[4] for row in rows[12:22]) == D
            if rows[6][10] == 0:
                assert rows[12][:11] == bits('11100100101')
                assert rows[22][6:9] in CORE
                qualified += 1
            composed += 1
    assert qualified
    for source, result, thirteenth in (
        ('11101000110100010', '010', 0),
        ('111010001101' + '10100010', '111', 1),
    ):
        rows = run(bits(source) + (0,)*40, 16)
        assert rows[0][10] == 0 and rows[0][12] == thirteenth
        assert rows[16][6:9] == bits(result)
    print(dict(ancestry=ancestry, short=short, white=white,
               prefix_implications=implications, composed=composed,
               admitted=qualified, literal_packed='PASS',
               white_A11='ALL-TAIL CORE ADMISSION',
               black_A11='OPEN', all_depth_bound='OPEN'))


if __name__ == '__main__':
    main()
