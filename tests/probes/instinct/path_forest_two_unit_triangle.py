#!/usr/bin/env python3
"""B100/MI226 prerega2cb4e2f: two unit gaps and three large gaps.

Thirty explicit formulas/27 E28 partitions, fixed-split independent maps,
naive unit-order/reflection/outside-premise controls;2CPU sec/64MiB.
No whole-cycle solver or full input-grid regeneration; general claim SKETCH.
OUTCOME MI227:30 formulas/27 E28 partitions/375 original-root checks pass;
10 reflected calls;0.028234CPU sec/20533248RSS bytes. Artifact SHA256
537fbb2bef3660662704b9c0d06a0a1f5eae8a23b3c2c93164a2909daa9ee1f6.
"""
from collections import Counter
from itertools import permutations,product
from pathlib import Path
import hashlib
import json
import resource
import time

import path_forest_partial_padding as validation


def construct(M,d,p,q):
    assert M%2==0 and len(d)==5 and list(d)==sorted(d) and d[:2]==[1,1]
    u,v,w=d[2:];h=M//2-1;L=u+v;W=L-w
    if u<5 or L>h or W<2:raise ValueError('outside triangle interleaving scope')
    K=sum(d);H=h-L;J=h-w-2;T=H+J
    assert min(p,q)>0 and p%2 and q%2 and p+q==2*K
    assert max(p,q)<=M-3 and not p==q==M-3 and T>=2
    alpha=(M-1-max(p,q))//2;assert 1<=alpha<=(T+1)//2
    root=alpha if alpha%2 else alpha-1
    assert root%2 and root in (alpha,alpha-1)
    if W>=4:
        x=min(H,(root-1)//2);z=root-2*x;y=x+z
        assert 1<=z<=W-3
        preA=[x,x+u,x+L];preB=[y,y+1,y+2,y+w+2]
        interleaved=[x,y,y+1,y+2,x+u,y+w+2,x+L]
        branch='units_first_positive_offset'
    else:
        assert W in (2,3) and H>=1
        x=(root+1)//2;y=(root-1)//2;z=-1
        preA=[x,x+u,x+L];preB=[y,y+w,y+w+1,y+w+2]
        interleaved=[y,x,x+u,y+w,y+w+1,y+w+2,x+L]
        branch='large_first_negative_offset'
    assert all(a<b for a,b in zip(interleaved,interleaved[1:]))
    assert 0<=x<=H and 0<=y<=J and x+y==root
    first=0 if p>=q else 1;reflected=root==alpha-1;A=preA;B=preB
    if reflected:
        A=[h-vv for vv in reversed(A)];B=[h-vv for vv in reversed(B)];first=1-first
    row=validation.validate(M,d,p,q,A,B,first,False)
    row.update(M=M,d=d,p=p,q=q,L=L,W=W,H=H,J=J,T=T,alpha=alpha,
               root=root,z=z,preA=preA,preB=preB,reflected=reflected,
               branch=branch,strict_interleaving=interleaved)
    return row


def partition(row):
    assert row['M']==28 and len(row['d'])==5
    d=row['d'];p=row['p'];q=row['q'];first=row['first_owner']
    e=[p,q]+[-2*v for v in d]+[0];sizes=[1,1]+[2]*6
    targets=[56*s+2*v for s,v in zip(sizes,e)]
    assert min(targets)>=68 and sum(targets)==784
    pool={v:[i+2 for i,w in enumerate(d) if w==v] for v in set(d)};selected={}
    for j,move in enumerate(row['word']):
        owner=first if j==0 else 1-first if j==len(row['B']) else pool[-move//2].pop(0)
        assert e[owner]==move;selected[owner]=row['positions'][j]
    assert set(selected)==set(range(7)) and all(not v for v in pool.values())
    bins=validation.instrument.materialize(28,set(),[0]*8,sizes,e,selected,targets)
    assert validation.instrument.literal_ok(28,bins,targets,sizes)
    assert validation.instrument.independent_ok(28,bins,targets)
    return dict(targets=targets,bins=bins,selected=selected,baseline_owner=7,owner_moves=e)


def independent_map(row):
    M=row['M'];d=row['d'];p=row['p'];q=row['q'];h=M//2-1;u,v,w=d[2:]
    H=h-u-v;J=h-w-2;K=sum(d);checks=0;accepted=[]
    for x in range(H+1):
        for y in range(J+1):
            P=M-1-2*(x+y);Q=2*K-P
            if Counter((P,Q))!=Counter((p,q)):continue
            for Asteps,Bsteps in product(sorted(set(permutations((u,v)))),
                                         sorted(set(permutations((1,1,w))))):
                A=[x,x+Asteps[0],x+sum(Asteps)]
                B=[y,y+Bsteps[0],y+sum(Bsteps[:2]),y+sum(Bsteps)]
                xs,word=validation.physical(M,A,B);checks+=1
                assert Counter(word)==Counter((p,q,*(-2*z for z in d)))
                direct=not set(A)&set(B)
                assert validation.literal(M,xs)==direct
                assert validation.instrument.literal_geometry(M,set(),xs)==direct
                if direct:accepted.append(dict(A=A,B=B,first_positive=P))
    assert any(v['A']==row['A'] and v['B']==row['B'] for v in accepted)
    return dict(original_root_order_candidates=checks,valid_candidates=accepted)


def main():
    start=time.process_time();raw=Path('/tmp/math-instinct-b87-admission-synthesis.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    assert digest=='3b53cad88d8f0930397f545953dbad8b3a2a38adc7e37242bd90641a9ad885d0'
    prior=json.loads(raw);chosen=[]
    for r in prior['records']:
        d=r['d']
        if r['N']==5 and d[:2]==[1,1] and d[2]>=5 and d[2]+d[3]+2>13:chosen.append(r)
    explicit={(1,1,5,7,w) for w in (7,8,9,10)}|{(1,1,6,6,w) for w in (6,7,8,9,10)}
    explicit|={(1,1,5,8,w) for w in (8,9)}|{(1,1,6,7,w) for w in (7,8,9)}
    assert {tuple(v['d']) for v in chosen}==explicit and len(chosen)==14
    assert sum(v['questions'] for v in chosen)==27
    overlap=next(v for v in chosen if v['d']==[1,1,5,7,10])
    assert 'MI193_SKETCH_shared' in overlap['admissions']
    rows=[];partitions=[];oracles=[]
    for r in chosen:
        for p,q in r['positive_pairs']:
            row=construct(28,r['d'],p,q);rows.append(row)
            partitions.append(partition(row));oracles.append(independent_map(row))
    assert len(rows)==27
    assert Counter(v['branch'] for v in rows)=={'units_first_positive_offset':21,
                                               'large_first_negative_offset':6}
    fixtures=[(34,[1,1,8,8,8],27,25),(26,[1,1,5,6,8],23,19),(26,[1,1,5,6,9],23,21)]
    generic=[]
    for M,d,p,q in fixtures:
        row=construct(M,d,p,q);generic.append(dict(row=row,oracle=independent_map(row)))
    assert generic[0]['row']['H']==0 and generic[0]['row']['z']==3
    # Correct original bag and window but shared index12: naive positive-offset order.
    A=[0,5,12];B=[1,2,3,12];xs,word=validation.physical(28,A,B)
    assert Counter(word)==Counter((21,25,-2,-2,-10,-14,-18))
    assert set(A)&set(B)=={12} and len(set(xs))==7 and all(0<=x<28 for x in xs)
    assert not validation.literal(28,xs) and not validation.instrument.literal_geometry(28,set(),xs)
    naive=dict(A=A,B=B,positions=xs,word=word,bag_valid=True,folded_valid=False)
    reflected=next(v for v in rows if v['d']==[1,1,5,7,9] and v['p']==v['q']==23)
    assert reflected['alpha']==2 and reflected['root']==1 and reflected['reflected']
    unreflected_xs,unreflected_word=validation.physical(28,reflected['preA'],reflected['preB'])
    assert validation.literal(28,unreflected_xs)
    assert unreflected_word[0]==25 and unreflected_word[len(reflected['preB'])]==21
    assert Counter(unreflected_word)!=Counter((23,23,-2,-2,-10,-14,-18))
    refused=False
    try:construct(20,[1,1,4,4,5],13,17)
    except ValueError:refused=True
    assert refused
    badA=[1,5,9];badB=[0,5,6,7];badxs,badword=validation.physical(20,badA,badB)
    assert Counter(badword)==Counter((13,17,-2,-2,-8,-8,-10))
    assert set(badA)&set(badB)=={5} and not validation.literal(20,badxs)
    assert not validation.instrument.literal_geometry(20,set(),badxs)
    alternate=validation.validate(20,[1,1,4,4,5],13,17,[0,4,9],[1,2,3,7],1,False)
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<2 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='a2cb4e2f',
                         input_sha256=digest,frozen_profiles=14,frozen_questions=27,
                         formula_calls=30,E28_partitions=27,rows=rows,partitions=partitions,
                         oracles=oracles,generic=generic,overlap_control=overlap,
                         naive_unit_order_control=naive,scope_refusal=refused,
                         omitted_reflection_control=dict(positions=unreflected_xs,word=unreflected_word,
                                                         geometry_valid=True,original_bag_valid=False),
                         outside_premise_bad_order=dict(A=badA,B=badB,word=badword),
                         outside_premise_alternate=alternate,cpu_seconds=elapsed,
                         peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
