#!/usr/bin/env python3
"""B26 / MI063, preregistered 5df6e91d before execution, 2026-10-16.

Exact six-case boundary question, not a general E28 census. Deviations are
(6,6,-22,p1,...,p5), positive p<=5, sum(p)=10. One negative forces one
8-cycle. Check positive-step orders and their six translations; stop at a
first witness. Predicted all six pass. Count full bounds independently:
420,420,630,630,420,21 orders; 15,246 translations in total.
Caps: 50,000 candidates/case, five process CPU seconds overall; UNKNOWN
on cutoff. Negative result is only a fixed-role one-token-model result.
Controls: direct pair-sum versus folded-label reflection tests; known
B25 shape embeds; bad eight-point shape has no translation despite fitting
the interval; pair reuse and coverage-preserving sum corruption rejected.
Raw JSON outside git.
OUTCOME (2026-10-16, GPT Intel CPU): all six cases WITNESS; 6..18
order/translation candidates each, no cutoff. Bounds independently agree.
All reflection, known-shape, pair-reuse and wrong-sum controls pass.
CPU 0.004333 s. Raw math-instinct-b26-extreme-cycle.json outside git,
SHA256 77d87a69605c01211b4136f92ecb1ee6cc72539ed17c7d4b6b38c47a5ccae2f1.

ADDENDUM BEFORE RECIPE CHECK (MI064): each found shape allowed root 3.
Test a search-free rule on the same six cases only: order the five p's
to avoid partial sum 5, then append 6,6, and translate by 3. If an initial
order hits 5, put unequal entries x,y on opposite sides of that cut and
swap them. All equal means five 2's, which cannot hit 5. Predict exact
pair and certificate success for all six, with at most one boundary swap.
No new cases or expanded search. RECIPE OUTCOME (2026-10-16): all six
literal certificates pass; two orders need the boundary exchange, four
do not. CPU 0.000963 s; raw math-instinct-b26-recipe.json outside git,
SHA256 b6f198834d1944ab0a9c90ba568247253bad0bc60f4cea08f2e3413997b623c6.
"""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations
from math import factorial
import json
import sys
import time

from path_forest_cycle_cover import materialize
from path_forest_receiving_chains import certificate_ok


EXPECTED = [(1, 1, 1, 2, 5), (1, 1, 1, 3, 4), (1, 1, 2, 2, 4),
            (1, 1, 2, 3, 3), (1, 2, 2, 2, 3), (2, 2, 2, 2, 2)]
COUNTS = [420, 420, 630, 630, 420, 21]


def roots(shape):
    assert len(shape) == len(set(shape))
    lo, hi = -min(shape), 27 - max(shape)
    folded, literal = [], []
    for r in range(lo, hi + 1):
        shifted = [r + x for x in shape]
        if len({min(x, 27 - x) for x in shifted}) == len(shifted):
            folded.append(r)
        if not any(a + b == 27 for a, b in combinations(shifted, 2)):
            literal.append(r)
    assert folded == literal
    return folded


def main():
    start = time.process_time()
    deadline = start + 5
    family = [p for p in combinations_with_replacement(range(1, 6), 5) if sum(p) == 10]
    assert family == EXPECTED
    orders_by_case = []
    for p, expected in zip(family, COUNTS):
        positive = (6, 6) + p
        count = factorial(7)
        for n in Counter(positive).values():
            count //= factorial(n)
        orders = sorted(set(permutations(positive)))
        assert len(orders) == count == expected
        orders_by_case.append(orders)
    assert 6 * sum(COUNTS) == 15246
    bad = [0, 1, 2, 5, 9, 12, 13, 14]
    assert roots(bad) == []
    A, B = {0, 1, 6, 7}, {0, 2, 4, 6}
    assert {a + b for a in A for b in B} == set(range(14))
    assert 0 in roots([0, 6, 11, 17, 22])
    results = []
    for p, orders in zip(family, orders_by_case):
        targets = [68] * 3 + [112 + 2 * x for x in p]
        assert sum(targets) == 784
        candidates = 0
        result = None
        for order in orders:
            if candidates + 6 > 50000 or time.process_time() >= deadline:
                result = dict(status='UNKNOWN', targets=targets, candidates=candidates)
                break
            shape = [0]
            for e in order:
                shape.append(shape[-1] + e)
            assert shape[-1] == 22 and len(shape) == 8
            candidates += 6
            translations = roots(shape)
            if not translations:
                continue
            r = translations[0]
            queues = defaultdict(list)
            for i, t in enumerate(targets):
                if i != 2:
                    queues[(t - (56 if i < 2 else 112)) // 2].append(i)
            selected = {}
            for x, e in zip(shape[:-1], order):
                i = queues[e].pop(0)
                selected[i] = r + x
            selected[2] = r + 22
            witness = materialize(targets, selected)
            assert len(witness['cycles']) == 1 and len(witness['cycles'][0]) == 8
            assert certificate_ok(witness['bins'], targets)
            corrupted = [set(b) for b in witness['bins']]
            a, b = max(corrupted[0]), min(corrupted[2])
            assert a > b
            corrupted[0].remove(a); corrupted[2].remove(b)
            corrupted[0].add(b); corrupted[2].add(a)
            assert Counter(v for c in corrupted for v in c) == Counter(range(1, 56, 2))
            assert not certificate_ok(corrupted, targets)
            wrong = dict(selected)
            wrong[7] = 27 - selected[6]
            try:
                materialize(targets, wrong)
            except ValueError as exc:
                assert str(exc) == 'complementary pair reused'
            else:
                raise AssertionError('pair reuse accepted')
            result = dict(status='WITNESS', targets=targets, p=p, order=order,
                          shape=shape, admissible_roots=translations,
                          candidates=candidates, witness=witness)
            break
        if result is None:
            result = dict(status='NO_WITNESS_IN_MODEL', targets=targets,
                          p=p, candidates=candidates)
        results.append(result)
    print(json.dumps(dict(results=results, full_order_counts=COUNTS,
                          full_translation_bound=15246, bad_shape_roots=[],
                          independent_reflection='PASS', pair_reuse='REJECTED',
                          sum_corruption='REJECTED_COVERAGE_PRESERVED',
                          cpu_seconds=time.process_time() - start), indent=2))


def avoid_half(p):
    total = 0
    cut = None
    for i, a in enumerate(p):
        total += a
        if total == 5:
            cut = i + 1
            break
    if cut is None:
        return tuple(p), False
    left, right = list(p[:cut]), list(p[cut:])
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            if x != y:
                return tuple(left[:i] + left[i+1:] + [y, x]
                             + right[:j] + right[j+1:]), True
    raise AssertionError('all equal cannot hit 5 in this five-term family')


def recipe():
    start = time.process_time()
    results = []
    for p in EXPECTED:
        q, swapped = avoid_half(p)
        partial = [0]
        for a in q:
            partial.append(partial[-1] + a)
        assert 5 not in partial and partial[-1] == 10
        assert Counter(q) == Counter(p)
        order = q + (6, 6)
        shape = partial + [16, 22]
        assert 3 in roots(shape)
        targets = [68] * 3 + [112 + 2 * a for a in p]
        queues = defaultdict(list)
        for i, t in enumerate(targets):
            if i != 2:
                queues[(t - (56 if i < 2 else 112)) // 2].append(i)
        selected = {2: 25}
        for x, e in zip(shape[:-1], order):
            selected[queues[e].pop(0)] = 3 + x
        witness = materialize(targets, selected)
        assert certificate_ok(witness['bins'], targets)
        results.append(dict(p=p, q=q, boundary_swap=swapped,
                            selected_indices=sorted(selected.values()), witness=witness))
    print(json.dumps(dict(results=results, status='WITNESS_ALL_SIX',
                          cpu_seconds=time.process_time() - start), indent=2))


if __name__ == '__main__':
    if sys.argv[1:] == ['--recipe']:
        recipe()
    elif not sys.argv[1:]:
        main()
    else:
        raise SystemExit('Only the preregistered fixed modes are available')
