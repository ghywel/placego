#!/usr/bin/env python3
"""B44/MI104, preregistered53b45584: unmatched dominant remainder.

Fixed all-after subdivision of W when R=W-q>=Z, W<22, no matching low/
negative magnitudes. Five fixed coordinates and two item-order variables.
Tentatively all targets have a root with a compatibility edge. Algebraic
forbidden-sum graph compared to direct labels at every root/item order;
independent direct low domain and literal certificates. Retain failures;
no extra parent/allocation/root class. Caps2500 targets/500000 root-order
checks/five CPU seconds. Valid core/no-completion, variable cross-collision
and coverage-preserving wrong-sum controls. Raw outside git.
OUTCOME: 1478 targets,1476 certified; all94008 algebraic/direct root-order
comparisons agree.2 failures:(u,v,W,Z;a,b,c)=(6,7,21,2;2,4,4) and
(7,7,21,2;3,3,3), exhaustive within the fixed all-after architecture.
Root classes8998 completed/1481 valid-core-no-completion/5189 bad-core.
Controls pass. CPU0.424268 s. Raw outside git SHA256
0dbafbbd7fcf3ce822ebc5effc442e4cd0f9f074a817c84f5af7daa96fed612c.
Blind universal allocation REFUTED; no class widening.
"""
from collections import Counter,defaultdict
from itertools import combinations,combinations_with_replacement
import json
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok


def parameters():
    out={}
    for a,b,c in combinations_with_replacement(range(1,6),3):
        q=a+b+c
        for u in range(6,15):
            for v in range(u,18):
                total=u+v+q
                for W in range((total+1)//2,min(21,28-v,total-1)+1):
                    Z=total-W;R=W-q
                    if R<Z or {u,v}&{W,Z}:continue
                    t=(56+2*u,56+2*v,112-2*W,112-2*Z,112,112+2*a,112+2*b,112+2*c)
                    assert t==tuple(sorted(t));out[t]=(u,v,W,Z,a,b,c)
    low=defaultdict(list)
    for t in combinations_with_replacement(range(68,111,2),4):low[sum(t)].append(t)
    direct=set()
    for a,b,c in combinations_with_replacement(range(1,6),3):
        high=(112,112+2*a,112+2*b,112+2*c);q=a+b+c
        for xs in low[784-sum(high)]:
            u,v=(xs[0]-56)//2,(xs[1]-56)//2;W,Z=(112-xs[2])//2,(112-xs[3])//2
            if W==22 or W-q<Z or {u,v}&{W,Z}:continue
            direct.add(xs+high)
    assert set(out)==direct
    return out


def fixed(p):
    u,v,W,Z,a,b,c=p;q=a+b+c;R=W-q;A=R-u
    assert A>0 and v!=R and R>=Z
    B=(0,q,q+A,q+v,q+R);D=max(B)
    assert len(set(B))==5 and D<=22
    return B,D


def algebra(p,r):
    B,D=fixed(p);T=27-2*r;q=sum(p[-3:]);steps=p[-3:]
    core_ok=all(x+y!=T for x,y in combinations(B,2))
    F={T-b for b in B};edges=[]
    if core_ok:
        for i in range(3):
            for j in range(3):
                if i!=j and steps[i] not in F and q-steps[j] not in F and steps[i]+q-steps[j]!=T:
                    edges.append((i,j))
    return core_ok,edges


def direct(p,r):
    B,D=fixed(p);q=sum(p[-3:]);steps=p[-3:];edges=[]
    for i in range(3):
        for j in range(3):
            if i==j:continue
            points=B+(steps[i],q-steps[j]);physical=[x+r for x in points]
            assert len(set(physical))==7 and min(physical)>=0 and max(physical)<=27
            labels=[min(x,27-x) for x in physical]
            if len(set(labels))==7:edges.append((i,j))
    return edges


def certificate(p,r,i,j):
    u,v,W,Z,a,b,c=p;steps=(a,b,c);q=sum(steps);A=W-q-u;k=3-i-j
    s={5+i:r,5+k:r+steps[i],5+j:r+q-steps[j],1:r+q,0:r+q+A,3:r+q+v,2:r+W}
    t=(56+2*u,56+2*v,112-2*W,112-2*Z,112,112+2*a,112+2*b,112+2*c)
    w=materialize(t,s);assert certificate_ok(w['bins'],t);return w


def main():
    start=time.process_time();family=parameters();results=[];failures=[];checks=0;root_stats=Counter()
    bad=(6,9,13,5,1,1,1)
    assert algebra(bad,9)==(True,[]) and direct(bad,9)==[]
    cross=(6,7,14,5,1,2,3);B,D=fixed(cross);T=5;F={T-x for x in B}
    assert algebra(cross,11)[0] and 1 not in F and 4 not in F and 1+4==T
    assert (0,1) not in algebra(cross,11)[1] and (0,1) not in direct(cross,11)
    for t,p in sorted(family.items()):
        if len(results)>=2500 or time.process_time()-start>=5:
            print(json.dumps(dict(status='UNKNOWN',total=len(family),completed=len(results))));return
        B,D=fixed(p);rows=[];best=None
        for r in range(28-D):
            checks+=6
            if checks>500000 or time.process_time()-start>=5:
                print(json.dumps(dict(status='UNKNOWN',total=len(family),completed=len(results))));return
            ok,edges=algebra(p,r);other=direct(p,r);assert edges==other
            root_stats['bad_core' if not ok else 'valid_core_no_completion' if not edges else 'completed']+=1
            rows.append(dict(root=r,core_ok=ok,edges=edges))
            if best is None and edges:
                i,j=edges[0];best=dict(root=r,first=i,last=j,witness=certificate(p,r,i,j))
        entry=dict(params=p,targets=t,fixed=B,span=D,roots=rows)
        if best:entry['chosen']=best
        else:failures.append(entry)
        results.append(entry)
    sample=next(x for x in results if 'chosen' in x);bins=[set(x) for x in sample['chosen']['witness']['bins']]
    x,y=min(bins[0]),min(bins[1]);bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert Counter(x for b in bins for x in b)==Counter(range(1,56,2))
    assert not certificate_ok(bins,sample['targets'])
    print(json.dumps(dict(status='DIAGNOSED',total=len(family),certified=len(results)-len(failures),
        results=results,failures=failures,root_order_checks=checks,root_stats=dict(root_stats),
        controls='PASS',cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
