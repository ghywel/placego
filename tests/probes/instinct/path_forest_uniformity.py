#!/usr/bin/env python3
"""B57/MI134, preregistered71c9c265: frozen E28 uniformity diagnostic.

2000 uniform distinct ranks each from even/all E28, seeds20261016/17.
Primitive zero-sum components, known opposite-sign order class (ANY first
term, explicitly lifted from B56), reflection-aware origins, joint labels.
No exception lookup/role search/arbitrary order/solver fallback. Prediction
97% even,1.3% unconditional,0% parity-inapplicable;95% portability gate.
First12 even component maps and packing checked independently; small full
rank/unrank domains/Gaussian counts, two literal checkers, duplicate/sum/
reflection counterfactuals; unexpected balanced multiple-component check.
Caps20k nodes/target,2M total,30CPU seconds,2M reference words/10M roots.
REFUTED-BY: observed fraction below prediction; no repair or cap increase.
Raw JSON outside git; no universal E28/L8 or novelty conclusion.
OUTCOME:2000/2000 even certify;25/2000 unconditional certify,1975 parity
inapplicable.217933 total nodes, max2194 per sampled target, no cap.
114 complete component-label placement maps and14 full packings agree
with independent permutation/direct-root/set-packing references;3099
reference words/9498 roots. Both literal checkers and controls pass.
CPU2.489268 s.97% even forecast exceeded;1.3% unconditional point
forecast missed by one case (1.25% observed); no significance claim.
Immutable full sample SHA256
c5b4ec84c7dc7232cd52b37d3a1c2afcbbeb52054a15870cadf95c0b6b8118f0.
INSTRUMENT NOTE: first run stopped before sampling: a B56 prefix-mask
fixture was mislabeled rootless. Replaced it with B55's actual first
exhausted greedy shape, as preregistered. No targets/caps/predictions changed.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement, permutations
import hashlib
import json
import random
import sys
import time

from path_forest_cycle_cover import materialize, setup
from path_forest_exceptional_counts import gaussian_coefficients
from path_forest_nyctalopic_reflection import ALL, extend, direct_mask
from path_forest_receiving_chains import certificate_ok
from path_forest_three_surplus_audit import bitset_ok


class Cap(Exception):
    pass


class Budget:
    def __init__(self):
        self.start=time.process_time();self.counts=Counter();self.local=0
    def add(self,key,n=1):
        self.counts[key]+=n
        if key=='nodes':self.local+=n
        if self.local>20000:raise Cap('target_nodes')
        limits={'nodes':2000000,'reference_words':2000000,'reference_roots':10000000}
        if key in limits and self.counts[key]>limits[key]:raise Cap(key)
        if time.process_time()-self.start>30:raise Cap('overall_cpu')


@lru_cache(None)
def count(k,lo,hi,total):
    if k==0:return int(total==0)
    if total<k*lo or total>k*hi:return 0
    return sum(count(k-1,x,hi,total-x) for x in range(lo,min(hi,total//k)+1))


def unrank(k,hi,total,r):
    assert 0<=r<count(k,0,hi,total)
    lo=0;answer=[]
    while k:
        for x in range(lo,min(hi,total//k)+1):
            n=count(k-1,x,hi,total-x)
            if r>=n:r-=n
            else:break
        answer.append(x);lo=x;total-=x;k-=1
    assert r==total==0
    return tuple(answer)


def rank(xs,hi,total):
    r=0;lo=0;k=len(xs)
    for x in xs:
        r+=sum(count(k-1,y,hi,total-y) for y in range(lo,x))
        total-=x;lo=x;k-=1
    assert total==0
    return r


def primitives(e):
    active=sum(1<<i for i,x in enumerate(e) if x)
    zero=[]
    for m in range(1,1<<8):
        if m&active==m and sum(e[i] for i in range(8) if m>>i&1)==0:zero.append(m)
    atoms=[m for m in zero if not any(s!=m and s&m==s for s in zero)]
    return active,atoms


def component_options(e,m,budget):
    """One witness per occupied label mask; later pieces see only labels."""
    ids=tuple(i for i in range(8) if m>>i&1);out={}
    def visit(left,s,points,origins,owners,coords):
        budget.add('nodes')
        if not left:
            assert s==0
            for b in range(28):
                if not origins>>b&1:continue
                selected={i:b+x for i,x in zip(owners,coords)}
                labels=sum(1<<min(x,27-x) for x in selected.values())
                assert labels.bit_count()==len(ids)
                out.setdefault(labels,selected)
            return
        mask=extend(origins,s,points)
        if not mask:return
        seen=set()
        for i in sorted(left,key=lambda i:(-abs(e[i]),e[i],i)):
            if e[i] in seen or (owners and s*e[i]>=0):continue
            seen.add(e[i])
            visit(tuple(j for j in left if j!=i),s+e[i],points+(s,),mask,
                  owners+(i,),coords+(s,))
    visit(ids,0,(),ALL,(),())
    return out


def reference_options(e,m,budget):
    ids=tuple(i for i in range(8) if m>>i&1);out={}
    for word in sorted(set(permutations(e[i] for i in ids))):
        budget.add('reference_words');s=0;xs=[];valid=True
        for k,x in enumerate(word):
            if k and s*x>=0:valid=False;break
            xs.append(s);s+=x
        if not valid:continue
        assert s==0 and len(set(xs))==len(xs)
        for b in range(max(0,-min(xs)),min(27,27-max(xs))+1):
            budget.add('reference_roots')
            labels=[min(b+x,27-b-x) for x in xs]
            if len(set(labels))==len(ids):out[tuple(word),b]=frozenset(labels)
    # Compare the full placement sets needed by packing, independently of
    # the selected representative for a repeated value or repeated label set.
    return {sum(1<<x for x in labels) for labels in out.values()}


def reference_pack(e,atoms,maps):
    active={i for i,x in enumerate(e) if x}
    pieces=[(frozenset(i for i in range(8) if m>>i&1),
             [frozenset(i for i in range(14) if mask>>i&1) for mask in maps[m]])
            for m in atoms]
    def go(left,used):
        if not left:return True
        pivot=min(left)
        for owners,placements in pieces:
            if pivot in owners and owners<=left:
                for labels in placements:
                    if used.isdisjoint(labels) and go(left-owners,used|labels):return True
        return False
    return go(active,frozenset())


def solve(t,budget,independent=False):
    if any(x%2 for x in t):return dict(status='OUTSIDE_CARDINALITY_CLASS')
    _,h,e=setup(t)
    for i,x in enumerate(e):
        for j,y in enumerate(e):
            if x==y and x:assert h[i]==h[j]
    active,atoms=primitives(e);maps={};reference={};failed=set()
    def options(m):
        if m not in maps:maps[m]=component_options(e,m,budget)
        return maps[m]
    if independent:
        for m in atoms:
            assert set(options(m))==reference_options(e,m,budget)
            reference[m]=set(maps[m])
        budget.counts['independent_component_maps']+=len(atoms)
    def pack(left,used):
        budget.add('nodes')
        if not left:return {}
        if (left,used) in failed:return None
        pivot=left&-left
        for m in sorted(atoms,key=lambda m:(m.bit_count(),m)):
            if not m&pivot or m&left!=m:continue
            for mask,selected in sorted(options(m).items()):
                if mask&used:continue
                rest=pack(left^m,used|mask)
                if rest is not None:return {**selected,**rest}
        failed.add((left,used));return None
    answer=pack(active,0)
    if independent:
        assert (answer is not None)==reference_pack(e,atoms,reference)
        budget.counts['independent_full_packing']+=1
    if answer is None:
        return dict(status='NO_WITNESS_IN_PRIMITIVE_NYCTALOPIC_CLASS',
                    moves=e,primitive_sizes=sorted(m.bit_count() for m in atoms))
    witness=materialize(t,answer)
    assert certificate_ok(witness['bins'],t) and bitset_ok(witness['bins'],t)
    return dict(status='WITNESS',bins=witness['bins'],selected=answer,
                component_sizes=sorted(map(len,witness['cycles'])))


def controls(budget):
    for k in range(1,4):
        for hi in range(5):
            for total in range(k*hi+1):
                direct=[xs for xs in combinations_with_replacement(range(hi+1),k) if sum(xs)==total]
                assert len(direct)==count(k,0,hi,total)
                assert [unrank(k,hi,total,r) for r in range(len(direct))]==direct
                assert [rank(xs,hi,total) for xs in direct]==list(range(len(direct)))
    points=(20,22,0,6,12,17,19,21)
    assert direct_mask(points)==0
    assert min(points)>=0 and max(points)<=27
    translated=list(points)
    assert len(set(translated))==8 and len({min(x,27-x) for x in translated})<8
    t=(98,)*8;budget.local=0;w=solve(t,budget,True)
    assert w['status']=='WITNESS' and len(w['component_sizes'])>1
    _,_,e=setup(t);active,atoms=primitives(e);assert active not in atoms
    bins=[list(b) for b in w['bins']];bins[0][0]=bins[1][0]
    assert not certificate_ok(bins,t) and not bitset_ok(bins,t)
    # Unlike balanced equal targets, this witness has unequal targets, so
    # coverage-preserving exchange is checked against exact assigned sums.
    t=(68,68,68,92,122,122,122,122);budget.local=0;w=solve(t,budget,True)
    assert w['status']=='WITNESS'
    bins=[set(b) for b in w['bins']];x=min(bins[0]);y=min(bins[2])
    bins[0].remove(x);bins[2].remove(y);bins[0].add(y);bins[2].add(x)
    assert not certificate_ok(bins,t) and not bitset_ok(bins,t)
    assert solve((97,97,98,98,98,98,98,100),budget)['status']=='OUTSIDE_CARDINALITY_CLASS'


def main():
    budget=Budget();controls(budget);groups=[]
    for name,hi,total,step,seed,N in [('even',27,120,2,20261016,326119),
                                    ('all',54,240,1,20261017,24688633)]:
        assert count(8,0,hi,total)==gaussian_coefficients(8,hi,total)[total]==N
        ranks=random.Random(seed).sample(range(N),2000);rows=[];statuses=Counter();types=Counter()
        for number,r in enumerate(ranks):
            budget.local=0;xs=unrank(8,hi,total,r);assert rank(xs,hi,total)==r
            t=tuple(68+step*x for x in xs)
            assert sum(t)==784 and list(t)==sorted(t)
            try:result=solve(t,budget,name=='even' and number<12)
            except Cap as cap:result=dict(status='UNKNOWN',cap=str(cap))
            result.update(rank=r,targets=t,nodes=budget.local);rows.append(result)
            statuses[result['status']]+=1
            if all(x%2==0 for x in t):
                _,_,e=setup(t);types[(sum(x<0 for x in e),result['status'])]+=1
            if result.get('cap') not in (None,'target_nodes'):break
        groups.append(dict(name=name,seed=seed,total_domain=N,sampled=len(rows),
                           statuses=dict(statuses),by_negative_count={str(k):v for k,v in types.items()},
                           rows=rows))
        if len(rows)!=2000:break
    print(json.dumps(dict(status='COMPLETE_SAMPLE' if len(groups)==2 and all(g['sampled']==2000 for g in groups) else 'PARTIAL_CAP',
                         preregistration='71c9c265',groups=groups,counts=dict(budget.counts),controls='PASS',
                         cpu_seconds=time.process_time()-budget.start),indent=2))


if __name__=='__main__':main()
