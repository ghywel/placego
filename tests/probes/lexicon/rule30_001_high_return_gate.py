"""GC1080: exact origin gate for001-to-D-to-high-LL.
Missing inference: decide the third-high return jointly with the
preceding001 low origin, then intersect with actual high b=0 past.
Record searched:001.*111|111.*001|H.D.H with inherit|third|repeat|
marker|return and ordinary|high|renew ->50 hits in16 files;
00100001|00110000|001011 with high|HLL|ordinary and
gate|origin|inherit ->5 hits in3 files, unrelated old31 template
and GC1079; no existing exact001-to-high-return gate.
P1 BEFORE controls: ordinary001 origin has D, returned111 and
following high LL exactly for these initial sites10..19 cylinders:
A:00100001**; B:00110000ij with i OR j=1;
C:001011ghij with g OR h=1 and (g,h)!=(1,1) or i=j=0.
In C the OR condition is required also when i=j=0.
Equivalent local gate, conditional on001 D returning111:
time3sites6..14=000000011; next high LL iff sites15,16 both0.
P2 corrected hand scope: actual earlier high b=0 returns001 with
initial10=11. Its D continuation requires that pair00, and THEN
12<=13. The unconditioned second guard was withdrawn after its
derivation was found to use pair00;64 samples had not caught this.
Under the D premise A/C are excluded; only B can renew high LL.
This identifies a concrete remaining inherited cylinder, not its
absence and not an all-depth bound.
P3 unexpected check: ordinary origin11100100100100001 really
gives D then high LL for EVERY farther tail, violating inherited
12<=13. So banning high LL after001 D without past is false.
Counterfactual: every001 D high successor returns S.
Controls:48 qualified local time1 bands;56 actual origin controls,
32 positives and24 negatives;64 selected earlier-high controls
for the inherited pair guards and composed gate, independent
literal and packed engines. No solver or language census.
P4 before additional controls:128 controlled high-b0 bands carry
the equal pair.32 with time5sites12,13=00 select D and satisfy
the conditional12<=13;96 others select X. GC1079's two known
21-bit controls give nonvacuous composed D-to111 cases, both S.
P5 before decoder controls:32 selected111001111100 origins with
d,e,f,g varied give high LL exactly when d=site13 is0, and
time5site10=NOT d. This checks the high closing sublemma directly.
OUTCOME:48 qualified local bands,32 high decoder controls,128 inherited pair controls,
56 actual origins (32 high LL,24 high S),64 earlier-high controls
and2 nonvacuous composed cases PASS. All literal/packed controls
agree. Unrestricted001 really gives D-high-LL on the predicted
cylinder; its conditional inherited pair guard is violated.
The unconditional inequality was withdrawn, not established by
the64 samples; all published uses retain the D premise.
"""
from itertools import product
from rule30_sl_no_refork import bits, run

D = bits('0101100000')
H = bits('0101101010')


def update(row):
    return tuple(row[k-1] ^ (row[k] | row[k+1])
                 for k in range(1, len(row)-1))


def band(row, start, end, track):
    rows = {start: row}
    for t in range(start, end):
        rows[t+1] = update((track[t],) + rows[t])
    return rows


def gate(tail):
    a, b, c, d, e, f, g, h, i, j = tail
    A = tail[:8] == bits('00100001')
    B = tail[:8] == bits('00110000') and bool(i | j)
    C = (tail[:6] == bits('001011') and bool(g | h)
         and ((g, h) != (1, 1) or (i, j) == (0, 0)))
    return A or B or C


def main():
    local = actual = inherited = qualifying = guard_D = guard_X = decoder = 0
    track = D + H
    for d, e, f in ((1, 0, 0), (0, 1, 0), (0, 1, 1)):
        for g, h, i in product((0, 1), repeat=3):
            for far in (0, 1):
                rows = band(bits('1111111') + (d, e, f, g, h, i)
                            + (far,)*24, 1, 20, track)
                assert rows[3][:9] == bits('000000011')
                v, w = rows[3][9:11]
                U = e ^ (f | g)
                V = f ^ (g | h)
                W = g ^ (h | i)
                assert (v, w) == (1-(U | V), U ^ (V | W))
                assert rows[5][:8] == bits('01000110')
                a = rows[5][8]
                assert a == v | w
                assert rows[10][:7] == bits('11111') + (a, a)
                if a == 0:
                    assert rows[5][9] == 1
                    assert rows[10][7] == 0
                assert (rows[17][1:3] == (0, 0)) == (v == w == 0)
                local += 1
    for tail in product((0, 1), repeat=4):
        for far in (0, 1):
            rows = run(bits('111001111100') + tail + (far,)*22, 10)
            assert tuple(r[4] for r in rows[:10]) == H
            assert rows[5][7:9] == (0, 0)
            assert rows[5][9] == 1-tail[0]
            assert (rows[10][:6] == bits('111001')) == (tail[0] == 0)
            decoder += 1
    for e, f in product((0, 1), repeat=2):
        for tail in product((0, 1), repeat=4):
            for far in (0, 1):
                rows = band(bits('100011') + (e, f) + tail + (far,)*24,
                            5, 15, H + D)
                assert rows[10][:4] == bits('1001')
                assert rows[10][4:6] == (e | f, e | f)
                if e | f:
                    assert rows[15][:2] == bits('00')
                    guard_X += 1
                else:
                    assert rows[15][:2] == bits('01')
                    assert rows[10][6] <= rows[10][7]
                    guard_D += 1
    tails = set()
    for ij in product((0, 1), repeat=2):
        tails.add(bits('00100001') + ij)
        tails.add(bits('00100000') + ij)
        tails.add(bits('00110000') + ij)
        for gh in product((0, 1), repeat=2):
            tails.add(bits('001011') + gh + ij)
    positives = negatives = 0
    for tail in sorted(tails):
        for far in (0, 1):
            rows = run(bits('111001001') + tail + (far,)*30, 20)
            assert tuple(r[4] for r in rows[:20]) == track
            assert rows[10][:9] == bits('111001111')
            assert rows[3][5:14] == bits('000000011')
            expected = gate(tail)
            assert (rows[20][:6] == bits('111001')) == expected
            assert (rows[3][14:16] == (0, 0)) == expected
            if expected:
                positives += 1
            else:
                assert rows[20][4] == 1
                negatives += 1
            actual += 1
    for prefix in ('11100111101', '111001111100'):
        for tail in product((0, 1), repeat=4):
            for far in (0, 1):
                rows = run(bits(prefix) + tail + (far,)*36, 30)
                assert tuple(r[4] for r in rows[:10]) == H
                if rows[10][:6] == bits('111001'):
                    assert rows[5][8] == 0
                    assert rows[10][6:9] == bits('001')
                    assert rows[10][9] == rows[10][10]
                    next_track = tuple(r[4] for r in rows[10:20])
                    if next_track == D:
                        assert rows[10][9:11] == (0, 0)
                        assert rows[10][11] <= rows[10][12]
                    if next_track == D and rows[20][6:9] == bits('111'):
                        origin_tail = rows[10][9:19]
                        remaining = (origin_tail[:8] == bits('00110000')
                                     and bool(origin_tail[8] | origin_tail[9]))
                        assert gate(origin_tail) == remaining
                        assert (rows[30][:6] == bits('111001')) == remaining
                        qualifying += 1
                inherited += 1
    for far in (0, 1):
        rows = run(bits('111001111011111110010') + (far,)*36, 30)
        assert rows[10][6:9] == bits('001')
        assert tuple(r[4] for r in rows[10:20]) == D
        assert rows[20][6:9] == bits('111')
        origin_tail = rows[10][9:19]
        assert not gate(origin_tail)
        assert rows[30][4] == 1
        qualifying += 1
    unexpected = run(bits('11100100100100001') + (0,)*35, 20)
    assert unexpected[10][:9] == bits('111001111')
    assert unexpected[20][:6] == bits('111001')
    assert unexpected[0][11] == 1 and unexpected[0][12] == 0
    assert (local, actual, positives, negatives, inherited) == (48, 56, 32, 24, 64)
    assert (guard_D, guard_X, qualifying) == (32, 96, 2)
    assert decoder == 32
    print({'local_qualified_bands': local, 'selected_actual': actual,
           'high_LL': positives, 'high_S': negatives,
           'inherited_controls': inherited, 'composed_cases': qualifying,
           'conditional_D_guards': guard_D, 'X_guards': guard_X,
           'high_return_decoder': decoder,
           'unexpected_actual_D_HLL': 'PASS', 'literal_packed': 'PASS'})


if __name__ == '__main__':
    main()
