"""GC1086: carry the core's black-eleventh branch across S-B.

Missing inference: GC1085's B reset loses actual core ancestry. Core11=1
forces high11100110111110 by GC1084. Prove its image prevents the next
B-to101 unit from returning A; no all-length mixed closure is claimed.
Record searched:11100110111110|11101001100111010000 with
reset|guard|ancestr|prefix|core ->5 hits in3 files; GC1084/1085 read.
P1 BEFORE controls: white B10,11 forces B12,13 white. HELD on1024
complete local high cones, but the hand proof below asserts only B12.
P2 BEFORE controls: generic1011000 has the same implication and B000000
returns1011000. REFUTED: nine images have B13 black, and three of16
short cones instead return1011001. Stop the proposed packet closure.
P3 BEFORE controls: B-to101-toA requires initial B12 black. HELD on
the512 first-antecedent cones, and proved by two time2 branches below.
P4 BEFORE controls: the actual high packet forces time4sites6..11=
001011 and time7=010110. Its closing formulas prove the sparse guard.
Counterfactual: a fresh B tail may restart A; GC1085 proves it, but
its B12 black violates this inherited image when B10,11 are white.
Unexpected check: initial high12,13 are black while its relevant B12
is white. Generic1011000 may have B13 black, so do not infer a closed
two-packet invariant or assert the stronger P1 from these equations.
Independent controls: scalar closing rows, literal versus packed
high/short cones. No solver, CUT, membership or record run.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_core_short_bridge import propagate
from rule30_high_101_shield import FIFTH as H


def main():
    high = closing = short = 0
    for far in product((0, 1), repeat=8):
        rows = run(bits('11100110111110') + far, 10)
        assert rows[2][9:12] == bits('100')
        assert rows[3][9:11] == (0, 1)
        assert rows[4][5:11] == bits('001011')
        assert rows[5][5:11] == bits('111010')
        u, v = rows[5][11:13]
        assert rows[6][10:12] == (1-u, u | v)
        assert rows[7][5:11] == bits('010110')
        K, L = rows[7][11:13]
        assert rows[8][10:12] == (1-K, K | L)
        assert rows[9][9:11] == (K, 1)
        assert rows[10][:10] == bits('1110100110')
        assert rows[10][10] == 1-K
        if K:
            assert rows[10][11] == 0
        high += 1
    # The final three updates do not need any farther origin assumptions.
    for far in product((0, 1), repeat=6):
        rows = propagate(bits('010110') + far, H[7:])
        K, L = far[:2]
        assert rows[1][5:7] == (1-K, K | L)
        assert rows[2][4:6] == (K, 1)
        assert rows[3][:5] == bits('00110')
        assert rows[3][5] == 1-K
        if K:
            assert rows[3][6] == 0
        closing += 1
    # f=0: either g=1 or the high selector forces h=i=0. Both give
    # time3sites11,12=01, making time4site12 black and high11 white.
    for far in product((0, 1), repeat=5):
        rows = run(bits('111010011000') + far, 6)
        g, h, i = far[:3]
        G = g | (1-(h | i))
        if G:
            assert rows[2][10:13] == bits('010' if g else '100')
            assert rows[3][10:12] == (0, 1)
            assert rows[4][11] == 1
            assert rows[6][6:9] == bits('101')
            assert rows[6][10] == 0
        short += 1
    print(dict(high_controls=high, scalar_closing=closing,
               short_controls=short, literal_packed='PASS',
               core_black11_B_101_A='BARRED BY HAND',
               core_white11_branch='OPEN', all_depth_bound='OPEN'))


if __name__ == '__main__':
    main()
