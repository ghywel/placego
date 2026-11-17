#!/usr/bin/env python3
"""B101/MI228 prereg78d950d7: arbitrary short pair in a five-gap cycle.

Eleven frozen nonunit E28 partitions/five generic formulas; fixed-split
original-root maps, wrong short order, reflection and capacity-scope controls.
2CPU sec/64MiB; no whole-cycle solver or widened input grid. Claim SKETCH.
OUTCOME MI229:16 formulas/11 E28 partitions/249 root-order candidates pass;
5 reflections;0.022620CPU sec/21659648RSS bytes. Artifact SHA256
c1334f28a3b50f8fa5bab634966e47fccb34b511bfa1f236977e9effaa68d244.
"""
from collections import Counter
from itertools import permutations,product
from pathlib import Path
import hashlib
import json
import resource
import time

import path_forest_partial_padding as validation
from path_forest_two_unit_triangle import partition


def prefix(root,gaps):
    out=[root]
    for gap in gaps:out.append(out[-1]+gap)
    return out


def construct(M,d,p,q):
    assert M%2==0 and len(d)==5 and list(d)==sorted(d) and min(d)>0
    a,b,u,v,w=d;C=a+b;L=u+v;S=w+C;h=M//2-1;H=h-L;J=h-S
    if u<C+3 or min(H,J)<0 or H>=C:raise ValueError('outside nonisolatable canonical-split scope')
    K=sum(d);D=L-S;T=H+J
    assert p>0 and q>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=M-3 and not p==q==M-3 and T>=2
    alpha=(M-1-max(p,q))//2;assert 1<=alpha< T and alpha<=(T+1)//2
    c=alpha;E=r=None
    if D>=2:
        c=alpha if alpha%2 else alpha-1
        x=min(H,(c-1)//2);z=c-2*x;y=x+z;order=[a,b,w]
        assert 1<=z<=D-1
        branch='wide_positive'
    elif D==1:
        c=alpha if alpha%2 else alpha-1
        x=(c+1)//2;y=(c-1)//2;order=[w,a,b]
        assert H>=1 and w-1>u
        branch='one_margin_negative'
    elif alpha<=2*J:
        c=alpha if alpha%2 else alpha-1
        x=(c-1)//2;y=(c+1)//2;order=[a,b,w]
        assert C+1<u and S+1>L
        branch='nonpositive_margin_positive_root'
    else:
        y=J;x=alpha-J;z=y-x;E=T-alpha;r=C-E
        assert z<0 and 0<E<C and z+w>u and z+S>L
        if r!=a:
            order=[w,a,b];branch='forced_big_first'
        elif a!=b:
            order=[w,b,a];branch='forced_short_order_swap'
        elif -z>=2:
            assert a==b and E==a and a>=2 and x>=2
            c=alpha-1;x-=1;E+=1;r-=1;order=[w,a,b]
            assert y-x<0 and 0<r<C and r!=a
            branch='equal_pair_root_shift'
        else:
            assert z==-1 and a==b and E==a and a>=2
            order=[a,b,w];branch='equal_pair_small_first'
    assert c in (alpha,alpha-1) and c>=1 and x+y==c
    assert 0<=x<=H and 0<=y<=J
    preA=prefix(x,[u,v]);preB=prefix(y,order)
    assert not set(preA)&set(preB) and len(set(preA+preB))==7
    first=0 if p>=q else 1;reflected=c==alpha-1;A=preA;B=preB
    if reflected:
        A=[h-z for z in reversed(A)];B=[h-z for z in reversed(B)];first=1-first
    row=validation.validate(M,d,p,q,A,B,first,False)
    row.update(M=M,d=d,p=p,q=q,C=C,L=L,S=S,H=H,J=J,D=D,T=T,
               alpha=alpha,root=c,z=y-x,E=E,r=r,B_gap_order=order,
               preA=preA,preB=preB,reflected=reflected,branch=branch)
    return row


def independent_map(row):
    M=row['M'];a,b,u,v,w=row['d'];h=M//2-1;H=h-u-v;J=h-w-a-b
    p=row['p'];q=row['q'];K=sum(row['d']);count=0;accepted=[]
    for x in range(H+1):
        for y in range(J+1):
            P=M-1-2*(x+y);Q=2*K-P
            if Counter((P,Q))!=Counter((p,q)):continue
            for ao,bo in product(sorted(set(permutations((u,v)))),sorted(set(permutations((a,b,w))))):
                A=prefix(x,ao);B=prefix(y,bo);xs,word=validation.physical(M,A,B);count+=1
                assert Counter(word)==Counter((p,q,*(-2*z for z in row['d'])))
                direct=not set(A)&set(B)
                assert validation.literal(M,xs)==direct
                assert validation.instrument.literal_geometry(M,set(),xs)==direct
                if direct:accepted.append(dict(A=A,B=B,first_positive=P))
    assert any(v['A']==row['A'] and v['B']==row['B'] for v in accepted)
    return dict(original_root_order_candidates=count,accepted=accepted)


def main():
    start=time.process_time();raw=Path('/tmp/math-instinct-b87-admission-synthesis.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    assert digest=='3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0'
    prior=json.loads(raw);chosen=[]
    for rec in prior['records']:
        d=rec['d']
        if rec['N']==5 and d[:2]==[1,2] and d[2]>=6 and d[2]+d[3]+3>13:
            if d[2]+d[3]<=13 and d[4]+3<=13:chosen.append(rec)
    explicit={(1,2,6,6,w) for w in (6,7,8,9)}|{(1,2,6,7,w) for w in (7,8)}
    assert {tuple(v['d']) for v in chosen}==explicit and len(chosen)==6
    assert sum(v['questions'] for v in chosen)==11
    rows=[];partitions=[];oracles=[]
    for rec in chosen:
        for p,q in rec['positive_pairs']:
            row=construct(28,rec['d'],p,q);rows.append(row)
            partitions.append(partition(row));oracles.append(independent_map(row))
    assert Counter(v['branch'] for v in rows)=={'wide_positive':8,'one_margin_negative':2,
                                               'nonpositive_margin_positive_root':1}
    fixtures=[(42,[2,3,8,8,15],39,33),(48,[3,3,9,9,17],43,39),
              (46,[3,3,9,9,16],43,37),(36,[2,2,7,7,13],31,31),
              (42,[2,3,8,8,13],39,29)]
    expected=['forced_short_order_swap','equal_pair_root_shift','equal_pair_small_first',
              'forced_big_first','nonpositive_margin_positive_root']
    generic=[]
    for args,branch in zip(fixtures,expected):
        row=construct(*args);assert row['branch']==branch
        generic.append(dict(row=row,oracle=independent_map(row)))
    # Same exact bag, but omitting the unequal short-order swap collides at17.
    badA=[1,9,17];badB=[0,15,17,20];xs,word=validation.physical(42,badA,badB)
    assert Counter(word)==Counter((39,33,-4,-6,-16,-16,-30))
    assert set(badA)&set(badB)=={17} and len(set(xs))==7 and all(0<=x<42 for x in xs)
    assert not validation.literal(42,xs) and not validation.instrument.literal_geometry(42,set(),xs)
    shifted=generic[1]['row'];assert shifted['reflected']
    prexs,preword=validation.physical(48,shifted['preA'],shifted['preB'])
    assert validation.literal(48,prexs) and validation.instrument.literal_geometry(48,set(),prexs)
    assert (preword[0],preword[len(shifted['preB'])])==(45,37)
    assert Counter(preword)!=Counter((43,39,-6,-6,-18,-18,-34))
    refused=False
    try:construct(40,[2,3,8,8,15],35,37)
    except ValueError:refused=True
    assert refused and 2+15==17<=19 and 3+8+8==19 and 8+8==16 and 15+2+3==20>19
    alternate=validation.validate(40,[2,3,8,8,15],35,37,[1,3,18],[0,8,11,19],1,False)
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<2 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='78d950d7',
                         input_sha256=digest,frozen_profiles=6,frozen_questions=11,
                         formula_calls=16,E28_partitions=11,rows=rows,partitions=partitions,
                         oracles=oracles,generic=generic,
                         omitted_short_order_swap=dict(A=badA,B=badB,positions=xs,word=word,
                                                       original_bag_valid=True,folded_valid=False),
                         omitted_reflection=dict(positions=prexs,word=preword,
                                                 geometry_valid=True,original_bag_valid=False),
                         canonical_capacity_refusal=refused,
                         outside_scope_alternate=alternate,cpu_seconds=elapsed,
                         peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
