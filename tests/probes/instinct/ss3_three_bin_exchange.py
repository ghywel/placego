#!/usr/bin/env python3
"""B139 / MI296: audit the explicit three-bin augmentation, not general SS3.

RUN-ON: GPT Intel CPU, one process; no solver or random selection.
COMMAND: python3 tests/probes/instinct/ss3_three_bin_exchange.py --output /tmp/math-instinct-b139-three-bin.json
PREDICTIONS: for n=6..9, sorted sizes>=2, every owner word and every
permutation of deviations (D,0,-D), D=1,2,3, retain SS-feasible targets.
The fixed hand constructor must decrease L1 by>=2 in <=4 adjacent swaps,
never increasing it; D=1 must finish exactly. No BFS/search fallback.
REFERENCE: literal independent count/sum/path checker; complete feasible
target sets from separate owner-word enumeration for n=6..8.
CF: singleton SS-feasible n7 target(14,4,3), sizes(3,3,1), is impossible.
UNEXPECTED: every constructed path also checks under index reflection
and translation by -11, with the corresponding prescribed sums.
CAPS: 15 CPU /25 wall seconds,128 MiB,30 wall watchdog; stop on first
failure, no fixes/retries/expanded domain. Raw report remains outside git.
No finite result proves the universal candidate or its novelty.

OUTCOME B139 (2026-10-17; prereg9f1c5ae6; MI297): PASS one invocation.
4976 primary words/89568 screens/82284 admitted formula calls; all seven
branches occur, including42 calls of each four-swap residual repair.
1280 independent reference words; literal/reflection/translation and
singleton-negative controls pass. CPU4.277403s,wall4.282420s,RSS16625664B;
no cap,retry or expansion. Universal candidate remains PROOF-SKETCH.
"""

import argparse
from collections import Counter
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import resource
import sys
import time


def ss(n, sizes, targets):
    if sum(sizes) != n or sum(targets) != n * (n - 1) // 2:
        return False
    for mask in range(1, 8):
        c = sum(sizes[j] for j in range(3) if mask & (1 << j))
        s = sum(targets[j] for j in range(3) if mask & (1 << j))
        lo = c * (c - 1) // 2
        if not lo <= s <= c * (n - 1) - lo:
            return False
    return True


def augment(word, targets):
    """Return the hand formula's adjacent EDGE indices and branch name."""
    n = len(word)
    sizes = tuple(word.count(j) for j in range(3))
    if set(word) != {0, 1, 2} or min(sizes) < 2 or not ss(n, sizes, targets):
        raise ValueError('outside the three-bin candidate hypotheses')
    sums = [sum(x for x, b in enumerate(word) if b == j) for j in range(3)]
    delta = [sums[j] - targets[j] for j in range(3)]
    if not any(delta):
        return [], 'already_exact'
    for x in range(n - 1):
        if delta[word[x + 1]] > 0 > delta[word[x]]:
            return [x], 'direct'
    positive = [j for j in range(3) if delta[j] > 0]
    negative = [j for j in range(3) if delta[j] < 0]
    assert len(positive) == len(negative) == 1, (word, delta)
    a, c = positive[0], negative[0]
    b = 3 - a - c
    assert delta[b] == 0 and delta[a] == -delta[c]
    ba = [x for x in range(n - 1) if word[x:x + 2] == (b, a)]
    cb = [x for x in range(n - 1) if word[x:x + 2] == (c, b)]
    assert ba and cb, (word, delta)
    for x in ba:
        for y in cb:
            if abs(x - y) > 1:
                return [x, y], 'disjoint'
    assert len(ba) == len(cb) == 1 and cb[0] == ba[0] - 1
    p = ba[0]
    if delta[a] >= 2:
        return [p, p - 1], 'overlap_large_error'
    assert delta[a] == 1
    for x in range(n - 1):
        disjoint = x + 1 < p - 1 or x > p + 1
        if disjoint and word[x:x + 2] == (b, c):
            return [p - 1, p, x], 'reverse_cb'
    for x in range(n - 1):
        disjoint = x + 1 < p - 1 or x > p + 1
        if disjoint and word[x:x + 2] == (a, b):
            return [p, p - 1, x], 'reverse_ba'
    # With no disjoint reverse edge, the complete owner word has one of
    # the two residual shapes in MI295, not just a matching local triple.
    if word[0] == a:
        left = next(x for x, owner in enumerate(word) if owner != a)
        middle = p - left
        right = n - p - 2
        assert left >= 1 and middle >= 2 and right >= 1
        assert word == (a,) * left + (c,) * middle + (b, a) + (b,) * right
        return [p, p - 1, p, left - 1], 'four_left'
    left = p - 1
    middle = sizes[a]
    right = sizes[c] - 1
    assert left >= 1 and middle >= 2 and right >= 1
    assert word == (b,) * left + (c, b) + (a,) * middle + (c,) * right
    return [p - 1, p, p - 1, p + middle], 'four_right'


def partitions(n, sizes):
    for first in combinations(range(n), sizes[0]):
        first_set = set(first)
        rest = tuple(x for x in range(n) if x not in first_set)
        for second in combinations(rest, sizes[1]):
            second_set = set(second)
            yield tuple(0 if x in first_set else 1 if x in second_set else 2
                        for x in range(n))


def literal_check(word, targets, steps, offset=0):
    """Separate arithmetic: no calls to augment, ss, or its sum routine."""
    current = list(word)
    sizes = tuple(current.count(j) for j in (0, 1, 2))
    values = tuple(range(offset, offset + len(word)))
    errors = []
    for step in [None] + steps:
        if step is not None:
            assert 0 <= step < len(current) - 1
            assert current[step] != current[step + 1]
            current[step], current[step + 1] = current[step + 1], current[step]
        assert tuple(current.count(j) for j in (0, 1, 2)) == sizes
        actual = [0, 0, 0]
        for value, owner in zip(values, current):
            actual[owner] += value
        errors.append(sum(abs(x - y) for x, y in zip(actual, targets)))
    assert all(y <= x for x, y in zip(errors, errors[1:])), errors
    assert 1 <= len(steps) <= 4 and errors[-1] <= errors[0] - 2, errors
    return tuple(current), errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    cpu0, wall0 = time.process_time(), time.monotonic()
    resource.setrlimit(resource.RLIMIT_CPU, (16, 17))
    branch_counts = Counter()
    counts = Counter()
    first_examples = {}

    def caps():
        cpu, wall = time.process_time() - cpu0, time.monotonic() - wall0
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
        if cpu > 15 or wall > 25 or rss_bytes > 128 * 1024 * 1024:
            raise RuntimeError(('registered cap', cpu, wall, rss_bytes))

    size_vectors = [(n, (a, b, n - a - b)) for n in range(6, 10)
                    for a in range(2, n) for b in range(a, n)
                    if b <= n - a - b]
    for n, sizes in size_vectors:
        # Reference completeness uses independent product enumeration, not
        # the combination enumerator or the constructor's formulas.
        feasible = set()
        if n <= 8:
            reference_count = 0
            for w in product(range(3), repeat=n):
                if tuple(w.count(j) for j in range(3)) == sizes:
                    reference_count += 1
                    feasible.add(tuple(sum(x for x in range(n) if w[x] == j)
                                       for j in range(3)))
            assert reference_count == math.factorial(n) // math.prod(
                math.factorial(c) for c in sizes)
            counts['reference_states'] += reference_count
        state_count = 0
        for word in partitions(n, sizes):
            state_count += 1
            actual = tuple(sum(x for x, b in enumerate(word) if b == j)
                           for j in range(3))
            for a, b, c in permutations(range(3)):
                for magnitude in (1, 2, 3):
                    targets = list(actual)
                    targets[a] -= magnitude
                    targets[c] += magnitude
                    targets = tuple(targets)
                    counts['screened'] += 1
                    if not ss(n, sizes, targets):
                        continue
                    steps, branch = augment(word, targets)
                    _, errors = literal_check(word, targets, steps)
                    if magnitude == 1:
                        assert errors[-1] == 0
                        if n <= 8:
                            assert targets in feasible
                    # Reflect THE PATH, not just a yes/no result or count.
                    reflected = tuple(reversed(word))
                    reflected_targets = tuple(sizes[j] * (n - 1) - targets[j]
                                              for j in range(3))
                    _, reflected_errors = literal_check(
                        reflected, reflected_targets, [n - 2 - x for x in steps])
                    assert reflected_errors == errors
                    shifted_targets = tuple(targets[j] - 11 * sizes[j]
                                            for j in range(3))
                    _, shifted_errors = literal_check(word, shifted_targets, steps, -11)
                    assert shifted_errors == errors
                    counts['passed'] += 1
                    branch_counts[branch] += 1
                    first_examples.setdefault(branch, {'word': word, 'targets': targets,
                                                      'steps': steps, 'errors': errors})
            caps()
        expected = math.factorial(n) // math.prod(math.factorial(c) for c in sizes)
        assert state_count == expected
        counts['primary_states'] += state_count
    # Required mechanism coverage: ordinary, shared-token, reverse relay,
    # and BOTH four-swap residual shapes must actually be exercised.
    assert set(branch_counts) == {'direct', 'disjoint', 'overlap_large_error',
                                 'reverse_cb', 'reverse_ba', 'four_left', 'four_right'}
    negative = (1, 1, 2, 1, 0, 0, 0)
    assert ss(7, (3, 3, 1), (14, 4, 3))
    try:
        augment(negative, (14, 4, 3))
    except ValueError:
        pass
    else:
        raise AssertionError('singleton control admitted')
    # Full independent enumeration of the impossible singleton control.
    assert not any(tuple(w.count(j) for j in range(3)) == (3, 3, 1)
                   and tuple(sum(x for x in range(7) if w[x] == j)
                             for j in range(3)) == (14, 4, 3)
                   for w in product(range(3), repeat=7))
    caps()
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    out = {'counts': dict(counts), 'branches': dict(branch_counts),
           'first_examples': first_examples, 'negative_control': 'SS true, impossible, rejected',
           'cpu_seconds': time.process_time() - cpu0,
           'wall_seconds': time.monotonic() - wall0,
           'peak_rss_bytes': rss if sys.platform == 'darwin' else rss * 1024,
           'status': 'PASS: fixed formula audit only; universal proof still unreviewed'}
    Path(args.output).write_text(json.dumps(out, sort_keys=True, indent=2) + '\n')
    print(json.dumps(out, sort_keys=True))


if __name__ == '__main__':
    main()
