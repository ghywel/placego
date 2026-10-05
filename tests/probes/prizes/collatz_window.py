#!/usr/bin/env python3
"""collatz_window.py: the window principle on the Collatz side. While an orbit fits in n binary digits, its parity
sequence cannot repeat a block of n symbols. (Local, 2026-10-05; PRIZE-PROBLEMS.md section 7.5; the Rule 30 twin is
RULE30-PRIZE.md section 8.58.)

RUN-ON:     cpu, one core, pure Python 3
COMMAND:    python3 tests/probes/prizes/collatz_window.py
COST:       about a minute.

THE STATEMENTS (proved in section 7.5; all follow from Terras's bijection between residues modulo 2^n and parity
blocks of length n, which holds on the rationals with odd denominator).
  W1 (equal futures, congruent presents). Let x = N/D with D odd, and let N_i / D be its i-th iterate under
     T(x) = x/2 or (3x + 1)/2. The parity blocks of length n that start at times i and j are equal exactly when
     2^n divides N_i - N_j. So the common length of the two futures is the 2-adic valuation of N_i - N_j.
  W2 (complexity is at least the sojourn). If the orbit of x is infinite, the number p(n) of different blocks of
     length n in its parity sequence is at least the number of iterates with |N_i| < 2^(n-1), which is at least
     (n - 1 - log2(|N| + D)) / log2(3/2).
  W3 (corollary). No rational with odd denominator has a Sturmian parity sequence (p(n) = n + 1), of any slope and
     any intercept; nor any aperiodic parity sequence with p(n) <= 1.7 n for infinitely many n.

PREDICTIONS, written 2026-10-05 before this script's first run.
  CW0 (control, must hold): Terras's bijection, for every residue modulo 2^n, n = 1 .. 12.
  CW1 (W1, must hold): for x = N/D with D in {1, 3, 5, 7} and |N| <= 300, and every pair of times i < j <= 80 with
      N_i != N_j, the common length of the two parity futures (capped at 64) equals the 2-adic valuation of
      N_i - N_j (capped at 64).
  CW2 (must hold): for the same x and n = 1 .. 24, the number of different parity blocks of length n starting at
      times 0 .. 80 equals the number of different residues of N_i modulo 2^n over those times.
  CW3 (blind; what W3 says in digits): for eight Sturmian words (slopes log3(2), 0.7, 0.8, 0.9; intercepts 0 and
      0.37), the first 3000 binary digits of the 2-adic number with that parity sequence have, among the last
      1500, a share of ones between 0.45 and 0.55 and no period of 500 or less.
  CW4 (blind): the least non-negative integer with the first M symbols of each of those words as its parity
      prefix has more than M - 24 binary digits, for M = 500, 1000, 2000, 3000 (it does not stay small).
  CF  (counterfactual, must fail): CW1 with the valuation taken of N_i + N_j is false for most pairs.
REFUTED-BY: CW0, CW1, CW2 or CF failing (the proof or the instrument); CW3 or CW4 the other way.

OUTCOME of the first run, 2026-10-05 (9 seconds):
  CW0, CW1, CW2 PASSED (4,910,527 pairs, 0 failures). CW4 HELD.
  CF FAILED by bad design: the valuation of N_i + N_j equals that of N_i - N_j for 75% of pairs, because both are
  0 or 1 for most pairs. Replaced by CF2 below.
  CW3 REFUTED, by my error: the slopes 0.7, 0.8 and 0.9 are rational, so those words are periodic, not Sturmian,
  and their 2-adic numbers are cycle points with periodic digits. The probe found exactly that: period 21 at slope
  4/5 (the cycle denominator is 2^5 - 3^4 = -49, and 2 has order 21 modulo 49) and period 166 at slope 7/10 with
  intercept 0.37 (denominator 2^10 - 3^7 = -1163). At intercept 0 floating point misplaced the floor at exact
  integers, so that word was not exactly periodic. For the one irrational slope, log3(2), the digits were balanced
  and aperiodic at both intercepts.

ADDENDUM, written 2026-10-05 after the first run and before the second.
  CF2 (counterfactual, must fail): CW1 with the wrong partner, the valuation of N_i - N_(j+1), is false for most
      pairs.
  CW3b (blind; replaces CW3): irrational slopes log3(2), 1/sqrt(2), pi/4 and e/3, intercepts 0 and 0.37: among
      digits 1500 to 3000 the share of ones is between 0.45 and 0.55 and there is no period of 500 or less.
  CW5 (the accident made a control; must hold): for the exactly periodic words of slopes 4/5 and 7/10 (built with
      exact fractions, intercepts 0 and 1/3), the digits are eventually periodic with periods 21 and 166.

OUTCOME of the second run, 2026-10-05: ALL CHECKS PASS. CF2 PASSED (the wrong partner gives the right valuation
  for 1,280,490 of 4,910,527 pairs, about a quarter, as chance gives). CW5 PASSED (periods 21, 21, 166, 166).
  CW3b HELD (ones 0.48 to 0.52 at all eight words, no period up to 500). CW4 HELD (the least integer with the first
  M parity symbols has M - 4 to M digits).
"""
import math, sys
from fractions import Fraction

FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def orbit_numerators(N, D, steps):
    """numerators N_i of T^i(N/D) (denominator D odd, fixed) and the parities"""
    nums, par = [], []
    for _ in range(steps):
        nums.append(N)
        b = N & 1                                   # N/D is odd exactly when N is (D is odd)
        par.append(b)
        N = (3 * N + D) // 2 if b else N // 2
    return nums, par


def val2(m, cap=64):
    if m == 0:
        return cap
    v = (m & -m).bit_length() - 1
    return min(v, cap)


def controls():
    ok = True
    for n in range(1, 13):
        seen = set()
        for r in range(1 << n):
            x, bits = r, 0
            for i in range(n):
                b = x & 1
                bits |= b << i
                x = (3 * x + 1) // 2 if b else x // 2
            seen.add(bits)
        ok &= len(seen) == 1 << n
    report("CW0 Terras's bijection, n = 1 .. 12", ok)


def part_identity(T=80, cap=64):
    bad = cf_true = cf2_true = pairs = 0
    bad2 = 0
    for D in (1, 3, 5, 7):
        for N in range(-300, 301):
            if N == 0 or math.gcd(abs(N), D) != 1:
                continue
            nums, par = orbit_numerators(N, D, T + cap + 1)
            for i in range(T):
                for j in range(i + 1, T + 1):
                    if nums[i] == nums[j]:
                        continue
                    n = 0
                    while n < cap and par[i + n] == par[j + n]:
                        n += 1
                    pairs += 1
                    bad += n != val2(nums[i] - nums[j], cap)
                    cf_true += n == val2(nums[i] + nums[j], cap)
                    cf2_true += n == val2(nums[i] - nums[j + 1], cap)
            for n in range(1, 25):
                blocks = {tuple(par[i:i + n]) for i in range(T + 1)}
                residues = {nums[i] % (1 << n) for i in range(T + 1)}
                bad2 += len(blocks) != len(residues)
    report("CW1 the common future of two iterates is the 2-adic valuation of their difference", bad == 0,
           f"{pairs} pairs, {bad} failures")
    report("CW2 blocks of length n and residues modulo 2^n are equally many", bad2 == 0, f"{bad2} failures")
    print(f"NOTE  CF (first design, a failed counterfactual, see the header): true for {cf_true} of {pairs}",
          flush=True)
    report("CF2 with the wrong partner N_(j+1) the identity fails for most pairs", cf2_true < pairs / 2,
           f"true for {cf2_true} of {pairs}")


def sturmian(alpha, theta, n):
    """the mechanical word of slope alpha and intercept theta; exact when both are Fractions"""
    return [1 if math.floor(theta + (s + 1) * alpha) > math.floor(theta + s * alpha) else 0 for s in range(n)]


def tail_period(digits, lo, pmax):
    tail = digits[lo:]
    return next((p for p in range(1, pmax + 1) if all(tail[k] == tail[k + p] for k in range(len(tail) - p))), None)


def phi_mod(v, M):
    """the residue modulo 2^M of the 2-adic number whose parity sequence starts with v[0:M] (Bernstein's series)"""
    mod = 1 << M
    inv3 = pow(3, -1, mod)
    x, p = 0, inv3
    for d in range(M):
        if v[d]:
            x = (x - (p << d)) % mod                 # the term 2^d / 3^(i+1) for the i-th one
            p = (p * inv3) % mod
    return x


def part_sturmian():
    crit = math.log(2) / math.log(3)
    words = [(a, t) for a in (crit, 2 ** -0.5, math.pi / 4, math.e / 3) for t in (0.0, 0.37)]
    okp = True
    for (num, den), want in (((4, 5), 21), ((7, 10), 166)):
        for theta in (Fraction(0), Fraction(1, 3)):
            v = sturmian(Fraction(num, den), theta, 3000)
            x = phi_mod(v, 3000)
            per = tail_period([(x >> k) & 1 for k in range(3000)], 1500, 500)
            okp &= per == want
            print(f"   rational slope {num}/{den}, intercept {theta}: digit period {per} (expected {want})", flush=True)
    report("CW5 periodic parity words give periodic digits, periods 21 and 166", okp)
    ok3 = ok4 = True
    notes = []
    for a, t in words:
        v = sturmian(a, t, 3000)
        x = phi_mod(v, 3000)
        y, good = x, True                            # control: x has that parity prefix
        for s in range(3000):
            if (y & 1) != v[s]:
                good = False; break
            y = (3 * y + 1) // 2 if y & 1 else y // 2
        if not good:
            report(f"control: the series reproduces the parity prefix (slope {a:.4f}, intercept {t})", False)
        digits = [(x >> k) & 1 for k in range(3000)]
        tail = digits[1500:]
        share = sum(tail) / len(tail)
        period = next((p for p in range(1, 501) if all(tail[k] == tail[k + p] for k in range(len(tail) - p))), None)
        ok3 &= 0.45 <= share <= 0.55 and period is None
        sizes = []
        for M in (500, 1000, 2000, 3000):
            xm = x % (1 << M)
            sizes.append(xm.bit_length())
            ok4 &= xm.bit_length() > M - 24
        notes.append(f"slope {a:.3f} intercept {t}: ones {share:.3f}, period {period}, digits {sizes}")
    for nline in notes:
        print("   " + nline, flush=True)
    verdict("CW3b irrational slopes: the 2-adic digits are balanced and have no period up to 500", ok3)
    verdict("CW4 the least integer with the parity prefix has more than M - 24 digits", ok4)


def main():
    controls()
    part_identity()
    part_sturmian()
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
