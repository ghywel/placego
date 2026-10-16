#!/usr/bin/env python3
"""B87/MI197 prerega28f88f0: fixed-domain admission synthesis, no cycle search.

M28, N1..6, halves1..11, K14..24,13/13 capacity; predict6788 questions.
Independent recursive profile and explicit subset-set control. Two literal
E28 witnesses, including a residual-positive diagnostic.5CPU sec/128MiB.
Only gcd admission PROVED; other tags SKETCH, no existence/coverage upgrade.
Outcome MI198: all prescribed checks pass;2173 eligible profiles/6788
questions,5266 selected admissions,1522 residual,476 PROVED-tag questions.
Two literal E28 partitions pass; residual-positive fixture stays residual.
CPU0.061249s/peakRSS18640896bytes. Raw data outside git; no solver run.
"""
from collections import Counter
from itertools import combinations_with_replacement,product
from math import gcd
import json
import resource
import time

import path_forest_partial_padding as validation


def capacity(d):
    bits=1
    for v in d:bits|=bits<<v
    K=sum(d);lo=max(0,K-13)
    return any((bits>>v)&1 for v in range(lo,14))


def capacity_set(d):
    sums={0}
    for v in d:sums|={s+v for s in sums}
    return any(sum(d)-13<=s<=13 for s in sums)


def admissions(d):
    N=len(d);K=sum(d);k=12-N;r=max(0,(K-2*N+1)//2);out={}
    g=gcd(*d)
    if g>=2:out['MI175_PROVED_gcd']=dict(gcd=g)
    for modulus in range(3,23):
        exceptions=[i for i,v in enumerate(d) if v%modulus]
        if len(exceptions)!=2:continue
        a,b=(d[i] for i in exceptions)
        if (a+b)%modulus:continue
        atom=[a+b]+[v for i,v in enumerate(d) if i not in exceptions]
        if capacity(atom):
            out['MI177_SKETCH_complementary']=dict(modulus=modulus,exceptions=exceptions,atomic_profile=atom)
            break
    if N%2==0 and min(d)>=2 and all(y-x<=3 for x,y in zip(d[::2],d[1::2])):
        out['MI186_SKETCH_sorted_pairs']=dict(pairs=list(zip(d[::2],d[1::2])))
    descending=sorted(d,reverse=True)
    if r==0 or len(d)>=2 and descending[1]>=r+2:
        out['MI191_SKETCH_partial']=dict(r=r,second=descending[1] if N>=2 else None)
    if r==0:out['MI193_SKETCH_shared']=dict(r=0)
    else:
        available=0;chosen=[];need=r+1-K%2
        for E in descending[1:]:
            if E<2:break
            available+=E-1;chosen.append(E)
            if available>=need:break
        if available>=need and descending[0]>=r+len(chosen)+1:
            out['MI193_SKETCH_shared']=dict(r=r,epsilon=K%2,E=chosen,required_D=r+len(chosen)+1)
    D=max(d);S=K-D
    if D>=S+2:out['MI197_SKETCH_dominant']=dict(D=D,S=S,inner_slack=D-S-1)
    old=N>=2 and descending[1]>=k+2
    assert not old or 'MI191_SKETCH_partial' in out
    assert 'MI191_SKETCH_partial' not in out or 'MI193_SKETCH_shared' in out
    if len([v for v in d if v!=1])==1 and D>=N+1:
        assert 'MI197_SKETCH_dominant' in out
    return out,old


def fixed_sum_profiles(N,K,lo=1):
    if N==0:
        if K==0:yield ()
        return
    if K<N*lo or K>N*11:return
    for v in range(lo,min(11,K//N)+1):
        for rest in fixed_sum_profiles(N-1,K-v,v):yield (v,)+rest


def mixed_dominant_witness():
    M=28;d=[11,3,2,2,1,1];p=25;q=15;n=14
    D=max(d);rest=d[1:];S=sum(rest);W=D-S-1;H=n-1-D
    assert W==1
    owners=[i for i,v in enumerate((p,q)) if (v-(M-3))%4==0];assert len(owners)==1
    first=owners[0];alpha=(M-1-(p,q)[first])//2
    b=min(W,alpha)
    if (alpha-b)%2:b-=1
    a=(alpha-b)//2;assert 0<=a<=H and 1<=b<=W
    A=[a,a+D];B=[a+b]
    for v in rest:B.append(B[-1]+v)
    assert A==[0,11] and B==[1,4,6,8,9,10]
    row=validation.validate(M,d,p,q,A,B,first,True)
    assert row['positions']==[0,25,19,15,11,9,7,22]
    return row


def main():
    start=time.process_time();records=[];all_profiles=0;profile_keys=set()
    tag_questions=Counter();tag_profiles=Counter();byN=Counter();residualN=Counter();residualK=Counter()
    for N in range(1,7):
        for d in combinations_with_replacement(range(1,12),N):
            all_profiles+=1;K=sum(d)
            if not(14<=K<=24) or not capacity(d):continue
            pairs=[(p,2*K-p) for p in range(max(1,2*K-25),K+1,2)]
            assert pairs and all(p%2 and q%2 and p<=q<=25 and p+q==2*K for p,q in pairs)
            tags,old=admissions(d);count=len(pairs);profile_keys.add(d)
            record=dict(d=d,N=N,K=K,positive_pairs=pairs,questions=count,admissions=tags,
                        old_MI180_admitted=old,proved_admitted='MI175_PROVED_gcd' in tags)
            records.append(record);byN[N]+=count
            for tag in tags:tag_questions[tag]+=count;tag_profiles[tag]+=1
            if not tags:residualN[N]+=count;residualK[K]+=count
    assert all_profiles==12375
    independent={d for N in range(1,7) for K in range(14,25)
                 for d in fixed_sum_profiles(N,K) if capacity_set(d)}
    assert independent==profile_keys
    independent_questions=sum(sum(1 for p in range(1,26,2) if p<=2*sum(d)-p<=25) for d in independent)
    questions=sum(v['questions'] for v in records)
    assert questions==independent_questions==6788
    residual=[v for v in records if not v['admissions']]
    assert residual
    control=next(v for v in records if v['d']==(2,2,3,4,4,9))
    assert not control['admissions'] and control['positive_pairs']==[(23,25)]
    pairs=list(zip(control['d'][::2],control['d'][1::2]))
    forced_loads=sorted({sum(v) for v in product(*pairs)})
    assert forced_loads==[9,10,14,15] and all(not 11<=v<=13 for v in forced_loads)
    residual_witness=validation.validate(28,control['d'],25,23,[0,2,11,13],[1,5,9,12],0,True)
    assert residual_witness['positions']==[0,25,17,9,3,26,22,4]
    dominant_profile=next(v for v in records if v['d']==(1,1,2,2,3,11))
    assert 'MI197_SKETCH_dominant' in dominant_profile['admissions']
    dominant_witness=mixed_dominant_witness()
    admitted_questions=sum(v['questions'] for v in records if v['admissions'])
    proved_questions=sum(v['questions'] for v in records if v['proved_admitted'])
    assert admitted_questions+sum(v['questions'] for v in residual)==questions
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<5 and rss<128*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='a28f88f0',
                         scope='M28,N1..6,d1..11,K14..24,capacity13/13; no existence solver',
                         all_input_profiles=all_profiles,eligible_profiles=len(records),questions=questions,
                         independent_profiles=len(independent),independent_questions=independent_questions,
                         admitted_profiles=len(records)-len(residual),admitted_questions=admitted_questions,
                         proved_only_questions=proved_questions,residual_profiles=len(residual),
                         residual_questions=sum(v['questions'] for v in residual),
                         tag_profiles=tag_profiles,tag_questions=tag_questions,questions_byN=byN,
                         residual_questions_byN=residualN,residual_questions_byK=residualK,
                         old_MI180_questions=sum(v['questions'] for v in records if v['old_MI180_admitted']),
                         records=records,residual=residual,
                         residual_positive_control=dict(forced_sorted_pair_loads=forced_loads,witness=residual_witness),
                         mixed_dominant_control=dominant_witness,E28_partitions=2,
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
