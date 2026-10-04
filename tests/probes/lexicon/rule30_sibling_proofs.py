#!/usr/bin/env python3
"""rule30_sibling_proofs.py: Proposition 5 (Rule 90 has no finite configuration with a period-two column), checked
by brute force, with its counterfactual, and the check that the same argument fails for Rule 30.

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_sibling_proofs.py [WMAX=6] [NMAX=8]
COST:       seconds.

Proposition 5 (PRIZE-PROBLEMS.md section 8.3). Under Rule 90, x' = l XOR r, let a finite row have support in [-w, w].
Then column 0 is 0 at time 2^n and at time 2^n + 1 whenever 2^n > w + 1.
Proof. A single 1 at position j reaches (0, t) with the value C(t, (t - j)/2) mod 2 (zero if t - j is odd or
|j| > t), and Rule 90 is linear, so column 0 is the XOR of these over the row's ones. By Lucas' theorem C(2^n, k) is
odd only for k = 0 and k = 2^n, which needs j = 2^n or j = -2^n; and C(2^n + 1, k) is odd only for k = 0, 1, 2^n,
2^n + 1, which needs |j| = 2^n + 1 or 2^n - 1. All of these lie outside [-w, w]. QED.
Corollary. Column 0 vanishes infinitely often at even times and at odd times, so if it is eventually periodic with
period 2 its word is 00; a period-two word with a 1 is impossible. (The same holds for every column, by translation.)
This is Rowland's "begin again" in its global form: at row 2^n Rule 90 holds two far-apart copies of the start, and
the middle is empty. Rule 30's restart is only local (Rowland), and the check below shows the conclusion is false for
Rule 30.

CHECKS (a theorem and its controls; nothing here is a prediction):
  P5  every row with support in [-w, w], w <= WMAX, and every n <= NMAX with 2^n > w + 1: column 0 under Rule 90 is
      0 at times 2^n and 2^n + 1.
  CF  (counterfactual, must be caught) the same claim at time 2^n + 2 is false for some row (so the check can fail).
  R30 (contrast) the same claim under Rule 30 is false for some row: the proof does not transfer.
"""
import sys

WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 8
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def column0(rule, bits, w, T):
    """Column 0 for times 0..T of the row whose cell at position i (|i| <= w) is bit i + w of `bits`."""
    off = w + T + 2
    row = bits << (off - w)
    mask = (1 << (2 * off + 1)) - 1
    out = []
    for _ in range(T + 1):
        out.append((row >> off) & 1)
        l, r = (row << 1) & mask, row >> 1
        row = (l ^ r) if rule == 90 else (l ^ (row | r)) & mask
    return out


def main():
    bad = cf = r30 = checked = 0
    for w in range(WMAX + 1):
        T = (1 << NMAX) + 2
        for bits in range(1, 1 << (2 * w + 1)):
            c90 = column0(90, bits, w, T)
            c30 = column0(30, bits, w, T)
            for n in range(1, NMAX + 1):
                t = 1 << n
                if t <= w + 1:
                    continue
                checked += 1
                bad += c90[t] != 0 or c90[t + 1] != 0
                cf += c90[t + 2] != 0
                r30 += c30[t] != 0 or c30[t + 1] != 0
    report("P5 Rule 90: column 0 is 0 at times 2^n and 2^n + 1 once 2^n > w + 1", bad == 0,
           f"{checked} (row, n) pairs, w <= {WMAX}, n <= {NMAX}, {bad} violations")
    report("CF the same claim at time 2^n + 2 is caught as false", cf > 0, f"false for {cf} pairs")
    report("R30 under Rule 30 the claim is false (the proof does not transfer)", r30 > 0, f"false for {r30} pairs")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
