#!/usr/bin/env python3
"""B31 / MI077, preregistered before execution, 2026-10-16.

Sparse core reordered to leave a runway for (+1^z,-z), z=3 or 4.
Predict 56 fan-3 and 14 fan-4 targets, independently joined; all literal
core/final certificates pass. Ordinary order u,a,v uses root 0 or 1;
one exception u=7,v=9,a=2 uses u,v,a at root 0. Omitted exception and
occupied-root fan must fail; independent coverage-preserving wrong-sum
control. Unexpected five-label runway for all a=0 cases. Cap 100 inputs/
five process CPU seconds, stop on disagreement or failure; raw outside git.
OUTCOME (2026-10-16, GPT Intel CPU; preregistration 28aa073d): all 70 core
and final certificates pass; independent full domains agree, 56 fan-3 and
14 fan-4. Exactly one core uses exceptional ordering. Both omitted-order
and occupied-fan counterfactuals rejected; wrong sums rejected; the stronger
five-label runway checks pass. CPU 0.015042 s, no cutoff.
Raw math-instinct-b31-unit-fans.json outside git, SHA256
250fd326107bf11c5ca3f890754e95f14f35fca31f51bd97f0f000b7299c5090.
Finite certificates COMPUTED; hand runway argument PROOF-SKETCH.
"""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement
import json
import time
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok


def construct(u,v,a,z,force=None):
    assert 6<=u<=v and 0<=a<=5 and u+2*v+a<=28
    assert z==3 or (z==4 and a==0)
    b=u+v+a
    core=(56+2*u,56+2*v,112-2*b)+(112,)*4+(112+2*a,)
    exception=(u,v,a)==(7,9,2)
    if a:
        root=int(27 in (2*u+v+a,2*u+v+2*a))
        if exception and force!='ordinary':
            root=0;selected={0:0,1:u,7:u+v,2:b}
        else:
            selected={0:root,7:root+u,1:root+u+a,2:root+b}
    else:
        root=int(2*u+v==27)
        selected={0:root,1:root+u,2:root+b}
    core_witness=materialize(core,selected)
    used={min(x,27-x) for x in selected.values()}
    start=root+1
    assert all(x not in used for x in range(start,start+z+1))
    if a==0:
        assert all(x not in used for x in range(start,start+5))
    zero=[i for i,t in enumerate(core) if i>=3 and t==112]
    negative=zero[0];positive=zero[1:z+1]
    assert len(positive)==z
    targets=list(core)
    if force=='occupied':start=root
    for j,i in enumerate(positive):
        targets[i]=114;selected[i]=start+j
    targets[negative]=112-2*z;selected[negative]=start+z
    order=sorted(range(8),key=lambda i:(targets[i],i))
    mapping={old:new for new,old in enumerate(order)}
    target=tuple(targets[i] for i in order)
    witness=materialize(target,{mapping[i]:x for i,x in selected.items()})
    assert certificate_ok(witness['bins'],target)
    return dict(targets=target,u=u,v=v,a=a,z=z,root=root,exception=exception,
                core=core_witness,witness=witness)


def domain(z):
    return [(u,v,a) for u in range(6,10) for v in range(u,12)
            for a in (range(6) if z==3 else (0,)) if u+2*v+a<=28]


def direct(z):
    low=defaultdict(list)
    for triple in combinations_with_replacement(range(68,111,2),3):low[sum(triple)].append(triple)
    result=set()
    for high in combinations_with_replacement(range(112,123,2),4):
        if high.count(114)<z:continue
        for triple in low.get(784-(112-2*z)-sum(high),[]):
            if triple[-1]<=112-2*z:result.add(triple+(112-2*z,)+high)
    return result


def main():
    start=time.process_time()
    for force in ('ordinary','occupied'):
        try:construct(7,9,2,3,force=force)
        except ValueError as exc:assert str(exc)=='complementary pair reused'
        else:raise AssertionError('deliberately wrong construction accepted')
    sample=construct(6,6,0,4)
    wrong=[set(b) for b in sample['witness']['bins']];a,b=min(wrong[0]),min(wrong[1])
    wrong[0].remove(a);wrong[1].remove(b);wrong[0].add(b);wrong[1].add(a)
    assert Counter(v for bins in wrong for v in bins)==Counter(range(1,56,2))
    assert not certificate_ok(wrong,sample['targets'])
    results=[];counts={}
    for z in (3,4):
        family=set()
        for u,v,a in domain(z):
            if len(results)>=100 or time.process_time()-start>=5:
                print(json.dumps(dict(status='UNKNOWN',completed=len(results))));return
            result=construct(u,v,a,z);target=tuple(result['targets'])
            assert target not in family;family.add(target);results.append(result)
        assert family==direct(z)
        counts[z]=len(family)
    assert counts=={3:56,4:14}
    assert sum(r['exception'] for r in results)==1
    print(json.dumps(dict(status='ALL_70',counts=counts,results=results,
                          omitted_exception='REJECTED_PAIR_COLLISION',
                          occupied_fan='REJECTED_PAIR_COLLISION',
                          wrong_sums='REJECTED_COVERAGE_PRESERVED',
                          zero_surplus_runway='FIVE_LABELS_CHECKED',
                          cpu_seconds=time.process_time()-start),indent=2))


if __name__=='__main__':main()
