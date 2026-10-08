#!/usr/bin/env python3
"""GC505 exact first-two-tick single-flip front controls.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_front_selection.py
PREDICTIONS registered before execution, 2026-10-08:
 FS0: sitewise XOR/OR and literal decimal updates agree for 512
      initial patches on -4..4 and their site-0 flips through two ticks.
 FS1: first L displacement has masses 1/2,1/4,1/4 at -1,0,1.
 FS2: first +1 implies next -1; next -1 probability is 5/8.
 CF: second-tick left-advance probability is 1/2, must fail.
 UNEXPECTED: conditional advance probabilities are 1/2,1/2,1 for
      the three first displacements; random-site fairness is insufficient.
 OUTCOME (2026-10-08): all 512 two-tick controls PASS; first counts
 256,128,128, second left-advance count 320. FS1/FS2 PASS; CF REFUTED.
 Finite cones only; no speed simulation.
"""
from collections import Counter


def step(black, literal):
    lo=min(black,default=0)-1; hi=max(black,default=0)+1
    out=set()
    for i in range(lo,hi+1):
        l,c,r=[int(j in black) for j in (i-1,i,i+1)]
        bit=(30>>(4*l+2*c+r))&1 if literal else l^(c|r)
        if bit: out.add(i)
    return out


def main():
    first=Counter(); second=Counter(); conditional=Counter()
    for seed in range(512):
        x={i-4 for i in range(9) if seed>>i&1}; y=x^{0}
        a,b=set(x),set(y)
        fronts=[]
        for _ in range(2):
            x,y=step(x,False),step(y,False)
            a,b=step(a,True),step(b,True)
            assert (x,y)==(a,b)
            assert x^y
            fronts.append(min(x^y))
        d1=fronts[0]; d2=fronts[1]-fronts[0]
        first[d1]+=1;second[d2]+=1
        conditional[(d1,d2==-1)]+=1
        if d1==1: assert d2==-1
    assert first=={-1:256,0:128,1:128}
    assert second[-1]==320
    assert conditional[(-1,True)]==128
    assert conditional[(0,True)]==64
    assert conditional[(1,True)]==128
    print('FS0 PASS: 512 patches, two ticks, independent rules')
    print('first displacement counts:',sorted(first.items()))
    print('second -1 count: 320/512; first +1 always undone')
    print('FS1/FS2 PASS; fresh-fair-front CF REFUTED')
    print('ALL CHECKS PASS')


if __name__=='__main__': main()
