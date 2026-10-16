#!/usr/bin/env python3
"""B39/B40 MI094-095, preregistered 36aff500, 2026-10-16.

Seven-position span16 obstruction; three-surplus q15 slice with top four
112,122,122,122. Predict72 inputs from three domains and all certified by
one fixed two-ended architecture, at most18 shapes/input. Allocate two5
moves to W and one5 to Z when Z>5; otherwise all15 to W. Ordinary parent
has two alternating orders; paired parent relative root1/2/3. All before/
after cuts only, no arbitrary-cycle/role search. Retain failed targets and
stop without widening. Caps120 targets/2160 candidates/five CPU seconds.
Independent displacement and whole-odd checks; invalid parent, wrong-sign,
coverage-preserving wrong-sum, span16 and point-deletion controls.
OUTCOME: 72 inputs agree across three domains;71 certify, one fixed-class
failure (u,v,W,Z)=(6,6,21,6), all12 attempts repeated a coordinate.
One other target needs the second cut.84 attempts:71 translated/13 duplicate,
no distinct reflection failure.8 targets reject all15-on-W parent; controls
pass. CPU0.013354 s. Raw outside git SHA256
f7a72f0689d567a766c020d0decb14edecab32222384b520fa7b611a92d92384.
Blind all72 prediction REFUTED; class stopped, no widening.
"""
from collections import Counter
from itertools import combinations_with_replacement,product
import json
import time
from path_forest_cycle_cover import setup,materialize
from path_forest_receiving_chains import certificate_ok
from path_forest_six_translation import roots,sum_roots


def target_for(u,v,W,Z):
    return (56+2*u,56+2*v,112-2*W,112-2*Z,112,122,122,122)


def domains():
    param={}
    for u in range(6,15):
        for v in range(u,18):
            total=u+v+15
            for W in range((total+1)//2,min(22,28-v,total-1)+1):
                Z=total-W;t=target_for(u,v,W,Z)
                assert t==tuple(sorted(t)) and t[3]<112
                param[t]=(u,v,W,Z)
    direct={low+(112,122,122,122) for low in
            combinations_with_replacement(range(68,111,2),4) if sum(low)==306}
    assert set(param)==direct
    dp=[[0]*18 for _ in range(5)];dp[0][0]=1
    for r in range(22):
        for k in range(1,5):
            for s in range(r,18):dp[k][s]+=dp[k-1][s-r]
    assert len(param)==dp[4][17]==72
    return param


def parent_shapes(u,v,R,S):
    if sorted((R,S))==[u,v]:
        first=2 if R==u else 3;second=5-first
        for d in (1,2,3):
            yield {0:0,first:u,1:d,second:d+v},f'paired{d}'
    else:
        large=2 if R>=S else 3;small=5-large;L=max(R,S);H=min(R,S)
        yield {1:0,small:v,0:v-H,large:L},'alternating_v'
        yield {0:0,small:u,1:u-H,large:L},'alternating_u'


def subdivide(base,R,S,groups,cuts):
    selected=dict(base)
    for negative,steps in groups.items():
        before=cuts[negative];x=base[negative];y=x-({2:R,3:S}[negative])
        current=x
        for i,step in steps[:before]:selected[i]=current;current+=step
        selected[negative]=current
        current=y-sum(step for i,step in steps[before:])
        for i,step in steps[before:]:selected[i]=current;current+=step
        assert current==y
    m=min(selected.values());return {i:x-m for i,x in selected.items()}


def main():
    start=time.process_time();family=domains();sharp=(0,5,7,8,9,11,16)
    assert roots(sharp)==sum_roots(sharp)==[]
    assert {x+y for x in sharp for y in sharp if x<y and (x+y)%2}==set(range(5,28,2))
    for i in range(7):assert roots(sharp[:i]+sharp[i+1:])
    results=[];failures=[];candidate_count=0;stats=Counter();both_needed=0
    for t,p in sorted(family.items()):
        u,v,W,Z=p
        if W<=15:
            both_needed+=1;assert W-15<=0
        if Z>5:
            R,S=W-10,Z-5;groups={2:[(6,5),(7,5)],3:[(5,5)]}
        else:R,S=W-15,Z;groups={2:[(5,5),(6,5),(7,5)]}
        assert R>0 and S>0 and R+S==u+v
        pe={0:u,1:v,2:-R,3:-S};_,_,e=setup(t);attempts=[];found=None
        for base,branch in parent_shapes(u,v,R,S):
            assert len(set(base.values()))==4
            assert Counter(x+pe[i] for i,x in base.items())==Counter(base.values())
            keys=list(groups)
            for values in product(*(range(len(groups[i])+1) for i in keys)):
                if len(results)>=120 or candidate_count>=2160 or time.process_time()-start>=5:
                    print(json.dumps(dict(status='UNKNOWN',completed=len(results))));return
                cuts=dict(zip(keys,values));s=subdivide(base,R,S,groups,cuts);candidate_count+=1
                assert Counter(x+e[i] for i,x in s.items())==Counter(s.values())
                distinct=len(set(s.values()))==7;r=roots(tuple(s.values())) if distinct else []
                key='duplicate' if not distinct else 'reflection_blocked' if not r else 'translated'
                stats[key]+=1
                attempt=dict(branch=branch,cuts=cuts,shape=s,span=max(s.values()),status=key,roots=r)
                attempts.append(attempt)
                if r:
                    witness=materialize(t,{i:x+r[0] for i,x in s.items()})
                    assert certificate_ok(witness['bins'],t)
                    found=dict(chosen=attempt,witness=witness);break
            if found:break
        entry=dict(params=p,targets=t,parent_magnitudes=(R,S),attempts=attempts)
        if found:entry.update(found)
        else:failures.append(entry)
        results.append(entry)
    sample=next(x for x in results if 'witness' in x);s=dict(sample['chosen']['shape']);_,_,e=setup(sample['targets'])
    s[2]+=1;assert Counter(x+e[i] for i,x in s.items())!=Counter(s.values())
    bins=[set(x) for x in sample['witness']['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert Counter(x for b in bins for x in b)==Counter(range(1,56,2))
    assert not certificate_ok(bins,sample['targets'])
    print(json.dumps(dict(status='DIAGNOSED',total=len(family),results=results,
        failures=failures,certified=sum('witness' in x for x in results),
        candidate_count=candidate_count,stats=dict(stats),invalid_all_on_W=both_needed,
        controls='PASS',cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
