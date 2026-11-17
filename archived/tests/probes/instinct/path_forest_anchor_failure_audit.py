#!/usr/bin/env python3
"""B69/MI159 prereg984b5a18: four exceptions, no broad sample.

ALL zero components/arbitrary orders at first policy, complete independent
label maps+packing. Explicit merged8 hand prediction; <=15 frozen repair
policies on other3, opposite-sign primitive class.250k nodes/target,1M global,
2M raw ref words/20M roots,10CPU sec/256MiB. No cap/target/policy expansion.
OUTCOME:3 all-order original allocations exhausted;24592715 has merged8
(primitive6 map0,8 map4). Other3 fail reverse then pass reserved start2.
18 all-order maps/4 packings and13 repair maps/6 packings independently agree.
73009nodes,216094raw words,880376roots,4.018391CPU sec,21086208bytes RSS.
All forecasts pass. Post-run delivery_audit checks old1996+4patched witnesses,
no new search; ALL2000 pass both validators. Final raw SHA256
 aff8cb81a6e7355b025ba1d27d9aaeb78a883741df1017a2388862e7d4b9ea21.
"""
from collections import Counter
from itertools import permutations
import json
import resource
import time

import path_forest_split_anchor_pilot as pilot
import path_forest_level_portability as level
import path_forest_uniformity as frozen

CASES=[(16461642,(77,77,83,85,107,117,119,119)),
       (24592715,(90,90,91,91,93,103,111,115)),
       (6321549,(71,73,77,105,107,109,121,121)),
       (2079026,(69,69,75,103,111,116,120,121))]


class Cap(Exception):pass


class Budget:
    def __init__(self):self.start=time.process_time();self.local=0;self.counts=Counter()
    def add(self,key,n=1):
        self.counts[key]+=n
        if key=='nodes':self.local+=n
        if self.local>250000:raise Cap('target_nodes')
        caps={'nodes':1000000,'reference_words':2000000,'reference_roots':20000000}
        if key in caps and self.counts[key]>caps[key]:raise Cap(key)
        if time.process_time()-self.start>10:raise Cap('overall_cpu')
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>256*1024*1024:raise Cap('peak_rss')


def all_components(e):
    active=sum(1<<i for i,x in enumerate(e) if x)
    masks=[m for m in range(1,256) if m&active==m and sum(e[i] for i in range(8) if m>>i&1)==0]
    # Independent recursive indexed subsets, no mask sum loop.
    def subsets(i,s,mask):
        if i==8:return [mask] if mask and s==0 else []
        out=subsets(i+1,s,mask)
        if e[i]:out+=subsets(i+1,s+e[i],mask|(1<<i))
        return out
    assert set(masks)==set(subsets(0,0,0))
    return active,masks


def options_any(e,c,R,budget):
    ids=tuple(i for i in range(8) if c>>i&1);out={};forbidden=sum(1<<r for r in R)
    def visit(left,s,points,origins,owners):
        budget.add('nodes')
        if not left:
            assert s==0
            for r in range(28):
                if not origins>>r&1:continue
                selected={i:r+p for i,p in zip(owners,points)}
                labels=sum(1<<min(x,27-x) for x in selected.values())
                assert labels.bit_count()==len(ids)
                if not labels&forbidden:out.setdefault(labels,selected)
            return
        origins=level.extend(origins,s,points,28)
        if not origins:return
        seen=set()
        for i in sorted(left,key=lambda i:(-abs(e[i]),e[i],i)):
            if e[i] in seen:continue
            seen.add(e[i]);visit(tuple(j for j in left if j!=i),s+e[i],points+(s,),origins,owners+(i,))
    visit(ids,0,(),(1<<28)-1,());return out


def direct_any(e,c,R,budget):
    vals=tuple(e[i] for i in range(8) if c>>i&1);seen=set();out=set()
    for word in permutations(vals):
        budget.add('reference_words')
        if word in seen:continue
        seen.add(word);s=0;points=[]
        for x in word:points.append(s);s+=x
        assert s==0
        if len(set(points))!=len(points):continue
        for r in range(28):
            budget.add('reference_roots');xs=[r+x for x in points]
            if any(x<0 or x>27 for x in xs):continue
            pairs=[frozenset((x,27-x)) for x in xs]
            labels={min(pair) for pair in pairs}
            if len(labels)==len(xs) and labels.isdisjoint(R):out.add(sum(1<<x for x in labels))
    return out


def audit(t,R,a,h,budget):
    e=[(x-z-56*s)//2 for x,z,s in zip(t,a,h)]
    active,components=all_components(e);maps={}
    for c in components:
        maps[c]=options_any(e,c,R,budget)
        assert set(maps[c])==direct_any(e,c,R,budget)
        budget.counts['all_order_component_maps']+=1
    failed=set()
    def pack(left,used):
        budget.add('nodes')
        if not left:return {}
        if (left,used) in failed:return None
        pivot=left&-left
        for c in sorted(components,key=lambda c:(c.bit_count(),c)):
            if not c&pivot or c&left!=c:continue
            for mask,selected in sorted(maps[c].items()):
                if mask&used:continue
                rest=pack(left^c,used|mask)
                if rest is not None:return {**selected,**rest}
        failed.add((left,used));return None
    selected=pack(active,0)
    assert (selected is not None)==level.reference_pack(e,components,maps,28)
    budget.counts['all_order_full_packings']+=1
    result=dict(status='WITNESS' if selected is not None else 'NO_WITNESS_ALL_ZERO_COMPONENTS_ALL_ORDERS',
                moves=e,reserved=sorted(R),anchors=a,slots=h,
                component_maps=[dict(mask=c,owners=[i for i in range(8) if c>>i&1],placements=len(maps[c]),
                                     label_masks=sorted(maps[c])) for c in components])
    if selected is not None:result.update(selected=selected,bins=pilot.materialize(t,R,a,h,selected))
    return result


def hand_candidate():
    t=CASES[1][1];R,a,h=next(pilot.policies(t))
    owners=(3,0,7,1,4,2,6,5);coords=(5,21,10,12,1,17,6,7)
    selected={i:x+3 for i,x in zip(owners,coords)}
    bins=pilot.materialize(t,R,a,h,selected)
    e=[(x-z-56*s)//2 for x,z,s in zip(t,a,h)]
    assert [e[i] for i in owners]==[16,-11,2,-11,16,-11,1,-2]
    assert e[5]+e[7]==0 and sum(e)==0
    assert len(set(coords))==len({min(x,21-x) for x in coords})==8
    return dict(rank=CASES[1][0],owners=owners,effective_positions=coords,selected=selected,bins=bins)



def delivery_audit(base,rows):
    """Post-run verification only: patch the four retained failures, no search."""
    assert base['preregistration']=='11fab479' and base['sampled']==2000
    pending={r['rank'] for r in base['rows'] if r['status']!='WITNESS'}
    assert pending=={r['rank'] for r in rows}
    patches={}
    for r in rows:
        t=r['targets'];w=r['audit'] if r['audit']['status']=='WITNESS' else r['repairs'][-1]
        assert w['status']=='WITNESS'
        patches[r['rank']]=(tuple(t),w)
    checked=0
    for r in base['rows']:
        t=tuple(r['targets'])
        if r['rank'] in patches:
            target,w=patches[r['rank']];assert t==target
        else:w=r;assert w['status']=='WITNESS'
        assert pilot.literal_ok(w['bins'],t,w['slots']) and pilot.independent_ok(w['bins'],t)
        checked+=1
    return dict(checked=checked,unchanged=checked-len(patches),patched=len(patches),
                status='ALL_EXISTING_2000_PARTITIONS_CHECKED_NO_NEW_SEARCH')


def main():
    budget=Budget();pilot.controls();hand=hand_candidate();rows=[]
    for rank,t in CASES:
        budget.local=0;row=dict(rank=rank,targets=t,repairs=[])
        try:
            R,a,h=next(pilot.policies(t));row['audit']=audit(t,R,a,h,budget)
            if rank!=24592715:
                for k,(R,a,h) in enumerate(pilot.policies(t)):
                    if k==0:continue
                    sizes=[2*s+x%2 for s,x in zip(h,t)]
                    if any(c*c>x or x>c*(56-c) for c,x in zip(sizes,t)):
                        r=dict(status='SIZE_BOUND_REJECTED',reserved=sorted(R),anchors=a,slots=h)
                    else:r=pilot.attempt(t,R,a,h,budget,True)
                    r['policy_index']=k;row['repairs'].append(r)
                    if r['status']=='WITNESS':break
        except Cap as cap:row['cap']=str(cap)
        row['nodes']=budget.local;rows.append(row)
        if row.get('cap') not in (None,'target_nodes'):break
    geometric=[r for r in rows if r['rank']!=24592715]
    merged=next((r for r in rows if r['rank']==24592715),None)
    forecasts=dict(three_all_order_failures=len(geometric)==3 and all(r.get('audit',{}).get('status')=='NO_WITNESS_ALL_ZERO_COMPONENTS_ALL_ORDERS' for r in geometric),
                   merged_candidate_works=bool(merged and merged.get('audit',{}).get('status')=='WITNESS'),
                   all_three_repair=len(geometric)==3 and all(r['repairs'] and r['repairs'][-1]['status']=='WITNESS' for r in geometric),
                   changed_reserved_set_needed=any(r['repairs'] and r['repairs'][-1]['status']=='WITNESS' and r['repairs'][-1]['policy_index']>=2 for r in geometric))
    print(json.dumps(dict(status='COMPLETE_FOUR_TARGET_AUDIT' if len(rows)==4 and all('cap' not in r for r in rows) else 'PARTIAL_CAP',
                         preregistration='984b5a18',controls='PASS',hand_candidate=hand,rows=rows,
                         counts=dict(budget.counts),forecasts=forecasts,
                         cpu_seconds=time.process_time()-budget.start,
                         peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),indent=2))


if __name__=='__main__':main()
