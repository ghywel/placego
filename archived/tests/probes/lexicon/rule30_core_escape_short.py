"""GC1084: actual C-to101 escape cannot return short A.
Missing inference: CL255's finite absence needs a structural transport
lemma. Record searched:1110100011|111010001 with00110000|00100001|
001011|high.LL ->9 hits,5 files. Initial short-B gate work parked after
CL255 reports the core-A premise empty; its x=0 exclusion was false,
with actual11101000110110111000001 resetting through B. A19-bit
preimage proposal also missed a branch. These failures do not dispute
CL255.1. The attempted contiguous core shield lost a sparse output;
a guessed nine-cell intermediate packet failed, corrected to seven.
P before controls: at core time4, returned101site11=1 forces either
sites9..14=000001 or9..13=10001. First case gives time6sites9..14=
100110; a white pair at time8sites12/13 forces site14 black.
Second case, retaining the time1prefix101, forces time1sites9..15=
0010001, then time3sites9..15=0000010. Its next pair is complementary:
time4sites14..16=(1,NOT H,H OR I). That fixes time5sites14,15=00,
time6site14=1, time7sites13,14=01, and time8site14=1.
Thus on core101 withsite11=1, sites12,13 are11. The short-A antecedent
requires101sites10..14=11100 or1101*, incompatible. In a continuing
mature SL history, its S return is B. Subsequent SS compatibility open.
Counterfactual: a fresh101 tail can return A; GC1083's unrestricted
25-bit cylinder does so, but this core ancestry bars its joint packet.
Independent controls: four finite local lemmas with fresh exterior,
then selected actual cones, literal against packed. The hand two-case
elimination is the proof; no membership, solver or record run.
Unexpected: the constructed core10011111100 zero-tail cone puts its
black time8 bit at14 rather than15 and returns B, explaining its failure.
"""
from itertools import product
from rule30_sl_no_refork import bits,run
from rule30_low_core_closure import D,update


def propagate(row,track):
    rows=[row]
    for left in track: rows.append(update((left,)+rows[-1]))
    return rows


def main():
    split=back=first=second=0; qualified=0
    # Independent split at4; tail is sites9..18, never a fixed exterior.
    for tail in product((0,1),repeat=10):
        rows=propagate(bits('010')+tail,D[4:8])
        if rows[2][3]==1 and rows[4][4:8]==(0,0,0,0):
            assert tail[:6]==bits('000001') or tail[:5]==bits('10001')
            qualified+=1
        split+=1
    assert qualified
    # Backward chain uses actual core prefix at1, not a fresh time4 row.
    for tail in product((0,1),repeat=9):
        rows=propagate(bits('101')+tail,D[1:4])
        if rows[3][3:8]==bits('10001'):
            assert tail[:7]==bits('0010001')
            assert rows[2][3:10]==bits('0000010')
        back+=1
    # First time4 branch masks two extra right bits through time6.
    for far in product((0,1),repeat=4):
        rows=propagate(bits('010000001')+far,D[4:8])
        assert rows[2][:9]==bits('110100110')
        if rows[4][6:8]==(0,0): assert rows[4][8]==1
        first+=1
    # Second branch's complementary OR packet, with unrelated farther bits.
    for H,I in product((0,1),repeat=2):
        for far in product((0,1),repeat=4):
            row=bits('01010001')+(1,1-H,H|I)+far
            rows=propagate(row,D[4:8])
            assert rows[1][8:10]==(0,0)
            assert rows[2][8]==1
            assert rows[3][7:9]==(0,1)
            assert rows[4][6:9]==(0,0,1)
            second+=1
    # Nonvacuous actual core escapes, including both time4 branches.
    origins=('1110010100010001','1110010111000001',
             '1110010110111100','111001011011101',
             '11100110011111100','1110011001111101')
    actual=0
    for origin in origins:
        for tail in product((0,1),repeat=5):
            for far in (0,1):
                rows=run(bits(origin)+tail+(far,)*26,20)
                assert rows[10][:14]==bits('11100110111110')
                assert rows[20][:9]==bits('111010011')
                actual+=1
    bad=run(bits('11100110011111100')+(0,)*30,20)
    assert bad[8][5:15]==bits('1111000010')
    assert bad[20][:9]==bits('111010011')
    print(dict(split_controls=split,qualified=qualified,backward_controls=back,
               first_packet=first,second_packet=second,actual_cones=actual,
               literal_packed='PASS',core_A='BARRED BY HAND',
               later_SS='OPEN',all_depth_bound='OPEN'))


if __name__=='__main__':main()
