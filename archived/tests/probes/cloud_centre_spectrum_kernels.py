#!/usr/bin/env python3
"""Cloud CL776/CL777: two observers the record had not pointed at the single-seed centre column.

N2a  power spectrum of the centre column (2^22 ticks): a fixed period of any length, prime or not, would be a line.
N2b  kernel sequences c(k^e n + r) in bases k = 2, 3, 5, 7: an automaton reading the tick in base k ("a code computed
     from a counter") would have only finitely many of them.
Predictions: CHAT-LEDGER CL776 addendum 2.  Both are calibrating observers: they cannot prove anything about the column.
Usage: cloud_centre_spectrum_kernels.py [LOGN=22]
"""
import math, pathlib, subprocess, sys, tempfile, itertools
import numpy as np

GEN_C = r'''
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc, char **argv) {
    long N = atol(argv[1]);
    long W = (2 * N + 64) / 64 + 2;
    uint64_t *a = calloc(W, 8), *b = calloc(W, 8);
    unsigned char *out = malloc(N);
    long c = N;
    a[c / 64] |= 1ull << (c % 64);
    for (long t = 0; t < N; t++) {
        out[t] = (a[c / 64] >> (c % 64)) & 1;
        long r = t + 1 < N - 1 - t ? t + 1 : N - 1 - t;
        if (r < 0) break;
        long lo = (c - r - 1) / 64 - 1, hi = (c + r + 1) / 64 + 1;
        if (lo < 1) lo = 1; if (hi > W - 2) hi = W - 2;
        for (long i = lo; i <= hi; i++) {
            uint64_t x = a[i];
            uint64_t left = (x << 1) | (a[i - 1] >> 63);
            uint64_t right = (x >> 1) | (a[i + 1] << 63);
            b[i] = left ^ (x | right);
        }
        b[lo - 1] = 0; b[hi + 1] = 0;
        uint64_t *tmp = a; a = b; b = tmp;
    }
    fwrite(out, 1, N, stdout);
    return 0;
}
'''
A051023 = [1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0]


def generate(n):
    d = pathlib.Path(tempfile.mkdtemp(prefix="centre-"))
    (d / "gen.c").write_text(GEN_C)
    subprocess.run(["cc", "-O3", "-o", str(d / "gen"), str(d / "gen.c")], check=True)
    out = subprocess.run([str(d / "gen"), str(n)], capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype=np.uint8)


def spectrum_report(name, c):
    N = len(c)
    x = 1.0 - 2.0 * c.astype(np.float64)
    P = np.abs(np.fft.rfft(x)) ** 2 / N
    P = P[1:N // 2]                                   # frequencies 1 .. N/2 - 1
    M = float(P.max()); k = int(P.argmax()) + 1
    tail = [float((P > th).mean()) for th in (1, 2, 4, 8)]
    print(f"   {name}: mean power {P.mean():.4f} | largest {M:.2f} at frequency {k}/{N} (period {N / k:.3f}) | "
          f"share above 1, 2, 4, 8: {[round(v, 5) for v in tail]} (coin: {[round(math.exp(-th), 5) for th in (1, 2, 4, 8)]})")
    return M


def kernel_report(name, c, k, E):
    N = len(c); L = N // k ** E
    seqs = []; labels = []
    for e in range(0, E + 1):
        for r in range(k ** e):
            seqs.append(c[r::k ** e][:L]); labels.append((e, r))
    S = np.array(seqs, dtype=np.uint8)
    packed = np.packbits(S, axis=1)
    distinct = len({row.tobytes() for row in packed})
    # least pairwise disagreement, by a Gram matrix on +-1 values
    X = 1.0 - 2.0 * S.astype(np.float32)
    G = X @ X.T
    np.fill_diagonal(G, -L)
    worst = float(G.max()); i, j = np.unravel_index(int(G.argmax()), G.shape)
    least = (L - worst) / (2 * L)
    print(f"   {name} base {k}, depth {E}: {len(seqs)} kernel sequences of {L} bits | distinct {distinct} | "
          f"least pairwise disagreement {least:.4f} between {labels[i]} and {labels[j]} "
          f"(a coin's sd per pair: {0.5 / math.sqrt(L):.4f}; pairs {len(seqs) * (len(seqs) - 1) // 2})")
    return distinct == len(seqs), least


def main():
    logn = int(sys.argv[1]) if len(sys.argv) > 1 else 22
    N = 1 << logn
    c = generate(N)
    print("control: first 50 bits equal A051023:", c[:50].tolist() == A051023, "| density", round(float(c.mean()), 5))
    rng = np.random.default_rng(20261111)
    coins = [rng.integers(0, 2, size=N, dtype=np.uint8) for _ in range(3)]
    tm = np.array([bin(n).count("1") & 1 for n in range(1 << 16)], dtype=np.uint8)
    print("== N2a power spectrum (power scaled to mean 1)")
    lo, hi = math.log(N / 2) - 1.93, math.log(N / 2) + 6.9
    M = spectrum_report("rule 30 centre", c)
    for i, co in enumerate(coins):
        spectrum_report(f"coin {i}", co)
    planted = c.copy(); planted[::1009] = 1                 # control: a line of prime period 1009
    Mp = spectrum_report("control: every 1009th tick forced black", planted)
    print(f"   prediction window for the largest value: {lo:.2f} to {hi:.2f} | rule 30 inside: {lo < M < hi} | "
          f"the planted prime period stands out: {Mp > hi}")
    print("== N2b kernel sequences")
    ok = True
    for k, E in ((2, 8), (3, 5), (5, 3), (7, 3)):
        a, least = kernel_report("rule 30 centre", c, k, E); ok &= a and least > 0.46
    kernel_report("coin 0", coins[0], 3, 5)
    L = len(tm) // 2 ** 6
    seqs = {tm[r::2 ** e][:L].tobytes() for e in range(7) for r in range(2 ** e)}
    print(f"   control: Thue-Morse, base 2, depth 6: {sum(2 ** e for e in range(7))} kernel sequences, distinct {len(seqs)}")
    print("N2b verdict (all distinct and least disagreement above 0.46 in every base):", ok)


if __name__ == "__main__":
    main()
