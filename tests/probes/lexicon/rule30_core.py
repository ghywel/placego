#!/usr/bin/env python3
"""rule30_core.py: where Problems 1 and 2 meet. How much entropy, and what density, the left side naturally has.

RUN-ON:     cpu (pure Python 3, standard library; exact simulation, seeded)
COMMAND:    python3 tests/probes/lexicon/rule30_core.py | rule30_core.py balance
COST:       about two minutes on one core.

Background. The entropy squeeze (rule30_squeeze.py, RULE30-PRIZE.md section 8.33) says that in a period-2
counterexample every column left of column 0 carries at most about 0.064 bits per step. Problem 2 asks whether the
centre column's black and white each average 1/2, which follows if its block statistics are those of a fair coin
(entropy 1). So both questions are about how random Rule 30's columns are: period 2 needs a weak lower bound (above
0.064, for a left side driven by 0101...), Problem 2 a strong one (exactly coin-like, for the free single seed).
This probe measures the left side's natural statistics in both settings, and the one region whose statistics are
known exactly, the universal left band (rule30_leftsides.py, section 8.31).

Measured:
  A. The band's exact density: the universal left side's certified cycle (strip of K = 40,000 diagonals), averaged
     over the cycle and the diagonals.
  B. The single seed's rows at depths near 2^16, split into the band (distance e from the left edge below 0.7 t),
     the core (e at least 0.8 t, and at least 3 log2 t + 10 cells from the right edge) and the rest.
  C. The centre column over 2^17 steps: density, and block entropy h_10 (the entropy of 10-blocks less that of
     9-blocks), against coin flips of the same length (the estimator's bias is the same for both).
  D. The left half-line driven by column 0 = 0101... (section 8.22: given column 0, it evolves alone) from 20 random
     finite left seeds of 1 to 64 cells, over 2^16 steps: block entropy h_10 of columns -1, -2, -4, ..., -64, the
     spatial entropy of the patterns just left of column 0, and how often the period-2 condition x_t(-1) = 1 holds at
     odd times.

PREDICTIONS, written 2026-10-05 before this script's first run (no exploratory run):
  CR0 (controls): the band's strip is certified periodic; the estimator gives h_10 for a periodic sequence of period
      7 at most 0.01, for a Markov chain with stay probability 0.9 within 0.03 of its rate 0.469, and for coin flips
      the reference value used below.
  CR1 (blind; the band): the universal band's density differs from 1/2 by more than 0.002, and lies above 1/2.
  CR2 (blind; Problem 2): the single seed's core density at depths near 2^16 is within 0.002 of 1/2; the centre
      column's density over 2^17 steps is within 0.004 of 1/2 (three standard deviations of a fair coin); its h_10 is
      within 0.01 of the coin flips'.
  CR3 (blind; the squeeze's gap): in the driven left half-line, every measured column has h_10 within 0.05 of the
      coin flips' (near 1 bit per step, where a counterexample needs at most 0.064), and so do the patterns just left
      of column 0, read as words of 10 cells (H_10 - H_9 per cell).
  CR4 (blind): in the driven left half-line the period-2 condition x_t(-1) = 1 holds at 0.50 +- 0.01 of odd times:
      a fair coin each time, with nothing pushing towards it.
REFUTED-BY: CR0 failing (the instrument); CR1 to CR4 failing.

OUTCOME of the first run, 2026-10-05 (24 seconds): CR0 PASSED (the band's strip certified with a cycle of 16;
period 7 0.0000; Markov 0.4665 against 0.469; coin flips 0.9971 over 2^17 steps, 0.9886 over 2^15).
  CR1 REFUTED: the universal band's density over diagonals 0 to 39,999 is 319,993 / 640,000 = 0.499989, balanced to
      about 10^-5 (0.50113 over diagonals 0 to 999, 0.49991 over 1,000 to 9,999, 0.49998 over 10,000 to 39,999). The
      band is completely ordered and still balanced.
  CR2 HELD: at depths 65,472 to 65,535 the band is 0.49979, the region between 0.50016, the core 0.50027; the centre
      column over 2^17 steps has density 0.49947 and h_10 0.9972 (coin flips 0.9971).
  CR3 HELD: in the left half-line driven by 0101 from 20 random seeds, the lowest column h_10 is 0.9868 (coin flips
      0.9886 at that length) and the lowest spatial entropy of 10-cell patterns next to column 0 is 0.9877 per cell
      (coin flips 0.9875). A counterexample needs at most 0.064: the natural left side is about 15 times richer.
  CR4 HELD: the period-2 condition x_t(-1) = 1 holds at 0.4998 of odd times.

ADDENDUM, written 2026-10-05 after the first run and before the second (python3 rule30_core.py balance): is the band's
balance structural? Each settled left diagonal repeats a block of 1 to 32 cells.
  CR5 (blind, uncertain): at least 75% of the diagonals 0 to 39,999 have a repeating block with exactly half its
      cells black, and the unbalanced rest (the eventually white and eventually black diagonals among them) cancel
      to within 0.001 in density.
OUTCOME of the second run, 2026-10-05 (python3 rule30_core.py balance, seconds): CR5 REFUTED, but the other way from
a failure of balance. Of the 40,000 band diagonals only 7,901 (19.75%) repeat an exactly balanced block; 6 are
eventually black, 4 eventually white, and 32,089 are unbalanced. Yet the 32,099 unbalanced diagonals together have
density 0.49999. The ordered band's balance is collective, a cancellation between diagonals, not a property of each.
"""
import math, random, sys
from collections import Counter

FAILS = 0
K = 40000
TS = 1 << 16
TC = 1 << 17


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def block_H(seq, k):
    if len(seq) < k:
        return 0.0
    c, v, m = Counter(), 0, (1 << k) - 1
    for i, b in enumerate(seq):
        v = ((v << 1) | b) & m
        if i >= k - 1:
            c[v] += 1
    n = sum(c.values())
    return -sum(x / n * math.log2(x / n) for x in c.values())


def h(seq, k=10):
    return block_H(seq, k) - block_H(seq, k - 1)


def H_words(words, k):
    c = Counter(words)
    n = sum(c.values())
    return -sum(x / n * math.log2(x / n) for x in c.values())


def band_cycle():
    mask = (1 << K) - 1
    V, tail = 1, []
    T = 1 << 16
    for t in range(T):
        if t >= T - 1024:
            tail.append(V)
        V = ((V << 2) ^ ((V << 1) | V)) & mask
    P = 1
    while P < 1024 and tail[-1] != tail[-1 - P]:
        P *= 2
    return tail[-P:] if P < 1024 else None


def main():
    rng = random.Random(1935)
    # CR0: estimator controls
    per7 = [int(c) for c in "0010111" * 20000][:TC]
    mk, s = [], 0
    for _ in range(TC):
        s = s if rng.random() < 0.9 else 1 - s
        mk.append(s)
    coin = [rng.getrandbits(1) for _ in range(TC)]
    h_per, h_mk, h_coin = h(per7), h(mk), h(coin)
    coin_D = [rng.getrandbits(1) for _ in range(TS // 2)]
    h_coin_D = h(coin_D)
    cyc = band_cycle()
    ok0 = cyc is not None and h_per <= 0.01 and abs(h_mk - 0.469) <= 0.03
    report("CR0 controls: the band's strip certified; h_10 of a period-7 sequence, a Markov chain, coin flips", ok0,
           f"cycle {len(cyc) if cyc else None}; period 7 {h_per:.4f}; Markov {h_mk:.4f} (0.469); coin flips "
           f"{h_coin:.4f} over {TC} steps, {h_coin_D:.4f} over {TS // 2}")
    # A: the band's exact density
    ones = sum(bin(v).count("1") for v in cyc)
    dens = ones / (len(cyc) * K)
    parts = []
    for lo, hi in ((0, 1000), (1000, 10000), (10000, 40000)):
        m = ((1 << (hi - lo)) - 1) << lo
        parts.append(sum(bin(v & m).count("1") for v in cyc) / (len(cyc) * (hi - lo)))
    print(f"   the universal band's density over diagonals 0 to {K - 1}: {dens:.6f} (exactly {ones} / "
          f"{len(cyc) * K}); by range 0-999 {parts[0]:.5f}, 1000-9999 {parts[1]:.5f}, 10000-39999 {parts[2]:.5f}",
          flush=True)
    verdict("CR1 the band's density differs from 1/2 by more than 0.002 and lies above it",
            dens - 0.5 > 0.002, f"{dens:.6f}")
    # B and C: the single seed
    T = TC
    row = 1 << T                                       # bit x + T holds cell x
    mask = (1 << (2 * T + 3)) - 1
    centre = []
    acc = {"band": [0, 0], "core": [0, 0], "rest": [0, 0]}
    for t in range(T):
        centre.append((row >> T) & 1)
        if TS - 64 <= t < TS:
            cut_band = T + int(-0.3 * t)               # e = x + t < 0.7 t  <=>  x < -0.3 t
            cut_core = T + int(-0.2 * t)               # e >= 0.8 t
            right = T + t - int(3 * math.log2(t)) - 10
            seg = lambda a, b: (row >> a) & ((1 << (b - a)) - 1)
            for name, a, b in (("band", T - t, cut_band), ("core", cut_core, right),
                               ("rest", cut_band, cut_core)):
                acc[name][0] += bin(seg(a, b)).count("1")
                acc[name][1] += b - a
        row = ((row << 1) ^ (row | (row >> 1))) & mask
    rd = {k: v[0] / v[1] for k, v in acc.items()}
    cd = sum(centre) / len(centre)
    hc = h(centre)
    print(f"   single seed, depths {TS - 64} to {TS - 1}: band {rd['band']:.5f}, between {rd['rest']:.5f}, core "
          f"{rd['core']:.5f}; centre column over {T} steps: density {cd:.5f}, h_10 {hc:.4f} (coin flips {h_coin:.4f})",
          flush=True)
    verdict("CR2 Problem 2's evidence: core density within 0.002 of 1/2, centre density within 0.004, centre h_10 "
            "within 0.01 of coin flips", abs(rd["core"] - 0.5) <= 0.002 and abs(cd - 0.5) <= 0.004 and
            abs(hc - h_coin) <= 0.01, f"core {rd['core']:.5f}, centre {cd:.5f}, h_10 {hc:.4f}")
    # D: the driven left half-line
    cols = [1, 2, 4, 8, 16, 32, 64]
    worst, spatial, odd_ok, odd_n = 1.0, [], 0, 0
    for _ in range(20):
        w = rng.randrange(1, 65)
        N = TS + w + 4                                 # bit i holds cell i - N; cell 0 is bit N
        row = (rng.getrandbits(w) << (N - w)) & ((1 << N) - 1)   # cells -w .. -1, column 0 = tau(0) = 0
        maskN = (1 << (N + 1)) - 1
        seqs = {k: [] for k in cols}
        words = []
        for t in range(TS):
            if t >= TS // 2:
                for k in cols:
                    seqs[k].append((row >> (N - k)) & 1)
                words.append((row >> (N - 10)) & 1023)
                if t % 2:
                    odd_n += 1
                    odd_ok += (row >> (N - 1)) & 1
            row = ((row << 1) ^ (row | (row >> 1))) & maskN
            row = (row & ~(1 << N)) | (((t + 1) % 2) << N)
        for k in cols:
            worst = min(worst, h(seqs[k]))
        spatial.append(H_words(words, 10) - H_words([x >> 1 for x in words], 9))
    sp = min(spatial)
    cw = [rng.getrandbits(10) for _ in range(TS // 2)]
    ref_sp = H_words(cw, 10) - H_words([x >> 1 for x in cw], 9)
    print(f"   driven left half-line, 20 seeds: lowest column h_10 {worst:.4f} (coin flips {h_coin_D:.4f}); lowest "
          f"spatial entropy per cell of 10-cell patterns {sp:.4f} (coin flips {ref_sp:.4f}); x(-1) = 1 at "
          f"{odd_ok / odd_n:.4f} of odd times", flush=True)
    verdict("CR3 the driven left side's columns and patterns are within 0.05 of coin flips (a counterexample needs at "
            "most 0.064)", worst >= h_coin_D - 0.05 and sp >= ref_sp - 0.05, f"columns {worst:.4f}, patterns {sp:.4f}")
    verdict("CR4 the period-2 condition holds at 0.50 +- 0.01 of odd times", abs(odd_ok / odd_n - 0.5) <= 0.01,
            f"{odd_ok / odd_n:.4f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def balance():
    cyc = band_cycle()
    P = len(cyc)
    kinds = Counter()
    unb_ones = unb_cells = 0
    for e in range(K):
        seq = [(v >> e) & 1 for v in cyc]
        p = 1
        while p < P and any(seq[i] != seq[(i + p) % P] for i in range(P)):
            p *= 2
        ones = sum(seq[:p])
        if 2 * ones == p:
            kinds["balanced"] += 1
        else:
            kinds["white" if ones == 0 else "black" if ones == p else "other"] += 1
            unb_ones += ones * (P // p)
            unb_cells += P
    share = kinds["balanced"] / K
    ud = unb_ones / unb_cells if unb_cells else float("nan")
    print(f"   diagonals 0 to {K - 1}: {dict(kinds)}; the unbalanced ones' density {ud:.5f} over {unb_cells // P} "
          f"diagonals", flush=True)
    verdict("CR5 at least 75% of band diagonals exactly balanced; the rest within 0.001 of 1/2",
            share >= 0.75 and abs(ud - 0.5) <= 0.001, f"{share:.4f} balanced; the rest {ud:.5f}")


if __name__ == "__main__":
    balance() if "balance" in sys.argv[1:] else main()
