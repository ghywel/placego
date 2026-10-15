#!/usr/bin/env python3
"""B01: independently check a known union-closed obstruction and sampling weights.

Predictions committed before execution: GPT-MATH-INSTINCT.md MI002, 19cdf81e.
Primary construction: Bruhn-Schaudt, arXiv:1309.3297, section 4 small-set example,
its k=3 case only. No novelty or all-size Frankl claim.
P1: 27 distinct sets, union-closed, unique smallest member A of size 3.
P2: counts 13 on A, 23 outside A; abundant elements all outside A.
P3: 8 fibres, sizes 1, six times 3, 8; weighted means 13/27.
Unexpected: equal-fibre means 25/48, on the opposite side of 1/2.
Independent: powerset equality control and direct counts versus fibre weights.
Counterfactual: {empty,{a},{b}} must fail closure; equal fibre weights must
not reproduce the original family law. Stop on any failed must-hold.
OUTCOME MI003: all controls pass; 27 sets, 729 ordered pair unions, counts
13 on the three-element smallest member and 23 on the six other elements.
Weighted frequency 13/27 versus equal-fibre frequency 25/48; powerset equality
control passes and the nonclosed counterfactual is rejected. Known example,
not a Frankl counterexample or a new theorem.
RUN: python3 tests/probes/instinct/union_closed_fibres.py
"""
from fractions import Fraction
from itertools import combinations
import json


def powerset(values):
    values = tuple(values)
    return {frozenset(c) for k in range(len(values) + 1)
            for c in combinations(values, k)}


def obstruction():
    inside = frozenset(range(3))
    outside = frozenset(range(3, 9))
    family = {inside}
    for i in range(3):
        for missing in (3 + 2 * i, 4 + 2 * i):
            d = outside - {missing}
            family.update((d, d | {i}, d | inside))
    family.update(outside | c for c in powerset(inside))
    # Generate with ordinary sets; verify and analyse through integer masks.
    return {sum(1 << i for i in s) for s in family}, 0b111


def closure_failure(family):
    return next(((s, t, s | t) for s in family for t in family
                 if s | t not in family), None)


def analyse(family, a, width):
    assert family and closure_failure(family) is None
    fibres = {}
    for s in family:
        fibres.setdefault(s & ~a, set()).add(s & a)
    for trace in fibres.values():
        assert a in trace and closure_failure(trace) is None
    # Cross-fibre unions are stronger than closure of the individual fibres.
    for d, trace in fibres.items():
        for e, other in fibres.items():
            assert all(c | z in fibres[d | e] for c in trace for z in other)
    direct = [sum(bool(s & (1 << i)) for s in family) for i in range(width)]
    weighted, equal = {}, {}
    for i in range(width):
        if not (a & (1 << i)):
            continue
        conditional = {d: Fraction(sum(bool(c & (1 << i)) for c in trace), len(trace))
                       for d, trace in fibres.items()}
        weighted[i] = sum((Fraction(len(fibres[d]), len(family)) * q
                           for d, q in conditional.items()), Fraction())
        equal[i] = sum(conditional.values(), Fraction()) / len(fibres)
        assert weighted[i] == Fraction(direct[i], len(family))
    return fibres, direct, weighted, equal


def main():
    family, a = obstruction()
    assert len(family) == 27
    assert [s for s in family if s.bit_count() == min(t.bit_count() for t in family)] == [a]
    fibres, counts, weighted, equal = analyse(family, a, 9)
    assert counts == [13] * 3 + [23] * 6
    assert sorted(map(len, fibres.values())) == [1] + [3] * 6 + [8]
    assert set(weighted.values()) == {Fraction(13, 27)}
    assert set(equal.values()) == {Fraction(25, 48)}
    assert all(weighted[i] < Fraction(1, 2) < equal[i] for i in weighted)
    assert {i for i, c in enumerate(counts) if 2 * c >= len(family)} == set(range(3, 9))
    _, cube_counts, cube_weighted, cube_equal = analyse(set(range(8)), 0b011, 3)
    assert cube_counts == [4, 4, 4]
    assert set(cube_weighted.values()) == set(cube_equal.values()) == {Fraction(1, 2)}
    bad = closure_failure({0, 1, 2})
    assert bad is not None and bad[2] == 3
    print(json.dumps(dict(
        family_size=len(family), ground_size=9, unique_smallest_size=3,
        counts=counts, fibre_sizes=sorted(map(len, fibres.values())),
        weighted_inside=str(weighted[0]), equal_fibre_inside=str(equal[0]),
        independent_powerset_control='PASS', nonclosed_counterfactual='REJECTED',
        pair_unions_checked=len(family) ** 2,
        cross_fibre_compatibility='PASS', verdict='ALL CONTROLS PASS'), indent=2))


if __name__ == '__main__':
    main()
