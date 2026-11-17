#!/usr/bin/env python3
"""B54/MI126 preregistered1c2c1bc5: known nyctalopic ordering.

Exactly605 primitive four-surplus targets. Start smallest positive, then
largest magnitude term opposite in sign to current sum; lowest owner tie.
Known minimal-zero-sum lemmas guarantee distinct vertices, span<=W+v-2<=26.
Blind all605 reflection-free translations, not implied by that theorem.
Independent primitive DP domain, direct labels/forbidden pair sums and two
literal checkers. Fixture root0 fail/root6 pass, nonprimitive repetition,
duplicate/wrong-sum controls. Unexpected nonzero roots and span26 boundary.
Cap700 targets/25000 roots/two CPU seconds, no other order/start/solver.
OUTCOME:605 exact primitive inputs, all distinct vertices/range bounds;
575 certificates,30 fixed-order reflection failures. All5918 direct/pair-
sum comparisons and both partition checkers/controls pass.481 successes
need nonzero root; spans12..24, no span26. CPU0.439922 s. Raw outside git
SHA25696edf2cd031e499a38f07e50290d2fa22d43c03c61c2bb7a3360f89619bfca32.
Blind universal fixed-greedy placement REFUTED; no alternate orders tested.
"""
from collections import Counter,defaultdict
from itertools import combinations,combinations_with_replacement
from pathlib import Path
import hashlib
import json
import sys
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok
from path_forest_three_surplus_audit import bitset_ok


def target(p):
    u,v,W,Z,steps=p
    return (56+2*u,56+2*v,112-2*W,112-2*Z)+tuple(112+2*s for s in steps)


def primitive_domain(prior_path):
    raw=Path(prior_path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='e25cb282fabd0cade077a3482743ff735c94f89cc25af39707358b64b99e66d2'
    prior=json.loads(raw);out={tuple(e['targets']):e['params'] for e in prior['primitive_targets']}
    lows=defaultdict(list)
    for xs in combinations_with_replacement(range(68,111,2),4):lows[sum(xs)].append(xs)
    direct=set()
    for high in combinations_with_replacement(range(114,123,2),4):
        steps=tuple((x-112)//2 for x in high)
        for xs in lows[784-sum(high)]:
            u,v=(xs[0]-56)//2,(xs[1]-56)//2;W=(112-xs[2])//2
            reachable=1
            for x in (u,v)+steps:reachable|=reachable<<x
            if not reachable&(1<<W):direct.add(xs+high)
    assert set(out)==direct and len(out)==605
    return out


def partial_vertices(values):
    vertices=[];current=0
    for value in values:vertices.append(current);current+=value
    assert current==0
    if len(set(vertices))!=len(values):raise ValueError('literal vertex repeated')
    return vertices


def greedy(p):
    u,v,W,Z,steps=p
    remaining={0:u,1:v,2:-W,3:-Z,**{4+i:s for i,s in enumerate(steps)}}
    pos={i:x for i,x in remaining.items() if x>0}
    first=min(pos,key=lambda i:(pos[i],i));order=[first];current=remaining.pop(first)
    while remaining:
        assert current!=0
        choices=[i for i,x in remaining.items() if x*current<0];assert choices
        owner=min(choices,key=lambda i:(-abs(remaining[i]),i))
        order.append(owner);current+=remaining.pop(owner)
    values={0:u,1:v,2:-W,3:-Z,**{4+i:s for i,s in enumerate(steps)}}
    vertices=partial_vertices([values[i] for i in order]);m=min(vertices)
    assert min(vertices)>=1-W and max(vertices)<=v-1
    normalized={i:x-m for i,x in zip(order,vertices)};D=max(normalized.values())
    assert D<=W+v-2<=26
    return order,normalized,D


def certificate(p,selected,r):
    w=materialize(target(p),{i:x+r for i,x in selected.items()})
    assert certificate_ok(w['bins'],target(p)) and bitset_ok(w['bins'],target(p))
    return w


def controls():
    p=(7,7,21,13,(5,5,5,5));order,S,D=greedy(p)
    assert order==[4,2,0,1,5,3,6,7]
    expected={4:22,2:27,0:6,1:13,5:20,3:25,6:12,7:17}
    assert {i:x+6 for i,x in S.items()}==expected
    try:certificate(p,S,0)
    except ValueError as e:assert str(e)=='complementary pair reused'
    else:raise AssertionError('wrong root accepted')
    w=certificate(p,S,6)
    try:partial_vertices((8,8,4,-20,2,2,2,-6))
    except ValueError as e:assert str(e)=='literal vertex repeated'
    else:raise AssertionError('nonprimitive prefix repetition accepted')
    bins=[list(b) for b in w['bins']];bins[0][0]=bins[1][0]
    assert not certificate_ok(bins,target(p)) and not bitset_ok(bins,target(p))
    bins=[set(b) for b in w['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert sorted(x for b in bins for x in b)==list(range(1,56,2))
    assert not certificate_ok(bins,target(p)) and not bitset_ok(bins,target(p))


def main():
    start=time.process_time();controls();family=primitive_domain(sys.argv[1]);results=[];failures=[]
    checks=0;spans=Counter();root_counts=Counter();nonzero=0
    for t,p in sorted(family.items()):
        if len(results)>=700 or time.process_time()-start>=2:
            print(json.dumps(dict(status='UNKNOWN',completed=len(results))));return
        order,S,D=greedy(p);spans[D]+=1;roots=[];blocks=[]
        for r in range(28-D):
            checks+=1;assert checks<=25000 and time.process_time()-start<2
            bad=[(i,j) for i,j in combinations(S,2) if S[i]+S[j]+2*r==27]
            labels={min(x+r,27-x-r) for x in S.values()}
            assert (len(labels)==8)==(not bad)
            if not bad:roots.append(r)
            blocks.append(dict(root=r,bad_owner_pairs=bad))
        root_counts[len(roots)]+=1
        entry=dict(params=p,targets=t,order=order,selected=S,span=D,roots=roots)
        if roots:
            r=roots[0];entry['chosen']=dict(root=r,witness=certificate(p,S,r));nonzero+=int(r>0)
        else:entry['blocked_roots']=blocks;failures.append(entry)
        results.append(entry)
    print(json.dumps(dict(status='DIAGNOSED',total=len(family),certified=len(results)-len(failures),
        results=results,failures=failures,root_checks=checks,spans=dict(spans),
        roots_per_target=dict(root_counts),nonzero_chosen_roots=nonzero,controls='PASS',
        cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
