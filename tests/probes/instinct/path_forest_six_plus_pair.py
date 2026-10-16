#!/usr/bin/env python3
"""B61/MI143 prereg bb346018: six-point span20 plus a cancelling pair.

Exactly15504 shapes x14 gaps,3003 six-label free-edge tables,10 CPU seconds.
Predict >=1 failure among gaps9..11; none at1,2,7,14 (perfect matchings).
Independent pair-sum/bitmask vs literal roots/physical-edge set instruments.
Counterfactual root0 cover for(0,6,7,8,9,10),g5; unexpected root1 rescues it.
Span21 rootless and duplicate controls. No target census or alternate order.
Finite COMPUTED only; REFUTED-BY any mismatch or absent predicted failure.
OUTCOME MI144: all217056 questions PASS, all3003 tables/full15504 root
lists agree; failure forecast REFUTED. CPU1.231821s. Artifact SHA256
81544cf1c7fc931cbb3be2ed99d60131e01e07f3c36f200c1394c99b46398b00.
"""
from collections import Counter
from itertools import combinations
import json
import math
import time


class Cap(Exception):pass


def formula_edges(g):
    return [(1<<i)|(1<<j) for i in range(14) for j in range(i+1,14)
            if j-i==g or i+j==27-g]


def root_masks(s):
    if len(s)!=len(set(s)):return []
    blocked={(27-x-y)//2 for x,y in combinations(s,2) if (x+y)%2}
    return [(r,sum(1<<min(x+r,27-x-r) for x in s))
            for r in range(28-max(s)) if r not in blocked]


def reference_roots(s):
    if len(set(s))!=len(s):return []
    out=[]
    for r in range(28-max(s)):
        labels=frozenset(min(x+r,27-x-r) for x in s)
        if len(labels)==len(s):out.append((r,labels))
    return out


def main():
    start=time.process_time()
    def cap():
        if time.process_time()-start>10:raise Cap()
    physical={g:[(x,x+g,frozenset((min(x,27-x),min(x+g,27-x-g))))
                 for x in range(28-g) if min(x,27-x)!=min(x+g,27-x-g)]
              for g in range(1,15)}
    graph={g:formula_edges(g) for g in range(1,15)}
    for g in graph:
        assert set(graph[g])=={sum(1<<x for x in labs) for _,_,labs in physical[g]}
    table={};reference={};covers=Counter()
    for labels in combinations(range(14),6):
        cap();mask=sum(1<<x for x in labels);used=frozenset(labels);available=0
        refs={}
        for g in range(1,15):
            if any(not e&mask for e in graph[g]):available|=1<<(g-1)
            pair=next(((x,y) for x,y,labs in physical[g] if not used&labs),None)
            if pair is not None:refs[g]=pair
            else:covers[g]+=1
        assert available==sum(1<<(g-1) for g in refs)
        table[mask]=available;reference[used]=refs
    assert len(table)==math.comb(14,6)==3003
    assert all(covers[g]==0 for g in (1,2,7,14))
    shape=(0,6,7,8,9,10);rr=dict(reference_roots(shape))
    assert 5 not in reference[rr[0]] and 5 in reference[rr[1]]
    sharp=(0,2,6,15,19,21)
    assert root_masks(sharp)==reference_roots(sharp)==[]
    assert root_masks((0,0,1))==reference_roots((0,0,1))==[]
    rows=[];failures=[];by_span=Counter();bad_gaps=Counter()
    for other in combinations(range(1,21),5):
        cap();s=(0,)+other;a=root_masks(s);b=reference_roots(s)
        assert a and [r for r,_ in a]==[r for r,_ in b]
        assert [m for _,m in a]==[sum(1<<x for x in labs) for _,labs in b]
        feasible=0
        for _,m in a:feasible|=table[m]
        witnesses={}
        for r,labs in b:
            for g,pair in reference[labs].items():witnesses.setdefault(g,(r,pair[0]))
        assert feasible==sum(1<<(g-1) for g in witnesses)
        for g,(r,x) in witnesses.items():
            xs=[r+y for y in s]+[x,x+g]
            assert all(0<=y<=27 for y in xs)
            assert len({min(y,27-y) for y in xs})==8
        missing=[g for g in range(1,15) if g not in witnesses]
        if missing:
            roots=[]
            for r in range(28-max(s)):
                labels=[min(x+r,27-x-r) for x in s]
                if len(set(labels))<6:
                    roots.append(dict(root=r,reflection=True,labels=labels));continue
                used=set(labels)
                for g in missing:assert all(used&labs for _,_,labs in physical[g])
                roots.append(dict(root=r,reflection=False,labels=labels,covers=missing))
            failures.append(dict(shape=s,gaps=missing,all_roots=roots))
            for g in missing:bad_gaps[g]+=1
        by_span[max(s)]+=1
        rows.append(dict(shape=s,feasible_gap_mask=feasible,
                         witnesses=[witnesses.get(g) for g in range(1,15)]))
    assert len(rows)==15504 and sum(by_span.values())*14==217056
    assert all(by_span[d]==math.comb(d-1,4) for d in range(5,21))
    assert all(bad_gaps[g]==0 for g in (1,2,7,14))
    print(json.dumps(dict(status='COMPLETE_GEOMETRY',shapes=len(rows),questions=217056,
        free_gap_tables=3003,by_span=dict(by_span),cover_counts=dict(covers),
        failed_shape_count=len(failures),failed_gap_counts=dict(bad_gaps),failures=failures,
        results=rows,controls='PASS',cpu_seconds=time.process_time()-start),separators=(',',':')))


if __name__=='__main__':
    try:main()
    except Cap:print(json.dumps(dict(status='UNKNOWN_CPU_CAP')))
