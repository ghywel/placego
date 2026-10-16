#!/usr/bin/env python3
"""B29 / MI072-073, preregistered before execution, 2026-10-16.

G306 core plus one/two cancelling (+z,-z) pairs, z in 1..5. Predict 940
single-insertion and 840 double-insertion targets. Independently join low
and high tuples to compare full domains. Five folded gap graphs must
match explicit paths; enumerate all 3,003 six-label sets for each graph,
with cover counts 0,0,1,1,4. All literal partitions must pass independent
coverage/sum/cardinality checks. Forced core-pair reuse and wrong sums
must fail. Unexpected: lower-only gap-2 obstruction disappears with upper
representatives; unanchored six-label gap-5 obstruction remains real.
Caps: 2,000 formula inputs / five process CPU seconds. No arbitrary cycle,
order, root or role search. Failure stops; cutoff UNKNOWN. Raw JSON outside
git. Uniform hand extension is PROOF-SKETCH, not an adopted theorem.
"""
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement
import json
import time

from path_forest_one_negative import construct as core_construct
from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok

PATHS = {
    1: ((0,1,2,3,4,5,6,7,8,9,10,11,12,13),),
    2: ((0,2,4,6,8,10,12,13,11,9,7,5,3,1),),
    3: ((0,3,6,9,12), (1,4,7,10,13,11,8,5,2)),
    4: ((0,4,8,12,11,7,3), (1,5,9,13,10,6,2)),
    5: ((0,5,10,12,7,2), (1,6,11), (3,8,13,9,4)),
}
COVERS = {
    1: set(), 2: set(),
    3: {frozenset((3,4,5,9,10,11))},
    4: {frozenset((4,5,6,7,12,13))},
    5: {frozenset(x) for x in ((2,5,6,8,9,12), (5,6,7,8,9,12),
                              (5,6,7,8,9,10), (0,6,7,8,9,10))},
}


def label(x):
    return min(x, 27-x)


def graph_controls():
    counts = {}
    for z, paths in PATHS.items():
        derived = {tuple(sorted((label(x), label(x+z)))) for x in range(28-z)
                   if label(x) != label(x+z)}
        displayed = {tuple(sorted((a,b))) for path in paths for a,b in zip(path, path[1:])}
        assert derived == displayed
        covers = {frozenset(c) for c in combinations(range(14), 6)
                  if all(a in c or b in c for a,b in derived)}
        assert covers == COVERS[z]
        counts[z] = len(covers)
    occupied = {2,3,6,7,10,11}
    assert not any(x not in occupied and x+2 not in occupied for x in range(12))
    assert label(12) not in occupied and label(14) not in occupied
    bad = {0,6,7,8,9,10}
    assert not any(label(x) not in bad and label(x+5) not in bad
                   and label(x) != label(x+5) for x in range(23))
    return counts


def enlarge(core, gaps, force=False):
    base = core_construct(core)
    selected = dict(base['witness']['selected'])
    zero = [i for i,t in enumerate(core) if i >= 3 and t == 112]
    assert len(zero) >= 2*len(gaps)
    targets, edges = list(core), []
    core_index = next(iter(selected.values()))
    for j,z in enumerate(gaps):
        negative, positive = zero[2*j:2*j+2]
        used = {label(x) for x in selected.values()}
        assert len(used) <= 6
        x = next(x for x in range(28-z) if label(x) != label(x+z)
                 and label(x) not in used and label(x+z) not in used)
        selected[positive], selected[negative] = x, x+z
        if force and j == 0:
            selected[positive] = core_index
        targets[positive], targets[negative] = 112+2*z, 112-2*z
        edges.append((x,x+z))
    order = sorted(range(8), key=lambda i: (targets[i], i))
    mapping = {old:new for new,old in enumerate(order)}
    targets = tuple(targets[i] for i in order)
    selected = {mapping[i]:x for i,x in selected.items()}
    witness = materialize(targets, selected)
    assert certificate_ok(witness['bins'], targets)
    return dict(targets=targets, core=core, gaps=gaps, edges=edges,
                core_branch=base['branch'], witness=witness)


def instances():
    single, double = {}, {}
    core_counts = Counter()
    for k, output in ((1,single), (2,double)):
        parameters = (combinations_with_replacement(range(6),3) if k == 1
                      else ((a,) for a in range(6)))
        parameters = list(parameters)
        for u in range(6,10):
            for v in range(u,12):
                for p in parameters:
                    q = sum(p)
                    if u+2*v+q > 28:
                        continue
                    core = (56+2*u,56+2*v,112-2*(u+v+q)) + (112,)*(2*k) + tuple(112+2*a for a in p)
                    assert len(core) == 8 and tuple(sorted(core)) == core
                    core_counts[k] += 1
                    for gaps in combinations_with_replacement(range(1,6), k):
                        zero = [i for i,t in enumerate(core) if i >= 3 and t == 112]
                        targets = list(core)
                        for j,z in enumerate(gaps):
                            targets[zero[2*j]],targets[zero[2*j+1]] = 112-2*z,112+2*z
                        key = tuple(sorted(targets))
                        assert key not in output
                        output[key] = (core,gaps)
    assert core_counts == {1:188,2:56}
    assert len(single) == 940 and len(double) == 840
    return single,double


def direct(k):
    low = defaultdict(list)
    for triple in combinations_with_replacement(range(68,111,2),3):
        low[sum(triple)].append(triple)
    high = list(combinations_with_replacement(range(112,123,2),5-k))
    result = set()
    for gaps in combinations_with_replacement(range(1,6),k):
        negative = tuple(sorted(112-2*z for z in gaps))
        required = Counter(gaps)
        for upper in high:
            have = Counter((t-112)//2 for t in upper)
            if any(have[z] < count for z,count in required.items()):
                continue
            total = 784-sum(negative)-sum(upper)
            for triple in low.get(total,[]):
                if triple[-1] <= negative[0]:
                    result.add(triple+negative+upper)
    return result


def main():
    start = time.process_time()
    cover_counts = graph_controls()
    single,double = instances()
    assert set(single) == direct(1) and set(double) == direct(2)
    first_core,first_gaps = next(iter(single.values()))
    try:
        enlarge(first_core,first_gaps,force=True)
    except ValueError as exc:
        assert str(exc) == 'complementary pair reused'
    else:
        raise AssertionError('occupied core label accepted')
    valid = enlarge(first_core,first_gaps)
    wrong = [set(b) for b in valid['witness']['bins']]
    a,b = min(wrong[0]),min(wrong[1])
    wrong[0].remove(a);wrong[1].remove(b)
    wrong[0].add(b);wrong[1].add(a)
    assert Counter(v for bins in wrong for v in bins) == Counter(range(1,56,2))
    assert not certificate_ok(wrong,valid['targets'])
    results = []
    for family in (single,double):
        for target,(core,gaps) in sorted(family.items()):
            if len(results) >= 2000 or time.process_time()-start >= 5:
                print(json.dumps(dict(status='UNKNOWN', completed=len(results))))
                return
            witness = enlarge(core,gaps)
            assert tuple(witness['targets']) == target
            results.append(witness)
    print(json.dumps(dict(status='ALL_1780', independent_counts=[len(single),len(double)],
                          results=results, cover_counts=cover_counts,
                          occupied_core='REJECTED_PAIR_COLLISION',
                          wrong_sums='REJECTED_COVERAGE_PRESERVED',
                          upper_representatives='LOWER_OBSTRUCTION_REMOVED',
                          unanchored_gap5='SIX_USED_CAN_BLOCK',
                          cpu_seconds=time.process_time()-start),indent=2))


if __name__ == '__main__':
    main()
