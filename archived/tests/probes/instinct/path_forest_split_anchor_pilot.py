#!/usr/bin/env python3
"""B67/MI155 preregisteredaa2cefa4: fixed-policy split-anchor pilot.

128 uniform full E28 ranks seed20261067; <=16 explicit policies, no fallback.
Reserved consecutive cyclic labels at0,2,4,6,8,10,12,13; ascending/reverse
anchor assignment; greedy pair slots; primitive any-first opposite-sign class.
10k nodes/target across policies,1M global/10CPU sec/256MiB,1M raw reference
words/10M roots. Hand fixture/negative controls; first4 odd-policy full maps
and packings independently checked. Failure is policy failure, not model failure.
Raw outside git; no full-domain theorem/novelty claim.
OUTCOME:128/128 certify,125 odd-containing; all FIRST policy, no cutoff.
Later-policy forecast REFUTED; mixed>=50% and all-even forecasts pass.
20 full maps/4 packings independently agree, all128 literal witnesses pass.
11751nodes/max1027,0.250950CPU sec,19804160bytes peakRSS. Full raw SHA256
d162c854c429b676c0372690c24d7f14954b07abef5d09542c66b724fab010e8.
"""
from collections import Counter
import json
import random
import resource
import time

import path_forest_uniformity as frozen
import path_forest_level_portability as level
from path_forest_exceptional_counts import gaussian_coefficients


class Cap(Exception):pass


class Budget:
    def __init__(self):self.start=time.process_time();self.local=0;self.counts=Counter()
    def add(self,key,n=1):
        self.counts[key]+=n
        if key=='nodes':self.local+=n
        if self.local>10000:raise Cap('target_nodes')
        caps={'nodes':1000000,'reference_words':1000000,'reference_roots':10000000}
        if key in caps and self.counts[key]>caps[key]:raise Cap(key)
        if time.process_time()-self.start>10:raise Cap('overall_cpu')
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>256*1024*1024:raise Cap('peak_rss')


def literal_ok(bins,t,h):
    return (len(bins)==8 and sorted(x for b in bins for x in b)==list(range(1,56,2))
            and [sum(b) for b in bins]==list(t)
            and [len(b) for b in bins]==[2*s+x%2 for s,x in zip(h,t)])


def independent_ok(bins,t):
    if len(bins)!=8:return False
    remaining=(1<<28)-1
    for target,bin in zip(t,bins):
        if len(bin)%2!=target%2:return False
        wanted=target
        for token in bin:
            if not isinstance(token,int) or token<1 or token>55 or token%2==0:return False
            bit=1<<((token-1)//2)
            if not remaining&bit:return False
            remaining^=bit;wanted-=token
        if wanted:return False
    return remaining==0


def materialize(t,R,a,h,selected):
    p=[x%2 for x in t];q=sum(p)
    if len(R)!=q//2 or set(x for x in a if x)!={v for r in R for v in (2*r+1,55-2*r)}:
        raise ValueError('anchors do not exactly split reserved pairs')
    if any(bool(a[i])!=bool(p[i]) for i in range(8)):
        raise ValueError('anchor parity ownership')
    assert len(h)==8 and min(h)>=1 and sum(h)==(28-q)//2
    e=[(x-56*s-z)//2 for x,s,z in zip(t,h,a)]
    assert sum(e)==0 and all((x-56*s-z)%2==0 for x,s,z in zip(t,h,a))
    active={i for i,x in enumerate(e) if x};assert set(selected)==active
    xs=list(selected.values());assert all(0<=x<28 for x in xs)
    labels=[min(x,27-x) for x in xs]
    if len(set(labels))!=len(xs) or set(labels)&R:raise ValueError('selected pair reused/reserved')
    ends={i:selected[i]+e[i] for i in active}
    assert Counter(ends.values())==Counter(xs)
    bins=[{x} if x else set() for x in a]
    for i,x in selected.items():bins[i].update((2*x+1,55-2*x))
    free=iter(r for r in range(14) if r not in R and r not in labels)
    for i in range(8):
        while len(bins[i])<2*h[i]+p[i]:
            r=next(free);bins[i].update((2*r+1,55-2*r))
    assert next(free,None) is None
    for i,x in selected.items():bins[i].remove(2*x+1)
    for i,x in ends.items():bins[i].add(2*x+1)
    bins=[sorted(b) for b in bins]
    assert literal_ok(bins,t,h) and independent_ok(bins,t)
    return bins


def policies(t):
    odd=[i for i,x in enumerate(t) if x%2];q=len(odd)
    if not q:yield set(),[0]*8,[1,1]+[2]*6;return
    for offset in (0,2,4,6,8,10,12,13):
        R={(offset+j)%14 for j in range(q//2)}
        tokens=sorted(v for r in R for v in (2*r+1,55-2*r))
        for order in (tokens,tokens[::-1]):
            a=[0]*8
            for i,x in zip(odd,order):a[i]=x
            h=[1]*8
            for _ in range((28-q)//2-8):
                i=max(range(8),key=lambda i:(t[i]-a[i]-56*h[i],-i));h[i]+=1
            yield R,a,h


def attempt(t,R,a,h,budget,independent=False):
    e=[(x-56*s-z)//2 for x,s,z in zip(t,h,a)]
    assert sum(e)==0
    forbidden=sum(1<<r for r in R);active,atoms=frozen.primitives(e);maps={};failed=set()
    def get(c):
        if c not in maps:maps[c]={mask:sel for mask,sel in level.options(e,c,28,budget).items() if not mask&forbidden}
        return maps[c]
    if independent:
        for c in atoms:
            reference={mask for mask in level.reference_options(e,c,28,budget) if not mask&forbidden}
            assert set(get(c))==reference
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
        assert (answer is not None)==level.reference_pack(e,atoms,maps,28)
        budget.counts['independent_full_packing']+=1
    result=dict(reserved=sorted(R),anchors=a,slots=h,moves=e,
                extrema_sum=max(e)+max(-x for x in e),primitive_sizes=sorted(c.bit_count() for c in atoms))
    if answer is None:result['status']='NO_WITNESS_THIS_POLICY'
    else:result.update(status='WITNESS',selected=answer,bins=materialize(t,R,a,h,answer))
    return result


def controls():
    t=(68,69,99,100,112,112,112,112);R={6};a=[0,13,43,0,0,0,0,0];h=[1,1,1,2,2,2,2,2]
    bins=materialize(t,R,a,h,{0:1,3:7})
    try:materialize(t,R,a,h,{0:6,3:12})
    except ValueError as error:assert str(error)=='selected pair reused/reserved'
    else:raise AssertionError('reserved pair accepted')
    bad=list(a);bad[2]=41
    try:materialize(t,R,bad,h,{0:1,3:7})
    except ValueError as error:assert str(error)=='anchors do not exactly split reserved pairs'
    else:raise AssertionError('wrong anchors accepted')
    corrupt=[list(b) for b in bins];corrupt[0][0]=corrupt[1][0]
    assert not literal_ok(corrupt,t,h) and not independent_ok(corrupt,t)
    corrupt=[set(b) for b in bins];x=min(corrupt[0]);y=min(corrupt[1]);assert x!=y
    corrupt[0].remove(x);corrupt[1].remove(y);corrupt[0].add(y);corrupt[1].add(x)
    assert sorted(x for b in corrupt for x in b)==list(range(1,56,2))
    assert not literal_ok(corrupt,t,h) and not independent_ok(corrupt,t)
    return dict(targets=t,reserved=sorted(R),anchors=a,slots=h,selected={0:1,3:7},bins=bins)


def main():
    budget=Budget();hand=controls();N=frozen.count(8,0,54,240)
    assert N==gaussian_coefficients(8,54,240)[240]==24688633
    ranks=random.Random(20261067).sample(range(N),128)
    rows=[];strata=Counter();statuses=Counter();odd_seen=0
    for rank in ranks:
        budget.local=0;xs=frozen.unrank(8,54,240,rank);assert frozen.rank(xs,54,240)==rank
        t=tuple(68+x for x in xs);q=sum(x%2 for x in t);attempts=[];cutoff=None
        if q:odd_seen+=1
        try:
            for k,(R,a,h) in enumerate(policies(t)):
                c=[2*s+x%2 for s,x in zip(h,t)]
                if any(n*n>x or x>n*(56-n) for n,x in zip(c,t)):
                    attempts.append(dict(status='SIZE_BOUND_REJECTED',reserved=sorted(R),anchors=a,slots=h));continue
                r=attempt(t,R,a,h,budget,bool(q and odd_seen<=4 and k==0));attempts.append(r)
                if r['status']=='WITNESS':break
        except Cap as cap:cutoff=str(cap)
        status='UNKNOWN' if cutoff else ('WITNESS' if attempts[-1]['status']=='WITNESS' else 'POLICY_EXHAUSTED')
        rows.append(dict(rank=rank,targets=t,odd_bins=q,status=status,cap=cutoff,nodes=budget.local,attempts=attempts))
        strata[q,status]+=1;statuses[status]+=1
        if cutoff not in (None,'target_nodes'):break
    mixed=[r for r in rows if r['odd_bins']];even=[r for r in rows if not r['odd_bins']]
    successes=[r for r in mixed if r['status']=='WITNESS']
    forecasts=dict(at_least_half_mixed=2*len(successes)>=len(mixed),
                   all_even=all(r['status']=='WITNESS' for r in even),
                   later_policy_needed=any(len(r['attempts'])>1 for r in successes))
    print(json.dumps(dict(status='COMPLETE_PILOT' if len(rows)==128 else 'PARTIAL_CAP',preregistration='aa2cefa4',
                         total_domain=N,seed=20261067,sampled=len(rows),statuses=dict(statuses),
                         by_odd_bins={str(k):v for k,v in strata.items()},mixed_sampled=len(mixed),
                         mixed_witnesses=len(successes),even_sampled=len(even),forecasts=forecasts,
                         counts=dict(budget.counts),controls='PASS',hand_fixture=hand,rows=rows,
                         cpu_seconds=time.process_time()-budget.start,
                         peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),indent=2))


if __name__=='__main__':main()
