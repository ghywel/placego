#!/usr/bin/env python3
"""rule30_churn.py: does the left side churn the wheel into noise? The owner's question (2026-10-04): "does it hold
that the left is still mostly random and the wheel churns the noise?"

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_churn.py [D=100000] [W=14] [K=192]
COST:       a few minutes on one core.

Under the pure wheel there is no noise going in: column 0 = 0101... and column 1 = the universal word U are both
exactly periodic, and the left half is a deterministic function of them. If it looks random, the left side
manufactures the noise, as Rule 30 does when it is used as a random-number generator. Three measurements:
  randomness  block entropy H_m / m (bits per cell, from the counts of all blocks of m cells), the share of ones, and
              the flatness of the spectrum (Wiener-Khinchin, M = 512 lags, as in rule30_spectrum.py), for the pure
              wheel's left half (all 28 phases of U, depths 1..D each), against coin flips of the same size;
  churn       flip one bit of column 1 (the wheel, at all 28 phases) at time t0, recompute the left half, and count
              the share of cells that change at depths t0 + 1 .. t0 + 1000;
  the arms    H_m / m for m <= 8 within depth K: coin flips, left alone (random columns 1), both sides exact (every
              right half up to W cells), the pure wheel.

PREDICTIONS, written 2026-10-04 before this script's first run:
  N1 (blind): the pure wheel's left half has H_m / m >= 0.99 for every m = 1..12.
  N2 (blind): its spectrum is flat: |S(f) - 1| <= 0.1 at every frequency.
  N3 (blind): a flip at an even time t0 = 1000 (column 0 is 0 there, so the left side sees it) changes between 45% and
     55% of the cells at depths 1001..2000: an avalanche.
  C0 (control, exact, Lemma 1): a flip at the odd time t0 = 1001 (column 0 is 1) changes no cell at all.
  C1 (control): coin flips of the same size give H_m / m >= 0.99 for m = 1..12, and |S(f) - 1| <= 0.1.
  CF (counterfactual): the wheel U itself, read as a sequence, has H_12 / 12 <= 0.5 and a spectral line above 2; so
     the instrument sees structure where there is some.
REFUTED-BY: C0, C1 or CF failing (the instrument); N1, N2 or N3 failing.

OUTCOME of the first run, 2026-10-04 (D = 100,000, W = 14, K = 192): C0 (0 cells changed), C1 (lowest H_m/m 0.9999,
largest |S - 1| 0.0407) and CF (H_12/12 0.3165, a line at 113.3) passed. N1 HELD (lowest H_m/m 0.9999; share of ones
0.5000). N2 HELD (largest |S - 1| 0.0341). N3 HELD (0.5046 of cells changed). The arms, H_8/8 within depth 192: coin
flips 1.0000, left alone 0.9997, both sides exact 0.9971, pure wheel 0.9920. The last is not comparable: its 28
sequences give only about 5,000 blocks, so the estimate is biased low by about 0.004; the other arms have about
3 million blocks each.
"""
import math, random, sys, pathlib
from collections import Counter

D = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
W = int(sys.argv[2]) if len(sys.argv) > 2 else 14
K = int(sys.argv[3]) if len(sys.argv) > 3 else 192
MLAG = 512

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
import rule30_wheel_left as wl                         # noqa: E402
sys.argv = _argv
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def entropies(seqs, mmax):
    out = []
    for m in range(1, mmax + 1):
        cnt = Counter()
        for s in seqs:
            x = 0
            for i, b in enumerate(s):
                x = ((x << 1) | b) & ((1 << m) - 1)
                if i >= m - 1:
                    cnt[x] += 1
        n = sum(cnt.values())
        out.append(-sum(c / n * math.log2(c / n) for c in cnt.values()) / m)
    return out


def spectrum_dev(seqs):
    agree, ones, cells, pairs = [0] * (MLAG + 1), 0, 0, [0] * (MLAG + 1)
    for s in seqs:
        n = len(s)
        x = sum(b << k for k, b in enumerate(s))
        ones += bin(x).count("1")
        cells += n
        for j in range(MLAG + 1):
            agree[j] += n - j - bin((x ^ (x >> j)) & ((1 << (n - j)) - 1)).count("1")
            pairs[j] += n - j
    mean = (2 * ones - cells) / cells
    C = [(2 * a - p) / p - mean * mean for a, p in zip(agree, pairs)]
    win = [(1 + math.cos(math.pi * j / (MLAG + 1))) / 2 * C[j] for j in range(MLAG + 1)]
    S = [C[0] + 2 * sum(win[j] * math.cos(2 * math.pi * (i / (2 * MLAG)) * j) for j in range(1, MLAG + 1))
         for i in range(MLAG + 1)]
    return max(abs(v - 1) for v in S), max(S), ones / cells


def left_from_col1(tau, c1bits, depth):
    c0 = sum(b << t for t, b in enumerate(tau))
    c1 = sum(b << t for t, b in enumerate(c1bits))
    cols, out = [c1, c0], []
    for k in range(1, depth + 1):
        m = (1 << (depth - k + 1)) - 1
        cols.append(((cols[-1] >> 1) ^ (cols[-1] | cols[-2])) & m)
        out.append(cols[-1] & 1)
    return out


def main():
    rng = random.Random(1729)
    tau56 = [t % 2 for t in range(56)]
    phases = [[int(wl.U[(t - r) % 56]) for t in range(56)] for r in range(0, 56, 2)]
    wheel = []
    for sigma in phases:
        L, _, _, _ = wl.forced(tau56, sigma, D)
        wheel.append(L[:D])
    coin = [[rng.getrandbits(1) for _ in range(D)] for _ in range(len(phases))]

    Hc = entropies(coin, 12)
    dc, _, _ = spectrum_dev(coin)
    report("C1 coin flips: H_m/m >= 0.99 for m = 1..12, and a flat spectrum", min(Hc) >= 0.99 and dc <= 0.1,
           f"lowest H_m/m {min(Hc):.4f}, largest |S - 1| {dc:.4f}")
    Hu = entropies([[int(c) for c in wl.U * 200]], 12)
    _, top, _ = spectrum_dev([[int(c) for c in wl.U * 200]])
    report("CF the wheel U itself shows its structure (H_12/12 <= 0.5, a line above 2)", Hu[-1] <= 0.5 and top > 2,
           f"H_12/12 {Hu[-1]:.4f}, highest S {top:.1f}")

    Hw = entropies(wheel, 12)
    dw, topw, onesw = spectrum_dev(wheel)
    print(f"\n   pure wheel's left half, 28 phases x {D} cells: share of ones {onesw:.4f}; H_m/m, m = 1..12: "
          + " ".join(f"{h:.4f}" for h in Hw), flush=True)
    verdict("N1 the pure wheel's left half has H_m/m >= 0.99 for m = 1..12", min(Hw) >= 0.99, f"lowest {min(Hw):.4f}")
    verdict("N2 its spectrum is flat, |S - 1| <= 0.1", dw <= 0.1, f"largest |S - 1| {dw:.4f}, highest S {topw:.3f}")

    T = 2200
    tau = [t % 2 for t in range(T + 1)]
    changed, odd_changed, cells = 0, 0, 0
    for sigma in phases:
        c1 = [sigma[t % 56] for t in range(T + 1)]
        base = left_from_col1(tau, c1, T)
        for t0, is_even in ((1000, True), (1001, False)):
            c1f = list(c1)
            c1f[t0] ^= 1
            Lf = left_from_col1(tau, c1f, T)
            diff = sum(a != b for a, b in zip(base[t0:t0 + 1000], Lf[t0:t0 + 1000]))
            if is_even:
                changed += diff
                cells += 1000
            else:
                odd_changed += sum(a != b for a, b in zip(base, Lf))
    report("C0 a flip at an odd time changes no cell (Lemma 1)", odd_changed == 0, f"{odd_changed} cells changed")
    share = changed / cells
    verdict("N3 a flip at an even time changes 45% to 55% of the next 1000 cells (an avalanche)", 0.45 <= share <= 0.55,
            f"{share:.4f}")

    print(f"\n   the arms, H_m/m for m = 1..8 within depth {K}:", flush=True)
    tauK = [t % 2 for t in range(K + 1)]
    arms = {
        "coin flips": [[rng.getrandbits(1) for _ in range(K)] for _ in range(1 << W)],
        "left alone": [left_from_col1(tauK, [rng.getrandbits(1) for _ in range(K + 1)], K) for _ in range(1 << W)],
        "both sides exact": [r30.forced_left(R, tauK, K) for R in range(1 << W)],
        "pure wheel (28 phases)": [w[:K] for w in wheel],
    }
    for name, seqs in arms.items():
        H = entropies(seqs, 8)
        ones = sum(map(sum, seqs)) / sum(map(len, seqs))
        print(f"      {name:>24}: ones {ones:.4f}; " + " ".join(f"{h:.4f}" for h in H), flush=True)
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
