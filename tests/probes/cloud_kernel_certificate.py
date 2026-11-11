#!/usr/bin/env python3
"""Cloud CL778, item K: the kernel counts of CL777 as a finite certificate under GPT's lemma GC487.

Lemma (GPT, GC487, 8 October 2026).  Let a(n) be a sequence and b a base.  A deterministic finite automaton with
output that reads the canonical base-b digits of n from the least significant end and returns a(n) has at least as
many states as there are pairwise different decimations n -> a(b^d n + r), 0 <= r < b^d, compared at positive n.
(After reading the d low digits of r the state fixes the output for every positive continuation n.)

For the centre column c of rule 30 from one cell, on its first N = 2^22 ticks, this probe finds for b = 2, 3, 5, 7
  * the largest depth D at which ALL (b^(D+1) - 1)/(b - 1) decimations of depth at most D are pairwise different on
    the common positive indices n = 1..L, L = N / b^D - 1 (so that every index b^d n + r lies inside the trace),
  * the least W such that they are already pairwise different on n = 1..W: the certificate is (trace digest, D, W),
  * the best count of pairwise different decimations at any depth (deeper levels have shorter samples).
Controls: the Thue-Morse sequence must give exactly 2; a pseudo-random coin must reach the same depths, since the
depth reached is set by the sample length alone (the birthday estimate), not by the sequence.

Scope, as GC487 says: this is a statement about the first 2^22 ticks.  A sequence equal to c there and zero
afterwards is automatic, so no finite sample can prove that the kernel is infinite.
Prediction (CL778, before the run): D = 16, 10, 7, 6 (base 7 may stop at 5).
Usage: cloud_kernel_certificate.py [SECOND_TRACE_FILE]   (a second trace, one byte per tick, to compare with)
"""
import hashlib, importlib.util, pathlib, sys
import numpy as np

here = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("spk", here / "cloud_centre_spectrum_kernels.py")
spk = importlib.util.module_from_spec(spec); spec.loader.exec_module(spk)
N = 1 << 22


def signatures(c, b, D, L):
    """Rows: every decimation (d, r), d <= D; columns: n = 1..L."""
    n = np.arange(1, L + 1, dtype=np.int64)
    rows = []
    for d in range(D + 1):
        q = b ** d
        r = np.arange(q, dtype=np.int64)
        rows.append(c[q * n[None, :] + r[:, None]])
    return np.concatenate(rows, axis=0)


def distinct(S):
    P = np.packbits(S, axis=1)
    v = np.ascontiguousarray(P).view(np.dtype((np.void, P.shape[1])))
    return len(np.unique(v))


def report(name, c, b):
    best = (0, 0, 0); full = None
    D = 0
    while True:
        L = len(c) // b ** D - 1
        if L < 1:
            break
        M = (b ** (D + 1) - 1) // (b - 1)
        S = signatures(c, b, D, L)
        k = distinct(S)
        if k == M:
            W = next(w for w in range(1, L + 1) if distinct(S[:, :w]) == M)
            full = (D, M, L, W)
        if k > best[0]:
            best = (k, D, L)
        if k < M and L < 8:
            break
        D += 1
    D, M, L, W = full
    print(f"   {name}, base {b}: all {M} decimations to depth {D} are pairwise different on n = 1..{L}; already on n = 1..{W}"
          f" | best count at any depth: {best[0]} (depth {best[1]}, n = 1..{best[2]})")
    return D, M, W, best[0]


def main():
    c = spk.generate(N)
    print("== the trace")
    print(f"   {N} ticks from the bit-packed generator; first 50 equal A051023: {c[:50].tolist() == spk.A051023}; density {c.mean():.5f}")
    print(f"   SHA-256 of the trace (one byte per tick): {hashlib.sha256(c.tobytes()).hexdigest()}")
    if len(sys.argv) > 1:
        other = np.fromfile(sys.argv[1], dtype=np.uint8)
        m = min(len(other), N)
        print(f"   second generator (the integer lift's byte code at modulus 2): first {m} ticks identical: {bool((other[:m] == c[:m]).all())}")
    print("== controls")
    n = np.arange(N, dtype=np.int64)
    tm = np.zeros(N, dtype=np.uint8); x = n.copy()
    while x.any():
        tm ^= (x & 1).astype(np.uint8); x >>= 1
    S = signatures(tm, 2, 8, N // 256 - 1)
    print(f"   Thue-Morse, base 2, depth 8: {distinct(S)} different decimations among {S.shape[0]} (2 expected)")
    rng = np.random.default_rng(20261111)
    coin = rng.integers(0, 2, size=N, dtype=np.uint8)
    cres = {b: report("pseudo-random coin", coin, b) for b in (2, 3, 5, 7)}
    print("== the centre column of rule 30")
    res = {b: report("rule 30 centre column", c, b) for b in (2, 3, 5, 7)}
    print("K: depths reached by rule 30:", {b: res[b][0] for b in res}, "| by the coin:", {b: cres[b][0] for b in cres})
    print("K: lower bounds on the states of a least-significant-digit-first automaton for the first 2^22 ticks (all decimations different):",
          {b: res[b][1] for b in res}, "| best counts:", {b: res[b][3] for b in res})


if __name__ == "__main__":
    main()
