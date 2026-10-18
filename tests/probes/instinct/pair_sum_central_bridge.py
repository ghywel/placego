#!/usr/bin/env python3
"""B243 / MI471: fixed order8 cut profiles containing14,15,16,17.
Independent complete domain and per-target search; physical reflection only.
20s/1M search nodes; first negative; no retry, expansion or random choice.
"""
from itertools import permutations,combinations_with_replacement
from functools import lru_cache
from math import factorial
import json,time
from pair_sum_group_capacity import profile_stream,cuts
START=time.monotonic(); NODES=0
CORE={14,15,16,17}; K=8

def guard():assert time.monotonic()-START<20,'wall cap'

def all_cuts(q):
    if sum(q)!=120:return False
    for mask in range(1,255):
        r=mask.bit_count();s=sum(x for i,x in enumerate(q) if mask>>i&1)
        if not r*(8+r-1)<=s<=r*(23-r):return False
    return True

def literal(high,q):
    assert len(high)==8 and sorted(high)==list(range(8,16))
    assert tuple(sorted(i+h for i,h in enumerate(high)))==q


def independent(q):
    # Fill target slots, unlike the primary low-row permutation enumeration.
    @lru_cache(None)
    def visit(slot,low,high):
        global NODES
        NODES+=1;assert NODES<=1000000,'search cap';guard()
        if slot==8:return ()
        t=q[slot]
        for a in range(8):
            b=t-8-a
            if not 0<=b<8 or low>>a&1 or high>>b&1:continue
            rest=visit(slot+1,low|1<<a,high|1<<b)
            if rest is not None:return ((a,8+b),)+rest
        return None
    out=visit(0,0,0)
    if out is not None:
        assert sorted(a for a,b in out)==list(range(8))
        assert sorted(b for a,b in out)==list(range(8,16))
        assert tuple(sorted(a+b for a,b in out))==q
    return out

def main():
    physical={};leaves=0
    for p in permutations(range(8,16)):
        q=tuple(sorted(i+h for i,h in enumerate(p)))
        physical.setdefault(q,p);leaves+=1
    assert leaves==factorial(8) and len(physical)==5270
    for q,p in physical.items():literal(p,q)
    assert {tuple(sorted(30-x for x in q)) for q in physical}==set(physical)
    positive=(14,14,14,15,15,15,16,17)
    literal((14,13,15,11,12,10,9,8),positive)
    reflected=tuple(sorted(30-x for x in positive))
    assert CORE.issubset(positive) and not CORE.issubset(reflected)
    assert reflected in physical and independent(reflected) is not None
    negative=(8,10,15,15,15,19,19,19)
    assert cuts(negative,8) and negative not in physical and independent(negative) is None
    primary={q for q in profile_stream(8) if CORE.issubset(q)}
    secondary=set()
    for tail in combinations_with_replacement(range(8,23),4):
        if sum(tail)!=58:continue
        q=tuple(sorted((14,15,16,17)+tail))
        if all_cuts(q):secondary.add(q)
    assert primary==secondary,'whole domain mismatch'
    assert positive in primary and reflected not in primary
    print(json.dumps({'controls':'complete profile/count map, whole independent target domain, literal positive, known negative, physical reflection and asymmetric bridge PASS','candidate_profiles':len(primary)}),flush=True)
    for i,q in enumerate(sorted(primary),1):
        guard()
        proof=independent(q)
        if q not in physical:
            assert proof is None,'negative oracle mismatch'
            print(json.dumps({'result':'FIRST COUNTEREXAMPLE','q':q,'index':i,'search_nodes':NODES,'seconds':time.monotonic()-START}),flush=True)
            return
        assert proof is not None,'positive oracle mismatch'
        p=physical[q];literal(p,q)
        print(json.dumps({'certificate':q,'highs':p}),flush=True)
    print(json.dumps({'result':'FIXED DOMAIN PASS','candidate_profiles':len(primary),'search_nodes':NODES,'permutations':leaves,'physical_profiles':len(physical),'seconds':time.monotonic()-START}),flush=True)

if __name__=='__main__':main()
