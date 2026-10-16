#!/usr/bin/env python3
"""B85/MI193 preregbfe20e26: merge several refined gaps into one D.

Twelve formula calls/six E28 partitions, two admission refusals with positive
controls, one over-deletion control.1CPU sec/64MiB. No search or census.
MI180 full parent PROVED; new merge/reversal and MI191 selector SKETCH.
OUTCOME:12 calls/6 partitions and controls pass;0.002849CPU sec,18489344RSS
bytes. Raw SHA256f6acd01680a04588b20faf398cb141957206442d6c0ddf40276400cac11e6ac2.
"""
from collections import Counter
import json
import resource
import time

import path_forest_coloured_chains as b79
import path_forest_partial_padding as b84
import path_forest_balanced_bridge as instrument
from path_forest_crossing_pairs import construct as crossing
from path_forest_interlaced_pairs import physical,literal


def construct(M,d,p,q,partition=False):
    assert M%2==0 and d and min(d)>=1 and p>0 and q>0 and p%2 and q%2
    n=M//2;N=len(d);K=sum(d);k=n-N-2
    assert k>=0 and p+q==2*K and max(p,q)<=M-3 and not p==q==M-3
    r=max(0,(K-2*N+1)//2);assert r<=k
    if r==0:
        row=b84.construct(M,d,p,q,partition);row['mode']='r0_MI191';return row
    eps=K%2;need=r+1-eps;ordered=sorted(d,reverse=True);D=ordered[0];others=ordered[1:]
    selected=[];available=0
    for E in others:
        if E<2:break
        selected.append(E);available+=E-1
        if available>=need:break
    assert available>=need,'no shared capacity'
    t=len(selected);assert D>=r+t+1,'D below shared bound'
    rest=others[t:];U=r-t+1-eps;assert U>=0
    pieces=[D-r-t+1]+[2]*(t-1);assert min(pieces)>=2
    refined=pieces+others+[1]*(U+eps)
    assert sum(pieces)+U+eps==D and len(refined)==N+r and sum(refined)==K
    internal=[v for f,E in zip(pieces,selected) for v in (f,E)]+[v for v in rest if v>1]
    nc=N+r+2;s=k-r;frameP=K+1-eps;frameQ=K-1+eps
    parent=b79.full(2*nc,frameP,frameQ,refined,internal)
    assert parent['run_lengths'][0]==1+eps and parent['run_lengths'][-1]==1
    deleted=parent['A'][1:r+1]
    assert len(deleted)==r
    A=parent['A'][:1]+parent['A'][r+1:];B=parent['B'][:]
    assert len(A)>=2 and A[0]==0 and A[1]==D
    assert (A[0],A[-1],B[0],B[-1])==(parent['A'][0],parent['A'][-1],parent['B'][0],parent['B'][-1])
    merged=b79.validate(2*nc,frameP,frameQ,d,A,B)
    # Exact MI191 selector: at most one residue correction, never a search.
    C=2*nc-3;lo=max(1,2*K-C);hi=min(C,2*K-1)
    a=max(lo,p-2*s);b=min(hi,p+2*s);residue=(p-2*s)%4
    x=a if a%4==residue else a+2;y=2*K-x
    assert a<=x<=b and min(x,y)>0 and max(x,y)<=C
    first=0 if x>=y else 1;P0=max(x,y);Q0=min(x,y);reverse=False
    if eps and P0==K+2:
        A=sorted(nc-1-v for v in A);B=sorted(nc-1-v for v in B);reverse=True
    else:assert (P0,Q0)==(frameP,frameQ)
    assert 2*nc-1-2*(A[0]+B[0])==P0
    assert 2*(A[-1]+B[-1])-(2*nc-1)==Q0
    shift=((p,q)[first]-P0)//2
    assert abs(shift)<=s and (shift-s)%2==0
    left=(s-shift)//2;right=(s+shift)//2
    A=[v+left for v in A];B=[v+left for v in B]
    row=b84.validate(M,d,p,q,A,B,first,partition)
    row.update(M=M,d=d,p=p,q=q,k=k,r=r,s=s,mode='shared_merge',epsilon=eps,
               D=D,selected_E=selected,merge_runs=t,required_capacity=need,
               refined_pieces=pieces,refined_units=U+eps,parent=parent,
               deleted=deleted,merged_frame=merged,core_n=nc,reversed_core=reverse,
               x=x,y=y,first_core=P0,second_core=Q0,padding_shift=shift,left=left,right=right)
    return row


def main():
    start=time.process_time()
    fixtures=[((7,2,2,2,2,2),19,15),((7,2,2,2,2,2),25,9),
              ((8,2,2,2,2,2),25,11),((7,3,2,2,2,2),23,13),
              ((6,3,3,2,2,2),19,17),((8,3,2,2,2,2),25,13)]
    rows=[construct(28,d,p,q,True) for d,p,q in fixtures]
    rows.extend((construct(12,(3,2),7,3),construct(10,(3,2),7,3),
                 construct(40,(11,3,3,3,2,2),35,13),
                 construct(100,(17,2,2,2,2,2,2,2,2,2),61,9),
                 construct(22,(1,1,2,2,2,2,3,3),17,15),
                 construct(28,(8,8,2,2,2,2),25,23)))
    assert len(rows)==12 and sum(v['bins'] is not None for v in rows)==6
    assert all(sorted(v['d'],reverse=True)[1]<v['r']+2 for v in rows[:6])
    assert rows[0]['epsilon']==1 and rows[0]['merge_runs']==3 and rows[0]['D']==7
    assert rows[1]['reversed_core'] and rows[5]['reversed_core']
    assert [v['merge_runs'] for v in rows[2:5]]==[4,3,2]
    assert rows[7]['s']==0 and rows[7]['reversed_core']
    assert rows[9]['r']==8 and rows[9]['s']==30 and rows[9]['merge_runs']==8
    assert rows[10]['mode']=='r0_MI191' and rows[11]['merge_runs']==1
    refused=[]
    for name,args in [('D_bound',(28,(5,3,3,3,2,2),19,17)),
                      ('no_eligible_E',(28,(11,1,1,1,1,1),19,13))]:
        try:construct(*args)
        except AssertionError as e:refused.append(dict(name=name,reason=str(e)))
        else:raise AssertionError('missing admission refusal '+name)
    outside_cross=crossing(28,(5,3,3,3,2,2),19,17)
    assert Counter(outside_cross['word'])==Counter((19,17,-10,-6,-6,-6,-4,-4))
    outside=[0,19,17,15,13,11,9,22]
    outside_word=[v-u for u,v in zip(outside,outside[1:]+outside[:1])]
    assert literal(28,outside) and instrument.literal_geometry(28,set(),outside)
    assert Counter(outside_word)==Counter((19,13,-22,-2,-2,-2,-2,-2))
    first=rows[0];parent=first['parent'];wrongA=parent['A'][:1]+parent['A'][first['r']+2:]
    wrongB=parent['B'][:]
    wrongA=[v+first['left'] for v in wrongA];wrongB=[v+first['left'] for v in wrongB]
    wrongxs,wrongword=physical(28,wrongA,wrongB)
    assert literal(28,wrongxs) and instrument.literal_geometry(28,set(),wrongxs)
    assert wrongword[0]==19 and wrongword[len(wrongB)]==15
    assert sum(-v//2 for v in wrongword if v<0)==sum(first['d'])==17
    assert Counter(wrongword)==Counter((19,15,-18,-4,-4,-4,-4))
    assert Counter(wrongword)!=Counter((19,15,-14,-4,-4,-4,-4,-4))
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='bfe20e26',
                         formula_calls=12,E28_partitions=6,rows=rows,refused=refused,
                         outside_D_admission=outside_cross,
                         outside_capacity_admission=dict(positions=outside,word=outside_word),
                         overdeletion=dict(A=wrongA,B=wrongB,positions=wrongxs,word=wrongword),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
