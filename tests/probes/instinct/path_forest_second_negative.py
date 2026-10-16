#!/usr/bin/env python3
"""B28 / MI069-070, preregistered before execution, 2026-10-16.

Formula-only check of sorted even E28 with t4=110 and t5>=112. Predict 320
inputs from two independent domain constructions; all literal certificates
pass. A matching +1/-1 pair uses an unused adjacent label block; otherwise
split the closing negative edge, with analytically specified order/root
branches. No arbitrary order/root/cycle search. Caps: 1,000 inputs, five
process CPU seconds; stop on disagreement, failure or control failure.
Counterfactuals: omitted q=11 repair and occupied-label 2-cycle rejected.
Independent coverage/sum/cardinality checker rejects coverage-preserving
sum corruption. Unexpected: seven alternating occupied labels defeat the
adjacency guarantee. Raw JSON outside git; hand proof awaits review.
OUTCOME (2026-10-16, GPT Intel CPU; preregistration 4f22d5d0): all 320
formula certificates pass. Independent parameter/direct domains agree as
sets; counts by u are 199/89/27/5. Branches: separate=188, q11=6,
constant5=1, high=38, low_0=74, low_1=6, constant2=1, q_equals_u=3,
low_cluster=3. Both wrong constructions and sum corruption rejected;
seven-used-label sharpness control holds. CPU 0.056426 s, no cutoff.
Raw math-instinct-b28-second-negative.json outside git, SHA256
69213638b1577728583c3c2e732d57895dcdb4fe28160bab4de176d8e1bb9d1a.
Finite certificates COMPUTED; uniform hand argument PROOF-SKETCH.
"""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement
import json
import time

from path_forest_cycle_cover import materialize, setup
from path_forest_one_negative import construct as core_construct, avoid_level
from path_forest_receiving_chains import certificate_ok


def domains():
    parameter = set()
    for u in range(6, 10):
        for v in range(u, 12):
            for p in combinations_with_replacement(range(6), 4):
                q = sum(p)
                if u + 2*v + q <= 29:
                    w = u + v + q - 1
                    parameter.add((56+2*u, 56+2*v, 112-2*w, 110)
                                  + tuple(112+2*a for a in p))
    lows, highs = defaultdict(list), defaultdict(list)
    for t in combinations_with_replacement(range(68, 111, 2), 3):
        lows[sum(t)].append(t)
    for t in combinations_with_replacement(range(112, 123, 2), 4):
        highs[sum(t)].append(t)
    direct = {low + (110,) + high for s, values in lows.items()
              for low in values for high in highs.get(674-s, [])}
    convolution = sum(len(values) * len(highs.get(674-s, []))
                      for s, values in lows.items())
    assert parameter == direct
    assert len(parameter) == convolution == 320
    return parameter, convolution


def construct(targets, force=None):
    targets, _, e = setup(targets)
    assert targets[3] == 110 and targets[4] >= 112
    u, v, w = e[0], e[1], -e[2]
    p = tuple(e[4:])
    q = sum(p)
    assert e[3] == -1 and w == u+v+q-1
    if 1 in p:
        j = 4 + p.index(1)
        neutral = list(targets)
        neutral[3] = neutral[j] = 112
        ordered = sorted(neutral)
        core = core_construct(ordered)
        queues = defaultdict(list)
        for i, t in enumerate(neutral):
            queues[t].append(i)
        mapping = {i: queues[t].pop(0) for i, t in enumerate(ordered)}
        selected = {mapping[int(i)]: x for i, x in core['witness']['selected'].items()}
        assert 3 not in selected and j not in selected and len(selected) <= 6
        used = {min(x, 27-x) for x in selected.values()}
        # Seven fixed two-label blocks; six occupied labels cannot hit all.
        a = next(a for a in range(0, 14, 2) if a not in used and a+1 not in used)
        if force == 'reuse':
            a = next(iter(selected.values()))
        selected[j], selected[3] = a, a+1
        branch, swapped, order, root = 'separate', False, None, None
    else:
        positive = tuple(a for a in p if a)
        swapped = False
        if q <= 6:
            if (u, v, q) == (7, 8, 6):
                order, root, branch = (u,) + positive + (v,), 0, 'low_cluster'
            else:
                order = positive + (u, v)
                root = int((q+u)+(w+1) == 27)
                branch = 'low_' + str(root)
        elif q == 11 and force != 'ordinary_q11':
            assert u == v == 6
            adjusted, swapped = avoid_level(tuple(sorted(positive, reverse=True)), 8)
            assert adjusted is not None
            running = 0
            for a in adjusted:
                running += a
                assert running not in (2, 8)
            order, root, branch = adjusted + (u, v), 1, 'q11'
        elif (u, v, q) == (7, 7, 7):
            adjusted, swapped = avoid_level(positive, 3)
            assert adjusted is not None
            order, root, branch = adjusted + (u, v), 5, 'q_equals_u'
        elif u == v == 6 and positive == (5, 5):
            order, root, branch = (6, 5, 6, 5), 0, 'constant5'
        elif u == v == 7 and positive == (2, 2, 2, 2):
            order, root, branch = (2, 7, 2, 7, 2, 2), 1, 'constant2'
        else:
            adjusted, swapped = avoid_level(positive, q-u+1)
            assert adjusted is not None
            order, root, branch = adjusted + (u, v), 13-q, 'high'
        queues = defaultdict(list)
        queues[u].append(0)
        queues[v].append(1)
        for i, a in enumerate(p, 4):
            if a:
                queues[a].append(i)
        selected, running = {}, root
        for a in order:
            selected[queues[a].pop(0)] = running
            running += a
        assert running == root + w + 1
        assert all(not values for values in queues.values())
        selected[2], selected[3] = running, root+1
    witness = materialize(targets, selected)
    assert certificate_ok(witness['bins'], targets)
    return dict(branch=branch, prefix_swap=swapped, root=root, order=order,
                witness=witness)


def main():
    start = time.process_time()
    family, convolution = domains()
    counts_u = Counter((t[0]-56)//2 for t in family)
    assert counts_u == {6: 199, 7: 89, 8: 27, 9: 5}
    q11_case = (68, 68, 68, 110, 112, 116, 120, 122)
    separate_case = next(t for t in sorted(family) if 114 in t[4:])
    for target, force in ((q11_case, 'ordinary_q11'), (separate_case, 'reuse')):
        try:
            construct(target, force=force)
        except ValueError as exc:
            assert str(exc) == 'complementary pair reused'
        else:
            raise AssertionError('deliberately wrong construction accepted')
    hand = construct(q11_case)
    wrong = [set(b) for b in hand['witness']['bins']]
    a, b = min(wrong[0]), min(wrong[1])
    wrong[0].remove(a)
    wrong[1].remove(b)
    wrong[0].add(b)
    wrong[1].add(a)
    assert Counter(v for bins in wrong for v in bins) == Counter(range(1, 56, 2))
    assert not certificate_ok(wrong, q11_case)
    occupied = set(range(0, 14, 2))
    assert len(occupied) == 7
    assert not any(a not in occupied and a+1 not in occupied for a in range(13))
    results, branches = [], Counter()
    for target in sorted(family):
        if len(results) >= 1000 or time.process_time() - start >= 5:
            status = 'UNKNOWN'
            break
        result = construct(target)
        branches[result['branch']] += 1
        results.append(dict(targets=target, construction=result))
    else:
        status = 'ALL_320'
    print(json.dumps(dict(status=status, results=results, branches=dict(branches),
                          counts_u=dict(counts_u), independent_count=convolution,
                          omitted_q11='REJECTED_PAIR_COLLISION',
                          occupied_pair='REJECTED_PAIR_COLLISION',
                          wrong_sums='REJECTED_COVERAGE_PRESERVED',
                          adjacency_sharpness='SEVEN_USED_CAN_FAIL',
                          cpu_seconds=time.process_time()-start), indent=2))


if __name__ == '__main__':
    main()
