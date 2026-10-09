#!/usr/bin/env python3
"""rule30_cloud_right_front.py: a right-hand front for the single cell, built from the edge ruler, and its spectrum.

RUN-ON:     cpu (Python 3 standard library; big-integer diagonals; a pure-Python FFT)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_right_front.py [LOG2T=23] [SEEDS=20]
COST:       about a minute.

Why (the owner, 2026-10-09): "Can we construct a 'right side' waveform of a type that makes sense given the chaotic
nature of the right half, possibly rooted in the discovery of the linear ruler".

By hand, before the run (Cloud). Right diagonal k is D_k(t) = x_t(t - k), and D_k(t + 1) = D_k(t) XOR (D_(k-1)(t)
OR D_(k-2)(t)), so each is a running XOR of a periodic sequence: purely periodic from t = 0, with period p_k =
p_(k-1) or 2 p_(k-1) (§8.27). So p_k is a non-decreasing power of 2 (OEIS A094605).
  The front. On the left, a diagonal counts as ordered once it has settled into its repeat (B(t), §8.74). On the
    right every diagonal repeats from the start, but its repeat is visible by row t only if p_k <= t. So the right
    front is R(t) = #{k >= 1 : p_k <= t}, the cell x = t - R(t). Both fronts are one rule: a cell is in order at
    row t when its diagonal, from row t on, repeats with a period no longer than t.
  It is the ruler. Proposition 23 says the white triangle on the edge at even t has width L(t) = min{j : p_j does
    not divide t} - 1. With p_j non-decreasing powers of 2, p_j divides t exactly when p_j <= 2^v(t), so
    L(t) = #{k >= 1 : p_k divides t} = R(2^v(t)), and R(t) = L(2^floor(log2 t)). The right front is a staircase that
    steps at each power of 2, and at row 2^n the edge triangle fills the ordered strip exactly: its inner corner
    touches the front. Between powers of 2 the triangles are the ruler's shorter marks.
  Its spectrum, exactly. L(t) = sum over k of the comb [p_k divides t]. Over the window t in [N, 2N), N = 2^n, every
    comb with p_k <= N is whole and starts at phase 0, and no comb with p_k > N has a tooth there. So the FFT of L
    over that window is X(b) = sum over k with p_k <= N and p_k b = 0 (mod N) of N / p_k, real and non-negative, and
    exactly 0 at every other bin: spikes at every dyadic frequency j / 2^m and nothing else. The left front's steps
    have a flat spectrum with no spikes (rule30_cloud_front_spectrum.py); the right front is the opposite case.
  Finite seeds. For any finite seed the pattern's right edge moves right at speed 1 and stays black, and the same
    recurrence holds with D_k(0) the seed's cell at depth k. A running XOR from any start is still purely periodic, so
    every finite seed has purely periodic right diagonals with power-of-2 periods; whether the periods match the single
    cell's is open here.

PREDICTIONS, written 2026-10-09 before any run of this script.
  RF1 (control). Direct simulation of the single cell: the white run just inside the edge at t = 2^n equals R(2^n)
      for n = 1 .. 12, and R(2^n) for n = 1 .. 21 equals §8.73's widths 2, 3, 5, 6, 8, 14, 15, 23, 24, 26, 28, 33,
      35, 36, 38, 40, 42, 47, 48, 50, 53.
  RF2 (the formula). The FFT of L over [2^16, 2^17), with L read directly off the diagonals, matches the formula
      above at every bin to within 1e-6 of the
      largest bin, and every bin the formula makes 0 is below that. Confidence 0.95 (a derivation; a failure would be
      an error in it or the code).
UNEXPECTED CHECK, RF3: the right front is not universal. Among SEEDS random finite seeds of width 16 (seeded, so
  repeatable), at least half have a period staircase p_1 .. p_40 that differs from the single cell's somewhere, yet
  every one has R(2^20) within 4 of the single cell's 50. Confidence 0.4.
Counterfactual: identical staircases for every seed would make the right strip universal, as the left stripes are
  (§8.31), so both fronts would forget the seed.
REFUTED-BY: RF1 or RF2 failing (the derivation or the instrument); RF3 failing as worded.
Disclosed: after writing these predictions and before pushing them, smoke tests at LOG2T = 18 with SEEDS = 0
  exercised the code (RF1's simulation and RF2's FFT ran, at a size too small for RF1's later widths; RF3 did not
  run). They showed RF2's formula exact there and the power shares by denominator printed below. Nothing above was
  changed after them.

OUTCOME of the first run, 2026-10-09 (by 10:50 BST, 29 s at LOG2T = 23, SEEDS = 20).
  RF1 PASS. R(2^n) for n = 1 .. 21 is §8.73's widths, and direct simulation agrees at t = 2^1 .. 2^12. R(2^n)/n is
    2.60 at n = 10, 2.50 at 16 and 2.53 at 19: the front sits about 2.5 log2(t) cells inside the right edge.
  RF2 PASS. The FFT of the ruler over [2^16, 2^17) equals the formula at every bin (error 0 in floating point). Its
    power sits on the coarse dyadic frequencies: 41% at 1/2, 57% on denominators up to 4, 78% up to 16, 99.5% up to
    256. Amplitudes, as a share of N, are 1.76, 0.76, 0.51, 0.26, 0.20, 0.14, 0.046 at 1/2 .. 1/128.
  RF3 HELD in part, REFUTED as worded. All 20 seeds have a staircase different from the single cell's (from k = 3,
    9, 12 or 14), but only 8 of 20 have R(2^20) within 4 of 50; the range is 39 to 58. The right front is not
    universal: right diagonals are running XORs from the seed's own cells and never forget them, while the left
    stripes forget the seed (§8.31).

CORRECTED 2026-10-09 after GPT's GC755 to GC757 (read by hand: correct); the text above is kept as first written.
  For a general seed the periods p_k need not be monotone, so the ordered strip is the prefix
    R_prefix(t) = min{k >= 1 : p_k > t} - 1 = #{j >= 1 : Q_j <= t}, with Q_j = lcm(p_0 .. p_j) (GC756). RF3's R(2^20)
    values are counts #{k <= 60 : p_k <= 2^20}, not prefixes; whether the two agree for those seeds was not checked.
    Every nonempty finite seed has unbounded periods (GC755), and R_prefix(t) >= floor(log2 t) (GC756).
  The white-run ruler and its spectrum are the single cell's: for a general seed the edge run is replaced by the
    return to the seed's own bits (GC756; seed 11 has a black cell just inside its edge at t = 2).
"""
import cmath
import math
import random
import sys

LOG2T = int(sys.argv[1]) if len(sys.argv) > 1 else 23
SEEDS = int(sys.argv[2]) if len(sys.argv) > 2 else 20
T = 1 << LOG2T
MASK = (1 << T) - 1
KMAX = 60


def prefix_xor(g):
    x, sh = g, 1
    while sh < T:
        x ^= (x << sh) & MASK
        sh <<= 1
    return x


def diagonals(init):
    """Right diagonals 0 .. KMAX as big integers (bit t = D_k(t)); init[k] = D_k(0)."""
    D = [MASK]                                              # the edge: black for ever
    prev2, prev1 = 0, MASK
    for k in range(1, KMAX + 1):
        g = prev1 | prev2
        d = (prefix_xor(g) << 1) & MASK                     # XOR of g(0 .. t-1)
        if init.get(k, 0):
            d ^= MASK
        D.append(d)
        prev2, prev1 = prev1, d
    return D


def periods(D):
    out = []
    for d in D:
        p, found = 1, None
        while 2 * p <= T // 2:
            m = (1 << (T - p)) - 1
            if (d >> p) & m == d & m:
                found = p
                break
            p <<= 1
        out.append(found)
    return out


def R_of(per, t):
    return sum(1 for p in per[1:] if p is not None and p <= t)


def fft(a):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j |= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    size = 2
    while size <= n:
        w = cmath.exp(-2j * math.pi / size)
        half = size // 2
        tw = [w ** k for k in range(half)]
        for start in range(0, n, size):
            for k in range(half):
                u, v = a[start + k], a[start + k + half] * tw[k]
                a[start + k], a[start + k + half] = u + v, u - v
        size <<= 1
    return a


def main():
    D = diagonals({})
    per = periods(D)
    known = [p for p in per if p is not None]
    print(f"T = 2^{LOG2T}; single cell's periods p_0 .. p_{len(known) - 1}:", ", ".join(map(str, known)))
    # RF1: the front at powers of 2, against the widths and against direct simulation
    widths = [2, 3, 5, 6, 8, 14, 15, 23, 24, 26, 28, 33, 35, 36, 38, 40, 42, 47, 48, 50, 53]
    Rn = [R_of(per, 1 << n) for n in range(1, 22)]
    print("R(2^n), n = 1 .. 21:", Rn, "(= §8.73's widths)" if Rn == widths else "(DIFFERS from §8.73's widths)")
    S = 1 << 12
    x, bad = 1 << S, 0
    for t in range(S + 1):
        if t and t & (t - 1) == 0:
            run, k = 0, 1
            while k <= t and not (x >> (S + t - k)) & 1:
                run, k = run + 1, k + 1
            n = t.bit_length() - 1
            if run != R_of(per, t):
                bad += 1
                print(f"  RF1 mismatch at t = 2^{n}: run {run}, R {R_of(per, t)}")
        x = ((x << 1) ^ (x | (x >> 1))) & ((1 << (2 * S + 2)) - 1)
    print(f"direct simulation at t = 2^1 .. 2^12: {bad} mismatches")
    print("the front x = t - R(t) and the fit R(2^n) / n:",
          ", ".join(f"n={n}: {R_of(per, 1 << n)} ({R_of(per, 1 << n) / n:.2f})" for n in range(4, 22, 3)))
    # RF2: the spectrum of the ruler L(t) over [N, 2N)
    n = 16
    N = 1 << n
    cols = [bin((D[k] >> N) & ((1 << N) - 1))[2:].zfill(N)[::-1] for k in range(KMAX + 1)]
    Lw = []
    for i in range(N):                                     # the white run just inside the edge, read off the diagonals
        k = 1
        while k <= KMAX and cols[k][i] == "0":
            k += 1
        Lw.append(k - 1)
    X = fft([complex(v) for v in Lw])
    pred = [sum(N // p for p in per[1:] if p is not None and p <= N and (p * b) % N == 0) for b in range(N)]
    top = max(abs(v) for v in X)
    err = max(abs(X[b] - pred[b]) for b in range(N))
    zero_max = max((abs(X[b]) for b in range(N) if pred[b] == 0), default=0.0)
    print(f"FFT of the ruler over [2^{n}, 2^{n + 1}): largest bin {top:.1f}; largest error against the formula "
          f"{err:.2e} ({err / top:.1e} of the largest); largest bin the formula makes 0: {zero_max:.2e}")
    tot = sum(abs(X[b]) ** 2 for b in range(1, N))
    shares = []
    for m in range(1, n + 1):
        step = N >> m                                      # frequencies j / 2^m are the bins that are multiples of this
        shares.append(sum(abs(X[b]) ** 2 for b in range(step, N, step)) / tot)
    print("  share of the power (zero frequency left out) on frequencies j/2^m with denominator at most 2^m: " +
          ", ".join(f"m={m}: {sh:.4f}" for m, sh in enumerate(shares, 1) if m in (1, 2, 3, 4, 6, 8, 10, 12, 16)))
    print("  amplitude depends only on the denominator 2^m of the frequency "
          "(a diagonal of period N adds 1 to every bin):")
    for m in range(1, 13):
        b = N >> m                                          # frequency 1 / 2^m
        print(f"    f = j/2^{m:<2d} (j odd): {pred[b]:8d}  ({pred[b] / N:.4f} of N)")
    # RF3: random finite seeds
    rng = random.Random(20261009)
    diff, near = 0, 0
    print(f"{SEEDS} random seeds of width 16 (rightmost cell black): staircase vs the single cell's, and R(2^20)")
    for i in range(SEEDS):
        w = [rng.randint(0, 1) for _ in range(15)] + [1]    # w[-1] is the rightmost cell
        init = {k: w[-1 - k] for k in range(1, 16)}         # depth k from the right edge
        Ds = diagonals(init)
        ps = periods(Ds)
        same = ps[1:41] == per[1:41]
        r20 = R_of(ps, 1 << 20)
        first = next((k for k in range(1, 41) if ps[k] != per[k]), None)
        diff += not same
        near += abs(r20 - R_of(per, 1 << 20)) <= 4
        print(f"  seed {''.join(map(str, w))}: " + ("same staircase" if same else f"differs from k = {first}")
              + f", R(2^20) = {r20}")
    print(f"RF3: {diff} of {SEEDS} differ; {near} of {SEEDS} have R(2^20) within 4 of {R_of(per, 1 << 20)}")


if __name__ == "__main__":
    main()
