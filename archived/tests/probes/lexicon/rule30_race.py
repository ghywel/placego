#!/usr/bin/env python3
"""rule30_race.py: the information race of the combined game, counted exactly (lead 1, after the owner's zeta note).

RUN-ON:     cpu (pure Python 3, standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_race.py
COST:       about a minute.

Background (RULE30-PRIZE.md sections 8.39, 8.40; PRIOR-ART, the owner's zeta note). Every form of the problem has
led back to one statement: keeping the wall's conditions costs real information. The combined game makes that a
race that can be counted exactly. A finite configuration has a left seed and a right seed of width s. Its centre
column is the word w as long as the wall's conditions hold. Before time s every condition can be met by the left
seed, which the conditions then fix cell by cell, so all 2^s right seeds survive to time s. After s each time
brings one condition, and the only new information is what the right seed delivers to column 1. Survival to time T
depends only on column 1's word up to T, so the natural count is M(s, T): the distinct column-1 words among the
right seeds that survive to T. N(s, T) counts the right seeds themselves.
Bertrand's postulate was proved by a size argument of this shape: a quantity forced to be large, which an empty
interval would make small. Here the race is between the information the right seed delivers and the conditions'
cost. If each condition halves the distinct words, the excess T_BW(s) - s is about log2 M(s, s) divided by the
net loss per step. The question is whether the counts show that balance, or an exact identity of the kind
Chebyshev and Erdos used.

PREDICTIONS, written 2026-10-05 before this script's first run (w = 01 unless named; s = 2 .. 16):
  RA0 (controls, must hold): N(s, s) = 2^s; the largest T with N(s, T) >= 1 equals rule30_words.py's T_BW(s) (01:
      6, 6, 6, 8, 9, 9, 14, 16, 16, 16, 16, 16, 19, 21, 25 at s = 2 .. 16).
  RA1 (blind): beyond the seed the distinct words shrink. The least-squares slope of log2 M(s, T) over T from s to
      T_BW(s) - 2 is a loss of 0.4 to 1.5 bits per step, at each s from 12 to 16.
  RA2 (blind; the bottleneck): by time s the right seed delivers little. log2 M(s, s) lies between 0.2 s and 0.6 s
      at each s from 12 to 16.
  RA3 (blind; the race balances): T_BW(s) - s lies within 3 of log2 M(s, s) / b, with b the loss rate RA1 measures at
      that s, at each s from 12 to 16.
  RA4 (expected null; a Chebyshev-type identity): no linear recurrence of order 5 or less, with rational
      coefficients, holds for N(s, s + e) as a sequence in s (s = 2 .. 16), for any e = 1 .. 4.
  RA5 (random-chaos: the solved extreme, w = 0, Condrey's case, the all-white pair left out): next to a white wall
      x_{t+1}(1) = x_t(1) OR x_t(2), so column 1 turns black once and stays black: M(s, s) <= s + 2 (a control). And
      the race over-predicts there: the excess T_BW(s) - s is at most 1 (seen already, in rule30_words.py's
      addendum) while log2 M(s, s) / b exceeds 2 at s = 16 (blind). Next to a white wall a condition costs more than a
      coin.
REFUTED-BY: RA0 failing (the instrument); RA1 to RA5 failing.

OUTCOME, 2026-10-05 (the first run, 5 seconds):
  RA0 PASSED (N(s, s) = 2^s, and every T_BW(s) as rule30_words.py found).
  RA1 HELD: beyond the seed the distinct column-1 words lose 0.50, 0.91, 0.83, 0.95 and 0.50 bits per step at s = 12
     to 16 (fits over 2 to 7 steps, so rough).
  RA2 HELD: log2 M(s, s) = 4.70, 5.00, 5.17, 5.46, 5.61 at s = 12 .. 16, about 0.37 s and falling slowly (0.39 s to
     0.35 s). By time s a right seed of width s has delivered about a third of a bit per cell to column 1.
  RA3 REFUTED at s = 12 only (excess 4 against 9.4, where RA1's fit has three points). At s = 13 .. 16 the excess and
     log2 M(s, s) / b agree within 2.5 (3 vs 5.5, 5 vs 6.3, 6 vs 5.7, 9 vs 11.2). The race roughly balances: the
     time won beyond the seed is about the information delivered, divided by the net cost per step.
  RA4 HELD (the null): no recurrence of order 5 or less in any of the four sequences N(s, s + e), and their 2-adic
     valuations (0 to 8) show no pattern. No Chebyshev-type identity is visible in these counts.
  RA5 control PASSED, and exactly: next to a white wall, M(s, s) = s (column 1 turns black at one of times 0 .. s - 1
     and stays black). The blind half HELD: the excess is at most 1 while log2 M(s, s) / b reaches 4.0 at s = 16.
     There, about log2 s bits are delivered and destroyed within one step.
"""
import math, statistics, sys
from fractions import Fraction

FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def slope(xs, ys):
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def right_col1(rrow, T, W):
    out, r, p = [], rrow, len(W)
    for t in range(T + 1):
        out.append(r & 1)
        r = ((r << 1) | W[t % p]) ^ (r | (r >> 1))
    return tuple(out)


FORCED = {}


def survival(col1, s, W, tmax):
    """Force the left seed (depths 1 .. s) to keep every condition before s, then the first failing time (both)."""
    p = len(W)

    def target(t):
        return 1 - W[(t + 1) % p] if W[t % p] else W[(t + 1) % p] ^ col1[t]

    key = (tuple(W), s, col1[:s])                             # the forced seed depends on column 1 before s only
    lrow = FORCED.get(key)
    if lrow is None:
        lrow = 0
        for t in range(s):
            r, mask = lrow, (1 << (t + 2)) - 1
            for u in range(t):
                r = ((r >> 1) ^ (r | ((r << 1) | W[u % p]))) & mask
            if (r & 1) != target(t):
                lrow |= 1 << t
        FORCED[key] = lrow
    width = s + tmax + 4
    r, mask = lrow, (1 << width) - 1
    for t in range(tmax + 1):
        if (r & 1) != target(t):
            return t, lrow
        r = ((r >> 1) ^ (r | ((r << 1) | W[t % p]))) & mask
    return tmax + 1, lrow


def race(W, s, skip_zero=False):
    tmax = 4 * s + 20
    words = {}
    for rr in range(1 << s):
        c = right_col1(rr, tmax + 1, W)
        words.setdefault(c, []).append(rr)
    T_of = {}
    for c, seeds in words.items():
        T, lrow = survival(c, s, W, tmax)
        if skip_zero and lrow == 0 and 0 in seeds:
            seeds = [x for x in seeds if x != 0]                  # the all-white pair (w = 0)
            if not seeds:
                continue
        T_of[c] = (T, len(seeds))
    N, M = {}, {}
    top = max(T for T, _ in T_of.values())
    for T in range(0, top + 1):
        surv = [(c, m) for c, (Tc, m) in T_of.items() if Tc >= T]
        N[T] = sum(m for _, m in surv)
        M[T] = len({c[:T] for c, _ in surv})
    return N, M, top


def fit_recurrence(u, r):
    M = [[Fraction(u[n - 1 - i]) for i in range(r)] + [Fraction(u[n])] for n in range(r, 2 * r)]
    for col in range(r):
        piv = next((i for i in range(col, r) if M[i][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        for i in range(r):
            if i != col and M[i][col] != 0:
                f = M[i][col] / M[col][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[col])]
    return [M[i][r] / M[i][i] for i in range(r)]


def main():
    W = [0, 1]
    known = {2: 6, 3: 6, 4: 6, 5: 8, 6: 9, 7: 9, 8: 14, 9: 16, 10: 16, 11: 16, 12: 16, 13: 16, 14: 19, 15: 21, 16: 25}
    res, ok0 = {}, True
    for s in range(2, 17):
        N, M, top = race(W, s)
        res[s] = (N, M, top)
        ok0 &= N[s] == 1 << s and top == known[s]
        print(f"   01 s {s:2d}: T_BW {top:2d}; log2 N(s, T), T = s .. T_BW: "
              + " ".join(f"{math.log2(N[T]):.1f}" for T in range(s, top + 1))
              + "; log2 M: " + " ".join(f"{math.log2(M[T]):.1f}" for T in range(s, top + 1)), flush=True)
    report("RA0 N(s, s) = 2^s and the largest surviving T is T_BW(s) (rule30_words.py)", ok0)
    b, m0 = {}, {}
    for s in range(12, 17):
        N, M, top = res[s]
        Ts = list(range(s, top - 1))
        b[s] = -slope(Ts, [math.log2(M[T]) for T in Ts]) if len(Ts) >= 2 else float("nan")
        m0[s] = math.log2(M[s])
    verdict("RA1 the distinct words lose 0.4 to 1.5 bits per step beyond the seed",
            all(0.4 <= b[s] <= 1.5 for s in b), ", ".join(f"{s}: {b[s]:.2f}" for s in b))
    verdict("RA2 log2 M(s, s) between 0.2 s and 0.6 s", all(0.2 * s <= m0[s] <= 0.6 * s for s in m0),
            ", ".join(f"{s}: {m0[s]:.2f} ({m0[s] / s:.2f} s)" for s in m0))
    pred = {s: m0[s] / b[s] for s in b}
    verdict("RA3 the excess T_BW - s is within 3 of log2 M(s, s) / b",
            all(abs((res[s][2] - s) - pred[s]) <= 3 for s in b),
            ", ".join(f"{s}: {res[s][2] - s} vs {pred[s]:.1f}" for s in b))
    found = []
    for e in range(1, 5):
        u = [res[s][0].get(s + e, 0) for s in range(2, 17)]
        for r in range(1, 6):
            if 2 * r > len(u):
                break
            c = fit_recurrence(u, r)
            if c is not None and all(sum(c[i] * u[n - 1 - i] for i in range(r)) == u[n] for n in range(r, len(u))):
                found.append((e, r))
                break
        print(f"   N(s, s + {e}), s = 2 .. 16: " + " ".join(str(x) for x in u)
              + "; 2-adic valuations: " + " ".join(str((x & -x).bit_length() - 1) if x else "-" for x in u))
    verdict("RA4 no linear recurrence of order <= 5 for N(s, s + e), e = 1 .. 4", not found, f"found {found}")
    W0 = [0]
    exc, rat, mono = {}, {}, True
    for s in range(2, 17):
        N, M, top = race(W0, s, skip_zero=True)
        mono &= M[s] <= s + 2
        exc[s] = top - s
        Ts = list(range(s, top - 1))
        bb = -slope(Ts, [math.log2(M[T]) for T in Ts]) if len(Ts) >= 2 else 1.0
        rat[s] = math.log2(M[s]) / bb if bb > 0 else float("inf")
        print(f"   0  s {s:2d}: T_BW {top:2d}, M(s, s) {M[s]}, log2 M / b {rat[s]:.2f}", flush=True)
    report("RA5 control: next to a white wall M(s, s) <= s + 2", mono)
    verdict("RA5 the race over-predicts next to a white wall (excess <= 1, log2 M / b > 2 at s = 16)",
            max(exc.values()) <= 1 and rat[16] > 2, f"largest excess {max(exc.values())}, at 16: {rat[16]:.2f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
