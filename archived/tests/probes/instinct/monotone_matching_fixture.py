#!/usr/bin/env python3
"""B07: one preregistered containment-matching fixture, not a family census.

Predictions/record search: GPT-MATH-INSTINCT.md MI021, commit aa0ea1be.
The hand construction was already seen before preregistration. This audit is
not a blind prediction. Expect 17 intersection-closed sets, frequencies
(5,7,7,7,7), and maximum downward matching 4 rather than 5 at x.
Counterfactual: adjoining {a,b} permits a matching of all five inputs.
Controls: independent frozenset construction, explicit matching certificates,
and powerset deletion. Unexpected check: complement gives union closure,
frequencies (12,10,10,10,10), and the same failed containment matching.
Stop after this fixture and controls. No search, optimization, or randomness.
"""

import itertools
import json


LABELS = ("x", "a", "b", "c", "d")
X, A, B = 1, 2 | 4, 8 | 16
E = X | A | B


def subsets(mask):
    return [s for s in range(E + 1) if s & ~mask == 0]


def powerset_names(names):
    return [frozenset(c) for k in range(len(names) + 1)
            for c in itertools.combinations(names, k)]


def mask_of(s):
    return sum(1 << LABELS.index(name) for name in s)


def check_closed(family, operation):
    assert all(operation(s, t) in family for s in family for t in family)


def frequencies(family):
    return [sum(bool(s & (1 << i)) for s in family)
            for i in range(len(LABELS))]


def matching(left, right, allowed):
    """Augmenting paths; return source -> target and check the certificate."""
    adjacency = {s: [t for t in sorted(right) if allowed(s, t)]
                 for s in sorted(left)}
    owner = {}

    def augment(s, seen):
        for t in adjacency[s]:
            if t in seen:
                continue
            seen.add(t)
            if t not in owner or augment(owner[t], seen):
                owner[t] = s
                return True
        return False

    for s in sorted(left):
        augment(s, set())
    result = {s: t for t, s in owner.items()}
    assert len(result) == len(owner)
    assert all(s in left and t in right and allowed(s, t)
               for s, t in result.items())
    return result


def check_certificate(certificate, left, right, allowed):
    assert set(certificate) <= left
    assert len(set(certificate.values())) == len(certificate)
    assert all(t in right and allowed(s, t)
               for s, t in certificate.items())


def main():
    lower = {j | k for j in subsets(A) if j != A for k in subsets(B)}
    core = {X | j for j in subsets(A)}
    family = lower | core | {E}
    assert len(lower) == 12 and len(core) == 4 and len(family) == 17

    # Separate representation and construction, with no mask operations.
    named = {j | k for j in powerset_names(("a", "b"))
             if j != frozenset(("a", "b"))
             for k in powerset_names(("c", "d"))}
    named |= {frozenset(("x",)) | j
              for j in powerset_names(("a", "b"))}
    named.add(frozenset(LABELS))
    assert {mask_of(s) for s in named} == family
    assert all(s & t in named for s in named for t in named)
    check_closed(family, lambda s, t: s & t)
    assert frequencies(family) == [5, 7, 7, 7, 7]

    left = {s for s in family if s & X}
    right = family - left
    downward = lambda s, t: t & ~s == 0
    neighborhood = {t for t in right if any(downward(s, t) for s in core)}
    assert neighborhood == {0, 2, 4}
    assert len(core) == 4 and len(neighborhood) == 3
    # Hall gives upper bound 4, this independent certificate attains it.
    certificate = {X: 0, X | 2: 2, X | 4: 4, E: 8}
    check_certificate(certificate, left, right, downward)
    monotone = matching(left, right, downward)
    assert len(monotone) == len(certificate) == 4

    unrestricted = {X: 0, X | 2: 2, X | 4: 4, X | A: 8, E: 16}
    check_certificate(unrestricted, left, right, lambda s, t: True)
    assert len(unrestricted) == len(left) == 5

    repaired = family | {A}
    check_closed(repaired, lambda s, t: s & t)
    repaired_right = repaired - left
    repaired_certificate = {s: s ^ X for s in core}
    repaired_certificate[E] = 8
    check_certificate(repaired_certificate, left, repaired_right, downward)
    assert len(matching(left, repaired_right, downward)) == 5

    cube = set(subsets(E))
    cube_left = {s for s in cube if s & X}
    cube_right = cube - cube_left
    check_certificate({s: s ^ X for s in cube_left},
                      cube_left, cube_right, downward)
    assert len(matching(cube_left, cube_right, downward)) == 16

    dual = {E ^ s for s in family}
    check_closed(dual, lambda s, t: s | t)
    assert frequencies(dual) == [12, 10, 10, 10, 10]
    dual_left = {s for s in dual if not s & X}
    dual_right = dual - dual_left
    upward = lambda s, t: s & ~t == 0
    dual_core = {E ^ s for s in core}
    dual_neighbors = {t for t in dual_right
                      if any(upward(s, t) for s in dual_core)}
    assert dual_neighbors == {E ^ s for s in neighborhood}
    assert len(matching(dual_left, dual_right, upward)) == 4

    print(json.dumps({
        "fixture_size": len(family),
        "frequencies_x_a_b_c_d": frequencies(family),
        "ordered_intersections_checked": len(family) ** 2,
        "Hall_left_size": len(core),
        "Hall_neighborhood_size": len(neighborhood),
        "maximum_downward_matching": len(monotone),
        "unrestricted_matching": len(unrestricted),
        "one_set_repair_matching": len(repaired_certificate),
        "dual_union_frequencies": frequencies(dual),
        "dual_upward_matching": 4,
        "controls": "independent representations, explicit certificates, powerset",
        "result": "ALL CHECKS PASS; candidate M refuted on this fixture"
    }, indent=2))


if __name__ == "__main__":
    main()
