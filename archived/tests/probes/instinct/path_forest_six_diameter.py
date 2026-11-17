#!/usr/bin/env python3
"""B62/MI145 prereg5764eeb2: two-positive/four-negative diameter.

Full arithmetic domain a>=c>=1,b1>=...>=b4>=1,a+c=sum b,a+b1<=28.
Predict minimum span<=22; >20 iff a>=21 or three declared rows. Balanced
negative-subset formula compared with independent nonnegative-prefix DP.
Primitive cases have distinct vertices;15 exceptional small-pair extensions
pass two literal checkers. Caps50k tuples/20CPU sec/10M DP states; no fallback.
Counterfactual maxstep20=>span20 fails. Unexpected sign/coordinate reflection.
OUTCOME MI146:7300 tuples,3409 primitive; all exact minima match independent
DP459900 states.32 wide tuples:29 large-step and3 predicted rows. All15
exception extensions/controls PASS;CPU0.413040s. Artifact SHA256
9d68e30cdd6ca8d44384fb9e9c9239ba29b4708d2eb1b76863a42164602bb01c.
"""
from collections import defaultdict,Counter
from itertools import combinations_with_replacement
import json
import time
from path_forest_cycle_cover import setup,materialize
from path_forest_receiving_chains import certificate_ok
from path_forest_three_surplus_audit import bitset_ok


EXCEPTIONS={
    (17,16,11,11,10,1):(21,1,[(2,3),(0,2),(0,3),(0,4),(3,8)]),
    (17,17,11,11,10,2):(21,4,[(0,1),(1,3),(0,3),(1,5),(0,5)]),
    (17,17,11,11,11,1):(22,1,[(2,3),(0,2),(0,3),(10,14),(3,8)])}


class Cap(Exception):pass


def domain_primary():
    out=set()
    for a in range(1,28):
        for c in range(1,a+1):
            p=a+c
            for b1 in range(1,29-a):
                for b2 in range(1,b1+1):
                    for b3 in range(1,b2+1):
                        b4=p-b1-b2-b3
                        if 1<=b4<=b3:out.add((a,c,b1,b2,b3,b4))
    return out


def domain_reference():
    out=set()
    # a>=P/2 and P>=b1+3, together with a+b1<=28,
    # imply3b1<=53;18 is a deliberately loose upper bound.
    for xs in combinations_with_replacement(range(1,19),4):
        p=sum(xs)
        for c in range(1,p//2+1):
            a=p-c
            if a+xs[-1]<=28:out.add((a,c)+tuple(reversed(xs)))
    return out


def word_points(p):
    a,c,b1,b2,b3,b4=p
    word=(a,-b1,-b4,c,-b2,-b3);s=0;points=[]
    for e in word:points.append(s);s+=e
    assert s==0
    return word,tuple(points)


def subset_minimum(p):
    a,c,*b=p;total=a+c
    sums=[sum(b[i] for i in range(4) if mask>>i&1) for mask in range(16)]
    return max(a,min(max(s,total-s) for s in sums))


def reference_minimum(word,budget):
    # Rotate an arbitrary closed walk at a global minimum. Then its vertices
    # are nonnegative. Optimize maximum height on the full subset lattice;
    # no two-run or balancing formula is used here.
    sums=[0]*64;dp=[10**9]*64;dp[0]=0
    for mask in range(1,64):
        budget['states']+=1
        if budget['states']>10000000:raise Cap('DP_STATES')
        bit=mask&-mask;i=bit.bit_length()-1
        sums[mask]=sums[mask^bit]+word[i]
        if sums[mask]<0:continue
        choices=[dp[mask^(1<<j)] for j in range(6) if mask>>j&1]
        dp[mask]=max(sums[mask],min(choices))
    return dp[63],all(sums[m]!=0 for m in range(1,63))


def extensions():
    rows=[]
    for p,(expected,root,pairs) in EXCEPTIONS.items():
        a,c,*b=p;word,points=word_points(p)
        assert max(points)-min(points)==expected and len(set(points))==6
        for g,pair in enumerate(pairs,1):
            t=(56+2*c,56+2*a)+tuple(sorted([112-2*x for x in b]+[112-2*g,112+2*g]))
            assert len(t)==8 and list(t)==sorted(t) and sum(t)==784
            _,_,e=setup(t);owners=defaultdict(list)
            for i,x in enumerate(e):owners[x].append(i)
            selected={}
            for x,step in zip(points,word):selected[owners[step].pop(0)]=root+x
            selected[owners[g].pop(0)]=pair[0]
            selected[owners[-g].pop(0)]=pair[1]
            xs=list(selected.values());labs=[min(x,27-x) for x in xs]
            assert len(selected)==8 and len(set(labs))==8 and all(0<=x<=27 for x in xs)
            assert Counter(selected[i]+e[i] for i in selected)==Counter(xs)
            reflected={i:27-x for i,x in selected.items()}
            assert Counter(reflected[i]-e[i] for i in reflected)==Counter(reflected.values())
            assert [min(reflected[i],27-reflected[i]) for i in selected]==[min(selected[i],27-selected[i]) for i in selected]
            witness=materialize(t,selected)
            assert certificate_ok(witness['bins'],t) and bitset_ok(witness['bins'],t)
            rows.append(dict(parameters=p,gap=g,targets=t,selected=selected,bins=witness['bins']))
    assert len(rows)==len({tuple(r['targets']) for r in rows})==15
    return rows


def main():
    start=time.process_time();budget={'states':0}
    domain=domain_primary();assert domain==domain_reference() and len(domain)<=50000
    rows=[];wide=[];primitive=Counter();spans=Counter()
    for p in sorted(domain):
        if time.process_time()-start>20:raise Cap('CPU')
        a,c,b1,b2,b3,b4=p;word,points=word_points(p)
        minimum=subset_minimum(p);reference,is_primitive=reference_minimum(word,budget)
        assert minimum==reference,(p,minimum,reference)
        span=max(points)-min(points)
        assert span==max(a,b1+b4,b2+b3)<=22
        assert b1+b4<=18 and a<=22
        assert (minimum>20)==(a>=21 or p in EXCEPTIONS)
        if p in EXCEPTIONS:assert minimum==EXCEPTIONS[p][0] and is_primitive
        if a>=21:assert minimum==a==span
        if is_primitive:assert len(set(points))==6
        primitive[is_primitive]+=1;spans[minimum]+=1
        row=dict(parameters=p,word=word,points=points,prescribed_span=span,
                 minimum_span=minimum,primitive=is_primitive)
        rows.append(row)
        if minimum>20:wide.append(row)
    third=(17,17,11,11,11,1)
    assert max(third)==17 and subset_minimum(third)==22
    word,points=word_points(third)
    assert len({min(x,27-x) for x in points})<6
    certificates=extensions()
    print(json.dumps(dict(status='COMPLETE_ARITHMETIC_CLASS',tuples=len(rows),
        primitive_counts={str(k):v for k,v in primitive.items()},minimum_spans=dict(spans),
        wide=wide,results=rows,extensions=certificates,dp_states=budget['states'],
        controls='PASS',cpu_seconds=time.process_time()-start),separators=(',',':')))


if __name__=='__main__':
    try:main()
    except Cap as e:print(json.dumps(dict(status='UNKNOWN_CAP',reason=str(e))))
