#!/usr/bin/env python3
"""CP32 hand-prefix certificate controls; predictions before first run.
C1: the five stated paired transitions hold on all needed tail completions.
C2: CP31's four cylinders force 000010 at time8 under sound abstract propagation.
CF: replacing repeated A in (NOT A) OR A OR B by an unrelated C still
makes the expression identically one; must fail at A=1,C=B=0.
Unexpected: CP31's unknown site6 after000010 becomes forced0 by correlation.
REFUTED-BY: a literal transition mismatch or a source missing the common prefix.
No visible-language census, new target enumeration or RV3 computation.
OUTCOME: C1 PASS on15 literal transition controls; C2 PASS for all four
cylinders; CF REFUTED and repeated-variable cancellation confirmed.
"""
from itertools import product
from rule30_gpt_gap_cylinders import one, TAILS
CHAIN = ('000010','101100','00101','01001','00000','100')
def literal_pair(source):
    row=list(source)
    for t in (0,1):
        left=[t]+row[:-1]
        row=[(30 >> (4*left[j]+2*row[j]+row[j+1]))&1
             for j in range(len(row)-1)]
    return ''.join(map(str,row))
def main():
    comparisons=0
    for before,after in zip(CHAIN,CHAIN[1:]):
        width=max(len(before),len(after)+2)
        for tail in product((0,1),repeat=width-len(before)):
            row=tuple(map(int,before))+tail
            assert literal_pair(row).startswith(after),(before,tail)
            comparisons+=1
    for tail in TAILS:
        row=list(map(int,'11100'+tail))+[None]*20
        for t in range(8):
            row=[one(t%2 if j==0 else row[j-1],row[j],row[j+1])
                 for j in range(len(row)-1)]
        assert row[:6]==[0,0,0,0,1,0],tail
    assert ((1^1)|0|0)==0
    for a,b in product((0,1),repeat=2):
        assert ((1^a)|a|b)==1
    print('C1 PASS:',comparisons,'literal transition controls; C2 PASS: four cylinders')
    print('CF REFUTED; unexpected shared-variable cancellation checked')
if __name__ == '__main__':main()
