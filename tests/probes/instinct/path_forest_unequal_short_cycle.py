#!/usr/bin/env python3
"""B106/MI238 prereg9fd542e7: six-cycle and one forced partner.

Sorted unequal-short nonisolatable five-gap sufficiency, PROOF-SKETCH.
Fixed grid/full canonical and forced offset maps/three named controls.
6000 formulas/100000 offset-order or exception-root cases;4CPU sec/64MiB.
No new E28 partitions, generic cycle solver or global residual count.
OUTCOME MI239:1578 formulas/787 complete maps and uniform repair pass;
0.561394CPU sec/18821120RSS bytes. Artifact SHA256
b199240da3750b789fb210798ba85d17bef7c5b34f798ddf81b91a39bf687dd9.
"""
from collections import Counter
from itertools import permutations,product
import json
import resource
import time

import path_forest_partial_padding as validation
from path_forest_paired_resonances import capacity,prefix,interval


def partners(d,h):
    small=d[:-1];w=d[-1];out=[]
    for r in sorted(set(small),reverse=True):
        rem=small.copy();rem.remove(r)
        if w+r<=h and sum(rem)<=h:
            out.append(dict(r=r,remaining=rem,X=h-w-r,Y=h-sum(rem),constant=len(set(rem))==1))
    return out


def selected_partner(d,h):
    fits=partners(d,h);assert fits
    choice=next((v for v in fits if not v['constant']),fits[0])
    r=choice['r'];D=choice['remaining'];X=choice['X'];Y=choice['Y']
    assert X<min(D) and Y<r
    if choice['constant']:
        a,b,u,v,w=d;assert r==a and b==u==v and w+b>h
        assert X<b-a and Y<a
    return choice


def bad_offsets(d,h):
    a,b,u,v,w=d;H=h-u-v;J=h-a-b-w
    bad={0,J-H}
    if u==v==b and w==a+b:bad.add(-a)
    assert all(-H<=z<=J for z in bad)
    return bad


def finish(d,h,p,q,preA,preB,c,alpha,kind,**extra):
    first=0 if p>=q else 1;reflected=c==alpha-1
    assert c in (alpha,alpha-1)
    A=preA;B=preB
    if reflected:
        A=[h-z for z in reversed(A)];B=[h-z for z in reversed(B)];first=1-first
    row=validation.validate(2*(h+1),d,p,q,A,B,first,False)
    row.update(d=d,h=h,p=p,q=q,alpha=alpha,root=c,kind=kind,
               preA=preA,preB=preB,reflected=reflected,**extra)
    return row


def construct(d,h,p,q):
    if h<6:raise ValueError('seven vertices require seven folded labels')
    a,b,u,v,w=d;C=a+b;L=u+v;K=sum(d)
    assert list(d)==sorted(d) and 0<a<b and C+L>h and capacity(d,h)
    assert p>0 and q>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=2*h-1 and not p==q==2*h-1
    alpha=(2*h+1-max(p,q))//2
    if w+C<=h:
        H=h-L;J=h-w-C;T=H+J
        assert H>=0 and J>=0 and T>=2 and 1<=alpha<=((T+1)//2)<T
        lo,hi=interval(H,J,alpha);bad=bad_offsets(d,h)
        z=next((z for z in range(lo,min(hi,lo+3)+1) if z not in bad),None)
        if z is None:
            assert a==1 and u==v==b and w==b+1 and h==2*b+2
            assert sorted((p,q))==[4*b+1,4*b+3] and alpha==1
            return finish(d,h,p,q,[0,b,2*b+1],[1,b+1,b+2,2*b+2],1,alpha,'uniform_repair',bad=sorted(bad),I=[lo,hi])
        c=alpha if z%2==alpha%2 else alpha-1;x=(c-z)//2;y=(c+z)//2
        assert 0<=x<=H and 0<=y<=J
        A=prefix(x,(u,v))
        B=next(prefix(y,order) for order in sorted(set(permutations((a,b,w))))
               if not set(A)&set(prefix(y,order)))
        return finish(d,h,p,q,A,B,c,alpha,'canonical',z=z,bad=sorted(bad),I=[lo,hi])
    choice=selected_partner(d,h);r=choice['r'];D=choice['remaining']
    X=choice['X'];Y=choice['Y'];T=X+Y;assert T>=2 and 1<=alpha<=((T+1)//2)<T
    lo,hi=interval(X,Y,alpha)
    z=next(z for z in range(lo,min(hi,lo+2)+1) if z not in (0,Y-X))
    c=alpha if z%2==alpha%2 else alpha-1;x=(c-z)//2;y=(c+z)//2
    F=r-z;R=sum(D);assert 0<F<R
    order=next(order for order in sorted(set(permutations(D))) if F not in prefix(0,order)[1:-1])
    return finish(d,h,p,q,prefix(x,(r,w)),prefix(y,order),c,alpha,
                  'forced_constant' if choice['constant'] else 'forced_nonconstant',
                  z=z,partner=choice,fitting_partners=partners(d,h),forbidden_prefix=F)


def geometry(M,A,B):
    direct=not set(A)&set(B);xs,word=validation.physical(M,A,B)
    assert validation.literal(M,xs)==direct
    assert validation.instrument.literal_geometry(M,set(),xs)==direct
    return direct,word


def offset_control(d,h,forced=False):
    a,b,u,v,w=d;M=2*(h+1)
    if forced:
        choice=selected_partner(d,h);r=choice['r'];D=choice['remaining']
        H=choice['X'];J=choice['Y'];ag=(r,w);orders=sorted(set(permutations(D)));bad={0,J-H}
    else:
        H=h-u-v;J=h-a-b-w;ag=(u,v);orders=sorted(set(permutations((a,b,w))));bad=bad_offsets(d,h)
    A0=prefix(0,ag);B0=[prefix(0,g) for g in orders]
    differences=[{a-b for a in A0 for b in B} for B in B0]
    independent=set.intersection(*differences)&set(range(-H,J+1));assert independent==bad
    observed=[];checks=0
    for z in range(-H,J+1):
        x=max(0,-z);y=x+z;assert 0<=x<=H and 0<=y<=J
        A=[x+t for t in A0];answers=[]
        for B in B0:
            B=[y+t for t in B];direct,word=geometry(M,A,B);checks+=1
            assert Counter(word)==Counter((word[0],word[len(B)],*(-2*t for t in d)))
            answers.append(direct)
        if not any(answers):observed.append(z)
    assert set(observed)==bad
    return dict(d=d,h=h,forced=forced,H=H,J=J,bad=observed,order_count=len(orders),checks=checks)


def complete_exception(d,h,p,q):
    a,b,u,v,w=d;M=2*(h+1);checks=0;counts=[]
    for ag,bg in [((u,v),(a,b,w)),((a,b,w),(u,v))]:
        candidates=valid=0
        for x,y in product(range(h-sum(ag)+1),range(h-sum(bg)+1)):
            for ao,bo in product(sorted(set(permutations(ag))),sorted(set(permutations(bg)))):
                A=prefix(x,ao);B=prefix(y,bo);direct,word=geometry(M,A,B);checks+=1
                if Counter(word)==Counter((p,q,*(-2*t for t in d))):candidates+=1;valid+=direct
        assert candidates and not valid;counts.append(dict(candidates=candidates,valid=valid))
    return dict(d=d,h=h,p=p,q=q,parity_roles=counts,checks=checks)


def main():
    start=time.process_time();rows=[];profiles=mask_checks=checked=0;maps=[];counts=Counter();exception_rows=[]
    identifications=Counter()
    for a in range(1,3):
        for b in range(a+1,a+4):
            for u in range(b,b+3):
                for v in range(u,u+3):
                    for w in range(v,v+4):
                        d=[a,b,u,v,w];C=a+b;L=u+v;K=sum(d)
                        for h in range(max(6,L,w),C+L):
                            profiles+=1;mask_checks+=32;fits=capacity(d,h)
                            if not fits:continue
                            is_forced=w+C>h
                            if is_forced:
                                for mask in fits:
                                    oriented=mask if mask&16 else mask^31
                                    assert oriented.bit_count()==2
                            rec=offset_control(d,h,is_forced);maps.append(rec);checked+=rec['checks']
                            if not is_forced:
                                if w==b:identifications['w_equals_b']+=1
                                if w==C:identifications['w_equals_C']+=1
                            for p in range(1,K+1,2):
                                q=2*K-p
                                if q>2*h-1 or p==q==2*h-1:continue
                                row=construct(d,h,p,q);rows.append(row);counts[row['kind']]+=1
                                if row['kind']=='uniform_repair':exception_rows.append((d,h,p,q))
                                assert len(rows)<=6000 and checked<=100000
    expected={(tuple([1,b,b,b,b+1]),2*b+2,4*b+1,4*b+3) for b in (2,3,4)}
    assert {(tuple(d),h,p,q) for d,h,p,q in exception_rows}==expected and len(exception_rows)==3
    exceptions=[complete_exception(*args) for args in exception_rows];checked+=sum(v['checks'] for v in exceptions)
    assert identifications['w_equals_b'] and identifications['w_equals_C']
    inside=next(v for v in rows if v['d']==[1,3,3,3,6] and (v['h'],v['p'],v['q'])==(9,15,17))
    assert inside['kind']=='forced_nonconstant' and inside['partner']['r']==3
    constant=construct([1,4,4,4,9],12,21,23)
    assert constant['kind']=='forced_constant' and constant['partner']['r']==1
    assert len(constant['fitting_partners'])==1
    alternative=construct([2,4,4,4,9],13,23,23)
    assert alternative['kind']=='forced_nonconstant' and alternative['partner']['r']==4
    larger=construct([1,10,10,10,11],22,41,43);assert larger['kind']=='uniform_repair'
    A=[2,4,13];B=[0,4,8,12];direct,word=geometry(28,A,B)
    assert not direct and set(A)&set(B)=={4} and Counter(word)==Counter((23,23,-4,-8,-8,-8,-18))
    try:construct([1,1,2,2,2],5,7,9)
    except ValueError:small_refused=True
    else:raise AssertionError('small-label fixture not refused')
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert len(rows)+3<=6000 and checked<=100000 and elapsed<4 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='9fd542e7',
                         grid_profiles=profiles,capacity_mask_checks=mask_checks,
                         formula_calls=len(rows)+3,grid_formula_calls=len(rows),branches=dict(counts),
                         offset_maps=maps,offset_and_exception_cases=checked,exception_maps=exceptions,
                         vertex_identifications=dict(identifications),rows=rows,
                         named_constant=constant,named_alternative=alternative,larger_repair=larger,
                         naive_partner_collision=dict(A=A,B=B,word=word),small_label_refused=small_refused,
                         new_E28_partitions=0,cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
