#!/usr/bin/env python3
"""B52/MI122 preregistered3cda72a1: factor all six positive moves.

Even E28 t4<112,t5>112. Positive moves u,v,a,b,c,d; subset sum W
gives two zero-sum cycles. Canonical minimum cardinality/lex owner subset,
then increasing(size,owner) within each part. Search only their two roots.
Tentative all-factorable availability. Independent full/direct DP domains,
primitive remainder COUNTED ONLY. B51 keys contained; direct/mask root-pair
checks and two literal checkers. Two-large-positives fixture, primitive,
same-root, duplicate/wrong-sum controls. Unexpected anchor/individual-root
losses. Caps15000 constructed targets/4M pairs/15 CPU seconds, no alternate
subset/order/solver fallback. Raw outside git.
OUTCOME: full four-surplus domain7828, factorable7223, primitive605.
Canonical rule certifies7221; failures(8,8,20,6;2,2,2,4) and
(8,10,18,8;2,2,2,2). All1469303 direct/mask comparisons, domains/controls
pass. No individually rootless shape;193 first-longer-root losses among
successes. CPU4.592863 s. Raw outside git SHA256
e25cb282fabd0cade077a3482743ff735c94f89cc25af39707358b64b99e66d2.
Blind all-canonical rule REFUTED. Primitive605 counted, never searched.
"""
from collections import Counter,defaultdict
from itertools import combinations,combinations_with_replacement
from pathlib import Path
import hashlib
import json
import sys
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok
from path_forest_three_surplus_audit import bitset_ok


def target(p):
    u,v,W,Z,steps=p
    return (56+2*u,56+2*v,112-2*W,112-2*Z)+tuple(112+2*s for s in steps)


def positives(p):
    return {0:p[0],1:p[1],**{4+i:s for i,s in enumerate(p[4])}}


def canonical(p):
    pos=positives(p)
    for n in range(1,6):
        for I in combinations(sorted(pos),n):
            if sum(pos[i] for i in I)==p[2]:return I
    return None


def dp_contains(values,W):
    sums={0}
    for x in values:sums|={s+x for s in sums}
    return W in sums


def domain(prior_path):
    all_signed={};factorable={};primitive={}
    for steps in combinations_with_replacement(range(1,6),4):
        q=sum(steps)
        for u in range(6,15):
            for v in range(u,18):
                total=u+v+q
                for W in range((total+1)//2,min(22,28-v,total-1)+1):
                    Z=total-W;p=(u,v,W,Z,steps);t=target(p)
                    assert t==tuple(sorted(t));all_signed[t]=p
                    (factorable if canonical(p) is not None else primitive)[t]=p
    lows=defaultdict(list)
    for xs in combinations_with_replacement(range(68,111,2),4):lows[sum(xs)].append(xs)
    direct=set();direct_factorable=set()
    for high in combinations_with_replacement(range(114,123,2),4):
        steps=tuple((x-112)//2 for x in high)
        for xs in lows[784-sum(high)]:
            t=xs+high;direct.add(t)
            u,v=(xs[0]-56)//2,(xs[1]-56)//2;W=(112-xs[2])//2
            if dp_contains((u,v)+steps,W):direct_factorable.add(t)
    assert set(all_signed)==direct and set(factorable)==direct_factorable
    assert set(primitive)==direct-direct_factorable
    raw=Path(prior_path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='02851403bc63388f571a9f52dfb6f4202616a2df706e4a2eb8f0e1f07174a7a1'
    prior=json.loads(raw);assert {tuple(e['targets']) for e in prior['results']}<=set(factorable)
    return factorable,primitive


def shapes(p):
    pos=positives(p);I=canonical(p);assert I is not None
    J=tuple(i for i in pos if i not in I)
    I=tuple(sorted(I,key=lambda i:(pos[i],i)));J=tuple(sorted(J,key=lambda i:(pos[i],i)))
    def cycle(ids):
        xs=[0]
        for i in ids:xs.append(xs[-1]+pos[i])
        return tuple(xs)
    S,T=cycle(I),cycle(J);assert S[-1]==p[2] and T[-1]==p[3]
    return S,T,I,J


def mask(shape,r):
    bits=0
    for x in shape:
        x+=r;bit=1<<min(x,27-x)
        if bits&bit:return None
        bits|=bit
    return bits


def direct(S,T,r,t):
    return len({min(x+r,27-x-r) for x in S}|{min(x+t,27-x-t) for x in T})==8


def certificate(p,r,t):
    S,T,I,J=shapes(p);selected={2:r+p[2],3:t+p[3]}
    for ids,shape,root in ((I,S,r),(J,T,t)):
        for k,i in enumerate(ids):selected[i]=root+shape[k]
    w=materialize(target(p),selected)
    assert certificate_ok(w['bins'],target(p)) and bitset_ok(w['bins'],target(p))
    return w


def controls():
    p=(6,6,12,6,(1,1,2,2));assert canonical(p)==(0,1)
    S,T,_,_=shapes(p);assert S==(0,6,12) and T==(0,1,2,4,6)
    w=certificate(p,0,3);assert not direct(S,T,0,0)
    primitive=(7,7,21,13,(5,5,5,5))
    assert canonical(primitive) is None and not dp_contains(positives(primitive).values(),21)
    bins=[list(b) for b in w['bins']];bins[0][0]=bins[1][0]
    assert not certificate_ok(bins,target(p)) and not bitset_ok(bins,target(p))
    bins=[set(b) for b in w['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert sorted(x for b in bins for x in b)==list(range(1,56,2))
    assert not certificate_ok(bins,target(p)) and not bitset_ok(bins,target(p))


def main():
    start=time.process_time();controls();family,primitive=domain(sys.argv[1]);results=[];failures=[]
    checks=0;anchor_losses=[];individual_failures=[];splits=Counter()
    for t,p in sorted(family.items()):
        if len(results)>=15000 or time.process_time()-start>=15:
            print(json.dumps(dict(status='UNKNOWN',total=len(family),completed=len(results))));return
        S,T,I,J=shapes(p);splits[(len(I),len(J))]+=1
        masksS=[mask(S,r) for r in range(28-S[-1])]
        masksT=[mask(T,r) for r in range(28-T[-1])]
        count=0;best=None;anchorS=len(S)>=len(T);masks=masksS if anchorS else masksT
        first=next((r for r,x in enumerate(masks) if x is not None),None);anchor_ok=False
        for r,a in enumerate(masksS):
            for s,b in enumerate(masksT):
                checks+=1
                if checks>4000000 or time.process_time()-start>=15:
                    print(json.dumps(dict(status='UNKNOWN',total=len(family),completed=len(results))));return
                algebra=a is not None and b is not None and not a&b
                assert algebra==direct(S,T,r,s)
                if algebra:
                    count+=1
                    if best is None:best=(r,s)
                    if (r if anchorS else s)==first:anchor_ok=True
        impossible=not any(x is not None for x in masksS) or not any(x is not None for x in masksT)
        if impossible:individual_failures.append(p)
        entry=dict(params=p,targets=t,partI=I,partJ=J,S=S,T=T,good_root_pairs=count)
        if best is not None:
            r,s=best;entry['chosen']=dict(rootS=r,rootT=s,witness=certificate(p,r,s))
            if not anchor_ok:anchor_losses.append(p)
        else:
            entry['individual_masks']=(masksS,masksT);failures.append(entry)
        results.append(entry)
    print(json.dumps(dict(status='DIAGNOSED',total_targets=len(family)+len(primitive),
        factorable=len(family),primitive_count=len(primitive),certified=len(results)-len(failures),
        results=results,failures=failures,primitive_targets=[dict(targets=t,params=p) for t,p in sorted(primitive.items())],
        root_pair_checks=checks,first_longer_root_losses=anchor_losses,individually_impossible=individual_failures,
        positive_part_sizes={str(k):v for k,v in splits.items()},controls='PASS',
        cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
