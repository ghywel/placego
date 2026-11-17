#!/usr/bin/env python3
"""sc2_socks.py: spark SC2 (SPARKS.md). What a mismatched drawer cannot lose.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/sparks/sc2_socks.py
COST:       about a minute.

Predictions (published in SPARKS.md before this ran): losing k of the 2n socks of n matched pairs at random leaves
k(2n - k)/(2n - 1) orphans on average; two socks drawn at random from n icon pairs match with chance 1/(2n - 1), so the
wait for a matching pair of icons averages 2n - 1 mornings; an all-black drawer orphans no sock while two remain.
Pass: every simulated mean within three standard errors of its formula. Fail: any beyond four.
Control: the same code with k = 0 must give no orphans, and with n = 1 must match every time.
"""
import math, random

random.seed(20261007)
TRIALS = 200_000


def mean_se(xs):
    m = sum(xs) / len(xs)
    v = sum((x - m) ** 2 for x in xs) / (len(xs) - 1)
    return m, math.sqrt(v / len(xs))


def orphans(n, k):
    lost = set(random.sample(range(2 * n), k))
    return sum(1 for s in range(2 * n) if s not in lost and (s ^ 1) in lost)


def black_orphans(n, k):
    left = 2 * n - k
    return 0 if left >= 2 else left  # any two black socks make a pair


def wait_for_match(n):
    days = 1
    while True:
        a, b = random.sample(range(2 * n), 2)
        if a ^ 1 == b:
            return days
        days += 1


def main():
    worst = 0.0
    assert all(orphans(5, 0) == 0 for _ in range(100))
    assert all(wait_for_match(1) == 1 for _ in range(100))
    print("orphans after losing k socks from n matched pairs")
    for n in (5, 10, 20):
        for k in (1, 3, 5, 10):
            if k > 2 * n:
                continue
            m, se = mean_se([orphans(n, k) for _ in range(TRIALS)])
            f = k * (2 * n - k) / (2 * n - 1)
            z = 0.0 if se == 0 and abs(m - f) < 1e-12 else (m - f) / se
            worst = max(worst, abs(z))
            assert black_orphans(n, k) == 0
            print(f"  n={n:2d} k={k:2d}  simulated {m:7.4f}  formula {f:7.4f}  z={z:+.2f}  all-black drawer 0")
    print("mornings until a matching pair of icons")
    for n in (5, 10, 20):
        m, se = mean_se([wait_for_match(n) for _ in range(TRIALS // 10)])
        z = (m - (2 * n - 1)) / se
        worst = max(worst, abs(z))
        print(f"  n={n:2d}  simulated {m:7.3f}  formula {2 * n - 1:3d}  z={z:+.2f}")
    print(f"largest |z| = {worst:.2f}: {'PASS' if worst <= 3 else 'FAIL (beyond 4)' if worst > 4 else 'BORDERLINE'}")


if __name__ == "__main__":
    main()
