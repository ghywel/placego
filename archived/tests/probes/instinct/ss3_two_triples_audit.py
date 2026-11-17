#!/usr/bin/env python3
"""MI316/B152 prereg: ONE audit after source/prediction push,not before.

Direct two-prescribed-triple recipe,N15..24,ALL SS-admitted ordered u<=v.
N15..18 independent whole feasibility maps from six-subsets/ten splits.
Two/three-disjoint representation palettes,M<=30;literal certificates,
reflection/signed control;N7 (4,14) SS-admitted but impossible control.
Predict every comparison passes;general claim remains SKETCH.
15CPU/25wall/128MiB/1M reference splits/50k recipe calls/2MiB report;
30wall external watchdog. First failure/cap stops,no repair/retry/extension.

CANCELLED BEFORE EXECUTION,MI317:Cloud CL434/5ef12b10 independently verified
MI295,which already implies this two-triple statement for N>=15. Keep this
alternative construction/preregistration as provenance;do not run a redundant
audit. No experimental outcome or finite pass is claimed.
"""
import argparse
import hashlib
import itertools
import json
import resource
import time
from pathlib import Path

CPU = time.process_time()
WALL = time.monotonic()
SPLITS = 0
CALLS = 0


def limits():
    assert time.process_time()-CPU < 15, 'CPU cap'
    assert time.monotonic()-WALL < 25, 'wall cap'
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 128*1024**2, 'RSS cap (macOS bytes)'
    assert SPLITS <= 1_000_000 and CALLS <= 50_000, 'work cap'


def low(r):
    return r*(r-1)//2


def high(n,r):
    return r*(2*n-r-1)//2


def palette(m,t,count):
    if count == 2:
        assert m>=6 and 8<=t<=3*m-8
        shift,residue=divmod(t-8,3)
        base=[((0,2,6),(1,3,4)),((0,4,5),(1,2,6)),((0,4,6),(2,3,5))][residue]
        return tuple(tuple(v+shift for v in a) for a in base)
    assert count==3 and m>=8 and 12<=t<=3*m-12
    bases=[((0,4,8),(1,5,6),(2,3,7)),((0,4,9),(1,5,7),(2,3,8)),((0,5,9),(1,6,7),(2,4,8))]
    if t==3*m-12:
        return tuple(tuple(sorted(m-v for v in a)) for a in bases[0])
    shift,residue=divmod(t-12,3)
    return tuple(tuple(v+shift for v in a) for a in bases[residue])


def core(n,u,v):
    if v<=13:
        if v==8:
            return ((0,2,5) if u==7 else (0,2,6)),(1,3,4),'small'
        if (u,v)==(6,10):
            return (0,2,4),(1,3,6),'small'
        a=(0,1,u-1)
        b={9:(2,3,4),10:(2,3,5),11:(2,3,6),12:(2,4,6),13:(2,4,7)}[v]
        corrections={(4,11):(2,4,5),(7,11):(2,4,5),(3,12):(3,4,5),
                     (5,12):(2,3,7),(7,12):(2,3,7),(3,13):(3,4,6),
                     (5,13):(2,3,8),(8,13):(2,3,8)}
        return a,corrections.get((u,v),b),'small'
    if u<=n:
        a=(0,1,u-1)
        if v<=3*n-11:
            options=palette(n-3,v-6,2)
            b=next(row for row in options if u-3 not in row)
            return a,tuple(x+2 for x in b),'two'
        j=3*n-6-v
        assert 0<=j<=4 and u<=7
        return a,(n-3-j,n-2,n-1),'top'
    if u%2:
        p,q=(u-1)//2,(u+1)//2
    else:
        p,q=u//2-1,u//2+1
    a=(0,p,q)
    b=next(row for row in palette(n-2,v-3,3) if p-1 not in row and q-1 not in row)
    return a,tuple(x+1 for x in b),'three'


def recipe(n,u,v):
    global CALLS
    CALLS+=1
    assert n>=15 and 3<=u<=v<=high(n,3) and low(6)<=u+v<=high(n,6)
    if u+v>3*(n-1):
        a,b,branch=core(n,3*(n-1)-v,3*(n-1)-u)
        return tuple(sorted(n-1-x for x in b)),tuple(sorted(n-1-x for x in a)),branch,True
    a,b,branch=core(n,u,v)
    return a,b,branch,False


def domain(n):
    return {(u,v) for u in range(3,high(n,3)+1) for v in range(u,high(n,3)+1)
            if low(6)<=u+v<=high(n,6)}


def reference(n):
    # Enumerate original six-token subsets and ALL unordered triple splits.
    # No palettes,reflection,SS bounds or recipe branches are used here.
    global SPLITS
    pairs=set()
    for six in itertools.combinations(range(n),6):
        total=sum(six)
        for other in itertools.combinations(range(1,6),2):
            chosen=(six[0],six[other[0]],six[other[1]])
            s=sum(chosen)
            pairs.add(tuple(sorted((s,total-s))))
            SPLITS+=1
        if SPLITS%1000==0:
            limits()
    limits()
    return pairs


def check(a,b,u,v,n):
    assert len(set(a))==len(a)==len(set(b))==len(b)==3
    assert not set(a)&set(b) and all(0<=x<n for x in a+b)
    assert sum(a)==u and sum(b)==v
    rest=tuple(x for x in range(n) if x not in a and x not in b)
    assert len(rest)==n-6 and sum(rest)==low(n)-u-v


def audit(path):
    palette_checks=0
    for count,start,lo in ((2,6,8),(3,8,12)):
        for m in range(start,31):
            for t in range(lo,3*m-lo+1):
                rows=palette(m,t,count)
                assert len(rows)==count and all(len(row)==len(set(row))==3 and sum(row)==t for row in rows)
                assert len(set(x for row in rows for x in row))==3*count
                assert all(0<=x<=m for row in rows for x in row)
                palette_checks+=1
    rows=[]
    branches={name:0 for name in ('small','two','top','three')}
    reflected=0
    by_n={}
    for n in range(15,25):
        expected=domain(n)
        if n<=18:
            assert reference(n)==expected
        for u,v in sorted(expected):
            a,b,branch,flip=recipe(n,u,v)
            check(a,b,u,v,n)
            rows.append((n,u,v,a,b,branch,flip))
            branches[branch]+=1
            reflected+=flip
        by_n[n]=len(expected)
        limits()
    assert all(branches.values()) and reflected>0
    # Independent negative control,plus a literal positive and signed translate.
    assert (4,14) in domain(7) and (4,14) not in reference(7)
    assert (3,12) in reference(6)
    a,b,_,_=recipe(15,3,12)
    check(a,b,3,12,15)
    shifted=tuple(x-17 for x in a),tuple(x-17 for x in b)
    assert sum(shifted[0])==3-51 and sum(shifted[1])==12-51
    assert not set(shifted[0])&set(shifted[1])
    limits()
    report=dict(status='PASS',rows=rows,by_n=by_n,branches=branches,reflected=reflected,
                palette_checks=palette_checks,reference_splits=SPLITS,recipe_calls=CALLS,
                negative_control=[7,4,14,False],cpu_seconds=time.process_time()-CPU,
                wall_seconds=time.monotonic()-WALL,
                peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw=json.dumps(report,sort_keys=True,separators=(',',':')).encode()
    assert len(raw)<=2*1024**2 and not path.exists()
    path.write_bytes(raw)
    summary={k:report[k] for k in ('status','by_n','branches','reflected','palette_checks','reference_splits','recipe_calls','cpu_seconds','wall_seconds','peak_rss_bytes')}
    summary.update(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
    print(json.dumps(summary,sort_keys=True))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--report',type=Path,required=True)
    audit(parser.parse_args().report)
