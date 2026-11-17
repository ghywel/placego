#!/usr/bin/env python3
"""B32 / MI079, preregistered before execution, 2026-10-16.

Predict 122 sparse G306 cores (u subtotals 69/37/14/2), independently
joined. Core order starts with u; at most six permutations of the remaining
v,a,b, roots 0/1: <=12 candidates. A runway at 1..3 (root 0) or 2..4
(root 1) should fit every core and support a two-unit fan. Direct fan-2
and mixed (+1,+2,-3) target joins each predict 122. Blind mixed-hypergraph
prediction: no five-label cover among all 2,002 subsets; report refutation
honestly without invalidating independent runway checks. Restricted four
candidates must fail on (7,9,1,1) and (6,6,5,5); reused pair and wrong sums
rejected; consecutive-three hypergraph really blocked by {2,5,8,11}.
Caps 150 cores / 2,000 candidates / five process CPU seconds; no expansion.
Raw outside git. No general E28/threshold claim or novelty assertion.
OUTCOME (2026-10-16, GPT Intel CPU; preregistration 6f6af2b9): all 122
runways, fan-2 and mixed-module certificates pass; all three independent
domains agree. Candidate count 191; chosen attempts 1..5. Restricted
controls both fail as predicted; ownership and wrong sums rejected.
Blind no-five-cover prediction REFUTED: unique cover {3,4,8,9,13}.
CPU 0.042113 s, no cutoff. Raw math-instinct-b32-two-surplus.json
outside git, SHA256
dc98daa13fc37d2d61e630ff93f10175dfcb042c5b780b48dc363a55856958a7.
Finite certificates COMPUTED; no independent hand read.
"""
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations
import json
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok


def label(x):
    return min(x,27-x)


def core_target(u,v,a,b):
    return (56+2*u,56+2*v,112-2*(u+v+a+b))+(112,)*3+(112+2*a,112+2*b)


def selected_for(params, order, root):
    u,v,a,b=params
    queue=defaultdict(list);queue[u].append(0);queue[v].append(1)
    if a:queue[a].append(6)
    if b:queue[b].append(7)
    selected={};x=root
    for step in order:
        selected[queue[step].pop(0)]=x;x+=step
    selected[2]=x
    assert all(not q for q in queue.values())
    labels=[label(x) for x in selected.values()]
    if min(selected.values())<0 or max(selected.values())>27 or len(set(labels))!=len(labels):
        return None
    start=root+1
    if any(x in labels for x in range(start,start+3)):
        return None
    materialize(core_target(*params),selected)
    return selected,start,order,root


def find(params, counter, restricted=False):
    u,v,a,b=params
    if restricted:
        tails=set(tuple(x for x in (a,b,v) if x) for a,b in ((a,b),(b,a)))
    else:
        tails=set(permutations(tuple(x for x in (v,a,b) if x)))
    attempts=0
    for tail in sorted(tails):
        order=(u,)+tail
        for root in (0,1):
            counter[0]+=1;attempts+=1
            if counter[0]>2000:raise RuntimeError('CANDIDATE_CAP')
            candidate=selected_for(params,order,root)
            if candidate is not None:return candidate,attempts
    return None,attempts


def extend(core, selected, positions, steps, force=False):
    # Three neutral bins; first two hold the positive steps, third the negative.
    target=list(core);selected=dict(selected)
    for i,x,step in zip((3,4,5),positions,steps):
        target[i]=112+2*step;selected[i]=x
    if force:selected[3]=next(x for i,x in selected.items() if i not in (3,4,5))
    order=sorted(range(8),key=lambda i:(target[i],i));mapping={old:new for new,old in enumerate(order)}
    target=tuple(target[i] for i in order)
    witness=materialize(target,{mapping[i]:x for i,x in selected.items()})
    assert certificate_ok(witness['bins'],target)
    return dict(targets=target,witness=witness)


def direct(high_count=5, minimum112=3, module=None):
    low=defaultdict(list)
    for triple in combinations_with_replacement(range(68,111,2),3):low[sum(triple)].append(triple)
    out=set()
    for high in combinations_with_replacement(range(112,123,2),high_count):
        if module is None:
            if high.count(112)<minimum112:continue
            fixed=()
        elif module=='fan':
            if high.count(114)<2:continue
            fixed=(108,)
        else:
            if high.count(114)<1 or high.count(116)<1:continue
            fixed=(106,)
        for triple in low.get(784-sum(high)-sum(fixed),[]):
            if fixed and triple[-1]>fixed[0]:continue
            out.add(triple+fixed+high)
    return out


def graph_controls():
    triples={frozenset(label(x+d) for d in (0,1,3)) for x in range(25)
             if len({label(x+d) for d in (0,1,3)})==3}
    covers=[c for c in combinations(range(14),5) if all(set(c)&t for t in triples)]
    consecutive={frozenset(label(x+d) for d in (0,1,2)) for x in range(26)
                 if len({label(x+d) for d in (0,1,2)})==3}
    assert all(set((2,5,8,11))&t for t in consecutive)
    return dict(edges=[sorted(t) for t in sorted(triples,key=lambda t:sorted(t))],
                five_covers=covers,prediction='PASS' if not covers else 'REFUTED',
                consecutive_control='FOUR_USED_CAN_BLOCK')


def main():
    start=time.process_time();counter=[0]
    params=[(u,v,a,b) for u in range(6,10) for v in range(u,12)
            for a,b in combinations_with_replacement(range(6),2) if u+2*v+a+b<=28]
    cores={core_target(*p) for p in params}
    assert len(params)==len(cores)==122 and cores==direct()
    assert Counter(p[0] for p in params)=={6:69,7:37,8:14,9:2}
    for p in ((7,9,1,1),(6,6,5,5)):
        bad,_=find(p,counter,restricted=True);assert bad is None
        good,_=find(p,counter);assert good is not None
    graph=graph_controls()
    results=[];fans=set();mixed=set();attempts_hist=Counter()
    for p in params:
        if len(results)>=150 or time.process_time()-start>=5:
            print(json.dumps(dict(status='UNKNOWN',completed=len(results),graph=graph)));return
        answer,attempts=find(p,counter)
        if answer is None:
            print(json.dumps(dict(status='REFUTED_RUNWAY',params=p,completed=len(results),graph=graph)));return
        selected,runway,order,root=answer;core=core_target(*p)
        fan=extend(core,selected,(runway,runway+1,runway+2),(1,1,-2))
        fans.add(tuple(fan['targets']))
        used={label(x) for x in selected.values()}
        free=[x for x in range(25) if len({label(x),label(x+1),label(x+3)})==3
              and all(label(x+d) not in used for d in (0,1,3))]
        if free:
            x=free[0];m=extend(core,selected,(x,x+1,x+3),(1,2,-3));mixed.add(tuple(m['targets']))
        else:m=None
        results.append(dict(params=p,order=order,root=root,runway=runway,
                            selected=selected,fan=fan,mixed=m,attempts=attempts))
        attempts_hist[attempts]+=1
    assert fans==direct(4,module='fan') and len(fans)==122
    if len(mixed)==122:assert mixed==direct(4,module='mixed')
    sample=results[0]
    try:extend(core_target(*sample['params']),sample['selected'],(1,2,3),(1,1,-2),force=True)
    except ValueError as exc:assert str(exc)=='complementary pair reused'
    else:raise AssertionError('forced pair reuse accepted')
    wrong=[set(b) for b in sample['fan']['witness']['bins']];a,b=min(wrong[0]),min(wrong[1])
    wrong[0].remove(a);wrong[1].remove(b);wrong[0].add(b);wrong[1].add(a)
    assert Counter(v for bins in wrong for v in bins)==Counter(range(1,56,2))
    assert not certificate_ok(wrong,sample['fan']['targets'])
    print(json.dumps(dict(status='ALL_RUNWAYS',results=results,graph=graph,core_count=len(cores),
                          fan_count=len(fans),mixed_count=len(mixed),attempts_hist=dict(attempts_hist),
                          candidate_count=counter[0],restricted_controls='BOTH_FAIL',
                          reused_pair='REJECTED',wrong_sums='REJECTED_COVERAGE_PRESERVED',
                          cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
