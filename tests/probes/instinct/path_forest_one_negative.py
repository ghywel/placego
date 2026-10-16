#!/usr/bin/env python3
"""B27 / MI066, preregistered 98702aba before execution, 2026-10-16.

Formula-only validation for sorted even E28 tuples with t4>=112. No search
for cycles, orders, roots or roles. Predict 271 inputs from independent
parameter and low-triple/high-five counting, and a certificate for each.
One exceptional input uses order 6,5,6,5. All other high-q inputs avoid
one prefix via at most one boundary exchange; low-q roots are 0 or 1.
Controls: omitting low-q root correction and exception ordering must cause
pair collisions. Literal allocator plus independent full checker validate
every formula output. Caps: 1,000 inputs, five process CPU seconds overall;
count disagreement or any formula failure stops the run. Raw JSON outside
git.
OUTCOME (2026-10-16, GPT Intel CPU): parameter and independent
low-triple/high-five domains agree exactly, 271 inputs. All formula
certificates pass; branches low_r0=161, low_r1=15, high=94, exception=1.
47 high orders use the prefix-boundary exchange. Both omitted-correction
counterfactuals rejected for pair collision. CPU 0.033113 s, no cutoff.
Raw math-instinct-b27-one-negative.json outside git, SHA256
e053622c52f595847795530491a93b923b18fff740fc1c889da44d4703a92d33.
Finite witnesses COMPUTED; uniform hand proof awaits independent review.
"""

from collections import Counter, defaultdict
from itertools import combinations_with_replacement
import json
import time

from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok


def avoid_level(positive, level):
    total, cut = 0, None
    for i, a in enumerate(positive):
        total += a
        if total == level:
            cut = i + 1
            break
    if cut is None:
        return tuple(positive), False
    left, right = list(positive[:cut]), list(positive[cut:])
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            if x != y:
                return tuple(left[:i] + left[i+1:] + [y, x]
                             + right[:j] + right[j+1:]), True
    return None, False


def construct(targets, force=None):
    targets = tuple(targets)
    assert list(targets) == sorted(targets) and len(targets) == 8
    assert sum(targets) == 784 and targets[3] >= 112
    assert all(t % 2 == 0 and 68 <= t <= 122 for t in targets)
    u, v = ((targets[i] - 56) // 2 for i in (0, 1))
    p = tuple((t - 112) // 2 for t in targets[3:])
    q = sum(p)
    w = u + v + q
    assert targets[2] == 112 - 2 * w
    positive = tuple(x for x in p if x)
    swapped = False
    if q <= 6:
        order = positive + (u, v)
        r = int((q + u) + w == 27)
        branch = 'low_r' + str(r)
        if force == 'r0':
            r = 0
    elif u == v == 6 and positive == (5, 5) and force != 'ordinary_exception':
        order, r, branch = (6, 5, 6, 5), 0, 'exception'
    else:
        level = q - u + 1
        adjusted, swapped = avoid_level(positive, level)
        if force == 'ordinary_exception':
            adjusted = positive
        assert adjusted is not None
        running = 0
        for a in adjusted:
            running += a
            if force != 'ordinary_exception':
                assert running != level
        order, r, branch = adjusted + (u, v), 13 - q, 'high'
    shape = [0]
    for a in order:
        shape.append(shape[-1] + a)
    assert shape[-1] == w
    queues = defaultdict(list)
    queues[u].append(0)
    queues[v].append(1)
    for i, a in enumerate(p, 3):
        if a:
            queues[a].append(i)
    selected = {2: r + w}
    for x, a in zip(shape[:-1], order):
        selected[queues[a].pop(0)] = r + x
    assert all(not items for items in queues.values())
    witness = materialize(targets, selected)
    assert certificate_ok(witness['bins'], targets)
    return dict(u=u, v=v, p=p, q=q, root=r, branch=branch,
                prefix_swap=swapped, order=order, witness=witness)


def main():
    start = time.process_time()
    deadline = start + 5
    parameter_family = set()
    for u in range(6, 10):
        for v in range(u, 12):
            for p in combinations_with_replacement(range(6), 5):
                q = sum(p)
                if u + 2 * v + q <= 28:
                    parameter_family.add((56 + 2*u, 56 + 2*v, 112 - 2*(u+v+q))
                                         + tuple(112 + 2*a for a in p))
    lows, highs = defaultdict(list), defaultdict(list)
    for triple in combinations_with_replacement(range(68, 112, 2), 3):
        lows[sum(triple)].append(triple)
    for five in combinations_with_replacement(range(112, 123, 2), 5):
        highs[sum(five)].append(five)
    direct_family = {low + high for s, values in lows.items()
                     for low in values for high in highs.get(784-s, [])}
    convolution_count = sum(len(values) * len(highs.get(784-s, []))
                            for s, values in lows.items())
    assert len(parameter_family) == len(direct_family) == convolution_count == 271
    assert parameter_family == direct_family
    exceptional = (68, 68, 68, 112, 112, 112, 122, 122)
    root_case = (68, 70, 78, 112, 112, 112, 112, 120)
    for target, force in ((root_case, 'r0'), (exceptional, 'ordinary_exception')):
        try:
            construct(target, force=force)
        except ValueError as exc:
            assert str(exc) == 'complementary pair reused'
        else:
            raise AssertionError('necessary correction omitted but accepted')
    results, branches = [], Counter()
    for target in sorted(parameter_family):
        if len(results) >= 1000 or time.process_time() >= deadline:
            status = 'UNKNOWN'
            break
        construction = construct(target)
        branches[construction['branch']] += 1
        results.append(dict(targets=target, construction=construction))
    else:
        status = 'WITNESS_ALL_271'
        assert branches['exception'] == 1 and branches['low_r1'] > 0
    print(json.dumps(dict(status=status, independent_count=convolution_count,
                          results=results, branches=dict(branches),
                          wrong_low_root='REJECTED_PAIR_COLLISION',
                          wrong_exception='REJECTED_PAIR_COLLISION',
                          cpu_seconds=time.process_time()-start), indent=2))


if __name__ == '__main__':
    main()
