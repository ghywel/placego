#!/usr/bin/env python3
"""B205 / MI400: one protected two-hole target; deterministic count feedback.

RUN-ON: CPU, Python standard library. COST: <5 CPU seconds; hard check.
COMMAND: python3 tests/probes/instinct_two_hole_feedback.py
Predictions registered in MI400 before execution. Blind: nontrivial cycles
occur despite actual feasibility. Independent subset-sum physical catalogue,
all 1680 rank partitions, and incompatible size2 one-hole countercontrol.
Unexpected check: relabel the same physical target. No random selection.
Output is JSON; retain raw output outside git. This tests a solver policy,
not universal existence or a new theorem. Outcome recorded in MI401.
"""
import itertools as it
import json
import time

START = time.process_time()
def guard():
    assert time.process_time() - START < 5, '5 CPU second cap'

def partitions(n, sizes):
    universe = tuple(range(n))
    for a in it.combinations(universe, sizes[0]):
        left = tuple(x for x in universe if x not in a)
        for b in it.combinations(left, sizes[1]):
            c = tuple(x for x in left if x not in b)
            assert len(c) == sizes[2]
            yield a,b,c

def independent(pool, sizes, targets):
    choices = [[c for c in it.combinations(pool,s) if sum(c)==u]
               for s,u in zip(sizes,targets)]
    out=set()
    for a in choices[0]:
        for b in choices[1]:
            if set(a).isdisjoint(b):
                c=tuple(x for x in pool if x not in a and x not in b)
                if len(c)==sizes[2] and sum(c)==targets[2]:
                    out.add((a,b,c))
    return out

def solve(target):
    n=9;p=3;q=6;sizes=(3,3,3)
    pool=tuple(x for x in range(n+2) if x not in (p,q))
    parts=tuple(partitions(n,sizes))
    assert len(parts)==1680 and len(set(parts))==1680
    assert all(sorted(sum(x,()))==list(range(n)) for x in parts)
    first={}
    for part in parts:
        first.setdefault(tuple(map(sum,part)),part)
    row=tuple((k,l) for k in range(4) for l in range(k+1))
    states=tuple(x for x in it.product(row,repeat=3)
                 if sum(k for k,l in x)==n-p and sum(l for k,l in x)==n-q+1)
    state_set=set(states); F={}; witnesses={}
    for x in states:
        w=tuple(u-k-l for u,(k,l) in zip(target,x))
        assert w in first, ('compressed infeasible',x,w)
        part=first[w]
        y=tuple((sum(j>=p for j in block),sum(j>=q-1 for j in block)) for block in part)
        assert y in state_set
        F[x]=y
        if x==y:
            physical=tuple(tuple(pool[j] for j in block) for block in part)
            assert tuple(map(sum,physical))==target
            witnesses[x]=physical
    cycles=set(); basin={}
    for x in states:
        seen={}; path=[]; z=x
        while z not in seen:
            seen[z]=len(path);path.append(z);z=F[z]
        cyc=tuple(path[seen[z]:]);cyc=min(cyc[i:]+cyc[:i] for i in range(len(cyc)))
        cycles.add(cyc);basin[cyc]=basin.get(cyc,0)+1
    mapped={tuple(tuple(pool[j] for j in block) for block in part) for part in parts
            if tuple(sum(pool[j] for j in block) for block in part)==target}
    oracle=independent(pool,sizes,target)
    assert mapped==oracle and oracle
    assert all(w in oracle for w in witnesses.values())
    guard()
    return {'target':target,'states':len(states),'literal_partitions':len(oracle),
            'fixed_points':len(witnesses),'cycles':[
              {'length':len(c),'basin':basin[c],'states':c} for c in sorted(cycles)],
            'witness':next(iter(witnesses.values()),None)}

results=[solve((15,15,16)),solve((15,16,15))]
assert results[0]['literal_partitions']==results[1]['literal_partitions']
toy_pool=(0,1,2,3,4,6);toy_target=(2,6,8)
assert not independent(toy_pool,(2,2,2),toy_target)
toy_parts=tuple(partitions(6,(2,2,2)))
for owner in range(3):
    w=tuple(u-(i==owner) for i,u in enumerate(toy_target))
    eligible=[part for part in toy_parts if tuple(map(sum,part))==w]
    assert eligible and not any(5 in part[owner] for part in eligible)
guard()
print(json.dumps({'results':results,'controls':'passed','toy_compressed_queries':3,
                  'toy_physical_partitions':0,'cpu_seconds':time.process_time()-START},indent=2))
