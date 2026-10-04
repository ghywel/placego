#!/usr/bin/env python3
"""rule30_spectrum_fine.py: column 1's dominant spectral line for trace 0101..., pinned with long sequences; and which
ring orbits have a 0101... column at all.

RUN-ON:     cpu (pure Python 3, standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_spectrum_fine.py [T=4096] [SAMPLES=200] [NMAX=18]
COST:       a few minutes on one core.

A measurement, not a prediction: rule30_spectrum.py (section 8.3) found column 1's highest spike for trace 0101...
at about 0.303 at T = 512, and a second one at 0.197; the two add to 1/2, which is what multiplying a signal by the
alternating trace does (f -> 1/2 - f). Here the line is located on a fine grid (step 0.00005) from 200 seeded random
right halves of 14 cells over T = 4096 steps, by the same Wiener-Khinchin estimate with M = T/4 lags; the strongest
autocovariance lags are listed; and every Rule 30 orbit on rings of 2 to NMAX cells is searched for a column with the
word 01 (to see whether the line could be a ring orbit's).

The control is that the same estimate on a planted line (a sequence with a 1 wherever the fractional part of
0.30357 t is below 0.3, with 10% of its bits flipped) puts the peak within 0.0002 of 0.30357.
"""
import math, random, sys, pathlib

T = int(sys.argv[1]) if len(sys.argv) > 1 else 4096
SAMPLES = int(sys.argv[2]) if len(sys.argv) > 2 else 200
NMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 18
M = T // 4

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_twosided as ts                           # noqa: E402
sys.argv = _argv
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def autocov(seqs):
    agree, ones, N = [0] * (M + 1), 0, len(seqs)
    for b in seqs:
        x = sum(v << k for k, v in enumerate(b))
        ones += bin(x).count("1")
        for j in range(M + 1):
            agree[j] += T - j - bin((x ^ (x >> j)) & ((1 << (T - j)) - 1)).count("1")
    mean = (2 * ones - N * T) / (N * T)
    return [(2 * a - N * (T - j)) / (N * (T - j)) - mean * mean for j, a in enumerate(agree)]


def S(C, f):
    return C[0] + 2 * sum((1 + math.cos(math.pi * j / (M + 1))) / 2 * C[j] * math.cos(2 * math.pi * f * j)
                          for j in range(1, M + 1))


def peak(C, lo, hi, n=300):
    grid = [lo + (hi - lo) * i / n for i in range(n + 1)]
    vals = [S(C, f) for f in grid]
    i = max(range(n + 1), key=lambda i: vals[i])
    return grid[i], vals[i]


def ring_01_columns(nmax):
    out = {}
    for n in range(2, nmax + 1):
        m = (1 << n) - 1
        visited = set()
        for x0 in range(1 << n):
            if x0 in visited:
                continue
            path, pos, x = [], {}, x0
            while x not in pos and x not in visited:
                pos[x] = len(path)
                path.append(x)
                x = (((x << 1) | (x >> (n - 1))) & m) ^ (x | (((x >> 1) | (x << (n - 1))) & m))
            visited.update(path)
            if x in pos:
                cyc = path[pos[x]:]
                for i in range(n):
                    w = [(s >> i) & 1 for s in cyc]
                    if len(cyc) % 2 == 0 and all(w[t] != w[t + 1] for t in range(len(cyc) - 1)) and w[0] != w[-1]:
                        out.setdefault(n, set()).add(len(cyc))
    return out


def main():
    rng = random.Random(41)
    planted = [[int(((0.30357 * t) % 1.0) < 0.3) ^ (rng.random() < 0.1) for t in range(T)] for _ in range(40)]
    f, _ = peak(autocov(planted), 0.295, 0.310)
    report("control: a planted line at 0.30357 is found within 0.0002", abs(f - 0.30357) <= 0.0002, f"found {f:.5f}")
    rng = random.Random(5)
    seqs = [ts.column1(rng.getrandbits(14), (0, 1), T) for _ in range(SAMPLES)]
    C = autocov(seqs)
    for lo, hi in [(0.295, 0.310), (0.190, 0.205)]:
        f, s = peak(C, lo, hi)
        print(f"   column 1, trace 0101..., T = {T}: peak in [{lo}, {hi}] at f = {f:.5f}, S = {s:.2f}")
    top = sorted(range(1, M + 1), key=lambda j: -abs(C[j]))[:12]
    print("   strongest autocovariance lags: " + ", ".join(f"{j} ({C[j]:+.3f})" for j in top))
    print("   candidates: 3/10 = 0.30000, 17/56 = 0.30357, 7/23 = 0.30435, 4/13 = 0.30769")
    rings = ring_01_columns(NMAX)
    print(f"   rings of 2..{NMAX} cells with an orbit holding a 0101... column (ring size: cycle lengths): "
          + (", ".join(f"{n}: {sorted(v)}" for n, v in sorted(rings.items())) or "none"))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
