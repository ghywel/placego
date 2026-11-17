#!/usr/bin/env python3
"""GC412 preregistered application, imported119 checked n3 domain.
Predict positive joint-minus-marginal information for first two Rule30
observations at noise1/4; zero at0 and1/2. Exact rational joint tables,
independent literal rule control, entropy chain versus direct MI.
This tests an application, not the imported general theorem or a seed.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import log2
import json


def entropy(table):
    return -sum(float(p)*log2(float(p)) for p in table.values() if p)


def marginal(table, selector):
    out=defaultdict(Fraction)
    for key,p in table.items(): out[selector(key)]+=p
    return out


def mi(table):
    left=marginal(table,lambda k:k[0]);right=marginal(table,lambda k:k[1])
    direct=sum(float(p)*log2(float(p/(left[u]*right[v]))) for (u,v),p in table.items() if p)
    chain=entropy(left)+entropy(right)-entropy(table)
    assert abs(direct-chain)<1e-12
    return direct


def main():
    results=[]
    for noise in (Fraction(0),Fraction(1,4),Fraction(1,2)):
        joint=defaultdict(Fraction)
        for x in product((0,1),repeat=3):
            a,b,c=x;f=(b,a^(b|c))
            assert f[1]==((30>>((a<<2)|(b<<1)|c))&1)
            for mask in product((0,1),repeat=3):
                flips=sum(mask);p=Fraction(1,8)*noise**flips*(1-noise)**(3-flips)
                y=tuple(u^v for u,v in zip(x,mask));joint[(f,y)]+=p
        assert sum(joint.values())==1
        assert set(marginal(joint,lambda k:k[0]).values())=={Fraction(1,4)}
        one=[mi(marginal(joint,lambda k:(k[0][i],k[1]))) for i in range(2)]
        total=mi(joint);gap=total-sum(one)
        conditioned=entropy(marginal(joint,lambda k:(k[0][0],k[1])))+entropy(marginal(joint,lambda k:(k[0][1],k[1])))-entropy(marginal(joint,lambda k:k[1]))-entropy(joint)
        assert abs(gap-conditioned)<1e-12
        assert gap>0 if noise==Fraction(1,4) else abs(gap)<1e-12
        results.append(dict(noise=str(noise),marginal_mi=one,joint_mi=total,gap=gap,conditional_mi=conditioned))
    print(json.dumps({'results':results,'exact_probability_and_independent_entropy_controls':'PASS'},indent=2))


if __name__=='__main__':main()
