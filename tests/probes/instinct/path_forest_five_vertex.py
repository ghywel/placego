#!/usr/bin/env python3
"""B88/MI199 prereg229dd244: H5 five-vertex iff diagnostic, n5..12.

Max40000 questions,10CPU sec/128MiB; stop first disagreement, no repair.
Independent physical-permutation existence n5..7; full witness checks.
Three negative controls and largest-alone/max-first shortcut counterfactual.
No M28 census, E28 partition or infinite proof status upgrade.
Run1 stopped on an over-specific expected control root (MI199 addendum).
Run2 passes1843 questions/112 independent comparisons,1747 accepted/96
rejected,3 refusals and opposite-owner controls;0.059006CPU sec,13168640RSS.
Artifact SHA2562797a5844c1b228c00365fa938a25f99757c135afc4e2a5388fc874a52c69b9c.
MI201's infinite hand argument is separate and remains PROOF-SKETCH.
"""
from collections import Counter
from itertools import combinations_with_replacement, permutations
import json
import resource
import time


def physical(n,A,B):
    M=2*n
    return [2*A[0]]+[M-1-2*b for b in B]+[2*a for a in reversed(A[1:])]


def literal(n,xs,bag):
    return (len(xs)==5 and all(0<=x<2*n for x in xs)
            and len({min(x,2*n-1-x) for x in xs})==5
            and Counter(v-u for u,v in zip(xs,xs[1:]+xs[:1]))==Counter(bag))


def chains(n,d,p,q,largest_only=False,max_first=False):
    h=n-1
    for P,Q in ((max(p,q),min(p,q)),) if max_first else ((p,q),(q,p)):
        alpha=(2*h+1-P)//2
        arrangements=[]
        if not largest_only:
            arrangements += [((),order) for order in sorted(set(permutations(d)))]
        for D,E,F in sorted(set(permutations(d))):
            if largest_only and D!=max(d):continue
            arrangements.append(((D,),(E,F)))
        for agaps,bgaps in arrangements:
            DA,DB=sum(agaps),sum(bgaps)
            lo=max(0,alpha+DB-h);hi=min(alpha,h-DA)
            for t in range(lo,hi+1):
                A=[t];B=[alpha-t]
                for v in agaps:A.append(A[-1]+v)
                for v in bgaps:B.append(B[-1]+v)
                if set(A)&set(B):continue
                xs=physical(n,A,B)
                assert literal(n,xs,(p,q,*(-2*v for v in d)))
                return dict(first=P,A=A,B=B,positions=xs)
    return None


def direct(n,d,p,q):
    # Fix one positive edge first by cyclic rotation; try all remaining orders.
    for tail in sorted(set(permutations((q,*(-2*v for v in d))))):
        word=(p,)+tail;xs=[0]
        for v in word[:-1]:xs.append(xs[-1]+v)
        if len(set(xs))!=5:continue
        lo=-min(xs);hi=2*n-1-max(xs)
        for root in range(lo,hi+1):
            translated=[v+root for v in xs]
            if len({min(v,2*n-1-v) for v in translated})==5:
                assert literal(n,translated,word)
                return translated
    return None


def criterion(n,d,p,q):
    a,b,c=sorted(d);h=n-1
    return (n>=5 and max(p,q)<=2*h-1 and (p,q)!=(2*h-1,2*h-1)
            and c<=h and a+b<=h)


def main():
    start=time.process_time();rows=[];by_n=Counter();independent=0
    for n in range(5,13):
        h=n-1
        for d in combinations_with_replacement(range(1,h+1),3):
            K=sum(d)
            if K>2*h-1:continue
            for p in range(max(1,2*K-(2*h-1)),K+1,2):
                q=2*K-p
                assert p%2 and q%2 and p<=q<=2*h-1
                row=chains(n,d,p,q);expected=criterion(n,d,p,q)
                if n<=7:
                    oracle=direct(n,d,p,q);independent+=1
                    assert bool(row)==bool(oracle),(n,d,p,q,'independent disagreement')
                if bool(row)!=expected:
                    print(json.dumps(dict(status='FIRST_H5_DISAGREEMENT',n=n,d=d,p=p,q=q,
                                          expected=expected,witness=row,questions_before=len(rows),
                                          independent_checks=independent,cpu_seconds=time.process_time()-start)))
                    return
                rows.append(dict(n=n,d=d,p=p,q=q,criterion=expected,witness=row));by_n[n]+=1
                assert len(rows)<=40000 and time.process_time()-start<10
    controls=[]
    for n,d,p,q in ((14,(8,8,8),23,25),(6,(1,4,4),9,9),(4,(1,1,2),3,5)):
        assert not criterion(n,d,p,q) and chains(n,d,p,q) is None and direct(n,d,p,q) is None
        controls.append(dict(n=n,d=d,p=p,q=q,refused=True))
    assert chains(10,(4,4,6),15,13,True,True) is None
    opposite=chains(10,(4,4,6),15,13,True)
    assert opposite and opposite['first']==13
    assert literal(10,opposite['positions'],(15,13,-8,-8,-12))
    assert literal(10,physical(10,[3,9],[0,4,8]),(15,13,-8,-8,-12))
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<10 and rss<128*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='229dd244',
                         questions=len(rows),questions_by_n=by_n,independent_checks=independent,
                         accepted=sum(v['criterion'] for v in rows),rejected=sum(not v['criterion'] for v in rows),
                         controls=controls,shortcut_fails=True,opposite_owner=opposite,rows=rows,
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
