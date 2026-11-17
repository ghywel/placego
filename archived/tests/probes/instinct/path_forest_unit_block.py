#!/usr/bin/env python3
"""B86/MI195 preregf150f935: nested consecutive block, D>=N+1.

Twelve formula calls/six E28 partitions, jump/scope and owner/parity controls.
1CPU sec/64MiB, no translations or profile search. Class iff SKETCH,
independent of MI191's construction (generic validation is reused only).
OUTCOME:12 calls/6 partitions and controls pass;0.001828CPU sec,15273984RSS
bytes. Raw SHA2560740a2cc1c643be4740343f2a0a6cd416390866e5347261b5cb63a6365c45aca.
"""
from collections import Counter
import json
import resource
import time

import path_forest_partial_padding as prior
import path_forest_balanced_bridge as instrument
from path_forest_interlaced_pairs import physical,literal


def construct(M,N,D,p,q,partition=False):
    assert M%2==0 and N>=1 and D>=1 and p>0 and q>0 and p%2 and q%2
    assert p+q==2*(D+N-1)
    assert D>=N+1,'inner-block scope'
    n=M//2
    assert max(p,q)<=M-3,'odd-jump bound'
    assert D<=n-1,'negative-jump bound'
    if D==N+1:
        owners=[i for i,v in enumerate((p,q)) if (v-(M-3))%4==0]
        assert len(owners)==1;first=owners[0]
    else:first=0 if p>=q else 1
    P=(p,q)[first];Q=(p,q)[1-first]
    assert Q<=M-5
    alpha=(M-1-P)//2;H=n-1-D;inner=D-N
    assert 1<=alpha<=2*H+inner
    b=min(inner,alpha);adjusted=(alpha-b)%2!=0
    if adjusted:b-=1
    a=(alpha-b)//2
    assert 2*a+b==alpha and 0<=a<=H and 1<=b<=inner
    A=[a,a+D];B=list(range(a+b,a+b+N))
    assert A[0]<B[0]<=B[-1]<A[-1]
    assert A[0]+B[0]==alpha and A[-1]+B[-1]==alpha+D+N-1
    d=[D]+[1]*(N-1)
    row=prior.validate(M,d,p,q,A,B,first,partition)
    # Complete bag and direct physical labels, independent of margin selection.
    assert Counter(row['word'])==Counter((p,q,-2*D,*([-2]*(N-1))))
    assert literal(M,row['positions']) and instrument.literal_geometry(M,set(),row['positions'])
    row.update(M=M,N=N,D=D,p=p,q=q,alpha=alpha,H=H,inner=inner,a=a,b=b,
               parity_adjusted=adjusted,d=d)
    return row


def main():
    start=time.process_time()
    rows=[construct(28,6,D,p,q,True) for D,p,q in
          ((11,19,13),(11,25,7),(10,17,13),(9,15,13),(8,19,7),(7,15,9))]
    rows.extend((construct(6,1,2,3,1),construct(8,1,3,3,3),
                 construct(16,6,7,13,11),construct(20,4,6,11,7),
                 construct(14,3,4,7,5),construct(100,10,35,47,41)))
    assert len(rows)==12 and sum(v['bins'] is not None for v in rows)==6
    assert rows[5]['first_owner']==1 and rows[5]['b']==1
    assert rows[6]['H']==rows[7]['H']==rows[8]['H']==0
    assert rows[-1]['parity_adjusted'] and (rows[-1]['a'],rows[-1]['b'])==(1,24)
    refused=[]
    for name,args in [('negative_bound',(20,4,10,15,11)),
                      ('odd_bound',(28,6,11,27,5)),
                      ('small_D_scope',(28,6,5,13,7))]:
        try:construct(*args)
        except AssertionError as e:refused.append(dict(name=name,reason=str(e)))
        else:raise AssertionError('missing refusal '+name)
    outside=prior.construct(28,(5,1,1,1,1,1),13,7)
    assert literal(28,outside['positions'])
    assert Counter(outside['word'])==Counter((13,7,-10,-2,-2,-2,-2,-2))
    wrongA=[2,9];wrongB=list(range(3,9));wrongxs,wrongword=physical(28,wrongA,wrongB)
    assert literal(28,wrongxs) and instrument.literal_geometry(28,set(),wrongxs)
    assert wrongword[0]==17 and wrongword[len(wrongB)]==7
    assert Counter(wrongword)==Counter((17,7,-14,-2,-2,-2,-2,-2))
    assert Counter(wrongword)!=Counter((15,9,-14,-2,-2,-2,-2,-2))
    parityA=[0,35];parityB=list(range(25,35));parityxs,parityword=physical(100,parityA,parityB)
    assert literal(100,parityxs) and instrument.literal_geometry(100,set(),parityxs)
    assert parityword[0]==49 and parityword[len(parityB)]==39
    assert Counter(parityword)==Counter((49,39,-70,*([-2]*9)))
    assert Counter(parityword)!=Counter((47,41,-70,*([-2]*9)))
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='f150f935',
                         formula_calls=12,E28_partitions=6,rows=rows,refused=refused,
                         outside_scope_positive=outside,
                         wrong_owner_control=dict(A=wrongA,B=wrongB,positions=wrongxs,word=wrongword),
                         unexpected_parity_control=dict(A=parityA,B=parityB,positions=parityxs,word=parityword),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
