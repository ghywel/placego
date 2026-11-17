#!/usr/bin/env python3
"""sc4_euclid.py: spark SC4 (SPARKS.md). Euclid's algorithm, still on shift.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/sparks/sc4_euclid.py
COST:       about a minute.

Predictions (published in SPARKS.md before this ran): the mean number of division steps for random pairs up to N,
fitted against ln N for N = 10^2 ... 10^8 (200,000 pairs each), has slope within 0.02 of 12 ln 2 / pi^2 = 0.8428; and an
exhaustive search of all pairs up to N finds none needing more steps than the largest consecutive Fibonacci pair up
to N, for N in {100, 500, 1000, 2000}. Fail: slope outside 0.80 to 0.88, or any pair beating the Fibonacci pair.
Control: steps(1, 1) = 1, steps(F_k, F_(k+1)) = k - 1 for the Fibonacci numbers F_1 = F_2 = 1.
"""
import math, random

random.seed(20261007)


def steps(a, b):
    n = 0
    while b:
        a, b = b, a % b
        n += 1
    return n


def fib_upto(N):
    f = [1, 1]
    while f[-1] + f[-2] <= N:
        f.append(f[-1] + f[-2])
    return f


def main():
    assert steps(1, 1) == 1
    f = fib_upto(10**6)
    assert all(steps(f[k + 1], f[k]) == k for k in range(1, len(f) - 1))  # F_(k+2) over F_(k+1): k steps
    target = 12 * math.log(2) / math.pi**2
    xs, ys = [], []
    print("   N         mean steps")
    for e in range(2, 9):
        N = 10**e
        m = sum(steps(random.randint(1, N), random.randint(1, N)) for _ in range(200_000)) / 200_000
        xs.append(math.log(N)); ys.append(m)
        print(f"  10^{e}   {m:8.4f}")
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    print(f"fitted slope {slope:.4f} against 12 ln 2 / pi^2 = {target:.4f}; intercept {my - slope * mx:.3f}")
    ok = abs(slope - target) <= 0.02
    for N in (100, 500, 1000, 2000):
        best, arg = 0, None
        for b in range(1, N + 1):
            for a in range(1, b + 1):
                s = steps(b, a)
                if s > best:
                    best, arg = s, (a, b)
        fu = fib_upto(N)
        fs = steps(fu[-1], fu[-2])
        beaten = best > fs
        ok &= not beaten
        print(f"  pairs up to {N}: most steps {best} at {arg}; Fibonacci pair ({fu[-2]}, {fu[-1]}) takes {fs}"
              f"{'  BEATEN' if beaten else ''}")
    print("PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
