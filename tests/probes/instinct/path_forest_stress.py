#!/usr/bin/env python3
"""B16 one-run stress calibration; predictions and limits in MI041.

Seven targets >=46, square total20^2 only. Same search as B15, fresh state.
Expect the2m-state cap; complete counts, if reached, must be162074/1588.
Stream completed records to stdout as JSONL; final summary distinguishes
pending UNKNOWN from resolved SAT/UNSAT. Never continue to m21 or eight paths.
"""

import json
import signal
import time

from path_forest_pilot import (LimitReached, Search, alarm_handler,
                               exhaustive_oracle, peak_rss, sorted_targets,
                               verify_witness)


def emit(record):
    print(json.dumps(record), flush=True)


def main():
    started = time.monotonic()
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(60)
    search = Search()
    summary = {"type": "summary", "status": "RUNNING", "m": 20,
               "minimum": 46, "declared_total": 163662,
               "attempted": 0, "feasible": 0, "deficient": 0,
               "pending_target": None, "complete": False, "controls": {}}
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
        assert checked == 189
        assert search.individual_ranges_pass(3, (3, 3, 3))
        assert search.solve(3, (3, 3, 3)) is None
        assert search.solve(9, (17, 17, 17, 30)) is None
        positive = search.solve(3, (1, 3, 5))
        assert verify_witness(3, (1, 3, 5), positive)
        corrupted = list(positive)
        corrupted[0] = (3,)
        assert not verify_witness(3, (1, 3, 5), corrupted)
        summary["controls"] = {"small_target_tuples": checked, "oracle": "PASS",
                               "negative_fixtures": "PASS",
                               "corrupted_witness_rejected": True}
        for targets in sorted_targets(400, 7, 46):
            summary["attempted"] += 1
            summary["pending_target"] = targets
            witness = search.solve(20, targets)
            if witness is None:
                record = {"type": "case", "result": "UNSAT", "targets": targets}
                emit(record)
                summary["deficient"] += 1
            else:
                assert verify_witness(20, targets, witness)
                record = {"type": "case", "result": "SAT", "targets": targets,
                          "bins": witness}
                emit(record)
                summary["feasible"] += 1
            summary["pending_target"] = None
        summary["complete"] = True
        assert (summary["feasible"], summary["deficient"]) == (162074, 1588)
        summary["status"] = "NUMERICAL CHECKS PASS"
    except LimitReached as error:
        summary["status"] = "UNKNOWN - RESOURCE CUTOFF"
        summary["reason"] = str(error)
    except Exception as error:
        summary["status"] = "INSTRUMENT FAILURE"
        summary["reason"] = f"{type(error).__name__}: {error}"
        raise
    finally:
        signal.alarm(0)
        summary["elapsed_seconds"] = time.monotonic() - started
        summary["expanded_states"] = search.expanded
        summary["cache_hits"] = search.cache_hits
        summary["cache_clears"] = search.cache_clears
        summary["peak_rss_bytes"] = peak_rss()
        summary["completed"] = summary["feasible"] + summary["deficient"]
        emit(summary)


if __name__ == "__main__":
    main()
