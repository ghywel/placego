#!/usr/bin/env python3
"""B94/MI214 preregedea6a7f: unequal repeated-gap allocation selector.

Nine formula calls/five E28 partitions, ten capacity-only comparisons,
one named allocation refusal, twelve bad-split candidates, one negative.
1CPU sec/64MiB; no ordering or general existence search. Uniform SKETCH.
OUTCOME MI215:9 calls/5 partitions pass;0.001459CPU sec,15675392RSS bytes.
Artifact SHA256 efa0e0ff6b8497ef065502b359131983b29c48722bdba3a7370b1d26df3850fb.
"""
from collections import Counter
import json
import resource
import time

import path_forest_partial_padding as validation


def select(h,m,s,a,b):
    assert m>=1 and 2<=s<=a<=b
    k0=max(0,(m*s+a-b+2*s-1)//(2*s))
    assert 0<=k0<=m
    L0=b+k0*s;S0=a+(m-k0)*s
    assert L0>=S0
    if L0<=h:
        j=k0;u=b;v=a;fallback=False
    else:
        if k0==0:raise ValueError('no separate-terminal capacity')
        k1=k0-1;L1=L0-s;S1=S0+s
        if S1>h:raise ValueError('no separate-terminal capacity')
        assert L1<S1<=h
        j=m-k1;u=a;v=b;fallback=True
    L=j*s+u;S=(m-j)*s+v;delta=L-S
    assert S<=L<=h and 0<=delta<=u
    return dict(j=j,u=u,v=v,L=L,S=S,delta=delta,k0=k0,fallback=fallback)


def construct(M,m,s,a,b,p,q,partition=False):
    h=M//2-1;d=[s]*m+[a,b];K=sum(d)
    assert M%2==0 and min(p,q)>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=2*h-1 and not p==q==2*h-1
    csel=select(h,m,s,a,b)
    j,u,v,L,S,delta=(csel[k] for k in ('j','u','v','L','S','delta'))
    H=h-L;J=h-S;T=H+J;alpha=(2*h+1-max(p,q))//2
    assert T>=2 and (delta!=1 or u>=3)
    assert 1<=alpha<=H+(delta+1)//2
    if alpha<=2*H:
        branch=1;c=alpha if alpha%2 else alpha-1
        z=-1 if delta==1 else 1
        x=(c-z)//2;y=(c+z)//2;z0=None
    else:
        branch=2;x=H;z0=alpha-2*H
        c=alpha-1 if z0%s==0 else alpha
        y=c-H;z=y-x
        assert delta>=2 and 0<z<delta and z%s
    assert 0<=x<=H and 0<=y<=J and x+y==c
    assert z%s and delta-u<z<delta+v and z!=delta
    preA=[x+i*s for i in range(j+1)]+[x+j*s+u]
    preB=[y+i*s for i in range(m-j+1)]+[y+(m-j)*s+v]
    assert not set(preA)&set(preB)
    first=0 if p>=q else 1;reflected=(c==alpha-1)
    A=preA;B=preB
    if reflected:
        A=[h-vv for vv in reversed(A)];B=[h-vv for vv in reversed(B)]
        first=1-first
    row=validation.validate(M,d,p,q,A,B,first,partition)
    row.update(M=M,m=m,s=s,a=a,b=b,p=p,q=q,d=d,selector=csel,
               H=H,J=J,alpha=alpha,c=c,z=z,z0=z0,branch=branch,
               preA=preA,preB=preB,reflected=reflected)
    return row


def capacity_control(M,m,s,a,b):
    h=M//2-1
    allowed=[k for k in range(m+1) if b+k*s<=h and a+(m-k)*s<=h]
    try:chosen=select(h,m,s,a,b)
    except ValueError:chosen=None
    assert bool(allowed)==(chosen is not None)
    if chosen:
        k=m-chosen['j'] if chosen['fallback'] else chosen['j']
        assert k in allowed
    return dict(M=M,m=m,s=s,a=a,b=b,allowed=allowed,selector=chosen)


def main():
    start=time.process_time()
    fixtures=[(28,4,3,3,8,25,21),(28,4,3,3,8,23,23),
              (28,4,2,2,10,25,15),(28,4,2,2,11,23,19),
              (28,4,2,3,7,23,13),(12,1,2,2,3,9,5),
              (30,4,3,3,8,23,23),(12,2,2,2,2,9,7),
              (56,7,4,5,18,51,51)]
    rows=[construct(*f,partition=i<5) for i,f in enumerate(fixtures)]
    assert len(rows)==9 and sum(v['bins'] is not None for v in rows)==5
    assert rows[0]['selector']['fallback'] and rows[0]['selector']['delta']==1
    assert rows[1]['selector']['fallback'] and rows[1]['reflected']
    assert rows[2]['selector']['k0']==0 and rows[2]['selector']['delta']==0
    assert rows[3]['selector']['k0']==0 and rows[3]['reflected']
    assert rows[4]['selector']['j']!=2 and rows[4]['selector']['delta']==0
    assert rows[6]['branch']==2 and rows[6]['z0']==3 and rows[6]['z']==2
    assert rows[6]['reflected'] and rows[8]['m']==7
    caps=[capacity_control(*f[:5]) for f in fixtures]
    refused=capacity_control(36,3,5,8,8)
    assert not refused['allowed'] and refused['selector'] is None
    assert 8+8<=17 and 3*5<=17  # arbitrary capacity does not imply separate-terminal admission
    accepted=[];candidates=0
    for x in range(2):
        for y in range(3):
            A=[x,x+2,x+4];B=[y,y+3]
            xs,word=validation.physical(12,A,B)
            for owner in (0,1):
                candidates+=1
                if word[0]!=(9,5)[owner] or Counter(word)!=Counter((9,5,-4,-4,-6)):continue
                v1=validation.literal(12,xs);v2=validation.instrument.literal_geometry(12,set(),xs)
                assert v1==v2
                if v1:accepted.append(dict(A=A,B=B,owner=owner))
    assert candidates==12 and not accepted
    A=[0,3,6,14];B=[3,6,9,12];xs,word=validation.physical(30,A,B)
    assert Counter(word)==Counter((23,23,-6,-6,-6,-6,-6,-16))
    assert all(0<=x<30 for x in xs) and len(set(xs))==8
    assert set(A)&set(B)=={3,6}
    assert not validation.literal(30,xs) and not validation.instrument.literal_geometry(30,set(),xs)
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='edea6a7f',
                         formula_calls=9,E28_partitions=5,rows=rows,
                         capacity_controls=caps,refused_separate_capacity=refused,
                         bad_balanced_split=dict(candidates=candidates,accepted=accepted),
                         divisible_offset_control=dict(A=A,B=B,positions=xs,word=word,
                                                       bag_valid=True,folded_geometry_valid=False),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
