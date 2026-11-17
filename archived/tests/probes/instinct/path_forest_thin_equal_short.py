#!/usr/bin/env python3
"""B107/MI240 prereg5127704e: two infinite thin-root obstructions.

s2..12,s<t<2s,w=t+s,h=t+3s,all legal odd positives;two named s50 controls.
66 profiles,22 canonical failures,198 candidates/zero witnesses predicted.
1000 formulas/6000 offset-order or exception-root cases;2CPU sec/64MiB.
No new partitions, generic cycle solver or general low-middle theorem.
OUTCOME MI241:449 formulas/66 complete maps,22 predicted failures/repairs;
0.104920CPU sec/16834560RSS bytes. Artifact SHA256
8a6994373bb333cdfa055bfcf6e810688cc77ccc60fd49088612f10b386a1801.
"""
from collections import Counter
from itertools import permutations,product
import json
import resource
import time

import path_forest_partial_padding as validation
from path_forest_paired_resonances import capacity,prefix


def bad_offsets(s,t):
    H=3*s-t;r=2*s-t
    return {-H,-s,-r,0}


def finish(s,t,p,q,preA,preB,c,alpha,kind,**extra):
    h=t+3*s;d=[s,s,t,t,t+s];first=0 if p>=q else 1;reflected=c==alpha-1
    assert c in (alpha,alpha-1)
    A=preA;B=preB
    if reflected:
        A=[h-v for v in reversed(A)];B=[h-v for v in reversed(B)];first=1-first
    row=validation.validate(2*(h+1),d,p,q,A,B,first,False)
    row.update(s=s,t=t,h=h,d=d,p=p,q=q,alpha=alpha,root=c,kind=kind,
               preA=preA,preB=preB,reflected=reflected,**extra)
    return row


def construct(s,t,p,q):
    assert s>=2 and s<t<2*s
    h=t+3*s;H=3*s-t;K=3*(s+t);alpha=(2*h+1-max(p,q))//2
    assert min(p,q)>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=2*h-1 and not p==q==2*h-1
    assert 1<=alpha<=(H+1)//2
    family1=t==2*s-1 and alpha==1
    family2=t==s+1 and alpha==s
    assert not(family1 and family2)
    if family1:
        assert sorted((p,q))==[8*s-3,10*s-3]
        return finish(s,t,p,q,[1,2*s,5*s-1],[0,s,3*s-1,4*s-1],1,alpha,'repair_F1')
    if family2:
        assert p==q==6*s+3
        return finish(s,t,p,q,[s-1,2*s,4*s+1],[0,s,2*s+1,3*s+1],s-1,alpha,'repair_F2')
    bad=bad_offsets(s,t)
    z=next(z for z in (-alpha,1-alpha) if z not in bad)
    c=-z;A=prefix(c,(t,t));w=t+s
    B=next(prefix(0,g) for g in sorted(set(permutations((s,s,w)))) if not set(A)&set(prefix(0,g)))
    return finish(s,t,p,q,A,B,c,alpha,'canonical',z=z,bad=sorted(bad))


def geometry(M,A,B):
    direct=not set(A)&set(B);xs,word=validation.physical(M,A,B)
    assert validation.literal(M,xs)==direct
    assert validation.instrument.literal_geometry(M,set(),xs)==direct
    return direct,xs,word


def offset_control(s,t):
    h=t+3*s;H=3*s-t;w=t+s;A0=[0,t,2*t]
    orders=sorted(set(permutations((s,s,w))))
    B0=[prefix(0,g) for g in orders]
    assert B0==[[0,s,2*s,2*s+w],[0,s,s+w,2*s+w],[0,w,w+s,w+2*s]]
    differences=[{a-b for a in A0 for b in B} for B in B0]
    independent=set.intersection(*differences)&set(range(-H,1))
    assert independent==bad_offsets(s,t)
    observed=[];checks=0
    for z in range(-H,1):
        A=[a-z for a in A0];answers=[]
        for B in B0:
            direct,xs,word=geometry(2*(h+1),A,B);checks+=1;answers.append(direct)
            assert Counter(word)==Counter((word[0],word[len(B)],-2*s,-2*s,-2*t,-2*t,-2*w))
        if not any(answers):observed.append(z)
    assert set(observed)==independent
    return dict(s=s,t=t,H=H,bad=observed,checks=checks)


def complete_exception(row):
    s=row['s'];t=row['t'];h=row['h'];p=row['p'];q=row['q'];w=t+s
    d=[s,s,t,t,w];counts=[];checks=0
    for ag,bg in [((t,t),(s,s,w)),((s,s,w),(t,t))]:
        candidates=valid=0
        for x,y in product(range(h-sum(ag)+1),range(h-sum(bg)+1)):
            for ao,bo in product(sorted(set(permutations(ag))),sorted(set(permutations(bg)))):
                A=prefix(x,ao);B=prefix(y,bo);direct,xs,word=geometry(2*(h+1),A,B);checks+=1
                if Counter(word)==Counter((p,q,*(-2*z for z in d))):candidates+=1;valid+=direct
        assert candidates and not valid;counts.append(dict(candidates=candidates,valid=valid))
    return dict(s=s,t=t,p=p,q=q,kind=row['kind'],parity_roles=counts,checks=checks)


def main():
    start=time.process_time();rows=[];maps=[];counts=Counter();exception_maps=[];masks=0;checked=0
    for s in range(2,13):
        for t in range(s+1,2*s):
            h=t+3*s;K=3*(s+t);H=3*s-t;d=[s,s,t,t,t+s]
            assert capacity(d,h);masks+=32
            expected=[(4*t-1+2*a,2*t+6*s+1-2*a) for a in range(1,(H+1)//2+1)]
            literal=[(p,2*K-p) for p in range(1,K+1,2)
                     if 2*K-p<=2*h-1 and not p==2*K-p==2*h-1]
            assert sorted(expected)==literal
            rec=offset_control(s,t);maps.append(rec);checked+=rec['checks']
            for p,q in literal:
                row=construct(s,t,p,q);rows.append(row);counts[row['kind']]+=1
                if row['kind']!='canonical':exception_maps.append(complete_exception(row))
                assert len(rows)<=1000
    assert len(maps)==66 and len(exception_maps)==22
    assert counts['repair_F1']==counts['repair_F2']==11
    checked+=sum(v['checks'] for v in exception_maps)
    assert sum(v['checks'] for v in exception_maps)==1518 and checked==4290
    assert sum(v['candidates'] for row in exception_maps for v in row['parity_roles'])==198
    overlap=[v for v in exception_maps if (v['s'],v['t'])==(2,3)]
    assert {(v['p'],v['q']) for v in overlap}=={(13,17),(15,15)}
    large1=construct(50,99,397,497);large2=construct(50,51,303,303)
    assert large1['kind']=='repair_F1' and large2['kind']=='repair_F2'
    A=[1,6,11];B=[0,3,6,14];direct,xs,word=geometry(30,A,B)
    assert not direct and set(A)&set(B)=={6} and Counter(word)==Counter((21,27,-6,-6,-10,-10,-16))
    assert -1 not in (0,-4) and -1 in bad_offsets(3,5)
    reflected=next(v for v in rows if (v['s'],v['t'],v['p'],v['q'])==(3,4,21,21))
    assert reflected['kind']=='repair_F2' and reflected['reflected']
    good,prexs,preword=geometry(28,reflected['preA'],reflected['preB'])
    assert good and (preword[0],preword[len(reflected['preB'])])==(23,19)
    assert Counter(preword)!=Counter((21,21,-6,-6,-8,-8,-14))
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert len(rows)+2<=1000 and checked<=6000 and elapsed<2 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='5127704e',
                         grid_profiles=66,capacity_mask_checks=masks,
                         formula_calls=len(rows)+2,grid_formula_calls=len(rows),branches=dict(counts),
                         offset_maps=maps,offset_and_exception_cases=checked,exception_maps=exception_maps,
                         rows=rows,larger_F1=large1,larger_F2=large2,
                         endpoint_only_counterfactual=dict(A=A,B=B,positions=xs,word=word),
                         omitted_reflection=dict(positions=prexs,word=preword,geometry_valid=True,original_bag_valid=False),
                         new_E28_partitions=0,cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
