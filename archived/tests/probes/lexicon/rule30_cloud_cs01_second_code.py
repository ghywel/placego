#!/usr/bin/env python3
"""Cloud CL776/CL777: a second code for JOB CS-01 (rule30_cloud_coin_shape.py, 8.114).

The single seed's centre column c(t), t < N = 2^LOGN, with x = 2c - 1, summed at prime times and against Liouville's
and Moebius's functions, each divided by the square root of its number of terms, exactly as the first probe defines
them.  The generator is the one in ../cloud_centre_spectrum_kernels.py (bit-parallel, shrinking cone); the sieve is
vectorised.  The prediction is CS-01's own, written on 15 October in the first probe's header.
Usage: rule30_cloud_cs01_second_code.py [LOGN=24]
"""
import importlib.util, pathlib, sys, time
import numpy as np

here = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("spk", here.parent / "cloud_centre_spectrum_kernels.py")
spk = importlib.util.module_from_spec(spec); spec.loader.exec_module(spk)


def sieve(n):
    """primes mask, Liouville lambda, Moebius mu for 0..n-1 (lambda(0) = mu(0) = 0)."""
    comp = np.zeros(n, dtype=bool); comp[:2] = True
    for p in range(2, int(n ** 0.5) + 1):
        if not comp[p]:
            comp[p * p::p] = True
    primes = np.flatnonzero(~comp)
    big = np.zeros(n, dtype=np.int8)       # Omega mod 2 accumulates in int8 (max Omega < 25)
    sq = np.zeros(n, dtype=bool)           # divisible by a square of a prime
    for p in primes.tolist():
        q = p
        while q < n:
            big[q::q] += 1
            q *= p
        if p * p < n:
            sq[p * p::p * p] = True
    lam = np.where(big % 2 == 0, 1, -1).astype(np.int64); lam[0] = 0
    small = np.zeros(n, dtype=np.int8)     # number of distinct prime factors
    for p in primes.tolist():
        small[p::p] += 1
    mu = np.where(small % 2 == 0, 1, -1).astype(np.int64); mu[sq] = 0; mu[0] = 0
    return ~comp, lam, mu


def sums(bits, pm, lam, mu):
    x = 2 * bits.astype(np.int64) - 1
    out = []
    for S, n_terms in ((x[pm].sum(), int(pm.sum())), ((x * lam).sum(), int((lam != 0).sum())), ((x * mu).sum(), int((mu != 0).sum()))):
        out.append((int(S), n_terms, S / n_terms ** 0.5))
    return out


def main():
    logn = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    N = 1 << logn
    t0 = time.time()
    bits = spk.generate(N)
    print("N = 2^%d; generator control (A051023): %s; density %.5f; %.0f s" % (logn, bits[:50].tolist() == spk.A051023, bits.mean(), time.time() - t0))
    pm, lam, mu = sieve(N)
    # sieve controls on small numbers
    ref_mu = [0, 1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0, -1, 1, 1, 0, -1, 0, -1, 0]
    ref_lam = [0, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1]
    print("sieve controls: mu(0..20) %s, lambda(0..20) %s, primes below 2^20: %d (82025 expected)"
          % (mu[:21].tolist() == ref_mu, lam[:21].tolist() == ref_lam, int(pm[:1 << 20].sum())))
    names = ("S_p (x at prime times)", "S_lambda (x . Liouville)", "S_mu (x . Moebius)")
    for label, lo, hi in (("whole run", 0, N), ("first 2^22", 0, 1 << 22), ("fresh part 2^22..2^%d" % logn, 1 << 22, N)):
        if hi > N or lo >= hi:
            continue
        print(label + ":")
        for name, (S, n, z) in zip(names, sums(bits[lo:hi], pm[lo:hi], lam[lo:hi], mu[lo:hi])):
            print("  %-26s S = %9d over %8d terms; S/sigma = %+.2f" % (name, S, n, z))
    rng = np.random.default_rng(20261111)
    worst = 0.0; zs = []
    for _ in range(20):
        coin = rng.integers(0, 2, size=N, dtype=np.uint8)
        r = sums(coin, pm, lam, mu)
        worst = max(worst, max(abs(z) for _, _, z in r)); zs.append([round(z, 2) for _, _, z in r])
    print("coins: largest |S/sigma| over 20 coins x 3 sums = %.2f" % worst)
    print("density of c at prime times %.5f against overall %.5f" % (bits[pm].mean(), bits.mean()))
    print("seconds %.0f" % (time.time() - t0))


if __name__ == "__main__":
    main()
