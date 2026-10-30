#!/usr/bin/env python3
"""Exact arithmetic on the retained GC2260 table; never evolves a state.

Usage: reanalyse_edge_distributions.py GC2260_ARCHIVE OUTPUT_JSON
The predeclared identities/controls are in GC2279. One small table only.
"""
import hashlib
import json
import sys
import tarfile
from fractions import Fraction
from pathlib import Path

EXPECTED = "f72474070a2696cd0695773c5434d6a0bee636894f1fc2c4b8447f3396659bd5"


def mean(hist):
    return sum(Fraction(k * count, sum(hist.values())) for k, count in hist.items())


def subtract(a, b):
    result = {k: a.get(k, 0) - b.get(k, 0) for k in a.keys() | b.keys()}
    assert all(count >= 0 for count in result.values())
    return {k: count for k, count in result.items() if count}


def lift_counts(old, new):
    """Number of old seeds in each clock class that double on extension."""
    result = {}
    previous = 0
    for k in range(max(old.keys() | new.keys()) + 2):
        assert new.get(k, 0) % 2 == 0
        d = old.get(k, 0) + previous - new.get(k, 0) // 2
        assert 0 <= d <= old.get(k, 0), (k, d)
        assert d % (1 << k) == 0, (k, d)
        result[k] = d
        previous = d
    assert previous == 0
    p = Fraction(sum(result.values()), sum(old.values()))
    assert p == mean(new) - mean(old)
    return {k: d for k, d in result.items() if d}, p


def main():
    archive, output = map(Path, sys.argv[1:])
    assert archive.stat().st_size < 1 << 20
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == EXPECTED
    assert not output.exists()
    with tarfile.open(archive) as tf:
        members = [m for m in tf.getmembers() if Path(m.name).name == "edge_distributions.json"]
        assert len(members) == 1 and members[0].size < 1 << 20
        raw = tf.extractfile(members[0]).read()
    rows = json.loads(raw)["full_prefix"]
    assert [r["prefix_bits"] for r in rows] == list(range(1, 22))
    gates = {}
    for gate in ("OR", "AND"):
        hist = [{0: 1}] + [{int(k): v for k, v in row[gate].items()} for row in rows]
        for n, h in enumerate(hist):
            assert sum(h.values()) == 1 << n
            assert all(c >= 0 and c % (1 << k) == 0 for k, c in h.items())
        assert hist[1] == {0: 2}
        assert hist[2] == ({0: 2, 1: 2} if gate == "OR" else {0: 4})
        odd = [None] + [subtract(hist[n], hist[n - 1]) for n in range(1, 22)]
        for n in range(1, 22):
            assert sum(odd[n].values()) == 1 << (n - 1)
            assert mean(odd[n]) == 2 * mean(hist[n]) - mean(hist[n - 1])
        previous_p = Fraction(0)
        records = []
        for n in range(1, 21):
            d, p = lift_counts(hist[n], hist[n + 1])
            od, op = lift_counts(odd[n], odd[n + 1])
            assert op == 2 * p - previous_p
            records.append({"old_bits": n, "doubling_seeds_by_exponent": d,
                            "probability": str(p), "odd_doubling_seeds_by_exponent": od,
                            "odd_probability": str(op)})
            previous_p = p
        assert records[0]["probability"] == ("1/2" if gate == "OR" else "0")
        gates[gate] = records
    result = {"status": "PASS", "input_archive_sha256": EXPECTED,
              "input_table_sha256": hashlib.sha256(raw).hexdigest(),
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "scope": "Exact retained-table arithmetic only; no new trajectories or fairness-marker counts",
              "gates": gates}
    encoded = (json.dumps(result, indent=2) + "\n").encode()
    assert len(encoded) < 128 << 10
    output.write_bytes(encoded)
    print("PASS: 40 unconditional and 40 black-edge-conditioned lift rows; no dynamics")
    for gate, records in gates.items():
        for r in records:
            if r["old_bits"] in (1, 2, 3, 4, 8, 12, 16, 20):
                print(gate, r["old_bits"], r["probability"], r["odd_probability"])


if __name__ == "__main__":
    main()
