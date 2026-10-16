#!/usr/bin/env python3
"""B46/MI108 strict two-edge corner, preregistered09a0a21e.

Three surplus moves, W<=q. Allocate b,c to W and a to Z; all after their
negative edges. Normalized coordinates 0<d-a<b<d<B<W<u+B span14..17.
Root0 except four explicit boundary configurations. Predict20 targets,
q counts3/4/5/8, signed/direct domains equal; literal certificates.
Every all-on-W strict parent invalid; four omitted-root and wrong-sum
controls fail. Unexpected all span16 shapes root0. Cap30 inputs/one CPU
second, no order search or added repair.
OUTCOME: all20 formula certificates pass; signed/direct domains and
q counts3/4/5/8 agree. Spans14:1,15:3,16:13,17:3; exactly four
nonzero root corrections. All single-donor parents invalid, omitted-root
and wrong-sum controls reject; every span16 shape root0. CPU0.006461 s.
Raw outside git SHA256
f7c46c9182bd125ef2159022b9cf1f5949bfba75f95d524aec0c42b06f2c05a0.
Uniform hand candidate PROOF-SKETCH, finite corner COMPUTED.
"""
from collections import Counter,defaultdict
from itertools import combinations_with_replacement
import json
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok

EXCEPTIONS={
    (6,6,12,12,3,4,5):1,(7,7,14,14,4,5,5):1,
    (7,7,15,14,5,5,5):3,(7,8,15,15,5,5,5):2}


def domains():
    out={}
    for a,b,c in combinations_with_replacement(range(1,6),3):
        q=a+b+c
        for u in range(6,15):
            for v in range(u,18):
                total=u+v+q
                for W in range((total+1)//2,min(22,28-v,q,total-1)+1):
                    Z=total-W;t=(56+2*u,56+2*v,112-2*W,112-2*Z,112,112+2*a,112+2*b,112+2*c)
                    assert t==tuple(sorted(t));out[t]=(u,v,W,Z,a,b,c)
    lows=defaultdict(list)
    for xs in combinations_with_replacement(range(68,111,2),4):lows[sum(xs)].append(xs)
    direct=set()
    for high in combinations_with_replacement(range(114,123,2),3):
        q=sum((t-112)//2 for t in high)
        for low in lows[784-112-sum(high)]:
            W=(112-low[2])//2
            if W<=q:direct.add(low+(112,)+high)
    assert set(out)==direct and len(out)==20
    assert [sum(sum(p[-3:])==q for p in out.values()) for q in range(12,16)]==[3,4,5,8]
    return out


def construct(p,force0=False):
    u,v,W,Z,a,b,c=p;q=a+b+c;B=b+c;d=W-v;D=u+B
    assert W<=q and W-q<=0
    assert W-B>0 and Z-a>0 and W-B<=5<Z-a
    coords=(0,d-a,b,d,B,W,D)
    assert all(x<y for x,y in zip(coords,coords[1:])) and 14<=D<=17
    r=0 if force0 else EXCEPTIONS.get(p,0)
    selected={6:0,5:d-a,7:b,1:d,0:B,2:W,3:D}
    target=(56+2*u,56+2*v,112-2*W,112-2*Z,112,112+2*a,112+2*b,112+2*c)
    witness=materialize(target,{i:x+r for i,x in selected.items()})
    assert certificate_ok(witness['bins'],target)
    return dict(params=p,targets=target,shape=coords,span=D,root=r,witness=witness)


def main():
    start=time.process_time();family=domains();results=[];spans=Counter();nonzero=[]
    for t,p in sorted(family.items()):
        assert len(results)<30 and time.process_time()-start<1
        r=construct(p);assert r['targets']==t;results.append(r);spans[r['span']]+=1
        if r['root']:nonzero.append(p)
        if r['span']==16:assert r['root']==0
    assert set(nonzero)==set(EXCEPTIONS)
    for p in EXCEPTIONS:
        try:construct(p,force0=True)
        except ValueError as ex:assert str(ex)=='complementary pair reused'
        else:raise AssertionError('omitted root accepted')
    sample=results[0];bins=[set(x) for x in sample['witness']['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert Counter(x for b in bins for x in b)==Counter(range(1,56,2))
    assert not certificate_ok(bins,sample['targets'])
    print(json.dumps(dict(status='ALL_20_TWO_DONOR',results=results,spans=dict(spans),
        nonzero_roots=nonzero,invalid_single_donor=20,controls='PASS',
        cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
