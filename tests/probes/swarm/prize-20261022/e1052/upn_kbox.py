#!/usr/bin/env python3
"""Complete box search for unitary perfect numbers N = 2^a * prod p^e with every odd component p^e <= B.

Method: seed-driven factor-chain closure. By the seed-reachability lemma (REPORT.md section 4) every odd prime
of N is reachable from 2^a+1, so the closure misses nothing.  Branching only on exponents.
Usage: upn_box.py B [time_limit_seconds]
"""
import sys, time, math
import numpy as np

T0 = time.time()
B = int(sys.argv[1])
KK = int(sys.argv[2])
TLIM = float(sys.argv[3]) if len(sys.argv) > 3 else 540.0
sys.setrecursionlimit(100000)

def elapsed():
    return time.time() - T0

class Timeout(Exception):
    pass

# ---------- smallest-prime-factor sieve up to B+1 ----------
NMAX = B + 2
spf = np.arange(NMAX + 1, dtype=np.int64 if NMAX > 2**31 - 1 else np.int32)
for i in range(2, math.isqrt(NMAX) + 1):
    if spf[i] == i:
        sl = spf[i * i::i]
        np.minimum(sl, i, out=sl)
spf_l = spf  # numpy array

def factor_small(n):
    """factor n <= NMAX via spf; returns dict"""
    f = {}
    while n > 1:
        p = int(spf_l[n])
        c = 0
        while n % p == 0:
            n //= p
            c += 1
        f[p] = c
    return f

_pl = []
_CH = 1 << 22
for _lo in range(2, NMAX + 1, _CH):
    _hi = min(NMAX + 1, _lo + _CH)
    _idx = np.flatnonzero(spf[_lo:_hi] == np.arange(_lo, _hi, dtype=spf.dtype)) + _lo
    _pl.append(_idx)
primes = np.concatenate(_pl)
primes = primes[primes <= B]
odd_primes = [int(p) for p in primes if p > 2]
print(f"[{elapsed():.1f}s] sieve done: B={B}, {len(odd_primes)} odd primes <= B", flush=True)

# ---------- seed filter: which a have 2^a+1 with all components <= B ----------
A = (B - 1) // 2  # Zsigmondy: for a != 3, 2^a+1 has a prime factor >= 2a+1
A = max(A, 3)
L = np.zeros(A + 1, dtype=np.float64)
bad = np.zeros(A + 1, dtype=bool)

def mult_order_2(p):
    t = p - 1
    for r in factor_small(p - 1):
        while t % r == 0 and pow(2, t // r, p) == 1:
            t //= r
    return t

for p in odd_primes:
    t = mult_order_2(p)
    if t % 2:
        continue
    h = t // 2
    if h > A:
        continue
    # base valuation v_p(2^h + 1)
    base = 1
    pk = p * p
    while pk <= 2 * B * B and pow(2, h, pk) == pk - 1:
        base += 1
        pk *= p
    lp = math.log(p)
    L[h::2 * h] += base * lp
    if p ** base > B:
        bad[h::2 * h] = True
    j = 1
    step = h * p
    while step <= A:
        # a = h * p^j * odd  -> extra +1 valuation (LTE, p odd, a/h odd)
        L[step::2 * step] += lp
        if p ** (base + j) > B:
            bad[step::2 * step] = True
        j += 1
        step *= p
    if elapsed() > TLIM:
        raise SystemExit("timeout in seed sieve")

cand = []
for _lo in range(0, A + 1, _CH):
    _hi = min(A + 1, _lo + _CH)
    alist = np.arange(_lo, _hi, dtype=np.float64)
    target = alist * math.log(2.0) + np.log1p(np.exp2(-np.minimum(alist, 1000)))
    cand += [int(a) + _lo for a in np.flatnonzero((L[_lo:_hi] >= target - 1e-7 * (1 + alist)) & (~bad[_lo:_hi])) if a + _lo >= 1]
    del alist, target
print(f"[{elapsed():.1f}s] seed filter: a <= {A}; candidate a with B-component-smooth 2^a+1: {cand}", flush=True)

def factor_seed(a):
    """exact factorization of 2^a+1 over primes <= B (only for candidate a)."""
    n = 2 ** a + 1
    f = {}
    for p in odd_primes:
        if p * p > n and n > 1:
            # n is prime or 1
            break
        if n % p == 0:
            c = 0
            while n % p == 0:
                n //= p
                c += 1
            f[p] = c
        if n == 1:
            break
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

# prefix products of (1+1/r) over smallest odd primes (upper bound for new primes)
pref = [1.0]
for r in odd_primes[:5000]:
    pref.append(pref[-1] * (1.0 + 1.0 / r))

def newmax_old(m):
    if m <= 0:
        return 1.0
    if m < len(pref):
        return pref[m]
    return float('inf')

LOGHALF = math.log((B + 1) / 2.0)
solutions = []
nodes = 0

_mx = {}
def maxexp(q):
    r = _mx.get(q)
    if r is None:
        e = 0
        v = 1
        while v * q <= B:
            v *= q
            e += 1
        _mx[q] = e
        r = e
    return r

_lg = {}
def lg(p):
    r = _lg.get(p)
    if r is None:
        r = math.log(p)
        _lg[p] = r
    return r

_fc = {}
def fac_plus1(q, e):
    """(v2, list of (odd prime, mult)) of q^e+1, cached"""
    k = (q, e)
    r = _fc.get(k)
    if r is None:
        f = factor_small(q ** e + 1)
        w = f.pop(2, 0)
        r = (w, tuple(f.items()))
        _fc[k] = r
    return r

def newmax_excl(m, excl):
    """product of (1+1/r) over the m smallest odd primes not in excl (upper bound for m new primes)"""
    if m <= 0:
        return 1.0
    prod = 1.0
    cnt = 0
    for r in odd_primes:
        if r in excl:
            continue
        prod *= 1.0 + 1.0 / r
        cnt += 1
        if cnt == m:
            return prod
    return float('inf')

def v2(n):
    return (n & -n).bit_length() - 1

V2K = (KK & -KK).bit_length() - 1
ODDK = KK >> V2K
VK = factor_small(ODDK) if ODDK > 1 else {}

def dfs(a, T, assigned, absent, R, used, logc):
    """sigma*(N) = KK*N.  final: R[p] = e_p + v_p(KK) for p in P; R[q] = v_q(KK) for odd q | KK not in P;
    sum v2(p^e+1) = a + v2(KK)."""
    global nodes
    nodes += 1
    if nodes % 20000 == 0 and elapsed() > TLIM:
        raise Timeout
    total = a + V2K
    U = [q for q in R if q not in assigned and q not in absent]
    Uns = [q for q in U if q not in VK]
    if used + len(Uns) > total:
        return
    D = 0.0
    for p, e in assigned.items():
        rp = R.get(p, 0)
        need = e + VK.get(p, 0)
        if rp > need:
            return
        D += (need - rp) * lg(p)
    for q in absent:
        rq = R.get(q, 0)
        if rq > VK[q]:
            return
        D += (VK[q] - rq) * lg(q)
    for q in Uns:
        if R[q] > maxexp(q):
            return
    for q in U:
        if q in VK and R[q] > VK[q] + maxexp(q):
            return
    rem = total - used
    if D > rem * LOGHALF + 1e-9:
        return
    c = math.exp(logc)
    if not U:
        if used == total and all(R.get(p, 0) == e + VK.get(p, 0) for p, e in assigned.items()) \
                and all(R.get(q, 0) == VK[q] for q in absent) \
                and all((q in assigned) or (q in absent) for q in VK):
            N = 2 ** a
            for p, e in assigned.items():
                N *= p ** e
            solutions.append((a, dict(sorted(assigned.items())), N))
        return
    if c * (1.0 + 1.0 / B) ** len(Uns) > T * (1 + 1e-12):
        return
    up = c
    for q in U:
        if q in VK:
            up *= (1.0 + q ** (-max(1, R[q] - VK[q])))
        else:
            up *= (1.0 + q ** (-R[q]))
    excl = assigned.keys() | set(U) | set(absent)
    if up * newmax_excl(rem - len(Uns), excl) < T * (1 - 1e-12):
        return
    best = None
    bo = 10 ** 9
    for q in U:
        if q in VK:
            o = maxexp(q) - max(1, R[q] - VK[q]) + 1 + (1 if R[q] <= VK[q] else 0)
        else:
            o = maxexp(q) - R[q] + 1
        if o < bo:
            bo = o
            best = q
    q = best
    if q in VK:
        if R[q] <= VK[q]:
            dfs(a, T, assigned, absent | {q}, R, used, logc)
        elo = max(1, R[q] - VK[q])
    else:
        elo = R[q]
    for e in range(elo, maxexp(q) + 1):
        qe = q ** e
        w, fl = fac_plus1(q, e)
        R2 = dict(R)
        for r, c2 in fl:
            R2[r] = R2.get(r, 0) + c2
        A2 = dict(assigned)
        A2[q] = e
        dfs(a, T, A2, absent, R2, used + w, logc + math.log1p(1.0 / qe))

def sigma_star_check(N, fac):
    s = 1
    for p, e in fac.items():
        s *= p ** e + 1
    return s == KK * N

timed_out = []
for a in cand:
    fs = factor_seed(a)
    if any(p > B or p ** e > B for p, e in fs.items()):
        print(f"  a={a}: seed has a component > B after exact factorization {fs} (float filter false positive)")
        continue
    T = KK * 2.0 ** a / (2.0 ** a + 1) if a < 1000 else float(KK)
    n0 = nodes
    t0 = elapsed()
    try:
        dfs(a, T, {}, frozenset(), dict(fs), 0, 0.0)
    except Timeout:
        timed_out.append(a)
        print(f"  a={a}: TIMEOUT after {nodes - n0} nodes", flush=True)
        break
    print(f"  a={a}: seed={fs} nodes={nodes - n0} time={elapsed() - t0:.2f}s", flush=True)

print(f"[{elapsed():.1f}s] done. total nodes={nodes}. timed_out={timed_out}")
for a, fac, N in solutions:
    full = dict(fac)
    full[2] = a
    ok = sigma_star_check(N, full)
    print(f"SOLUTION k={KK} a={a} N={N} odd={fac} sigma*=kN:{ok}")
print(f"#solutions={len(solutions)}")
