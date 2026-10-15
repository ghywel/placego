#!/usr/bin/env python3
"""B17 counting-only audit, preregistered in GPT-MATH-INSTINCT MI043.

No burnability solver. Compare Gaussian-polynomial coefficients with a
separate bounded-partition recurrence, small direct tuples and complement.
Degree480, 5s alarm, sampled128MiB RSS guard. Raw JSON stays outside git.
"""

import json
import signal
import time
from functools import lru_cache

from path_forest_scope import check_memory, convolution_counts


EXPECTED = [3319, 425632, 5523890, 19382158, 24688633, 12385850,
            2271658, 106518, 186]
misses = 0


def gaussian_coefficients(k, bound, degree):
    assert 0 <= degree <= 480
    coefficients = [1] + [0] * degree
    for j in range(1, k + 1):
        # Divide by1-q^j, then multiply by1-q^(bound+j), truncated exactly.
        for d in range(j, degree + 1):
            coefficients[d] += coefficients[d - j]
        shift = bound + j
        for d in range(degree, shift - 1, -1):
            coefficients[d] -= coefficients[d - shift]
    return coefficients


@lru_cache(None)
def rectangle(k, bound, total):
    global misses
    misses += 1
    if misses % 1024 == 1:
        check_memory()
    if total < 0 or total > k * bound:
        return 0
    if total == 0:
        return 1
    if k == 0 or bound == 0:
        return 0
    # Either no part equals bound, or remove one such part.
    return rectangle(k, bound - 1, total) + rectangle(k - 1, bound, total - bound)


def direct_tuples(k, bound, total, lower=0):
    if k == 0:
        return int(total == 0)
    return sum(direct_tuples(k - 1, bound, total - first, first)
               for first in range(lower, min(bound, total // k) + 1))


def main():
    started = time.monotonic()
    signal.alarm(5)
    check_memory()
    controls = 0
    for k in range(4):
        for bound in range(5):
            degree = k * bound + 1
            coefficients = gaussian_coefficients(k, bound, degree)
            for total in range(degree + 1):
                assert coefficients[total] == rectangle(k, bound, total)
                assert coefficients[total] == direct_tuples(k, bound, total)
                controls += 1
    assert rectangle(0, 0, 0) == 1
    assert rectangle(8, 0, 1) == 0
    assert rectangle(8, 64, 33 * 33 - 544) == 0
    rows = []
    for m, expected in zip(range(24, 33), EXPECTED):
        rectangle.cache_clear()
        bound, total = 2 * m - 2, m * m - 544
        count = gaussian_coefficients(8, bound, total)[total]
        assert count == rectangle(8, bound, total), m
        assert count == expected, m
        rows.append({"m": m, "bound": bound, "surplus": total,
                     "exceptional_targets": count})
        check_memory()
    unrestricted = convolution_counts(8, 32)
    assert rows[0]["exceptional_targets"] == unrestricted[32] == 3319
    assert rectangle(8, 62, 480) == rectangle(8, 62, 16) == unrestricted[16] == 186
    assert sum(row["exceptional_targets"] for row in rows) == 64787844
    signal.alarm(0)
    print(json.dumps({"status": "NUMERICAL CHECKS PASS", "rows": rows,
                      "total": sum(row["exceptional_targets"] for row in rows),
                      "small_direct_controls": controls,
                      "complement_control": 186,
                      "elapsed_seconds": time.monotonic() - started,
                      "peak_rss_bytes": check_memory()}, indent=2))


if __name__ == "__main__":
    main()
