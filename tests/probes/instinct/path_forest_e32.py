#!/usr/bin/env python3
"""B18 complete E32 calibration, preregistered in MI045.

Eight targets68..130, total1024; independently generate by deficits totaling16.
Predict186 SAT in5s. Hard60s/2m expanded states/sampled128MiB; no widening.
First negative is an unaudited candidate, resource cutoff is UNKNOWN.
Raw JSON with witnesses belongs outside git.
"""

import json
import signal
import time

from path_forest_pilot import (LimitReached, Search, alarm_handler,
                               exhaustive_oracle, peak_rss, sorted_targets,
                               verify_witness)


def bounded_targets(total, slots, lower, upper):
    if slots == 0:
        if total == 0:
            yield ()
        return
    start = max(lower, total - (slots - 1) * upper)
    stop = min(upper, total // slots)
    for first in range(start, stop + 1):
        for rest in bounded_targets(total - first, slots - 1, first, upper):
            yield (first,) + rest


def main():
    started = time.monotonic()
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(60)
    search = Search()
    output = {"status": "RUNNING", "domain": "E32 only", "controls": {},
              "attempted": 0, "completed": 0, "pending_target": None,
              "complete": False, "positive_witnesses": []}
    try:
        direct = list(bounded_targets(1024, 8, 68, 130))
        by_deficit = [tuple(sorted(130 - x for x in deficit))
                      for deficit in sorted_targets(16, 8, 0)]
        assert len(direct) == len(set(direct)) == 186
        assert len(by_deficit) == len(set(by_deficit)) == 186
        assert set(direct) == set(by_deficit)
        checked = 0
        for m in range(1, 7):
            oracle = exhaustive_oracle(m)
            for targets in sorted_targets(m * m, 3, 1):
                witness = search.solve(m, targets)
                assert (witness is not None) == (targets in oracle), (m, targets)
                if witness is not None:
                    assert verify_witness(m, targets, witness)
                checked += 1
        assert checked == 189
        assert search.solve(26, (67,) * 4 + (102,) * 4) is None
        pairs = [(x, 64 - x) for x in range(1, 32, 2)]
        hand = [pairs[2 * i] + pairs[2 * i + 1] for i in range(8)]
        assert verify_witness(32, (128,) * 8, hand)
        balanced = search.solve(32, (128,) * 8)
        assert verify_witness(32, (128,) * 8, balanced)
        corrupted = [tuple(x for x in group if x != 63) for group in balanced]
        assert not verify_witness(32, (128,) * 8, corrupted)
        output["controls"] = {"coverage_generators": "PASS", "domain_size": 186,
                              "small_oracle_cases": checked, "oracle": "PASS",
                              "eight_bin_negative": "PASS",
                              "independent_balanced_certificate": "PASS",
                              "missing_largest_odd_rejected": True}
        for targets in direct:
            output["attempted"] += 1
            output["pending_target"] = targets
            witness = search.solve(32, targets)
            if witness is None:
                output["status"] = "NEGATIVE CANDIDATE - NEEDS INDEPENDENT AUDIT"
                output["negative_candidate"] = targets
                output["completed"] += 1
                output["pending_target"] = None
                break
            assert verify_witness(32, targets, witness)
            output["positive_witnesses"].append({"targets": targets, "bins": witness})
            output["completed"] += 1
            output["pending_target"] = None
        else:
            output["complete"] = True
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
