"""GC1054: a mature hidden fork has an L0-S-L0-L1 past.
Missing inference: which surviving S ancestry can prepare a hidden fork
now that GC1053 bars L0-L0-L1? Record searched: S.S.L0.L1|S.S.L1|
short.*short|111010001|111011100 with fork|ancestr|preimage|successor|
gate ->40 hits; read GC629/689 and GC1014, reuse GC1051/1052/1053.
P1 before controls proposed a nonempty S-image characterization of
111011100; hand work instead proves that image prefix impossible, so
P1 is vacuous, not a nonempty predecessor classification.
Informed P2 before controls: S returning S with blacksite6 has
returned7=1 and returned8 OR9=1, hence cannot begin111011100.
P3 before controls: initial111010001 returns with sites7..9=
(0,NOT C,C OR E), C=c10(4),E=c11(4), hence misses the fork prefix.
This output shield is new evidence from GC1053; it does not repair
GC1052's failed complete fork formula. Its formerly wrong time4site6
is retained correctly as1. All farther tails allowed in both lemmas.
Combining with the three mature S-to-L0 branches, GC1052 and GC1050,
only111011100 can prepare L1. S images cannot start it; an L1-S past
is barred by GC1051. Thus every interior fork needs L0-S-L0-L1.
Independent controls:1024 complete S cones,128 complete first-branch
cones, literal/packed plus intermediate equations. No mixed-word scan,
solver, strip sweep or all-depth record bound.
Unexpected: retained1110100010000100 returns1110010101, and relaxed
1110111001110... still forks. Startup111010010 feeds L0 but lacks a
white/black past; keep maturity and initial/terminal exemptions.
OUTCOME: P2/P3 HELD,96 black-sixth S returns; all local controls PASS.
"""
from itertools import product
from rule30_sl_no_refork import bits, run


def main():
    black_sixth = 0
    for tail in product((0, 1), repeat=10):
        rows = run(bits('11101') + tail, 6)
        end = rows[6]
        assert end[:9] != bits('111011100')
        if end[4] == end[5] == 1:
            black_sixth += 1
            assert rows[2][5:8] == (1, 0, 1)
            assert rows[3][5:8] == (0, 0, 1)
            assert rows[4][5:8] == (0, 1, 1)
            assert rows[5][5:8] == (0, 1, 0)
            F, G = rows[5][8:10]
            assert end[5:9] == (1, 1, 1-F, F | G)
    for tail in product((0, 1), repeat=7):
        rows = run(bits('111010001') + tail, 6)
        assert rows[2][:9] == bits('010110010')
        U, V = rows[2][9:11]
        assert rows[3][5:10] == (1, 1, 1, 1-U, U | V)
        assert rows[4][:9] == bits('000101000')
        C, E = rows[4][9:11]
        assert rows[5][5:10] == (1, 1, 0, C, C | E)
        assert rows[6][:6] == bits('111001')
        assert rows[6][6:9] == (0, 1-C, C | E)
    old_failure = bits('1110100010000100') + (0,)*9
    assert run(old_failure, 6)[-1][:10] == bits('1110010101')
    free_birth = bits('111011100111') + (0,)*13
    assert run(free_birth, 6)[-1][:10] == bits('1110010001')
    assert run(free_birth, 16)[-1][:9] == bits('111000001')
    startup = bits('111010010') + (0,)*7
    assert run(startup, 6)[-1][:6] == bits('111001')
    a, b, c, d = startup[5:9]
    assert a == b == 0 and c > d
    print({'S_cones': 1024, 'black_sixth': black_sixth,
           'first_branch_cones': 128, 'P2_P3': 'HELD',
           'independent_engines': 'PASS', 'unexpected': 'PASS',
           'P1': 'VACUOUS; not a nonempty classification'})


if __name__ == '__main__':
    main()
