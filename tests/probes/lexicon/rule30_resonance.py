#!/usr/bin/env python3
"""rule30_resonance.py: are the two-sided left halves resonating with Rule 30's ring orbits?

RUN-ON:     cpu (pure Python 3, standard library; exact for the two-sided arm, seeded for the left-alone arm)
COMMAND:    python3 tests/probes/lexicon/rule30_resonance.py [W=16] [K=192] [JOBS=4]
COST:       about five minutes on 4 cores.

Where this comes from. rule30_harmonics.py tested the owner's "harmonics" lead (structure at multiples of column 0's
period p) and refuted it: the strongest excess correlation sat at lag 7 for all three words of period 4. Rule 30 on a
ring of 7 cells has 4-cycles, and their columns are 0001, 0011 and 0111 up to rotation. So the resonator may be a ring
orbit whose column carries the trace word, not the word's period. This script lists, for each word, the ring sizes
n <= 15 with such an orbit (cycles up to 64 steps), and measures the interaction with a covariance:
  Xc(j) = [A_both(j) - m_both^2] - [A_left(j) - m_left^2],
where A(j) is the mean of s(k) s(k+j), s = 2L - 1, and m is the mean of s, so that a difference in density between
the arms no longer raises every lag (the flaw found in rule30_harmonics.py's X). Both arms are as there: every right
half up to W cells against the same number of seeded random columns 1.

Ring sizes (computed below, printed, and checked against these before the measurement runs):
  01: 7, 14.  001, 011: 12.  0001, 0011, 0111: 7, 14.  01011: 5, 10, 15.  00001, 01111: 15.
  00011, 00101, 00111: none.  Every primitive word of period 6: none.

PREDICTIONS, written 2026-10-04 before this script's first run:
  Q0 (check, not blind): 0001, 0011 and 0111 keep their peak at lag 7 with the covariance, |Xc(7)| >= 0.05.
  Q1 (blind): 01011, the only period-5 word with an orbit on a ring of 12 or fewer cells, peaks at lag 5 or 10, with
     |Xc| >= 0.05 there.
  Q2 (blind): the other five words of period 5, and all nine of period 6, have |Xc(j)| < 0.05 at every lag 1..12.
  C  (control, the noise floor): two independent left-alone samples differ by at most 0.005 in every Xc(j).
  R  (control): the ring sizes computed here equal the list above.
REFUTED-BY: C or R failing (the instrument); Q0, Q1 or Q2 failing for any word.
"""
import random, sys, pathlib
from multiprocessing import Pool

W = int(sys.argv[1]) if len(sys.argv) > 1 else 16
K = int(sys.argv[2]) if len(sys.argv) > 2 else 192
JOBS = int(sys.argv[3]) if len(sys.argv) > 3 else 4
LAGS = list(range(1, 13))
OLD = ["01", "10", "001", "011", "0001", "0011", "0111"]
P5 = ["00001", "00011", "00101", "00111", "01011", "01111"]
P6 = ["000001", "000011", "000101", "000111", "001011", "001101", "001111", "010111", "011111"]
EXPECTED_RINGS = {"01": [7, 14], "001": [12], "011": [12], "0001": [7, 14], "0011": [7, 14], "0111": [7, 14],
                  "01011": [5, 10, 15], "00001": [15], "01111": [15], "00011": [], "00101": [], "00111": [],
                  **{w: [] for w in P6}}

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
sys.argv = _argv
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def canon(w):
    p = len(w)
    for d in range(1, p + 1):
        if p % d == 0 and w == w[:d] * (p // d):
            w = w[:d]
            break
    return min(w[i:] + w[:i] for i in range(len(w)))


def ring_words(nmax=15, cmax=64):
    """canonical column word -> ring sizes n with a cycle (length <= cmax) having that column."""
    out = {}
    for n in range(2, nmax + 1):
        m = (1 << n) - 1

        def step(x):
            return (((x << 1) | (x >> (n - 1))) & m) ^ (x | (((x >> 1) | (x << (n - 1))) & m))
        visited = set()
        for x0 in range(1 << n):
            if x0 in visited:
                continue
            path, pos, x = [], {}, x0
            while x not in pos and x not in visited:
                pos[x] = len(path)
                path.append(x)
                x = step(x)
            visited.update(path)
            if x in pos and len(path) - pos[x] <= cmax:
                cyc = path[pos[x]:]
                for i in range(n):
                    out.setdefault(canon("".join(str((s >> i) & 1) for s in cyc)), set()).add(n)
    return out


def sums(L):
    x = sum(b << k for k, b in enumerate(L))
    ones = bin(x).count("1")
    agree = [K - j - bin((x ^ (x >> j)) & ((1 << (K - j)) - 1)).count("1") for j in LAGS]
    return ones, agree


def both_chunk(args):
    word, lo, hi = args
    tau = [word[t % len(word)] for t in range(K + 1)]
    ones, agree = 0, [0] * len(LAGS)
    for R in range(lo, hi):
        o, a = sums(r30.forced_left(R, tau, K))
        ones += o
        agree = [u + v for u, v in zip(agree, a)]
    return ones, agree, hi - lo


def left_chunk(args):
    word, seed, n = args
    rng = random.Random(seed)
    tau = [word[t % len(word)] for t in range(K + 1)]
    c0 = sum(b << t for t, b in enumerate(tau))
    ones, agree = 0, [0] * len(LAGS)
    for _ in range(n):
        cols, L = [rng.getrandbits(K + 1), c0], []
        for k in range(1, K + 1):
            m = (1 << (K - k + 1)) - 1
            cols.append(((cols[-1] >> 1) ^ (cols[-1] | cols[-2])) & m)
            L.append(cols[-1] & 1)
        o, a = sums(L)
        ones += o
        agree = [u + v for u, v in zip(agree, a)]
    return ones, agree, n


def merge(parts):
    ones, agree, n = 0, [0] * len(LAGS), 0
    for o, a, m in parts:
        ones += o
        agree = [u + v for u, v in zip(agree, a)]
        n += m
    return ones, agree, n


def cov(arm):
    ones, agree, n = arm
    mean = (2 * ones - n * K) / (n * K)
    return [(2 * a - n * (K - j)) / (n * (K - j)) - mean * mean for a, j in zip(agree, LAGS)]


def main():
    rings = ring_words()
    got = {w: sorted(rings.get(canon(w), [])) for w in EXPECTED_RINGS}
    report("R ring sizes as listed in the header", got == EXPECTED_RINGS,
           "; ".join(f"{w}: {got[w]}" for w in got if got[w] != EXPECTED_RINGS[w]) or "all equal")
    N = 1 << W
    floor = 0.0
    with Pool(JOBS) as pool:
        for name in OLD + P5 + P6:
            word = tuple(int(c) for c in name)
            p = len(word)
            both = merge(pool.map(both_chunk, [(word, lo, min(lo + 2048, N)) for lo in range(0, N, 2048)]))
            left = merge(pool.map(left_chunk, [(word, 7919 * p + int(name, 2) + 31 * s, N // 32) for s in range(32)]))
            if name in ("0001", "00101"):
                left2 = merge(pool.map(left_chunk, [(word, 104729 + 31 * s + int(name, 2), N // 32) for s in range(32)]))
                floor = max(floor, max(abs(u - v) for u, v in zip(cov(left), cov(left2))))
            X = [u - v for u, v in zip(cov(both), cov(left))]
            jmax = max(range(1, len(LAGS)), key=lambda i: abs(X[i])) + 1
            peak = max(abs(x) for x in X)
            ring = sorted(rings.get(canon(name), []))
            print(f"\nword {name} (p = {p}, rings {ring or 'none'}): Xc(j), j = 1..12: "
                  + " ".join(f"{x:+.3f}" for x in X), flush=True)
            if name in ("0001", "0011", "0111"):
                verdict(f"Q0 word {name}: peak still at lag 7, |Xc(7)| >= 0.05", jmax == 7 and abs(X[6]) >= 0.05,
                        f"peak lag {jmax}, Xc(7) = {X[6]:+.4f}")
            elif name == "01011":
                verdict(f"Q1 word {name}: peak at lag 5 or 10, strong", jmax in (5, 10) and abs(X[jmax - 1]) >= 0.05,
                        f"peak lag {jmax}, Xc = {X[jmax - 1]:+.4f}")
            elif name in P5 + P6:
                verdict(f"Q2 word {name}: weak at every lag (< 0.05)", peak < 0.05, f"largest |Xc| {peak:.4f} at lag "
                        f"{max(range(len(LAGS)), key=lambda i: abs(X[i])) + 1}")
            else:
                print(f"   (looked at before) peak lag {jmax}, largest |Xc| {peak:.4f}")
    report("C noise floor: two left-alone samples agree within 0.005 in Xc", floor <= 0.005, f"largest gap {floor:.4f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
