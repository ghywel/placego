#!/usr/bin/env python3
"""B141/MI300: fixed four-state all-pair energy barrier; no new census.

RUN-ON: GPT Intel CPU, one process.
COMMAND: python3 tests/probes/instinct/ss3_pair_barrier.py --output /tmp/math-instinct-b141-barrier.json
P1: n12 sizes3^4,target(23,7,26,10) obeys SS with minimum proper slack2;
    the explicitly supplied target partition is literal and complete.
P2: ALL nonincreasing single-token swaps, including nonadjacent values,
    leave the start in exactly FOUR states, every one with L1 error2.
CF: target existence does NOT imply such monotone pair-swap reachability.
P3: supplied three-swap path has energies2,2,4,0; its last two disjoint
    swaps as ONE two-for-two exchange give energies2,2,0.
REFERENCE: per-pair affine change from current bin deviations; compare
    with direct full-sum recomputation after swapping actual owners.
UNEXPECTED: complete closure/allowed-neighbor maps reflect and translate.
CAPS: 5 CPU /10 wall seconds /64 MiB;12 wall external watchdog.
Stop first failure/cap;no fix/retry/expanded graph or two-for-two search.

OUTCOME B141 (2026-10-17;prereg5f6823f0;MI301): all controls PASS,
one invocation. Exactly4 closed states/error2/two allowed neighbors,
all648 literal-affine pair checks/reflection/translation maps agree.
Goal witness exists;three-swap escape errors2,2,4,0,atomic2-for-2 gives
2,2,0. Exact minimum single-token path barrier4. CPU0.002579s,
wall0.002577s,RSS16437248B;no cap/retry/expansion. General SS3 untouched;
universal monotone single-token strategy is refuted and parked.
"""

import argparse
from collections import deque
from itertools import combinations
import json
from pathlib import Path
import resource
import sys
import time


TARGET = (23, 7, 26, 10)
START = (1, 1, 3, 3, 3, 2, 1, 0, 0, 0, 2, 2)
GOAL_BINS = ((4, 8, 11), (0, 1, 6), (7, 9, 10), (2, 3, 5))


def swapped(w, x, y):
    assert w[x] != w[y]
    v = list(w)
    v[x], v[y] = v[y], v[x]
    return tuple(v)


def deviations(w, target, offset):
    sums = [0] * 4
    for x, b in enumerate(w):
        sums[b] += x + offset
    return tuple(sums[b] - target[b] for b in range(4))


def closure(start, target, offset):
    seen, queue = {start}, deque([start])
    allowed = {}
    pair_checks = 0
    while queue:
        w = queue.popleft()
        delta = deviations(w, target, offset)
        old_error = sum(map(abs, delta))
        allowed[w] = set()
        tested = 0
        for x, y in combinations(range(12), 2):
            if w[x] == w[y]:
                continue
            tested += 1
            other = swapped(w, x, y)
            literal = sum(map(abs, deviations(other, target, offset)))
            # Reference arithmetic changes ONLY the two original bin sums.
            a, b = w[x], w[y]
            da = delta[a] + (y - x)
            db = delta[b] - (y - x)
            reference = sum(abs(delta[j]) for j in range(4) if j not in (a, b))
            reference += abs(da) + abs(db)
            assert literal == reference
            assert tuple(other.count(j) for j in range(4)) == (3, 3, 3, 3)
            if literal <= old_error:
                allowed[w].add(other)
                if other not in seen:
                    seen.add(other)
                    assert len(seen) <= 4, ('prediction fails; retained first escape', other)
                    queue.append(other)
        assert tested == 54
        pair_checks += tested
    assert len(seen) == 4 and all(len(v) == 2 for v in allowed.values())
    assert all(sum(map(abs, deviations(w, target, offset))) == 2 for w in seen)
    return seen, allowed, pair_checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    cpu0, wall0 = time.process_time(), time.monotonic()
    resource.setrlimit(resource.RLIMIT_CPU, (6, 7))
    proper_slacks = []
    for mask in range(1, 16):
        count = 3 * mask.bit_count()
        value = sum(TARGET[j] for j in range(4) if mask & (1 << j))
        lo = count * (count - 1) // 2
        hi = count * 11 - lo
        assert lo <= value <= hi
        if mask != 15:
            proper_slacks.extend((value - lo, hi - value))
    assert min(proper_slacks) == 2
    flat = [x for part in GOAL_BINS for x in part]
    assert sorted(flat) == list(range(12))
    assert tuple(len(part) for part in GOAL_BINS) == (3,) * 4
    assert tuple(sum(part) for part in GOAL_BINS) == TARGET
    goal = tuple(next(j for j in range(4) if x in GOAL_BINS[j]) for x in range(12))
    states, neighbors, checks = closure(START, TARGET, 0)
    expected = {START, swapped(START, 4, 5), swapped(START, 6, 7),
                swapped(swapped(START, 4, 5), 6, 7)}
    assert states == expected and goal not in states
    # Whole maps, rather than agreement of their cardinalities.
    reflected = tuple(reversed(START))
    reflected_targets = tuple(33 - s for s in TARGET)
    r_states, r_neighbors, r_checks = closure(reflected, reflected_targets, 0)
    assert r_states == {tuple(reversed(w)) for w in states}
    for w in states:
        assert r_neighbors[tuple(reversed(w))] == {tuple(reversed(v)) for v in neighbors[w]}
    shifted_targets = tuple(s - 33 for s in TARGET)
    t_states, t_neighbors, t_checks = closure(START, shifted_targets, -11)
    assert t_states == states and t_neighbors == neighbors
    current = START
    errors = [sum(map(abs, deviations(current, TARGET, 0)))]
    for x, y in ((4, 5), (4, 7), (9, 11)):
        current = swapped(current, x, y)
        errors.append(sum(map(abs, deviations(current, TARGET, 0))))
    assert current == goal and errors == [2, 2, 4, 0]
    intermediate = swapped(START, 4, 5)
    compound = swapped(swapped(intermediate, 4, 7), 9, 11)
    assert compound == goal
    assert sum(map(abs, deviations(intermediate, TARGET, 0))) == 2
    assert deviations(compound, TARGET, 0) == (0, 0, 0, 0)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
    cpu, wall = time.process_time() - cpu0, time.monotonic() - wall0
    assert cpu <= 5 and wall <= 10 and rss_bytes <= 64 * 1024 * 1024
    result = {'status': 'PASS: monotone single-token swap reachability REFUTED',
              'n': 12, 'sizes': [3] * 4, 'targets': TARGET,
              'start': START, 'closed_states': sorted(states),
              'allowed_neighbors_per_state': 2, 'pair_checks_per_arm': checks,
              'total_pair_checks': checks + r_checks + t_checks,
              'minimum_proper_ss_slack': min(proper_slacks),
              'goal_bins': GOAL_BINS, 'escape_errors': errors,
              'compound_errors': [2, 2, 0], 'exact_minimum_pair_path_barrier': 4,
              'cpu_seconds': cpu, 'wall_seconds': wall, 'peak_rss_bytes': rss_bytes}
    Path(args.output).write_text(json.dumps(result, sort_keys=True, indent=2) + '\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
