#!/usr/bin/env python3
"""B48/MI113 preregistered1d161ca7: bypass equal-step literal traps.

Two prescribed cancelling cycles: {0,s,h+s} and {0,s,2s,g+2s}.
Predict all112 B47 literal failures admit disjoint folded labels after
independent root choices. Signed trap/direct target/B47 failure domains
must agree, as must direct labels and independent masks at every root pair.
Full certificate checker, same-root and wrong-donor/wrong-sum controls.
Unexpected: does the first individually legal four-cycle root ever lose
solutions requiring joint root selection? Caps120 inputs/50000 pairs/two
CPU seconds, no extra allocation, cycle class, or solver. Raw outside git.
OUTCOME: all112 targets certify; all25612 direct/mask root-pair comparisons
agree. Independent domains and controls pass. First individually legal
four-cycle root loses NO target. CPU0.254758 s. Raw outside git SHA256
5c0790e809234bd0df79cdc4c8ce4a580bc0233f65713bf4edd34d6142e79e7d.
Two-cycle identity SKETCH; finite placement availability COMPUTED.
"""
from collections import Counter,defaultdict
from itertools import combinations_with_replacement
import hashlib
import json
import sys
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok


def target(p):
    u,v,W,Z,a,b,c=p
    return (56+2*u,56+2*v,112-2*W,112-2*Z,112,
            112+2*a,112+2*b,112+2*c)


def domains(prior_path):
    prior_bytes=open(prior_path,'rb').read()
    assert hashlib.sha256(prior_bytes).hexdigest()=='a989a08e571ff50a5668fc70c9b320eda257f3e02323dd5dab0f5b77cd688633'
    prior=json.loads(prior_bytes);out={}
    for s in range(1,6):
        for u in range(6,15):
            for v in range(u,18):
                for W,Z in ((v+s,u+2*s),(v+2*s,u+s)):
                    p=(u,v,W,Z,s,s,s)
                    if W<22 and W>=Z and v+W<=28 and 0<W-3*s<Z and not {u,v}&{W,Z}:
                        t=target(p);assert t==tuple(sorted(t));out[t]=p
    assert set(out)=={tuple(x['targets']) for x in prior['failures']}
    lows=defaultdict(list)
    for xs in combinations_with_replacement(range(68,111,2),4):lows[sum(xs)].append(xs)
    direct=set()
    for s in range(1,6):
        high=(112,)+(112+2*s,)*3
        for xs in lows[784-sum(high)]:
            u,v=(xs[0]-56)//2,(xs[1]-56)//2
            W,Z=(112-xs[2])//2,(112-xs[3])//2
            if W<22 and 0<W-3*s<Z and not {u,v}&{W,Z} and W-v in (s,2*s):
                direct.add(xs+high)
    assert set(out)==direct and len(out)==112
    return out


def shapes(p):
    u,v,W,Z,s,b,c=p;assert s==b==c
    if W-v==s:h,g,hi,gi,Hidx,Gidx=v,u,1,0,2,3
    else:
        assert W-v==2*s
        h,g,hi,gi,Hidx,Gidx=u,v,0,1,3,2
    H=h+s;G=g+2*s
    assert sorted((H,G))==sorted((W,Z))
    return (0,s,H),(0,s,2*s,G),(hi,gi,Hidx,Gidx)


def mask(shape,r):
    bits=0
    for x in shape:
        x+=r;bit=1<<min(x,27-x)
        if bits&bit:return None
        bits|=bit
    return bits


def direct(S,T,r,t):
    labels=[min(x+r,27-x-r) for x in S]+[min(x+t,27-x-t) for x in T]
    return len(set(labels))==7


def certificate(p,r,t,swap=False):
    S,T,(hi,gi,Hidx,Gidx)=shapes(p);s=p[4]
    selected={5:r,hi:r+s,Hidx:r+S[-1],6:t,7:t+s,gi:t+2*s,Gidx:t+T[-1]}
    if swap:selected[Hidx],selected[Gidx]=selected[Gidx],selected[Hidx]
    w=materialize(target(p),selected);assert certificate_ok(w['bins'],target(p));return w


def controls():
    p=(6,6,8,7,1,1,1);S,T,_=shapes(p)
    assert not direct(S,T,0,0) and mask(S,0)&mask(T,0)
    w=certificate(p,0,3)
    try:certificate(p,0,3,swap=True)
    except ValueError as e:assert str(e)=='not a permutation of selected tokens'
    else:raise AssertionError('wrong donor assignment accepted')
    bins=[set(x) for x in w['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert Counter(x for b in bins for x in b)==Counter(range(1,56,2))
    assert not certificate_ok(bins,target(p))


def main():
    start=time.process_time();controls();family=domains(sys.argv[1]);results=[];failures=[]
    checks=0;first_root_losses=[]
    for t,p in sorted(family.items()):
        if len(results)>=120 or time.process_time()-start>=2:
            print(json.dumps(dict(status='UNKNOWN',total=len(family),completed=len(results))));return
        S,T,_=shapes(p);masks3=[mask(S,r) for r in range(28-S[-1])]
        masks4=[mask(T,r) for r in range(28-T[-1])]
        good=[]
        for r,a in enumerate(masks3):
            for s,b in enumerate(masks4):
                checks+=1
                if checks>50000 or time.process_time()-start>=2:
                    print(json.dumps(dict(status='UNKNOWN',total=len(family),completed=len(results))));return
                algebra=a is not None and b is not None and not a&b
                assert algebra==direct(S,T,r,s)
                if algebra:good.append((r,s))
        entry=dict(params=p,targets=t,three=S,four=T,root_pairs=good)
        if good:
            r,s=good[0];entry['chosen']=dict(three_root=r,four_root=s,witness=certificate(p,r,s))
            first=next(s for s,b in enumerate(masks4) if b is not None)
            if not any(s==first for r,s in good):first_root_losses.append(p)
        else:failures.append(entry)
        results.append(entry)
    print(json.dumps(dict(status='DIAGNOSED',total=len(family),certified=len(results)-len(failures),
        results=results,failures=failures,root_pair_checks=checks,first_four_root_losses=first_root_losses,
        controls='PASS',cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
