#!/usr/bin/env python3
"""B242 / MI468: cuts + all sum-class matching capacities, fixed k6..8.
20s / 100k capacity queries / 200k independent search states; first negative.
No solver, random choice, size expansion or retry.
"""
from itertools import permutations
from math import factorial
from collections import Counter
from functools import lru_cache
import json,time
START=time.monotonic(); queries=0

def guard():
    assert time.monotonic()-START<20,'wall cap'

def cuts(q,k):
    return sum(q)==k*(2*k-1) and all(sum(q[:r])>=r*(k+r-1) for r in range(1,k))

def profile_stream(k):
    goal=k*(2*k-1)
    def rec(prefix,last,left,total):
        if left==1:
            if last<=total<=3*k-2:
                q=prefix+(total,)
                if cuts(q,k):yield q
            return
        for x in range(last,min(3*k-2,total//left)+1):
            rem=total-x
            if rem>(left-1)*(3*k-2):continue
            new=prefix+(x,);r=len(new)
            if sum(new)<r*(k+r-1):continue
            yield from rec(new,x,left-1,rem)
    yield from rec((),k,k,goal)

@lru_cache(None)
def capacity(k,mask):
    global queries
    queries+=1;assert queries<=100000,'query cap';guard()
    adj=[[j for j in range(k) if mask>>(i+j)&1] for i in range(k)]
    mate=[-1]*k
    def augment(i,seen):
        for j in adj[i]:
            if j in seen:continue
            seen.add(j)
            if mate[j]<0 or augment(mate[j],seen):mate[j]=i;return True
        return False
    value=sum(augment(i,set()) for i in range(k))
    # Independent Hall-deficiency formula: max matching = k-max_X(|X|-|N(X)|).
    neighbor_bits=[sum(1<<j for j in range(k) if mask>>(i+j)&1) for i in range(k)]
    unions=[0]*(1<<k);deficiency=0
    for rows in range(1,1<<k):
        one=rows&-rows;i=one.bit_length()-1
        unions[rows]=unions[rows^one]|neighbor_bits[i]
        deficiency=max(deficiency,rows.bit_count()-unions[rows].bit_count())
    assert value==k-deficiency,'capacity mismatch'
    return value

def checked_capacity(k,mask):
    val=capacity(k,mask)
    reflected=sum(1<<(2*k-2-d) for d in range(2*k-1) if mask>>d&1)
    assert val==capacity(k,reflected),'reflection mismatch'
    return val

def independent_exists(q,k):
    counts=Counter(q);states=0
    def rec(i,used):
        nonlocal states
        states+=1;assert states<=200000,'independent cap';guard()
        if i==k:return True
        for j in range(k):
            x=k+i+j
            if used>>j&1 or not counts[x]:continue
            counts[x]-=1
            result=rec(i+1,used|1<<j)
            counts[x]+=1
            if result:return True
        return False
    return rec(0,0),states

def main():
    assert checked_capacity(6,1<<(9-6))==4
    assert checked_capacity(6,1<<(13-6))==4
    assert checked_capacity(6,(1<<(9-6))|(1<<(13-6)))==4
    assert checked_capacity(6,1<<(11-6))==6
    assert cuts((9,9,9,13,13,13),6)
    print(json.dumps({'controls':'known clump, singleton-only counterfactual, positive reverse, Hall/augment and reflection PASS'}),flush=True)
    expected={6:246,7:1105,8:5270}
    for k in (6,7,8):
        actual=set();leaves=0
        for p in permutations(range(k)):
            q=tuple(sorted(k+i+j for i,j in enumerate(p)))
            actual.add(q);leaves+=1
        assert leaves==factorial(k) and len(actual)==expected[k]
        assert all(cuts(q,k) for q in actual)
        seen=missing=rejected=0
        for q in profile_stream(k):
            guard();seen+=1
            if q in actual:continue
            missing+=1;cc=Counter(q);support=tuple(cc)
            witness=None
            for bits in range(1,1<<len(support)):
                sums=tuple(x for i,x in enumerate(support) if bits>>i&1)
                demand=sum(cc[x] for x in sums)
                cap=checked_capacity(k,sum(1<<(x-k) for x in sums))
                if demand>cap:witness=(sums,demand,cap);break
            if witness:rejected+=1;continue
            exists,nodes=independent_exists(q,k);assert not exists,'negative oracle mismatch'
            print(json.dumps({'result':'FIRST GROUP-ADMITTED NEGATIVE','k':k,'profile':q,'cuts':True,'all_support_subsets':(1<<len(support))-1,'independent_nodes':nodes,'cut_profiles_seen':seen,'missing_seen':missing,'capacity_queries':queries,'seconds':time.monotonic()-START}),flush=True)
            return
        print(json.dumps({'result':'FIXED ORDER PASS','k':k,'permutations':leaves,'actual_profiles':len(actual),'cut_profiles':seen,'missing':missing,'rejected_by_groups':rejected,'capacity_queries':queries,'seconds':time.monotonic()-START}),flush=True)
    print(json.dumps({'result':'FIXED DOMAIN PASS ONLY','capacity_queries':queries,'seconds':time.monotonic()-START}),flush=True)

if __name__=='__main__':main()
