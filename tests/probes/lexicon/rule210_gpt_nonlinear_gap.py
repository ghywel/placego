#!/usr/bin/env python3
"""GC419 bounded linear-gap controls; not a Rule210 periodic-witness search.
Prediction: dyadic separation forces p centre zeros. Controls compare literal
Rule90 truth-table updates with shift-XOR. Unexpected check: an infinite
period-three background has a nonzero constant wall, so finiteness matters.
"""
import json


def shifted(row):
    return {i - 1 for i in row} ^ {i + 1 for i in row}


def literal(row):
    if not row:
        return set()
    return {i for i in range(min(row) - 1, max(row) + 2)
            if (90 >> (4 * (i - 1 in row) + 2 * (i in row)
                       + (i + 1 in row))) & 1}


def ring(row):
    return tuple(row[(i - 1) % 3] ^ row[(i + 1) % 3]
                 for i in range(3))


def main():
    cases = 0
    for R in range(3):
        for mask in range(1 << (2 * R + 1)):
            seed = {i for i in range(-R, R + 1) if mask >> (i + R) & 1}
            for s in range(4):
                for p in range(1, 5):
                    N = 1
                    while N < R + s + p:
                        N *= 2
                    row = seed.copy()
                    for lag in range(1, N + p):
                        direct = literal(row)
                        assert direct == shifted(row)
                        row = direct
                        if lag == N:
                            assert row == ({i - N for i in seed}
                                           ^ {i + N for i in seed})
                        if lag >= N:
                            assert 0 not in row
                    assert s + N + p - 2 <= 3 * s + 2 * R + 3 * p
                    cases += 1
    assert ring((1, 0, 0)) == (0, 1, 1)
    assert ring((0, 1, 1)) == (0, 1, 1)
    print(json.dumps(dict(finite_linear_controls=cases,
                         scalar_shift_and_dyadic_support="PASS",
                         infinite_period_three_guard="PASS",
                         scope="time-s rows supported in [-R,R] only; not all reachable rows or full periodic witnesses"), indent=2))


if __name__ == "__main__":
    main()
