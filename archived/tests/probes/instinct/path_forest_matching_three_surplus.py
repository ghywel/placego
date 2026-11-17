#!/usr/bin/env python3
"""B42/MI099 uniform matching-edge family, preregistered a353851a.

Cancel g/-g, embed five-point core h,a,b,c,-H using seven roots selected
by gap-graph covers, then place a spare gap-g 2-cycle. Exact physical vs
label graph, displayed six-matchings and all five-cover classifications.
Independent signed-target domain; stable role mapping; full odd checker.
Countercontrol h10/g9/(1,1,1) root0 covers all gap9 edges; restricted roots
repair. Forced occupied endpoint and coverage-preserving wrong sums fail.
Caps2500 parameter instances/five CPU seconds, stop without widening.
OUTCOME:999 parameter instances,999 distinct targets, independent domain
sets equal; all certificates and cover/graph controls pass. Gap6..14
counts148,148,146,140,127,107,83,60,40. Bad root control repaired at4.
CPU0.131515 s. Raw outside git SHA256
d03a0e92d5878e200535ec0c8016220a328668f1d3e16c328d341d6ede0573c8.
Uniform hand argument PROOF-SKETCH pending independent review.
"""
from collections import Counter
from itertools import combinations,combinations_with_replacement
import json
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok

MATCHINGS={
    6:((0,6),(1,7),(2,8),(3,9),(4,10),(5,11)),
    7:((0,7),(1,8),(2,9),(3,10),(4,11),(5,12)),
    8:((0,8),(1,9),(2,10),(3,11),(4,12),(5,13)),
    12:((0,12),(1,13),(4,11),(5,10),(6,9),(7,8)),
    13:((0,13),(2,12),(3,11),(4,10),(5,9),(6,8)),
    14:((0,13),(1,12),(2,11),(3,10),(4,9),(5,8))}


def label(x):return min(x,27-x)


def graph(g):
    physical={frozenset((label(x),label(x+g))) for x in range(28-g)}
    physical={e for e in physical if len(e)==2}
    formula={frozenset((i,j)) for i in range(14) for j in range(i+1,14)
             if j-i==g or i+j==27-g}
    assert physical==formula
    return physical


def covers(g):
    edges=graph(g)
    found={frozenset(c) for c in combinations(range(14),5) if all(set(c)&e for e in edges)}
    if g in MATCHINGS:
        matching=MATCHINGS[g]
        assert len(set(x for edge in matching for x in edge))==12
        assert all(frozenset(e) in edges for e in matching)
        assert not found
    elif g==9:
        assert found=={frozenset((10,11,12,13,x)) for x in (0,9)}
    elif g==10:
        assert found=={frozenset((10,11,12,13,x)) for x in (8,9)}
    else:
        assert g==11
        assert found=={frozenset((11,12,13,x,y)) for x in (6,10) for y in (7,9)}
    return found


def allowed_roots(g):
    if g==9:return tuple(range(1,8))
    if g==11:return (0,1,2,3,4,5,8)
    return tuple(range(7))


def core(h,a,b,c,r):
    return {0:r,5:r+h,6:r+h+a,7:r+h+a+b,2:r+h+a+b+c}


def core_valid(s):
    xs=list(s.values());return min(xs)>=0 and max(xs)<=27 and len({label(x) for x in xs})==5


def gap(g,used):
    return next((x for x in range(28-g) if label(x)!=label(x+g)
                 and label(x) not in used and label(x+g) not in used),None)


def construct(h,g,a,b,c,force_occupied=False):
    H=h+a+b+c
    r=next(r for r in allowed_roots(g) if core_valid(core(h,a,b,c,r)))
    selected=core(h,a,b,c,r);used={label(x) for x in selected.values()}
    x=gap(g,used);assert x is not None
    if force_occupied:x=r
    selected.update({1:x,3:x+g})
    original=(56+2*h,56+2*g,112-2*H,112-2*g,112,112+2*a,112+2*b,112+2*c)
    order=sorted(range(8),key=lambda i:(original[i],i));mapping={old:new for new,old in enumerate(order)}
    target=tuple(original[i] for i in order)
    selected={mapping[i]:x for i,x in selected.items()}
    witness=materialize(target,selected);assert certificate_ok(witness['bins'],target)
    return dict(params=(h,g,a,b,c),targets=target,root=r,gap_start=x,witness=witness)


def direct_domain():
    out=set()
    for a,b,c in combinations_with_replacement(range(1,6),3):
        q=a+b+c
        for u in range(6,15):
            for v in range(u,18):
                total=u+v+q
                for W in range((total+1)//2,min(22,28-v,total-1)+1):
                    Z=total-W
                    if not {u,v}&{W,Z}:continue
                    out.add((56+2*u,56+2*v,112-2*W,112-2*Z,112,112+2*a,112+2*b,112+2*c))
    return out


def main():
    start=time.process_time();all_covers={g:covers(g) for g in range(6,15)}
    assert [len(all_covers[g]) for g in range(6,15)]==[0,0,0,2,2,4,0,0,0]
    for g in (9,10,11):
        assert len(allowed_roots(g))==7
        assert all(r not in set().union(*all_covers[g]) for r in allowed_roots(g))
    bad=core(10,1,1,1,0);assert core_valid(bad)
    assert {label(x) for x in bad.values()}=={0,10,11,12,13}
    assert gap(9,{label(x) for x in bad.values()}) is None
    repaired=construct(10,9,1,1,1);assert repaired['root']==4
    try:construct(10,9,1,1,1,force_occupied=True)
    except ValueError as ex:assert str(ex)=='complementary pair reused'
    else:raise AssertionError('forced occupied label accepted')
    bins=[set(x) for x in repaired['witness']['bins']];x,y=min(bins[0]),min(bins[1])
    bins[0].remove(x);bins[1].remove(y);bins[0].add(y);bins[1].add(x)
    assert Counter(x for b in bins for x in b)==Counter(range(1,56,2))
    assert not certificate_ok(bins,repaired['targets'])
    results=[];roots_hist=Counter();by_gap=Counter()
    for h in range(6,15):
        for g in range(6,15):
            for a,b,c in combinations_with_replacement(range(1,6),3):
                H=h+a+b+c
                if max(h,g)+max(H,g)>28:continue
                if len(results)>=2500 or time.process_time()-start>=5:
                    print(json.dumps(dict(status='UNKNOWN',completed=len(results))));return
                assert H<=21 and H<=28-g
                # Every prescribed root fits; pair-count is only over these seven.
                assert all(r+H<=27 for r in allowed_roots(g))
                result=construct(h,g,a,b,c);results.append(result)
                roots_hist[result['root']]+=1;by_gap[g]+=1
    targets={tuple(x['targets']) for x in results};assert targets==direct_domain()
    print(json.dumps(dict(status='ALL_MATCHING_THREE_SURPLUS',instances=len(results),
        distinct_targets=len(targets),results=results,by_gap=dict(by_gap),roots=dict(roots_hist),
        five_covers={g:[sorted(s) for s in sorted(cs,key=lambda s:tuple(sorted(s)))]
                     for g,cs in all_covers.items()},controls='PASS',
        bad_root='VALID_CORE_BUT_NO_GAP',repair_root=4,cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
