#!/usr/bin/env python3
"""B15 instrument calibration, preregistered in GPT-MATH-INSTINCT MI039.

Complete domain: seven positive targets >=46, total m*m, m in {18,19}.
Expected published feasible/deficient counts: (2,0), (5553,178).
Independent small assignment oracle and independent witness checker precede it.
No eight-path search. Hard limits: 60s, 2m expanded states, sampled RSS128MiB,
failed-state cache50k (cleared when full). A cutoff is UNKNOWN, never UNSAT.
JSON output, including all positive witnesses, belongs outside git.
"""

import itertools
import json
import math
import resource
import signal
import sys
import time
from functools import lru_cache


class LimitReached(Exception):
    pass


def peak_rss():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return value if sys.platform == "darwin" else value * 1024


def alarm_handler(signum, frame):
    raise LimitReached("60-second runtime cap")


def sorted_targets(total, slots, lower):
    if slots == 1:
        if total >= lower:
            yield (total,)
        return
    for first in range(lower, total // slots + 1):
        for rest in sorted_targets(total - first, slots - 1, first):
            yield (first,) + rest


def verify_witness(m, targets, bins):
    """Independent of all search pruning and residual-capacity bookkeeping."""
    if bins is None or len(bins) != len(targets):
        return False
    flat = [value for group in bins for value in group]
    return (sorted(flat) == list(range(1, 2 * m, 2))
            and all(sum(group) == target for target, group in zip(targets, bins)))


def exhaustive_oracle(m):
    """Labeled assignments to three bins; no pruning or search-code reuse."""
    answer = set()
    odds = list(range(1, 2 * m, 2))
    for assignment in itertools.product(range(3), repeat=m):
        totals = [0, 0, 0]
        for odd, label in zip(odds, assignment):
            totals[label] += odd
        if min(totals) > 0:
            answer.add(tuple(sorted(totals)))
    return answer


class Search:
    def __init__(self):
        self.expanded = 0
        self.cache_hits = 0
        self.dead = set()
        self.cache_clears = 0

    @staticmethod
    @lru_cache(maxsize=20000)
    def count_range(k, residual):
        # c distinct numbers from the first k odds have min c*c and
        # max c*(2*k-c), with parity c. These bounds are necessary here.
        if residual == 0:
            return 0, 0
        if residual > k * k or residual < 0:
            return None
        low = k - math.isqrt(k * k - residual)
        if low % 2 != residual % 2:
            low += 1
        high = min(k, math.isqrt(residual))
        if high % 2 != residual % 2:
            high -= 1
        if low > high:
            return None
        return low, high

    def individual_ranges_pass(self, k, capacities):
        low_sum = high_sum = 0
        for residual in capacities:
            interval = self.count_range(k, residual)
            if interval is None:
                return False
            low, high = interval
            low_sum += low
            high_sum += high
        return low_sum <= k <= high_sum

    def solve(self, k, capacities):
        """Returns bins aligned with sorted capacities, or exhaustive None."""
        state = k, capacities
        if state in self.dead:
            self.cache_hits += 1
            return None
        if self.expanded >= 2_000_000:
            raise LimitReached("2,000,000 expanded-state cap")
        self.expanded += 1
        if self.expanded % 1024 == 1 and peak_rss() > 128 * 1024**2:
            raise LimitReached("sampled128MiB RSS guard")
        assert sum(capacities) == k * k
        if not self.individual_ranges_pass(k, capacities):
            self.remember_dead(state)
            return None
        if k == 0:
            return tuple(() for _ in capacities)
        if sum(value > 0 for value in capacities) == 1:
            return tuple(tuple(range(1, 2 * k, 2)) if value else ()
                         for value in capacities)
        odd = 2 * k - 1
        previous = None
        # Best-fit order; equal residual capacities give symmetric choices.
        for index, value in enumerate(capacities):
            if value < odd or value == previous:
                continue
            previous = value
            reduced = list(capacities)
            reduced[index] -= odd
            permutation = sorted(range(len(reduced)), key=reduced.__getitem__)
            child_capacities = tuple(reduced[i] for i in permutation)
            child = self.solve(k - 1, child_capacities)
            if child is not None:
                bins = [None] * len(capacities)
                for child_index, parent_index in enumerate(permutation):
                    bins[parent_index] = child[child_index]
                bins[index] += (odd,)
                return tuple(bins)
        self.remember_dead(state)
        return None

    def remember_dead(self, state):
        if len(self.dead) >= 50000:
            self.dead.clear()
            self.cache_clears += 1
        self.dead.add(state)


def main():
    started = time.monotonic()
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(60)
    search = Search()
    output = {"status": "RUNNING", "controls": {}, "rows": []}
    try:
        checked = 0
        for m in range(1, 7):
            oracle = exhaustive_oracle(m)
            for targets in sorted_targets(m * m, 3, 1):
                witness = search.solve(m, targets)
                assert (witness is not None) == (targets in oracle), (m, targets)
                if witness is not None:
                    assert verify_witness(m, targets, witness)
                checked += 1
        assert search.individual_ranges_pass(3, (3, 3, 3))
        assert search.solve(3, (3, 3, 3)) is None
        assert search.solve(9, (17, 17, 17, 30)) is None
        positive = search.solve(3, (1, 3, 5))
        assert verify_witness(3, (1, 3, 5), positive)
        corrupted = list(positive)
        corrupted[0] = (3,)
        assert not verify_witness(3, (1, 3, 5), corrupted)
        output["controls"] = {"small_target_tuples": checked,
                              "oracle": "PASS", "negative_fixtures": "PASS",
                              "corrupted_witness_rejected": True}
        for m, expected in ((18, (2, 0)), (19, (5553, 178))):
            row = {"m": m, "attempted": 0, "feasible": 0, "deficient": 0,
                   "pending_target": None,
                   "complete": False, "positive_witnesses": [],
                   "deficient_targets": []}
            output["rows"].append(row)
            for targets in sorted_targets(m * m, 7, 46):
                row["attempted"] += 1
                row["pending_target"] = targets
                witness = search.solve(m, targets)
                if witness is None:
                    row["deficient"] += 1
                    row["deficient_targets"].append(targets)
                else:
                    assert verify_witness(m, targets, witness)
                    row["feasible"] += 1
                    row["positive_witnesses"].append({"targets": targets,
                                                      "bins": witness})
                row["pending_target"] = None
            row["complete"] = True
            assert (row["feasible"], row["deficient"]) == expected, row
        output["status"] = "NUMERICAL CHECKS PASS"
    except LimitReached as error:
        output["status"] = "UNKNOWN - RESOURCE CUTOFF"
        output["reason"] = str(error)
    except Exception as error:
        output["status"] = "INSTRUMENT FAILURE"
        output["reason"] = f"{type(error).__name__}: {error}"
        raise
    finally:
        signal.alarm(0)
        output["elapsed_seconds"] = time.monotonic() - started
        output["expanded_states"] = search.expanded
        output["cache_hits"] = search.cache_hits
        output["cache_clears"] = search.cache_clears
        output["peak_rss_bytes"] = peak_rss()
        print(json.dumps(output))


if __name__ == "__main__":
    main()
