#!/usr/bin/env python3
"""B70/MI161 prereg9fd713a3: one hand-selected E28 target, three allocations.

Hand predicts start0/2 no all-order cycle; start4 explicit positive path works.
Full independent all-order maps; opposite-sign maps equal on one-negative slice.
Long-edge existence is insufficient: start2 entry/exit test. No broad sample.
100k nodes/allocation,300k total,200k raw words/5M roots,5CPU sec/128MiB.
OUTCOME:first two maps0,third map12; all3 full maps/packings independent,
all3 opposite-sign maps equal all-order maps. Boundary first/last obstruction
confirms long-edge existence is insufficient.6863nodes,30240raw words,
65520roots,0.379755CPU sec,18214912bytes RSS. Full raw SHA256
0205800cc55c812bebe4618b9db66e02e76ecf3001abc7d8dec19bca712cdf5f.
"""
from collections import Counter
import json
import resource
import time

import path_forest_anchor_failure_audit as audit
import path_forest_split_anchor_pilot as pilot
import path_forest_level_portability as level
import path_forest_uniformity as frozen

TARGET=(69,71,73,109,111,112,118,121)


class Cap(Exception):pass


class Budget:
    def __init__(self):self.start=time.process_time();self.local=0;self.counts=Counter()
    def add(self,key,n=1):
        self.counts[key]+=n
        if key=='nodes':self.local+=n
        if self.local>100000:raise Cap('allocation_nodes')
        caps={'nodes':300000,'reference_words':200000,'reference_roots':5000000}
        if key in caps and self.counts[key]>caps[key]:raise Cap(key)
        if time.process_time()-self.start>5:raise Cap('overall_cpu')
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>128*1024*1024:raise Cap('peak_rss')


def valid_points(points,R):
    if any(x<0 or x>27 for x in points):return False
    labels=[min(x,27-x) for x in points]
    return len(labels)==len(set(labels)) and not set(labels)&R


def boundary_controls():
    R={2,3,4};parts=(4,4,4,3,3,3)
    endpoints=[u for u in range(7) if valid_points((u,u+21),R)]
    assert endpoints==[0,1,5,6]
    rows=[]
    for u in endpoints:
        entries=sorted({v for v in parts if valid_points((u,u+v,u+21),R)})
        exits=sorted({v for v in parts if valid_points((u,u+21-v,u+21),R)})
        rows.append(dict(start=u,end=u+21,allowed_first_steps=entries,allowed_last_steps=exits))
        assert not entries or not exits
    # Formula endpoint-label graph is independent of the physical point validator.
    formula=[u for u in range(7) if u!=6-u and u not in R and 6-u not in R]
    assert formula==endpoints
    assert len({tuple(sorted((u,6-u))) for u in endpoints})==2
    return rows


def main():
    budget=Budget();pilot.controls();boundary=boundary_controls();rows=[]
    policies=list(pilot.policies(TARGET));R,a,h=policies[4]
    expected_a=[9,11,13,43,45,0,0,47];assert a==expected_a
    selected=dict(zip((0,3,4,1,2,6,7),(0,2,7,12,14,16,19)))
    hand=pilot.materialize(TARGET,R,a,h,selected)
    for k in (0,2,4):
        budget.local=0;R,a,h=policies[k]
        try:
            row=audit.audit(TARGET,R,a,h,budget)
            active,components=audit.all_components(row['moves'])
            assert len(components)==1 and components[0]==active
            c=components[0];forbidden=sum(1<<r for r in R)
            known={mask for mask in level.options(row['moves'],c,28,budget) if not mask&forbidden}
            ref={mask for mask in level.reference_options(row['moves'],c,28,budget) if not mask&forbidden}
            assert known==ref==set(row['component_maps'][0]['label_masks'])
            budget.counts['sign_class_complete_comparisons']+=1
            row.update(policy_index=k,nodes=budget.local)
        except Cap as cap:row=dict(policy_index=k,status='UNKNOWN',cap=str(cap),nodes=budget.local)
        rows.append(row)
        if row.get('cap') is not None:break
    status='COMPLETE_THREE_ALLOCATION_AUDIT' if len(rows)==3 and all(r['status']!='UNKNOWN' for r in rows) else 'PARTIAL_CAP'
    forecasts=dict(first_two_fail=len(rows)>=2 and all(r['status']=='NO_WITNESS_ALL_ZERO_COMPONENTS_ALL_ORDERS' for r in rows[:2]),
                   third_succeeds=len(rows)==3 and rows[2]['status']=='WITNESS',
                   sign_class_lossless=budget.counts['sign_class_complete_comparisons']==3,
                   long_edge_insufficient=bool(boundary) and len(rows)>=2 and rows[1]['status']=='NO_WITNESS_ALL_ZERO_COMPONENTS_ALL_ORDERS')
    rank=frozen.rank(tuple(x-68 for x in TARGET),54,240)
    assert tuple(68+x for x in frozen.unrank(8,54,240,rank))==TARGET
    print(json.dumps(dict(status=status,preregistration='9fd713a3',targets=TARGET,rank=rank,
                         boundary_control=boundary,explicit_selected=selected,explicit_bins=hand,
                         rows=rows,counts=dict(budget.counts),forecasts=forecasts,controls='PASS',
                         cpu_seconds=time.process_time()-budget.start,
                         peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),indent=2))


if __name__=='__main__':main()
