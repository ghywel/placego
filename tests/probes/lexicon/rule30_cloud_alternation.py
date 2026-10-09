#!/usr/bin/env python3
"""rule30_cloud_alternation.py: the arpeggio-staccato alternation the owner heard, as an exact law of Rule 30's rows.

RUN-ON:     cpu (Python 3 standard library; bit-sliced big integers)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_alternation.py [KMAX=12]
COST:       about 10 s at KMAX = 12 (the exact part doubles its cost with each further lag).
Exploratory: the exact part is a finite calculation, not a measurement, and the Monte Carlo part only checks it on
random rows. No prediction was pushed before either, and none is needed for an exact count. The measurement on the
single seed is left for a worker, with its predictions pushed first in CL078. Cloud, 2026-10-09, from the owner's
remark on the necklace page's music box: "the sequence runs staccato arpeggio staccato arpeggio repeat ... looking for
sequences that fall into the form of alternative staccato arpeggio for some N>2 times might reveal interesting
structures".

The law. Rule 30 is x_(t+1)(i) = x_t(i-1) xor (x_t(i) or x_t(i+1)), so k steps give x_(t+k)(i) = x_t(i-k) xor g_k, where
g_k does not depend on x_t(i-k) (left permutivity). Take a fair row (independent fair cells, which Rule 30 preserves on
the line). For any d other than -k, x_(t+k)(i) xor x_t(i+d) still contains x_t(i-k) once, so it is a fair bit and the
covariance is zero. So the correlation between the density of a window of width w in row t and in row t+k is, up to
edge terms of order k/w (exactly a factor max(w - k, 0)/w, zero for k >= w, where the window loses the
diagonal's partner; added after GPT's GC776, G.GPT255),
    rho_k = E (-1)^(g_k) = E (-1)^(x_(t+k)(i) xor x_t(i-k)),
the correlation between a cell and the cell k steps down the rightward light-speed diagonal. At k = 1 it is the OR
term, -1/2 (RULE30-PRIZE.md §8.70's frame at light speed sees change three times in four). A dense row (an arpeggio)
is followed by a sparse one (staccato) because each cell is the opposite of its upper-left neighbour three times in
four. The pair statistic (adjacent black cells, the arpeggio's runs) is computed exactly too, without the collapse.

OUTCOME of the first run, 2026-10-09 (KMAX = 12, 6 s in the cloud container). The edge-term comparison
was added after the first run, and the probe rerun.
  Window density, exact: rho_1 .. rho_12 = -1/2, 1/4, -1/4, 5/32, -5/64, 77/1024, -141/2048, 39/512, -3273/65536,
    2785/131072, -21759/1048576, 27905/2097152. The sign alternates at every lag computed, and the size falls from 1/2
    to 0.013, not monotonically (0.078, 0.075, 0.069, 0.076 at k = 5 to 8). The collapse holds at every lag: every
    covariance term but d = -k is exactly 0.
  Pair statistic, exact (k = 1 .. 7): -1/2, 11/40, -29/160, 87/640, -153/2560, 747/10240, -2919/40960, the same signs.
  Monte Carlo on random fair rows (2^19 cells, windows of 63, 24 rows): rho_1 .. rho_6 measure -0.495, +0.242,
    -0.238, +0.148, -0.073, +0.068. The first comparison, against rho_k itself, missed by up to 0.012 in the same
    direction every time. That is the edge term: only (w - k)/w of a window's cells have their upper-left partner
    k rows up inside the same window. Against rho_k (w - k)/w the largest gap is 0.0025. A window flips between
    denser and sparser than half at 0.668 of steps (2/3 for a Gaussian at correlation -1/2; 1/2 for no correlation).
    N flips in a row: 0.668, 0.459, 0.328, 0.236, 0.168, 0.120, 0.087, 0.063 for N = 1 .. 8, against 2^-N. Eight in
    a row is 16 times commoner than for uncorrelated rows: alternation is Rule 30's default rhythm, not a rare form.
  The unexpected check: the necklace's whole 84-cell ring has 43 black cells at every beat (each step is a pure
    rotation), so its alternation lives only in the comb's 14-cell window (9, 6, 8, 7, 8, 5), which reads the ring
    word's six 14-bead segments in turn. That is why a bar has 43 plucks: the comb reads the whole ring once.
  Not proved: that the sign alternates at every lag, or that rho_k tends to 0.
"""
import random
import sys
from fractions import Fraction as F

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 12


def var_masks(n):
    """Bit j of word w, for every word w of n bits, as one big integer (bit w of mask j)."""
    M, masks = 1 << n, []
    for j in range(n):
        rep, span = ((1 << (1 << j)) - 1) << (1 << j), 1 << (j + 1)
        while span < M:
            rep |= rep << span
            span <<= 1
        masks.append(rep & ((1 << M) - 1))
    return masks


def evolve(rows, k):
    for _ in range(k):
        rows = [rows[i - 1] ^ (rows[i] | rows[i + 1]) for i in range(1, len(rows) - 1)]
    return rows


def ones(v):
    return bin(v).count("1")


def density_terms(k):
    """The terms 4 cov(x_(t+k)(0), x_t(d)) for d = -k .. k, exactly."""
    n = 2 * k + 1
    x = var_masks(n)
    y = evolve(x, k)[0]
    return [F(4 * ones(y & xd), 1 << n) - 1 for xd in x]


def pair_corr(k):
    """Correlation of the window counts of adjacent black pairs, k rows apart (per-cell variance 5/16 in each row)."""
    n = 2 * k + 4
    x = var_masks(n)
    y = evolve(x, k)
    q = y[1] & y[2]
    return sum(F(ones(q & x[d] & x[d + 1]), 1 << n) - F(1, 16) for d in range(n - 1)) / F(5, 16)


def monte_carlo(L=1 << 19, T=24, w=63, seed=30):
    rnd = random.Random(seed)
    V = rnd.getrandbits(L + 2 * T)
    lo, hi = T, L + T
    starts = list(range(lo, hi - w + 1, w))
    dens = []
    for _ in range(T + 1):
        dens.append([ones((V >> s) & ((1 << w) - 1)) for s in starts])
        V = ((V << 1) ^ (V | (V >> 1))) & ((1 << (L + 2 * T)) - 1)
    m, var = w / 2, w / 4
    rho = []
    for k in range(1, 7):
        c = [(dens[t][j] - m) * (dens[t + k][j] - m) for t in range(T + 1 - k) for j in range(len(starts))]
        rho.append(sum(c) / len(c) / var)
    side = [[d > m for d in row] for row in dens]
    flips = [[side[t][j] != side[t + 1][j] for j in range(len(starts))] for t in range(T)]
    rate = sum(map(sum, flips)) / (T * len(starts))
    streak = []
    for N in range(1, 9):
        hits = sum(all(flips[t + u][j] for u in range(N)) for t in range(T - N + 1) for j in range(len(starts)))
        streak.append(hits / ((T - N + 1) * len(starts)))
    return rho, rate, streak


def necklace():
    N, word = 84, int("688eb74a45efb082671ee", 16)
    r = [(word >> i) & 1 for i in range(N)]
    whole, comb = [], []
    for _ in range(6):
        whole.append(sum(r))
        comb.append(sum(r[:14]))
        r = [r[i - 1] ^ (r[i] | r[(i + 1) % N]) for i in range(N)]
    return whole, comb


def main():
    print("window density: rho_k = correlation of a window's density k rows apart, exact under fair rows")
    exact = []
    for k in range(1, KMAX + 1):
        terms = density_terms(k)
        assert all(v == 0 for v in terms[1:]), f"collapse fails at k = {k}"
        exact.append(terms[0])
        print(f"  k = {k:2d}: rho = {str(terms[0]):>14s} = {float(terms[0]):+.5f}   (every term but d = -k is 0)")
    print("adjacent black pairs: correlation of window counts k rows apart, exact")
    for k in range(1, min(KMAX, 7) + 1):
        c = pair_corr(k)
        print(f"  k = {k:2d}: {str(c):>14s} = {float(c):+.5f}")
    rho, rate, streak = monte_carlo()
    print("Monte Carlo, random fair rows, windows of 63 cells:")
    print("  rho_1 .. rho_6 measured:", " ".join(f"{v:+.3f}" for v in rho))
    edge = [float(b) * (63 - k) / 63 for k, b in enumerate(exact[:6], 1)]
    print("  exact, with the edge term (w - k)/w:", " ".join(f"{v:+.3f}" for v in edge))
    print("  largest gap to them:", f"{max(abs(a - b) for a, b in zip(rho, edge)):.4f}")
    print(f"  fraction of steps that flip denser/sparser than half: {rate:.3f}"
          " (2/3 Gaussian at -1/2; 1/2 uncorrelated)")
    for N, s in enumerate(streak, 1):
        print(f"  N = {N} flips in a row: {s:.4f}   (uncorrelated rows: {2 ** -N:.4f})")
    whole, comb = necklace()
    print("necklace: whole-ring black count per beat", whole, "; the comb's 14 sites per beat", comb)


if __name__ == "__main__":
    main()
