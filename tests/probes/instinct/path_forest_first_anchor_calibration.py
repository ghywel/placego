#!/usr/bin/env python3
"""B68/MI157 prereg11fab479, tie clarification7f541a18.

B57 full2000-rank E28 sample seed20261017, ONLY first split-anchor policy.
No extra anchor/slot/order policy. Forecast>=99%,zero caps; greedy slots1/2.
20k nodes/target,5M global/30CPU sec/256MiB,2M raw words/20M ref roots.
First12 odd full maps/packings independent. Two literal validators plus actual
anchor-removal/shifted-inventory checks on every witness. No universal theorem.
One calibration then a structural decision, not automatic census escalation.
OUTCOME:1996/2000 witnesses,4 FIRST_POLICY_EXHAUSTED,zero cutoffs.59 full
maps/12 packings agree with independent instruments. All1996 reduced pools
check; greedy slot sort agrees on2000.1092 successes have extrema>N;1061
role-boundary target reversals.3.071017CPU sec,29478912bytes peakRSS.
Full raw SHA256 a580dd9bea76765b479d18a9656fb17cc6d28c2ff5ee8e42a9598902e9d4cc3e.
No extra policy attempted; four-target diagnosis follows separately.
"""
from collections import Counter
import json
import random
import resource
import time

import path_forest_split_anchor_pilot as pilot
import path_forest_uniformity as frozen
from path_forest_exceptional_counts import gaussian_coefficients


class Cap(Exception):pass


class Budget:
    def __init__(self):self.start=time.process_time();self.local=0;self.counts=Counter()
    def add(self,key,n=1):
        self.counts[key]+=n
        if key=='nodes':self.local+=n
        if self.local>20000:raise Cap('target_nodes')
        caps={'nodes':5000000,'reference_words':2000000,'reference_roots':20000000}
        if key in caps and self.counts[key]>caps[key]:raise Cap(key)
        if time.process_time()-self.start>30:raise Cap('overall_cpu')
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>256*1024*1024:raise Cap('peak_rss')


def sorted_slots(t,a):
    q=sum(x%2 for x in t);r=6-q//2
    initial=[(x-z-56)//2 for x,z in zip(t,a)]
    ids=sorted(range(8),key=lambda i:(-initial[i],-i if q==0 else i))
    chosen=set(ids[:r]);return [1+int(i in chosen) for i in range(8)]


def reduced_witness(w,t):
    q=sum(x%2 for x in t);N=28-q;a=w['anchors'];h=w['slots']
    reduced=[];T=[]
    for i,bin in enumerate(w['bins']):
        remaining=list(bin)
        if a[i]:remaining.remove(a[i])
        reduced.append([x-q for x in remaining]);T.append(t[i]-a[i]-2*q*h[i])
    assert sorted(x for b in reduced for x in b)==list(range(1,2*N,2))
    assert [sum(b) for b in reduced]==T
    assert [len(b) for b in reduced]==[2*x for x in h]
    assert all(x%2==0 for x in T) and sum(T)==N*N
    assert [(x-2*N*s)//2 for x,s in zip(T,h)]==w['moves']
    shift=q//2;selected={i:int(x)-shift for i,x in w['selected'].items()}
    assert all(0<=x<N for x in selected.values())
    assert len({min(x,N-1-x) for x in selected.values()})==len(selected)
    assert Counter(selected.values())==Counter(x+w['moves'][int(i)] for i,x in selected.items())
    return dict(N=N,targets=T,bins=reduced,selected=selected)


def controls():
    hand=pilot.controls()
    for t in ((98,)*8,(97,97,98,98,98,98,98,100)):
        R,a,h=next(pilot.policies(t));assert h==sorted_slots(t,a)
    removed={1,3,5,51,53,55}
    assert [x-6 for x in range(1,56,2) if x not in removed]==list(range(1,44,2))
    assert [x-6 for x in range(1,56,2) if x not in removed-{55}]!=list(range(1,44,2))
    return hand


def main():
    budget=Budget();hand=controls();N=frozen.count(8,0,54,240)
    assert N==gaussian_coefficients(8,54,240)[240]==24688633
    ranks=random.Random(20261017).sample(range(N),2000)
    rows=[];strata=Counter();stats=Counter();odd_seen=0;first_reversal=None
    for rank in ranks:
        budget.local=0;xs=frozen.unrank(8,54,240,rank);assert frozen.rank(xs,54,240)==rank
        t=tuple(68+x for x in xs);q=sum(x%2 for x in t)
        R,a,h=next(pilot.policies(t));assert h==sorted_slots(t,a)
        assert all(x in (1,2) for x in h) and h.count(2)==6-q//2
        if q:odd_seen+=1
        if any(c*c>x or x>c*(56-c) for c,x in zip([2*s+x%2 for s,x in zip(h,t)],t)):
            w=dict(status='SIZE_BOUND_REJECTED',reserved=sorted(R),anchors=a,slots=h)
        else:
            try:w=pilot.attempt(t,R,a,h,budget,bool(q and odd_seen<=12))
            except Cap as cap:w=dict(status='UNKNOWN',cap=str(cap),reserved=sorted(R),anchors=a,slots=h)
        if w['status']=='WITNESS':
            reduced=reduced_witness(w,t);w['reduced']=reduced
            stats['witness_extrema_gt_effective_pool']+=w['extrema_sum']>28-q
            stats['witness_extrema_gt28']+=w['extrema_sum']>28
            low=max((i for i in range(8) if h[i]==1),key=lambda i:(t[i]-a[i],i))
            high=min((i for i in range(8) if h[i]==2),key=lambda i:(t[i]-a[i],i))
            reversed_boundary=reduced['targets'][low]>reduced['targets'][high]
            stats['role_boundary_target_reversals']+=reversed_boundary
            if reversed_boundary and first_reversal is None:
                first_reversal=dict(rank=rank,targets=t,anchors=a,slots=h,low_bin=low,high_bin=high,
                                    reduced_targets=reduced['targets'])
        elif w['status']=='NO_WITNESS_THIS_POLICY':w['status']='FIRST_POLICY_EXHAUSTED'
        w.update(rank=rank,targets=t,odd_bins=q,nodes=budget.local)
        rows.append(w);strata[q,w['status']]+=1
        if w.get('cap') not in (None,'target_nodes'):break
    forecasts=dict(at_least99percent=100*sum(r['status']=='WITNESS' for r in rows)>=99*len(rows),
                   zero_caps=all(r['status']!='UNKNOWN' for r in rows),all_slots_one_two=True)
    print(json.dumps(dict(status='COMPLETE_CALIBRATION' if len(rows)==2000 else 'PARTIAL_CAP',
                         preregistration='11fab479',control_clarification='7f541a18',seed=20261017,
                         total_domain=N,sampled=len(rows),statuses=dict(Counter(r['status'] for r in rows)),
                         by_odd_bins={str(k):v for k,v in strata.items()},counts=dict(budget.counts),
                         controls='PASS',hand_fixture=hand,diagnostics=dict(stats),
                         first_reversal=first_reversal,forecasts=forecasts,rows=rows,
                         cpu_seconds=time.process_time()-budget.start,
                         peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),indent=2))


if __name__=='__main__':main()
