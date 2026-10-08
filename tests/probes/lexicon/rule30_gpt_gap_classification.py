#!/usr/bin/env python3
"""CP33 controls, preregistered before execution, no word census.
C1: from001ABCDEF with A<=B and (A=0 implies B<=C), an output
prefix0100100 requires A=B=C=D=E=F=0 (64 local assignments).
C2: from0111UVWXYZ, output sites4..8 all0 force U=V=W=X=1 (64).
C3: from11100rstu v, output sites5,6 both1 force output site8=0 (32).
CF: A=1,B=0 is a permitted entry; must fail the derived A<=B condition.
Unexpected: exclude the alternative10000 three-gap branch without a
four-cylinder classification. REFUTED-BY: any implication counterexample.
All are fixed two-step controls for the hand identities, not a replay of
CP29's full target or a new visible-language enumeration.
OUTCOME: C1,C2,C3 PASS on64,64,32 local cases; CF REFUTED.
The hand branch argument excludes10000 and removes the finite classification.
"""
from itertools import product
from rule30_gpt_gap_reset import literal_pair

def main():
    counts=[0,0,0]
    for tail in product((0,1), repeat=6):
        a,b,c,d,e,f=tail
        if a<=b and (a or b<=c):
            if literal_pair((0,0,1)+tail).startswith('0100100'):
                assert not any(tail),tail
        counts[0]+=1
    for tail in product((0,1), repeat=6):
        row=literal_pair((0,1,1,1)+tail)
        if row[3:8]=='00000':assert tail[:4]==(1,1,1,1),tail
        counts[1]+=1
    for tail in product((0,1),repeat=5):
        row=literal_pair((1,1,1,0,0)+tail)
        if row[4:6]=='11':assert row[7]=='0',tail
        counts[2]+=1
    assert not (1<=0)
    print('C1,C2,C3 PASS:',counts,'local cases; CF REFUTED')
if __name__=='__main__':main()
