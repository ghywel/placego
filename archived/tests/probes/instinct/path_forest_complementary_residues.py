#!/usr/bin/env python3
"""B78/MI177 preregd0428cf3: two exceptional half-residues; root and order.

Exactly216 tight formula geometries, three E28 partitions, g2 and atomic-split
scope controls;2CPU sec/64MiB. No geometry search, repair or expanded grid.
General sufficient statement remains SKETCH; no new carrying-read queue.
OUTCOME:216 tight geometries pass (108 second roots,36 swaps,160 actual gcd1),
three E28 partitions and all controls pass.0.009510CPU sec,15638528bytes RSS.
Raw SHA256 44aa07289ff083320cddecd5f0e1faf2d6cabd84e2d970f9540e81ab5caa3556.
"""
from itertools import product
from math import gcd
import json
import resource
import time

import path_forest_balanced_bridge as instrument


def word_points(p,q,d,A,B,h):
    owners=[0]+[i+2 for i in A]+[1]+[i+2 for i in B]
    word=[p]+[-2*d[i] for i in A]+[q]+[-2*d[i] for i in B]
    xs=[h]
    for e in word:xs.append(xs[-1]+e)
    assert xs[-1]==h
    return owners,word,xs[:-1]


def independent_geometry(M,xs):
    if not all(0<=x<M for x in xs):return False
    if len(xs)!=len(set(xs)):return False
    return len({min(x,M-1-x) for x in xs})==len(xs)


def construct(M,p,q,d,g,A,B,partition=False):
    assert g>=3 and M%2==0 and p>0 and q>0 and p%2 and q%2
    assert p+q==2*sum(d) and min(d)>0 and max(p,q)<=M-3
    assert sorted(A+B)==list(range(len(d)))
    exceptional=[i for i,v in enumerate(d) if v%g]
    assert len(exceptional)==2 and all(i in A for i in exceptional)
    assert sum(d[i] for i in exceptional)%g==0
    slots=[A.index(i) for i in exceptional]
    original=list(A);reverse=list(A)
    reverse[slots[0]],reverse[slots[1]]=reverse[slots[1]],reverse[slots[0]]
    orders=[original,reverse]
    s=sum(d[i] for i in A);t=sum(d[i] for i in B);w=p-2*s
    assert s<=M//2-1 and t<=M//2-1
    L=max(0,-w);R=min(M-1-p,M-1-2*t);H=(M-1-p)//2
    assert R>=L+1
    choice=None;checks=[]
    for root,orientation in product((L,L+1),(0,1)):
        order=orders[orientation]
        first=next(i for i in order if i in exceptional);r=d[first]%g
        good=(root-H)%g not in (0,r)
        checks.append((root,orientation,r,good))
        if good and choice is None:choice=(root,orientation,order)
    assert choice is not None
    root,orientation,order=choice
    owners,word,xs=word_points(p,q,d,order,B,root)
    assert independent_geometry(M,xs) and instrument.literal_geometry(M,set(),xs)
    # The geometry check uses actual integers, not the residue predicate.
    cross_sums=sorted({x+y for x in xs for y in xs if x%2==0 and y%2==1})
    assert M-1 not in cross_sums
    selected=dict(zip(owners,xs));targets=None;bins=None
    if partition:
        assert M==28 and len(d)==6
        e=[p,q]+[-2*v for v in d];h=[1,1]+[2]*6
        targets=[56*a+2*b for a,b in zip(h,e)]
        assert all(68<=v<=122 for v in targets) and sum(targets)==784
        bins=instrument.materialize(M,set(),[0]*8,h,e,selected,targets)
        assert instrument.literal_ok(M,bins,targets,h)
        assert instrument.independent_ok(M,bins,targets)
    return dict(M=M,p=p,q=q,d=d,g=g,actual_gcd=gcd(*d),A=order,B=B,
                loads=(s,t),root_interval=(L,R),root=root,orientation=orientation,
                residue_checks=checks,positions=xs,owners=owners,word=word,
                cross_sums=cross_sums,targets=targets,bins=bins)


def main():
    start=time.process_time();rows=[]
    for g in range(3,12):
        for a in range(1,g):
            d=(a,g-a,g,g,g,g)
            for p,q in ((4*g+1,6*g-1),(6*g-1,4*g+1)):
                for A in ([0,1,2,3],[0,2,1,3]):
                    row=construct(6*g+2,p,q,d,g,A,[4,5])
                    assert row['root_interval'][1]-row['root_interval'][0]==1
                    rows.append(row)
                    assert len(rows)<=216 and time.process_time()-start<2
                    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<64*1024*1024
    assert len(rows)==216
    second=sum(r['root']==r['root_interval'][0]+1 for r in rows)
    swapped=sum(r['orientation']==1 for r in rows)
    assert second==108 and swapped==36
    fixtures=[construct(28,p,q,(1,2,3,3,6,9),3,[0,1,5],[2,3,4],True)
              for p,q in ((25,23),(23,25))]
    fixtures.append(construct(28,21,21,(1,2,3,3,6,6),3,[0,1,2,4],[3,5],True))
    assert all(r['actual_gcd']==1 for r in fixtures)
    assert fixtures[-1]['root']==4 and fixtures[-1]['orientation']==1
    # Omitting the modulus restriction makes even the claimed existence false.
    d=(1,1,2,2,2,2);A=[0,1,2,3];B=[4,5];bad=[]
    for root,orientation in product((3,4),(0,1)):
        order=list(A)
        if orientation:order[0],order[1]=order[1],order[0]
        _,_,xs=word_points(9,11,d,order,B,root)
        assert not independent_geometry(14,xs)
        bad.append(dict(root=root,orientation=orientation,positions=xs))
    try:construct(14,9,11,d,2,A,B)
    except AssertionError:pass
    else:raise AssertionError('g2 wrongly in scope')
    # Actual reflection freedom need not require a missing modular class.
    _,_,outside=word_points(7,13,d,A,B,7)
    assert outside==[7,14,12,10,6,2,15,11]
    assert independent_geometry(16,outside) and instrument.literal_geometry(16,set(),outside)
    H=(15-7)//2
    assert all((root-H)%2 in (0,1) for root in range(5,8))
    atomic=(6,9,9);original=(2,4,9,9)
    sums=lambda seq:{sum(x for i,x in enumerate(seq) if mask>>i&1) for mask in range(1<<len(seq))}
    assert not any(11<=v<=13 for v in sums(atomic))
    assert {11,13}<=sums(original)
    elapsed=time.process_time()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed<2 and rss<64*1024*1024
    print(json.dumps(dict(status='ALL_PRESCRIBED_CHECKS_PASS',preregistration='d0428cf3',
                         tight_geometries=len(rows),second_root=second,swapped_orientation=swapped,
                         actual_gcd1=sum(r['actual_gcd']==1 for r in rows),rows=rows,
                         E28=fixtures,g2_negative=bad,outside_scope_positive=outside,
                         atomic_admission_refusal=dict(atomic=atomic,original=original,
                                                       atomic_sums=sorted(sums(atomic)),original_sums=sorted(sums(original))),
                         cpu_seconds=elapsed,peak_rss_bytes=rss),separators=(',',':')))


if __name__=='__main__':main()
