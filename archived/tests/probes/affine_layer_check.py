#!/usr/bin/env python3
"""GC2385: tiny exhaustive checks of the written affine-family identities.

Prediction/counterfactual/searches: GPT-BOUNDARY-LAYER-REVIEW-20261102.md.
No trajectory census, random sample, or claim about reachable seed states.
"""
import itertools
import json
import time


def phi(x):
    # Current, one shallower, two shallower: interior edge-frame convention.
    return x[0] ^ (x[1] | x[2])


def add(u, v):
    return tuple(x ^ y for x, y in zip(u, v))


def dot(a, z):
    return (a & z).bit_count() & 1


def step_finite(row):
    # Nonnegative support on an otherwise zero whole line; include full output.
    return [
        (row[n] if n < len(row) else 0)
        ^ ((row[n - 1] if 0 <= n - 1 < len(row) else 0)
           | (row[n - 2] if 0 <= n - 2 < len(row) else 0))
        for n in range(len(row) + 2)
    ]


def main():
    start = time.process_time()
    bits = list(itertools.product(range(2), repeat=3))
    polar_checks = 0
    for e, u, v in itertools.product(bits, repeat=3):
        g = lambda d: phi(add(e, d)) ^ phi(e)
        assert g(add(u, v)) ^ g(u) ^ g(v) == (u[1] & v[2]) ^ (u[2] & v[1])
        polar_checks += 1

    family_checks = 0
    affine_families = 0
    # Four parameter bits: all incoming/current labels and all eight backgrounds.
    k = 4
    for e in bits:
        for c, a, b in itertools.product(range(1 << k), repeat=3):
            values = [phi(add(e, (dot(c, z), dot(a, z), dot(b, z)))) ^ phi(e)
                      for z in range(1 << k)]
            inferred = sum(values[1 << j] << j for j in range(k))
            linear = all(y == dot(inferred, z) for z, y in enumerate(values))
            compatible = a == 0 or b == 0 or a == b
            assert linear == compatible, (e, c, a, b)
            if compatible:
                expected = c ^ (a if e[2] == 0 else 0) ^ (b if e[1] == 0 else 0)
                expected ^= a if a == b else 0
                assert expected == inferred
                affine_families += 1
            family_checks += 1

    # Separation is not an invariant: independent disturbances at positions0,2.
    rows = [[dot(a, z) for a in (1, 0, 2)] for z in range(4)]
    defects = []
    for tick in range(3):
        defect = [rows[0][i] ^ rows[1][i] ^ rows[2][i] ^ rows[3][i]
                  for i in range(len(rows[0]))]
        defects.append([i for i, bit in enumerate(defect) if bit])
        rows = [step_finite(row) for row in rows]
    assert defects == [[], [], [3, 4]]

    # A local damaged-pair pattern does not determine the next jump generally.
    jumps = []
    for b2 in (0, 1):
        a = {-1: 1, 0: 0, 1: 1}
        b = {-1: 1, 0: 1, 1: 0, 2: b2}
        evolve = lambda row, x: row.get(x - 1, 0) ^ (row.get(x, 0) | row.get(x + 1, 0))
        next_front = next(x for x in range(-3, 5) if evolve(a, x) != evolve(b, x))
        jumps.append(next_front + 1)
    assert jumps == [3, 2]

    print(json.dumps({
        "status": "PASS", "polarization_cases": polar_checks,
        "four_parameter_families": family_checks, "affine_families": affine_families,
        "separated_modes_nonaffine_sites_at_t0_t1_t2": defects,
        "same_four_bit_pattern_next_jumps": jumps,
        "iid_reference_expected_p32_coincidences": 912132 / 2**32,
        "cpu_seconds": time.process_time() - start,
        "scope": "finite Boolean self-checks; hand criterion remains PROOF-SKETCH pending carrying read"
    }, indent=2))


if __name__ == "__main__":
    main()
