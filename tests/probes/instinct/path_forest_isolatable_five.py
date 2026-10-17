#!/usr/bin/env python3
"""B109/MI244 prereg9274c23c: isolated-largest nonconstant companion.

Fixed four-companion1..3 grid and four named t50 formulas.
Five predicted isolated-allocation failures,all repaired explicitly.
1500 formulas/30000 offset-order or exception-root cases;3CPU sec/64MiB.
Rich case depends on MI204 SKETCH;no new partitions/global census.
OUTCOME MI245:707 formulas/192 complete maps,five predicted failures/repairs;
0.228932CPU sec/17154048RSS bytes. Artifact SHA256
a33a9b32e71e6b149c3cb8d0c41c2624287765f79da7d8164a108ebb4598a787.
"""
from collections import Counter
from itertools import combinations_with_replacement,permutations,product
import json
import resource
import time

import path_forest_partial_padding as validation
from path_forest_paired_resonances import capacity,prefix,interval


def near_constant(B):
    counts=Counter(B)
    if max(counts.values())==4:raise ValueError('constant companions already covered by MI218')
    if max(counts.values())==3:
        s=next(v for v,n in counts.items() if n==3);t=next(v for v in counts if v!=s)
        return s,t
    return None


def bad_offsets(B,D,h):
    S=sum(B);H=h-D;J=h-S;bad={-S,0,D-S,D};near=near_constant(B)
    if near:
        s,t=near
        if D%s==t%s:bad|={z for z in range(D-S+1,0) if z%s==0}
    return {z for z in bad if -H<=z<=J}


def finish(B,D,h,p,q,A,Bchain,c,alpha,kind,**extra):
    d=list(B)+[D];preA=A;preB=Bchain;first=0 if p>=q else 1;reflected=c==alpha-1
    assert c in (alpha,alpha-1)
    if reflected:
        A=[h-z for z in reversed(A)];Bchain=[h-z for z in reversed(Bchain)];first=1-first
    row=validation.validate(2*(h+1),d,p,q,A,Bchain,first,False)
    row.update(d=d,h=h,p=p,q=q,kind=kind,alpha=alpha,root=c,
               preA=preA,preB=preB,reflected=reflected,**extra)
    return row


def repair(B,D,h,p,q,alpha):
    assert list(B[:3])==[1,1,1];t=B[3];pair=sorted((p,q))
    if D==t and h==t+3 and t>=3:
        if pair==[2*t+1,2*t+5]:kind='U1'
        else:assert p==q==2*t+3;kind='U2'
        return finish(B,D,h,p,q,[0,t,t+1],[1,2,t+2,t+3],1,alpha,kind)
    if D==t and h==t+4 and t>=2:
        assert p==q==2*t+3
        if t==2:return finish(B,D,h,p,q,[3,5,6],[0,1,2,4],3,alpha,'U3_small')
        return finish(B,D,h,p,q,[2,3,t+3],[0,1,t+1,t+2],2,alpha,'U3')
    assert D==t+1 and h==t+3 and t>=3 and pair==[2*t+3,2*t+5]
    return finish(B,D,h,p,q,[0,t+1,t+2],[1,2,3,t+3],1,alpha,'U4')


def construct(B,D,h,p,q):
    B=list(B);near=near_constant(B);S=sum(B);K=S+D;H=h-D;J=h-S
    assert len(B)==4 and B==sorted(B) and min(B)>0 and D>=max(B)
    assert h>=6 and H>=0 and J>=0 and min(p,q)>0 and p%2 and q%2
    assert p+q==2*K and max(p,q)<=2*h-1 and not p==q==2*h-1
    T=H+J;alpha=(2*h+1-max(p,q))//2;assert T>=2 and 1<=alpha<=((T+1)//2)<T
    lo,hi=interval(H,J,alpha);bad=bad_offsets(B,D,h);assert len(bad)<=6
    z=next((z for z in range(lo,min(hi,lo+6)+1) if z not in bad),None)
    if z is None:return repair(B,D,h,p,q,alpha)
    c=alpha if z%2==alpha%2 else alpha-1;x=(c-z)//2;y=(c+z)//2
    assert 0<=x<=H and 0<=y<=J
    A=[x,x+D]
    order=next(order for order in sorted(set(permutations(B))) if not set(A)&set(prefix(y,order)))
    return finish(B,D,h,p,q,A,prefix(y,order),c,alpha,'isolated',z=z,bad=sorted(bad),near_constant=near)


def geometry(M,A,B):
    direct=not set(A)&set(B);xs,word=validation.physical(M,A,B)
    assert validation.literal(M,xs)==direct
    assert validation.instrument.literal_geometry(M,set(),xs)==direct
    return direct,xs,word


def offset_control(B,D,h):
    S=sum(B);H=h-D;J=h-S;A0=[0,D];bos=sorted(set(permutations(B)))
    shapes=[prefix(0,g) for g in bos];diffs=[{a-b for a in A0 for b in shape} for shape in shapes]
    independent=set.intersection(*diffs)&set(range(-H,J+1));bad=bad_offsets(B,D,h)
    assert independent==bad
    if S+D<=h:assert {-S,D}<=bad
    observed=[];checks=0
    for z in range(-H,J+1):
        x=max(0,-z);y=x+z;assert 0<=x<=H and 0<=y<=J;answers=[]
        A=[x,x+D]
        for shape in shapes:
            Bc=[y+t for t in shape];direct,xs,word=geometry(2*(h+1),A,Bc)
            assert Counter(word)==Counter((word[0],word[len(Bc)],*(-2*t for t in list(B)+[D])))
            answers.append(direct);checks+=1
        if not any(answers):observed.append(z)
    assert set(observed)==bad
    return dict(companions=B,D=D,h=h,H=H,J=J,bad=observed,checks=checks)


def complete_failure(row):
    d=row['d'];B=d[:-1];D=d[-1];h=row['h'];p=row['p'];q=row['q'];counts=[];checks=0
    for ag,bg in [((D,),B),(B,(D,))]:
        candidates=valid=0
        for x,y in product(range(h-sum(ag)+1),range(h-sum(bg)+1)):
            for ao,bo in product(sorted(set(permutations(ag))),sorted(set(permutations(bg)))):
                A=prefix(x,ao);Bc=prefix(y,bo);direct,xs,word=geometry(2*(h+1),A,Bc);checks+=1
                if Counter(word)==Counter((p,q,*(-2*t for t in d))):candidates+=1;valid+=direct
        assert candidates and not valid;counts.append(dict(candidates=candidates,valid=valid))
    return dict(d=d,h=h,p=p,q=q,kind=row['kind'],parity_roles=counts,checks=checks)


def main():
    start=time.process_time();profiles=masks=checked=low_total_questions=0;rows=[];maps=[];counts=Counter();failures=[]
    for B in combinations_with_replacement(range(1,4),4):
        if len(set(B))==1:continue
        S=sum(B)
        for D in range(max(B),max(B)+4):
            for h in range(max(6,S,D),max(6,S,D)+4):
                profiles+=1;masks+=32;d=list(B)+[D];K=sum(d);assert capacity(d,h)
                rec=offset_control(list(B),D,h);maps.append(rec);checked+=rec['checks']
                for p in range(1,K+1,2):
                    q=2*K-p
                    if q>2*h-1 or p==q==2*h-1:continue
                    row=construct(B,D,h,p,q);rows.append(row);counts[row['kind']]+=1
                    low_total_questions+=K<=h
                    if row['kind']!='isolated':failures.append(row)
                    assert len(rows)<=1500 and checked<=30000
    assert len(failures)==5 and {v['kind'] for v in failures}=={'U1','U2','U3','U3_small','U4'}
    assert low_total_questions>0
    failure_maps=[complete_failure(row) for row in failures];checked+=sum(v['checks'] for v in failure_maps)
    assert checked<=30000
    large=[construct([1,1,1,50],50,53,101,105),construct([1,1,1,50],50,53,103,103),
           construct([1,1,1,50],50,54,103,103),construct([1,1,1,50],51,53,103,105)]
    assert [v['kind'] for v in large]==['U1','U2','U3','U4']
    A=[1,4];B=[0,1,2,3,6];direct,xs,word=geometry(14,A,B)
    assert not direct and set(A)&set(B)=={1} and Counter(word)==Counter((7,11,-2,-2,-2,-6,-6))
    wrongA=[2,3,5];wrongB=[0,1,3,4];direct,wrongxs,wrongword=geometry(14,wrongA,wrongB)
    assert not direct and set(wrongA)&set(wrongB)=={3}
    postA=[6-z for z in reversed(wrongA)];postB=[6-z for z in reversed(wrongB)]
    direct,postxs,postword=geometry(14,postA,postB)
    assert not direct and Counter(postword)==Counter((7,7,-2,-2,-2,-4,-4))
    r=next(v for v in failures if v['kind']=='U2')
    direct,prexs,preword=geometry(14,r['preA'],r['preB'])
    assert direct and (preword[0],preword[len(r['preB'])])==(11,7)
    assert Counter(preword)!=Counter((9,9,-2,-2,-2,-6,-6))
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert len(rows)+4<=1500 and elapsed<3 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='9274c23c',
                         grid_profiles=profiles,capacity_mask_checks=masks,formula_calls=len(rows)+4,
                         grid_formula_calls=len(rows),branches=dict(counts),K_le_h_questions=low_total_questions,
                         offset_maps=maps,offset_and_exception_cases=checked,failure_maps=failure_maps,rows=rows,
                         large_formulas=large,naive_isolated=dict(A=A,B=B,positions=xs,word=word),
                         wrong_small_repair=dict(preA=wrongA,preB=wrongB,preword=wrongword,postword=postword),
                         omitted_reflection=dict(positions=prexs,word=preword,geometry_valid=True,original_bag_valid=False),
                         new_E28_partitions=0,cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
