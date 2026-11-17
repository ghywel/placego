#!/usr/bin/env python3
"""GC506 fixed position-only Markov audit, three ticks only.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_front_markov.py
PREDICTIONS registered in CLOUD-LOCAL before first execution:
 FM0 must: independent rule implementations agree on all 8192 initial
      patches on -6..6, their single flips, and all three ticks.
 FM1 blind: with L_2=0, the third-step law differs for some L_1 histories.
 CF: second-step left-advance probability is 1/2, must fail (GC505).
 UNEXPECTED: compare full jump distributions even if healing rates agree.
 REFUTED-BY: FM0 failure invalidates instrument; FM1 failure retained.
 OUTCOME (2026-10-08): FM0 PASS on 8192 patches; FM1 HELD.
 L_2=0 history counts for L_1=-1,0,1: 1280,512,2048.
 Third left-advance probabilities: 1,1/2,1/2. Full laws in stdout.
 CF REFUTED: second left-advance probability 5/8.
 No larger horizon or speed simulation.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from rule30_gpt_front_selection import step


def main():
    groups=defaultdict(Counter); first=Counter();second_left=0
    for seed in range(8192):
        x={i-6 for i in range(13) if seed>>i&1};y=x^{0}
        a,b=set(x),set(y);fronts=[]
        for _ in range(3):
            x,y=step(x,False),step(y,False)
            a,b=step(a,True),step(b,True)
            assert (x,y)==(a,b)
            assert x^y
            fronts.append(min(x^y))
        first[fronts[0]]+=1
        second_left+=fronts[1]-fronts[0]==-1
        if fronts[1]==0:
            groups[fronts[0]][fronts[2]]+=1
    assert first=={-1:4096,0:2048,1:2048}
    assert second_left==5120
    laws=[]
    for key,counts in sorted(groups.items()):
        total=sum(counts.values())
        law={k:Fraction(v,total) for k,v in sorted(counts.items())}
        laws.append(law)
        print('L1=%d L2=0 count=%d next law=%s'%(key,total,law))
    held=any(law!=laws[0] for law in laws[1:])
    print('FM0 PASS: 8192 initial patches, three ticks, independent rules')
    print('FM1 %s'%('HELD' if held else 'REFUTED'))
    print('fresh-fair CF REFUTED: second left advance 5120/8192')
    print('ALL CHECKS PASS')


if __name__=='__main__':main()
