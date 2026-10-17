#!/usr/bin/env python3
"""B92/MI210 prereg4bbac7c1: span-dominant top-two/rich-four completion.

Six named calls and actual E28 partitions; <=24 local companion orders/call.
Independent start rectangles; ascending-order and thin-endpoint negatives.
1CPU sec/64MiB, no profile census or whole-cycle existence solver.
Uniform hand argument remains SKETCH, conditional on MI204.
OUTCOME MI211:6 calls/6 partitions pass;0.015802CPU sec,19771392RSS bytes.
SHA256 eca46cfeddf245f8d024f1f8e673dd9c813fe8631c75482a3034d6cba900a302.
"""
from collections import Counter
from itertools import permutations
from pathlib import Path
import hashlib
import json
import resource
import time

import path_forest_partial_padding as validation


def prefixes(start, steps):
    out=[start]
    for v in steps:out.append(out[-1]+v)
    return out


def construct(d,p,q):
    b=sorted(d)[:4];D,E=sorted(d)[4:];S=sum(b);L=D+E
    assert len(d)==6 and 1<=min(d) and max(Counter(b).values())<=2
    assert S<=L<=13 and p+q==2*(L+S) and p%2 and q%2
    assert min(p,q)>0 and max(p,q)<=25 and not p==q==25
    H=13-L;J=13-S;T=H+J;alpha=(27-max(p,q))//2
    assert 1<=alpha<=(T+1)//2 and J>=H and J>0
    lo=-alpha if alpha<=H else alpha-1-2*H
    I=set(range(lo,alpha+1))
    direct={y-x for x in range(H+1) for y in range(J+1)
            if x+y in (alpha,alpha-1)}
    assert I==direct
    bad={-S,0,L-S,L}
    if D==E:bad.update((D,D-S))
    elif E-D==S:bad.add(D)
    z=min(I-bad,key=lambda v:(abs(v),v))
    c=alpha if z%2==alpha%2 else alpha-1
    x=(c-z)//2;y=(c+z)//2
    assert 0<=x<=H and 0<=y<=J and x+y==c and y-x==z
    orders=[(D,E),(E,D)]
    aorder=next(o for o in orders if not set(prefixes(x,o))&{y,y+S})
    preA=prefixes(x,aorder)
    forbidden=sorted(v-y for v in preA if y<v<y+S)
    assert len(forbidden)<=2
    if len(forbidden)==2:assert forbidden[1]-forbidden[0]>=max(b)
    tried=0;chosen=None
    for o in sorted(set(permutations(b))):
        tried+=1
        if not set(prefixes(0,o)[1:-1])&set(forbidden):
            chosen=o;break
    assert chosen is not None and tried<=24
    preB=prefixes(y,chosen)
    first=0 if p>=q else 1
    reflected=(c==alpha-1)
    A=preA;B=preB
    if reflected:
        A=[13-v for v in reversed(A)];B=[13-v for v in reversed(B)]
        first=1-first
    row=validation.validate(28,list(d),p,q,A,B,first,True)
    row.update(d=d,p=p,q=q,L=L,S=S,H=H,J=J,alpha=alpha,
               offset_interval=sorted(I),bad_offsets=sorted(bad),z=z,c=c,
               preA=preA,preB=preB,forbidden=forbidden,A_order=aorder,
               B_order=chosen,local_orders_tried=tried,reflected=reflected)
    return row


def negative(d,p,q,A,B):
    xs,word=validation.physical(28,A,B)
    assert Counter(word)==Counter((p,q,*(-2*v for v in d)))
    assert all(0<=x<28 for x in xs) and len(set(xs))==8
    assert not validation.literal(28,xs)
    assert not validation.instrument.literal_geometry(28,set(),xs)
    return dict(A=A,B=B,positions=xs,word=word,bag_valid=True,
                folded_geometry_valid=False,shared_indices=sorted(set(A)&set(B)))


def main():
    start=time.process_time()
    fixtures=[((2,2,3,4,4,9),25,23),((2,2,3,4,4,8),25,21),
              ((2,2,3,4,4,8),23,23),((1,2,2,3,3,7),19,17),
              ((1,1,2,2,3,3),17,7),((1,1,2,3,3,10),21,19)]
    prior_raw=Path('/tmp/math-instinct-b87-admission-synthesis.json').read_bytes()
    digest=hashlib.sha256(prior_raw).hexdigest()
    assert digest=='3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0'
    prior=json.loads(prior_raw);residual=[]
    for d,pairs in [(fixtures[0][0],[[23,25]]),(fixtures[1][0],[[21,25],[23,23]])]:
        r=next(v for v in prior['records'] if v['d']==list(d))
        assert not r['admissions'] and r['positive_pairs']==pairs
        residual.append(r)
    rows=[construct(*f) for f in fixtures]
    assert rows[3]['forbidden']==[1,4] and rows[3]['reflected']
    assert rows[3]['first_owner']==1
    assert rows[4]['preA']==[3,6,9] and rows[4]['preB']==[2,4,5,7,8]
    ascending=negative(fixtures[4][0],17,7,[3,6,9],[2,3,4,6,8])
    assert ascending['shared_indices']==[3,6]
    assert rows[5]['z']==2 and rows[5]['reflected']
    assert rows[5]['offset_interval']==[2,3] and 3 in rows[5]['bad_offsets']
    endpoint=[negative(fixtures[5][0],21,19,A,[3,4,5,7,10])
              for A in ([0,3,13],[0,10,13])]
    assert [r['shared_indices'] for r in endpoint]==[[3],[10]]
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<1 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='4bbac7c1',
                         formula_calls=6,E28_partitions=6,rows=rows,
                         source_artifact_sha256=digest,prior_residuals=residual,
                         ascending_control=ascending,thin_endpoint_controls=endpoint,
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
