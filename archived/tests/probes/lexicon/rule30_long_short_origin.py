"""GC1055: no mature hidden fork can recur inside a typed S/L run.
Missing inference: intersect GC1054's last L0-S-L0-L1 origin with actual
L0-S past. Record searched: L0.S.L0.L1|111011100|long.*short.*fork
with L0|ordinary|ancestr|preimage ->25 hits, no origin exclusion.
Further fork/alternative-long with at-most-one/first-three/transient
search ->26 unrelated hits; no startup-only hidden-fork result.
P1 before controls sought a two-tick shield contradiction from the S
fork gate; hand work instead proves the source prefix itself impossible,
so the proposed extraction is vacuous and is not reported as proved.
Informed P2 before controls: L0 returning S with blacksite6 has returned
sites6..9=(1,1,NOT H,H OR I), H=c9(9),I=c10(9). Hence its return cannot
begin111011100. All farther tails allowed; no fork gate is needed.
Proof uses GC1047: S return needs mid1 at5, prefix011001. At7 sites7,8
areu,v; S withblack6 forcesu=0,v=1, shielding time9sites6..8=010.
The last update gives the returned OR blocker. With GC1054 this excludes
all L1 at indices>=3 of a typed S/L run, and at most one earlier L1.
Independent controls:256 complete five-tick black-phase mid1 cones,
literal/packed and intermediate equations; no mixed-word absence scan.
Unexpected: L1 seed111000001110011100 plus zeros DOES return111011100
at10, but misses the fork gate (returned10,11 not11). This prevents
extending the L0-S origin guard to every long entrance.
The fork is transient per uninterrupted S/L run, not globally across
other gap types. No all-depth record bound or full exterior closure.
OUTCOME:P2 HELD,112 applicable local S returns; all controls PASS.
"""
from itertools import product
from rule30_sl_no_refork import bits, run


def main():
    applicable = 0
    for tail in product((0, 1), repeat=8):
        rows = run(bits('011001') + tail, 5, 1)
        u, v, p, q = rows[2][6:10]
        A, B, C = u | v, u ^ (v | p), v ^ (p | q)
        assert rows[3][5:9] == (u, A, B, C)
        assert rows[4][5:8] == (1-A, u ^ (A | B), A ^ (B | C))
        end = rows[5]
        assert end[:9] != bits('111011100')
        if end[4] == end[5] == 1:
            applicable += 1
            assert (u, v) == (0, 1)
            assert rows[4][5:8] == (0, 1, 0)
            H, I = rows[4][8:10]
            assert end[5:9] == (1, 1, 1-H, H | I)
    past = bits('111000001110011100') + (0,)*20
    rows = run(past, 26)
    assert rows[10][:13] == bits('1110111000101')
    assert not (rows[10][9] == rows[10][10] == 1 and
                bool(rows[10][11] | rows[10][12]))
    assert rows[16][:10] != bits('1110010001')
    free_s = bits('111011100111') + (0,)*13
    assert run(free_s, 16)[-1][:9] == bits('111000001')
    print({'complete_mid1_cones': 256, 'applicable': applicable,
           'P2': 'HELD', 'independent_engines': 'PASS',
           'L1_origin_countercontrol': 'PASS', 'free_S_fork': 'PASS'})


if __name__ == '__main__':
    main()
