#!/usr/bin/env python3
"""rule30_sturmian.py: almost every quasi-periodic column 1 is excluded. A consequence of Theorem A (section 8.54),
stated and proved in RULE30-PRIZE.md section 8.57. (Local, 2026-10-05; PERIOD-TWO.md section 7, question 7.)

RUN-ON:     cpu, one core (Python 3 with numpy; the control needs a C compiler for ladder.c)
COMMAND:    python3 tests/probes/lexicon/rule30_sturmian.py [SAMPLES=300]
COST:       about a minute.

THE STATEMENT (Theorem E, proved in section 8.57). Let column 0 be 0101... and let column 1's visible bits be a
rotation coding c_s = 1 if frac(theta + s alpha) >= 1 - alpha, else 0, with alpha irrational (a Sturmian sequence).
Then for Lebesgue-almost every theta the forced left half is not eventually zero.
The mechanism. Let q be a denominator of a convergent of alpha, and v the first s with c_s != c_(s+q). Then c has
period q on the visible window [0, v - 1 + q], and Theorem A forces v <= q + (L - 1)/2 if the left half is zero
beyond depth L. For a typical theta this fails at infinitely many q. The zero-run form (Theorem B on a window): if
columns 0 and 1 are P-periodic on the times [0, b], every zero run of row 0 that starts at a depth d with
2(d + P - 1) + 1 <= b has length at most 2P - 2. Here P = 2q and b = 2(v - 1 + q) + 1, so every zero run starting
at depth d <= v - q is at most 4q - 2 cells long.

PREDICTIONS, written 2026-10-05 before this script's first run.
  SP0 (controls, must hold): the row routine gives the stripes 1010... for c = 0, and equals ladder.c's
      "left" mode on 20 random columns 1.
  SP1 (the zero-run form, must hold): alpha the golden rotation, SAMPLES random theta, the forced row to depth 2000,
      q over the Fibonacci numbers 1 to 233: every zero run starting at depth d <= v - q is at most 4q - 2 long.
  SP2 (blind; the metric statement, no Rule 30 in it): among 100,000 random theta, the share with
      v(q_n) <= q_n + (L - 1)/2 for every n up to 20 (Fibonacci q up to 6765), at L = 9, is below 1%.
  SP3 (blind): the share falls by a factor between 0.3 and 0.7 for each n from 10 to 20 (the guess: about
      q |q alpha| = 0.447 at each scale, with some dependence between neighbouring scales).
  CF  (counterfactual, must fail): SP1's bound with 2q - 2 in place of 4q - 2 is violated.
REFUTED-BY: SP0, SP1 or CF failing (the proof or the instrument); SP2 or SP3 the other way.

OUTCOME: (written after the first run, below)
"""
import pathlib, random, subprocess, sys, tempfile
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 300
ALPHA = (5 ** 0.5 - 1) / 2
FIB = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def prefix_xor(x, nbits):
    s = 1
    while s < nbits:
        x ^= x << s
        s <<= 1
    return x & ((1 << nbits) - 1)


def forced_row(col1, depth):
    """row 0 of the forced left half, depths 1..depth, for column 0 = 0101... and column 1 = col1 (a function of
    time; only even times matter). records.c's anti-diagonal recurrence, on Python integers."""
    P, Q, row = 0, 0, []                        # A_0 = (tau(0)) = 0, A_{-1} empty
    for k in range(1, depth + 1):
        X = (P << 1) | (Q << 2)
        if (k - 1) % 2 == 0 and col1(k - 1):
            X |= 2
        X = (X & ~1) | (k & 1)
        A = prefix_xor(X, k + 1)
        row.append((A >> k) & 1)
        Q, P = P, A
    return row


def sturmian(theta, n):
    x = (theta + ALPHA * np.arange(n)) % 1.0
    return (x >= 1 - ALPHA).astype(np.uint8)


def controls():
    ok_stripes = forced_row(lambda t: 0, 60) == [k % 2 for k in range(1, 61)]
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_sturmian_ladder"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "ladder.c")], check=True)
    rng = random.Random(1005)
    ok_ladder = True
    for _ in range(20):
        bits = [rng.randint(0, 1) for _ in range(120)]
        out = subprocess.run([str(exe), "left", "".join(map(str, bits))], capture_output=True, text=True,
                             check=True).stdout.strip()
        mine = "".join(map(str, forced_row(lambda t: bits[t], 120)))
        ok_ladder &= out == mine
    report("SP0 the row routine: stripes for c = 0, and ladder.c's left mode on 20 random columns", ok_stripes and
           ok_ladder)


def zero_runs(row):
    """(start depth, length) of every maximal zero run"""
    runs, d = [], 0
    while d < len(row):
        if row[d] == 0:
            e = d
            while e < len(row) and row[e] == 0:
                e += 1
            runs.append((d + 1, e - d)); d = e
        else:
            d += 1
    return runs


def part_rows():
    rng = random.Random(54)
    depth, viol, cf_viol, tested, longest = 2000, 0, 0, 0, 0
    for _ in range(SAMPLES):
        theta = rng.random()
        c = sturmian(theta, depth // 2 + 400)
        row = forced_row(lambda t: int(c[t // 2]), depth)
        runs = zero_runs(row)
        longest = max(longest, max(r for _, r in runs))
        for q in FIB[:12]:
            diff = np.nonzero(c[:-q] != c[q:])[0]
            v = int(diff[0]) if len(diff) else len(c)
            if v - q < 1 or 2 * (v - 1 + q) + 1 > 2 * (len(c) - q):   # nothing to test, or beyond what was built
                continue
            for d, r in runs:
                if d <= v - q and d + r - 1 < depth:      # a complete run starting inside the tested range
                    tested += 1
                    viol += r > 4 * q - 2
                    cf_viol += r > 2 * q - 2
    report("SP1 every zero run starting at depth d <= v - q is at most 4q - 2 long", viol == 0,
           f"{tested} runs tested over {SAMPLES} thetas, {viol} violations; longest run seen anywhere {longest}")
    report("CF  with 2q - 2 the bound is violated", cf_viol > 0, f"{cf_viol} violations")


def part_metric(L=9, n_theta=100000):
    rng = np.random.default_rng(57)
    theta = rng.random(n_theta)
    alive = np.ones(n_theta, dtype=bool)
    shares = []
    for n, q in enumerate(FIB[:19], start=2):               # n = 2 .. 20, q = 1 .. 6765
        limit = q + (L - 1) // 2                            # v <= limit is needed
        ok = np.zeros(n_theta, dtype=bool)
        x = theta.copy()
        for s in range(limit + 1):                          # is c_s != c_(s+q) for some s <= limit?
            a = (x % 1.0) >= 1 - ALPHA
            b = ((x + q * ALPHA) % 1.0) >= 1 - ALPHA
            ok |= a != b
            x += ALPHA
        alive &= ok
        shares.append((n, q, alive.mean()))
    s20 = shares[-1][2]
    verdict("SP2 the share allowed at every scale up to n = 20 is below 1% (L = 9)", s20 < 0.01,
            ", ".join(f"n {n}: {s:.4f}" for n, q, s in shares if n in (6, 8, 10, 12, 14, 16, 18, 20)))
    ratios = [shares[i][2] / shares[i - 1][2] for i in range(1, len(shares)) if shares[i][0] >= 10 and
              shares[i - 1][2] > 0]
    verdict("SP3 the share falls by 0.3 to 0.7 per scale, n = 10 to 20", bool(ratios) and
            all(0.3 <= r <= 0.7 for r in ratios), ", ".join(f"{r:.2f}" for r in ratios))


def main():
    controls()
    part_rows()
    part_metric()
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
