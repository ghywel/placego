#!/usr/bin/env python3
"""B51/MI120 preregisteredbeda707c: canonical subset cancellation.

Four positive surpluses1..5; proper subset I sum W-v, J complement.
Choose min-cardinality then lex indices; increasing item order per cycle.
Only independent translations of these two prescribed cycles are tested.
Tentative all-family feasibility, independent direct/DP target domain,
masks/direct labels at all root pairs, two literal partition checkers.
No-subset/included-constant, wrong-subset with distinct labels, overlap,
duplicate/wrong-sum controls. Unexpected first longer-cycle root losses.
Prior133 targets included, no additive counts. Cap15000 targets/4M root
pairs/15 CPU seconds. Retain failures; no subset/order/solver fallback.
OUTCOME: all4938 targets certify, signed and independent direct/DP domains
agree; all993670 direct/mask root-pair checks agree, controls pass. Splits
3+1:1471,2+2:2639,1+3:828 positive items. First longer-cycle root fails
on56 targets, all repaired by joint root choice in the SAME fixed shapes;
no individually impossible shape. CPU2.841127 s. Raw outside git SHA256
02851403bc63388f571a9f52dfb6f4202616a2df706e4a2eb8f0e1f07174a7a1.
Finite canonical family COMPUTED, greedy-anchor rule REFUTED on that family.
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


def canonical(steps,D):
    for n in range(1,4):
        for I in combinations(range(4),n):
            if sum(steps[i] for i in I)==D:return I
    return None


def dp_contains(steps,D):
    possible={(0,0)}
    for value in steps:possible|={(s+value,n+1) for s,n in possible}
    return any((D,n) in possible for n in (1,2,3))


def domain(prior_path):
    out={}
    for steps in combinations_with_replacement(range(1,6),4):
        q=sum(steps)
        for u in range(6,15):
            for v in range(u,18):
                total=u+v+q
                for W in range((total+1)//2,min(22,28-v,total-1)+1):
                    Z=total-W
                    if canonical(steps,W-v) is not None:
                        p=(u,v,W,Z,steps);t=target(p)
                        assert t==tuple(sorted(t));out[t]=p
    lows=defaultdict(list)
    for xs in combinations_with_replacement(range(68,111,2),4):lows[sum(xs)].append(xs)
    direct=set()
    for high in combinations_with_replacement(range(114,123,2),4):
        steps=tuple((x-112)//2 for x in high)
        for xs in lows[784-sum(high)]:
            v=(xs[1]-56)//2;W=(112-xs[2])//2
            if dp_contains(steps,W-v):direct.add(xs+high)
    assert set(out)==direct
    raw=Path(prior_path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='665da55308b4e401a424e56d26c43947615c7705b924114ce2c6426a6aaff8bd'
    prior=json.loads(raw)
    assert {tuple(x['targets']) for x in prior['results']}<=set(out)
    return out


def shapes(p,I=None):
    u,v,W,Z,steps=p
    if I is None:I=canonical(steps,W-v)
    assert I is not None
    J=tuple(i for i in range(4) if i not in I)
    def cycle(ids,negative):
        xs=[0]
        for i in ids:xs.append(xs[-1]+steps[i])
        return tuple(xs)+(negative,)
    return cycle(I,W),cycle(J,Z),I,J


def mask(shape,r):
    bits=0
    for x in shape:
        x+=r;bit=1<<min(x,27-x)
        if bits&bit:return None
        bits|=bit
    return bits


def direct(S,T,r,t):
    return len({min(x+r,27-x-r) for x in S}|{min(x+t,27-x-t) for x in T})==8


def certificate(p,r,t,I=None):
    u,v,W,Z,steps=p;S,T,I,J=shapes(p,I)
    selected={1:r+S[-2],2:r+W,0:t+T[-2],3:t+Z}
    for ids,shape,root in ((I,S,r),(J,T,t)):
        for k,i in enumerate(ids):selected[4+i]=root+shape[k]
    w=materialize(target(p),selected)
    assert certificate_ok(w['bins'],target(p)) and bitset_ok(w['bins'],target(p))
    return w


def controls():
    p=(6,7,10,9,(1,1,2,2));assert canonical(p[-1],3)==(0,2)
    w=certificate(p,0,4);S,T,_,_=shapes(p)
    assert not direct(S,T,0,0)
    badS,badT,_,_=shapes(p,(0,));assert direct(badS,badT,0,2)
    try:certificate(p,0,2,(0,))
    except ValueError as e:assert str(e)=='not a permutation of selected tokens'
    else:raise AssertionError('wrong subset balance accepted')
    assert canonical((5,5,5,5),14) is None and not dp_contains((5,5,5,5),14)
    assert canonical((5,5,5,5),15)==(0,1,2) and dp_contains((5,5,5,5),15)
    bins=[list(b) for b in w['bins']];bins[0][0]=bins[1][0]
    assert not certificate_ok(bins,target(p)) and not bitset_ok(bins,target(p))
    bins=[set(b) for b in w['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert sorted(x for b in bins for x in b)==list(range(1,56,2))
    assert not certificate_ok(bins,target(p)) and not bitset_ok(bins,target(p))


def main():
    start=time.process_time();controls();family=domain(sys.argv[1]);results=[];failures=[]
    checks=0;anchor_losses=[];individual_failures=[];splits=Counter()
    for target_tuple,p in sorted(family.items()):
        if len(results)>=15000 or time.process_time()-start>=15:
            print(json.dumps(dict(status='UNKNOWN',total=len(family),completed=len(results))));return
        S,T,I,J=shapes(p);splits[(len(I),len(J))]+=1
        assert len(set(S))==len(S) and len(set(T))==len(T)
        masksS=[mask(S,r) for r in range(28-S[-1])]
        masksT=[mask(T,r) for r in range(28-T[-1])]
        count=0;best=None;anchorS=len(S)>=len(T);masks=masksS if anchorS else masksT
        first=next((r for r,x in enumerate(masks) if x is not None),None);anchor_ok=False
        for r,a in enumerate(masksS):
            for t,b in enumerate(masksT):
                checks+=1
                if checks>4000000 or time.process_time()-start>=15:
                    print(json.dumps(dict(status='UNKNOWN',total=len(family),completed=len(results))));return
                algebra=a is not None and b is not None and not a&b
                assert algebra==direct(S,T,r,t)
                if algebra:
                    count+=1
                    if best is None:best=(r,t)
                    if (r if anchorS else t)==first:anchor_ok=True
        impossible=not any(x is not None for x in masksS) or not any(x is not None for x in masksT)
        if impossible:individual_failures.append(p)
        entry=dict(params=p,targets=target_tuple,subset=I,S=S,T=T,good_root_pairs=count)
        if best is not None:
            r,t=best;entry['chosen']=dict(rootS=r,rootT=t,witness=certificate(p,r,t))
            if not anchor_ok:anchor_losses.append(p)
        else:
            entry['individual_masks']=(masksS,masksT);failures.append(entry)
        results.append(entry)
    print(json.dumps(dict(status='DIAGNOSED',total=len(family),certified=len(results)-len(failures),
        results=results,failures=failures,root_pair_checks=checks,
        first_longer_root_losses=anchor_losses,individually_impossible=individual_failures,
        subset_sizes={str(k):v for k,v in splits.items()},controls='PASS',
        cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
