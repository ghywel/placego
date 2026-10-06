#!/usr/bin/env python3
"""collatz_threehalves.py: Dubickas's conjecture, measured. For x_0 = 1 and x_n = ceil(3 x_(n-1) / 2) (the Josephus
sequence A061419, the 3x+1 map without the halving of even numbers), Dubickas (Glasgow Math. J. 51, 2009; read in
full 2026-10-06, COLLATZ-PRIZE.md section 5) proves that the parity sequence X has complexity P(X, n) > 1.7095 n and
conjectures P(X, n) = 2^n: every parity block of every length occurs. That is the Collatz-side shape of Rule 30's
"cost side as a count" (RULE30-PRIZE.md section 8.58): the trace is as complex as it can be. (Local, 2026-10-06;
COLLATZ-PRIZE.md section 6, a new row.)

RUN-ON:     cpu, one core (pure Python 3, big integers)
COMMAND:    python3 tests/probes/prizes/collatz_threehalves.py [STEPS=4000000]
COST:       about five minutes (x_n has 0.585 n bits, so the last terms are 300 KB integers).

WHY A COUNT OF BLOCKS IS A COUNT OF RESIDUES. For this map x mod 2^n determines the next n parities (Terras's
bijection for the 3/2 map), so P(X, n) over a stretch of the orbit equals the number of distinct residues x_i mod
2^n visited on that stretch, and P(X, n) = 2^n means the orbit visits every residue class modulo 2^n.

PREDICTIONS, written 2026-10-06 before this script's first run.
  TH0 (control, must hold): the first 40 terms equal A061419 as computed independently by the recurrence written
      out longhand (1, 2, 3, 5, 8, 12, 18, 27, 41, 62, ...), and blocks equal residues: the number of distinct
      parity blocks of length n over the first 100,000 terms equals the number of distinct residues mod 2^n there,
      for n = 1 .. 12.
  TH1 (blind; the conjecture at small n): P(X, n) = 2^n for every n <= 16 over the first STEPS terms (a coupon
      collector needs about 2^n ln 2^n terms: 7.3 x 10^5 at n = 16).
  TH2 (blind): at n = 18 the orbit has visited at least 99.9% of the 2^18 residues after STEPS terms (the coupon
      collector's 1 - exp(-STEPS / 2^18) = 1 - e^(-15) if the residues were visited like fair coins); at n = 20 at
      least 97% (1 - e^(-3.8) = 0.978).
  TH3 (blind; the share of ones): the parity sequence has ones at a share within 0.002 of 1/2 over STEPS terms.
  CF  (counterfactual, must fail): the map x -> 2x (p/q = 2/1) has a constant parity sequence, P = 1 for every n;
      and the periodic control x -> x mod 2^12 + ... is not needed: the first is enough to show the counter sees
      low complexity when it is there.
REFUTED-BY: TH0 or CF failing (the instrument); TH1 to TH3 the other way.

OUTCOME: (to be recorded after the first run)
"""
import math, sys

STEPS = int(sys.argv[1]) if len(sys.argv) > 1 else 4000000
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def main():
    NMAX = 20
    mask = (1 << NMAX) - 1
    x = 1
    seen = [set() for _ in range(NMAX + 1)]              # residues mod 2^n visited, n = 1..NMAX
    ones = 0
    first = []
    par = []
    for i in range(STEPS):
        if i < 40:
            first.append(x)
        r = x & mask
        b = r & 1
        ones += b
        if i < 100000:
            par.append(b)
        for n in range(1, NMAX + 1):
            seen[n].add(r & ((1 << n) - 1))
        x = (3 * x + b) >> 1                               # ceil(3x/2) = (3x + (x mod 2)) / 2
    # TH0: the recurrence longhand, and blocks = residues on the first 100,000 terms
    y, long = 1, []
    for _ in range(40):
        long.append(y)
        y = y * 3 // 2 if y % 2 == 0 else (y * 3 + 1) // 2
    ok0 = long == first and long[:10] == [1, 2, 3, 5, 8, 12, 18, 27, 41, 62]
    blocks_ok = True
    x2 = 1
    res = [set() for _ in range(13)]
    for i in range(100000):
        for n in range(1, 13):
            res[n].add(x2 & ((1 << n) - 1))
        x2 = (3 * x2 + (x2 & 1)) >> 1
    for n in range(1, 13):
        blocks = {tuple(par[i:i + n]) for i in range(100000 - n + 1)}
        blocks_ok &= len(blocks) == len(res[n])
    report("TH0 the first terms are A061419, and parity blocks of length n are as many as residues mod 2^n", ok0 and blocks_ok)
    # CF: x -> 2x
    z, pz = 1, set()
    for _ in range(1000):
        pz.add(z & 1); z *= 2
    report("CF  the map x -> 2x has a constant parity sequence (P = 1)", len(pz) == 1)
    full = [n for n in range(1, NMAX + 1) if len(seen[n]) == 1 << n]
    verdict("TH1 P(X, n) = 2^n for every n <= 16", all(n in full for n in range(1, 17)),
            f"full at n = {full}; at 17..20: " + ", ".join(f"{len(seen[n])}/{1 << n}" for n in range(17, NMAX + 1)))
    c18, c20 = len(seen[18]) / (1 << 18), len(seen[20]) / (1 << 20)
    verdict("TH2 coverage >= 99.9% at n = 18 and >= 97% at n = 20", c18 >= 0.999 and c20 >= 0.97,
            f"{c18:.5f}, {c20:.5f}; a coin would give {1 - math.exp(-STEPS / (1 << 18)):.5f}, "
            f"{1 - math.exp(-STEPS / (1 << 20)):.5f}")
    share = ones / STEPS
    verdict("TH3 the share of ones within 0.002 of 1/2", abs(share - 0.5) <= 0.002, f"{share:.5f}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
