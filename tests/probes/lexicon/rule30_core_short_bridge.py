"""GC1083: a core's 101-S-A escape returns the exceptional low001.
Missing inference: carry GC1082's finite long-run counter across S.
Record searched:111001101 with111010001|mixed|next short ->3 hits,
2 files; GC1052/1075 leave this bridge. CL254 confirms GC1082.
P1 BEFORE controls: high101 returns S-A=111010001 iff time4sites9..12
are0011 and13 OR14=1; returned site10=1. The0011 antecedent alone
is equivalent to initial sites10..14=11100 or1101*.
P2: on actual C-to101 past, the11100 option is barred. A forces
core time8sites10..15=000001 and returned101site14=1. The latter
origin11100110111011 forces S prefix1110100011a1, hence A-toL001.
P3: unrestricted11100110111010000000 plus zeros returns A then001.
HELD, but initial101site14=0 excludes its C past; no mixed core
counterexample is asserted. P4: one of010-zero,100-period110 or
011-period110 core sources gives the proposed A bridge. REFUTED:
all remain in C at10; two reach101 at20 with initial11=0.
Counterfactual: knowing a101 escape alone bars low001 across S.
The unrestricted25-bit all-tail cylinder refutes that shortcut; actual
core ancestry needs the separate sparse guard, not a fresh101 tail.
Unexpected: returned A-site10 was first misindexed as white; it is
black. A19-cell control cone cannot read site10 at10 (IndexError);
use20 cells. Both failures retained before correcting controls.
Independent controls: scalar local implications with free exterior,
then literal versus packed complete cones. No solver, membership,
CUT or record run. A core-origin preimage of the joint packet is open.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_high_101_shield import FIFTH as H

D=bits('0101100000')
S=bits('111000')
CORE={bits(w) for w in ('010','011','100')}
WITNESS='1110011011101000000000000'


def update(row):
    return tuple(row[k-1]^(row[k]|row[k+1]) for k in range(1,len(row)-1))


def propagate(old,track):
    rows=[old]
    for left in track:
        rows.append(update((left,)+rows[-1]))
    return rows


def main():
    cones=positives=0
    for far in product((0,1),repeat=11):
        rows=run(bits('111001101')+far,10)
        gate=(rows[4][8:12]==bits('0011') and
              bool(rows[4][12]|rows[4][13]))
        is_a=rows[10][:9]==bits('111010001')
        assert bool(gate)==is_a
        pre=(far[:5]==bits('11100') or far[:4]==bits('1101'))
        assert (rows[4][8:12]==bits('0011'))==pre
        if is_a:
            assert rows[10][9]==1
            positives+=1
        cones+=1
    # Scalar core-closing relations at time8, sites6 onward1111.
    core=joint=0
    for tail in product((0,1),repeat=7):
        rows=propagate(bits('1111')+tail,D[8:])
        out=rows[2]
        is_101=out[1:4]==bits('101')
        assert is_101==(tail[:2]==(0,0))
        if is_101:
            assert out[4]==1
            if out[5]:
                assert out[6]<=out[7]
                pre=(out[4:8]==bits('1101'))
                assert pre==(tail[:6]==bits('000001'))
                if pre:
                    assert out[8]==1
                    joint+=1
            core+=1
    # Two-step inherited packet, plus the high shield; arbitrary new bits.
    packet=0
    for far in product((0,1),repeat=10):
        rows=propagate(bits('1111000001')+far,D[8:]+H)
        assert rows[2][:9]==bits('110111011')
        assert rows[12][:7] in (bits('0001101'),bits('0001111'))
        packet+=1
    # All-tail hand chain: each missing exterior is fresh, not zero.
    implications=0
    shields={0:'110111011',1:'100100010',2:'01111011',3:'11000010',
             5:'11111100',6:'1000001',7:'0100011',8:'1110110'}
    for t in (0,1,2,5,6,7):
        old=bits(shields[t]); new=bits(shields[t+1])
        needed=len(new)+1-len(old)
        for far in product((0,1),repeat=max(0,needed)):
            assert update((H[t],)+old+far)[:len(new)]==new
            implications+=1
    for a,b in product((0,1),repeat=2):
        row4=update((H[3],)+bits(shields[3])+(a,b))
        assert row4==bits('0010011')+(1-a,a|b)
        assert update((H[4],)+row4)[:8]==bits(shields[5])
        row9=update((H[8],)+bits(shields[8])+(a,b))
        assert row9==bits('000010')+(1-a,a|b)
        assert update((H[9],)+row9)[:7]==bits('00011')+(a,1)
        implications+=4
    # The high packet and the next S return, independent full engines.
    high=0
    for far in product((0,1),repeat=7):
        rows=run(bits('11100110111011')+far+(0,)*18,16)
        assert rows[10][:10]==bits('1110100011')
        assert rows[10][11]==1
        assert rows[16][:9]==bits('111001001')
        assert tuple(r[4] for r in rows[:10])==H
        assert tuple(r[4] for r in rows[10:16])==S
        high+=1
    # Independent short gate; site10=1 is essential to its equation.
    short=0
    for far in product((0,1),repeat=8):
        rows=run(bits('1110100011')+far,6)
        assert rows[4][9]==(far[0]|far[1])
        short+=1
    # The unrestricted source has no core past of the specified kind.
    witness=0
    for far in product((0,1),repeat=6):
        rows=run(bits(WITNESS)+far,16)
        assert rows[10][:9]==bits('111010001')
        assert rows[16][:9]==bits('111001001')
        assert rows[0][13]==0
        witness+=1
    for tri,far in [('010','0'*39),('100','110'*13),('011','110'*13)]:
        rows=run(bits('111001'+tri+far),26)
        assert rows[10][6:9] in CORE
        if rows[20][6:9]==bits('101'):
            assert rows[20][10]==0
    print(dict(high_101_cones=cones,A=positives,core_closing=core,
               joint_packets=joint,packet_controls=packet,
               high_packet=high,local_implications=implications,
               short_gate=short,witness=witness,
               literal_packed='PASS',core_A_existence='OPEN',
               P4='REFUTED; retained',all_depth_bound='OPEN'))


if __name__=='__main__': main()

# OUTCOME: all local implications and both full engines PASS. Core A
# preimage remains OPEN; P4 and the indexing/cone failures stay retained.
