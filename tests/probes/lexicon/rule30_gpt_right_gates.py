#!/usr/bin/env python3
"""G61 preregistered controls published at82e86c0 before this run.
RG1 MUST: all8(s,d,s_next) triples,4(b,c) pairs: scalar Rule210
existence iff d=0 OR(s=0 AND s_next=1).
RG2 MUST: n=0..4095 transitions match n=2^(2r+1)-1 exactly.
CF MUST FAIL: all invisible odd-time bits are free; obstruction(1,1,0).
Unexpected guard MUST: s=1,b=1,d=0 can activate a deeper pair.
No blind predictions; no claim of full column2 realization.
"""
from itertools import product


def f(l,c,r):return (210>>(4*l+2*c+r))&1


def effective(n):return 1 if n==0 else (n.bit_length()-1)%2


def main():
    accepted=0;pair_checks=0
    for s,d,nxt in product((0,1),repeat=3):
        possible=[]
        for b,c in product((0,1),repeat=2):
            pair_checks+=1
            if f(0,s,b)==d and f(1,d,c)==nxt:possible.append((b,c))
        assert bool(possible)==(d==0 or (s==0 and nxt==1))
        accepted+=bool(possible)
    found=[n for n in range(4096) if effective(n)==0 and effective(n+1)==1]
    predicted=[];r=0
    while 2**(2*r+1)-1<4096:
        predicted.append(2**(2*r+1)-1);r+=1
    assert found==predicted
    assert not any(f(0,1,b)==1 and f(1,1,c)==0 for b,c in product((0,1),repeat=2))
    # (s,d,next,b,c)=(1,0,0,1,1): both updates allowed, s*b=1.
    assert f(0,1,1)==0 and f(1,0,1)==0 and 1*1==1
    print('RG1 PASS:8 triples,',pair_checks,'pair checks,',accepted,'accepted triples')
    print('RG2 PASS:4096 indices; gates',found)
    print('CF REFUTED:(s,d,next)=(1,1,0); deeper nonlinear guard PASS')


if __name__=='__main__':main()

# OUTCOME 2026-10-06: RG1 PASS8 triples/32 pairs/5 accepted; RG2
# PASS4096 indices; CF REFUTED; even-time nonlinear guard PASS.
