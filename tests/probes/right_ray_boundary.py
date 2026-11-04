#!/usr/bin/env python3
"""Classify futures at the two frozen depths via their full finite-register boundary movies."""
import hashlib
import json
import os
from pathlib import Path
from right_ray_memory import guard, step


def movies(v, d):
    # Compute a complete dyadic return, preserving the phase at the observation cut.
    period_bound = 1 << (d - 1)
    row = v
    mask = (1 << d) - 1
    top = bytearray()
    gate = bytearray()
    for _ in range(period_bound):
        parents = row >> (d - 2)
        top.append(parents >> 1)
        gate.append(int(parents != 0))
        row = step(row) & mask
    assert row == v
    return bytes(top), bytes(gate)


def probe_controls():
    # Unconditional future possible/necessary white tests; enumerate free high bits at the cut.
    for d in (2, 3, 4):
        for low in range(1, 1 << d, 2):
            for k in (d - 1, d - 2):
                for m in (1, 2):
                    for odd_start in (0, 1):
                        n = k + 3 * m - 1 + odd_start
                        if n < d:
                            continue
                        start = 2 * (n-d) + odd_start
                        length = 2 * m + odd_start
                        high = n + m - 1 + odd_start
                        snapshot = low
                        for _ in range(start):
                            snapshot = step(snapshot) % (1 << d)
                        predicted = (snapshot >> k) == 0
                        okay = False
                        mask = (2 << high) - 1
                        for free in range(1 << (high + 1 - d)):
                            row = low | (free << d)
                            for _ in range(start):
                                row = step(row) & mask
                            for s in range(length):
                                j = n + (s + odd_start) // 2
                                if row & (1 << j):
                                    break
                                row = step(row) & mask
                            else:
                                okay = True
                                break
                        assert okay == predicted, (d, low, k, m, odd_start)
                    guard()


def main():
    guard(True)
    probe_controls()
    result = {}
    for d in (8, 10):
        classes = {}
        tops = set()
        for v in range(1, 1 << d, 2):
            key = movies(v, d)
            tops.add(key[0])
            classes.setdefault(key, []).append(v)
        duplicates = [g for g in classes.values() if len(g) > 1]
        result[d] = dict(odd_states=1 << (d-1), top_movies=len(tops),
                         boundary_movies=len(classes), nontrivial_classes=duplicates)
        guard()
    path = Path(os.environ["CAPPED_OUT"]) / "boundary.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result), hashlib.sha256(path.read_bytes()).hexdigest(), guard(True))


if __name__ == "__main__":
    main()
