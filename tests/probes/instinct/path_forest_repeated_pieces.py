#!/usr/bin/env python3
"""B58/MI137 preregistered eeb2b7a6: repeated two-valued zero-sum pieces.

All +a/-b words with <=8 moves and a+b<=28: normalize primitive
nyctalopic vertices to an arithmetic progression, then place copies by
residue orbits or folded gap-path matching. No arbitrary placement search.
Predict every instance succeeds and the E28 corollary has33 targets with
q-counts4,9,4,7,3,6. Independent multiplicity domain, complete unique word
geometry, physical/formula gap graphs and matching controls; two literal
partition checkers. Counterfactual roots0/1 at k4,g5 and pool8 gap3 twice
must fail. Unexpected reflection plus sign reversal preserves certificates.
Caps1000 instances/100000 reference words/fiveCPU seconds; stop on failure,
no repairs or enlargement. Raw outside git. REFUTED-BY: any formula,
domain, geometry, forest, certificate or control failure. Hand SKETCH.
OUTCOME: all184 parameter instances pass prescribed placements; independent
multiplicity domain agrees.1224 reference words,220 nyctalopic words, all
normalized vertex sets agree. All14 folded graphs are forests of paths
with the stated edge counts and matching size>=4.33 exact E28 partitions,
q-counts4,9,4,7,3,6, both literal checkers and controls pass. CPU0.015507s.
Full immutable output SHA256
aceee1a5b4ea58787582c8e5794f86cedadbe2fbbdc88368f438555292d4afbd.
Finite validation COMPUTED; uniform hand argument unreviewed SKETCH;
no assertion for mixed primitive pieces, full even E28 or L8.
"""
from collections import Counter
from itertools import combinations
from math import gcd
import json
import time

from path_forest_cycle_cover import materialize,setup
from path_forest_receiving_chains import certificate_ok
from path_forest_three_surplus_audit import bitset_ok


def label(x,N=28):return min(x,N-1-x)


def gap_graph(g,N=28):
    E={tuple(sorted((label(x,N),label(x+g,N)))) for x in range(N-g)
       if label(x,N)!=label(x+g,N)}
    return E


def path_matching(g):
    E=gap_graph(g);adj={i:set() for i in range(14)}
    for x,y in E:adj[x].add(y);adj[y].add(x)
    assert max(map(len,adj.values()))<=2
    unseen=set(range(14));paths=[];chosen=[]
    while unseen:
        endpoint=min(i for i in unseen if len(adj[i])<=1)
        path=[];previous=None;current=endpoint
        while current in unseen:
            unseen.remove(current);path.append(current)
            nxt=adj[current]-{previous}
            if not nxt:break
            assert len(nxt)==1
            previous,current=current,next(iter(nxt))
        paths.append(path)
        chosen.extend(tuple(sorted((path[j],path[j+1]))) for j in range(0,len(path)-1,2))
    assert len(E)==14-len(paths)==14-(g+1)//2
    assert len(chosen)>=4
    assert len(set(i for edge in chosen for i in edge))==2*len(chosen)
    return chosen,paths


def progression_roots(g,k,r):
    assert k*r<=8 and g*k<=28 and k>=2
    if r==1:
        if g==1 or g%2==0:return [0]
        return [next(c for c in range(g) if (2*c-27)%g)]
    if r==2:
        if g==1:return [0,k]
        if g<=3:return [0,1]
        # One representative per nonfixed orbit of reflection modulo g.
        orbits=sorted({tuple(sorted((c,(27-c)%g))) for c in range(g)
                       if c!=(27-c)%g})
        assert len(orbits)>=2
        return [orbits[0][0],orbits[1][0]]
    assert r in (3,4) and k==2
    matching,_=path_matching(g);roots=[]
    for edge in matching[:r]:
        roots.append(next(x for x in range(28-g)
                          if tuple(sorted((label(x),label(x+g))))==edge))
    return roots


def primitive_word(a,b):
    g=gcd(a,b);k=(a+b)//g;s=0;word=[];points=[]
    for _ in range(k):
        points.append(s);x=a if s<=0 else -b;word.append(x);s+=x
    assert s==0 and Counter(word)=={a:b//g,-b:a//g}
    normalized=tuple(x-min(points) for x in points)
    assert sorted(normalized)==list(range(0,k*g,g))
    return word,normalized


def geometry_ok(e,selected,N=28):
    if set(selected)!=set(range(len(e))):return False
    xs=list(selected.values())
    if any(not 0<=x<N for x in xs):return False
    if len({label(x,N) for x in xs})!=len(xs):return False
    return sorted(selected[i]+e[i] for i in selected)==sorted(xs)


def construct(a,b,r):
    g=gcd(a,b);k=(a+b)//g;p=r*(b//g);q=r*(a//g)
    word,points=primitive_word(a,b);roots=progression_roots(g,k,r)
    selected={};positive=0;negative=p
    for root in roots:
        for x,point in zip(word,points):
            if x>0:i=positive;positive+=1
            else:i=negative;negative+=1
            selected[i]=root+point
    e=[a]*p+[-b]*q
    assert geometry_ok(e,selected)
    return dict(a=a,b=b,r=r,g=g,k=k,p=p,q=q,roots=roots,selected=selected)


def reference_geometry(a,b):
    g=gcd(a,b);p=b//g;q=a//g;k=p+q;checked=0;accepted=0
    for positions in combinations(range(k),p):
        positive=set(positions);word=[a if i in positive else -b for i in range(k)]
        checked+=1;s=0;points=[];valid=True
        for i,x in enumerate(word):
            if i and s*x>=0:valid=False;break
            points.append(s);s+=x
        if valid:
            assert s==0 and len(set(points))==k
            assert sorted(x-min(points) for x in points)==list(range(0,k*g,g))
            accepted+=1
    assert accepted==2
    return checked,accepted


def graph_controls():
    rows=[]
    for g in range(1,15):
        physical=gap_graph(g)
        formula={(i,j) for i in range(14) for j in range(i+1,14)
                 if j-i==g or i+j==27-g}
        assert physical==formula
        matching,paths=path_matching(g)
        assert set(edge for path in paths for edge in
                   (tuple(sorted((x,y))) for x,y in zip(path,path[1:])))==physical
        rows.append(dict(g=g,edges=len(physical),paths=paths,matching=matching))
    bad=[0,5,10,15,1,6,11,16]
    assert len(set(bad))==8 and len({label(x) for x in bad})<8
    E=gap_graph(3,8)
    maxmatch=max(len(c) for n in range(len(E)+1) for c in combinations(E,n)
                 if len({v for edge in c for v in edge})==2*n)
    assert maxmatch==1 and len(E)==2
    return rows


def e28_corollary(results):
    table={(row['a'],row['b'],row['p'],row['q']):row for row in results}
    rows=[];counts=Counter()
    for q in range(1,7):
        for a in range(6,28):
            for b in range(1,23):
                if 2*a!=q*b or a+b>28:continue
                t=(56+2*a,)*2+(112-2*b,)*q+(112,)*(6-q)
                assert tuple(sorted(t))==t and sum(t)==784
                row=table[a,b,2,q]
                w=materialize(t,row['selected'])
                assert certificate_ok(w['bins'],t) and bitset_ok(w['bins'],t)
                counts[q]+=1;rows.append(dict(targets=t,bins=w['bins'],q=q,a=a,b=b))
    direct=set()
    for low in range(68,111,2):
        for high in range(low,111,2):
            for q in range(1,7):
                t=(low,low)+(high,)*q+(112,)*(6-q)
                if sum(t)==784:direct.add(t)
    assert {tuple(r['targets']) for r in rows}==direct and len(direct)==33
    assert [counts[q] for q in range(1,7)]==[4,9,4,7,3,6]
    t=rows[0]['targets'];bins=[set(x) for x in rows[0]['bins']]
    x,y=min(bins[0]),min(bins[2]);bins[0].remove(x);bins[2].remove(y)
    bins[0].add(y);bins[2].add(x)
    assert sorted(v for bucket in bins for v in bucket)==list(range(1,56,2))
    assert not certificate_ok(bins,t) and not bitset_ok(bins,t)
    return rows,dict(counts)


def main():
    start=time.process_time();graphs=graph_controls();rows=[];words=0;accepted=0
    for a in range(1,28):
        for b in range(1,29-a):
            g=gcd(a,b);k=(a+b)//g
            if k>8:continue
            w,z=reference_geometry(a,b);words+=w;accepted+=z
            for r in range(1,8//k+1):
                assert len(rows)<1000 and words<=100000 and time.process_time()-start<5
                row=construct(a,b,r);p,q=row['p'],row['q']
                # Independent sign-reversal bijection: reflect physical points,
                # then relabel the old negative owners as the new positives.
                reverse={i-p if i>=p else q+i:27-x for i,x in row['selected'].items()}
                assert geometry_ok([b]*q+[-a]*p,reverse)
                rows.append(row)
    direct={(a,b,p,q) for p in range(1,8) for q in range(1,9-p)
            for a in range(1,28) for b in range(1,29-a) if p*a==q*b}
    assert {(r['a'],r['b'],r['p'],r['q']) for r in rows}==direct
    corollary,counts=e28_corollary(rows)
    assert time.process_time()-start<5
    print(json.dumps(dict(status='ALL_PRESCRIBED_CONSTRUCTIONS_PASS',parameters=len(rows),
        reference_words=words,nyctalopic_words=accepted,graphs=graphs,results=rows,
        e28_targets=corollary,e28_counts_by_q=counts,controls='PASS',
        cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
