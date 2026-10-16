#!/usr/bin/env python3
"""B37/MI088 diagnostic, preregistered 08513a02.

Fixed choices only: remove either surplus from either still-negative bin,
then use the B35 abstract parent or its reverse-reflected permutation.
Predict a distinct <=20-span six-point candidate for every two-surplus
target. Retain candidate failures; finish diagnosis if the class fails,
without widening. Independent parameter/direct/DP domain, displacement,
whole-odd checker, involution and wrong-sign/sum controls. Unexpected:
directly classify span21 translation instead of assuming bound necessary.
Caps 5,000 targets / 40,000 candidates / five process CPU seconds.
OUTCOME: all 2,919 targets certify; 3,074 candidate attempts, 129 repeated
positions. The stronger <=20-span prediction fails on seven targets, all
certified at span21. Every observed distinct span21 candidate translated
(33), no reflection-blocked distinct candidate. Controls and three domain
counts agree, CPU 0.694618 s. Raw outside git SHA256
417726155858aa98f6202e180396d2da9c25c986a6a0fca3145f076a26e9b48b.
Finite family COMPUTED; no all-family uniform proof yet adopted.
"""
from collections import Counter
from itertools import combinations_with_replacement
import json
import time
from path_forest_one_surplus_subdivision import abstract
from path_forest_six_translation import roots
from path_forest_cycle_cover import materialize,setup
from path_forest_receiving_chains import certificate_ok


def target_for(u,v,W,Z,a,b):
    return (56+2*u,56+2*v,112-2*W,112-2*Z,112,112,112+2*a,112+2*b)


def domains():
    param={}
    for a in range(1,6):
        for b in range(a,6):
            for u in range(6,15):
                for v in range(u,17):
                    total=u+v+a+b
                    for W in range((total+1)//2,min(22,28-v,total-1)+1):
                        Z=total-W;t=target_for(u,v,W,Z,a,b)
                        assert t==tuple(sorted(t))
                        param[t]=(u,v,W,Z,a,b)
    lows={s:[] for s in range(22,31)}
    for low in combinations_with_replacement(range(68,111,2),4):
        s=(sum(low)-272)//2
        if s in lows:lows[s].append(low)
    direct=set()
    for a in range(1,6):
        for b in range(a,6):
            direct.update(low+(112,112,112+2*a,112+2*b) for low in lows[32-a-b])
    assert set(param)==direct
    dp=[[0]*33 for _ in range(5)];dp[0][0]=1
    for r in range(22):
        for k in range(1,5):
            for s in range(r,33):dp[k][s]+=dp[k-1][s-r]
    counts=Counter((p[-2],p[-1]) for p in param.values())
    assert all(counts[a,b]==dp[4][32-a-b] for a,b in counts)
    assert len(param)==sum(dp[4][32-a-b] for a in range(1,6) for b in range(a,6))
    return param


def normalize(s):
    m=min(s.values());return {i:x-m for i,x in s.items()}


def inverse(s,e):
    return normalize({i:-x-e[i] for i,x in s.items()})


def candidate(params,insert,negative,reverse):
    u,v,W,Z,a,b=params;surplus=(a,b);c=surplus[insert];other=surplus[1-insert]
    magnitudes=[W,Z]
    if magnitudes[negative]<=c:return None
    magnitudes[negative]-=c
    L,S=sorted(magnitudes,reverse=True)
    base,branch,_=abstract((u,v,L,S,other))
    pe={0:u,1:v,2:-L,3:-S,7:other}
    assert inverse(inverse(base,pe),pe)==base
    if reverse:base=inverse(base,pe)
    large_actual=2 if magnitudes[0]>=magnitudes[1] else 3
    mapping={0:0,1:1,2:large_actual,3:5-large_actual,7:7-insert}
    selected={mapping[i]:x for i,x in base.items()}
    old=selected[2+negative];selected[6+insert]=old;selected[2+negative]=old+c
    selected=normalize(selected);target=target_for(*params);_,_,e=setup(target)
    assert Counter(x+e[i] for i,x in selected.items())==Counter(selected.values())
    distinct=len(set(selected.values()))==6
    r=roots(tuple(selected.values())) if distinct else []
    return dict(choice=(insert,negative,reverse),branch=branch,shape=selected,
                distinct=distinct,span=max(selected.values()),roots=r)


def main():
    start=time.process_time();family=domains();results=[];failures=[];candidate_count=0
    statuses=Counter();long=Counter();branches=Counter();span21=[]
    for t,p in sorted(family.items()):
        if len(results)>=5000 or candidate_count>=40000 or time.process_time()-start>=5:
            print(json.dumps(dict(status='UNKNOWN',completed=len(results))));return
        attempts=[];best=None;fallback=None
        for insert in (0,1):
            for negative in (0,1):
                for reverse in (False,True):
                    q=candidate(p,insert,negative,reverse)
                    if q is None:continue
                    candidate_count+=1;attempts.append(q)
                    key='duplicate' if not q['distinct'] else 'translated' if q['roots'] else 'reflection_blocked'
                    statuses[key]+=1
                    if q['distinct'] and q['span']>20:
                        long[f"{q['span']}:{bool(q['roots'])}"]+=1
                        if q['span']==21:span21.append(dict(params=p,attempt=q))
                    if q['roots']:
                        if fallback is None:fallback=q
                        if q['span']<=20:best=q;break
                if best:break
            if best:break
        chosen=best or fallback
        entry=dict(params=p,targets=t,attempts=attempts,prediction_met=best is not None)
        if chosen:
            s={i:x+chosen['roots'][0] for i,x in chosen['shape'].items()}
            witness=materialize(t,s);assert certificate_ok(witness['bins'],t)
            entry.update(chosen=chosen,witness=witness);branches[chosen['branch']]+=1
        if not best:failures.append(dict(params=p,targets=t,certified=chosen is not None,attempts=attempts))
        results.append(entry)
    sample=next(x for x in results if 'witness' in x)
    selected=sample['witness']['selected'];_,_,e=setup(sample['targets'])
    wrong=dict(selected);wrong[2]+=1
    assert Counter(x+e[i] for i,x in wrong.items())!=Counter(wrong.values())
    bins=[set(x) for x in sample['witness']['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert Counter(x for b in bins for x in b)==Counter(range(1,56,2))
    assert not certificate_ok(bins,sample['targets'])
    print(json.dumps(dict(status='DIAGNOSED',total=len(family),results=results,
        prediction_failures=failures,candidate_count=candidate_count,statuses=dict(statuses),
        long_shapes=dict(long),span21=span21,branches=dict(branches),
        certified=sum('witness' in x for x in results),controls='PASS',
        cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
