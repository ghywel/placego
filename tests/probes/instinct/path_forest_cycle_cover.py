#!/usr/bin/env python3
"""B25 / MI061; preregistered 801fae29, 2026-10-16.

Only the nine B24 fixtures; keep their two smallest roles fixed. Selected
indices 0..27 have distinct labels min(x,27-x), and x+deviation permutes x.
Predict literal success for the fixed 5+3 hand construction and witnesses
for the nine fixtures within 50,000 nodes/fixture, five process CPU seconds
overall. Limits yield UNKNOWN, never a burning verdict.
Independent checker validates full coverage, targets and cardinalities.
Counterfactuals: repeated pair rejected; coverage-preserving sum corruption
rejected. Unexpected: balanced 98^8 has no single 8-cycle (all steps are
multiples of 7, at most four vertices/residue); disjoint cycles succeed.
No new fixtures, role search, census or cap increase. Raw JSON outside git.
OUTCOME (2026-10-16, GPT Intel CPU): fixed hand 5+3 construction passes;
all nine existing fixtures return WITNESS, 7..25 nodes each, no cutoff.
Balanced single-cycle class exhausted in 64 nodes, no witness; unrestricted
cycles succeed. Both counterfactuals rejected. CPU 0.001639 s.
Raw math-instinct-b25-cycle-cover.json outside git, SHA256
7bda63c36f170e5fdb71da8d4a62d325201cc081b61426a3080d75da3114fec1.
Finite certificates COMPUTED; no general E28 result or independent reader.
"""

from collections import Counter
import json
import time

from path_forest_coupled_chains import FIXTURES
from path_forest_receiving_chains import certificate_ok


class Limit(Exception):
    pass


def setup(targets):
    targets = sorted(targets)
    assert len(targets) == 8 and sum(targets) == 784
    assert all(t % 2 == 0 and 68 <= t <= 122 for t in targets)
    h = [1, 1] + [2] * 6
    e = [(t - 56 * slots) // 2 for t, slots in zip(targets, h)]
    assert sum(e) == 0
    return targets, h, e


def materialize(targets, selected):
    targets, h, e = setup(targets)
    active = {i for i in range(8) if e[i]}
    assert set(selected) == active
    xs = list(selected.values())
    if any(not 0 <= x <= 27 for x in xs):
        raise ValueError('position outside pool')
    labels = [min(x, 27 - x) for x in xs]
    if len(labels) != len(set(labels)):
        raise ValueError('complementary pair reused')
    ends = {i: selected[i] + e[i] for i in active}
    if Counter(ends.values()) != Counter(xs):
        raise ValueError('not a permutation of selected tokens')
    bins = [set() for _ in range(8)]
    for i, x in selected.items():
        bins[i] = {2 * x + 1, 55 - 2 * x}
    free = iter(p for p in range(14) if p not in set(labels))
    for i in range(8):
        while len(bins[i]) < 2 * h[i]:
            p = next(free)
            bins[i].update((2 * p + 1, 55 - 2 * p))
    assert next(free, None) is None
    before = [sorted(b) for b in bins]
    assert Counter(v for b in bins for v in b) == Counter(range(1, 56, 2))
    owner = {x: i for i, x in selected.items()}
    successor = {i: owner[ends[i]] for i in active}
    cycles = []
    unseen = set(active)
    while unseen:
        start = min(unseen)
        cycle, cur = [], start
        while cur in unseen:
            unseen.remove(cur)
            cycle.append(cur)
            cur = successor[cur]
        assert cur == start
        cycles.append(cycle)
    # Remove all selected tokens before redistributing the same multiset.
    for i, x in selected.items():
        assert 2 * x + 1 in bins[i]
        bins[i].remove(2 * x + 1)
    for i, x in ends.items():
        bins[i].add(2 * x + 1)
    assert list(map(sum, bins)) == targets
    assert certificate_ok(bins, targets)
    return dict(selected=selected, deviations=e, successors=successor,
                cycles=cycles, before=before, bins=[sorted(b) for b in bins])


def find(targets, deadline, single=False):
    targets, h, e = setup(targets)
    mask = sum(1 << i for i in range(8) if e[i])
    nodes = 0

    def begin(left, used, selected, cycles):
        if not left:
            return selected, cycles
        i = (left & -left).bit_length() - 1
        for root in range(28):
            answer = place(i, root, root, left, used, selected, [], cycles)
            if answer is not None:
                return answer
        return None

    def place(i, x, root, left, used, selected, path, cycles):
        nonlocal nodes
        if nodes >= 50000 or time.process_time() >= deadline:
            raise Limit
        nodes += 1
        if not 0 <= x <= 27:
            return None
        label = min(x, 27 - x)
        if used & (1 << label):
            return None
        nxt = x + e[i]
        if not 0 <= nxt <= 27:
            return None
        remaining = left ^ (1 << i)
        used2 = used | (1 << label)
        selected2 = dict(selected)
        selected2[i] = x
        path2 = path + [i]
        if nxt == root:
            if single and remaining:
                return None
            return begin(remaining, used2, selected2, cycles + [path2])
        if used2 & (1 << min(nxt, 27 - nxt)):
            return None
        seen_steps = set()
        choices = [j for j in range(8) if remaining & (1 << j)]
        for j in sorted(choices, key=lambda j: (abs(e[j]), j)):
            if e[j] in seen_steps:
                continue
            seen_steps.add(e[j])
            answer = place(j, nxt, root, remaining, used2, selected2, path2, cycles)
            if answer is not None:
                return answer
        return None

    try:
        answer = begin(mask, 0, {}, [])
    except Limit:
        return dict(status='UNKNOWN', nodes=nodes, targets=targets)
    if answer is None:
        return dict(status='NO_WITNESS_IN_CLASS', nodes=nodes, targets=targets)
    selected, cycles = answer
    witness = materialize(targets, selected)
    assert sorted(sorted(c) for c in cycles) == sorted(sorted(c) for c in witness['cycles'])
    return dict(status='WITNESS', nodes=nodes, targets=targets, witness=witness)


def main():
    start = time.process_time()
    deadline = start + 5
    target = [68, 68, 68, 92, 122, 122, 122, 122]
    selected = {0: 0, 4: 6, 1: 11, 5: 17, 2: 22, 6: 2, 7: 7, 3: 12}
    hand = materialize(target, selected)
    assert sorted(map(len, hand['cycles'])) == [3, 5]
    bad = dict(selected)
    bad[7] = 27 - bad[6]
    try:
        materialize(target, bad)
    except ValueError as exc:
        assert str(exc) == 'complementary pair reused'
    else:
        raise AssertionError('pair reuse accepted')
    wrong = [set(b) for b in hand['bins']]
    wrong[0].remove(13)
    wrong[2].remove(1)
    wrong[0].add(1)
    wrong[2].add(13)
    assert Counter(v for b in wrong for v in b) == Counter(range(1, 56, 2))
    assert not certificate_ok(wrong, target)
    single = find([98] * 8, deadline, single=True)
    assert single['status'] == 'NO_WITNESS_IN_CLASS'
    results = []
    for name, targets in FIXTURES:
        result = find(targets, deadline)
        result['name'] = name
        results.append(result)
    print(json.dumps(dict(hand=hand, results=results, single_balanced=single,
                          pair_reuse='REJECTED', sum_corruption='REJECTED_COVERAGE_PRESERVED',
                          cpu_seconds=time.process_time() - start), indent=2))


if __name__ == '__main__':
    main()
