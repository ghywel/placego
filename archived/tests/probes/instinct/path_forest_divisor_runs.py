#!/usr/bin/env python3
"""B77/MI175 preregde4d6970: gcd>=2 exact criterion is two-run load capacity.

12375 sorted M28 profile candidates,N<=6,d1..11,high total K14..25;<=5000
p/q questions. Full subset-sum DP vs independent masks, exact formula roots,
all eligible partitions; general-M/gcd1/long-jump controls.10CPU sec/128MiB.
No order/root/role search or census extrapolation. Hand theorem remains SKETCH.
OUTCOME:490 high-total questions:476 construct,14 no capacity;443 eligible
partitions. Full subset sums and all controls agree.0.078908CPU sec,16584704bytes
RSS. Raw SHA256 1d660fd7cecfda6ef66353bc7277ee3d5ec05bd6285dc50d951d913edf1a59f9.
"""
from collections import Counter
from itertools import combinations_with_replacement
from math import gcd
import json
import resource
import time

import path_forest_balanced_bridge as instrument


def capacity(d,C):
    reach=1;parents={0:0}
    for i,v in enumerate(d):
        reach|=reach<<v
        for old,mask in list(parents.items()):
            parents.setdefault(old+v,mask|(1<<i))
    sums={s for s in range(sum(d)+1) if reach>>s&1}
    assert sums==set(parents)
    reference={sum(v for i,v in enumerate(d) if mask>>i&1) for mask in range(1<<len(d))}
    assert sums==reference
    lower=max(0,sum(d)-C)
    possible=[s for s in range(lower,C+1) if s in sums]
    if not possible:return None,sorted(sums)
    s=possible[0];mask=parents[s]
    assert sum(v for i,v in enumerate(d) if mask>>i&1)==s
    assert s<=C and sum(d)-s<=C
    return mask,sorted(sums)


def raw_word(p,q,d,A,B,h):
    owners=[0]+[i+2 for i in A]+[1]+[i+2 for i in B]
    word=[p]+[-2*d[i] for i in A]+[q]+[-2*d[i] for i in B]
    xs=[h]
    for e in word:xs.append(xs[-1]+e)
    assert xs[-1]==h
    return owners,word,xs[:-1]


def construct(M,p,q,d,mask=None):
    N=len(d);K=sum(d);g=gcd(*d)
    assert M%2==0 and p>0 and q>0 and p%2 and q%2 and p+q==2*K and min(d)>0
    assert g>=2
    if max(p,q)>M-3:return dict(status='ODD_JUMP_BOUND_REJECTED',M=M,p=p,q=q,d=d)
    C=M//2-1
    if mask is None:
        mask,_=capacity(d,C)
        if mask is None:return dict(status='NO_TWO_RUN_CAPACITY',M=M,p=p,q=q,d=d)
    A=[i for i in range(N) if mask>>i&1];B=[i for i in range(N) if not(mask>>i&1)]
    s=sum(d[i] for i in A);t=sum(d[i] for i in B)
    assert s<=C and t<=C
    w=p-2*s;L=max(0,-w);R=min(M-1-p,M-1-2*t);H=(M-1-w)//2
    assert R>=L+1 and (M-1-w)%2==0 and N+2<=M//2
    root=L+int(L%g==H%g)
    assert L<=root<=R and (H-root)%g!=0
    owners,word,xs=raw_word(p,q,d,A,B,root)
    assert len(xs)==len(set(xs))==N+2 and instrument.literal_geometry(M,set(),xs)
    labels=[min(x,M-1-x) for x in xs];assert len(set(labels))==N+2
    reflected=[M-1-x for x in xs]
    assert instrument.literal_geometry(M,set(),reflected)
    selected=dict(zip(owners,xs));eligible=False;bins=None;targets=None
    if M==28 and N<=6:
        e=[p,q]+[-2*v for v in d]+[0]*(6-N);h=[1,1]+[2]*6
        targets=[56*a+2*b for a,b in zip(h,e)]
        assert sum(targets)==784
        eligible=all(68<=v<=122 for v in targets)
        if eligible:bins=instrument.materialize(28,set(),[0]*8,h,e,selected,targets)
    return dict(status='CONSTRUCTED',M=M,p=p,q=q,d=d,gcd=g,group_mask=mask,
                loads=(s,t),root_interval=(L,R),root=root,forbidden_residue=H%g,
                selected=selected,positions=xs,labels=labels,E28=eligible,
                targets=targets,bins=bins)


def controls():
    generic=[construct(6,1,3,(2,)),construct(16,11,13,(2,)*6),construct(22,17,19,(3,)*6)]
    assert all(r['status']=='CONSTRUCTED' for r in generic)
    negative=construct(28,23,25,(8,8,8))
    assert negative['status']=='NO_TWO_RUN_CAPACITY'
    positive=construct(28,23,25,(4,)*6)
    assert positive['status']=='CONSTRUCTED' and positive['E28']
    odd_g=construct(28,21,21,(3,3,3,3,3,6))
    assert odd_g['status']=='CONSTRUCTED' and odd_g['gcd']==3 and odd_g['root']==1
    long_jump=construct(28,27,21,(4,)*6)
    assert long_jump['status']=='ODD_JUMP_BOUND_REJECTED'
    d=(3,3,3,4,4,4);A=[0,1,2];B=[3,4,5];bad=[]
    for root in range(4):
        _,_,xs=raw_word(21,21,d,A,B,root)
        assert not instrument.literal_geometry(28,set(),xs)
        bad.append(xs)
    alternative=[0,21,15,7,1,22,14,8]
    assert instrument.literal_geometry(28,set(),alternative)
    try:construct(28,21,21,d)
    except AssertionError:pass
    else:raise AssertionError('gcd1 incorrectly admitted to theorem')
    return dict(general_M=generic,no_capacity=negative,matching_positive=positive,
                odd_divisor=odd_g,long_jump=long_jump,
                gcd1=dict(fixed_run_failures=bad,known_alternative=alternative))


def main():
    start=time.process_time();candidates=0;retained=0;rows=[];statuses=Counter();odd_g=0
    for N in range(1,7):
        for d in combinations_with_replacement(range(1,12),N):
            candidates+=1;K=sum(d);g=gcd(*d)
            if not(14<=K<=25 and g>=2):continue
            retained+=1;mask,sums=capacity(d,13)
            for p in range(1,min(K,25)+1,2):
                q=2*K-p
                if q>25:continue
                if mask is None:
                    row=dict(status='NO_TWO_RUN_CAPACITY',M=28,p=p,q=q,d=d,
                             gcd=g,reachable_sums=sums,E28=(p>=7))
                    # Different independent instrument verifies the refusal interval.
                    assert not any(K-13<=s<=13 for s in sums)
                else:
                    row=construct(28,p,q,d,mask)
                    assert row['status']=='CONSTRUCTED'
                    if g%2:odd_g+=1
                rows.append(row);statuses[row['status']]+=1
                assert len(rows)<=5000
                assert time.process_time()-start<10
                assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<128*1024*1024
    assert candidates==12375 and statuses['CONSTRUCTED'] and statuses['NO_TWO_RUN_CAPACITY']
    assert odd_g>0
    control=controls();eligible=[r for r in rows if r['status']=='CONSTRUCTED' and r['E28']]
    distinct={tuple(sorted(r['targets'])) for r in eligible}
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<10 and rss<128*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='de4d6970',
                         candidate_profiles=candidates,retained_profiles=retained,
                         profile_pair_questions=len(rows),status_counts=dict(statuses),
                         E28_constructed=len(eligible),distinct_sorted_E28=len(distinct),
                         odd_divisor_constructions=odd_g,rows=rows,controls=control,
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
