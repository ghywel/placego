#!/usr/bin/env python3
"""Fixed SS3 neutral-exchange diagnostic; MI293 preregistration.

RUN-ON: GPT CPU, one process. No solver, random targets, or sample expansion.
COMMAND: python3 tests/probes/instinct/ss3_neutral_diagnostic.py --output /tmp/math-instinct-b138-neutral.json
COST/CAPS: 5 CPU seconds, 10 wall seconds, 96 MiB; stop on control failure.
P1 controls: partition counts 1680,1680,20,2520; independent goal/closure maps agree.
P2 blind: every partition of the fixed n9 sizes(3,3,3), target(20,6,10),
         reaches a target via adjacent-value swaps without increasing L1 error.
CF: strict pair-swap descent from MI292's initial partition must FAIL.
Unexpected: reflect every index and target; reachable sets must correspond.
Reference enumerates all owner words; primary enumerates disjoint combinations.
Reference closure uses synchronous full-set iteration, not primary reverse BFS.
No changes/retries after a failed prediction. A failure is retained, not repaired.
"""

import argparse
from collections import deque
from itertools import combinations, product
import json
import math
from pathlib import Path
import resource
import sys
import time


def partition_words(n, sizes):
    word = [-1] * n

    def rec(rest, bin_id):
        if bin_id == len(sizes) - 1:
            assert len(rest) == sizes[bin_id]
            for x in rest:
                word[x] = bin_id
            yield tuple(word)
            return
        for chosen in combinations(rest, sizes[bin_id]):
            for x in chosen:
                word[x] = bin_id
            chosen_set = set(chosen)
            yield from rec(tuple(x for x in rest if x not in chosen_set), bin_id + 1)

    yield from rec(tuple(range(n)), 0)


def sums_of(word, k):
    out = [0] * k
    for x, b in enumerate(word):
        out[b] += x
    return tuple(out)


def energy(word, target):
    return sum(abs(a - b) for a, b in zip(sums_of(word, len(target)), target))


def neighbors(word):
    for x in range(len(word) - 1):
        if word[x] != word[x + 1]:
            other = list(word)
            other[x], other[x + 1] = other[x + 1], other[x]
            yield tuple(other)


def ss(n, sizes, targets):
    for mask in range(1, 1 << len(sizes)):
        c = sum(sizes[j] for j in range(len(sizes)) if mask >> j & 1)
        s = sum(targets[j] for j in range(len(sizes)) if mask >> j & 1)
        low = c * (c - 1) // 2
        if not low <= s <= c * (n - 1) - low:
            return False
    return True


def diagnose(n, sizes, target):
    states = set(partition_words(n, sizes))
    expected = math.factorial(n) // math.prod(math.factorial(c) for c in sizes)
    assert len(states) == expected
    values = {w: energy(w, target) for w in states}
    goals = {w for w in states if values[w] == 0}
    depth = {w: 0 for w in goals}
    queue = deque(goals)
    while queue:
        current = queue.popleft()
        for previous in neighbors(current):
            if previous not in depth and values[previous] >= values[current]:
                depth[previous] = depth[current] + 1
                queue.append(previous)

    # Separate enumeration and arithmetic; do not call primary sums/energy here.
    reference = {}
    for w in product(range(len(sizes)), repeat=n):
        if tuple(w.count(b) for b in range(len(sizes))) != sizes:
            continue
        bin_sums = tuple(sum(x for x in range(n) if w[x] == b) for b in range(len(sizes)))
        reference[w] = sum(abs(bin_sums[b] - target[b]) for b in range(len(sizes)))
    assert reference == values
    ref_goals = {w for w, e in reference.items() if e == 0}
    assert ref_goals == goals
    reachable = set(ref_goals)
    rounds = 0
    while True:
        added = set()
        for w, e in reference.items():
            if w in reachable:
                continue
            for x in range(n - 1):
                if w[x] == w[x + 1]:
                    continue
                v = w[:x] + (w[x + 1], w[x]) + w[x + 2:]
                if v in reachable and reference[v] <= e:
                    added.add(w)
                    break
        if not added:
            break
        reachable.update(added)
        rounds += 1
    assert reachable == set(depth)
    assert rounds == max(depth.values(), default=0)
    missing = sorted(states - reachable)
    representative = missing[0] if missing else None
    return {
        'n': n, 'sizes': sizes, 'target': target, 'SS': ss(n, sizes, target),
        'states': len(states), 'goals': len(goals), 'reachable': len(reachable),
        'unreachable': len(missing), 'max_shortest_nonincreasing_path': max(depth.values(), default=0),
        'first_unreachable_bins': None if representative is None else
            [[x for x in range(n) if representative[x] == b] for b in range(len(sizes))],
        'independent_complete_maps_agree': True,
    }, reachable


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU, (5, 6))
    started = time.monotonic()
    cpu = time.process_time()
    cases = [(9, (3, 3, 3), (20, 6, 10)),
             (9, (3, 3, 3), (4, 18, 14)),
             (6, (3, 3), (7, 8)),
             (8, (2, 2, 2, 2), (2, 6, 8, 12))]
    reports, reachable_sets = [], []
    for n, sizes, targets in cases:
        report, reachable = diagnose(n, sizes, targets)
        reports.append(report)
        reachable_sets.append(reachable)
        assert time.monotonic() - started < 10, 'WALL_CAP'
    assert [r['states'] for r in reports] == [1680, 1680, 20, 2520]
    assert all(r['SS'] for r in reports)
    assert all(reports[i]['goals'] > 0 for i in (0, 1, 2))
    assert reports[3]['goals'] == reports[3]['reachable'] == 0
    assert {tuple(reversed(w)) for w in reachable_sets[0]} == reachable_sets[1]

    initial = (1, 1, 2, 2, 2, 1, 0, 0, 0)
    target = cases[0][2]
    assert energy(initial, target) == 2
    improving = []
    for x in range(9):
        for y in range(x + 1, 9):
            if initial[x] == initial[y]:
                continue
            w = list(initial)
            w[x], w[y] = w[y], w[x]
            if energy(tuple(w), target) < 2:
                improving.append((x, y))
    assert not improving, 'Counterfactual strict descent unexpectedly passes'
    w = list(initial)
    repair_energies = []
    for x, y in ((4, 5), (5, 6), (1, 2)):
        assert w[x] != w[y]
        w[x], w[y] = w[y], w[x]
        repair_energies.append(energy(tuple(w), target))
    assert repair_energies == [2, 2, 0]
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        peak *= 1024
    assert peak <= 96 * 1024 * 1024, 'RSS_CAP'
    result = {'status': 'COMPLETED', 'cases': reports,
              'P1_controls': True,
              'P2_fixed_n9_all_states_reach_goal': reports[0]['unreachable'] == 0,
              'CF_strict_descent_fails': True, 'unexpected_reflection': True,
              'literal_repair_energies': repair_energies,
              'cpu_seconds': time.process_time() - cpu,
              'wall_seconds': time.monotonic() - started, 'peak_RSS_bytes': peak}
    Path(args.output).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
