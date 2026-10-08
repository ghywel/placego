"""GC479 local rule-transfer scope audit, not an orbit census.
P1: every U=1 Rule210 pair update clears occupancy marker (1-P)Q.
P2: verbatim Rule30 clearing implication fails on an unrestricted patch.
CF0: replacing Rule210 by Rule30 preserves all16 pair identities; must fail.
Unexpected: both rules retain the all-zero fixed row; period1 remains possible.
REFUTED-BY: a Rule210 marker failure or no Rule30 witness.
"""
def step(rule,l,c,r):return (rule>>(4*l+2*c+r))&1
if __name__=='__main__':
    counts={210:0,30:0};first=None
    for U in (0,1):
        for B in (0,1):
            for P in (0,1):
                for Q in (0,1):
                    target=(1-U)*(B^((1-P)*Q))
                    for rule in (210,30):
                        pp=step(rule,U,B,P);qq=step(rule,B,P,Q)
                        if (1-pp)*qq!=target:
                            counts[rule]+=1
                            if rule==30 and first is None:first=(U,B,P,Q,pp,qq)
                        if rule==210 and U:assert (1-pp)*qq==0
    assert counts[210]==0 and counts[30]>0
    assert (step(30,1,1,0),step(30,1,0,0))==(0,1)
    assert step(210,0,0,0)==step(30,0,0,0)==0
    print('pair identity mismatches',counts,'first Rule30 witness',first,
          'designated U1 witness outputs01; zero-row guard PASS')
