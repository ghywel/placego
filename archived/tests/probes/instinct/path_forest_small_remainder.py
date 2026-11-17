#!/usr/bin/env python3
"""B47/MI111, preregistered941bb4fa: remaining unmatched parent.

W>q, 0<R=W-q<Z, W<22; all three surplus steps after -W.
Fixed-five/two-variable graph checks literal as well as reflected collisions.
Must match direct folded labels for every root/item order and independently
derived target domain. Blind prediction some architecture failures, possibly
literal-only. Retain all failures; no repair or widened cycle search.
Controls: literal-only trap, nonzero base offset, matching fixed duplicate,
coverage-preserving wrong sums. Unexpected classify literal-no-order versus
reflection-only exhaustion and maximum actual span. Caps5000 targets,
500000 root-order comparisons, five CPU seconds. Raw JSON outside git.
OUTCOME: 2760 targets,2648 certify; all181956 graph/direct comparisons
agree. All112 failures have no literal-admissible order; no reflection-only
exhaustion. Max span25 attained once with a valid root0. Independent domains
and all controls pass. CPU0.911747 s. Raw outside git SHA256
a989a08e571ff50a5668fc70c9b320eda257f3e02323dd5dab0f5b77cd688633.
Hand obstruction classification MI112; no full E28/L8 conclusion.
"""
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement
import json
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok


def target(p):
    u,v,W,Z,a,b,c=p
    return (56+2*u,56+2*v,112-2*W,112-2*Z,112,
            112+2*a,112+2*b,112+2*c)


def parameters():
    out={}
    for a,b,c in combinations_with_replacement(range(1,6),3):
        q=a+b+c
        for u in range(6,15):
            for v in range(u,18):
                total=u+v+q
                for W in range((total+1)//2,min(21,28-v,total-1)+1):
                    Z=total-W;R=W-q
                    if not 0<R<Z or {u,v}&{W,Z}:continue
                    p=(u,v,W,Z,a,b,c);t=target(p)
                    assert t==tuple(sorted(t));out[t]=p
    lows=defaultdict(list)
    for t in combinations_with_replacement(range(68,111,2),4):lows[sum(t)].append(t)
    direct=set()
    for high in combinations_with_replacement(range(114,123,2),3):
        q=sum((x-112)//2 for x in high)
        for xs in lows[784-112-sum(high)]:
            u,v=(xs[0]-56)//2,(xs[1]-56)//2
            W,Z=(112-xs[2])//2,(112-xs[3])//2
            if W<22 and 0<W-q<Z and not {u,v}&{W,Z}:
                direct.add(xs+(112,)+high)
    assert set(out)==direct
    return out


def fixed(p):
    u,v,W,Z,a,b,c=p;q=a+b+c;R=W-q;A=v-R
    assert A==Z-u and A>0 and 0<R<Z
    raw=(0,A,v,Z,A-q)
    if len(set(raw))!=5:raise ValueError('fixed coordinate duplicated')
    m=min(raw);C=tuple(x-m for x in raw);b=A-q-m;D=max(C)
    assert m==min(0,A-q) and 0<=b and D<=25
    return C,b,D,m


def algebra(p,r,omit_literal=False):
    C,b,D,m=fixed(p);T=27-2*r;q=sum(p[-3:]);steps=p[-3:]
    L={x-b for x in C};F={T-b-x for x in C}
    core_ok=all(x+y!=T for x,y in combinations(C,2))
    literal=[];edges=[]
    for i in range(3):
        for j in range(3):
            if i==j:continue
            x,y=steps[i],q-steps[j]
            lit=x not in L and y not in L
            if lit:literal.append((i,j))
            if core_ok and (lit or omit_literal) and x not in F and y not in F and 2*b+x+y!=T:
                edges.append((i,j))
    return core_ok,literal,edges


def direct(p,r):
    C,b,D,m=fixed(p);q=sum(p[-3:]);steps=p[-3:];edges=[]
    for i in range(3):
        for j in range(3):
            if i==j:continue
            points=C+(b+steps[i],b+q-steps[j])
            physical=[x+r for x in points]
            assert min(physical)>=0 and max(physical)<=27
            labels=[min(x,27-x) for x in physical]
            if len(set(labels))==7:edges.append((i,j))
    return edges


def certificate(p,r,i,j):
    u,v,W,Z,a,b,c=p;steps=(a,b,c);q=sum(steps);R=W-q;A=v-R
    C,b,D,m=fixed(p);k=3-i-j
    # Independently rebuild the actual directed cycle, preserving bin identities.
    selected={1:0,2:v,5+i:A-q,5+k:A-q+steps[i],5+j:A-steps[j],0:A,3:Z}
    selected={owner:x+r-m for owner,x in selected.items()}
    witness=materialize(target(p),selected)
    assert certificate_ok(witness['bins'],target(p))
    return witness


def controls():
    trap=(6,6,15,11,4,5,5)
    assert (0,2) in algebra(trap,0,omit_literal=True)[2]
    assert (0,2) not in algebra(trap,0)[2] and (0,2) not in direct(trap,0)
    certificate(trap,0,1,0)
    offset=(6,14,12,11,1,1,1)
    assert fixed(offset)[1]==2 and (0,2) in algebra(offset,0)[2]
    certificate(offset,0,0,2)
    try:fixed((6,10,10,9,1,1,1))
    except ValueError as e:assert str(e)=='fixed coordinate duplicated'
    else:raise AssertionError('matching duplicate accepted')
    w=certificate(trap,0,1,0);bins=[set(s) for s in w['bins']]
    x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert Counter(x for s in bins for x in s)==Counter(range(1,56,2))
    assert not certificate_ok(bins,target(trap))


def main():
    start=time.process_time();controls();family=parameters();results=[];failures=[]
    checks=0;roots=Counter();spans=Counter();literal_none=[];bad_reflection=[]
    for t,p in sorted(family.items()):
        if len(results)>=5000 or time.process_time()-start>=5:
            print(json.dumps(dict(status='UNKNOWN',total=len(family),completed=len(results))));return
        C,b,D,m=fixed(p);spans[D]+=1;rows=[];best=None
        lit=algebra(p,0)[1]
        for r in range(28-D):
            checks+=6
            if checks>500000 or time.process_time()-start>=5:
                print(json.dumps(dict(status='UNKNOWN',total=len(family),completed=len(results))));return
            ok,literal,edges=algebra(p,r);other=direct(p,r)
            assert literal==lit and edges==other
            roots['bad_core' if not ok else 'completed' if edges else 'valid_core_no_completion']+=1
            rows.append(dict(root=r,core_ok=ok,edges=edges))
            if best is None and edges:
                i,j=edges[0];best=dict(root=r,first=i,last=j,witness=certificate(p,r,i,j))
        entry=dict(params=p,targets=t,fixed=C,base=b,span=D,literal_edges=lit,roots=rows)
        if best:entry['chosen']=best
        else:
            failures.append(entry)
            (bad_reflection if lit else literal_none).append(p)
        results.append(entry)
    print(json.dumps(dict(status='DIAGNOSED',total=len(family),certified=len(results)-len(failures),
        results=results,failures=failures,root_order_checks=checks,root_stats=dict(roots),
        spans=dict(spans),literal_no_order=literal_none,reflection_exhaustion=bad_reflection,
        controls='PASS',cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
