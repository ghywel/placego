#!/usr/bin/env python3
"""GC2404: tiny exact review countercontrols, no census/solver/long trajectory.

Predictions written in the review: wrong frontier key, wrong strip boundary,
and binomial distance/pairwise fairness insufficient for independence/parity.
"""
from collections import Counter
from fractions import Fraction

seed = tuple(map(int,'100100000')); N=len(seed); orbit=[seed]
while True:
    y=orbit[-1];z=tuple(y[j]^(y[j-1]|y[j-2]) for j in range(N))
    if z==seed:break
    assert z not in orbit;orbit.append(z)
q=len(orbit)
rates=[]
for correct in (False,True):
    seen={};x=t=0
    while True:
        key=(t%q,(t-x)%N) if correct else (x%N,t%q)
        if key in seen:break
        seen[key]=(x,t)
        x-=orbit[t%q][(t-x)%N]==0;t+=1
    x0,t0=seen[key];rates.append(Fraction(x0-x,t-t0))
assert rates==[Fraction(9,19),Fraction(1,2)]
print('healing_bound one-alignment cycle: legacy9/19, phase-complete1/2')

# G8 tq0,j0=1, actual strip cells at k,k+1 are1,0. The lower
# diagonal k-1 has depth j0+1=2; current Ebelow looks at j0-1=0.
ring=(1,0,0,0);j0=1
actual=ring[(j0+1)%4]^(1|0)
coded=ring[(j0-1)%4]^(1|0)
assert (actual,coded)==(1,0)
print('strip_graph G8 lower-boundary control: actual next cell1, coded0')

# A uniform2-bit A, independent D~Binomial(2,1/2), V chosen as a
# SINGLE mask per weight. Both A/B uniform, distance binomial, A/B dependent.
joint=Counter();aa=Counter();bb=Counter();dist=Counter()
for a in range(4):
    for mask,weight in ((0,1),(1,2),(3,1)):
        b=a^mask;joint[a,b]+=weight;aa[a]+=weight;bb[b]+=weight
        dist[(a^b).bit_count()]+=weight
assert set(aa.values())=={4} and set(bb.values())=={4}
assert dist=={0:4,1:8,2:4} and joint[0,2]==0
print('binomial Hamming distance and uniform marginals hold exactly; independence fails')
triples=[(u,v,u^v) for u in (0,1) for v in (0,1)]
assert all(len({(row[i],row[j]) for row in triples})==4 for i,j in ((0,1),(0,2),(1,2)))
assert all(a^b^c==0 for a,b,c in triples)
print('three pairwise independent fair bits have constant parity0')
print('CLOUD_REVIEW_CONTROLS_DONE')
