#!/usr/bin/env python3
"""B38/MI090 direct two-surplus formula, preregistered a221b287.

Same 2,919 targets as B37, no widened search. Split 4+2 / 3+3 cases,
otherwise a four-move abstract cycle with simultaneous forward/backward
subdivision of -R. Distinctness handled algebraically, six-point span<=20
bound except eight explicit span21 geometries with prescribed roots.
Predict all certificates and controls pass, five process CPU second cap.
Unexpected: extra inverse-geometry exception has a <=20-span B37 witness.
OUTCOME: all 2,919 direct certificates pass. Branches forward1105,
backward620, paired_large305, paired_small265, split_3_3=499,
split_4_2_Wv=125. Exactly eight prescribed span21 geometries. All controls
pass; extra span21 target has B37 span17 witness. CPU 0.481749 s.
Raw outside git SHA256
25a3d75cd7017f257d54d82f6ecba765c689d488889678e9a6e73a7789709aa0.
Hand argument PROOF-SKETCH pending independent review; family COMPUTED.
REVIEW (2026-10-16): MI090 adopted as G309 after Cloud CL422/fde83bd8 carrying read and independent finite implementation; span subcase verified by that complete finite check.
"""
from collections import Counter
import json
import time
from path_forest_two_surplus_subdivision import domains,target_for,normalize
from path_forest_six_translation import roots
from path_forest_cycle_cover import materialize,setup
from path_forest_receiving_chains import certificate_ok

LONG_ROOTS={
    (6,6,21,1,5,5):1,(6,7,21,2,5,5):1,(6,7,21,1,4,5):1,
    (7,7,21,3,5,5):4,(7,7,21,2,4,5):0,(7,7,21,1,3,5):2,
    (7,7,21,1,4,4):1,(11,11,17,15,5,5):1}


def abstract(p,force=None):
    u,v,W,Z,a,b=p;q=a+b;R=W-q
    assert R>0 and W<=21
    def positive_slots(c,d):
        return (6,7) if (c,d)==(a,b) else (7,6)
    if W==v:
        s={0:0,6:u,7:u+a,3:Z,1:1,2:v+1};branch='split_4_2_Wv'
    elif sorted((R,Z))==[u,v]:
        if R==v:
            r=0 if force=='no_shift' else 1
            s={0:0,3:u,1:r,6:r+v,7:r+v+a,2:r+W};branch='paired_large'
        else:
            r=next(r for r in (1,2,3) if r+v not in (u+a,W))
            if force=='no_shift':r=0
            s={0:0,6:u,7:u+a,2:W,1:r,3:r+v};branch='paired_small'
    elif any(W==v+d and Z==u+c for c,d in ((a,b),(b,a))):
        c,d=next((c,d) for c,d in ((a,b),(b,a)) if W==v+d and Z==u+c)
        i,j=positive_slots(c,d)
        r=next(r for r in (1,2,3) if u+c not in (r+v,r+v+d))
        if force=='no_shift':r=0
        s={0:0,i:u,3:u+c,1:r,j:r+v,2:r+W};branch='split_3_3'
    elif R>=Z:
        A=R-u;assert A>0 and R!=v
        c=next(c for c in (b,a) if R+c!=v);d=q-c;i,j=positive_slots(c,d)
        s={1:0,3:v,0:A,i:R,j:R+c,2:W};branch='forward'
    else:
        A=v-R;assert A>0 and A!=q
        c=next(c for c in (b,a) if c!=A);d=q-c;i,j=positive_slots(c,d)
        s={1:0,0:A,3:Z,2:v,j:A-q,i:A-c};branch='backward'
    s=normalize(s);target=target_for(*p);_,_,e=setup(target)
    assert len(s)==len(set(s.values()))==6,'repeated index'
    assert Counter(x+e[i] for i,x in s.items())==Counter(s.values())
    span=max(s.values())
    if span>20:assert span==21 and p in LONG_ROOTS
    return s,branch,span


def construct(p,force=None):
    s,branch,span=abstract(p,force)
    if span==21:r=LONG_ROOTS[p]
    else:
        valid=roots(tuple(s.values()));assert valid;r=valid[0]
    if force=='root0':r=0
    t=target_for(*p);witness=materialize(t,{i:x+r for i,x in s.items()})
    assert certificate_ok(witness['bins'],t)
    return dict(params=p,targets=t,shape=s,span=span,branch=branch,root=r,witness=witness)


def main():
    start=time.process_time();family=domains();results=[];branches=Counter();long=[]
    for t,p in sorted(family.items()):
        if time.process_time()-start>=5:
            print(json.dumps(dict(status='UNKNOWN',completed=len(results))));return
        x=construct(p);assert x['targets']==t
        results.append(x);branches[x['branch']]+=1
        if x['span']==21:long.append(p)
    assert set(long)==set(LONG_ROOTS)
    for p in ((6,6,7,7,1,1),(6,6,8,6,1,1),(6,7,8,7,1,1)):
        try:abstract(p,force='no_shift')
        except AssertionError as ex:assert str(ex)=='repeated index'
        else:raise AssertionError('omitted shift accepted')
    try:construct((6,6,21,1,5,5),force='root0')
    except ValueError as ex:assert str(ex)=='complementary pair reused'
    else:raise AssertionError('wrong long-shape root accepted')
    sample=results[0];s=dict(sample['shape']);_,_,e=setup(sample['targets'])
    s[2]+=1
    assert Counter(x+e[i] for i,x in s.items())!=Counter(s.values())
    bins=[set(x) for x in sample['witness']['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert Counter(x for b in bins for x in b)==Counter(range(1,56,2))
    assert not certificate_ok(bins,sample['targets'])
    prior=json.load(open('/tmp/math-instinct-b37-two-surplus.json'))
    unexpected=next(x for x in prior['results'] if tuple(x['params'])==(11,11,17,15,5,5))
    assert unexpected['chosen']['span']<=20
    assert certificate_ok(unexpected['witness']['bins'],unexpected['targets'])
    print(json.dumps(dict(status='ALL_2919_DIRECT',results=results,branches=dict(branches),
        span21=long,controls='PASS',unexpected_prior_span=unexpected['chosen']['span'],
        cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
