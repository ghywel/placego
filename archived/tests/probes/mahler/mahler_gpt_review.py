#!/usr/bin/env python3
"""Fixed-input census review for L708, preregistered in GC1220.1.

Record searched: Mahler closed and Pi^0_2/independence; G51 and both census
sources read. No census, membership search or extension of Local's runs.

Predictions before execution: the saved starts 119619616250377 and
9850069454682037 have horizons 120 and 137. The former is classified by C;
the latter is a T124 straggler. Fixed chunks (10,6,3) and (12,8,7) each
contribute exactly 16 deaths at step 2. Counterfactual: either fixed horizon
or the corrected chunk multiplicity disagrees with independent arithmetic.
Unexpected control: the all-zero fixed start produces neither deaths nor
stragglers. Additional finite-width guard, before execution: on starts
2^62 and 2^63-1, the wrapped 128-bit recurrence and exact integer recurrence
have the same parity for 124 steps, although their high bits may differ.

Run: python3 tests/probes/mahler/mahler_gpt_review.py
Cost: one temporary C build, five fixed C inputs, four fixed Python inputs.
Temporary executable and data are outside git. No external Python library.

OUTCOME (2026-10-14 08:24 BST): all fixed controls PASS; no large census replay.
The saved horizons are 120 and 137; the second is a C straggler. Both
early-death chunks contribute 16 starts. Zero is excluded, and both
128-bit overflow controls preserve all 124 tested parities.
"""
from fractions import Fraction
from pathlib import Path
import subprocess
import tempfile


def initial_window_horizon(start):
    """G51's original-fraction inequalities, not the walker's moving window."""
    n, c, p2, p3 = start, 0, 1, 1
    upper = Fraction(1, 2)
    for t in range(1, 201):
        bit = n % 2
        c = 3 * c + bit * p2
        p2 *= 2
        p3 *= 3
        upper = min(upper, Fraction(2 * c + p2, 2 * p3))
        if Fraction(c, p3) >= upper:
            return t
        n = (3 * n + bit) // 2
    raise AssertionError("Fixed fixture did not terminate within its registered cap")


def parse_output(output):
    hist, strag = {}, []
    for line in output.splitlines():
        fields = line.split()
        if fields[0] == "H":
            hist[int(fields[1])] = int(fields[2])
        elif fields[0] == "S":
            strag.append(int(fields[1]))
    return hist, strag


def check_precision(start):
    exact = wrapped = start
    mask = (1 << 128) - 1
    differed = False
    for _ in range(124):
        assert exact % 2 == wrapped % 2
        bit = exact % 2
        exact = (3 * exact + bit) // 2
        wrapped = ((3 * wrapped + bit) & mask) // 2
        differed |= exact != wrapped
    assert differed, "The overflow guard did not exercise lost high bits"


def main():
    source = Path(__file__).with_name("mahler_census.c")
    with tempfile.TemporaryDirectory(prefix="mahler-review-") as tmp:
        binary = str(Path(tmp) / "walker")
        subprocess.run(["cc", "-O2", "-o", binary, str(source)], check=True)

        def run(*args):
            result = subprocess.run([binary, *map(str, args)], check=True,
                                    capture_output=True, text=True)
            return parse_output(result.stdout)

        first, second = 119619616250377, 9850069454682037
        assert initial_window_horizon(first) == 120
        assert initial_window_horizon(second) == 137
        assert run(48, 48, first) == ({120: 1}, [])
        assert run(56, 56, second) == ({}, [second])
        for args in ((10, 6, 3), (12, 8, 7)):
            assert run(*args) == ({2: 16}, [])
        assert run(8, 8, 0) == ({}, [])
    for start in (1 << 62, (1 << 63) - 1):
        check_precision(start)
    print("PASS: fixed horizons 120/137, straggler boundary, two chunk counts,")
    print("excluded zero, and two overflowing parity-precision controls.")


if __name__ == "__main__":
    main()
