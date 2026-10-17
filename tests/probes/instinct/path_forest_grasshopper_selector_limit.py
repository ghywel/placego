#!/usr/bin/env python3
"""B119/MI258 preregistration: strict Grasshopper selector's small limit.

BEFORE RUN: M20,d=(2,2,2,2,3,3),p13/q15. All64 labelled splits;
exactly8 fitting splits have a distinct side, all equivalent to A=(2,3).
Four B orders times both positive owners give8 root/order candidates.
Exactly3 endpoint-safe rows, each with2 forbidden proper levels against
the Grasshopper allowance1. Zero strict selector admissions, but exactly4
geometries among16 literal A-order/B-order/owner candidates. Full positive
control M30,d1..6,p21/q21,A-gaps1..4,B=(0,5,11),rootA4 has2 barriers
and must be admitted by Grasshopper. Repeated-gap misuse and collision
counterfactual must reject. Unexpected: distinct A itself solves the miss;
the bound on forbidden-point count, not only repetitions, loses reach.
Independent Cartesian roots, physical geometry and move bags;1CPU sec,
64MiB,200 cases. Stop any mismatch, retain failure, no grid expansion.
REFUTED-BY: a strict admission or a different literal count on the miss.
OUTCOME MI259: predictions/controls pass;0 strict admissions/4 geometries,
10 positive-control orders;CPU0.001193sec/RSS15380480bytes. Raw3635bytes SHA256
acbe4129a0d8f976c4aadc2f32a80aa5a369e5be83351b7b7393d2ca1c3fdbdb.
Shared artifact upload blocked by approval review;raw remains local.
"""
from collections import Counter
from itertools import accumulate, permutations, product
import json
import resource
import time

import path_forest_partial_padding as validation


def prefixes(gaps):
    return (0, *accumulate(gaps))


def classify(M, a, b, p, x, y):
    A = [x, x+sum(a)]
    B = [y+v for v in prefixes(b)]
    endpoints = not set(A) & set(B)
    forbidden = sorted(v-x for v in B if x < v < A[-1])
    distinct = len(set(a)) == len(a)
    accepted = distinct and endpoints and len(forbidden) < len(a)
    return dict(x=x,y=y,B=B,forbidden=forbidden,endpoints=endpoints,
                distinct=distinct,accepted=accepted,p=p)


def main():
    start = time.process_time()
    M=20; h=9; d=(2,2,2,2,3,3); p=13; q=15
    split_rows=[]
    for mask in range(64):
        a=tuple(v for i,v in enumerate(d) if mask>>i & 1)
        b=tuple(v for i,v in enumerate(d) if not mask>>i & 1)
        if sum(a)<=h and sum(b)<=h and len(a)==len(set(a)):
            split_rows.append((a,b))
    assert len(split_rows)==8 and set(split_rows)=={((2,3),(2,2,2,3))}
    # Independent capacity calculation using multiplicities rather than masks.
    load_splits=[(i,j) for i in range(2) for j in range(2)
                 if 14-h <= 2*i+3*j <= h]
    assert load_splits==[(1,1)]
    a=(2,3); orders=sorted(set(permutations((2,2,2,3))))
    rows=[]; witnesses=[]; roots=[]
    for first,P in enumerate((p,q)):
        alpha=(M-1-P)//2
        direct={(x,y) for x,y in product(range(h-5+1),range(h-9+1))
                if x+y==alpha}
        interval={(x,alpha-x) for x in range(max(0,alpha),min(h-5,alpha)+1)}
        assert direct==interval
        roots.append(sorted(direct))
        for b in orders:
            for x,y in sorted(direct):
                row=classify(M,a,b,P,x,y);rows.append(row)
                for order in permutations(a):
                    A=[x+v for v in prefixes(order)];B=row['B']
                    xs,word=validation.physical(M,A,B)
                    good=not set(A)&set(B)
                    assert validation.literal(M,xs)==good
                    assert validation.instrument.literal_geometry(M,set(),xs)==good
                    assert Counter(word)==Counter((p,q,*(-2*v for v in d)))
                    assert word[0]==P and word[len(B)]==(q,p)[first]
                    if good:
                        witnesses.append(validation.validate(M,d,p,q,A,B,first))
    assert roots==[[(3,0)],[(2,0)]]
    safe=[v for v in rows if v['endpoints']]
    assert len(rows)==8 and len(safe)==3 and all(len(v['forbidden'])==2 for v in safe)
    assert not any(v['accepted'] for v in rows) and len(witnesses)==4
    # A genuinely admitted known-theorem case: four distinct A jumps, three B vertices.
    control=classify(30,(1,2,3,4),(5,6),21,4,0)
    assert control['accepted'] and control['forbidden']==[1,7]
    good=[]
    for order in permutations((1,2,3,4)):
        A=[4+v for v in prefixes(order)];B=[0,5,11]
        if not set(A)&set(B):
            good.append(validation.validate(30,(1,2,3,4,5,6),21,21,A,B,0))
    assert good
    # Without the distinct-jump hypothesis, the count test can falsely certify.
    repeated=classify(12,(2,2),(),7,0,2)
    assert repeated['forbidden']==[2] and repeated['endpoints']
    assert not repeated['accepted'] and len(repeated['forbidden'])<2
    assert set(prefixes((2,2))) & {2}
    # Correct move bag with a folded collision must not count as a witness.
    badA=[3,6,8];badB=[0,2,4,6,9]
    xs,word=validation.physical(M,badA,badB)
    assert Counter(word)==Counter((p,q,*(-2*v for v in d)))
    assert not validation.literal(M,xs)
    assert not validation.instrument.literal_geometry(M,set(),xs)
    elapsed=time.process_time()-start
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',
        labelled_splits=64,fitting_distinct_splits=8,root_order_rows=rows,
        strict_admissions=0,endpoint_safe=3,literal_witnesses=witnesses,
        positive_control=control,positive_control_witnesses=good,
        repeated_hypothesis_control=repeated,collision_rejected=True,
        cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':
    main()
