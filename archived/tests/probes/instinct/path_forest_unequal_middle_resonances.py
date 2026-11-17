#!/usr/bin/env python3
"""B105/MI236 prereg50b7f1b6: intersect both middle-order obstructions.

Fixed diagnostic grid/two A orders/three B orders/three explicit repairs.
4000 formulas/60000 offset-order or exception-root cases;3CPU sec/64MiB.
No generic cycle solver, new partitions or general E28 conclusion.
OUTCOME MI237:1036 formulas/413 complete offset maps,exactly three repairs;
0.341547CPU sec/19570688RSS bytes. Artifact SHA256
343075fb71404d75cf1bb822be7a0b627fd23587691f1ac99c1bd978e0c53912.
"""
from collections import Counter
from itertools import permutations,product
import json
import resource
import time

import path_forest_partial_padding as validation
import path_forest_forced_short_ownership as forced
from path_forest_paired_resonances import capacity,prefix,interval,shapes


EXCEPTIONS={(1,2,3,3,6,9,11),(1,3,4,4,8,11,15),(1,3,4,4,8,13,13)}


def bad_offsets(s,u,v,w,h):
    H=h-u-v;J=h-2*s-w;delta=J-H;bad={0,delta}
    if v==w==u+s and H>=s:bad|={-s,delta+s}
    assert all(-H<=z<=J for z in bad)
    return bad


def finish(s,u,v,w,h,p,q,preA,preB,c,alpha,kind,**extra):
    first=0 if p>=q else 1;reflected=c==alpha-1
    assert c in (alpha,alpha-1)
    A=preA;B=preB
    if reflected:
        A=[h-z for z in reversed(A)];B=[h-z for z in reversed(B)];first=1-first
    row=validation.validate(2*(h+1),[s,s,u,v,w],p,q,A,B,first,False)
    row.update(s=s,u=u,v=v,w=w,h=h,p=p,q=q,alpha=alpha,kind=kind,
               root=c,preA=preA,preB=preB,reflected=reflected,**extra)
    return row


def construct(s,u,v,w,h,p,q):
    if h<6:raise ValueError('seven vertices require seven folded labels')
    assert s>=1 and 2*s<=u<v<=w and h<2*s+u+v
    d=[s,s,u,v,w];K=sum(d)
    assert p>0 and q>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=2*h-1 and not p==q==2*h-1 and capacity(d,h)
    if w+2*s>h:
        row=forced.construct(2*(h+1),d,p,q)
        row.update(s=s,u=u,v=v,w=w,h=h,kind='forced_capacity')
        return row
    H=h-u-v;J=h-2*s-w;T=H+J
    alpha=(2*h+1-max(p,q))//2
    assert H>=0 and J>=0 and T>=2 and 1<=alpha<=((T+1)//2)<T
    lo,hi=interval(H,J,alpha);bad=bad_offsets(s,u,v,w,h)
    z=next((z for z in range(lo,min(hi,lo+4)+1) if z not in bad),None)
    if z is None:
        assert (s,u,v,w,h,min(p,q),max(p,q)) in EXCEPTIONS
        preA=[0,v,2*v]
        preB=[1,2,4,5] if u==2 else [1,2,3,6]
        return finish(s,u,v,w,h,p,q,preA,preB,1,alpha,'finite_repair',bad=sorted(bad),I=[lo,hi])
    c=alpha if alpha%2==z%2 else alpha-1
    x=(c-z)//2;y=(c+z)//2
    assert 0<=x<=H and 0<=y<=J
    for g in (u,v):
        for bs in shapes(s,w):
            preA=[x,x+g,x+u+v];preB=[y+t for t in bs]
            if not set(preA)&set(preB):
                return finish(s,u,v,w,h,p,q,preA,preB,c,alpha,'canonical',z=z,
                              chosen_middle=g,bad=sorted(bad),I=[lo,hi])
    raise AssertionError('formula predicted a free offset but all six orders collide')


def offset_control(s,u,v,w,h):
    H=h-u-v;J=h-2*s-w;aa=[[0,u,u+v],[0,v,u+v]];bs=shapes(s,w)
    assert [prefix(0,g) for g in sorted(set(permutations((u,v))))]==aa
    assert [prefix(0,g) for g in sorted(set(permutations((s,s,w))))]==bs
    difference_sets=[{a-b for a in A for b in B} for A,B in product(aa,bs)]
    common=set.intersection(*difference_sets)&set(range(-H,J+1))
    assert common==bad_offsets(s,u,v,w,h)
    order_maps=[[],[]];measured=[];checks=0
    for z in range(-H,J+1):
        x=max(0,-z);y=x+z;answers=[]
        assert 0<=x<=H and 0<=y<=J
        for i,A0 in enumerate(aa):
            A=[x+t for t in A0];one=[]
            for B0 in bs:
                B=[y+t for t in B0];direct=not set(A)&set(B)
                xs,word=validation.physical(2*(h+1),A,B)
                assert validation.literal(2*(h+1),xs)==direct
                assert validation.instrument.literal_geometry(2*(h+1),set(),xs)==direct
                assert Counter(word)==Counter((word[0],word[len(B)],-2*s,-2*s,-2*u,-2*v,-2*w))
                one.append(direct);answers.append(direct);checks+=1
            if not any(one):order_maps[i].append(z)
        if not any(answers):measured.append(z)
    assert set(measured)==common
    return dict(s=s,u=u,v=v,w=w,h=h,H=H,J=J,bad=measured,
                per_middle_bad=order_maps,checks=checks)


def complete_exception(key):
    s,u,v,w,h,p,q=key;M=2*(h+1);counts=[];checks=0
    for ag,bg in [((u,v),(s,s,w)),((s,s,w),(u,v))]:
        candidates=valid=0
        for x,y in product(range(h-sum(ag)+1),range(h-sum(bg)+1)):
            for ao,bo in product(sorted(set(permutations(ag))),sorted(set(permutations(bg)))):
                A=prefix(x,ao);B=prefix(y,bo);xs,word=validation.physical(M,A,B)
                direct=not set(A)&set(B);checks+=1
                assert validation.literal(M,xs)==direct
                assert validation.instrument.literal_geometry(M,set(),xs)==direct
                if Counter(word)==Counter((p,q,-2*s,-2*s,-2*u,-2*v,-2*w)):
                    candidates+=1;valid+=direct
        assert candidates and valid==0
        counts.append(dict(candidates=candidates,valid=valid))
    return dict(key=key,parity_roles=counts,checks=checks)


def main():
    start=time.process_time();rows=[];offsets=[];profiles=capacity_checks=checked=0
    counts=Counter();exceptions=[]
    for s in range(1,4):
        for u in range(2*s,2*s+3):
            for v in range(u+1,u+4):
                for w in range(v,u+v+s):
                    for h in range(max(6,u+v),2*s+u+v):
                        profiles+=1;capacity_checks+=32;d=[s,s,u,v,w]
                        if not capacity(d,h):continue
                        if w+2*s<=h:
                            rec=offset_control(s,u,v,w,h);offsets.append(rec);checked+=rec['checks']
                        K=sum(d)
                        for p in range(1,K+1,2):
                            q=2*K-p
                            if q>2*h-1 or p==q==2*h-1:continue
                            row=construct(s,u,v,w,h,p,q);rows.append(row);counts[row['kind']]+=1
                            if row['kind']=='finite_repair':exceptions.append((s,u,v,w,h,p,q))
                            assert len(rows)<=4000 and checked<=60000
    assert set(exceptions)==EXCEPTIONS and len(exceptions)==3
    exception_maps=[complete_exception(key) for key in sorted(EXCEPTIONS)]
    checked+=sum(v['checks'] for v in exception_maps)
    assert checked<=60000 and counts['forced_capacity']>0
    named=next(v for v in rows if (v['s'],v['u'],v['v'],v['w'],v['h'],v['p'],v['q'])==(2,4,5,9,12,21,23))
    assert named['kind']=='forced_capacity'
    asymmetry=next(v for v in offsets if (v['s'],v['u'],v['v'],v['w'],v['h'])==(1,2,4,4,7))
    assert -1 not in asymmetry['per_middle_bad'][0] and -1 in asymmetry['per_middle_bad'][1]
    badA=[1,2,5];badB=[0,2,3,6];xs,word=validation.physical(14,badA,badB)
    assert Counter(word)==Counter((9,11,-2,-2,-4,-6,-6))
    assert set(badA)&set(badB)=={2} and not validation.literal(14,xs)
    assert not validation.instrument.literal_geometry(14,set(),xs)
    larger=construct(4,8,12,12,26,33,47);assert larger['kind']=='canonical'
    try:construct(1,2,2,2,5,7,9)
    except ValueError:small_refused=True
    else:raise AssertionError('missing small-label refusal')
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert len(rows)+1<=4000 and elapsed<3 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='50b7f1b6',
                         grid_profiles=profiles,capacity_mask_checks=capacity_checks,
                         formula_calls=len(rows)+1,grid_formula_calls=len(rows),branches=dict(counts),
                         canonical_profile_maps=offsets,offset_and_exception_cases=checked,
                         exception_maps=exception_maps,rows=rows,larger_resonance_control=larger,
                         middle_order_counterfactual=asymmetry,small_label_control_refused=small_refused,
                         old_repair_collision=dict(A=badA,B=badB,positions=xs,word=word),
                         new_E28_partitions=0,cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
