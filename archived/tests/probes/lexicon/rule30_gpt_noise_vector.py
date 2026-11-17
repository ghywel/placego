#!/usr/bin/env python3
"""GC413: fresh-pivot vector ceiling, preregistered before this small run.
T1..4, q0,1/4,1/2. Predict uniform ideal trace; full-noisy-input MI at
most T*(1-h(q)); noisy-copy trace MI no larger (unexpected control).
Independent scalar and literal cone evolution; exact rational tables.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json
from rule30_gpt_toolkit_information import entropy,mi,marginal


def trace(row,T,literal=False):
    result=[]
    for _ in range(T):
        result.append(row[len(row)//2])
        if literal:
            row=tuple((30>>((a<<2)|(b<<1)|c))&1 for a,b,c in zip(row,row[1:],row[2:]))
        else:
            row=tuple(a^(b|c) for a,b,c in zip(row,row[1:],row[2:]))
    return tuple(result)


def main():
    results=[]
    for T in range(1,5):
        n=2*T-1;words=list(product((0,1),repeat=n))
        traces={x:trace(x,T) for x in words}
        assert all(traces[x]==trace(x,T,True) for x in words)
        for q in (Fraction(0),Fraction(1,4),Fraction(1,2)):
            full=defaultdict(Fraction);copy=defaultdict(Fraction)
            for x in words:
                for mask in words:
                    flips=sum(mask);p=Fraction(1,2**n)*q**flips*(1-q)**(n-flips)
                    y=tuple(a^b for a,b in zip(x,mask))
                    full[(traces[x],y)]+=p;copy[(traces[x],traces[y])]+=p
            assert sum(full.values())==1
            assert set(marginal(full,lambda k:k[0]).values())=={Fraction(1,2**T)}
            value=mi(full);two=mi(copy)
            ceiling=T*(1-entropy({0:q,1:1-q}))
            assert two<=value+1e-12 and value<=ceiling+1e-12
            assert abs(value-ceiling)<1e-12 if q in (0,Fraction(1,2)) or T==1 else value<ceiling
            results.append(dict(T=T,q=str(q),full_mi=value,copy_mi=two,ceiling=ceiling))
    print(json.dumps({'cases':results,'exact_probability_literal_and_entropy_controls':'PASS'},indent=2))


if __name__=='__main__':main()
