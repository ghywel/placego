#!/usr/bin/env python3
"""B30 / MI075, preregistered before execution, 2026-10-16.

All sorted even E28 with t4=108,t5>=112. Predict 421 inputs and certificates,
independent domains agreeing as sets; subtotals by u: 249/119/43/9/1.
Use G306 plus gap-2 pair, three-cycle for two unit positives, or prescribed
negative-edge insertion. No arbitrary order/root/cycle/role search. The
three-cycle placement predicts exactly two default-core failures repaired
by translation +1, with explicit core ownership recheck. Counterfactuals:
omit those shifts, omit q=11 correction, omit constant-3 ordering. Independent
coverage-preserving wrong-sum control. Caps 600 inputs/five process CPU
seconds; stop on any disagreement or failure. Raw JSON outside git.
OUTCOME (2026-10-16, GPT Intel CPU; preregistration c1208711): all 421
formula certificates pass; independent domains agree. Matched2=188;
triple=83, triple_shift=2; remaining 148 use insertion branches. All four
omission controls and coverage-preserving sum corruption rejected.
CPU 0.084272 s, no cutoff. Raw math-instinct-b30-gap-two.json outside git,
SHA256 9684ee21d18ab0c22fbe7f77c74928cd962ae51e43f5a6ccd6c3cf56f330c5a7.
Finite certificates COMPUTED; uniform argument not independently read.
"""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement
import json
import time

from path_forest_one_negative import construct as core_construct, avoid_level
from path_forest_cycle_cover import setup, materialize
from path_forest_receiving_chains import certificate_ok


def lab(x):
    return min(x,27-x)


def domains():
    param = set()
    for u in range(6,11):
        for v in range(u,13):
            for p in combinations_with_replacement(range(6),4):
                q = sum(p)
                if u+2*v+q <= 30:
                    w = u+v+q-2
                    param.add((56+2*u,56+2*v,112-2*w,108)+tuple(112+2*a for a in p))
    lows,highs = defaultdict(list),defaultdict(list)
    for low in combinations_with_replacement(range(68,111,2),3):
        lows[sum(low)].append(low)
    for high in combinations_with_replacement(range(112,123,2),4):
        highs[sum(high)].append(high)
    direct = {low+(108,)+high for s,ls in lows.items() for low in ls
              for high in highs.get(676-s,[]) if low[-1] <= 108}
    assert param == direct and len(param) == 421
    assert Counter((t[0]-56)//2 for t in param) == {6:249,7:119,8:43,9:9,10:1}
    return param


def construct(targets, force=None):
    targets,_,e = setup(targets)
    assert targets[3] == 108 and targets[4] >= 112
    u,v = e[0:2]
    p = tuple(e[4:]);q=sum(p);w=-e[2];b=w+2
    assert b == u+v+q
    repaired = False
    if 2 in p or p.count(1) >= 2:
        neutral = list(targets);neutral[3]=112
        if 2 in p:
            positives = [4+p.index(2)]
            mode = 'pair'
        else:
            positives = [i for i in range(4,8) if e[i] == 1][:2]
            mode = 'triple'
        for i in positives:
            neutral[i]=112
        ordered = tuple(sorted(neutral))
        core = core_construct(ordered)
        selected_core = dict(core['witness']['selected'])
        remaining = tuple(a for a in ((t-112)//2 for t in ordered[3:]) if a)
        repaired = mode == 'triple' and u == v == 6 and remaining in ((3,3),(3,5))
        if repaired and force != 'no_shift':
            selected_core = {i:x+1 for i,x in selected_core.items()}
            materialize(ordered,selected_core)
        queues=defaultdict(list)
        for i,t in enumerate(neutral):queues[t].append(i)
        mapping={i:queues[t].pop(0) for i,t in enumerate(ordered)}
        selected={mapping[i]:x for i,x in selected_core.items()}
        used={lab(x) for x in selected.values()}
        if mode == 'pair':
            x=next(x for x in range(26) if lab(x)!=lab(x+2)
                   and lab(x) not in used and lab(x+2) not in used)
            selected[positives[0]],selected[3]=x,x+2
            branch='matched2'
        else:
            free=[x for x in range(12) if all(x+j not in used for j in range(3))]
            if not free:
                raise ValueError('no free consecutive triple')
            x=free[0]
            selected[positives[0]],selected[positives[1]],selected[3]=x,x+1,x+2
            branch='triple_shift' if repaired else 'triple'
        order,root=None,None
    else:
        pos=tuple(a for a in p if a)
        if q <= 6:
            if (u,v,q) in ((7,8,6),(8,8,6)):
                order,root,branch=(u,)+pos+(v,),0,'low_cluster'
            elif (u,v,q)==(6,9,6):
                order=(v,)+pos+(u,) if pos==(1,5) else (3,u,3,v)
                assert pos in ((1,5),(3,3))
                root,branch=0,'low_69'
            else:
                order=pos+(u,v);root=int(q+u+b==27);branch='low_'+str(root)
        elif q==12:
            assert u==v==6
            order,root,branch=tuple(sorted(pos,reverse=True))+(u,v),1,'q12'
        elif q==11 and force!='ordinary_q11':
            assert u==v==6
            largest=max(pos);rest=list(pos);rest.remove(largest)
            adjusted,_=avoid_level(tuple(rest),4)
            assert adjusted is not None
            order,root,branch=adjusted+(largest,u,v),0,'q11'
        elif u==6 and v in (6,7) and pos==(5,5):
            order,root,branch=(u,5,v,5),0,'constant5'
        elif u==v==7 and pos==(4,4):
            order,root,branch=(7,4,7,4),0,'constant4'
        elif u==v==7 and pos==(3,3,3) and force!='ordinary_constant3':
            order,root,branch=(3,7,3,7,3),0,'constant3'
        else:
            alt=q==u+1 or (u,v,q)==(7,8,7)
            level=q-u+(3 if alt else 1)
            adjusted,_=avoid_level(pos,level)
            if adjusted is None:raise ValueError('unavoidable prefix')
            order,root,branch=adjusted+(u,v),(12 if alt else 13)-q,'high_alt' if alt else 'high'
        queues=defaultdict(list);queues[u].append(0);queues[v].append(1)
        for i,a in enumerate(p,4):
            if a:queues[a].append(i)
        selected={};x=root
        for a in order:
            selected[queues[a].pop(0)]=x;x+=a
        assert x==root+b and all(not z for z in queues.values())
        selected[2],selected[3]=x,root+2
    witness=materialize(targets,selected)
    assert certificate_ok(witness['bins'],targets)
    return dict(branch=branch,order=order,root=root,repaired=repaired,witness=witness)


def main():
    start=time.process_time();family=domains()
    shifts=((68,68,76,108,114,114,118,118),(68,68,72,108,114,114,118,122))
    for t in shifts:
        try:construct(t,force='no_shift')
        except ValueError as exc:assert str(exc)=='no free consecutive triple'
        else:raise AssertionError('omitted shift did not expose predicted obstruction')
    for target,force,reason in (
        ((68,68,70,108,112,118,118,122),'ordinary_q11','complementary pair reused'),
        ((70,70,70,108,112,118,118,118),'ordinary_constant3','unavoidable prefix')):
        try:construct(target,force=force)
        except ValueError as exc:assert str(exc)==reason
        else:raise AssertionError('omitted correction accepted')
    sample=next(iter(sorted(family)));cert=construct(sample)
    wrong=[set(b) for b in cert['witness']['bins']];a,b=min(wrong[0]),min(wrong[1])
    wrong[0].remove(a);wrong[1].remove(b);wrong[0].add(b);wrong[1].add(a)
    assert Counter(v for bins in wrong for v in bins)==Counter(range(1,56,2))
    assert not certificate_ok(wrong,sample)
    results=[];branches=Counter()
    for t in sorted(family):
        if len(results)>=600 or time.process_time()-start>=5:
            print(json.dumps(dict(status='UNKNOWN',completed=len(results))));return
        result=construct(t);branches[result['branch']]+=1
        results.append(dict(targets=t,construction=result))
    assert branches['triple_shift']==2
    print(json.dumps(dict(status='ALL_421',results=results,branches=dict(branches),
                          independent_count=len(family),omitted_shifts='NO_FREE_TRIPLE',
                          wrong_q11='REJECTED_PAIR_COLLISION',
                          wrong_constant3='REJECTED_PREFIX_OBSTRUCTION',
                          wrong_sums='REJECTED_COVERAGE_PRESERVED',
                          cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
