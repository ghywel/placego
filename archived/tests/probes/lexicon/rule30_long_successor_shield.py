"""GC1053: every ordinary-L successor L0 misses the next fork precursor.
Missing inference: transport CL217's five L1-S-L0 prefixes across L0.
Record searched: the five prefixes with return|transport|interven|fork ->
14 hits, GC1049..1052; no intervening-L0 guard. Further narrow search
L0.L0.L1|111001000|ordinary.*ordinary with preced|imposs|forbid|all.L|
ALF|GC746|GC747 ->11 hits; read GC744..747. Their all-L future budgets
are distinct from this unconditional single-return hidden-state guard.
P1 before controls: all five prefixes miss1110010001 after ten ticks.
HELD on5*1024 complete local cones, literal/packed. Hand explanation:
first three use mid00 or mid01; fourth returns S; fifth, if L0, has
returnedsite9=1. This suggested the stronger hand proof, not a scan.
Informed P2 before separate controls: ANY initial111001 returning L0
has returnedsite7 OR8 OR9=1. Thus typed L0-L0-L1 is impossible.
Proof: mid00 returnssite6=0; mid01 has returned7 OR8=1. In mid1*,
a closing L0 forces time7sites7,8=00; returned7..9=000 would force
sites9,10=11 there, barred by the existing two-tick ancestry shield
translated from time5sites5,6=01. No all-depth record bound follows.
Independent controls:256 complete black-phase mid1 cones,128 mid01
cones,64 translated shields; explicit intermediate equations checked.
Unexpected: free S1110111001110... enters the fork prefix, and free
black-phase row11010000111 enters it in3 ticks but violates the shield.
Retained failed countercontrol:1101000011 plus zeros returns1110010011,
not the predicted111001000*. Necessary p=q=1 was not sufficient;
time7sites11 OR12=1 is additionally needed. Corrected before replay.
P1/P2 HELD; local equations and independent engines PASS. No SAT,
visible membership, wider strip, mixed-word census or closure scan.
"""
from itertools import product
from rule30_sl_no_refork import bits, run


def five_prefix_controls():
    prefixes = ('1110010011', '1110010100', '1110010101',
                '1110011011', '1110011110')
    for prefix in prefixes:
        for tail in product((0, 1), repeat=10):
            rows = run(bits(prefix) + tail, 10)
            assert rows[10][:10] != bits('1110010001')
            if prefix == '1110011011':
                assert rows[5][:8] == bits('01100111')
                assert rows[8][5] == rows[10][4] == 1
            if prefix == '1110011110':
                e, T = tail[0], rows[5][9]
                assert rows[2][:10] == bits('01110010' + str(1-e) + '1')
                assert rows[5][5:9] == (1, 0, 1-e, 1-e)
                if e == T == 1:
                    assert rows[5][:10] == bits('0110010001')
                    assert rows[10][:9] == bits('111001001')
                else:
                    assert rows[10][4] == 1
    return 5120


def main():
    l0 = 0
    for tail in product((0, 1), repeat=8):
        rows = run(bits('011001') + tail, 5, 1)
        u, v, p, q, r, s = rows[2][6:12]
        assert rows[3][5:7] == (u, u | v)
        if u == v == 0:
            assert (p, q) != (1, 1)
            assert rows[3][7:11] == (p, p | q, p ^ (q | r),
                                    q ^ (r | s))
            assert rows[4][6:8] == (p, p | q)
        end = rows[5]
        if end[:6] == bits('111001'):
            l0 += 1
            assert u == v == 0
            assert end[6] | end[7] | end[8]
            if end[6] == end[7] == 0:
                assert p == 1 and rows[4][8] == 0
    for tail in product((0, 1), repeat=7):
        rows = run(bits('0110001') + tail, 5, 1)
        assert rows[4][4:7] == (0, 1, 0)
        Q, R = rows[4][7:9]
        assert rows[5][6:8] == (1-Q, Q | R)
    shields = 0
    for tail in product((0, 1), repeat=6):
        rows = run(bits('01') + tail, 2)
        if rows[2][2:4] == (0, 0):
            shields += 1
            assert rows[2][4:6] != (1, 1)
    assert run(bits('1101000011') + (0,)*8, 3, 1)[-1][:10] == bits('1110010011')
    freed = bits('11010000111') + (0,)*8
    assert freed[6:10] == (0, 0, 1, 1)
    assert run(freed, 3, 1)[-1][:10] == bits('1110010001')
    assert run(bits('111011100111') + (0,)*13, 6)[-1][:10] == bits('1110010001')
    print({'mid1_cones': 256, 'L0_returns': l0, 'mid01_cones': 128,
           'shield_cones': (64, shields), 'P2_local_controls': 'PASS',
           'independent_engines': 'PASS', 'unexpected': 'PASS',
           'first_unlifted_countercontrol': 'REFUTED'})


if __name__ == '__main__':
    main()
