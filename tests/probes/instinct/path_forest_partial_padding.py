#!/usr/bin/env python3
"""B84/MI191 preregb4fb6292: minimal core contraction then outer padding.

Twelve formula calls/six E28 partitions and named threshold/owner controls.
1CPU sec/64MiB; no core-word, order or profile search. Infinite claim SKETCH,
depending on independently verified MI180.
OUTCOME:12 calls/6 partitions and controls pass;0.002820CPU sec,15527936RSS
bytes. Raw SHA256496b51fd8b795a09bc6bec999efa3d6cce78973fa2d17ab1c29e11f91fb8634b.
"""
from collections import Counter
import json
import resource
import time

import path_forest_coloured_chains as b79
import path_forest_balanced_bridge as instrument
from path_forest_interlaced_pairs import physical,literal


def validate(M,d,p,q,A,B,first,partition=False):
    P=(p,q)[first];Q=(p,q)[1-first]
    xs,word=physical(M,A,B)
    assert word[0]==P and word[len(B)]==Q
    assert Counter(word)==Counter((p,q,*(-2*v for v in d)))
    assert A==sorted(A) and B==sorted(B) and not set(A)&set(B)
    assert min(A+B)>=0 and max(A+B)<=M//2-1
    assert len(A)+len(B)==len(d)+2 and literal(M,xs)
    assert instrument.literal_geometry(M,set(),xs)
    assert all(u+v!=M-1 for i,u in enumerate(xs) for v in xs[i+1:])
    targets=bins=selected=None
    if partition:
        assert M==28 and len(d)==6
        e=[p,q]+[-2*v for v in d];h=[1,1]+[2]*6
        targets=[56*s+2*v for s,v in zip(h,e)]
        assert min(targets)>=68 and max(targets)<=122 and sum(targets)==784
        pool={v:[i+2 for i,w in enumerate(d) if w==v] for v in set(d)};selected={}
        for j,move in enumerate(word):
            owner=first if j==0 else 1-first if j==len(B) else pool[-move//2].pop(0)
            assert e[owner]==move;selected[owner]=xs[j]
        assert all(not v for v in pool.values())
        bins=instrument.materialize(M,set(),[0]*8,h,e,selected,targets)
        assert instrument.literal_ok(M,bins,targets,h)
        assert instrument.independent_ok(M,bins,targets)
    return dict(A=A,B=B,positions=xs,word=word,first_owner=first,targets=targets,bins=bins,selected=selected)


def construct(M,d,p,q,partition=False):
    assert M%2==0 and d and min(d)>=1 and p>0 and q>0 and p%2 and q%2
    n=M//2;N=len(d);K=sum(d);k=n-N-2
    assert k>=0 and p+q==2*K and max(p,q)<=M-3 and not p==q==M-3
    r=max(0,(K-2*N+1)//2);assert r<=k
    s=k-r;nc=N+r+2;core=None
    if K==1:
        assert N==1 and d[0]==1 and p==q==1
        row=validate(M,d,p,q,[0,1],[n-1],0,partition)
        row.update(M=M,d=d,p=p,q=q,k=k,r=r,s=s,tiny_exception=True)
        return row
    if r:
        ordered=sorted(d,reverse=True)
        assert len(ordered)>=2 and ordered[1]>=r+2
    else:ordered=list(d)
    C=2*nc-3;L=max(1,2*K-C);U=min(C,2*K-1)
    assert K<=C-1 and U-L>=2
    a=max(L,p-2*s);b=min(U,p+2*s);assert a<=b
    residue=(p-2*s)%4;x=a if a%4==residue else a+2;y=2*K-x
    assert a<=x<=b and x%4==residue and min(x,y)>0 and max(x,y)<=C
    first=0 if x>=y else 1;P0=max(x,y);Q0=min(x,y)
    if r:core=b79.sparse(2*nc,P0,Q0,ordered)
    else:core=b79.full(2*nc,P0,Q0,ordered)
    t=((p,q)[first]-P0)//2
    assert abs(t)<=s and (t-s)%2==0
    left=(s-t)//2;right=(s+t)//2
    assert left>=0 and right>=0 and left+right==s
    A=[v+left for v in core['A']];B=[v+left for v in core['B']]
    row=validate(M,d,p,q,A,B,first,partition)
    row.update(M=M,d=d,p=p,q=q,k=k,r=r,s=s,tiny_exception=False,
               core_n=nc,core=core,interval=(L,U),transport=(p-2*s,p+2*s),
               intersection=(a,b),residue=residue,x=x,y=y,t=t,left=left,right=right)
    return row


def main():
    start=time.process_time()
    fixtures=[((2,2,2,2,3,3),15,13),((2,2,2,2,3,3),21,7),
              ((1,1,2,2,4,4),19,9),((1,1,2,4,4,4),23,9),
              ((1,1,3,3,5,5),25,11),((8,8,2,2,2,2),25,23)]
    rows=[construct(28,d,p,q,True) for d,p,q in fixtures]
    rows.extend((construct(6,(1,),1,1),construct(8,(1,),1,1),construct(10,(2,),3,1),
                 construct(20,(2,2,3,3),13,7),
                 construct(60,(8,8,1,1,1,1,1,1,1,1),45,3),
                 construct(22,(1,1,2,2,2,2,3,3),17,15)))
    assert len(rows)==12 and sum(v['bins'] is not None for v in rows)==6
    assert all(sorted(v['d'],reverse=True)[1]<v['k']+2 for v in rows[:5])
    assert rows[0]['first_owner']==1 and (rows[0]['left'],rows[0]['right'])==(3,2)
    assert (rows[3]['left'],rows[3]['right'])==(4,0)
    assert (rows[4]['left'],rows[4]['right'])==(0,3)
    assert rows[5]['r']==rows[5]['k']==6 and rows[5]['s']==0
    assert rows[10]['r']==2 and rows[10]['s']==16
    assert rows[11]['r']==0 and rows[11]['s']==1 and rows[11]['first_owner']==1
    refused=[]
    for name,args in [('second_large_condition',(28,(2,2,2,2,2,7),19,15)),
                      ('doubled_longest',(28,(2,2,2,2,8,9),25,25)),
                      ('too_long',(28,fixtures[0][0],27,1))]:
        try:construct(*args)
        except AssertionError:refused.append(name)
        else:raise AssertionError('missing refusal '+name)
    outside=[0,19,15,11,7,3,18,14]
    outside_word=[v-u for u,v in zip(outside,outside[1:]+outside[:1])]
    assert literal(28,outside) and instrument.literal_geometry(28,set(),outside)
    assert Counter(outside_word)==Counter((19,15,-4,-4,-4,-4,-4,-14))
    # Ignoring mod4: wrong but legal core15/13; rounded padding2/3.
    wrong_core=b79.sparse(18,15,13,[3,3,2,2,2,2])
    wrongA=[v+2 for v in wrong_core['A']];wrongB=[v+2 for v in wrong_core['B']]
    wrongxs,wrongword=physical(28,wrongA,wrongB)
    assert literal(28,wrongxs) and instrument.literal_geometry(28,set(),wrongxs)
    assert wrongword[0]==17 and wrongword[len(wrongB)]==11
    assert Counter(wrongword)!=Counter((15,13,-4,-4,-4,-4,-6,-6))
    assert Counter(wrongword)==Counter((17,11,-4,-4,-4,-4,-6,-6))
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='b4fb6292',
                         formula_calls=12,E28_partitions=6,rows=rows,refused=refused,
                         outside_admission_positive=dict(positions=outside,word=outside_word),
                         wrong_residue_control=dict(A=wrongA,B=wrongB,positions=wrongxs,word=wrongword),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
