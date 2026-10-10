"""GC1050: complete L0 -> L1 gate, by hand rather than a closure sweep.
Missing inference: GC619 gives one sufficient switch cylinder, but a
complete entrance condition is needed for typed relation composition.
Record searched:1110010001 with complete|necessary|MUX|selector|gate|
thirteen ->9 hits: GC614/618/619 and GC1047, no complete switch gate.
New hand evidence: GC1047's complemented mid-pair transports its first
bit to returnedsite7. Trace that bit backwards, then reuse GC618/619.
Predictions registered before controls:
P1: initial111001 returns11100000 iff it initially begins1110010001.
P2: under that ten-bit prefix, returnedsite9 is
    (NOT f AND g) OR (NOT g AND NOT h), f,g,h=initialsites11,12,13.
Thus exactly four thirteen-bit cylinders feed L1, for every farther tail.
Independent controls: literal versus packed;512 complete cones for the
fixed-prefix mux;256 varied-prefix farther-tail extremes for necessity.
Unexpected positive:1110010001100 is outside GC619's old cylinder.
Unexpected negative:1110010001110 has white thirteenth bit but fails;
GC619's single-bit rule must not be extended after forgetting its prefix.
No visible membership solver, larger strip or record scan. Hand proof
supplies all-tail necessity; varied-prefix extremes are controls only.
OUTCOME: P1/P2 HELD;512 complete mux cones and256 varied-prefix
extremes agree with independent engines; both unexpected controls PASS.
"""
from itertools import product
from rule30_sl_collar import literal, packed


def gate(row):
    f,g,h=row[10:13]
    return row[:10]==tuple(map(int,"1110010001")) and ((1-f)&g or (1-g)&(1-h))


def check(start):
    r=literal(start,10);assert r==packed(start,10)
    first8=r[10][:8]==tuple(map(int,"11100000"))
    assert first8==(start[:10]==tuple(map(int,"1110010001")))
    assert (r[10][:9]==tuple(map(int,"111000001")))==bool(gate(start))
    return r


def main():
    present=set();total=0
    for tail in product((0,1),repeat=9):
        start=tuple(map(int,"1110010001"))+tail;r=check(start)
        f,g,h=start[10:13]
        assert r[10][8]==((1-f)&g | (1-g)&(1-h))
        if r[10][8]:present.add("".join(map(str,start[:13])))
        total+=1
    assert present=={"1110010001000","1110010001100",
                     "1110010001010","1110010001011"}
    for bits in product((0,1),repeat=7):
        for far in (0,1):check(tuple(map(int,"111001"))+bits+(far,)*6)
    pos=check(tuple(map(int,"1110010001100"))+(0,)*6)
    neg=check(tuple(map(int,"1110010001110"))+(0,)*6)
    assert pos[10][8]==1 and neg[10][8]==0
    print({"complete_mux_cones":total,"prefix_extremes":256,
           "L1_cylinders":sorted(present),"P1_P2":"HELD",
           "literal_packed":"PASS","unexpected":"PASS"})


if __name__=="__main__":main()
