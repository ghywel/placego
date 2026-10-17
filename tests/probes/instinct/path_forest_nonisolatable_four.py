#!/usr/bin/env python3
"""B99/MI224 preregeb0b7b6d, pre-run correction23bedaef.

Extreme/middle pairing when the largest of four gaps cannot be isolated.
26 frozen residual+4 boundary calls,26 E28 partitions; independent fixed-
split maps and a paired-failure/alternate-split-success scope control.
2CPU sec/64MiB; no whole-cycle solver or regenerated input domain.
General theorem remains SKETCH pending independent scrutiny.
OUTCOME MI225: all30 formulas/26 E28 partitions pass;123 offset entries,
197 original-root candidates agree;0.019213CPU sec/17588224RSS bytes.
Artifact SHA2568a8a6f738d36ae308ad5798ab1da83d5a28b9eaddad44d5352b48bd86f1ecc99.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib
import json
import resource
import time

import path_forest_partial_padding as validation
from path_forest_low_count_frontier import materialize_two_baselines


def data(M,d):
    assert M%2==0 and len(d)==4 and list(d)==sorted(d) and min(d)>0
    h=M//2-1;a,b,c,dd=d;L=a+dd;S=b+c
    if a+b+c<=h:raise ValueError('largest isolation is available: outside theorem')
    if max(L,S)>h:raise ValueError('no ordinary two-bin capacity')
    return h,L,S,h-L,h-S


def orders(d,x,y):
    a,b,c,dd=d
    for u,v in product(sorted({a,dd}),sorted({b,c})):
        yield [x,x+u,x+a+dd],[y,y+v,y+b+c]


def construct(M,d,p,q):
    h,L,S,H,J=data(M,d);K=sum(d);T=H+J
    assert p>0 and q>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=M-3 and not p==q==M-3 and T>=2 and h>=5
    alpha=(M-1-max(p,q))//2
    assert 1<=alpha< T and alpha<=(T+1)//2
    if alpha<=min(H,J):lo,hi=-alpha,alpha
    elif H<alpha<=J:lo,hi=alpha-1-2*H,alpha
    else:
        assert J<alpha<=H;lo,hi=-alpha,2*J-alpha+1
    d0=L-S
    if H==0:z=alpha
    elif J==0:z=-alpha
    else:z=next(v for v in range(lo,lo+3) if v not in (0,d0))
    assert lo<=z<=hi and z not in (0,d0)
    root=alpha if z%2==alpha%2 else alpha-1
    x=(root-z)//2;y=(root+z)//2
    assert 0<=x<=H and 0<=y<=J and x+y==root
    tried=0
    for preA,preB in orders(d,x,y):
        tried+=1
        if not set(preA)&set(preB):break
    else:raise AssertionError('endpoint-free offset has no order')
    assert tried<=4
    reflected=root==alpha-1;A=preA;B=preB;first=0 if p>=q else 1
    if reflected:
        A=[h-v for v in reversed(A)];B=[h-v for v in reversed(B)];first=1-first
    row=validation.validate(M,d,p,q,A,B,first,False)
    row.update(M=M,d=d,p=p,q=q,H=H,J=J,L=L,S=S,T=T,alpha=alpha,z=z,
               root=root,preA=preA,preB=preB,reflected=reflected,orders_tried=tried)
    return row


def maps(M,d,p,q,nonisolation=True):
    h=M//2-1;a,b,c,dd=d;L=a+dd;S=b+c;H=h-L;J=h-S
    assert min(H,J)>=0
    offsets=[]
    for z in range(-H,J+1):
        x=max(0,-z);y=x+z
        assert 0<=x<=H and 0<=y<=J
        candidates=[]
        for A,B in orders(d,x,y):
            xs,word=validation.physical(M,A,B)
            direct=not set(A)&set(B)
            assert validation.literal(M,xs)==direct
            assert validation.instrument.literal_geometry(M,set(),xs)==direct
            assert len(set(xs))==6 and all(0<=v<M for v in xs)
            candidates.append(dict(A=A,B=B,valid=direct))
        valid=any(v['valid'] for v in candidates)
        if nonisolation:assert valid==(z not in (0,L-S))
        offsets.append(dict(z=z,valid=valid,orders=candidates))
    rooted=[];tests=0
    for x in range(H+1):
        for y in range(J+1):
            for A,B in orders(d,x,y):
                P=M-1-2*(x+y);Q=2*K_value(d)-P
                if Counter((P,Q))!=Counter((p,q)):continue
                tests+=1;xs,word=validation.physical(M,A,B)
                assert Counter(word)==Counter((p,q,*(-2*v for v in d)))
                direct=not set(A)&set(B)
                assert validation.literal(M,xs)==direct
                assert validation.instrument.literal_geometry(M,set(),xs)==direct
                if direct:rooted.append(dict(A=A,B=B,first_positive=P))
    assert bool(rooted)==nonisolation
    return dict(offsets=offsets,root_order_candidates=tests,valid_original_join_orders=rooted)


def K_value(d):return sum(d)


def main():
    start=time.process_time();raw=Path('/tmp/math-instinct-b98-low-count-frontier.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    assert digest=='34e2246d5c58a72c4e4a6f5afdabfe7321ed2252961da3d2e24d14bcf3bd5e29'
    residual=json.loads(raw)['remaining'];assert len(residual)==15
    assert sum(v['questions'] for v in residual)==26
    rows=[];partitions=[];oracles=[]
    for r in residual:
        assert r['N']==4 and sum(r['d'][:3])>13
        for p,q in r['positive_pairs']:
            row=construct(28,r['d'],p,q);rows.append(row)
            partitions.append(materialize_two_baselines(row))
            oracles.append(dict(M=28,d=r['d'],p=p,q=q,oracle=maps(28,r['d'],p,q)))
    assert len(rows)==len(partitions)==26
    fixtures=[(16,[1,3,4,4],13,11),(20,[2,4,4,6],17,15),
              (12,[2,2,2,2],9,7),(28,[4,5,6,9],25,23)]
    boundaries=[]
    for M,d,p,q in fixtures:
        boundaries.append(dict(row=construct(M,d,p,q),oracle=maps(M,d,p,q)))
    assert boundaries[0]['row']['J']==0 and boundaries[3]['row']['H']==0
    assert len(set(boundaries[2]['row']['A']+boundaries[2]['row']['B']))==6
    refused=False
    try:construct(12,[1,1,2,2],9,3)
    except ValueError:refused=True
    assert refused
    negative=maps(12,[1,1,2,2],9,3,False)
    assert [v['z'] for v in negative['offsets']]==[-2,-1,0,1,2]
    alpha=1
    allowed=[v for v in negative['offsets'] if -alpha<=v['z']<=alpha]
    assert [v['z'] for v in allowed]==[-1,0,1] and all(not v['valid'] for v in allowed)
    alternate=validation.validate(12,[1,1,2,2],9,3,[0,2],[1,3,4,5],0,False)
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<2 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='eb0b7b6d',
                         pre_run_correction='23bedaef',input_sha256=digest,
                         frozen_profiles=15,frozen_questions=26,formula_calls=30,
                         E28_partitions=26,rows=rows,partitions=partitions,oracles=oracles,
                         boundaries=boundaries,scope_refusal=refused,
                         paired_failure_control=negative,alternate_split=alternate,
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
