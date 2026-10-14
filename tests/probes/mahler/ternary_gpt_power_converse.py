#!/usr/bin/env python3
"""Bounded controls for INSTINCT-GPT S7's nonlinear ternary converse.
COMMAND: python3 tests/probes/mahler/ternary_gpt_power_converse.py
RUN-ON: Intel host, one standard-library Python process, expected <30s.
Record searched: record_find.py 'converse' 'ternary' -> four paragraphs;
Cloud8.110/GC1246, S7 and Lagarias2009 Lemma4.1 read. The latter is linear
multiplication, not this power-map claim. No exact nonlinear prior attribution.
PREDICTIONS BEFORE FIRST RUN (GC1248):
 PC1: for every nonzero e=-80..80 with 3-free(e)=1 mod3 and h1..6,
      greedy input digits extend the seed1+3^h to96 digits, with all
      corresponding output digits through96+v3(e) in{0,1}.
 PC2: for the16 signed sign-plus exponents in PLUS, every locally admissible
      unit prefix of lengths1..10 has at least one admissible next digit.
 PC3: each candidate child changes the output digit at i+v3(e) by d mod3,
      and preserves every lower output digit; checked throughout PC1/PC2.
 CF1 must FAIL: the same seed extends for sign-minus exponents in MINUS,
      h1..6. Its first nonconstant output digit must instead be2.
 CF2 must FAIL: omit the output shift when e=3; input4->13 changes digit3,
      not digit2, of its cube.
 U unexpected: ordinary integer4 and its fourth power256 are both ternary01.
      This controls against overclaiming all constructed pairs must be noninteger.
REFUTED-BY: any PC failure, either bad rule surviving, or a failure of U.
Finite controls do not prove infinite existence, novelty, uncountability,
termination of the greedy sequence, or any assertion about powers of2.
OUTCOME at registration: NOT RUN. Append results; preserve predictions.
"""
from itertools import product
from time import perf_counter

PLUS=(-54,-24,-8,-6,-2,1,3,4,7,9,10,12,27,28,36,81)
MINUS=(-27,-9,-3,-1,2,6,8,18,24,54,80)

def valuation(n):
    assert n
    b=0
    while n%3==0:
        n//=3
        b+=1
    return b,n

def allowed(n,k):
    for _ in range(k):
        if n%3==2:
            return False
        n//=3
    return True

def children(x,i,e):
    b,u=valuation(e)
    mod=3**(i+b+1)
    old=pow(x,e,mod)
    out=[]
    for d in (0,1):
        y=pow(x+d*3**i,e,mod)
        assert (y-old)%3**(i+b)==0,(e,x,i,d,'lower digits')
        assert ((y-old)//3**(i+b))%3==d*u%3,(e,x,i,d,'digit slope')
        if allowed(y,i+b+1):
            out.append(d)
    return out

def main():
    start=perf_counter()
    cases=steps=0
    examples={}
    for e in range(-80,81):
        if not e:
            continue
        b,u=valuation(e)
        if u%3!=1:
            continue
        for h in range(1,7):
            x=1+3**h
            assert allowed(pow(x,e,3**(h+b+1)),h+b+1)
            for i in range(h+1,96):
                ds=children(x,i,e)
                assert ds,(e,h,i,'greedy dead end')
                x+=ds[0]*3**i
                steps+=1
            assert allowed(x,96) and x%3==1
            assert (x-1)%3**h==0 and (x-1)%3**(h+1)!=0
            assert allowed(pow(x,e,3**(96+b)),96+b)
            cases+=1
            if h==1 and e in(-2,3,4):
                examples[e]=x
    print('PC1 PASS',cases,'greedy paths;',steps,'extension steps')
    prefixes=0
    for e in PLUS:
        b,u=valuation(e)
        assert u%3==1
        for k in range(1,11):
            for bits in product((0,1),repeat=k-1):
                x=1+sum(d*3**(j+1) for j,d in enumerate(bits))
                if not allowed(pow(x,e,3**(k+b)),k+b):
                    continue
                assert children(x,k,e),(e,k,x,'prefix dead end')
                prefixes+=1
    print('PC2 PASS',prefixes,'admissible prefixes; lengths1..10,16 exponents')
    print('PC3 PASS shifted digit slope and lower-digit preservation in every child')
    rejects=0
    for e in MINUS:
        b,u=valuation(e)
        assert u%3==2
        for h in range(1,7):
            y=pow(1+3**h,e,3**(h+b+1))
            assert y//3**(h+b)%3==2
            rejects+=1
    print('CF1 rejected',rejects,'wrong-sign seeds')
    assert (13**3-4**3)%3**3==0 and (13**3-4**3)//3**3%3==1
    print('CF2 rejected: cube digit2 unchanged, digit3 changes by1')
    assert 4**4==256 and allowed(4,2) and allowed(256,6)
    print('U PASS: 4=(11)_3, 256=(100111)_3')
    for e,x in examples.items():
        print('96-digit residue, e=',e,':',x)
    print('ALL CONVERSE CONTROLS PASS; seconds',round(perf_counter()-start,3))

if __name__=='__main__':
    main()
