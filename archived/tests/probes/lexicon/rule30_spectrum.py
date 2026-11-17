#!/usr/bin/env python3
"""rule30_spectrum.py: the owner's Fourier lead (2026-10-04, after Rowland's pyramid and triangle). Power spectra of
the forced left half and of column 1, looking for frequency spikes: at sevenths (the 7-cell ring, section 8.3) or at
dyadic frequencies (octaves: Rowland's and Jen's right diagonals have periods 2^alpha)?

RUN-ON:     cpu (pure Python 3, standard library; exact two-sided arm, seeded comparison arms)
COMMAND:    python3 tests/probes/lexicon/rule30_spectrum.py [W=14] [K=192] [T=512] [JOBS=4]
COST:       a few minutes on 4 cores.

Method. A sequence b(0..n-1) becomes s = 2b - 1. Its autocovariance C(j), pooled over the samples of an arm, comes
from exact bit counts (agreements at lag j by XOR and popcount). The spectrum is the Fourier transform of C
(Wiener-Khinchin), with a Hann lag window over M = n/2 lags:
    S(f) = C(0) + 2 * sum_{j=1..M} w(j) C(j) cos(2 pi f j),   w(j) = (1 + cos(pi j / (M + 1))) / 2,
at f = m / (2M), m = 0..M. A spike is a local maximum of S with 0 < f < 1/2.
  left half: L(1..K), both sides exact (every right half up to W cells) against left alone (the same number of
             seeded random columns 1); the excess spectrum is S_both - S_left.
  column 1:  sigma(0..T-1) made by every right half up to W cells, column 0 clamped to the word.

PREDICTIONS, written 2026-10-04 before this script's first run:
  F0 (consistency, not blind: section 8.3 found the lag-7 resonance): for 0001, 0011 and 0111, the highest spike of
     the left half's excess spectrum lies within 1/192 of 1/7, 2/7 or 3/7.
  F1 (octaves, blind): for trace 0101..., at least three of the five highest spikes of column 1's spectrum lie within
     1/512 of a multiple of 1/32. (By chance, about 4 in 100.)
  C1 (control, known answer): coin flips of the same length and number give a flat spectrum, |S(f) - 1| <= 0.05.
  C2 (counterfactual, must be seen): the 7-periodic word 0001011 repeated, with 10% of its bits flipped at random,
     has its highest spike within 1/512 of a multiple of 1/7.
REFUTED-BY: C1 or C2 failing (the instrument); F0 or F1 failing.
(The tolerances are coded as 1/K and 1/T, which are the 1/192 and 1/512 above at the default sizes.)

OUTCOME of the first run, 2026-10-04 (W = 14, K = 192, T = 512): C1 passed (largest |S - 1| = 0.0206), and so did C2
(spike at 0.1426). F0 HELD for 0001, 0011 and 0111 (highest excess lines 1/7, 2/7, 2/7). It was not blind: a dry run
at a tiny size had already shown 0001 and 0011. The excess spectra are harmonic series of the 7-cell ring (1/7, 2/7,
3/7) with the 14-cell ring's 1/14, 3/14, 5/14; 01's highest excess line is 2/7 too (+0.52). F1 was REFUTED (1 of 5
spikes dyadic). Column 1 for 0101... is dominated by a line near 0.303 and its mirror 0.197 = 1/2 - 0.303, pinned by
rule30_spectrum_fine.py at 0.30365. Column 1 for 0001 is a line at 1/4 of power 122, against 0.1 elsewhere.
"""
import math, random, sys, pathlib
from fractions import Fraction
from multiprocessing import Pool

W = int(sys.argv[1]) if len(sys.argv) > 1 else 14
K = int(sys.argv[2]) if len(sys.argv) > 2 else 192
T = int(sys.argv[3]) if len(sys.argv) > 3 else 512
JOBS = int(sys.argv[4]) if len(sys.argv) > 4 else 4

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
import rule30_twosided as ts                           # noqa: E402
sys.argv = _argv
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def counts(bits, M):
    """(ones, agreements at lags 0..M) of one binary sequence."""
    n = len(bits)
    x = sum(b << k for k, b in enumerate(bits))
    return bin(x).count("1"), [n - j - bin((x ^ (x >> j)) & ((1 << (n - j)) - 1)).count("1") for j in range(M + 1)]


def add(acc, c):
    if acc is None:
        return [c[0], list(c[1]), 1]
    acc[0] += c[0]
    acc[1] = [u + v for u, v in zip(acc[1], c[1])]
    acc[2] += 1
    return acc


def spectrum(acc, n, M):
    ones, agree, N = acc
    mean = (2 * ones - N * n) / (N * n)
    C = [(2 * a - N * (n - j)) / (N * (n - j)) - mean * mean for j, a in enumerate(agree)]
    out = []
    for m in range(M + 1):
        f = m / (2 * M)
        s = C[0] + 2 * sum((1 + math.cos(math.pi * j / (M + 1))) / 2 * C[j] * math.cos(2 * math.pi * f * j)
                           for j in range(1, M + 1))
        out.append(s)
    return out


def spikes(S, M, top=5):
    peaks = [m for m in range(1, M) if S[m] > S[m - 1] and S[m] >= S[m + 1]]
    peaks.sort(key=lambda m: -S[m])
    return [(m / (2 * M), S[m]) for m in peaks[:top]]


def near(f, step, tol):
    return abs(f / step - round(f / step)) * step <= tol and round(f / step) > 0


def name_of(f):
    fr = Fraction(f).limit_denominator(16)
    return f"{f:.4f} (~{fr.numerator}/{fr.denominator})"


def left_both(args):
    word, lo, hi = args
    tau = [word[t % len(word)] for t in range(K + 1)]
    acc = None
    for R in range(lo, hi):
        acc = add(acc, counts(r30.forced_left(R, tau, K), K // 2))
    return acc


def left_alone(args):
    word, seed, n = args
    rng = random.Random(seed)
    tau = [word[t % len(word)] for t in range(K + 1)]
    c0 = sum(b << t for t, b in enumerate(tau))
    acc = None
    for _ in range(n):
        cols, L = [rng.getrandbits(K + 1), c0], []
        for k in range(1, K + 1):
            m = (1 << (K - k + 1)) - 1
            cols.append(((cols[-1] >> 1) ^ (cols[-1] | cols[-2])) & m)
            L.append(cols[-1] & 1)
        acc = add(acc, counts(L, K // 2))
    return acc


def col1_chunk(args):
    word, lo, hi = args
    acc = None
    for R in range(lo, hi):
        acc = add(acc, counts(ts.column1(R, word, T), T // 2))
    return acc


def control_chunk(args):
    kind, seed, n = args
    rng = random.Random(seed)
    acc = None
    for _ in range(n):
        if kind == "coin":
            bits = [rng.getrandbits(1) for _ in range(T)]
        else:
            ph = rng.randrange(7)
            bits = [int("0001011"[(t + ph) % 7]) ^ (rng.random() < 0.1) for t in range(T)]
        acc = add(acc, counts(bits, T // 2))
    return acc


def merge(parts):
    acc = None
    for p in parts:
        if acc is None:
            acc = [p[0], list(p[1]), p[2]]
        else:
            acc[0] += p[0]
            acc[1] = [u + v for u, v in zip(acc[1], p[1])]
            acc[2] += p[2]
    return acc


def main():
    N = 1 << W
    Mk, Mt = K // 2, T // 2
    with Pool(JOBS) as pool:
        coin = merge(pool.map(control_chunk, [("coin", 11 + s, N // 16) for s in range(16)]))
        Sc = spectrum(coin, T, Mt)
        report("C1 coin flips give a flat spectrum", max(abs(s - 1) for s in Sc) <= 0.05,
               f"largest |S - 1| = {max(abs(s - 1) for s in Sc):.4f}")
        planted = merge(pool.map(control_chunk, [("planted", 97 + s, N // 16) for s in range(16)]))
        top = spikes(spectrum(planted, T, Mt), Mt)
        report("C2 a planted 7-periodic signal shows its spike at a multiple of 1/7", near(top[0][0], 1 / 7, 1 / T),
               f"highest spike {name_of(top[0][0])}")
        print("\nLeft half, excess spectrum S_both - S_left (highest spikes, 0 < f < 1/2):")
        for word in [(0, 1), (0, 0, 0, 1), (0, 0, 1, 1), (0, 1, 1, 1)]:
            name = "".join(map(str, word))
            b = merge(pool.map(left_both, [(word, lo, min(lo + 1024, N)) for lo in range(0, N, 1024)]))
            a = merge(pool.map(left_alone, [(word, 4241 + 17 * s + int(name, 2), N // 16) for s in range(16)]))
            Sb, Sa = spectrum(b, K, Mk), spectrum(a, K, Mk)
            ex = spikes([u - v for u, v in zip(Sb, Sa)], Mk)
            print(f"   {name}: " + "; ".join(f"{name_of(f)} +{h:.3f}" for f, h in ex))
            if len(word) == 4:
                hit = min(abs(ex[0][0] - k / 7) for k in (1, 2, 3)) <= 1 / K
                verdict(f"F0 word {name}: the highest excess spike within 1/192 of 1/7, 2/7 or 3/7", hit,
                        f"highest {name_of(ex[0][0])}")
        print("\nColumn 1 made by the right side, spectrum (highest spikes, 0 < f < 1/2):")
        for word in [(0, 1), (1, 0), (0, 0, 0, 1)]:
            name = "".join(map(str, word))
            acc = merge(pool.map(col1_chunk, [(word, lo, min(lo + 1024, N)) for lo in range(0, N, 1024)]))
            sp = spikes(spectrum(acc, T, Mt), Mt)
            print(f"   {name}: " + "; ".join(f"{name_of(f)} {h:.3f}" for f, h in sp))
            if word == (0, 1):
                dy = sum(near(f, 1 / 32, 1 / T) for f, _ in sp)
                verdict("F1 trace 0101...: at least 3 of column 1's 5 highest spikes at multiples of 1/32", dy >= 3,
                        f"{dy} of 5")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
