#!/usr/bin/env python3
"""B95/MI216 prereg4c93bbd7: one smaller exceptional gap.

Eleven formula calls/five E28 partitions, capacity-only controls, one
capacity rejection and twelve minimal balanced-split countercontrols.
1CPU sec/64MiB; no ordering or whole-cycle existence census. Uniform SKETCH.
OUTCOME MI217:11 calls/5 partitions pass;0.001474CPU sec,15626240RSS bytes.
Artifact SHA256 c0d7083aa2e2c5fd84468e32b74620277d342545b19c4148f34748d19e2a3487.
"""
from collections import Counter
import json
import resource
import time

import path_forest_partial_padding as validation


def capacity(R,s,t,h):
    assert R>=1 and 1<=t<s and s>=2
    r=R//2;C=r*s+t if R%2==0 else (r+1)*s
    loads=[max(k*s+t,(R-k)*s) for k in range(R+1)]
    assert C==min(loads)
    return dict(minimum=C,enumerated_minimum=min(loads),
                admitted=C<=h,feasible_k=[k for k,v in enumerate(loads) if v<=h])


def prefix(x,steps):
    out=[x]
    for v in steps:out.append(out[-1]+v)
    return out


def construct(M,R,s,t,p,q,partition=False):
    assert M%2==0;h=M//2-1;K=R*s+t;d=[s]*R+[t]
    assert min(p,q)>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=2*h-1 and not p==q==2*h-1
    cap=capacity(R,s,t,h)
    if not cap['admitted']:raise ValueError('no two-bin capacity')
    r=R//2
    if R%2==0:
        case='even';ag=[s]*r+[t];bg=[s]*r
    elif (s,t)==(2,1):
        case='unit-rebalance';ag=[2]*(r+1)+[1];bg=[2]*r
    else:
        case='odd';ag=[s]*(r+1);bg=[s]*r+[t]
    L=sum(ag);S=sum(bg);H=h-L;J=h-S;delta=L-S;T=H+J
    assert 0<=H<=J and T>=2 and R+3<=M//2
    alpha=(2*h+1-max(p,q))//2
    assert 1<=alpha<=H+(delta+1)//2
    if case=='unit-rebalance':
        branch='corner';c=alpha if alpha%2 else alpha-1;z=1
        x=(c-1)//2;y=(c+1)//2
    elif alpha<=2*H:
        branch='margin';c=alpha if alpha%2 else alpha-1
        z=-1 if case=='even' or delta==1 else 1
        x=(c-z)//2;y=(c+z)//2
    else:
        branch='thin';c=alpha;x=H;y=alpha-H;z=y-x
        assert delta>=2 and 0<z<delta
    assert 0<=x<=H and 0<=y<=J and x+y==c and z%s
    if case=='even':assert z<t
    elif case=='odd':assert -t<z<s and z!=delta
    preA=prefix(x,ag);preB=prefix(y,bg)
    assert not set(preA)&set(preB)
    first=0 if p>=q else 1;reflected=(c==alpha-1)
    A=preA;B=preB
    if reflected:
        A=[h-v for v in reversed(A)];B=[h-v for v in reversed(B)]
        first=1-first
    row=validation.validate(M,d,p,q,A,B,first,partition)
    row.update(M=M,R=R,s=s,t=t,p=p,q=q,d=d,capacity=cap,case=case,
               L=L,S=S,H=H,J=J,delta=delta,alpha=alpha,c=c,z=z,
               branch=branch,preA=preA,preB=preB,reflected=reflected)
    return row


def main():
    start=time.process_time()
    fixtures=[(28,5,2,1,13,9),(28,5,2,1,11,11),(28,5,3,1,25,7),
              (28,5,3,2,23,11),(28,5,4,3,23,23),(20,4,3,2,17,11),
              (18,4,3,2,13,15),(14,4,2,1,11,7),(8,1,3,1,5,3),
              (8,1,2,1,5,1),(70,8,7,6,63,61)]
    rows=[construct(*f,partition=i<5) for i,f in enumerate(fixtures)]
    assert len(rows)==11 and sum(v['bins'] is not None for v in rows)==5
    assert rows[0]['case']==rows[1]['case']=='unit-rebalance'
    assert rows[1]['reflected'] and rows[3]['reflected'] and rows[4]['reflected']
    assert rows[6]['case']=='even' and rows[6]['branch']=='thin' and rows[6]['z']>0
    assert rows[10]['case']=='even' and rows[10]['branch']=='thin' and rows[10]['z']==3
    assert rows[7]['case']=='even' and rows[7]['branch']=='margin'
    assert len(rows[9]['preB'])==1
    refused=capacity(3,5,1,9)
    assert refused['minimum']==10 and not refused['admitted']
    try:construct(20,3,5,1,17,15)
    except ValueError:pass
    else:raise AssertionError('missing capacity rejection')
    candidates=0;accepted=[]
    for x in range(2):
        for y in range(3):
            A=[x,x+2];B=[y,y+1];xs,word=validation.physical(8,A,B)
            for owner in (0,1):
                candidates+=1
                if word[0]!=(5,1)[owner] or Counter(word)!=Counter((5,1,-4,-2)):continue
                v1=validation.literal(8,xs);v2=validation.instrument.literal_geometry(8,set(),xs)
                assert v1==v2
                if v1:accepted.append(dict(A=A,B=B,owner=owner))
    assert candidates==12 and not accepted
    assert set(min(v,7-v) for v in rows[9]['positions'])==set(range(4))
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='4c93bbd7',
                         formula_calls=11,E28_partitions=5,rows=rows,
                         capacity_rejection=refused,
                         bad_balanced_split=dict(candidates=candidates,accepted=accepted),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
