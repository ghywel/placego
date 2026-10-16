#!/usr/bin/env python3
"""B35 / MI085 plus pre-run addendum, preregistered before execution.

Every E28 even target with exactly one high surplus a=1..5. Four-move
zero-surplus parent plus one subdivided negative edge; literal-collision
split/paired cases handled first. Predict 1,198 targets: 268/256/239/226/209.
Parameter/direct/bounded-DP domains agree; every five-point shape distinct,
span <=20 (stronger pre-run bound), and reflection-free translation exists.
All parent/child permutation and full-odd checks. Sharp span-23 shape fails;
omitted split/paired correction repeats an index; omitted translation and
wrong sums rejected. Exceptional parent can occur only at a=1. Cap 1,500
inputs/five process CPU seconds, stop on any failure. Raw outside git.
"""
from collections import Counter
from itertools import combinations_with_replacement
import json
import time
from path_forest_zero_surplus import construct as parent_construct
from path_forest_cycle_cover import materialize,setup
from path_forest_receiving_chains import certificate_ok


def target_for(u,v,W,Z,a):
    return (56+2*u,56+2*v,112-2*W,112-2*Z)+(112,)*3+(112+2*a,)


def domains():
    param={}
    for a in range(1,6):
        for u in range(6,15):
            for v in range(u,17):
                S=u+v+a
                for W in range((S+1)//2,min(22,28-v,S-1)+1):
                    Z=S-W;t=target_for(u,v,W,Z,a)
                    assert t==tuple(sorted(t));param[t]=(u,v,W,Z,a)
    direct={}
    for a in range(1,6):
        for low in combinations_with_replacement(range(68,111,2),4):
            if sum(low)==336-2*a:direct[low+(112,)*3+(112+2*a,)]=a
    assert set(param)==set(direct)
    dp=[[0]*33 for _ in range(5)];dp[0][0]=1
    for r in range(22):
        for k in range(1,5):
            for s in range(r,33):dp[k][s]+=dp[k-1][s-r]
    counts=Counter(p[-1] for p in param.values())
    assert [counts[a] for a in range(1,6)]==[268,256,239,226,209]
    assert [dp[4][32-a] for a in range(1,6)]==[counts[a] for a in range(1,6)]
    assert len(param)==1198
    return param


def abstract(params,force=None):
    u,v,W,Z,a=params
    assert W>a
    reduced=W-a;L,S=max(reduced,Z),min(reduced,Z)
    parent=parent_construct((u,v,L,S))
    if W==v and force!='no_split':
        selected={0:0,7:u,3:u+a,1:1,2:v+1};branch='split'
    elif L==v:
        assert S==u
        if reduced==v:
            selected={0:0,3:u,1:1,7:v+1,2:v+1+a};branch='paired_large'
        else:
            assert reduced==u<v and Z==v
            r=2 if W==v+1 else 1
            if force=='no_paired_correction':r=1
            selected={0:0,1:r,3:r+v,7:u,2:W};branch='paired_small'
    else:
        base=parent['witness']['selected']
        modified=2 if reduced>=Z else 3
        other=5-modified
        selected={0:base[0],1:base[1],2:base[modified],3:base[other]}
        old=selected[2];selected[7]=old;selected[2]=old+a
        branch='ordinary_subdivision'
        if parent['branch']=='exception':
            assert a==1 and modified==2
            branch='exceptional_parent'
    minimum=min(selected.values());selected={i:x-minimum for i,x in selected.items()}
    if len(set(selected.values()))!=5:raise ValueError('repeated index')
    target=target_for(*params);_,_,e=setup(target)
    assert Counter(x+e[i] for i,x in selected.items())==Counter(selected.values())
    assert max(selected.values())<=20
    return selected,branch,parent['branch']


def translation(points):
    points=tuple(sorted(points));base=points[0];shape=tuple(x-base for x in points)
    if len(shape)!=len(set(shape)):return None
    for r in range(28-shape[-1]):
        labels=[min(r+x,27-r-x) for x in shape]
        if len(labels)==len(set(labels)):return r
    return None


def construct(params,force=None):
    selected,branch,parent_branch=abstract(params,force=force)
    r=translation(selected.values())
    assert r is not None
    if force=='no_translation':r=0
    translated={i:x+r for i,x in selected.items()};target=target_for(*params)
    witness=materialize(target,translated)
    assert certificate_ok(witness['bins'],target)
    return dict(params=params,targets=target,branch=branch,parent_branch=parent_branch,
                shape=selected,span=max(selected.values()),translation=r,witness=witness)


def main():
    start=time.process_time();family=domains()
    sharp=(0,2,4,19,23);assert translation(sharp) is None
    assert {x+y for x in sharp for y in sharp if x<y and (x+y)%2} >= {19,21,23,25,27}
    for p,force in (((6,8,8,7,1),'no_split'),((6,7,8,7,2),'no_paired_correction')):
        try:abstract(p,force=force)
        except ValueError as exc:assert str(exc)=='repeated index'
        else:raise AssertionError('literal collision accepted')
    try:construct((8,10,18,1,1),force='no_translation')
    except ValueError as exc:assert str(exc)=='complementary pair reused'
    else:raise AssertionError('required translation omitted but accepted')
    sample=construct((6,8,8,7,1));wrong=[set(b) for b in sample['witness']['bins']]
    a,b=min(wrong[0]),min(wrong[1]);wrong[0].remove(a);wrong[1].remove(b)
    wrong[0].add(b);wrong[1].add(a)
    assert Counter(v for bins in wrong for v in bins)==Counter(range(1,56,2))
    assert not certificate_ok(wrong,sample['targets'])
    results=[];branches=Counter();spans=Counter();parents=Counter()
    for t,p in sorted(family.items()):
        if len(results)>=1500 or time.process_time()-start>=5:
            print(json.dumps(dict(status='UNKNOWN',completed=len(results))));return
        result=construct(p);assert tuple(result['targets'])==t
        results.append(result);branches[result['branch']]+=1;spans[result['span']]+=1
        parents[result['parent_branch']]+=1
    print(json.dumps(dict(status='ALL_1198',results=results,branches=dict(branches),
        spans=dict(spans),parents=dict(parents),independent_count=len(family),
        sharp_span23='NO_TRANSLATION',literal_collisions='BOTH_REJECTED',
        omitted_translation='REJECTED_PAIR_COLLISION',wrong_sums='REJECTED_COVERAGE_PRESERVED',
        exceptional_parents='ONLY_A1',cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
