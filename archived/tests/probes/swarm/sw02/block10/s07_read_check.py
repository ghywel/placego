#!/usr/bin/env python3
"""GC2804 fixed controls for XP4.1 and the new finite reflection proof.

Prediction: all four literal radius2 rules have the stated block rows and
alternating columns through64; reflected block sums are the exact even bands.
Counterfactual: any mismatch blocks the affected carrying/handoff statement.
Record searched: XP4 and its SKM/SKR packets, GC1165, current known-find radius
and outside CL752; no producer imported. This is a finite self-check of the
new proof, not Local's independent carrying read and not an enlarged census.
"""
import itertools
import json


def g(word, p, q):
    a, b, c, d = word
    if word == (1, 1, 0, 1):
        return p
    if word == (1, 0, 1, 1):
        return q
    return int(not b == c == d)


def step(row, p, q, seen=None, mutate=False):
    out = set()
    for i in range(min(row) - 2, max(row) + 3):
        w = tuple(int(j in row) for j in (i - 1, i, i + 1, i + 2))
        if seen is not None:
            seen.add(w)
        v = g(w, p, q) ^ int(mutate and w == (0, 0, 1, 0))
        if int(i - 2 in row) ^ v:
            out.add(i)
    return out


def evolve_blocks(z, t, centre=True):
    out = set()
    for j in z:
        out.symmetric_difference_update((j - 1, j + 1))
        if centre:
            out.symmetric_difference_update((j,))
    out.symmetric_difference_update((t,))
    if t % 2 == 0:
        out.symmetric_difference_update((t - 1,))
    return out


def band(n):
    return {2 * k for k in range(-n, n)}


def main():
    all_histories = []
    for p, q in itertools.product((0, 1), repeat=2):
        row, z, seen, history = {0, 2}, set(), set(), []
        for t in range(65):
            assert all(-t <= j <= t - 1 for j in z)
            assert ((t - 1 in z), (t - 2 in z)) == (bool(t % 2),) * 2
            pred = {k for j in z for k in (2 * j, 2 * j + 1)} | {2 * t + 2}
            if t % 2 == 0:
                pred.add(2 * t)
            assert row == pred
            assert (-2 in row) == (-1 in row) == bool(t % 2)
            reflected = z ^ {-2 - j for j in z}
            assert reflected == band((t + 1) // 2)
            assert bool(0 in reflected) ^ bool(t == 0)
            history.append(frozenset(row))
            row, z = step(row, p, q, seen), evolve_blocks(z, t)
        assert seen == set(itertools.product((0, 1), repeat=4)) - {(1, 1, 0, 1), (1, 0, 1, 1)}
        assert not any(all((a0 ^ sum(a * b for a, b in zip(coeff, w)) % 2) == g(w, p, q)
                           for w in seen)
                       for a0 in (0, 1) for coeff in itertools.product((0, 1), repeat=4))
        assert g((0, 0, 0, 0), p, q) == 0 and g((0, 0, 0, 1), p, q) == 1
        assert g((0, 0, 1, 0), p, q) == g((0, 0, 1, 1), p, q)
        all_histories.append(history)
    assert all(h == all_histories[0] for h in all_histories)
    # Algebraic band update, with the n=0 endpoint retained.
    for n in range(33):
        e = band(n)
        te = set()
        for j in e:
            te.symmetric_difference_update((j - 1, j, j + 1))
        assert te == e ^ {2 * n - 1} ^ {-2 * n - 1}
    # Negative: block90 with identical sources already fails at t=2.
    z = set()
    for t in range(2):
        z = evolve_blocks(z, t, centre=False)
    assert -1 in z
    # Negative: a visited nonlinear boundary window matters at the first tick.
    assert -1 not in step({0, 2}, 1, 1, mutate=True)
    # The alternate seed is not uniform over the parameter family.
    r = {0, 3}
    for _ in range(3):
        r = step(r, 0, 0)
    assert -1 not in r
    print(json.dumps({"rules": 4, "rows_per_rule": 65, "reflection_checks": 260,
                      "parameters_unread_on_witness": ["p", "q"],
                      "affine_fits_to_14_read_windows": 0,
                      "negative_controls": ["block90", "visited-window mutation", "seed03 at p0"]}))
    print("S07_BLOCK_AND_REFLECTION_PASS")


if __name__ == "__main__":
    main()
