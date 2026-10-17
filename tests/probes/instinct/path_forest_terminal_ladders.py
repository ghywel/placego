#!/usr/bin/env python3
"""B93/MI212 prereg5e23e8b0: rebalance constant companions into two ladders.

Ten explicit formula calls, seven actual E28 partitions, 720 restricted
root/order/owner controls on one named bag, divisible-offset negative.
1CPU sec/64MiB; no ordering or whole-cycle existence search.
Uniform hand construction SKETCH, independent of MI201/204.
OUTCOME MI213:10 calls/7 partitions pass, restricted counts0/0/0/0/2.
CPU0.003540s,RSS15458304bytes; artifact SHA256
2b01b76b49b2bdfde371e992a9b973048ae7b650c5a00447cfe70903a90a95aa.
"""
from collections import Counter
import json
import resource
import time

import path_forest_partial_padding as validation


def construct(M,r,s,a,b,p,q,partition=False):
    h=M//2-1
    assert M%2==0 and r>=1 and 2<=s<=a<=b and r*s+b<=h
    d=[s]*(2*r)+[a,b];K=sum(d)
    assert p>0 and q>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=2*h-1 and not p==q==2*h-1
    H=h-r*s-b;J=h-r*s-a;delta=b-a;T=H+J
    alpha=(2*h+1-max(p,q))//2
    assert T>=2 and 1<=alpha<=H+(delta+1)//2
    if alpha<=2*H:
        branch=1;c=alpha if alpha%2 else alpha-1
        x=(c+1)//2;y=(c-1)//2;z0=None
        assert y-x==-1
    else:
        branch=2;x=H;z0=alpha-2*H
        c=alpha-1 if z0%s==0 else alpha
        y=c-H;z=y-x
        assert delta>=2 and 0<z<delta and z<b and z%s
    assert 0<=x<=H and 0<=y<=J and x+y==c
    preA=[x+i*s for i in range(r+1)]+[x+r*s+b]
    preB=[y+i*s for i in range(r+1)]+[y+r*s+a]
    assert not set(preA)&set(preB)
    first=0 if p>=q else 1
    reflected=(c==alpha-1)
    A=preA;B=preB
    if reflected:
        A=[h-v for v in reversed(A)];B=[h-v for v in reversed(B)]
        first=1-first
    row=validation.validate(M,d,p,q,A,B,first,partition)
    row.update(M=M,r=r,s=s,a=a,b=b,d=d,p=p,q=q,H=H,J=J,
               alpha=alpha,c=c,z=y-x,z0=z0,branch=branch,
               preA=preA,preB=preB,reflected=reflected)
    return row


def fixed_split(p,q):
    d=[2,2,2,2,3,5];bag=Counter((p,q,*(-2*v for v in d)))
    accepted=[];candidates=0;bag_valid=0
    for x in range(6):
        for y in range(6):
            B=[y+2*j for j in range(5)]
            for middle in (3,5):
                A=[x,x+middle,x+8]
                xs,word=validation.physical(28,A,B)
                for first in (0,1):
                    candidates+=1
                    if word[0]!=(p,q)[first] or Counter(word)!=bag:continue
                    bag_valid+=1
                    v1=validation.literal(28,xs)
                    v2=validation.instrument.literal_geometry(28,set(),xs)
                    assert v1==v2
                    if v1:
                        assert not set(A)&set(B)
                        accepted.append(dict(A=A,B=B,first_owner=first,positions=xs,word=word))
    alpha=(27-max(p,q))//2
    assert bool(accepted)==(alpha>=5)
    return dict(p=p,q=q,alpha=alpha,candidates=candidates,
                bag_valid=bag_valid,accepted=accepted)


def main():
    start=time.process_time()
    pairs=[(25,7),(23,9),(21,11),(19,13),(17,15)]
    rows=[construct(28,2,2,3,5,p,q,True) for p,q in pairs]
    rows.extend([construct(28,2,3,4,7,25,21,True),
                 construct(28,2,3,4,7,23,23,True),
                 construct(46,2,3,4,16,33,31),
                 construct(78,5,4,5,18,63,63),
                 construct(12,1,2,2,2,9,7)])
    assert len(rows)==10 and sum(v['bins'] is not None for v in rows)==7
    assert rows[7]['branch']==2 and rows[7]['z0']==6 and rows[7]['z']==5
    assert rows[7]['reflected'] and rows[7]['first_owner']==1
    assert rows[8]['r']==5 and rows[8]['p']==rows[8]['q']
    assert rows[9]['a']==rows[9]['b']
    split=[fixed_split(p,q) for p,q in pairs]
    assert sum(v['candidates'] for v in split)==720
    assert not any(v['accepted'] for v in split[:4]) and split[4]['accepted']
    A=[0,3,6,22];B=[6,9,12,16]
    xs,word=validation.physical(46,A,B)
    assert Counter(word)==Counter((33,31,-6,-6,-6,-6,-8,-32))
    assert all(0<=v<46 for v in xs) and len(set(xs))==8
    assert set(A)&set(B)=={6}
    assert not validation.literal(46,xs)
    assert not validation.instrument.literal_geometry(46,set(),xs)
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='5e23e8b0',
                         formula_calls=10,E28_partitions=7,rows=rows,
                         restricted_split=split,
                         divisible_offset_control=dict(A=A,B=B,positions=xs,word=word,
                                                       bag_valid=True,folded_geometry_valid=False),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
