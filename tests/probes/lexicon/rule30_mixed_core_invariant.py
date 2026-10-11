"""GC1087: the ordinary low core closes through arbitrarily many S returns.

Missing inference: GC1086 left the white-eleventh core escape open.
Record searched:1110011011000|111100010|white.eleventh core ->3 hits
in3 files; GC1085/1086 read. An initial broad search was discarded.
P1 BEFORE controls: actual time4packet000001 at9..14 forces white15
using time2prefix001. Thus E=1 always gives a black eleventh high bit;
E=0 gives high10..13=1000. P2: high1000 reaches001011 at time4.
P3 BEFORE controls: high100 (site13 free) already reaches that packet,
and guarded B outputs high100. All three HELD locally and by hand.
P4 BEFORE controls: C->C orJ, J->guarded B, guarded B->C orJ closes
every renewal length by induction. J is high100* orhigh11110;
guarded B has10=0 and (11=0 implies12=0). Reuse reviewed GC1078,
GC1084 and GC1086; no repeated long-history or language census.
Counterfactual: a fresh time4 first packet can assign black15. Four
controls show that it returns101 with11 white,12 black, outsideJ;
the actual earlier core rows forbid that assignment.
Unexpected: generic high1000 may yield B13 black; the old two-white
pair closure stays refuted. The invariant needs only the sparse B12
implication and permits the actual high1001 successor.
Controls: backward local packet, complementary pair, scalar closing,
then literal/packed high and outgoing short cones. No solver, CUT,
membership or record run. All-depth R_real(d) remains OPEN.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_core_short_bridge import propagate
from rule30_low_core_closure import D


def main():
    backward = qualified = pair = white = high = short = counterfeit = 0
    # Sites6 onward, time2: a core's actual prefix001 is essential.
    for far in product((0, 1), repeat=10):
        rows = propagate(bits('001') + far, D[2:4])
        if rows[2][3:9] == bits('000001'):
            assert rows[1][3:10] == bits('1111011')
            assert rows[2][9] == 0
            qualified += 1
        backward += 1
    # The newly forced white15 supplies the sparse complementary pair.
    for far in product((0, 1), repeat=2):
        rows = propagate(bits('0100000010') + far, D[4:6])
        assert rows[1][9] | rows[1][10]
        assert rows[2][9] == 0
        pair += 1
    # E=0,J=1 at time6: closing always gives high1000 at10..13.
    for far in product((0, 1), repeat=4):
        rows = propagate(bits('11010001') + far, D[6:])
        assert rows[4][:8] == bits('11011000')
        white += 1
    # The broader high100 shield is what the guarded short actually emits.
    for far in product((0, 1), repeat=5):
        rows = run(bits('111001101100') + far, 4)
        assert rows[1][9:11] == (0, 1)
        assert rows[2][9:11] == (0, 1)
        assert rows[3][9:11] == (0, 1)
        assert rows[4][5:11] == bits('001011')
        high += 1
    high_outputs = 0
    for far in product((0, 1), repeat=6):
        rows = run(bits('111010011000') + far, 6)
        if rows[6][6:9] == bits('101'):
            assert rows[4][11] == 1
            assert rows[5][9:12] == bits('111')
            assert rows[6][9:12] == bits('100')
            high_outputs += 1
        short += 1
    for far in product((0, 1), repeat=2):
        rows = propagate(bits('010000001110') + far, D[4:])
        assert rows[6][1:4] == bits('101')
        assert rows[6][5:7] == (0, 1)
        counterfeit += 1
    print(dict(backward=backward, qualified=qualified, pair=pair,
               white_closing=white, high=high, short=short,
               high_outputs=high_outputs, counterfeit=counterfeit,
               literal_packed='PASS', mixed_core='ALL-LENGTH HAND INDUCTION',
               all_depth_records='OPEN'))


if __name__ == '__main__':
    main()
