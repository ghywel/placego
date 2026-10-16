#!/usr/bin/env python3
"""B50/MI118 preregisteredb3ed973e: eight-position cancelling cycles.

Four equal positive steps s, W-v=j*s,1<=j<=3, unmatched W<22,
0<W-4s<Z. Two prescribed shapes0,s,..,j*s,W and0,s,..,(4-j)*s,Z.
Blind all-family root-pair availability. Independent signed/direct target
domains, masks/direct labels at every pair, literal full certificates with
two checkers. Same-root, negative-owner swap, duplicate/wrong-sum controls.
Unexpected first legal longer-cycle root and individually impossible shapes.
Cap300 targets/100000 pairs/three CPU seconds; no repair or widened class.
OUTCOME: all133 targets certify; all29461 mask/direct root-pair checks
agree, independent domains and adverse controls pass. No individually
impossible shape or first-longer-root loss. CPU0.090257 s. Raw outside git
SHA256665da55308b4e401a424e56d26c43947615c7705b924114ce2c6426a6aaff8bd.
Finite eight-position family COMPUTED; no full four-surplus conclusion.
"""
from collections import defaultdict
from itertools import combinations_with_replacement
import json
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok
from path_forest_three_surplus_audit import bitset_ok


def target(p):
    u,v,W,Z,s,j=p
    return (56+2*u,56+2*v,112-2*W,112-2*Z)+(112+2*s,)*4


def domain():
    out={}
    for s in range(1,6):
        for u in range(6,15):
            for v in range(u,18):
                for j in (1,2,3):
                    W,Z=v+j*s,u+(4-j)*s
                    if W<22 and W>=Z and v+W<=28 and 0<W-4*s<Z and not {u,v}&{W,Z}:
                        p=(u,v,W,Z,s,j);t=target(p)
                        assert t==tuple(sorted(t));out[t]=p
    lows=defaultdict(list)
    for xs in combinations_with_replacement(range(68,111,2),4):lows[sum(xs)].append(xs)
    direct=set()
    for s in range(1,6):
        high=(112+2*s,)*4
        for xs in lows[784-sum(high)]:
            u,v=(xs[0]-56)//2,(xs[1]-56)//2
            W,Z=(112-xs[2])//2,(112-xs[3])//2
            if W<22 and 0<W-4*s<Z and not {u,v}&{W,Z} and W-v in (s,2*s,3*s):
                direct.add(xs+high)
    assert set(out)==direct
    return out


def shapes(p):
    u,v,W,Z,s,j=p
    return tuple(range(0,(j+1)*s,s))+(W,),tuple(range(0,(5-j)*s,s))+(Z,)


def mask(shape,r):
    bits=0
    for x in shape:
        x+=r;bit=1<<min(x,27-x)
        if bits&bit:return None
        bits|=bit
    return bits


def direct(S,T,r,t):
    labels=[min(x+r,27-x-r) for x in S]+[min(x+t,27-x-t) for x in T]
    return len(set(labels))==8


def certificate(p,r,t,swap=False):
    u,v,W,Z,s,j=p
    selected={1:r+j*s,2:r+W,0:t+(4-j)*s,3:t+Z}
    for k in range(j):selected[4+k]=r+k*s
    for k in range(4-j):selected[4+j+k]=t+k*s
    if swap:selected[2],selected[3]=selected[3],selected[2]
    w=materialize(target(p),selected)
    assert certificate_ok(w['bins'],target(p)) and bitset_ok(w['bins'],target(p))
    return w


def controls():
    p=(6,6,21,11,5,3);S,T=shapes(p)
    assert not direct(S,T,0,0)
    w=certificate(p,0,2)
    try:certificate(p,0,2,swap=True)
    except ValueError as e:assert str(e)=='not a permutation of selected tokens'
    else:raise AssertionError('negative owners swap accepted')
    bins=[list(b) for b in w['bins']];bins[0][0]=bins[1][0]
    assert not certificate_ok(bins,target(p)) and not bitset_ok(bins,target(p))
    bins=[set(b) for b in w['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert sorted(x for b in bins for x in b)==list(range(1,56,2))
    assert not certificate_ok(bins,target(p)) and not bitset_ok(bins,target(p))


def main():
    start=time.process_time();controls();family=domain();results=[];failures=[]
    checks=0;anchor_losses=[];individual_failures=[]
    for target_tuple,p in sorted(family.items()):
        if len(results)>=300 or time.process_time()-start>=3:
            print(json.dumps(dict(status='UNKNOWN',total=len(family),completed=len(results))));return
        S,T=shapes(p);masksS=[mask(S,r) for r in range(28-S[-1])]
        masksT=[mask(T,r) for r in range(28-T[-1])]
        good=[]
        for r,a in enumerate(masksS):
            for t,b in enumerate(masksT):
                checks+=1
                if checks>100000 or time.process_time()-start>=3:
                    print(json.dumps(dict(status='UNKNOWN',total=len(family),completed=len(results))));return
                algebra=a is not None and b is not None and not a&b
                assert algebra==direct(S,T,r,t)
                if algebra:good.append((r,t))
        entry=dict(params=p,targets=target_tuple,S=S,T=T,root_pairs=good)
        if not any(x is not None for x in masksS) or not any(x is not None for x in masksT):
            individual_failures.append(p)
        if good:
            r,t=good[0];entry['chosen']=dict(rootS=r,rootT=t,witness=certificate(p,r,t))
            anchorS=len(S)>=len(T);masks=masksS if anchorS else masksT
            first=next(r for r,x in enumerate(masks) if x is not None)
            if not any((r if anchorS else t)==first for r,t in good):anchor_losses.append(p)
        else:failures.append(entry)
        results.append(entry)
    print(json.dumps(dict(status='DIAGNOSED',total=len(family),certified=len(results)-len(failures),
        results=results,failures=failures,root_pair_checks=checks,
        first_longer_root_losses=anchor_losses,individually_impossible=individual_failures,
        controls='PASS',cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
