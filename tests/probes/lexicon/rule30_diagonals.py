#!/usr/bin/env python3
"""rule30_diagonals.py: the pyramid as a stack of rational numbers. Every diagonal of Rule 30 from a single 1 is
eventually periodic, and the centre column reads them along a Cantor diagonal.

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_diagonals.py [LOGT=18]
COST:       about two minutes on one core.

The owner (2026-10-05): "I find myself wondering if there is more than one irrational number embedded."

The diagonals. Write c(t, x) for the cell at time t and position x (single 1 at t = 0, x = 0). The d-th right diagonal
is D_d(t) = c(t, t - d) and the e-th left diagonal is E_e(t) = c(t, e - t), both read from t = 0, so each starts with
the zeros above the pyramid. The centre cell at time t is D_t(t) = E_t(t): the t-th digit of the t-th diagonal. So the
centre column is the Cantor diagonal through two lists of numbers, the right diagonals 0.D_d(0) D_d(1) ... and the
left diagonals 0.E_e(0) E_e(1) ....

The right diagonals are rational, with periods that are powers of 2 (Jen, 1990; Rowland, Complex Systems 16, gives the
first diagonal of each period, a(n) = 1, 3, 4, 6, 7, 9, 15, 16, 24, ...). A short proof (this script's, not checked
against the papers): Rule 30 is c' = l XOR (c OR r), so D_d(t) = D_d(t-1) XOR (D_{d-1}(t-1) OR D_{d-2}(t-1)). That
makes D_d a running XOR of u = D_{d-1} OR D_{d-2}, starting from D_d(0) = [d = 0], with D_{-1} = D_{-2} = 0 and
D_0 = 1. If D_{d-1} and D_{d-2} are purely periodic with power-of-2 periods, u is purely periodic with period p, the
larger of the two. Then D_d(t + p) = D_d(t) XOR X, where X is the XOR of one period of u, so D_d is purely periodic
with period p (X = 0, or a divisor of p) or exactly 2p (X = 1). By induction every right diagonal is purely periodic,
and p_d <= 2 max(p_{d-1}, p_{d-2}). A lower bound: D_d(t) = 0 for t < ceil(d/2) (above the pyramid) and
D_d(ceil(d/2)) = 1 (the pyramid's left edge, or the cell next to it, which is always 1). So the period exceeds
ceil(d/2), and the periods grow without bound.

The left diagonals are only eventually periodic (Rowland, section 5). The same induction: E_e(t) = E_{e-2}(t-1) XOR
(E_{e-1}(t-1) OR E_e(t-1)). Whenever E_{e-1} = 1 the new cell is NOT E_{e-2}, whatever the old one was: a reset. So
once E_{e-1} and E_{e-2} are periodic, one period later E_e is periodic with a period dividing the larger of theirs,
unless E_{e-1} is eventually 0 (no resets), and then the period can double. So a left period can grow only just after an
eventually-zero left diagonal. It came out of this review, before any run of the left side.

An exploratory look (2026-10-05, 2^14 steps, right diagonals only, read from the centre, not recorded) reproduced a(n)
and found periods up to 2^12 by diagonal 29. The review before the first run moved the reading to t = 0 (to make the
Cantor diagonal exact and the proof apply) and fixed an off-by-one in the a(n) check.

PREDICTIONS, written 2026-10-05 before this script's first run:
  DG0 (control; proved above): every right diagonal up to the last whose period fits twice in the window is purely
      periodic from t = 0 with a power-of-2 period; p_d <= 2 max(p_{d-1}, p_{d-2}) and p_d > ceil(d/2); the first
      diagonals with periods 2, 4, ..., 512 are 1, 3, 4, 6, 7, 9, 15, 16, 24 (Rowland's a(n)); and the centre column
      equals D_t(t) and E_t(t) at every t.
  DG1 (blind, but after the exploratory look): the periods keep doubling at a steady rate. log2 of the period grows by
      0.3 to 0.5 per diagonal, by a least-squares fit over diagonals 10 to the last one measured.
  DG2 (blind): every right diagonal from 10 on has a period above 2^(0.3 d), so the centre column reads diagonal t
      before it has repeated once (2^(0.3 t) > t for t >= 10).
  DG3 (control; proved above): every left diagonal up to e = 63 is eventually periodic with a power-of-2 period, and
      its period exceeds the larger of the two before it only when the one before it is eventually 0.
  DG4 (blind, uncertain): the left periods stay small. Eventually-zero left diagonals are rare, so every left period
      up to e = 63 is at most 4. The left side's disorder lives in the transients, not the periods.
  DG5 (blind): the transients grow, and the centre lies inside them. Every left diagonal from e = 10 has a preperiod
      m_e > e (it is still in its transient where it crosses column 0). The transients end on a line moving left at
      between 0.5 and 1 cell per step: (e - m_e) / m_e, fitted as e / m_e - 1 by least squares of m_e on e through
      0, lies in [-1, -0.5].
  CF  (counterfactual): the same test finds no power-of-2 period in random sequences of length 2^(LOGT-3), nor in the
      centre column itself over the window.
REFUTED-BY: DG0, DG3 or CF failing (the instrument or the proof); DG1, DG2, DG4 or DG5 failing.

A FAILURE OF METHOD, recorded before the first full run: a smoke test at LOGT = 11 (2,048 steps), meant only to check
that the script runs, printed its verdicts before this file was committed, and they were seen. DG0, DG3 and CF passed
and DG2 held; DG1 (slope 0.243), DG4 (left periods of 8 from e = 29, after an eventually-zero diagonal at e = 28) and
DG5 (m_e <= e for e = 10 to 19; m_e ~ 1.34 e) failed. The predictions above are left exactly as written before it, so
the full run at 2^18 is not blind for DG1, DG4 and DG5.

OUTCOME of the first full run, 2026-10-05 (LOGT = 18, 20 seconds): DG0 PASSED. Right diagonals 0 to 42 are purely
periodic from t = 0 (diagonal 43's period no longer fits twice in 2^18 steps); a(n) = 1, 3, 4, 6, 7, 9, 15, 16, 24 as
Rowland gives; both bounds hold; the centre column is D_t(t) = E_t(t). log2 of the periods, d = 0 .. 42: 0, 1, 1, 2, 3,
3, 4, 5, 5, 6 (six times), 7, 8 (eight times), 9, 10, 10, 11, 11, 12 (five times), 13, 13, 14, 15, 15, 16, 16, 17, 17.
DG1 HELD (slope 0.353 over 10 to 42: a doubling every 2.8 diagonals; the smoke test's 0.243 saw only up to 26). DG2 HELD
(no exceptions; its parenthetical was wrong, since 2^(0.3 t) > t only from t = 12, but every measured period exceeds d
for d = 3 to 63, those beyond 42 exceeding 2^17). DG3 PASSED: left diagonals 0 to 63 are all eventually periodic; only e
= 2, 7 and 28 are eventually 0, and the period grows exactly after them, to 2 at e = 3, 4 at e = 8 and 8 at e = 29. DG4
REFUTED (periods of 8 from e = 29), but the left periods stay tiny: 8 at e = 63, where the right side has 2^17 at d =
41. DG5 REFUTED (not blind): m_e <= e for e = 10 to 17 and 19, m_e > e from 20 on; m_e = 23, 55, 91 at e = 20, 40, 63;
the fit through 0 gives m_e ~ 1.34 e (a line at -0.25 cells per step), but m_e / e was still growing at e = 63 (1.44).
CF PASSED.
The two sides are opposite kinds of rational number: the right purely periodic with periods doubling, the left a growing
transient followed by a period of at most 8.
"""
import math, random, sys

LOGT = int(sys.argv[1]) if len(sys.argv) > 1 else 18
T = 1 << LOGT
D = 64
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def as_int(bits):
    """Bit i of the result is bits[i]."""
    return int("".join(map(str, reversed(bits))), 2) if bits else 0


def pow2_period(S, n, eventually=False):
    """Smallest power of 2 p with s[i] == s[i + p] for i < n - p (pure), or for pre <= i < n - p (eventually), the
    periodic part spanning at least two periods and, when eventual, at least a quarter of the window (two periods
    alone would pass a random sequence at p = 1 half the time); s is held as the integer S (bit i = s[i]). Returns
    (p, pre) or (None, None)."""
    p = 1
    while 2 * p <= n:
        diff = (S ^ (S >> p)) & ((1 << (n - p)) - 1)
        if diff == 0:
            return p, 0
        if eventually:
            pre = diff.bit_length()                    # one past the last mismatch
            if n - pre >= max(2 * p, n // 4):
                return p, pre
        p *= 2
    return None, None


def bit_column(wins, j):
    """The sequence of bit j of each window, as an integer (bit t = bit j of wins[t])."""
    return int("".join("1" if (w >> j) & 1 else "0" for w in reversed(wins)), 2)


def main():
    row = 1 << T                                       # bit x + T holds cell x
    mask = (1 << (2 * T + 3)) - 1
    W = (1 << 64) - 1
    rwin, lwin, centre = [], [], []
    for t in range(T):
        rwin.append((row >> (t - 63 + T)) & W)         # bit j: cell x = t - 63 + j, so D_d(t) is bit 63 - d
        lwin.append((row >> (T - t)) & W)              # bit e: cell x = e - t, so E_e(t) is bit e
        centre.append((row >> T) & 1)
        row = ((row << 1) ^ (row | (row >> 1))) & mask
    ident = all(centre[t] == (rwin[t] >> (63 - t)) & 1 == (lwin[t] >> t) & 1 for t in range(D))
    Rint = [bit_column(rwin, 63 - d) for d in range(D)]
    per = {}
    for d in range(D):
        p, _ = pow2_period(Rint[d], T)
        if p is None:
            break
        per[d] = p
    last = max(per)
    print("   right diagonal periods (log2): " + ", ".join(f"{d}: {int(math.log2(p))}" for d, p in per.items()),
          flush=True)
    first = {}
    for d, p in sorted(per.items()):
        first.setdefault(int(math.log2(p)), d)
    a = [first.get(k) for k in range(1, 10)]
    doubling = all(per[d] <= 2 * max(per.get(d - 1, 1), per.get(d - 2, 1)) for d in per)
    lower = all(per[d] > math.ceil(d / 2) for d in per)
    report("DG0 right diagonals purely periodic from t = 0 with power-of-2 periods; p_d <= 2 max of the two before; "
           "p_d > ceil(d/2); Rowland's a(n); the centre column is D_t(t) = E_t(t)",
           a == [1, 3, 4, 6, 7, 9, 15, 16, 24] and doubling and lower and ident,
           f"diagonals 0 to {last} periodic; a(n) found {a}; doubling bound {doubling}; lower bound {lower}; "
           f"centre identity {ident}")
    xs = [d for d in per if d >= 10]
    ys = [math.log2(per[d]) for d in xs]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    verdict("DG1 log2 of the period grows by 0.3 to 0.5 per diagonal", 0.3 <= slope <= 0.5,
            f"slope {slope:.3f} over diagonals 10 to {xs[-1]}")
    low = [d for d in xs if per[d] <= 2 ** (0.3 * d)]
    verdict("DG2 every right diagonal from 10 on has a period above 2^(0.3 d)", not low, f"exceptions {low}")

    lp = [pow2_period(bit_column(lwin, e), T, eventually=True) for e in range(D)]
    print("   left diagonals (period, preperiod): " + ", ".join(f"{e}: {p}, {pre}" for e, (p, pre) in enumerate(lp)),
          flush=True)
    ok3 = all(p is not None for p, _ in lp)
    zero = [p == 1 and (lwin[-1] >> e) & 1 == 0 for e, (p, _) in enumerate(lp)]
    grows = []
    if ok3:
        for e in range(2, D):
            if lp[e][0] > max(lp[e - 1][0], lp[e - 2][0]):
                grows.append(e)
                ok3 &= zero[e - 1]
    report("DG3 every left diagonal up to 63 eventually periodic with a power-of-2 period; it grows only after an "
           "eventually-zero diagonal", ok3,
           f"eventually zero: {[e for e in range(D) if zero[e]]}; period grows at {grows}")
    big = [e for e, (p, _) in enumerate(lp) if p is not None and p > 4]
    verdict("DG4 every left period up to e = 63 is at most 4", not big, f"periods above 4 at {big}")
    es = [e for e in range(10, D) if lp[e][1] is not None]
    inside = [e for e in es if lp[e][1] <= e]
    c = sum(e * lp[e][1] for e in es) / sum(e * e for e in es) if es else float("nan")
    v = 1 / c - 1 if c else float("nan")
    verdict("DG5 every left diagonal from 10 is still in its transient at column 0 (m_e > e), and the transients end "
            "on a line moving left at 0.5 to 1 cell per step", not inside and -1 <= v <= -0.5,
            f"exceptions {inside}; m_e ~ {c:.2f} e, so the line moves at {v:+.3f} cells per step")

    rng = random.Random(7)
    n = T >> 3
    rnd = [as_int([rng.getrandbits(1) for _ in range(n)]) for _ in range(16)]
    cp = pow2_period(as_int(centre), T, eventually=True)[0]
    report("CF random sequences and the centre column show no power-of-2 period",
           all(pow2_period(S, n, eventually=True)[0] is None for S in rnd) and cp is None,
           f"centre column: {cp}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
