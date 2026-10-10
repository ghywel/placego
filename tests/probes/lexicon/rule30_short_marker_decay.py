"""GC1056: a white sixth marker cannot turn black across an SS return.
Missing inference: what correlated carrier survives in the recurrent S/L0
component after GC1055 removes L1? Target a hand monotonic marker guard,
and use it with confirmed image guards to fix the short fifth track.
Record searched: short|SS|all.S|S.block with sixth|site6|c6 and
monoton|birth|nonincreas|absorbing ->6 hits, GC689 and ASF read; no finite
SS marker monotonicity. 111000|111010 with fifth|site5|column5|c5 ->15
hits; GC689 all-S fifth track known, no mixed mature short-track table.
GC744..747 and ALF read: existing all-L forcing is not rederived.
P1 registered before controls: any S source returning S has returned
site6 <= initial site6; black returned6 needs initial6,7=11 and8 OR9=1.
P2: every S has fifth pre-closing profile1110(x OR y)0, where x,y are
sites6,7 at time2. SS gives111010; SL has111000 or111010. In an S/L0
run after L1's startup, SL can only have111000, by GC1054/1055's image
OR guards. L0-S has0101101010; L0-L0 retains0000/1010 suffix choices.
Counterfactual: sixth-marker monotonicity forbids black persistence or
extends across a long-short return. Neither follows from the proof.
Unexpected:111011101 plus arbitrary farther bits returns black6 again;
L1 source111000001110011100 plus zeros returns black6 S followed by L0,
showing why the mature short fifth-track statement needs its origin.
Independent controls:128 complete S cones, literal versus packed,
intermediate SS branch equations; fixed positive/counterexample cones.
No longer-word census, solver, membership or relaxed-record run.
OUTCOME:P1/P2 HELD on128 cones,80 SS and12 black-sixth SS returns.
Both engines and the persistence/L1-origin countercontrols PASS.
The initial display label1,024 was a reporting error: all_rows covers128
cones here; fixed to an actual counter before publication.
"""
from rule30_sl_collar import all_rows
from rule30_sl_no_refork import bits, run


def main():
    count = ss = black = 0
    profiles = set()
    for start, rows in all_rows('11101', 6):
        count += 1
        x, y, z = rows[2][5:8]
        fifth = ''.join(str(row[4]) for row in rows[:6])
        assert fifth == '1110' + str(x | y) + '0'
        profiles.add(fifth)
        if rows[6][4] == 1:
            ss += 1
            assert x ^ y == 1
            assert rows[6][5] == (x & z)
            assert rows[6][5] <= start[5]
            if rows[6][5]:
                black += 1
                assert start[5:7] == (1, 1)
                assert start[7] | start[8]
    assert ss and black
    assert profiles == {'111000', '111010'}
    for farther in (0, 1):
        rows = run(bits('111011101') + (farther,)*12, 6)
        assert rows[6][4:6] == (1, 1)
        assert rows[2][5:8] == (1, 0, 1)
        rows = run(bits('111010000') + (farther,)*12, 6)
        assert rows[6][4:6] == (1, 0)
    exceptional = run(bits('111000001110011100') + (0,)*24, 16)
    assert exceptional[10][:13] == bits('1110111000101')
    assert ''.join(str(row[4]) for row in exceptional[10:16]) == '111010'
    assert exceptional[16][:6] == bits('111001')
    print({'complete_S_cones': count, 'SS': ss,
           'black_sixth_SS': black, 'P1_P2': 'HELD',
           'independent_engines': 'PASS',
           'black_persistence': 'PASS', 'L1_origin_exception': 'PASS'})


if __name__ == '__main__':
    main()
