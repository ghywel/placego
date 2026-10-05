#!/usr/bin/env python3
"""rule30_jenclock.py: Jen's theorem with a clock. Two quantitative forms of "two adjacent columns are never both
eventually periodic" (RULE30-PRIZE.md section 8.13), stated and proved in section 8.54, and checked here.
(Local, 2026-10-05; PERIOD-TWO.md section 7, questions 5 and 7.)

RUN-ON:     cpu, one core
COMMAND:    python3 tests/probes/lexicon/rule30_jenclock.py [QMAX=10] [WMAX=10]
COST:       about a minute (jenclock.c does the periodic words; the finite seeds are numpy).

THE TWO STATEMENTS (proved in section 8.54; a violation here means the proof or this script is wrong).
  Theorem A (a window cannot outlast the edge). In a nonzero configuration whose leftmost black cell is L >= 0 cells
    to the left of column i at time 0, if columns i and i+1 are both P-periodic on the time window [a, b] (the pair
    at t equals the pair at t + P whenever a <= t and t + P <= b), then b <= 2a + L + 2P - 1.
  Theorem B (a zero run cannot outlast two periods). If columns 0 and 1 are both P-periodic from time 0, and column 0
    is not zero, every run of zeros in row 0 of the forced left half has length at most 2P - 2.
Jen's theorem is the case b = infinity of A. For column 0 = 0101... and a column 1 whose visible (even-time) bits
have least period q, P = 2q, so B says every zero run is at most 4q - 2 cells long.

PREDICTIONS, written 2026-10-05 before this script's first run.
  JC0 (control, must hold): with columns 0 and 1 both zero, jenclock.c reports an infinite run.
  JC1 (Theorem B, must hold): for every q from 1 to QMAX and every word of least period q, the longest zero run is at
      most 4q - 2, none is infinite, and every word is decided.
  JC2 (blind; how tight is B?): for q >= 4 the longest run over all words of period q is at most 2.5 q + 4, and for
      q >= 6 it is at least q. (The guess: a run is the coin's best over about 2^q words times a depth period of
      about 2^(1.2 q), so about 2.2 q, against the theorem's 4q - 2.)
  JC3 (Theorem A, must hold): over every seed of width 1 to WMAX, every column pair from the seed's left end to 12
      cells past its right end, every P from 1 to 8 and every complete window in 400 steps: b <= 2a + L + 2P - 1.
  JC4 (blind; how tight is A?): the least slack (2a + L + 2P - 1) - b over all those windows is at most 2, and it is
      reached only by columns with L <= 3 (next to the left edge).
  CF (counterfactual, must fail): the same check against the bound without its 2P term, b <= 2a + L - 1, is violated.
REFUTED-BY: JC0, JC1, JC3 or CF failing (the proof or the instrument); JC2 or JC4 the other way.

OUTCOME of the first run, 2026-10-05 (QMAX 10, WMAX 10, 6 seconds on the M5):
  JC0 PASSED. JC1 PASSED: longest zero runs 1, 6, 5, 6, 9, 10, 10, 17, 14, 17 for q = 1 .. 10 against the bounds
  2, 6, 10, .., 38; the bound is attained at q = 2; no word infinite or undecided (longest depth cycle 25,000).
  JC2 HELD (about 1.7 q for q >= 3). JC3 PASSED: 5,254,135 complete windows, 0 violations. CF PASSED: 17,500
  violations of the bound without its 2P term. JC4 REFUTED as worded: the least slack is 0 (seed 101, L = 0, P = 1,
  window [0, 1]), but windows with slack <= 2 reach L = 12, not L <= 3. Post hoc: all 1,734 of them start at a <= 3
  (the latest at a = 3), and the long ones are zeros waiting for an edge (the single cell seen from L cells to its
  right). So Theorem A is sharp at the start and loose later.
  A correction made while writing section 8.54: Theorem B needs P >= 2 (for P = 1 the bound is 1, the stripes).
  Every case run here has P = 2q >= 2.
"""
import pathlib, subprocess, sys, tempfile
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
QMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10
WMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 10
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def part_b():
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_jenclock"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "jenclock.c")], check=True)
    out = subprocess.run([str(exe), "zero"], capture_output=True, text=True, check=True).stdout
    report("JC0 the zero columns give an infinite run", "run -1" in out, out.strip())
    rows = []
    ok = True
    for q in range(1, QMAX + 1):
        out = subprocess.run([str(exe), str(q)], capture_output=True, text=True, check=True).stdout
        line = [ln for ln in out.splitlines() if ln.startswith("SUMMARY")][0]
        f = line.replace(";", " ").replace(",", " ").replace("(", " ").replace(")", " ").split()
        words = int(f[f.index("words") - 1])
        longest = int(f[f.index("run") + 1])
        infinite = int(f[f.index("infinite") + 1])
        undecided = int(f[f.index("undecided") + 1])
        lam = int(f[-1])
        rows.append((q, words, longest, 4 * q - 2, infinite, undecided, lam))
        ok &= longest <= 4 * q - 2 and infinite == 0 and undecided == 0
        print(f"   q {q:2d}: {words:5d} words, longest zero run {longest:3d} (bound {4 * q - 2:3d}), "
              f"longest depth cycle {lam}", flush=True)
    report("JC1 Theorem B: every zero run is at most 4q - 2", ok)
    big = [r for r in rows if r[0] >= 4]
    held = all(r[2] <= 2.5 * r[0] + 4 for r in big) and all(r[2] >= r[0] for r in rows if r[0] >= 6)
    verdict("JC2 the longest run lies between q and 2.5 q + 4", held,
            ", ".join(f"q {r[0]}: {r[2]}" for r in rows))
    return rows


def step(x):
    """one Rule 30 step on a 1-D uint8 array with zero boundaries"""
    left = np.zeros_like(x); left[1:] = x[:-1]
    right = np.zeros_like(x); right[:-1] = x[1:]
    return left ^ (x | right)


def part_a(T=400, pmax=8):
    worst = None                     # (slack, w, seed, column offset L, P, a, b)
    violations = cf_violations = windows = 0
    near = []
    for w in range(1, WMAX + 1):
        inner = max(w - 2, 0)
        for s in range(1 << inner):
            bits = [1] + [(s >> i) & 1 for i in range(inner)] + ([1] if w > 1 else [])
            width = w + 2 * T + 8
            x = np.zeros(width, dtype=np.uint8)
            off = T + 4                                   # the seed's left end cell sits at index off
            x[off:off + w] = bits
            hist = np.zeros((T + 1, width), dtype=np.uint8)
            hist[0] = x
            for t in range(T):
                x = step(x); hist[t + 1] = x
            for L in range(0, w + 12):                    # column i = left end + L
                i = off + L
                pair = hist[:, i].astype(np.int8) * 2 + hist[:, i + 1]
                for P in range(1, pmax + 1):
                    eq = pair[:T + 1 - P] == pair[P:]
                    n = len(eq)
                    t = 0
                    while t < n:
                        if not eq[t]:
                            t += 1; continue
                        a = t
                        while t < n and eq[t]:
                            t += 1
                        if t == n:                        # runs into the horizon: not a complete window
                            break
                        b = (t - 1) + P
                        windows += 1
                        slack = 2 * a + L + 2 * P - 1 - b
                        if slack < 0:
                            violations += 1
                        if 2 * a + L - 1 - b < 0:
                            cf_violations += 1
                        if worst is None or slack < worst[0]:
                            worst = (slack, w, s, L, P, a, b)
                        if slack <= 2:
                            near.append((slack, w, s, L, P, a, b))
    report("JC3 Theorem A: b <= 2a + L + 2P - 1 on every complete window", violations == 0,
           f"{windows} windows, {violations} violations")
    report("CF  without the 2P term the bound is violated", cf_violations > 0, f"{cf_violations} violations")
    maxL = max((n[3] for n in near), default=None)
    verdict("JC4 the least slack is at most 2, only at L <= 3", worst[0] <= 2 and maxL is not None and maxL <= 3,
            f"least slack {worst[0]} at width {worst[1]}, seed {worst[2]}, L {worst[3]}, P {worst[4]}, window "
            f"[{worst[5]}, {worst[6]}]; {len(near)} windows with slack <= 2, largest L among them {maxL}")
    return worst, near


def main():
    part_b()
    part_a()
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
