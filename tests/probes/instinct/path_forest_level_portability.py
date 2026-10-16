#!/usr/bin/env python3
"""B65/MI151 preregistered6c776421: even exchange at token levels26/30.

2000 distinct uniform ranks each; seeds20261026/30. Same B57 primitive,
any-first opposite-sign class, fixed level-derived slots. No exception repair.
95%/99% witness forecasts, strict higher rate30.20k nodes/target,4M global,
30CPU seconds/256MiB,4M raw reference words/20M roots. First12 each full
independent maps and packing; two literal validators; frozen28 status control.
Counts/sampling not a universal theorem. Raw outside git. See MI151 for controls.
OUTCOME:2000/2000 each level certify;119 full maps/24 packings agree with
independent instruments; all4000 partitions pass both literal validators.
539318 nodes, maxima2576/4918,6.265620CPU seconds,27189248bytes peakRSS.
95%/99% forecasts pass; strict higher observed rate30 REFUTED by tie.
Full raw SHA256 998c17b7602ead4830197d887b1715bb0aad5972857300d77def49b202d765b2.
"""
from collections import Counter
from itertools import permutations, combinations_with_replacement
import json
import random
import resource
import sys
import time

import path_forest_uniformity as frozen
from path_forest_exceptional_counts import gaussian_coefficients


class Cap(Exception):
    pass


class Budget:
    def __init__(self):
        self.start=time.process_time();self.local=0;self.counts=Counter()
    def add(self,key,n=1):
        self.counts[key]+=n
        if key=='nodes':self.local+=n
        if self.local>20000:raise Cap('target_nodes')
        limits={'nodes':4000000,'reference_words':4000000,'reference_roots':20000000}
        if key in limits and self.counts[key]>limits[key]:raise Cap(key)
        if time.process_time()-self.start>30:raise Cap('overall_cpu')
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>256*1024*1024:
            raise Cap('peak_rss')


def setup(t,m):
    assert m in (26,28,30) and len(t)==8 and list(t)==sorted(t)
    assert sum(t)==m*m and all(68<=x<=66+2*m and x%2==0 for x in t)
    h=[1]*(16-m//2)+[2]*(m//2-8)
    assert len(h)==8 and sum(h)==m//2
    e=[(x-2*m*s)//2 for x,s in zip(t,h)]
    assert sum(e)==0
    return h,e


def sorted_ok(bins,t,m):
    if len(bins)!=8:return False
    h=[1]*(16-m//2)+[2]*(m//2-8)
    return (sorted(x for b in bins for x in b)==list(range(1,2*m,2))
            and [sum(b) for b in bins]==list(t)
            and [len(b) for b in bins]==[2*s for s in h])


def inventory_ok(bins,t,m):
    # Independent slot derivation and literal subtraction; no fold helper.
    if len(bins)!=8:return False
    inventory=(1<<m)-1;singles=16-m//2
    for i,b in enumerate(bins):
        if len(b)!=(2 if i<singles else 4):return False
        remaining=t[i]
        for x in b:
            if not isinstance(x,int) or not 1<=x<2*m or x%2==0:return False
            bit=1<<((x-1)//2)
            if not inventory&bit:return False
            inventory^=bit;remaining-=x
        if remaining:return False
    return inventory==0


def materialize(t,selected,m):
    h,e=setup(t,m);active={i for i,x in enumerate(e) if x}
    assert set(selected)==active
    xs=list(selected.values());assert all(0<=x<m for x in xs)
    labels=[min(x,m-1-x) for x in xs]
    assert len(set(labels))==len(xs)
    ends={i:selected[i]+e[i] for i in active}
    assert Counter(ends.values())==Counter(xs)
    bins=[set() for _ in range(8)]
    for i,x in selected.items():bins[i]={2*x+1,2*m-1-2*x}
    free=iter(p for p in range(m//2) if p not in set(labels))
    for i in range(8):
        while len(bins[i])<2*h[i]:
            p=next(free);bins[i].update((2*p+1,2*m-1-2*p))
    assert next(free,None) is None
    for i,x in selected.items():bins[i].remove(2*x+1)
    for i,x in ends.items():bins[i].add(2*x+1)
    answer=[sorted(b) for b in bins]
    assert sorted_ok(answer,t,m) and inventory_ok(answer,t,m)
    return answer


def extend(mask,p,earlier,m):
    if p in earlier:return 0
    lo=max(0,-p);hi=min(m-1,m-1-p)
    if lo>hi:return 0
    mask&=((1<<(hi-lo+1))-1)<<lo
    for q in earlier:
        n=m-1-p-q
        if n%2==0 and 0<=n//2<m:mask&=~(1<<(n//2))
    return mask


def direct_origins(points,m):
    return {r for r in range(m)
            if all(0<=r+p<m for p in points)
            and len({min(r+p,m-1-r-p) for p in points})==len(points)}


def options(e,component,m,budget):
    ids=tuple(i for i in range(8) if component>>i&1);out={}
    def visit(left,s,points,origins,owners):
        budget.add('nodes')
        if not left:
            assert s==0
            for r in range(m):
                if not origins>>r&1:continue
                selected={i:r+x for i,x in zip(owners,points)}
                mask=sum(1<<min(x,m-1-x) for x in selected.values())
                assert mask.bit_count()==len(ids)
                out.setdefault(mask,selected)
            return
        origins=extend(origins,s,points,m)
        if not origins:return
        seen=set()
        for i in sorted(left,key=lambda i:(-abs(e[i]),e[i],i)):
            if e[i] in seen or (owners and s*e[i]>=0):continue
            seen.add(e[i])
            visit(tuple(j for j in left if j!=i),s+e[i],points+(s,),origins,owners+(i,))
    visit(ids,0,(),(1<<m)-1,())
    return out


def reference_options(e,component,m,budget):
    # Full raw permutations with duplicate words skipped only after counting.
    values=tuple(e[i] for i in range(8) if component>>i&1)
    seen=set();out=set()
    for word in permutations(values):
        budget.add('reference_words')
        if word in seen:continue
        seen.add(word);s=0;points=[]
        for k,x in enumerate(word):
            if k and s*x>=0:break
            points.append(s);s+=x
        else:
            assert s==0 and len(set(points))==len(values)
            for r in range(m):
                budget.add('reference_roots')
                physical=[r+x for x in points]
                if any(x<0 or x>=m for x in physical):continue
                pairs={frozenset((x,m-1-x)) for x in physical}
                if len(pairs)==len(values):
                    out.add(sum(1<<min(pair) for pair in pairs))
    return out


def reference_pack(e,atoms,maps,m):
    pieces=[(set(i for i in range(8) if c>>i&1),
             [set(i for i in range(m//2) if mask>>i&1) for mask in maps[c]])
            for c in atoms]
    def go(left,used):
        if not left:return True
        pivot=min(left)
        return any(go(left-owners,used|labels)
                   for owners,placements in pieces if pivot in owners and owners<=left
                   for labels in placements if used.isdisjoint(labels))
    return go({i for i,x in enumerate(e) if x},set())


def solve(t,m,budget,independent=False):
    h,e=setup(t,m)
    assert max(e,default=0)+max((-x for x in e),default=0)<=m
    assert not ({x for x,s in zip(e,h) if s==1}&{x for x,s in zip(e,h) if s==2})
    active,atoms=frozen.primitives(e);maps={};failed=set()
    def get(c):
        if c not in maps:maps[c]=options(e,c,m,budget)
        return maps[c]
    if independent:
        for c in atoms:
            assert set(get(c))==reference_options(e,c,m,budget)
            budget.counts['independent_component_maps']+=1
    def pack(left,used):
        budget.add('nodes')
        if not left:return {}
        if (left,used) in failed:return None
        pivot=left&-left
        for c in sorted(atoms,key=lambda c:(c.bit_count(),c)):
            if not c&pivot or c&left!=c:continue
            for mask,selected in sorted(get(c).items()):
                if mask&used:continue
                rest=pack(left^c,used|mask)
                if rest is not None:return {**selected,**rest}
        failed.add((left,used));return None
    answer=pack(active,0)
    if independent:
        assert (answer is not None)==reference_pack(e,atoms,maps,m)
        budget.counts['independent_full_packing']+=1
    if answer is None:return dict(status='NO_WITNESS_IN_PRIMITIVE_NYCTALOPIC_CLASS',moves=e)
    return dict(status='WITNESS',selected=answer,bins=materialize(t,answer,m),moves=e)


def controls(budget):
    for k in range(1,4):
        for hi in range(5):
            for total in range(k*hi+1):
                direct=[x for x in combinations_with_replacement(range(hi+1),k) if sum(x)==total]
                assert frozen.count(k,0,hi,total)==len(direct)
                assert [frozen.unrank(k,hi,total,r) for r in range(len(direct))]==direct
                assert [frozen.rank(x,hi,total) for x in direct]==list(range(len(direct)))
    for m in (26,30):
        assert sum([1,1]+[2]*6)!=m//2
        mask=(1<<m)-1;points=()
        for p in (0,3,-4,7):
            mask=extend(mask,p,points,m);points+=(p,)
            assert {r for r in range(m) if mask>>r&1}==direct_origins(points,m)
    assert 0 not in direct_origins((0,25),26)
    assert len({min(x,27-x) for x in (0,25)})==2
    oldbudget=frozen.Budget()
    for j in range(24):
        r=j*(326119-1)//23
        t=tuple(68+2*x for x in frozen.unrank(8,27,120,r))
        oldbudget.local=0;budget.local=0
        assert solve(t,28,budget)['status']==frozen.solve(t,oldbudget)['status']
    budget.counts['frozen_m28_status_checks']=24


def main():
    budget=Budget();groups=[]
    try:
        controls(budget)
        for m in (26,30):
            hi=m-1;total=(m*m-544)//2
            N=frozen.count(8,0,hi,total)
            assert N==gaussian_coefficients(8,hi,total)[total]
            ranks=random.Random(20261000+m).sample(range(N),2000)
            rows=[];statuses=Counter();strata=Counter()
            for number,r in enumerate(ranks):
                budget.local=0
                xs=frozen.unrank(8,hi,total,r);assert frozen.rank(xs,hi,total)==r
                t=tuple(68+2*x for x in xs)
                try:result=solve(t,m,budget,number<12)
                except Cap as cap:result=dict(status='UNKNOWN',cap=str(cap))
                result.update(rank=r,targets=t,nodes=budget.local)
                if result['status']=='WITNESS' and number==0:
                    bins=[list(b) for b in result['bins']];bins[0][0]=bins[1][0]
                    assert not sorted_ok(bins,t,m) and not inventory_ok(bins,t,m)
                    bins=[set(b) for b in result['bins']];i,j=0,7
                    x=min(bins[i]);y=min(bins[j]);assert x!=y
                    bins[i].remove(x);bins[j].remove(y);bins[i].add(y);bins[j].add(x)
                    assert sorted(x for b in bins for x in b)==list(range(1,2*m,2))
                    assert not sorted_ok(bins,t,m) and not inventory_ok(bins,t,m)
                rows.append(result);statuses[result['status']]+=1
                _,e=setup(t,m);strata[(sum(x<0 for x in e),result['status'])]+=1
                if result.get('cap') not in (None,'target_nodes'):break
            groups.append(dict(m=m,seed=20261000+m,total_domain=N,sampled=len(rows),
                               statuses=dict(statuses),by_negatives={str(k):v for k,v in strata.items()},rows=rows))
            if len(rows)!=2000:break
        status='COMPLETE_SAMPLE' if len(groups)==2 and all(g['sampled']==2000 for g in groups) else 'PARTIAL_CAP'
    except Cap as cap:status='CONTROL_CAP_'+str(cap)
    print(json.dumps(dict(status=status,preregistration='6c776421',groups=groups,
                         counts=dict(budget.counts),controls='PASS' if groups else 'INCOMPLETE',
                         cpu_seconds=time.process_time()-budget.start,
                         peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),indent=2))


if __name__=='__main__':main()
