#!/usr/bin/env python3
"""B73/MI167 prereg59aa9e29: parametric even-pool balanced parity bridge.

9408 prescribed matrix fixtures, two named E28 fixtures,2002 greedy grouping
checks against32 subsets;10CPU sec/128MiB. No role/order/anchor search, random
sample or inferred full-domain coverage. General hand proof remains SKETCH.
OUTCOME:9408 matrix fixtures and two named E28 examples pass dual validators;
2002 groupings agree with subset reference. Asymmetric/corruption controls pass.
0.956523CPU sec,41308160bytes RSS. Raw SHA256
9decbd5ddbf4881aaefdb9fbd74514d44144848336ff9dc69601108420a3ade0.
"""
from collections import Counter
from itertools import combinations
import json
import resource
import time

import path_forest_odd_bridge_family as prior
import path_forest_split_anchor_pilot as pilot


def literal_geometry(M,R,xs):
    return (all(0<=v<M for v in xs) and len(set(xs))==len(xs)
            and all(u+v!=M-1 for i,u in enumerate(xs) for v in xs[i+1:])
            and all(min(v,M-1-v) not in R for v in xs))


def literal_ok(M,bins,t,h):
    return (len(bins)==8 and sorted(v for b in bins for v in b)==list(range(1,2*M,2))
            and [sum(b) for b in bins]==list(t)
            and [len(b) for b in bins]==[2*s+v%2 for s,v in zip(h,t)])


def independent_ok(M,bins,t):
    if len(bins)!=8:return False
    unused=(1<<M)-1
    for target,values in zip(t,bins):
        if len(values)%2!=target%2:return False
        residual=target
        for value in values:
            if type(value) is not int or value<1 or value>=2*M or value%2==0:return False
            bit=1<<((value-1)//2)
            if not unused&bit:return False
            unused^=bit;residual-=value
        if residual:return False
    return unused==0


def materialize(M,R,a,h,e,selected,t):
    q=sum(v%2 for v in t)
    assert {v for v in a if v}=={v for r in R for v in (2*r+1,2*M-1-2*r)}
    assert len(R)==q//2 and sum(h)==(M-q)//2 and min(h)>=1
    assert set(selected)=={i for i,v in enumerate(e) if v}
    assert literal_geometry(M,R,list(selected.values()))
    ends={i:x+e[i] for i,x in selected.items()}
    assert Counter(ends.values())==Counter(selected.values())
    bins=[{v} if v else set() for v in a]
    labels={min(x,M-1-x) for x in selected.values()}
    for i,x in selected.items():bins[i].update((2*x+1,2*M-1-2*x))
    free=iter(r for r in range(M//2) if r not in R and r not in labels)
    for i in range(8):
        while len(bins[i])<2*h[i]+bool(a[i]):
            r=next(free);bins[i].update((2*r+1,2*M-1-2*r))
    assert next(free,None) is None
    for i,x in selected.items():bins[i].remove(2*x+1)
    for i,x in ends.items():bins[i].add(2*x+1)
    bins=[sorted(b) for b in bins]
    assert literal_ok(M,bins,t,h) and independent_ok(M,bins,t)
    if M==28:
        assert bins==pilot.materialize(t,R,a,h,selected)
        assert pilot.literal_ok(bins,t,h) and pilot.independent_ok(bins,t)
    return bins


def balance(c):
    m=max(c);j=c.index(m);A=[];B=[];left=right=0
    for i,v in enumerate(c):
        if i==j:continue
        if left<=right:A.append(i);left+=v
        else:B.append(i);right+=v
        assert abs(left-right)<=m
    if left<right:A,B=B,A;left,right=right,left
    S=sum(c)
    assert left<=S//2
    if S%2==0:assert right<=S//2-1
    return j,A,B,left,right


def construct(M,k,R,a,g,P,c):
    n=M//2;S=n-k
    assert M>0 and M%2==0 and 3<=k<n and k%2==1
    q=sum(bool(v) for v in a)
    assert len(a)==len(g)==8 and q%2==0 and len(R)==q//2
    assert set(R)<=set(range(S+1,n-1))
    assert min(g)>=1 and sum(g)==(M-q)//2-1
    assert len(P)==2 and len(set(P))==2 and set(P)<=set(range(8))
    other=[i for i in range(8) if i not in P]
    assert len(c)==6 and min(c)>=0 and sum(c)==S
    j,A,B,L,H=balance(c);negative=other[j]
    before=[other[i] for i in A if c[i]];after=[other[i] for i in B if c[i]]
    cv=dict(zip(other,c));z=n-1 if n%2==0 else n
    root=z-k-2*L;positions=[root]
    owners=(*before,*P,*after,negative)
    for i in owners[:-1]:positions.append(positions[-1]+(k if i in P else 2*cv[i]))
    selected=dict(zip(owners,positions));h=list(g);h[negative]+=1
    t=[2*M*g[i]+a[i]+(2*k if i in P else 4*cv[i]) for i in range(8)]
    e=[(v-2*M*s-anchor)//2 for v,s,anchor in zip(t,h,a)]
    assert sum(t)==M*M and sum(e)==0 and e[negative]==2*c[j]-M<0
    assert positions[-1]-root==M-2*c[j]
    assert 0<=root and positions[-1]<=M-2 and z%2==1
    assert sum(x%2 for x in positions)==1 and z in positions
    assert all(min(x,M-1-x)<=S or min(x,M-1-x)==n-1 for x in positions)
    assert literal_geometry(M,R,positions)
    bins=materialize(M,R,a,h,e,selected,t)
    return dict(M=M,k=k,reserved=sorted(R),anchors=a,base_slots=g,bridge_owners=P,
                parameters=c,targets=t,slots=h,moves=e,selected=selected,bins=bins,
                group_loads=(L,H),root=root,centre=z)


def anchors(M,R,q):
    return sorted(v for r in R for v in (2*r+1,2*M-1-2*r))+[0]*(8-q)


def grouping_audit():
    count=0
    for c in prior.compositions(9,6):
        j,A,B,L,H=balance(c);rest=[i for i in range(6) if i!=j]
        masks=[mask for mask in range(32)
               if sum(c[i] for b,i in enumerate(rest) if mask>>b&1)<=4
               and sum(c[i] for b,i in enumerate(rest) if not(mask>>b&1))<=4]
        chosen=sum(1<<rest.index(i) for i in A)
        assert chosen in masks and L<=4 and H<=4
        count+=1
    assert count==2002
    return count


def main():
    start=time.process_time();rows=[];regimes=0;byM=Counter()
    for M in (24,26,28,30,32):
        n=M//2
        for q in (0,2,4,6,8):
            extra=(M-q)//2-1-8
            if extra<0:continue
            admissible=[k for k in range(3,n,2) if k>=q//2+2]
            for k in (admissible[0],admissible[-1]):
                regimes+=1;S=n-k;R=set(range(S+1,S+1+q//2));a=anchors(M,R,q)
                g=[1]*8
                for i in range(7,7-extra,-1):g[i]+=1
                for P in combinations(range(8),2):
                    cs=[tuple(S if i==j else 0 for i in range(6)) for j in range(6)]
                    quotient,remainder=divmod(S,6)
                    cs.append(tuple(quotient+(i<remainder) for i in range(6)))
                    for c in cs:
                        rows.append(construct(M,k,R,a,g,P,c));byM[M]+=1
                        assert time.process_time()-start<10
                        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<128*1024*1024
    assert regimes==48 and len(rows)==9408
    grouping_count=grouping_audit()
    a=[21,23,25,31,33,35,0,0];g=[1]*6+[2,2]
    first=construct(28,5,{10,11,12},a,g,(3,4),(2,2,2,1,1,1))
    assert first['targets']==[85,87,89,97,99,95,116,116]
    second=construct(28,11,{4,5,6,7},[9,11,13,15,41,43,45,47],[2,1,1,1,1,1,1,1],
                     (1,2),(0,1,1,1,0,0))
    assert second['targets']==[121,89,91,75,101,103,101,103]
    assert all(68<=v<=122 for r in (first,second) for v in r['targets'])
    assert sum(v%2 for v in first['targets'])==6 and all(v%2 for v in second['targets'])
    correct=construct(26,11,set(),[0]*8,[1,1,1,1,2,2,2,2],(0,1),(1,1,0,0,0,0))
    assert list(correct['selected'].values())==[0,2,13,24]
    bad_positions=[2,13,24,26]
    assert not literal_geometry(26,set(),bad_positions)
    bins=first['bins'];t=first['targets'];h=first['slots']
    bad=[list(b) for b in bins];bad[0][0]=bad[1][0]
    assert not literal_ok(28,bad,t,h) and not independent_ok(28,bad,t)
    bad=[list(b) for b in bins];bad[0][0],bad[1][0]=bad[1][0],bad[0][0]
    assert sorted(v for b in bad for v in b)==list(range(1,56,2))
    assert not literal_ok(28,bad,t,h) and not independent_ok(28,bad,t)
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<10 and rss<128*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='59aa9e29',
                         fixture_evaluations=len(rows),regimes=regimes,by_M=dict(byM),
                         greedy_grouping_checks=grouping_count,named_E28=[first,second],
                         asymmetric_control=correct,reversed_geometry_rejected=bad_positions,
                         corruption_controls='PASS',rows=rows,cpu_seconds=elapsed,
                         peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
