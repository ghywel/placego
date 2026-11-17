#!/usr/bin/env python3
"""rule30_cloud_wheel_drift.py: RD, does the wheel's rotation carry a remainder beyond 17/56? (row 6.1)

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_wheel_drift.py [TRIALS=300] [T=20000] [SEED=4256]
COST:       a few minutes.

The owner's question (2026-10-08): 17/56 = 0.303571428571... never ends in decimal, so must its rounding leave a
remainder somewhere, a place for a sign to flip? Rule 30 never computes 17/56. It only XORs and ORs bits, so no
floating point and no rounding enter its dynamics or this script. But the owner's picture has an exact counterpart.
Between kicks column 1 runs the wheel U, an exact coding of the rotation by 17/56. Each kick moves the rotation by a
whole number k of notches (1/28 of a turn), forward or backward. So over a stretch of N steps the rotation actually
performed is 17N/56 + (sum of k)/28 turns, and the effective rotation number is f = 17/56 + (sum of k)/(28 N). If
forward kicks outweigh backward ones, f sits above 17/56 and the kicks are the leap days of a calendar keeping step
with it. The record's spectrum pinned column 1's line at f = 0.30365 over 4,096 steps (section 8.8), 0.00008 above
17/56, which is within that window's resolution of about 0.00024. So the record cannot tell which.

Method: real right halves next to the 0101 wall (widths 16 .. 64, ones at random), T steps each. A lock is a stretch
of at least 56 steps on which column 1 equals U shifted by an even phase d. Consecutive locks less than 56 steps
apart are joined into a chain, and the net kick between them is kick_of(d' - d) notches, as in KB and KC. Over each
chain, sum the kicks and the steps.
Control:
  RD-C1: inside every lock, column 1 matches U exactly (by construction), and every single kick has a size between
         -14 and 13 notches, with the forward and backward counts reported by class.
PREDICTIONS (Cloud's, pushed before the first run):
  RD-P1: the net drift is forward: the sum of k over all chains is positive. Confidence 0.6 (KB saw more class-32
         forward kicks than class-52 backward ones).
  RD-P2: the effective rotation number over all chains lies above 17/56 by between 0.00002 and 0.0002, consistent
         with the recorded line at 0.30365. Confidence 0.4.
Counterfactual: if the summed kicks are near zero (|f - 17/56| < 0.00001), the wheel is frequency-locked at exactly
  17/56 with only diffusing phase (sections 8.10, 8.11), and the line's offset at 0.30365 was resolution, not a
  remainder.

OUTCOME, 2026-10-08 (by 15:36 BST; seed 4256, 300 trials, T = 20000, 26 s): 288 chains covering 5,732,242 steps,
  40,012 forward and 31,004 backward kicks (by departure class: 32 forward 38,133, 42 forward 632, 12 forward 36,
  52 backward 31,004, 52 forward 1,211). The net kick sum is +301 notches, so the effective rotation number is
  0.3035733 against 17/56 = 0.3035714, an offset of +0.0000019.
  RD-P1 HELD by its letter (the sum is positive) but not in substance. Post-hoc, same seed: forward kicks total
  +130,434 notches and backward -130,133, and the root sum of squares of the 288 chain sums is 1,208 notches. The
  offset is therefore +1.9e-6 +/- 7.5e-6 per step, consistent with zero. RD-P2 REFUTED: no remainder near 0.0001.
  The counterfactual is the outcome. The wheel keeps exactly 17/56 in the long run to within about 1e-5, and the
  recorded line at 0.30365 was the spectrum's resolution. What remains to explain is the balance. Forward kicks are
  more frequent but smaller (mean 3.26 notches), backward kicks rarer but larger (mean 4.20), and their totals agree
  to 0.2%.
"""
import os
import random
import sys
from collections import Counter
from fractions import Fraction

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_walls as wl                                    # noqa: E402
sys.argv = _argv

U = [int(c) for c in wl.U]
P = 56
TRIALS = int(sys.argv[1]) if len(sys.argv) > 1 else 300
T = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 4256


def kick_of(dn):
    k = (-17 * (dn // 2)) % 28
    return k if k < 14 else k - 28


def column1(R):
    """Column 1 of a right half with initial row R (bit i is site i + 1), wall white at even times."""
    row, c1 = R << 1, []
    for t in range(T):
        c1.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & ~1) | ((t + 1) % 2)
    return c1


def locks(c1):
    out, t, n = [], 0, len(c1)
    while t + P <= n:
        d = next((d for d in range(0, P, 2) if all(c1[t + j] == U[(t + j - d) % P] for j in range(P))), None)
        if d is None:
            t += 1
            continue
        s = t + P
        while s < n and c1[s] == U[(s - d) % P]:
            s += 1
        out.append((t, s, d))
        t = s
    return out


def main():
    rng = random.Random(SEED)
    total_k, total_steps, chains = 0, 0, 0
    fwd, back, by_class = 0, 0, Counter()
    for i in range(TRIALS):
        w = (16, 24, 32, 48, 64)[i % 5]
        lk = locks(column1(rng.getrandbits(w) | 1))
        chain_start, chain_k = None, 0
        for (a, s, d), nxt in zip(lk, lk[1:] + [None]):
            if chain_start is None:
                chain_start, chain_k = a, 0
            if nxt is not None and nxt[0] - s < P:
                k = kick_of((nxt[2] - d) % P)
                chain_k += k
                fwd += k > 0
                back += k < 0
                by_class[((s - d) % P, 1 if k > 0 else -1)] += 1
                continue
            if s > chain_start + P:                                  # close the chain at the end of this lock
                total_k += chain_k
                total_steps += s - chain_start
                chains += 1
            chain_start = None
    f = Fraction(17, 56) + Fraction(total_k, 28 * total_steps)
    off = float(f - Fraction(17, 56))
    print(f"SEED {SEED}: {TRIALS} trials, T = {T}; {chains} chains, {total_steps} steps on chains, "
          f"{fwd} forward and {back} backward kicks")
    print("kicks by (departure class, sign):", dict(sorted(by_class.items())))
    print(f"net kick sum {total_k} notches; effective rotation number {float(f):.7f} (17/56 = {17/56:.7f}); "
          f"offset {off:+.7f}")
    print("RD-P1", "HELD" if total_k > 0 else "REFUTED")
    print("RD-P2", "HELD" if 0.00002 <= off <= 0.0002 else "REFUTED")


if __name__ == "__main__":
    main()
