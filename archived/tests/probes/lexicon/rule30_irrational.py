#!/usr/bin/env python3
"""rule30_irrational.py: Rule 30's columns read as binary numbers. Do they look like typical irrational numbers?

RUN-ON:     cpu (pure Python 3, standard library; exact integer arithmetic)
COMMAND:    python3 tests/probes/lexicon/rule30_irrational.py [NBITS=20000]
COST:       about a minute on one core.

The owner (2026-10-05): "If the pattern never repeats itself, given the kick and the wheel, is it possible to describe
the problem generally as an irrational number? Do any of the known irrational numbers look similar?"

The dictionary. A column read as the binary number 0.b0 b1 b2 ... is eventually periodic exactly when that number is
rational. So Prize Problem 1 says that the centre column's number, from a single 1, is irrational. The period-2 case
says it is never eventually 0.0101..., the pattern of 1/3. In this project's construction (section 5), each right
half gives the forced left half's number 0.L1 L2 L3 ..., and a finite counterexample would make that number a
terminating binary fraction.

The test. Almost every real number (all but a set of measure zero) obeys three laws of its continued fraction
[a0; a1, a2, ...]: the geometric mean of a1..an tends to Khinchin's constant K0 = 2.68545; the share of partial
quotients equal to 1 tends to log2(4/3) = 0.41504 (Gauss-Kuzmin); and (1/n) ln q_n, q_n the n-th convergent's
denominator, tends to pi^2 / (12 ln 2) = 1.18657 (Levy). Proved irrationals such as pi and e were proved by their
structure, not by such statistics; the statistics say only whether a number looks typical. From NBITS binary digits
only the partial quotients whose convergent has q_n < 2^(NBITS/2) are reliable; only those are used.

PREDICTIONS, written 2026-10-05 before this script's first run:
  IR0 (controls): sqrt(2) gives the partial quotients 1; 2, 2, 2, ...; a coin-flip number obeys all three laws
      (geometric mean within 0.1 of K0, share of 1s within 0.02, Levy within 0.05); and 1/3, cut to NBITS digits,
      shows a partial quotient above 2^(NBITS/2) within its first three, the mark of a near-rational.
  IR1 (blind): the centre column from a single 1 looks like a typical irrational: all three laws within those
      tolerances, and no reliable partial quotient above 10^7.
  IR2 (blind): so does the forced left half's number for a real right half (the 20-cell right half 0xB5E3F).
  IR3 (blind, uncertain): column 1 next to column 0 = 0101..., whose digits carry only about 0.04 bits per step
      (rule30_metric.py), does NOT look typical: its geometric mean lies outside [2.55, 2.85] or its share of 1s is
      outside 0.415 +- 0.03.
REFUTED-BY: IR0 failing (the instrument); IR1, IR2 or IR3 failing.

OUTCOME of the first run, 2026-10-05 (NBITS = 20,000): IR0 passed (sqrt(2): 7,864 terms, all 2; coin flips: geometric
mean 2.699, share of 1s 0.4185, Levy 1.193; 1/3: [3, ~2^19999]). IR1 HELD: the centre column from a single 1 gives
2.669, 0.413, 1.181 over 5,871 terms, largest 2,625. IR2 HELD: the forced left half of 0xB5E3F gives 2.683, 0.416,
1.185, largest 7,345. IR3 HELD, but not as foreseen: column 1 next to 0101... has only 3 reliable terms, [1, 3, 1],
then a giant partial quotient. Its first digits are a long clean stretch of the wheel, so the number lies extremely
close to a fraction (a Liouville-like near-rational), and the statistics never start. Its later stretches do not
show in a continued fraction, which reads a number from its first digits.
"""
import math, random, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
NBITS = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
sys.argv = _argv
K0, GK1, LEVY = 2.6854520010, math.log2(4 / 3), math.pi ** 2 / (12 * math.log(2))
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def cf_stats(bits):
    """Continued fraction of 0.b0 b1 b2 ... (binary), reliable terms only: (terms, geo mean, share of 1s, Levy, max)."""
    n = len(bits)
    num = int("".join(map(str, bits)), 2) if bits else 0
    den = 1 << n
    terms, q1, q0 = [], 1, 0                        # q_{-1} = 0, q_0 = 1
    a, b = num, den
    a0, a, b = a // b, b, a % b                     # integer part (0 here), then 1 / fraction
    while b:
        t = a // b
        q = t * q1 + q0
        if q.bit_length() > n // 2:
            break
        terms.append(t)
        q0, q1 = q1, q
        a, b = b, a - t * b
    if not terms:
        return terms, float("nan"), float("nan"), float("nan"), 0
    geo = math.exp(sum(math.log(t) for t in terms) / len(terms))
    share1 = sum(1 for t in terms if t == 1) / len(terms)
    levy = (q1.bit_length() * math.log(2)) / len(terms)
    return terms, geo, share1, levy, max(terms)


def typical(st, tol=(0.1, 0.02, 0.05)):
    _, g, s, l, _ = st
    return abs(g - K0) <= tol[0] and abs(s - GK1) <= tol[1] and abs(l - LEVY) <= tol[2]


def show(name, st):
    terms, g, s, l, mx = st
    print(f"   {name}: {len(terms)} reliable terms; geometric mean {g:.4f} (K0 {K0:.4f}); share of 1s {s:.4f} "
          f"({GK1:.4f}); Levy {l:.4f} ({LEVY:.4f}); largest {mx if mx < 10 ** 12 else f'~2^{mx.bit_length()}'}; "
          f"first terms {terms[:12]}", flush=True)


def main():
    rng = random.Random(1979)
    # controls
    s2 = math.isqrt(2 << (2 * NBITS))               # sqrt(2) * 2^NBITS
    sqrt2_bits = [int(c) for c in bin(s2)[3:]][:NBITS]   # fractional digits of sqrt(2)
    st_s2 = cf_stats(sqrt2_bits)
    coin = cf_stats([rng.getrandbits(1) for _ in range(NBITS)])
    third = cf_stats([t % 2 for t in range(NBITS)])
    third_big = any(t.bit_length() > NBITS // 2 for t in third[0][:3]) or len(third[0]) <= 3
    # for 1/3 the huge quotient breaks the reliability cut-off, so read it from the raw expansion
    num, den = int("".join(str(t % 2) for t in range(NBITS)), 2), 1 << NBITS
    raw = []
    a, b = den, num
    while b and len(raw) < 4:
        raw.append(a // b)
        a, b = b, a % b
    third_big = any(x.bit_length() > NBITS // 2 for x in raw[:3])
    for name, st in (("sqrt(2)", st_s2), ("coin flips", coin)):
        show(name, st)
    print(f"   1/3 cut to {NBITS} digits: first partial quotients {[x if x < 10 ** 12 else f'~2^{x.bit_length()}' for x in raw]}")
    ok0 = st_s2[0][:1] == [2] and all(t == 2 for t in st_s2[0]) and typical(coin) and third_big
    report("IR0 controls: sqrt(2) gives 2, 2, 2, ...; coin flips are typical; 1/3 shows a giant partial quotient", ok0)

    # the centre column from a single 1
    T = NBITS
    row, c = 1 << (T + 1), []
    mask = (1 << (2 * T + 4)) - 1
    for _ in range(T):
        c.append((row >> (T + 1)) & 1)
        row = ((row << 1) ^ (row | (row >> 1))) & mask
    st_c = cf_stats(c)
    show("centre column, single 1", st_c)
    verdict("IR1 the centre column looks like a typical irrational", typical(st_c) and st_c[4] < 10 ** 7)

    L = r30.forced_left(0xB5E3F, [t % 2 for t in range(NBITS + 2)], NBITS)
    st_l = cf_stats(L)
    show("forced left half, right half 0xB5E3F", st_l)
    verdict("IR2 the forced left half's number looks typical", typical(st_l) and st_l[4] < 10 ** 7)

    R = rng.getrandbits(2400) | (1 << 2399)
    steps = NBITS + 600
    mask = (1 << (R.bit_length() + steps + 3)) - 1
    row, col1 = R << 1, []
    for t in range(steps):
        if t >= 600:
            col1.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
    st_1 = cf_stats(col1)
    show("column 1 next to 0101...", st_1)
    verdict("IR3 column 1 next to 0101... does not look typical (geometric mean outside [2.55, 2.85] or share of 1s "
            "outside 0.415 +- 0.03)", not (2.55 <= st_1[1] <= 2.85) or abs(st_1[2] - GK1) > 0.03)
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
