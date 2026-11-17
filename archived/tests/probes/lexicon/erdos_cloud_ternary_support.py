"""How many nonzero ternary digits does 2^n have? The unexpected check of RULE30-PRIZE.md 8.101 (Cloud, 2026-10-14).

Senge and Straus (1973) proved that only finitely many integers have few nonzero digits in two multiplicatively
independent bases at once; Stewart (1980) made it effective. 2^n has one nonzero binary digit, so its number of
nonzero ternary digits tends to infinity. Erdős's question asks which nonzero digits occur (some must be 2), which those
theorems do not see. This probe only looks at the count.

Predictions, committed before the run (8.101):
  E1  With at most K nonzero ternary digits, K = 1 .. 6, only n <= 20 appear.
  E2  The fewest nonzero digits over n in (N/2, N] grows roughly linearly, near the coin's (2/3) n log_3 2 = 0.42 n,
      far above Stewart's log n / log log n floor.
  Counterfactual: a large n with few nonzero digits.
Controls: the ternary digits are checked against Python's own conversion by re-summing them; the digit-2-free
exponents found must be exactly 0, 2 and 8 below 2000 (Erdős's known list).
"""
import math

NMAX = 2000


def ternary(m):
    digits = []
    while m:
        m, d = divmod(m, 3)
        digits.append(d)
    return digits


def main():
    counts, free = {}, []
    for n in range(NMAX + 1):
        d = ternary(2 ** n)
        assert sum(x * 3 ** i for i, x in enumerate(d)) == 2 ** n
        counts[n] = sum(1 for x in d if x)
        if 2 not in d:
            free.append(n)
    print("control: n <= %d with 2^n free of the ternary digit 2:" % NMAX, free)
    assert free == [0, 2, 8]
    for k in range(1, 7):
        print("E1 K=%d: n with at most %d nonzero ternary digits:" % (k, k), [n for n in counts if counts[n] <= k])
    print("E2: N, fewest nonzero digits over n in (N/2, N], ratio to 0.42 n at the minimiser, log n / log log n")
    n_ = 16
    while n_ <= NMAX:
        lo = n_ // 2 + 1
        m = min(range(lo, n_ + 1), key=lambda n: counts[n])
        floor = math.log(m) / math.log(math.log(m))
        print("  %5d  %4d (at n = %d)  %.2f  %.2f" % (n_, counts[m], m, counts[m] / (0.42 * m), floor))
        n_ *= 2


if __name__ == "__main__":
    main()
