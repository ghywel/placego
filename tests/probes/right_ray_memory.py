#!/usr/bin/env python3
"""Finite checks for the right-edge observer reading each wheel twice."""
import itertools
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import time

out = Path(os.environ["CAPPED_OUT"])
last_thermal = 0.0


def guard(force=False):
    global last_thermal
    if force or time.monotonic() - last_thermal > 1:
        status = subprocess.run(["pmset", "-g", "therm"], text=True, capture_output=True,
                                check=True, timeout=3)
        limits = re.findall(r"CPU_(?:Speed|Scheduler)_Limit\s*=\s*(\d+)", status.stdout)
        if sorted(limits) != ["100", "100"]:
            raise RuntimeError("thermal monitor unavailable or throttled")
        last_thermal = time.monotonic()
    cpu = sum(u.ru_utime + u.ru_stime for u in
              (resource.getrusage(resource.RUSAGE_SELF), resource.getrusage(resource.RUSAGE_CHILDREN)))
    if cpu > 20:
        raise RuntimeError("aggregate worker CPU stop")
    return cpu


def step(v):
    return v ^ ((v << 1) | (v << 2))


def bit(v, d):
    return (v >> d) & 1


def reply(v, depth, a):
    # v is the low depth bits at physical tick 2*depth. Supply the next observed bit.
    x = v | (a << depth)
    y = step(x)
    return bit(y, depth), step(y) % (2 << depth)


def word(v, depth, inputs):
    result = []
    for a in inputs:
        b, v = reply(v, depth, a)
        result.append(b)
        depth += 1
    return tuple(result)


def signatures(depth, horizon):
    # Equal IDs iff both automata reply identically to every word of the given length.
    next_ids = None
    for d in reversed(range(depth, depth + horizon)):
        ids = []
        classes = {}
        for v in range(1, 1 << d, 2):
            b0, x0 = reply(v, d, 0)
            b1, x1 = reply(v, d, 1)
            assert b1 == 1 - b0
            key = (b0, next_ids[x0 // 2], next_ids[x1 // 2]) if next_ids is not None else (b0,)
            ids.append(classes.setdefault(key, len(classes)))
        next_ids = ids
        guard()
    return next_ids


def brute_signature(v, d, h):
    return tuple(word(v, d, a) for a in itertools.product(range(2), repeat=h))


def cone_check():
    # An independent ordinary-coordinate three-neighbour truth table, indexed right edge inward.
    for depth in range(1, 10):
        for pairs in range(1, 4):
            width = depth + pairs
            low = depth - 3 * pairs + 1
            for snapshot in range(1, 1 << width, 2):
                row = [bit(snapshot, j) for j in range(width)]
                all_white = True
                for tick in range(2 * pairs):
                    all_white &= not row[depth + tick // 2]
                    padded = [0, 0] + row
                    row = [int(4 * padded[j+2] + 2 * padded[j+1] + padded[j] in (1, 2, 3, 4))
                           for j in range(width)]
                assert all_white == (snapshot >> max(0, low) == 0)
            guard()


def phase_control():
    # Actual finite seed phases at one common age, with the low register period measured directly.
    d, maximum_delay = 9, 2
    n = d + maximum_delay + 1
    mask = (1 << n) - 1
    rows = [1]
    y = step(1) & mask
    while y != 1 and len(rows) <= 1 << n:
        rows.append(y)
        y = step(y) & mask
    assert y == 1
    for q in range(maximum_delay + 1):
        r = (d - 3 * q - 1) // 2
        launch = (r - 2 * d) % len(rows)
        outputs = [bit(rows[(launch + 2 * d + s) % len(rows)], d + s // 2)
                   for s in range(2 * q + 2)]
        assert outputs == [0] * (2 * q + 1) + [1]
    return len(rows)


def main():
    guard(True)
    cone_check()
    period = phase_control()
    counts = {}
    for d in (3, 5, 8, 10):
        counts[d] = {}
        for h in range(1, min(8, 17-d) + 1):
            ids = signatures(d, h)
            counts[d][h] = len(set(ids))
            if d == 3 or (d == 5 and h <= 4):
                brute = [brute_signature(v, d, h) for v in range(1, 1 << d, 2)]
                for i in range(len(ids)):
                    for j in range(i):
                        assert (ids[i] == ids[j]) == (brute[i] == brute[j])
            if h > 1:
                assert counts[d][h] >= counts[d][h-1]
    # Holding with a black parent produces an output toggle on either supplied input.
    assert reply(1, 1, 0)[0] == 1 and reply(1, 1, 1)[0] == 0
    cpu = guard(True)
    result = {"status": "PASS", "classes": counts, "phase_register_period": period, "worker_cpu_s": cpu}
    (out / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
