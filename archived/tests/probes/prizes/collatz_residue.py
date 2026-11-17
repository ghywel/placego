#!/usr/bin/env python3
"""collatz_residue.py: what the state after the free bits is. For r < 2^k, the k-th iterate y = T^k(r) of the Collatz
map T(n) = n/2 or (3n + 1)/2 is the least residue of a Syracuse offset modulo 3^a, for all but a vanishing share of
r. (Local, 2026-10-05; COLLATZ-PRIZE.md section 4; PERIOD-TWO.md section 7, question 9.)

RUN-ON:     cpu, one core, pure Python 3
COMMAND:    python3 tests/probes/prizes/collatz_residue.py [KMAX=18]
COST:       about 10 seconds.

THE STATEMENT (proved in COLLATZ-PRIZE.md section 4; a failure here means the proof or this script is wrong). Let r < 2^k have
parity vector v over its first k steps, with a odd steps at positions i_0 < ... < i_(a-1). Terras's formula is
    T^k(r) = (3^a r + c_v) / 2^k,   c_v = sum over j of 3^(a-1-j) 2^(i_j).
So y = T^k(r) satisfies y = c_v / 2^k modulo 3^a. And 0 <= y < 3^a + (3/2)^a, because r < 2^k and
c_v / 2^k < (3/2)^a. So y is the least non-negative residue rho of c_v 2^(-k) modulo 3^a, or rho + 3^a.

PREDICTIONS, written 2026-10-05 before this script's first run.
  CR0 (control, must hold): the formula for c_v reproduces T^k(r) for every r < 2^k, k = 1 .. KMAX.
  CR1 (the statement, must hold): for every such r with a >= 1, y is rho or rho + 3^a.
  CR2 (blind; how often the second case): for k >= 12, the share of r with y = rho + 3^a is below 2^(-k/3). (The
      guess: it needs r / 2^k > 1 - 2^(-a), and a is about k/2.)
  CF  (counterfactual, must fail): with the residue taken modulo 3^(a+1) in place of 3^a, the statement is false
      for most r.
REFUTED-BY: CR0, CR1 or CF failing (the proof or the instrument); CR2 the other way.

OUTCOME of the first run, 2026-10-05 (KMAX 18, 4 seconds): CR0, CR1 and CF PASSED (modulo 3^(a+1) the statement
is true for 87,381 of 262,143 numbers, one third, as it must be). CR2 HELD, and the truth is stronger than the guess:
the share with y = rho + 3^a is exactly 0 at every k. The reason, found after the run: r - 2^k is negative and has
the same first k parities, T keeps negative integers negative, and T^k(r - 2^k) = T^k(r) - 3^a. So T^k(r) < 3^a
always, and y is exactly the least residue. Section 7.4 states it that way.
"""
import sys

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 18
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def main():
    ok0 = ok1 = True
    shares = {}
    cf_true = cf_total = 0
    for k in range(1, KMAX + 1):
        second = total = 0
        for r in range(1 << k):
            n, odd_pos = r, []
            for i in range(k):
                if n & 1:
                    odd_pos.append(i); n = (3 * n + 1) >> 1
                else:
                    n >>= 1
            y, a = n, len(odd_pos)
            c = sum(3 ** (a - 1 - j) * (1 << i) for j, i in enumerate(odd_pos))
            if (3 ** a * r + c) != (y << k):
                ok0 = False
            if a == 0:
                continue
            m = 3 ** a
            rho = (c * pow(1 << k, -1, m)) % m
            total += 1
            if y == rho + m:
                second += 1
            elif y != rho:
                ok1 = False
            if k == KMAX:                                   # the counterfactual, at the largest k only
                m2 = 3 ** (a + 1)
                rho2 = (c * pow(1 << k, -1, m2)) % m2
                cf_total += 1
                cf_true += y in (rho2, rho2 + m2)
        shares[k] = second / total
    report("CR0 Terras's formula reproduces T^k(r)", ok0)
    report("CR1 y is the least residue of c_v 2^(-k) mod 3^a, or that plus 3^a", ok1)
    report("CF  modulo 3^(a+1) the statement fails for most r", cf_true < cf_total / 2,
           f"true for {cf_true} of {cf_total} at k = {KMAX}")
    big = [k for k in shares if k >= 12]
    verdict("CR2 the share with y = rho + 3^a is below 2^(-k/3) for k >= 12",
            all(shares[k] < 2 ** (-k / 3) for k in big),
            ", ".join(f"k {k}: {shares[k]:.2e}" for k in (8, 12, 16, KMAX) if k in shares))
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
