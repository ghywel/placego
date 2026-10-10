"""GC1073: a preceding ordinary long return pins the high LL selector.
Missing inference: can the mature LL fifth selector treat its farther
origin bits as independent? Prove an actual past gate on the high track.
Record searched: 0101100000|LL.*selector|long.*selector with successor|
transport|alternat|consecutive|reset ->10 hits in5 files; CL219 already
reported absence of returned seventh/ninth triple110 computationally.
GC1053 proves the other triple blocker000; the110 hand consequence and
its high-selector ninth-site pin were not established there.
P1 before controls: every L0 return into L0 has sites7..9 !=110.
GC1047's mid01 and mid1 branches reduce this to the two local updates
tested below. No renewed long-cone exhaustion of CL219.
P2: high fifth LL track0101101010 requires initial site7 black and
sites8 OR9=1. With an L0 predecessor, P1 therefore forces site9=1.
Counterfactual: the ninth-site pin holds without the preceding L0.
Unexpected check: initial1110011100 plus selected farther extremes
has forbidden-past triple110 but might still give a valid high LL;
this distinguishes an actual initial row from an actual long-return image.
Independent controls: literal Rule30 updates against the hand formulas;
selected actual origins against literal/packed shrinking cones.
No word membership, solver, record computation or horizon census.
RETAINED FAILURE: none of the eight predicted no-past110 high-LL
counterexamples returns L0. Hand propagation instead forces a short
return for EVERY tail. Thus the proposed dependence on past was wrong.
ADDENDUM before new controls: P3 initial111001110 always has fifth
track0101101010 and returns S, for every tail. High LL therefore
requires initial sites7,9 both1 even WITHOUT the preceding long.
Check the exact shielding chain on128 complete cones for this single
cylinder, and selected positive101/111 origins. Counterfactual: the
initial110 triple forbids a high fifth track itself; P3 predicts the
track remains high but the successor changes to S.
SECOND FAILURE retained: P3 omitted initial site10. At time2 site8
is NOT initial10, not identically1; the intermediate control caught it.
P3b BEFORE rerun: prefix1110011100 (ten bits) forces high then S.
P4: changing initial10 to1 admits a high LL without an L0 past,
so the ninth-site pin remains specifically an ancestry implication.
P4 REFUTED on32 selected origins. A second shielding chain covers
initial10=1 as well. P3's conclusion survives; its original constant
intermediate table did not. P5 informed BEFORE final controls: prefix
111001110 forces high then S in BOTH site10 branches, for all tails.
Thus high LL pins sites7,9 black without any preceding-L hypothesis.
FINAL OUTCOME:24 local identities and256 complete prefix110 shielding
cones PASS;15 selected high-LL positive origins exist. The initial
eight and revised32 no-past counterexamples both fail as retained.
Literal/packed engines agree. No broader mixed-word search follows.
"""
from itertools import product
from rule30_sl_no_refork import bits,run


def update(row):
    return tuple(row[j-1]^(row[j]|row[j+1]) for j in range(1,len(row)-1))


def main():
    local=0
    for Q,R,Z in product((0,1),repeat=3):
        out=update((1,0,Q,R,Z))
        assert out==(1-Q,Q|R,Q^(R|Z))
        assert out!=(1,1,0)
        local+=1
    for p,q,r,z in product((0,1),repeat=4):
        n=(1-p)&(q|r)
        out=update((1,p,p|q,n,z))
        assert out==(1-(p|q),n,(p|q)^(n|z))
        assert out!=(1,1,0)
        local+=1
    origin_controls=counterexamples=0
    for tail in product((0,1),repeat=3):
        row=bits('1110011100')+tail+(0,)*24
        rows=run(row,10)
        fifth=tuple(r[4] for r in rows[:10])
        if rows[10][:6]==bits('111001') and fifth==bits('0101101010'):
            assert row[6:9]==(1,1,0)
            counterexamples+=1
        origin_controls+=1
    assert counterexamples==0
    forced_short=0
    for e in (0,1):
      chain=({1:(1,0,0),2:(0,1,1),3:(1,1,0,0),
                           4:(0,0,1),5:(1,1,1),6:(1,0,0),
                           7:(0,1),8:(1,1),9:(0,)} if e==0 else
             {1:(1,0,0),2:(0,1,0,1),3:(1,1,0,1),4:(0,0,0,1),
              5:(1,0,1),6:(1,0,1),7:(0,0,1),8:(0,1),9:(0,)})
      for tail in product((0,1),repeat=7):
        rows=run(bits('111001110')+(e,)+tail,10)
        assert tuple(r[4] for r in rows[:10])==bits('0101101010')
        assert rows[10][:5]==bits('11101')
        for t,expected in chain.items():
            assert rows[t][5:5+len(expected)]==expected,(t,expected,rows[t][5:5+len(expected)])
        forced_short+=1
    high_LL=0
    for tri in ('101','111'):
        for tail in product((0,1),repeat=5):
            rows=run(bits('111001'+tri)+tail+(0,)*10,10)
            if rows[10][:6]==bits('111001') and tuple(r[4] for r in rows[:10])==bits('0101101010'):
                high_LL+=1
    assert high_LL
    no_past=0
    for tail in product((0,1),repeat=5):
        rows=run(bits('1110011101')+tail+(0,)*10,10)
        if rows[10][:6]==bits('111001') and tuple(r[4] for r in rows[:10])==bits('0101101010'):
            no_past+=1
    assert no_past==0
    print({'local_identity_controls':local,'origin_controls':origin_controls,
           'failed_no_past_counterexamples':counterexamples,
           'all_tail_short_controls':forced_short,
           'selected_high_LL_positives':high_LL,
           'failed_site10_repair_countercontrols':no_past,'literal_packed':'PASS'})


if __name__=='__main__': main()
