#!/usr/bin/env python3
"""B108/MI242 prereg0d585d5a: remaining equal-short/forced-constant cases.

Fixed s1..4,low-middle grid;12 predicted canonical failures.
4000 formulas/60000 offset-order or exception-root cases;3CPU sec/64MiB.
No new partitions, generic cycle solver or global residual census.
OUTCOME MI243:1221 formulas/489 complete maps,12 predicted failures/repairs;
0.397857CPU sec/19689472RSS bytes. Artifact SHA256
53a8c40c854e7272aa232c3ecac3f57ac36e3fa4bc64a34b4301d31cc21da89c.
"""
from collections import Counter
from itertools import permutations,product
import json
import resource
import time

import path_forest_partial_padding as validation
import path_forest_thin_equal_short as thin
from path_forest_paired_resonances import capacity,prefix,interval
from path_forest_unequal_short_cycle import partners


FIXED={((2,2,3,3,3),8,11,15),((2,2,3,3,3),8,13,13),((2,2,3,3,3),9,9,17),
       ((2,2,3,5,5),10,15,19),((2,2,3,5,5),10,17,17),((2,2,3,5,5),11,13,21)}


def select_partner(d,h):
    fits=partners(d,h);assert fits
    choice=next((v for v in fits if not v['constant']),fits[0]).copy()
    r=choice['r'];D=choice['remaining'];X=choice['X'];Y=choice['Y'];w=d[-1]
    assert X<min(D) and Y<r
    choice['comparison']='nonconstant'
    if choice['constant']:
        t=D[0]
        if r<t:
            assert w+t>h and X<t-r and Y<r;choice['comparison']='r_lt_t'
        elif r==t:
            assert X<t and Y<t;choice['comparison']='r_eq_t'
        else:
            assert w+t<=h and h<r+2*t and Y<r-t and X<2*t-r
            choice['comparison']='r_gt_t'
    return choice


def bad_offsets(d,h):
    s,_,u,v,w=d;H=h-u-v;J=h-2*s-w;delta=J-H;bad={0,delta}
    if u==v:
        extra=w in (u,u+s) and H>=s
    else:extra=v==w==u+s and H>=s
    if extra:bad|={-s,delta+s}
    assert all(-H<=z<=J for z in bad)
    return bad


def finish(d,h,p,q,A,B,c,alpha,kind,**extra):
    preA=A;preB=B;first=0 if p>=q else 1;reflected=c==alpha-1
    assert c in (alpha,alpha-1)
    if reflected:
        A=[h-v for v in reversed(A)];B=[h-v for v in reversed(B)];first=1-first
    row=validation.validate(2*(h+1),d,p,q,A,B,first,False)
    row.update(d=d,h=h,p=p,q=q,kind=kind,alpha=alpha,root=c,
               preA=preA,preB=preB,reflected=reflected,**extra)
    return row


def construct(d,h,p,q):
    s,s0,u,v,w=d;K=sum(d)
    assert list(d)==sorted(d) and s==s0 and s>=1 and s<=u<2*s
    assert h>=6 and 2*s+u+v>h and capacity(d,h)
    assert p>0 and q>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=2*h-1 and not p==q==2*h-1
    alpha=(2*h+1-max(p,q))//2
    if w+2*s<=h:
        H=h-u-v;J=h-2*s-w;T=H+J
        assert H>=0 and J>=0 and T>=2 and 1<=alpha<=((T+1)//2)<T
        lo,hi=interval(H,J,alpha);bad=bad_offsets(d,h)
        z=next((z for z in range(lo,min(hi,lo+4)+1) if z not in bad),None)
        if z is None:
            if u==v and w==u+s and J==0:
                row=thin.construct(s,u,p,q);row['kind']='thin_'+row['kind'];return row
            assert (tuple(d),h,min(p,q),max(p,q)) in FIXED
            A=[1,3,6] if w==3 else [1,3,8]
            B=[0,2,5,8] if w==3 else [0,2,5,10]
            return finish(d,h,p,q,A,B,1,alpha,'fixed_repair')
        c=alpha if z%2==alpha%2 else alpha-1;x=(c-z)//2;y=(c+z)//2
        assert 0<=x<=H and 0<=y<=J
        for ao,bo in product(sorted(set(permutations((u,v)))),sorted(set(permutations((s,s,w))))):
            A=prefix(x,ao);B=prefix(y,bo)
            if not set(A)&set(B):return finish(d,h,p,q,A,B,c,alpha,'canonical',z=z)
        raise AssertionError('free offset has no local-order witness')
    choice=select_partner(d,h);r=choice['r'];D=choice['remaining'];X=choice['X'];Y=choice['Y']
    T=X+Y;assert T>=2 and 1<=alpha<=((T+1)//2)<T
    lo,hi=interval(X,Y,alpha)
    z=next(z for z in range(lo,min(hi,lo+2)+1) if z not in (0,Y-X))
    c=alpha if z%2==alpha%2 else alpha-1;x=(c-z)//2;y=(c+z)//2;F=r-z
    assert 0<F<sum(D)
    if choice['constant']:
        t=D[0];assert F not in (t,2*t)
    bo=next(bo for bo in sorted(set(permutations(D))) if F not in prefix(0,bo)[1:-1])
    return finish(d,h,p,q,prefix(x,(r,w)),prefix(y,bo),c,alpha,
                  'forced_'+choice['comparison'],z=z,partner=choice,forbidden_prefix=F)


def geometry(M,A,B):
    direct=not set(A)&set(B);xs,word=validation.physical(M,A,B)
    assert validation.literal(M,xs)==direct
    assert validation.instrument.literal_geometry(M,set(),xs)==direct
    return direct,xs,word


def offset_control(d,h,forced):
    s,_,u,v,w=d;M=2*(h+1)
    if forced:
        choice=select_partner(d,h);H=choice['X'];J=choice['Y'];bad={0,J-H}
        aos=[(choice['r'],w)];bos=sorted(set(permutations(choice['remaining'])))
    else:
        H=h-u-v;J=h-2*s-w;bad=bad_offsets(d,h)
        aos=sorted(set(permutations((u,v))));bos=sorted(set(permutations((s,s,w))))
    shapes=[(prefix(0,a),prefix(0,b)) for a,b in product(aos,bos)]
    diffs=[{a-b for a in A for b in B} for A,B in shapes]
    assert set.intersection(*diffs)&set(range(-H,J+1))==bad
    observed=[];checks=0
    for z in range(-H,J+1):
        x=max(0,-z);y=x+z;assert 0<=x<=H and 0<=y<=J;answers=[]
        for A0,B0 in shapes:
            A=[x+a for a in A0];B=[y+b for b in B0]
            direct,xs,word=geometry(M,A,B);checks+=1;answers.append(direct)
            assert Counter(word)==Counter((word[0],word[len(B)],*(-2*t for t in d)))
        if not any(answers):observed.append(z)
    assert set(observed)==bad
    return dict(d=d,h=h,forced=forced,H=H,J=J,bad=observed,checks=checks)


def complete_exception(row):
    d=row['d'];s,_,u,v,w=d;h=row['h'];p=row['p'];q=row['q'];checks=0;counts=[]
    for ag,bg in [((u,v),(s,s,w)),((s,s,w),(u,v))]:
        candidates=valid=0
        for x,y in product(range(h-sum(ag)+1),range(h-sum(bg)+1)):
            for ao,bo in product(sorted(set(permutations(ag))),sorted(set(permutations(bg)))):
                direct,xs,word=geometry(2*(h+1),prefix(x,ao),prefix(y,bo));checks+=1
                if Counter(word)==Counter((p,q,*(-2*t for t in d))):candidates+=1;valid+=direct
        assert candidates and not valid;counts.append(dict(candidates=candidates,valid=valid))
    return dict(d=d,h=h,p=p,q=q,kind=row['kind'],parity_roles=counts,checks=checks)


def main():
    start=time.process_time();profiles=masks=checked=0;rows=[];maps=[];counts=Counter();failures=[]
    constant_five_maps=0
    for s in range(1,5):
        for u in range(s,2*s):
            for v in range(u,u+3):
                for w in range(v,v+s+1):
                    d=[s,s,u,v,w];K=sum(d)
                    for h in range(max(6,u+v,w),2*s+u+v):
                        profiles+=1;masks+=32;fits=capacity(d,h)
                        if not fits:continue
                        forced=w+2*s>h
                        if forced:
                            for mask in fits:assert (mask if mask&16 else mask^31).bit_count()==2
                        rec=offset_control(d,h,forced);maps.append(rec);checked+=rec['checks']
                        if len(set(d))==1:
                            assert not forced and set(rec['bad'])=={-s,0};constant_five_maps+=1
                        for p in range(1,K+1,2):
                            q=2*K-p
                            if q>2*h-1 or p==q==2*h-1:continue
                            row=construct(d,h,p,q);rows.append(row);counts[row['kind']]+=1
                            if 'repair' in row['kind']:failures.append(row)
                            assert len(rows)<=4000 and checked<=60000
    expected=set(FIXED)
    for s in (2,3,4):
        expected.add(((s,s,2*s-1,2*s-1,3*s-1),5*s-1,8*s-3,10*s-3))
        expected.add(((s,s,s+1,s+1,2*s+1),4*s+1,6*s+3,6*s+3))
    assert len(failures)==12 and {(tuple(v['d']),v['h'],v['p'],v['q']) for v in failures}==expected
    exceptions=[complete_exception(row) for row in failures];checked+=sum(v['checks'] for v in exceptions)
    assert constant_five_maps>0 and checked<=60000
    equal=next(v for v in rows if v['d']==[2,2,2,2,4] and (v['h'],v['p'],v['q'])==(7,11,13))
    larger=next(v for v in rows if v['d']==[4,4,4,5,5] and (v['h'],v['p'],v['q'])==(12,21,23))
    assert equal['kind']=='forced_r_eq_t' and larger['kind']=='forced_r_gt_t'
    control=next(v for v in rows if v['d']==[2,2,2,3,5] and (v['h'],v['p'],v['q'])==(8,13,15))
    assert control['kind']=='forced_nonconstant' and control['partner']['r']==2
    A=[0,3,8];B=[1,3,5,7];direct,xs,word=geometry(18,A,B)
    assert not direct and set(A)&set(B)=={3} and Counter(word)==Counter((13,15,-4,-4,-4,-6,-10))
    outside=construct([10,10,10,11,11],30,45,59);assert outside['kind']=='forced_r_gt_t'
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert len(rows)+1<=4000 and elapsed<3 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='0d585d5a',
                         grid_profiles=profiles,capacity_mask_checks=masks,formula_calls=len(rows)+1,
                         grid_formula_calls=len(rows),branches=dict(counts),offset_maps=maps,
                         constant_five_maps=constant_five_maps,offset_and_exception_cases=checked,
                         exception_maps=exceptions,rows=rows,outside_larger_partner=outside,
                         naive_constant_partner=dict(A=A,B=B,positions=xs,word=word),
                         new_E28_partitions=0,cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
