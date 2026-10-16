#!/usr/bin/env python3
"""B75/MI171 preregd4f2b8e4: arbitrary negative sizes, odd p/q,total<=26.

Complete24982 labelled geometries, independent4095 positive compositions,
all eligible E28 partitions and four prescribed controls.10CPU sec/128MiB.
No order/root search or sample; prefix rearrangement is the recorded MI117 tool.
General carrying argument remains PROOF-SKETCH, not upgraded by finite checks.
OUTCOME:24982 geometries pass,12700 eligible E28 evaluations/735 distinct
sorted targets;7309 actual prefix rearrangements. All controls pass.2.426114CPU
sec,64249856bytes RSS. Raw SHA256
d639545c88683c4dd82600fc7a5821d6dba66af54490e9b07e64313dbc900e62.
"""
from collections import Counter
from itertools import combinations
from math import comb
import json
import resource
import time

import path_forest_balanced_bridge as instrument


def compositions(K,N):
    if N==1:
        yield (K,)
    else:
        for first in range(1,K-N+2):
            for rest in compositions(K-first,N-1):yield (first,*rest)


def avoid_prefix(d,F):
    assert len(set(d))>1 and 0<F<sum(d)
    order=list(range(len(d)));total=0;cut=None
    for k,i in enumerate(order):
        total+=d[i]
        if total==F:cut=k+1;break
        if total>F:break
    if cut is None:return order,False
    left=order[:cut];right=order[cut:]
    i,j=next((i,j) for i in left for j in right if d[i]!=d[j])
    result=[k for k in left if k!=i]+[j,i]+[k for k in right if k!=j]
    assert sorted(result)==order
    sums=[];total=0
    for k in result:total+=d[k];sums.append(total)
    assert F not in sums
    return result,True


def positions(p,q,d,negative_order,root):
    word=[p,q]+[-2*d[i] for i in negative_order]
    xs=[root]
    for v in word:xs.append(xs[-1]+v)
    assert xs[-1]==root
    return word,xs[:-1]


def construct(p,q,d):
    N=len(d);K=sum(d)
    assert 1<=N<=6 and min(d)>0 and p>0 and p%2 and q%2 and p<=q
    assert p+q==2*K<=26
    H=(27-p)//2;order=list(range(N));changed=False
    if H>K:root=0;case='OUTSIDE_PREFIX_RANGE';F=None
    elif len(set(d))==1:
        D=d[0];assert D>=2
        root=int(H%D==0);case='CONSTANT';F=None
    else:
        root=int(H==K);F=H-root
        order,changed=avoid_prefix(d,F);case='NONCONSTANT'
    negative_order=order[::-1]
    word,xs=positions(p,q,d,negative_order,root)
    labels=[min(x,27-x) for x in xs]
    assert len(set(labels))==N+2 and all(0<=x<=27 for x in xs)
    assert instrument.literal_geometry(28,set(),xs)
    prefix={0};total=0
    for i in order:total+=d[i];prefix.add(total)
    assert H-root not in prefix
    reflected=[27-x for x in xs]
    assert instrument.literal_geometry(28,set(),reflected)
    assert all(reflected[(i+1)%len(xs)]-reflected[i]==-word[i] for i in range(len(xs)))
    assert [min(x,27-x) for x in reflected]==labels
    owners=[0,1]+[i+2 for i in negative_order];selected=dict(zip(owners,xs))
    h=[1,1]+[2]*6;e=[p,q]+[-2*v for v in d]+[0]*(6-N)
    t=[56*s+2*v for s,v in zip(h,e)]
    assert sum(t)==784
    eligible=all(68<=v<=122 for v in t)
    bins=instrument.materialize(28,set(),[0]*8,h,e,selected,t) if eligible else None
    return dict(p=p,q=q,negative_halves=d,K=K,case=case,root=root,
                forbidden=F,rearranged=changed,positive_prefix_order=order,
                positions=xs,selected=selected,labels=labels,targets=t,
                E28=eligible,bins=bins)


def controls():
    d=(1,1,1,2,2,6);_,bad=positions(13,13,d,list(range(6))[::-1],0)
    assert 13 in bad and 14 in bad and not instrument.literal_geometry(28,set(),bad)
    fixed=construct(13,13,d)
    assert fixed['rearranged'] and fixed['root']==0
    d2=(2,)*6;_,bad2=positions(7,17,d2,list(range(6))[::-1],0)
    assert not instrument.literal_geometry(28,set(),bad2)
    fixed2=construct(7,17,d2);assert fixed2['root']==1
    de=(1,1,1,1,1,6);_,bade=positions(5,17,de,list(range(6))[::-1],0)
    assert not instrument.literal_geometry(28,set(),bade)
    fixede=construct(5,17,de);assert fixede['root']==1 and fixede['forbidden']==10
    dh=(1,1,1,1,1,9);_,badh=positions(13,15,dh,list(range(6))[::-1],0)
    assert 28 in badh and not instrument.literal_geometry(28,set(),badh)
    try:construct(13,15,dh)
    except AssertionError:pass
    else:raise AssertionError('outside positive-total cap accepted')
    return dict(prefix_hit=dict(bad_positions=bad,repaired=fixed),
                constant=dict(bad_positions=bad2,repaired=fixed2),
                endpoint=dict(bad_positions=bade,repaired=fixede),
                high_total=dict(bad_positions=badh,status='OUTSIDE_THEOREM_REJECTED'))


def main():
    start=time.process_time();rows=[];lists=0;counts=Counter();swaps=0
    for K in range(1,14):
        for N in range(1,min(6,K)+1):
            ds=list(compositions(K,N))
            reference={tuple(b-a for a,b in zip((0,*bars),(*bars,K)))
                       for bars in combinations(range(1,K),N-1)}
            assert len(ds)==comb(K-1,N-1) and set(ds)==reference
            lists+=len(ds)
            for d in ds:
                for p in range(1,K+1,2):
                    row=construct(p,2*K-p,d);rows.append(row)
                    counts[(N,row['case'],row['E28'])]+=1
                    swaps+=row['rearranged']
                assert time.process_time()-start<10
                assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<128*1024*1024
    assert lists==sum(comb(13,N) for N in range(1,7))==4095
    predicted=sum(comb(K-1,N-1)*((K+1)//2) for K in range(1,14) for N in range(1,min(6,K)+1))
    assert len(rows)==predicted==24982
    control=controls();eligible=[r for r in rows if r['E28']]
    distinct={tuple(sorted(r['targets'])) for r in eligible}
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<10 and rss<128*1024*1024
    print(json.dumps(dict(status='ALL_FORMULA_CERTIFICATES_PASS',preregistration='d4f2b8e4',
                         geometry_questions=len(rows),composition_lists=lists,
                         eligible_E28_evaluations=len(eligible),distinct_sorted_E28=len(distinct),
                         prefix_rearrangements=swaps,
                         case_counts={str(k):v for k,v in sorted(counts.items())},
                         controls=control,rows=rows,cpu_seconds=elapsed,peak_rss_bytes=rss),
                     separators=(',',':')))


if __name__=='__main__':main()
