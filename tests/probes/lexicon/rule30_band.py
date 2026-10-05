#!/usr/bin/env python3
"""rule30_band.py: the window principle meets the band of stripes. A repeat of the trace is a white run in the later
row, and the later row's left end is never white for long: infinitely many of its diagonals are black for ever. So a
repeat must stay a growing distance below Theorem A' (Local, 2026-10-05; RULE30-PRIZE.md section 8.59; it builds
on sections 8.27, 8.30, 8.31 and 8.58).

RUN-ON:     cpu, one core (Python 3 with numpy)
COMMAND:    python3 tests/probes/lexicon/rule30_band.py [WMAX=9]
COST:       a few minutes.

THE STATEMENTS (proved in section 8.59). Diagonal k of a row is the cell k places right of the row's leftmost black
cell; D_k(t) is its colour at time t. D_k(t+1) = D_(k-2)(t) xor (D_(k-1)(t) or D_k(t)), so each diagonal depends only
on diagonals nearer the edge, and is eventually periodic in time (sections 8.27, 8.30).
  Lemma B1. If diagonal j is eventually white, diagonal j + 2 is eventually black. No two adjacent diagonals are
      both eventually white. A diagonal other than 0 and 1 is eventually black only two after an eventually white one.
  Lemma B2. The eventual periods of the diagonals are unbounded. (If they were bounded, two pairs of adjacent
      diagonals would repeat, and Rule 30 read from right to left would carry the repeat back to the edge.) So
      there are infinitely many eventually white diagonals, and infinitely many eventually black ones.
  Theorem A'''. Let the leftmost black cell at time 0 be L cells left of column i, and let the pair of columns
      (i, i+1) show the same block of n values from times a and a' > a. Then row a' is white on its diagonals
      L + a' - n + 1 to a' - a - 1. So if diagonal b is black at time a' and b < a' - a, then n <= L + a' - b.
  Corollary F. Write the visible bits c of column 1 next to the wall 0101... If c has repetitions of unbounded
      period d that start at index i and run for at least i + 2d - K symbols, for one fixed K, then the forced left
      half is never finite. (Sequences that begin with longer and longer squares, or miss one by a bounded amount.)

SEEN BEFORE these predictions were written: no run of this script. Section 8.30's measured list of eventually white
diagonals (2, 7, 28, 399). Diagonals 0 to 9 worked by hand. The first run of rule30_window.py (the longest late
recurring blocks are 15 to 19 cells).

PREDICTIONS, written 2026-10-05 before this script's first run.
  BD0 (control, must hold): the strip system V' = ((V << 2) xor ((V << 1) or V)) mod 2^K gives the rows of a direct
      simulation, for 20 random seeds, K = 64, 200 steps.
  BD1 (must hold; section 8.30 re-measured with a certificate V(t) = V(t + P)): for the single cell and 40 random
      seeds of up to 64 cells, the eventually white diagonals below 450 are exactly 2, 7, 28 and 399.
  BD2 (Lemma B1, must hold): for the same seeds, the eventually black diagonals below 450 are exactly 0, 1, 4, 9, 30
      and 401, and no two adjacent diagonals are both eventually white.
  BD3 (exhaustive; blind in its number): over every one of the 512 contents of the first 10 diagonals, diagonal 4
      is black from time 4 on, and diagonal 9 is black from a time T9 on with T9 <= 16.
  BD4 (Theorem A''', must hold): for every seed of width 1 to WMAX, every column pair from the seed's left end to
      8 cells past its right end, and every pair of times a < a' <= 120 whose common block is complete within 160
      steps: row a' is white on diagonals L + a' - n + 1 to a' - a - 1. And n <= L + a' - b for b = 1, 4 and 9
      whenever a' - a > b and a' >= T_b (T_1 = 1, T_4 = 4, T_9 from BD3).
  BD5 (blind; tightness): the bound with b = 9 is attained: some pair with a' - a >= 10 and a' >= T9 has
      n = L + a' - 9.
  BD6 (blind): for every pair with a' - a >= 31 and a' >= 60, n <= L + a' - 30 (diagonal 30 has settled by then
      for these seeds).
  CF  (counterfactual, must fail): the cells of BD4's white run are white one row later as well. This must be false
      for every pair whose run has two cells or more (a white run loses a cell at each end each step).
  BD7 (the hypothesis of Corollary F, must hold): for the period-doubling word, the first 2^k symbols recur at
      2^k for 2^k - 1 symbols exactly (k = 1 .. 12). For Chacon's word (fixed by 0 -> 0010, 1 -> 1) the first h
      symbols recur at h for at least h symbols, h = 4, 13, 40, ..., 3280. Control of the dictionary: for the
      period-doubling word as column 1, the forced rows at times 0 and 2^(k+1) agree to depth 2^(k+1) - 3 at
      least (k = 3 .. 8).
  BD8 (blind; which words the corollary reaches): with slack(i, i') = i' minus the common length of the futures at
      i and i', the least slack over pairs with i' - i >= 64 and i' <= 4096 is 1 for period-doubling, 0 or less for
      Chacon and for Fibonacci, and at least 16 for Thue-Morse, Rudin-Shapiro and paperfolding (the corollary
      does not reach those three).
  BD9 (blind): with the period-doubling word, Chacon's word and their complements as column 1, the forced row at
      time 0 to depth 6000 has no zero run longer than 30 and ones at a share between 0.45 and 0.55.
REFUTED-BY: BD0, BD1, BD2, BD4, BD7 or CF failing (a proof or the instrument); BD3, BD5, BD6, BD8, BD9 the other
  way.

OUTCOME: (to be recorded after the first run)
"""
import random, sys
import numpy as np

WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 9
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def step(x):
    left = np.zeros_like(x); left[1:] = x[:-1]
    right = np.zeros_like(x); right[:-1] = x[1:]
    return left ^ (x | right)


def strip_step(v, mask):
    return ((v << 2) ^ ((v << 1) | v)) & mask


def part_strip():
    rng = random.Random(30)
    # BD0: the strip against a direct simulation
    K, T, ok = 64, 200, True
    mask = (1 << K) - 1
    for _ in range(20):
        w = rng.randint(1, 40)
        bits = [1] + [rng.randint(0, 1) for _ in range(w - 1)]
        x = np.zeros(w + 2 * T + 8, dtype=np.uint8)
        off = T + 4
        x[off:off + w] = bits
        v = sum(b << k for k, b in enumerate(bits))
        for t in range(T + 1):
            row = [int(x[off - t + k]) for k in range(K)]
            ok &= row == [(v >> k) & 1 for k in range(K)]
            x = step(x); v = strip_step(v, mask)
    report("BD0 the strip system gives the rows of a direct simulation", ok)

    # BD1, BD2: the eventually white and eventually black diagonals below 450, with a certificate
    K = 450
    mask = (1 << K) - 1
    seeds = [1] + [(rng.getrandbits(rng.randint(2, 64)) << 1) | 1 for _ in range(40)]
    white_ok = black_ok = adj_ok = cert_ok = True
    periods = set()
    for v in seeds:
        for _ in range(4000):
            v = strip_step(v, mask)
        orbit, u = [v], strip_step(v, mask)
        while u != v and len(orbit) < 1024:
            orbit.append(u); u = strip_step(u, mask)
        cert_ok &= u == v
        periods.add(len(orbit))
        any1 = all1 = orbit[0]
        for u in orbit[1:]:
            any1 |= u; all1 &= u
        white = [k for k in range(K) if not (any1 >> k) & 1]
        black = [k for k in range(K) if (all1 >> k) & 1]
        white_ok &= white == [2, 7, 28, 399]
        black_ok &= black == [0, 1, 4, 9, 30, 401]
        adj_ok &= all(b - a > 1 for a, b in zip(white, white[1:]))
    report("certificate: every strip of 450 diagonals returns to itself", cert_ok, f"periods {sorted(periods)}")
    report("BD1 the eventually white diagonals below 450 are 2, 7, 28, 399", white_ok, f"{len(seeds)} seeds")
    report("BD2 the eventually black diagonals below 450 are 0, 1, 4, 9, 30, 401; no two white ones adjacent",
           black_ok and adj_ok)

    # BD3: exhaustive over the first 10 diagonals
    K = 10
    mask = (1 << K) - 1
    last4 = last9 = -1
    for s in range(1 << (K - 1)):
        v = (s << 1) | 1
        for t in range(400):
            if not (v >> 4) & 1:
                last4 = max(last4, t)
            if not (v >> 9) & 1:
                last9 = max(last9, t)
            v = strip_step(v, mask)
    t4, t9 = last4 + 1, last9 + 1
    report("BD3a diagonal 4 is black from time 4 on, for every content of the first 10 diagonals", t4 <= 4,
           f"black from time {t4}")
    verdict("BD3 diagonal 9 is black from a time T9 <= 16, for every content", t9 <= 16, f"T9 = {t9}")
    return t9


def part_window(t9, T=160, amax=120):
    tb = {1: 1, 4: 4, 9: t9}
    runs = run_viol = bound_viol = cf_total = cf_white = attained = 0
    b30_pairs = b30_viol = 0
    least_gap_late = None
    for w in range(1, WMAX + 1):
        inner = max(w - 2, 0)
        for s in range(1 << inner):
            bits = [1] + [(s >> i) & 1 for i in range(inner)] + ([1] if w > 1 else [])
            width = w + 2 * T + 8
            x = np.zeros(width, dtype=np.uint8)
            off = T + 4
            x[off:off + w] = bits
            hist = np.zeros((T + 1, width), dtype=np.uint8)
            hist[0] = x
            for t in range(T):
                x = step(x); hist[t + 1] = x
            for L in range(0, w + 8):
                i = off + L
                pair = hist[:, i].astype(np.int16) * 2 + hist[:, i + 1]
                for d in range(1, amax + 1):
                    eq = pair[:T + 1 - d] == pair[d:]
                    m = len(eq)
                    a = np.arange(m)
                    nextfalse = np.minimum.accumulate(np.where(eq, m, a)[::-1])[::-1]
                    run = nextfalse - a
                    complete = (nextfalse < m) & (a + d <= amax) & (run > 0)
                    if not complete.any():
                        continue
                    n = run[complete]
                    a1 = a[complete]
                    a2 = a1 + d
                    for b, tmin in tb.items():
                        if d > b:
                            sel = a2 >= tmin
                            bound_viol += int((n[sel] > L + a2[sel] - b).sum())
                    if d >= 10:
                        attained += int(((a2 >= t9) & (n == L + a2 - 9)).sum())
                    if d >= 31:
                        sel = a2 >= 60
                        if sel.any():
                            b30_pairs += int(sel.sum())
                            b30_viol += int((n[sel] > L + a2[sel] - 30).sum())
                            g = int((L + a2[sel] - n[sel]).min())
                            least_gap_late = g if least_gap_late is None else min(least_gap_late, g)
                    hit = n - 1 > L + a1                       # the later row has a white run to show
                    for nn, aa, bb in zip(n[hit], a1[hit], a2[hit]):
                        lo, hi = i - int(nn) + 1, i - L - int(aa)      # cells at distances L + a + 1 .. n - 1
                        runs += 1
                        run_viol += bool(hist[bb, lo:hi].any())
                        if hi - lo >= 2:
                            cf_total += 1
                            cf_white += not hist[bb + 1, lo:hi].any()
    report("BD4 the later row is white on diagonals L + a' - n + 1 to a' - a - 1", run_viol == 0,
           f"{runs} repeats with a run to show, {run_viol} violations")
    report("BD4 n <= L + a' - b for b = 1, 4, 9 once a' - a > b and a' >= T_b", bound_viol == 0,
           f"{bound_viol} violations")
    report("CF  the run is not white one row later (runs of two cells or more)", cf_total > 0 and cf_white == 0,
           f"white again in {cf_white} of {cf_total}")
    verdict("BD5 the bound with b = 9 is attained by a pair with a' - a >= 10", attained > 0,
            f"{attained} attaining pairs")
    verdict("BD6 n <= L + a' - 30 for pairs with a' - a >= 31 and a' >= 60", b30_viol == 0,
            f"{b30_pairs} pairs, {b30_viol} violations, least L + a' - n = {least_gap_late}")


def fixed_point(rules, n, start="0"):
    w = start
    while len(w) < n:
        w = "".join(rules[ch] for ch in w)
    return [int(ch) for ch in w[:n]]


def words(n):
    pd = [((i + 1) & -(i + 1)).bit_length() - 1 & 1 for i in range(n)]
    tm = [bin(i).count("1") & 1 for i in range(n)]
    rs = [bin(i & (i >> 1)).count("1") & 1 for i in range(n)]
    pf = [0 if ((i + 1) // ((i + 1) & -(i + 1))) % 4 == 1 else 1 for i in range(n)]
    return {"period-doubling": pd, "Chacon": fixed_point({"0": "0010", "1": "1"}, n),
            "Fibonacci": fixed_point({"0": "01", "1": "0"}, n), "Thue-Morse": tm, "Rudin-Shapiro": rs,
            "paperfolding": pf}


def lcp_shift(c, d, limit):
    """common length of the futures of c at i and i + d, for every i < limit (capped at the data's end)"""
    c = np.asarray(c, dtype=np.int8)
    m = len(c) - d
    eq = c[:m] == c[d:]
    a = np.arange(m)
    nextfalse = np.minimum.accumulate(np.where(eq, m, a)[::-1])[::-1]
    return (nextfalse - a)[:limit]


def forced_row(c, depth):
    """row 0 of the left half forced by column 0 = 0101... and column 1's visible bits c, to the given depth"""
    T = depth + 2
    t = np.arange(T)
    col0 = (t & 1).astype(np.uint8)
    cc = np.asarray(c[:T // 2 + 1], dtype=np.uint8)
    colm1 = np.where(t & 1, 1, 1 - cc[t // 2]).astype(np.uint8)
    row = [int(colm1[0])]
    right, cur = col0, colm1
    for _ in range(depth - 1):
        nxt = cur[1:] ^ (cur[:-1] | right[:len(cur) - 1])
        right, cur = cur[:-1], nxt
        row.append(int(cur[0]))
    return row                                    # row[d - 1] is the cell at depth d


def forced_rows(c, times, depth):
    """rows of the forced left half at the given even times, to the given depth (by shifting c)"""
    return {t: forced_row(c[t // 2:], depth) for t in times}


def part_words():
    W = words(1 << 15)
    pd, ch = W["period-doubling"], W["Chacon"]
    ok = all(int(lcp_shift(pd, 1 << k, 1)[0]) == (1 << k) - 1 for k in range(1, 13))
    hs = [(3 ** (k + 1) - 1) // 2 for k in range(1, 8)]
    ok2 = all(int(lcp_shift(ch, h, 1)[0]) >= h for h in hs)
    ok3 = True
    for k in range(3, 9):
        depth = (1 << (k + 1)) - 3
        rows = forced_rows(pd, [0, 1 << (k + 1)], depth)
        ok3 &= rows[0] == rows[1 << (k + 1)]
    report("BD7 period-doubling: the first 2^k symbols recur at 2^k for exactly 2^k - 1 symbols", ok)
    report("BD7 Chacon: the first h symbols recur at h for at least h symbols", ok2, f"h = {hs}")
    report("BD7 the forced rows at times 0 and 2^(k+1) agree to depth 2^(k+1) - 3 (period-doubling)", ok3)

    least = {}
    for name, c in W.items():
        best = None
        for d in range(64, 4096):
            lim = 4096 - d + 1                               # i' = i + d <= 4096
            l = lcp_shift(c[:12288], d, lim)
            slack = np.arange(len(l)) + d - l
            v = int(slack.min())
            best = v if best is None else min(best, v)
        least[name] = best
        print(f"   least slack over pairs with i' - i >= 64, i' <= 4096: {name}: {best}", flush=True)
    verdict("BD8 least slack: 1 period-doubling; <= 0 Chacon, Fibonacci; >= 16 Thue-Morse, Rudin-Shapiro, "
            "paperfolding",
            least["period-doubling"] == 1 and least["Chacon"] <= 0 and least["Fibonacci"] <= 0
            and min(least["Thue-Morse"], least["Rudin-Shapiro"], least["paperfolding"]) >= 16)

    ok9, notes = True, []
    for name in ("period-doubling", "Chacon"):
        for comp in (0, 1):
            c = [b ^ comp for b in W[name]]
            row = forced_row(c, 6000)
            longest = cur = 0
            for b in row:
                cur = 0 if b else cur + 1
                longest = max(longest, cur)
            share = sum(row) / len(row)
            ok9 &= longest <= 30 and 0.45 <= share <= 0.55
            notes.append(f"{name}{' (complement)' if comp else ''}: longest zero run {longest}, ones {share:.3f}")
    for nline in notes:
        print("   " + nline, flush=True)
    verdict("BD9 the forced row to depth 6000 looks like coin flips for the words the corollary excludes", ok9)


def main():
    t9 = part_strip()
    part_window(t9)
    part_words()
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
