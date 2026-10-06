#!/usr/bin/env python3
"""rule30_ring_census.py: CONSTELLATION.md row 10, the cycles of Rule 30 on rings, n = 1 .. 24, complete (ring_census.c
visits every one of the 2^n states once and certifies each cycle by a state and a length). Literature first (the
row's instruction): OEIS A334497 gives the maximum period by n and A334496 the period reached from the single
cell, both to n = 20 at least; NKS note 6.4 records the n = 13 exception (maximum 832, single cell 260) and an
estimate 2^(0.61 (n+1)) for the maximum period. A search of the OEIS for the NUMBER of cycles, the states on
cycles, the transients or the gliding cycles of Rule 30 on rings found nothing; those four are what this census
adds, with the two known sequences as its controls. (Local, 2026-10-06; RULE30-PRIZE.md section 8.67.)

RUN-ON:     cpu, one core, about 300 MB at n = 24
COMMAND:    python3 tests/probes/lexicon/rule30_ring_census.py [NMAX=24]
COST:       under a minute.

SEEN BEFORE these predictions: the two OEIS sequences to n = 20; the 7-ring's cycles (RULE30-PRIZE.md section 5);
nothing about cycle counts, periodic states, transients or gliders at any n.

PREDICTIONS, written 2026-10-06 before the first run.
  RC0 (control, must hold): the maximum periods equal A334497 and the single-cell periods equal A334496 for n <= 20.
  CF  (counterfactual, must fail): the single-cell period equals the maximum period at every n <= 24. It fails at
      n = 7 already (4 against 63): the single cell is not the generic seed on a ring either.
  RC1 (blind): the number of periodic states P(n) grows like 2^(a n) with a between 0.6 and 0.8 over n = 12 .. 24
      (a least-squares slope of log2 P against n); the periodic set is a vanishing fraction of the ring.
  RC2 (blind): the number of cycles is divisor-sensitive: for at least 5 of the 6 primes p = 7, 11, 13, 17, 19, 23,
      c(p) < max(c(p - 1), c(p + 1)), because a composite n inherits every cycle of the rings dividing it.
  RC3 (blind): the longest transient is short against the cycles: at n = 24 it is below 200 and below the maximum
      period at every n >= 10.
  RC4 (blind): gliding cycles (a cycle mapped to itself by rotation, i.e. a travelling pattern) exist at n = 23, so
      c(23) - 1 is not a multiple of 23 (on a prime ring every non-gliding cycle other than the white fixed point
      comes in a rotation class of exactly 23 cycles).
REFUTED-BY: RC0 failing or CF holding (the engine); RC1 to RC4 the other way. What would change my mind: a cycle
count that is smooth in n (no divisor structure) would say the ring's cycles do not come from sub-rings, which is
how the 7-periodic tails of section 5 were explained.

OUTCOME of the first run, 2026-10-06 (n = 1 .. 24, 40 seconds; the table is rule30_ring_census.txt). RC0 PASSED, and
  after the run the OEIS b-file of A334497 (to n = 36) was checked against n = 21 .. 24 as well: 2793, 3553, 38249,
  185040 agree. CF PASSED (n = 7: 4 against 63; n = 13: 260 against 832; n = 19: 247 against 3705; n = 20, 21). RC1
  REFUTED: a = 0.553, and the periodic states are wildly irregular (4,350 at n = 18, 4,124 at 19, 33,926 at 20, 16,619
  at 21, 194,991 at 24). RC2 REFUTED at 7 and 11 (hits 13, 17, 19, 23 only): the primes 7 and 11 have MORE cycles than
  their neighbours because one short cycle there comes in a full rotation class (seven 4-cycles at n = 7, eleven
  17-cycles at n = 11). RC3 REFUTED twice: the longest transient at n = 24 is 9,568, and at n = 21 (4,308 against a
  maximum period of 2,793) and n = 22 (5,477 against 3,553) the longest transient EXCEEDS the longest cycle. RC4 HELD,
  and more than held: at n = 13, 17, 19 and 23 EVERY cycle is gliding (5 of 5, 7 of 7, 5 of 5, 4 of 4). The reason is
  a pigeonhole, not a mechanism: rotation permutes the cycles of each length, its orbits on a prime ring have size 1
  or p, and at those n every cycle length occurs once, so every cycle is fixed by rotation, i.e. rotation by one cell
  is a power of the time map on it. At n = 7 and 11 the one repeated length is the one non-gliding class.

DEEP ADDENDUM, written 2026-10-06 before the second run (python3 rule30_ring_census.py deep): n = 25 to 29, one n at
  a time (12 GB at n = 29). Controls from the OEIS b-files, read on 2026-10-06 before the run: A334497 (maximum
  period) 588425, 312156, 240300, 249165, 1466066 and A334496 (single cell) 588425, 312156, 240300, 249165, 833808
  for n = 25 .. 29.
  RD0 (control, must hold): both sequences reproduced at n = 25 .. 29.
  CF  (must fail): the periodic states number 2^n at some n (the map would be a bijection; Rule 30 on a ring is not
      injective).
  RD1 (blind, the prime-ring test): at the prime n = 29 every cycle length occurs once, so every cycle is a glider
      (gliding count = cycle count).
  RD2 (blind): at some n in 25 .. 28 the longest transient exceeds the longest cycle, as at 21 and 22.
  RD3 (blind): fewer than 100 cycles at every n in 25 .. 29.
  REFUTED-BY: RD0 failing or CF holding (the engine); RD1 to RD3 the other way. What would change my mind: a repeated
  cycle length at n = 29 (then 29 copies by rotation, and non-gliding cycles) would say the distinct lengths at 13,
  17, 19, 23 were small-number luck rather than a pattern of prime rings.
"""
import pathlib, re, subprocess, sys, tempfile
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "rule30_ring_census.txt"
NMAX = int(next((a for a in sys.argv[1:] if a.isdigit()), 24))
FAILS = 0
A334497 = [1, 1, 1, 8, 5, 1, 63, 40, 171, 15, 154, 102, 832, 1428, 1455, 6016, 10846, 2844, 3705, 6150]
A334496 = [1, 1, 1, 8, 5, 1, 4, 40, 72, 15, 154, 102, 260, 1428, 1455, 6016, 10846, 2844, 247, 3420]


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def deep():
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_ring_census"
    arch = ["-mcpu=apple-m1"] if sys.platform == "darwin" else []
    subprocess.run(["cc", "-O3", *arch, "-o", str(exe), str(HERE / "ring_census.c")], check=True)
    A497 = {25: 588425, 26: 312156, 27: 240300, 28: 249165, 29: 1466066}
    A496 = {25: 588425, 26: 312156, 27: 240300, 28: 249165, 29: 833808}
    rows = {}
    for n in range(25, 30):
        out = subprocess.run([str(exe), str(n), str(n)], capture_output=True, text=True, check=True).stdout
        with open(OUT, "a") as fh:
            fh.write(out)
        print(out, end="", flush=True)
        m = re.match(r"n (\d+) cycles (\d+) periodic (\d+) maxper (\d+) single (\d+) maxtransient (\d+) gliding (\d+)", out)
        nn, c, P, mp, sg, mt, gl = map(int, m.groups()); rows[n] = dict(c=c, P=P, mp=mp, sg=sg, mt=mt, gl=gl)
    report("RD0 A334497 and A334496 reproduced at n = 25 .. 29",
           all(rows[n]["mp"] == A497[n] and rows[n]["sg"] == A496[n] for n in rows),
           f"max {[rows[n]['mp'] for n in rows]}; single {[rows[n]['sg'] for n in rows]}")
    report("CF  periodic states = 2^n at some n is FALSE", all(rows[n]["P"] < 2**n for n in rows))
    verdict("RD1 at n = 29 every cycle is a glider", rows[29]["gl"] == rows[29]["c"], f"gliding {rows[29]['gl']} of {rows[29]['c']}")
    verdict("RD2 some n in 25 .. 28 has longest transient > longest cycle",
            any(rows[n]["mt"] > rows[n]["mp"] for n in range(25, 29)), f"{[(n, rows[n]['mt'], rows[n]['mp']) for n in range(25, 29)]}")
    verdict("RD3 fewer than 100 cycles at every n", all(rows[n]["c"] < 100 for n in rows), f"{[rows[n]['c'] for n in rows]}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def main():
    if "deep" in sys.argv[1:]:
        deep()
        return
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_ring_census"
    arch = ["-mcpu=apple-m1"] if sys.platform == "darwin" else []
    subprocess.run(["cc", "-O3", *arch, "-o", str(exe), str(HERE / "ring_census.c")], check=True)
    out = subprocess.run([str(exe), str(NMAX)], capture_output=True, text=True, check=True).stdout
    with open(OUT, "a") as fh:
        fh.write(out)
    print(out, flush=True)
    rows = {}
    for ln in out.splitlines():
        m = re.match(r"n (\d+) cycles (\d+) periodic (\d+) maxper (\d+) single (\d+) maxtransient (\d+) gliding (\d+)", ln)
        if m:
            n, c, P, mp, sg, mt, gl = map(int, m.groups()); rows[n] = dict(c=c, P=P, mp=mp, sg=sg, mt=mt, gl=gl)
    k = min(20, NMAX)
    report("RC0 maximum periods = A334497 and single-cell periods = A334496 for n <= 20",
           [rows[n]["mp"] for n in range(1, k + 1)] == A334497[:k] and [rows[n]["sg"] for n in range(1, k + 1)] == A334496[:k],
           f"max {[rows[n]['mp'] for n in range(1, k + 1)]}; single {[rows[n]['sg'] for n in range(1, k + 1)]}")
    report("CF  single-cell period = maximum period at every n is FALSE", any(rows[n]["sg"] != rows[n]["mp"] for n in rows))
    ns = [n for n in range(12, NMAX + 1)]
    a = np.polyfit(ns, [np.log2(rows[n]["P"]) for n in ns], 1)[0]
    verdict("RC1 periodic states grow like 2^(a n), 0.6 <= a <= 0.8", 0.6 <= a <= 0.8, f"a = {a:.3f}; P = {[rows[n]['P'] for n in ns]}")
    primes = [p for p in (7, 11, 13, 17, 19, 23) if p + 1 <= NMAX]
    hits = [p for p in primes if rows[p]["c"] < max(rows[p - 1]["c"], rows[p + 1]["c"])]
    verdict("RC2 divisor-sensitive cycle counts at 5 of 6 primes", len(hits) >= len(primes) - 1,
            f"hits {hits}; c = {[rows[n]['c'] for n in range(1, NMAX + 1)]}")
    verdict("RC3 longest transient below 200 at n = 24 and below the maximum period for n >= 10",
            (NMAX < 24 or rows[24]["mt"] < 200) and all(rows[n]["mt"] < rows[n]["mp"] for n in range(10, NMAX + 1)),
            f"transients {[rows[n]['mt'] for n in range(1, NMAX + 1)]}")
    if NMAX >= 23:
        verdict("RC4 gliding cycles exist at n = 23", rows[23]["gl"] > 0 and (rows[23]["c"] - 1) % 23 != 0,
                f"gliding {rows[23]['gl']}, cycles {rows[23]['c']}, (c-1) mod 23 = {(rows[23]['c'] - 1) % 23}")
    print("   gliding by n:", [rows[n]["gl"] for n in range(1, NMAX + 1)])
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
