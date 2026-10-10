"""GC1074: transport the high ordinary-long selector through a mature short.
Missing inference: GC1073's sites 7,9 high-LL pins are not independent.
Give the exact S-origin relation producing the high fifth long track.
Record searched: 111010011|1110011 with high.*LL|0101101010|ninth.*pin|
selector|sixth.*track ->7 hits in 5 files; GC1052 supplies the returned
pair, GC1054/1056 the mature SL branches; no ninth-selector formula.
P1 before controls: from initial11101001100, write f,g,h,i at 12..15.
Returned site 9 at 6 is G=(f OR g) OR NOT(h OR i). Returned7,8=10.
P2: the following L0 fifth track is 0101101010 iff G=1, otherwise
0101100000, for every farther tail. This selects a track, not its
following S/L0 gap. The mature SL high track can occur only on this
branch: A has returned7=0; B with initial 10 OR 11=1 has returned7=0.
Counterfactual: initial12 OR13 alone determines the next high track.
Unexpected check f=g=h=i=0 is high despite its two white first pins;
f=g=0 with h OR i=1 is low. The complementary final pair matters.
Controls: 16 exact gate assignments, two farther patterns, literal and
packed updates, and the intermediate symbolic shielding identities.
No solver, cut extraction, mixed-word or relaxed-record census.
OUTCOME: 32 gate controls PASS,26 high and 6 low tracks; literal/packed
and all intermediate identities agree. The all-white first pair gives
both high and low according to the last pair, refuting the counterfactual.
"""
from itertools import product
from rule30_sl_no_refork import bits,run


def main():
    count=high=0
    for f,g,h,i in product((0,1),repeat=4):
      G=(f|g)|(1-(h|i))
      for far in (0,1):
        rows=run(bits('11101001100')+(f,g,h,i)+(far,)*20,16)
        A=1-(f|g)
        B=(1-f)&(g|h)
        C=(f|g)^((f^(g|h))|(g^(h|i)))
        D=1-(A|B)
        E=A^(B|C)
        assert rows[2][10:13]==(A,B,C)
        assert rows[3][10:12]==(D,E)
        assert rows[4][8:11]==(1,0,1-(D|E))
        assert rows[5][7:10]==(0,0,D|E)
        assert rows[6][6:9]==(1,0,G)
        assert D|E==G
        assert rows[6][:6]==bits('111001')
        fifth=tuple(r[4] for r in rows[6:16])
        assert fifth==bits('0101101010' if G else '0101100000')
        assert rows[9][5]==rows[11][5]==G
        count+=1;high+=G
    assert count==32 and high==26
    print({'gate_controls':count,'high_tracks':high,'low_tracks':count-high,
           'literal_packed':'PASS','intermediate_formula':'PASS',
           'white_first_pair_positive':'PASS'})


if __name__=='__main__': main()
