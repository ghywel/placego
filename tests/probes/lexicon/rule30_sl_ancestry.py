"""GC1049: an entrance-sensitive successor clause, with failed closure tests.
Missing inference: can GC1048's L1-S-L0 branch forbid an immediate new
L1 and thus close a small typed transition relation?
Record searched: LLSLL|L1SL0L1|alternative.*short.*long with
forbid|absen|return|gate ->4 prior, unrelated hits;
111011100110|000111001 with ancestor|prehistory|image|successor ->0.
Predictions were registered before each check in the work-block log:
P1: S111011100 cannot reach next L0's mid00. REFUTED:228/512.
P2, informed: this S cylinder cannot refork into L1. REFUTED by a
complete cone; it does not claim that cone has L1 prehistory.
P3, informed: an actual L1-S-L0-L1 occurs among1024 deterministic
random site35 cones. Sample prediction REFUTED; actual existence UNKNOWN. There are
147 L1-S-L0 cases,94 with next mid00, so the sample is nonvacuous.
P4: the seven-bit return1110000 requires initialsites10..12=110.
REFUTED by the retained111 case. P5, informed full-gate repair: the
nine-bit L1 return requires110. REFUTED by the same longer cone.
Both shortcut targets are stopped; no additional scan proposed.
Hand result: on the actual L1-S-L0 branch the S entrance cannot
have110 atsites10..12; the preceding two-tick row is000111001.
Control:32 complete two-tick cones, literal versus packed.
Unexpected check: the111-tail refork passes this clause, so this
one clause does not forbid all relaxed reforks. No actual absence,
solver result, finite closure or all-depth bound inferred.
OUTCOME: clause controls PASS; shortcut predictions retained as above.
"""
from itertools import product
from random import Random
from collections import Counter
from rule30_sl_collar import literal, packed


def main():
    for tail in product((0, 1), repeat=5):
        start=tuple(map(int, "000111001"))+tail
        r=literal(start,2)
        assert r==packed(start,2)
        assert r[1][8]==1
        assert r[2][9:12]!=(1,1,0)
    cases=(
        ("111011100100000000",11,(0,0)),
        ("1110111001101000000000000",16,"111000001"),
        ("11101110011100000000000",16,"1110000"),
        ("1110111001110000000000000",16,"111000001"),
    )
    for start,t,expected in cases:
        r=literal(tuple(map(int,start)),t)
        assert r==packed(tuple(map(int,start)),t)
        if isinstance(expected,tuple):assert r[t][5:7]==expected
        else:assert "".join(map(str,r[t][:len(expected)]))==expected
    rng=Random(1049); counts=Counter(); reforks=0; l0=mid00=0
    for _ in range(1024):
        start=tuple(map(int,"111000001"))+tuple(rng.randrange(2) for _ in range(26))
        r=packed(start,26);assert r==literal(start,26)
        if r[16][4]==0:
            assert r[10][:9]==tuple(map(int,"111011100"))
            assert r[10][9:12]!=(1,1,0)
            l0+=1;mid00+=r[21][5:7]==(0,0)
            counts["".join(map(str,r[26][:9]))]+=1
            reforks+=r[26][:9]==tuple(map(int,"111000001"))
    assert l0==147 and mid00==94 and reforks==0
    print({"clause_cones":32,"countercontrols":4,"sample_L1SL0":l0,
           "sample_mid00":mid00,"sample_reforks":reforks,
           "refork_existence":"UNKNOWN","literal_packed":"PASS"})


if __name__=="__main__":main()
