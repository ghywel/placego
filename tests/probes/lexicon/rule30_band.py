#!/usr/bin/env python3
"""rule30_band.py: the window principle meets the band of stripes. A repeat of the trace is a white run in the later
row, and the later row's left end is never white for long: infinitely many of its diagonals are black for ever. So a
repeat must stay a growing distance below Theorem A' (Local, 2026-10-05; RULE30-PRIZE.md section 8.59; it builds
on sections 8.27, 8.30, 8.31 and 8.58).

RUN-ON:     cpu, one core (Python 3 with numpy)
COMMAND:    python3 tests/probes/lexicon/rule30_band.py [WMAX=9]          (everything)
            python3 tests/probes/lexicon/rule30_band.py 9 front        (the addendum's part alone)
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

OUTCOME of the first run, 2026-10-05 (45 seconds): ALL CHECKS PASS, and every blind prediction held.
  BD0, BD1, BD2 PASSED (41 seeds; every strip of 450 diagonals returns to itself with period 16).
  BD3 HELD: diagonal 4 is black from time 4 and diagonal 9 from time 11, for every content of the first 10 diagonals.
  BD4 PASSED (7,763 repeats with a white run to show, 0 violations; the bounds with b = 1, 4, 9: 0 violations).
  CF PASSED (the run is white again one row later in 0 of 3,025 cases).
  BD5 HELD: the bound with b = 9 is sharp (166 pairs attain n = L + a' - 9).
  BD6 HELD (3,755,410 pairs, 0 violations; the least L + a' - n among them is 51, well above 30).
  BD7 PASSED. BD8 HELD: least slack 1 (period-doubling), 0 (Chacon), -1595 (Fibonacci); 32, 32 and 33 for
  Thue-Morse, Rudin-Shapiro and paperfolding. BD9 HELD: longest zero runs 11 to 13, ones 0.497 to 0.510.

ADDENDUM, written 2026-10-05 after the first run and before the second. Two more statements (section 8.59):
  Lemma B3. If at time t the diagonals 0 to M have been periodic, with a common period P, for at least P steps, then
      no white run of the row inside diagonals 0 to M is longer than 2P.
  Theorem A''''. With the notation of Theorem A''': if the diagonals 0 to M are settled in that sense at time a',
      and M < a' - a, then n <= L + a' - M + 2P. So a repeat's white run cannot lie in the settled band.
  A settled diagonal k settles the next one at the first black cell it shows afterwards (a reset). So the times
  tau(k+1) = 1 + the first t >= max(tau(k), tau(k-1)) with diagonal k black (tau(k+1) = max(tau(k), tau(k-1)) after
  an eventually white diagonal) bound the settling of every row with a white left tail, in the worst of the 16
  phases. S(t) is the number of diagonals with tau + 16 <= t.
SEEN BEFORE the addendum's predictions: the first run above. Nothing of the strip beyond diagonal 450, no front.
  BF0 (control, must hold): the strip of 53,200 diagonals from the single cell returns to itself with period 16
      (run 200,000 steps first); its eventually white diagonals are 2, 7, 28 and 399; three random seeds reach
      the same cycle.
  BF1 (Lemma B3, must hold): no white run in any of the cycle's 16 rows is longer than 32. Blind: the longest is
      between 5 and 16.
  BF2 (blind): the worst-phase front's slope tau(k) / k at k = 53,199 is between 1.5 and 2.0.
  BF3 (must hold): for 30 random seeds of up to 40 cells and t = 200, 400, 800 and 1600, the row agrees with one
      phase of the cycle on every diagonal below S(t).
  CF2 (counterfactual, must fail): the same on every diagonal below 2 S(t). It must fail in every case.
  BF4 (what Theorem A'''' reaches; the control must hold, the rest is blind). For a word c as column 1, a pair
      i < i' with common length l excludes every left edge L with L + 2i' - 2l + 32 <= min(2(i' - i) - 1, 53,199)
      and tau(L + 2i' - 2l + 32) <= 2i' - 16. L* is the largest L excluded, over pairs with i' - i = m 2^j, m odd
      below 16. Control: L* >= 50,000 for the period-doubling word (Corollary F excludes every L). Blind:
      L* >= 8,000 for Thue-Morse, and L* >= 1,000 for Rudin-Shapiro and for paperfolding.
REFUTED-BY: BF0, BF1's bound, BF3, CF2 or BF4's control failing (a proof or the instrument); the blind parts the
  other way.

OUTCOME of the second run, 2026-10-05 (11 seconds; a third run after fixing a print that crashed on an empty
  result, same numbers):
  BF0 PASSED: one cycle of period 16 to 53,200 diagonals, white diagonals 2, 7, 28, 399, reached by the single cell
  and three random seeds.
  BF1 PASSED its bound (longest white run 17 <= 32); its blind half REFUTED by one (17, not 5 to 16).
  BF2 REFUTED: the worst-phase front's slope is 2.0168 at diagonal 53,199 (1.992 at 1,000; 2.018 at 10,000).
  BF3 PASSED (S(200) = 97, S(1600) = 804).
  CF2 FAILED by design: 2 of 120 rows (seeds of width 21 and 6, at t = 200) agree with the cycle below 2 S(t).
  Post hoc: the actual settled width over t at t = 200 ranges from 0.76 to 1.01 over the 30 seeds, median 0.82;
  at t = 1600 from 0.76 to 0.81, median 0.78. The counterfactual assumed the average rate for every row.
  BF4: control PASSED (period-doubling to 53,165). Thue-Morse L* = 15,870 HELD (pair i = 0, i' = 49,152,
  common length 32,768). Rudin-Shapiro: no pair excludes any L; paperfolding L* = 15,868 (i = 16,384,
  i' = 49,152, common length 32,767): the joint prediction REFUTED by Rudin-Shapiro.
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


def cycle_of(v, K, steps):
    mask = (1 << K) - 1
    for _ in range(steps):
        v = strip_step(v, mask)
    orbit, u = [v], strip_step(v, mask)
    while u != v and len(orbit) < 1024:
        orbit.append(u); u = strip_step(u, mask)
    return orbit if u == v else None


def part_front(K=53200, P=16):
    rng = random.Random(59)
    cyc = cycle_of(1, K, 200000)
    ok = cyc is not None and len(cyc) == P
    U = np.array([np.unpackbits(np.frombuffer(v.to_bytes((K + 7) // 8, "little"), dtype=np.uint8),
                                bitorder="little")[:K] for v in cyc], dtype=np.uint8) if ok else None
    white = [int(k) for k in np.nonzero(~U.any(axis=0))[0]] if ok else []
    same = ok
    for _ in range(3):
        other = cycle_of((rng.getrandbits(rng.randint(2, 64)) << 1) | 1, K, 200000)
        same &= other is not None and set(other) == set(cyc)
    report("BF0 the strip of 53,200 diagonals has one cycle of period 16; white diagonals 2, 7, 28, 399",
           ok and white == [2, 7, 28, 399] and same, f"period {len(cyc) if cyc else None}, white {white}")
    if not ok:
        return
    longest = 0
    for row in U:
        z = np.concatenate(([1], row, [1]))
        edges = np.nonzero(z)[0]
        longest = max(longest, int((np.diff(edges) - 1).max()))
    report("BF1 no white run in the cycle is longer than 2P = 32", longest <= 2 * P, f"longest {longest}")
    verdict("BF1 the longest white run in the cycle is between 5 and 16", 5 <= longest <= 16, f"{longest}")

    iswhite = ~U.any(axis=0)
    worst = np.zeros(K, dtype=np.int64)
    for phi in range(P):
        tau = np.zeros(K, dtype=np.int64)
        prev = 0                                        # tau(k - 1)
        for k in range(K - 1):
            start = max(int(tau[k]), prev)
            if iswhite[k]:
                nxt = start
            else:
                t = start
                while not U[(t + phi) % P, k]:
                    t += 1
                nxt = t + 1
            prev = int(tau[k])
            tau[k + 1] = nxt
        worst = np.maximum(worst, tau)
    worst = np.maximum.accumulate(worst)
    slope = worst[K - 1] / (K - 1)
    verdict("BF2 the worst-phase front's slope at diagonal 53,199 is between 1.5 and 2.0", 1.5 <= slope <= 2.0,
            f"tau = {int(worst[K - 1])}, slope {slope:.4f}; at 1,000: {worst[1000] / 1000:.3f}, "
            f"at 10,000: {worst[10000] / 10000:.3f}")

    def settled(t):
        return int(np.searchsorted(worst, t - P, side="right"))

    ok3, cf_fail, cases, agree = True, 0, 0, []
    KK = 3400
    mask = (1 << KK) - 1
    for _ in range(30):
        v = (rng.getrandbits(rng.randint(1, 39)) << 1) | 1
        width = v.bit_length()
        t = 0
        for T in (200, 400, 800, 1600):
            while t < T:
                v = strip_step(v, mask); t += 1
            S = settled(T)
            m1, m2 = (1 << S) - 1, (1 << min(2 * S, KK)) - 1
            ok3 &= any((v ^ u) & m1 == 0 for u in cyc)
            cases += 1
            if any((v ^ u) & m2 == 0 for u in cyc):
                agree.append((width, T))              # post hoc: which rows are settled that far
            else:
                cf_fail += 1
    report("BF3 every row agrees with a phase of the cycle on the diagonals below S(t)", ok3,
           f"S(200), S(1600) = {settled(200)}, {settled(1600)}")
    report("CF2 no row agrees with a phase of the cycle on the diagonals below 2 S(t)", cf_fail == cases,
           f"{cf_fail} of {cases} disagree; agreeing (seed width, time): {agree}")

    N = 1 << 18
    W = words(N)
    ds = sorted({m << j for m in range(1, 16, 2) for j in range(4, 17) if (m << j) <= 100000})
    lstar = {}
    for name in ("period-doubling", "Thue-Morse", "Rudin-Shapiro", "paperfolding"):
        c = W[name]
        best, arg = -1, None
        for d in ds:
            l = lcp_shift(c, d, N - d).astype(np.int64)
            i2 = np.arange(len(l), dtype=np.int64) + d
            real = i2 + l < N - 1                              # the common length is not cut by the data's end
            w0 = 2 * i2 - 2 * l
            mt = np.searchsorted(worst, 2 * i2 - P, side="right") - 1
            lmax = np.minimum(np.minimum(2 * d - 1, K - 1), mt) - w0 - 2 * P
            lmax = np.where(real, lmax, -1)
            j = int(np.argmax(lmax))
            if int(lmax[j]) > best:
                best, arg = int(lmax[j]), (j, j + d, int(l[j]))
        lstar[name] = best
        where = f"(pair i = {arg[0]}, i' = {arg[1]}, common length {arg[2]})" if arg else "(no pair excludes any L)"
        print(f"   L* for {name}: {best}  {where}", flush=True)
    report("BF4 control: Theorem A'''' excludes every left edge to 50,000 for the period-doubling word",
           lstar["period-doubling"] >= 50000)
    verdict("BF4 L* >= 8,000 for Thue-Morse", lstar["Thue-Morse"] >= 8000, f"{lstar['Thue-Morse']}")
    verdict("BF4 L* >= 1,000 for Rudin-Shapiro and paperfolding",
            min(lstar["Rudin-Shapiro"], lstar["paperfolding"]) >= 1000,
            f"{lstar['Rudin-Shapiro']}, {lstar['paperfolding']}")


def main():
    if len(sys.argv) > 2 and sys.argv[2] == "front":
        part_front()
        print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")
        return
    t9 = part_strip()
    part_window(t9)
    part_words()
    part_front()
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
