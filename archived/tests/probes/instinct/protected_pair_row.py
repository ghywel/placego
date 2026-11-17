#!/usr/bin/env python3
"""B238/MI454 preregistered H2 diagnostic: counts233/234, every internal hole.
Independent full maps: bin subsets and token owners. First negative stops.
20 seconds/1M owner nodes per domain; 60 seconds overall. No expansion.
"""
import itertools as it
import json
import math
import time

START = time.monotonic()

def combinations_map(pool, counts, start):
    out = {}
    leaves = 0
    for a in it.combinations(pool, counts[0]):
        rest = tuple(x for x in pool if x not in a)
        for b in it.combinations(rest, counts[1]):
            c = tuple(x for x in rest if x not in b)
            assert tuple(sorted(a+b+c)) == pool
            assert tuple(map(len,(a,b,c))) == counts
            out.setdefault(tuple(map(sum,(a,b,c))), (a,b,c))
            leaves += 1
        assert time.monotonic()-start < 20, 'combination cap'
    assert leaves == math.factorial(len(pool))//math.prod(math.factorial(c) for c in counts)
    return out, leaves


def owner_map(pool, counts, start):
    targets = set()
    rem = list(counts)
    sums = [0,0,0]
    nodes = leaves = 0
    def visit(pos):
        nonlocal nodes, leaves
        nodes += 1
        assert nodes <= 1000000, 'owner node cap'
        if nodes % 1000 == 0:
            assert time.monotonic()-start < 20, 'owner time cap'
        if pos == len(pool):
            assert rem == [0,0,0]
            leaves += 1
            targets.add(tuple(sums))
            return
        for j in range(3):
            if rem[j]:
                rem[j] -= 1
                sums[j] += pool[pos]
                visit(pos+1)
                sums[j] -= pool[pos]
                rem[j] += 1
    visit(0)
    return targets, nodes, leaves


def protected(v, counts):
    return all(sum(v[j] for j in range(3) if mask>>j&1) >=
               (r := sum(counts[j] for j in range(3) if mask>>j&1))*(r+1)//2
               for mask in range(1,7))


def run(counts, q, negative=False):
    start=time.monotonic()
    m=sum(counts)
    pool=tuple(x for x in range(m+1) if x != q)
    physical, leaves=combinations_map(pool,counts,start)
    independent,nodes,other_leaves=owner_map(pool,counts,start)
    assert set(physical)==independent and leaves==other_leaves
    reflected_pool=tuple(x for x in range(m+1) if x != m-q)
    reflected,_=combinations_map(reflected_pool,counts,start)
    assert {tuple(c*m-v for c,v in zip(counts,t)) for t in physical}==set(reflected)
    total=sum(pool)
    admitted=set()
    for a in range(total+1):
        for b in range(total-a+1):
            v=(a,b,total-a-b)
            if protected(v,counts): admitted.add(v)
    if negative:
        v=(2,6,8)
        assert all(any(sum(s)==v[j] for s in it.combinations(pool,counts[j])) for j in range(3))
        for mask in range(1,7):
            r=sum(counts[j] for j in range(3) if mask>>j&1)
            val=sum(v[j] for j in range(3) if mask>>j&1)
            assert sum(pool[:r]) <= val <= sum(pool[-r:])
        assert v not in physical
    if counts==(2,3,3) and q==4:
        assert (4,8,20) in physical
    if counts==(2,3,3) and q==1:
        assert protected((14,9,12),counts) and (14,9,12) in physical
        assert not protected((2,15,12),counts) and (2,15,12) in reflected
    missing=sorted(admitted-set(physical))
    assert time.monotonic()-start < 20 and time.monotonic()-START < 60, 'total cap'
    return dict(counts=counts,hole=q,partitions=leaves,owner_nodes=nodes,
                physical=len(physical),admitted=len(admitted),missing=len(missing),
                first_missing=missing[:1],seconds=time.monotonic()-start,
                controls='whole independent maps, count, coverage, reflection PASS')

if __name__=='__main__':
    print(json.dumps(dict(negative_control=run((2,2,2),5,True)),sort_keys=True),flush=True)
    for counts in ((2,3,3),(2,3,4)):
        for q in range(1,sum(counts)):
            result=run(counts,q)
            print(json.dumps(result,sort_keys=True),flush=True)
            if result['missing']:
                print(json.dumps({'stop':'first H2 negative'}),flush=True)
                raise SystemExit(0)
