"""GC1075: hand closure of the high-LL 101 origin branch.
Missing inference: CL245 excludes initial 101 by exhaustion; derive an
all-tail shielding chain so GC1074's high mature SL successor is S.
Record searched: 111001101|101.*high|high.*101 with shield|return|exclu
-> 11 hits in 5 files. GC1053 already handles 1011; no complete 101 hand
chain there. Reuse GC1073's exact high selector and 1100 shield.
P1 BEFORE controls: initial 111001101 has sites 6 onward at times1..9
1001,0111,1100,001,111,100,01,11,0. These prefixes are independent
of every farther tail, so fifth high0101101010 returns S, never L0.
P2: the chain at time 3 is exactly the established 1100 chain; initial
site10 affects neither branch. This promotes CL245's 101 exclusion to
hand provenance and closes high SL -> S, not ordinary-L composition.
Counterfactual: a high fifth selector can always choose the next L0
return independently. This cylinder forces S despite a high track.
Unexpected check: sources101 and1100 have different first two rows,
yet the same sites 6..9=1100 at 3 shields their return for every tail.
Independent controls: each one-step shield implication with arbitrary
fresh right bits, then 128 complete local cones, literal against packed.
No solver, word membership, mixed-word scan or record computation.
RETAINED FAILURE: the unexpected check predicted different first two
shield prefixes. The first cone already shares time 1 sites 6..9=1001
with 1100. P3 BEFORE rerun: the distinct origins merge this four-site
shield at 1, then 0111 at 2 and1100 at 3, for unrelated farther tails.
The main P1 shield and high-then-S checks passed on that first cone
before this failure.
OUTCOME: all 15 one-step shield implications and 128 complete cones
PASS; literal and packed agree. Distinct origins share the shield
already at time 1, correcting the unexpected-check prediction.
"""
from itertools import product
from rule30_sl_no_refork import bits, run

FIFTH=bits('0101101010')
SHIELD={1:bits('1001'),2:bits('0111'),3:bits('1100'),
        4:bits('001'),5:bits('111'),6:bits('100'),
        7:bits('01'),8:bits('11'),9:bits('0')}


def update(row):
    return tuple(row[k-1]^(row[k]|row[k+1]) for k in range(1,len(row)-1))


def main():
    local=0
    # The first shield update starts from the actual initial sites5..9.
    old=bits('1101') # initial sites6..9
    for t in range(9):
        wanted=SHIELD[t+1]
        needed=max(0,len(wanted)+1-len(old))
        for fresh in product((0,1),repeat=needed):
            row=(FIFTH[t],)+old+fresh
            assert update(row)[:len(wanted)]==wanted,(t,row,wanted)
            local+=1
        old=wanted
    cones=0
    for tail in product((0,1),repeat=7):
        rows=run(bits('111001101')+tail,10)
        assert tuple(r[4] for r in rows[:10])==FIFTH
        assert rows[10][:5]==bits('11101')
        for t,expected in SHIELD.items():
            assert rows[t][5:5+len(expected)]==expected,(t,tail)
        # Unexpected common shield, with unrelated outer tails.
        other=run(bits('1110011100')+tuple(1-x for x in tail),10)
        assert rows[0][5:9]!=other[0][5:9]
        assert rows[1][5:9]==other[1][5:9]==bits('1001')
        assert rows[2][5:9]==other[2][5:9]==bits('0111')
        assert rows[3][5:9]==other[3][5:9]==bits('1100')
        cones+=1
    assert cones==128
    print({'local_shield_implications':local,'exact_origin_cones':cones,
           'high_then_S':'PASS','literal_packed':'PASS',
           'different_origins_common_shield':'PASS'})


if __name__=='__main__': main()
