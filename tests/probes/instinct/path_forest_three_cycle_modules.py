#!/usr/bin/env python3
"""B33 / MI081, preregistered before execution, 2026-10-16.

Default G306 core plus (+c,+d,-c-d), 1<=c<=d<=5, on 122 sparse cores:
1,830 instances, deduplicated targets independently joined. Default mixed
(1,2) must succeed for all 122, from the hand unique-cover argument.
Compare default core with the fixed <=12 u-first/root-0-or-1 runway cores;
predict one supports every instance. Default failures retained; first
failure of the complete fixed class stops, not repaired by wider search.
Cap 2,000 instances / five process CPU seconds. No general cycle solver.
Controls: 23 mixed coordinate hyperedges equal hand description; bad cover
{3,4,8,9,13} blocks; occupied core and wrong sums rejected; old minimum
boundary target recovered as its known 5+3 decomposition. Raw outside git.
"""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement, permutations
import json
import time
from path_forest_one_negative import construct as core_construct
from path_forest_two_surplus_runway import core_target,selected_for
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok


def lab(x):return min(x,27-x)


def slot(selected,c,d):
    used={lab(x) for x in selected.values()}
    for x in range(28-c-d):
        positions=(x,x+c,x+c+d);labels=[lab(y) for y in positions]
        if len(set(labels))==3 and not set(labels)&used:return positions
    return None


def extend(core,selected,gaps,positions,force=False):
    c,d=gaps;target=list(core);selected=dict(selected)
    for i,step,x in zip((3,4,5),(c,d,-c-d),positions):
        target[i]=112+2*step;selected[i]=x
    if force:selected[3]=next(x for i,x in selected.items() if i not in (3,4,5))
    order=sorted(range(8),key=lambda i:(target[i],i));mapping={old:new for new,old in enumerate(order)}
    target=tuple(target[i] for i in order)
    witness=materialize(target,{mapping[i]:x for i,x in selected.items()})
    assert certificate_ok(witness['bins'],target)
    return dict(targets=target,positions=positions,witness=witness)


def candidates(params):
    u,v,a,b=params;core=core_target(*params)
    default=core_construct(core)['witness']['selected']
    out=[dict(kind='default',selected=default)]
    seen={tuple(sorted(default.items()))}
    for tail in sorted(set(permutations(tuple(x for x in (v,a,b) if x)))):
        for root in (0,1):
            answer=selected_for(params,(u,)+tail,root)
            if answer is not None:
                sel,_,order,root=answer;key=tuple(sorted(sel.items()))
                if key not in seen:
                    seen.add(key);out.append(dict(kind='u_first',selected=sel,order=order,root=root))
    assert len(out)<=13
    return core,out


def direct():
    lows=defaultdict(list)
    for t in combinations_with_replacement(range(68,111,2),3):lows[sum(t)].append(t)
    highs=list(combinations_with_replacement(range(112,123,2),4));out=set()
    for c,d in combinations_with_replacement(range(1,6),2):
        negative=112-2*(c+d);need=Counter((c,d))
        for high in highs:
            have=Counter((t-112)//2 for t in high)
            if any(have[x]<count for x,count in need.items()):continue
            for low in lows.get(784-negative-sum(high),[]):
                if low[-1]<=negative:out.add(low+(negative,)+high)
    return out


def main():
    start=time.process_time();params=[(u,v,a,b) for u in range(6,10) for v in range(u,12)
        for a,b in combinations_with_replacement(range(6),2) if u+2*v+a+b<=28]
    assert len(params)==122
    expected={frozenset((i,i+1,i+3)) for i in range(11)}
    expected|={frozenset((i,i+2,i+3)) for i in range(11)}
    expected.add(frozenset((11,12,13)))
    generated={frozenset(lab(x+d) for d in (0,1,3)) for x in range(25)
               if len({lab(x+d) for d in (0,1,3)})==3}
    assert expected==generated and len(generated)==23
    assert all(set((3,4,8,9,13))&t for t in generated)
    pool={p:candidates(p) for p in params}
    parameter_targets=set()
    for core,_ in pool.values():
        for c,d in combinations_with_replacement(range(1,6),2):
            t=list(core);t[3:6]=(112+2*c,112+2*d,112-2*(c+d));parameter_targets.add(tuple(sorted(t)))
    independent=direct();assert parameter_targets==independent
    mixed=[]
    for p,(core,choices) in pool.items():
        positions=slot(choices[0]['selected'],1,2);assert positions is not None
        mixed.append(extend(core,choices[0]['selected'],(1,2),positions))
    # Known 5+3 fixture is a carrying control, not a fresh target discovered here.
    core,choices=pool[(6,6,5,5)];positions=slot(choices[0]['selected'],5,5)
    assert positions==(2,7,12)
    minimum=extend(core,choices[0]['selected'],(5,5),positions)
    assert minimum['targets']==(68,68,68,92,122,122,122,122)
    try:extend(core,choices[0]['selected'],(5,5),positions,force=True)
    except ValueError as exc:assert str(exc)=='complementary pair reused'
    else:raise AssertionError('forced core reuse accepted')
    wrong=[set(b) for b in minimum['witness']['bins']];a,b=min(wrong[0]),min(wrong[1])
    wrong[0].remove(a);wrong[1].remove(b);wrong[0].add(b);wrong[1].add(a)
    assert Counter(v for bins in wrong for v in bins)==Counter(range(1,56,2))
    assert not certificate_ok(wrong,minimum['targets'])
    results=[];defaults_failed=[];targets=set();used_choices=Counter()
    for p,(core,choices) in pool.items():
        for gaps in combinations_with_replacement(range(1,6),2):
            if len(results)+len(mixed)>=2000 or time.process_time()-start>=5:
                print(json.dumps(dict(status='UNKNOWN',completed=len(results),mixed_count=len(mixed))));return
            positions=slot(choices[0]['selected'],*gaps)
            if positions is None:defaults_failed.append(dict(params=p,gaps=gaps))
            for index,choice in enumerate(choices):
                positions=slot(choice['selected'],*gaps)
                if positions is not None:
                    answer=extend(core,choice['selected'],gaps,positions)
                    results.append(dict(params=p,gaps=gaps,core_choice=index,choice=choice,certificate=answer))
                    targets.add(tuple(answer['targets']));used_choices[index]+=1
                    break
            else:
                print(json.dumps(dict(status='REFUTED_FIXED_CLASS',params=p,gaps=gaps,
                    candidates=choices,completed=len(results),mixed_count=len(mixed),
                    defaults_failed=defaults_failed,results=results,
                    distinct_parameter_targets=len(parameter_targets),independent_count=len(independent),
                    cpu_seconds=time.process_time()-start),indent=2));return
    assert len(results)==1830 and targets==independent
    for p in ((6,6,3,3),(6,6,3,5)):
        assert any(tuple(x['params'])==p and tuple(x['gaps'])==(1,1) for x in defaults_failed)
    print(json.dumps(dict(status='ALL_1830',results=results,mixed_count=len(mixed),
        defaults_failed=defaults_failed,used_choices=dict(used_choices),
        distinct_target_count=len(targets),independent_count=len(independent),
        occupied_core='REJECTED',wrong_sums='REJECTED_COVERAGE_PRESERVED',
        mixed_hypergraph='23_EDGES_MATCH_HAND_FORMULA',minimum_fixture='KNOWN_5_PLUS_3_REPRODUCED',
        cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
