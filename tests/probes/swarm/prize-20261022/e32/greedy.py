"""Greedy additive complements on a window.

For a set Q (primes, or a random model of the primes) and a window W = [M, 2M), find by (lazy) greedy set cover a
set A of shifts a in [1, 2M) such that every n in W has n - a in Q for some a in A.  Report |A| = g(M).

Usage: python3 greedy.py KIND SEED M1 M2 ...   KIND in {primes, cramer, granville}
Time limit: 540 s wall for the whole run (checked between steps).
"""
import sys, time, math
import numpy as np

T0 = time.time()
TLIM = 540.0

def sieve(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = False
    return s

def model_set(L, kind, rng):
    """Indicator array of length L for the set Q (only entries >= 2 can be 1)."""
    m = np.arange(L, dtype=np.float64)
    if kind == 'primes':
        return sieve(L - 1)
    q = np.zeros(L, dtype=bool)
    if kind == 'cramer':
        prob = np.zeros(L); prob[3:] = 1.0 / np.log(m[3:]); prob[2] = 1.0
        q = rng.random(L) < prob
        return q
    if kind in ('granville', 'granville13'):
        # random among integers coprime to P(z), z = 5 (keeps parity and mod-3, mod-5 structure) or z = 13,
        # with probability kappa / log m, kappa = prod p/(p-1); the primes <= z are put in.
        z_primes = [2, 3, 5] if kind == 'granville' else [2, 3, 5, 7, 11, 13]
        kappa = 1.0
        cop = np.ones(L, dtype=bool)
        for p in z_primes:
            kappa *= p / (p - 1.0)
            cop[::p] = False
        prob = np.zeros(L); prob[3:] = np.minimum(1.0, kappa / np.log(m[3:]))
        q = cop & (rng.random(L) < prob)
        for p in z_primes:
            q[p] = True
        q[:2] = False
        return q
    raise ValueError(kind)

def greedy_cover(M, Qind):
    L = 1
    while L < 4 * M:
        L *= 2
    U = np.zeros(L, dtype=np.float64); U[M:2 * M] = 1.0
    Qa = np.zeros(L, dtype=np.float64)
    qs = np.nonzero(Qind[:2 * M])[0]
    qs = qs[qs >= 2]
    Qa[qs] = 1.0
    FQ = np.conj(np.fft.rfft(Qa))
    def all_counts():
        c = np.fft.irfft(np.fft.rfft(U) * FQ, L)[:2 * M]
        c = np.rint(c); c[0] = -1.0  # a >= 1
        return c
    Ub = U.astype(bool)
    stale = all_counts()
    A = []
    unc = int(Ub.sum())
    recomputes = 0
    K = min(2048, 2 * M - 2)
    while unc > 0:
        if time.time() - T0 > TLIM:
            return None, A
        # candidate pool: top K stale
        top = np.argpartition(-stale, K)[:K]
        thr = np.partition(-stale, K)[K] * -1.0  # (K+1)-th largest stale value: bound for all others
        top = top[np.argsort(-stale[top])]
        best_a, best_c = -1, -1
        # lazy evaluation inside the pool
        pool = {int(a): stale[a] for a in top}
        while True:
            a = max(pool, key=pool.get)
            sc = pool[a]
            if sc <= best_c:
                break
            tc = int(Ub[a + qs].sum()); recomputes += 1
            stale[a] = tc; pool[a] = tc
            if tc > best_c:
                best_a, best_c = a, tc
        if best_c < thr:
            # bound outside the pool may exceed: refresh everything by FFT
            U[:] = Ub
            stale = all_counts()
            continue
        A.append(best_a)
        idx = best_a + qs
        Ub[idx] = False
        unc -= best_c
        stale[best_a] = 0
    return A, A

def main():
    kind = sys.argv[1]; seed = int(sys.argv[2])
    rng = np.random.default_rng(seed)
    Ms = [int(x) for x in sys.argv[3:]]
    Lmax = 1
    while Lmax < 4 * max(Ms):
        Lmax *= 2
    Qind = model_set(Lmax, kind, rng)
    for M in Ms:
        t = time.time()
        res, A = greedy_cover(M, Qind)
        lm = math.log(M)
        if res is None:
            print(f"{kind} seed={seed} M={M} TIMEOUT partial={len(A)}", flush=True)
            break
        g = len(res)
        # control: independent check that A covers the window
        cov = np.zeros(2 * M, dtype=bool)
        qs = np.nonzero(Qind[:2 * M])[0]; qs = qs[qs >= 2]
        for a in res:
            idx = a + qs; idx = idx[idx < 2 * M]; cov[idx] = True
        assert cov[M:2 * M].all(), 'cover check failed'
        print(f"{kind} seed={seed} M={M} lnM={lm:.3f} g={g} g/lnM={g/lm:.3f} g/lnM^2={g/lm**2:.4f} "
              f"t={time.time()-t:.1f}s", flush=True)

if __name__ == '__main__':
    main()
