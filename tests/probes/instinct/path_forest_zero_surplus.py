#!/usr/bin/env python3
"""B34 / MI083, preregistered before execution, 2026-10-16.

All E28 even targets (t1,t2,t3,t4,112,112,112,112), t4<112. Four deviations
u,v,-w,-z: matching case two 2-cycles; otherwise alternating 4-cycle with
root 0/1 and two explicit order exceptions. Predict 284 targets (45 paired,
2 exceptional,237 ordinary), from parameter/direct/bounded-DP domains;
check 351-67 generating coefficient arithmetic. Omitted root, order and
paired-root corrections must fail; coverage-preserving wrong sums rejected.
Unexpected all-14 deviation case: monotone shape spans 28, split cycles
work. Cap 500 inputs/five process CPU seconds. No search or cap increase.
Raw outside git; hand construction PROOF-SKETCH pending independent read.
"""
from collections import Counter
from itertools import combinations_with_replacement
import json
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok


def target_for(u,v,w,z):
    return (56+2*u,56+2*v,112-2*w,112-2*z)+(112,)*4


def domains():
    param={}
    for u in range(6,15):
        for v in range(u,17):
            for w in range((u+v+1)//2,min(22,28-v,u+v-1)+1):
                z=u+v-w
                t=target_for(u,v,w,z)
                assert t==tuple(sorted(t)) and z>=1
                param[t]=(u,v,w,z)
    direct={low+(112,)*4 for low in combinations_with_replacement(range(68,111,2),4)
            if sum(low)==336}
    assert set(param)==direct
    dp=[[0]*33 for _ in range(5)];dp[0][0]=1
    for r in range(22):
        for k in range(1,5):
            for s in range(r,33):dp[k][s]+=dp[k-1][s-r]
    def partitions(n,parts):
        a=[1]+[0]*n
        for j in range(1,parts+1):
            for s in range(j,n+1):a[s]+=a[s-j]
        return a
    unrestricted=partitions(32,4)[32]
    excluded=sum(partitions(10,3))
    assert unrestricted==351 and excluded==67
    assert len(param)==dp[4][32]==unrestricted-excluded==284
    return param


def construct(params,force=None):
    u,v,w,z=params;target=target_for(*params)
    if w==v:
        assert z==u and v<=14
        r=2 if (u,v) in ((13,13),(12,14)) else 1
        if force=='paired1':r=1
        selected={0:0,3:u,1:r,2:r+v};branch='paired2' if r==2 else 'paired1'
    elif z==2 and v+w==27 and force!='ordinary':
        assert params in ((9,10,17,2),(7,11,16,2))
        selected={0:0,1:u,2:u+v,3:z};r=0;branch='exception'
    else:
        A=w-u;assert A>0 and v!=w
        r=int(27 in (v+w,A+w))
        if force=='root0':r=0
        selected={1:r,3:r+v,0:r+A,2:r+w};branch='ordinary'+str(r)
    witness=materialize(target,selected)
    assert certificate_ok(witness['bins'],target)
    return dict(params=params,targets=target,root=r,branch=branch,witness=witness)


def main():
    start=time.process_time();family=domains()
    controls=[((8,10,17,1),'root0'),((9,10,17,2),'ordinary'),((7,11,16,2),'ordinary'),
              ((13,13,13,13),'paired1'),((12,14,14,12),'paired1')]
    for p,force in controls:
        try:construct(p,force=force)
        except ValueError as exc:assert str(exc)=='complementary pair reused'
        else:raise AssertionError('omitted correction accepted')
    maximal=[p for p in family.values() if p[0]+p[1]==28]
    assert maximal==[(14,14,14,14)]
    split=construct(maximal[0])
    try:materialize(split['targets'],{0:0,1:14,2:28,3:14})
    except ValueError as exc:assert str(exc)=='position outside pool'
    else:raise AssertionError('out-of-pool monotone shape accepted')
    wrong=[set(b) for b in split['witness']['bins']];a,b=min(wrong[0]),min(wrong[1])
    wrong[0].remove(a);wrong[1].remove(b);wrong[0].add(b);wrong[1].add(a)
    assert Counter(v for bins in wrong for v in bins)==Counter(range(1,56,2))
    assert not certificate_ok(wrong,split['targets'])
    results=[];branches=Counter()
    for t,p in sorted(family.items()):
        if len(results)>=500 or time.process_time()-start>=5:
            print(json.dumps(dict(status='UNKNOWN',completed=len(results))));return
        r=construct(p);assert tuple(r['targets'])==t
        branches[r['branch']]+=1;results.append(r)
    assert branches['paired1']+branches['paired2']==45 and branches['exception']==2
    assert branches['ordinary0']+branches['ordinary1']==237
    print(json.dumps(dict(status='ALL_284',results=results,branches=dict(branches),
        independent_count=284,omitted_corrections='ALL_FIVE_REJECTED_PAIR_COLLISION',
        wrong_sums='REJECTED_COVERAGE_PRESERVED',maximal_split='PASS_MONOTONE_REJECTED',
        cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
