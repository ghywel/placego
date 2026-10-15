#!/usr/bin/env python3
"""B13 feasibility counts, preregistered in GPT-MATH-INSTINCT MI035.

P1: fewer than 100000 sorted eight-target tuples at m=24; over 10^9 at m=32.
P2: independent integer coefficient constructions agree. Controls include
direct small tuple enumeration and the failure of exact division by 8!.
No path burning or partition-feasibility search. No new mathematical bound.
Degree cap 480, runtime cap 5s, memory cap 128MiB. JSON output goes to stdout.
"""

import json
import math
import resource
import signal
import sys
from functools import lru_cache


CAP = 480


def check_memory():
    # Darwin reports bytes; other supported Unix hosts report KiB.
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak if sys.platform == "darwin" else peak * 1024
    if peak_bytes > 128 * 1024**2:
        raise MemoryError("sampled peak RSS exceeds 128MiB")
    return peak_bytes


def convolution_counts(parts, cap):
    """Multiply finite geometric series, keeping coefficients through cap."""
    coefficients = [1] + [0] * cap
    for step in range(1, parts + 1):
        old = coefficients
        coefficients = [
            sum(old[degree - multiple] for multiple in range(0, degree + 1, step))
            for degree in range(cap + 1)
        ]
        check_memory()
    return coefficients


@lru_cache(None)
def partitions(total, max_part):
    """Independent include/exclude recurrence for partitions with bounded parts."""
    if total == 0:
        return 1
    if total < 0 or max_part == 0:
        return 0
    if max_part == 1:
        return 1
    return partitions(total, max_part - 1) + partitions(total - max_part, max_part)


def direct_tuples(total, slots, lower=0):
    """Enumerate sorted tuples directly, independently of partition conjugation."""
    if slots == 1:
        return int(total >= lower)
    return sum(
        direct_tuples(total - first, slots - 1, first)
        for first in range(lower, total // slots + 1)
    )


def main():
    signal.alarm(5)
    # Darwin rejected RLIMIT_AS before arithmetic on the initial attempt.
    # Use an explicitly reported sampled RSS guard, not a claimed OS hard cap.
    if sys.platform != "darwin":
        resource.setrlimit(resource.RLIMIT_AS, (128 * 1024**2, 128 * 1024**2))
    check_memory()
    q = convolution_counts(8, CAP)
    assert all(q[r] == partitions(r, 8) for r in range(CAP + 1))
    check_memory()
    assert convolution_counts(1, 32) == [1] * 33
    assert convolution_counts(2, 32) == [r // 2 + 1 for r in range(33)]
    assert q[0] == 1
    for r in range(33):
        assert q[r] == direct_tuples(r, 8)
        check_memory()
    rows = []
    for m in range(24, 33):
        surplus = m * m - 544
        ordered = math.comb(surplus + 7, 7)
        count = q[surplus]
        assert count <= ordered <= math.factorial(8) * count
        rows.append({"m": m, "surplus": surplus, "sorted_targets": count})
    assert rows[0]["sorted_targets"] < 100000
    assert rows[-1]["sorted_targets"] > 10**9
    # At surplus zero there is one orbit, despite the naive 1/8! quotient.
    assert q[0] * math.factorial(8) != math.comb(7, 7)
    signal.alarm(0)
    print(json.dumps({"status": "NUMERICAL CHECKS PASS", "rows": rows,
                      "peak_rss_bytes": check_memory(),
                      "memory_enforcement": "sampled RSS guard" if sys.platform == "darwin"
                      else "RLIMIT_AS and sampled RSS guard"}, indent=2))


if __name__ == "__main__":
    main()
