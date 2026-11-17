#!/usr/bin/env python3
"""Prime-power (and composite) extension of the volume lemma.
Relation on Z[i]/M (residues a+bi, a,b mod M): x ~ y iff M | N(x-y). Cayley: U = {d : M | N(d)}.
Bicliques via closures: Q = N(S) = intersection of (s+U), P = N(Q) = {x : (1_Q * 1_{U^c})(x) = 0} (cyclic FFT conv),
then Q' = N(P). Seeds S = {0} and {0,s} for all s (translation invariance), plus random triples.
Claim under test: max |P||Q| = M^2 (single ideal coset), for M = 25, 125, 169, 325."""
import sys, time, math
import numpy as np
T0 = time.time(); TLIM = 300.0
def run(M, all_pairs=True, npairs=3000, ntriples=2000):
    a = np.arange(M)
    A, B = np.meshgrid(a, a, indexing='ij')
    U = ((A * A + B * B) % M == 0)            # d = A + Bi in U iff M | N(d)
    Uc = (~U).astype(float)
    FUc = np.fft.fft2(Uc)
    def nbhd(S):                              # N(S) = {x : x - s in U for all s in S}
        out = np.ones((M, M), bool)
        for (s1, s2) in S:
            out &= np.roll(np.roll(U, s1, 0), s2, 1)
        return out
    def nbhd_big(Qm):                         # N(Q) via FFT: x in N(Q) iff sum_q Uc(x - q) = 0
        c = np.real(np.fft.ifft2(np.fft.fft2(Qm.astype(float)) * FUc))
        return c < 0.5
    best = (0, None); seen = 0
    rng = np.random.default_rng(1)
    seeds = [((0, 0),)]
    if all_pairs:
        seeds += [((0, 0), (i, j)) for i in range(M) for j in range(M) if (i, j) != (0, 0)]
    else:
        seeds += [((0, 0), tuple(rng.integers(0, M, 2))) for _ in range(npairs)]
    seeds += [((0, 0), tuple(rng.integers(0, M, 2)), tuple(rng.integers(0, M, 2))) for _ in range(ntriples)]
    for S in seeds:
        if time.time() - T0 > TLIM: print('  TIME LIMIT'); break
        Q = nbhd(S)
        P = nbhd_big(Q)
        Q2 = nbhd_big(P)
        v = int(P.sum()) * int(Q2.sum()); seen += 1
        if v > best[0]: best = (v, (int(P.sum()), int(Q2.sum())))
    print(f'M={M}: closures={seen} max volume={best[0]} sizes={best[1]}  M^2={M*M}  |U|={int(U.sum())}', flush=True)
for M, ap in [(25, True), (125, True), (169, False), (325, False)]:
    run(M, ap)
print('time', round(time.time() - T0, 1))
