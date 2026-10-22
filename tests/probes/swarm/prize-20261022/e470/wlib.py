# Shared tools for e470: exact weirdness tests.
import time, math
T0 = time.time()
LIMIT = 540  # seconds, hard budget per script

def budget():
    if time.time() - T0 > LIMIT:
        raise SystemExit("TIME LIMIT")

MR_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)
def is_prime(n):
    if n < 2: return False
    for p in MR_BASES:
        if n % p == 0: return n == p
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in MR_BASES:
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else:
            return False
    return True

def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1 if d == 2 else 2
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def divisors(n):
    divs = [1]
    for p, e in factor(n).items():
        divs = [d * p**i for d in divs for i in range(e + 1)]
    return sorted(divs)

def sigma(n):
    s = 1
    for p, e in factor(n).items():
        s *= (p**(e + 1) - 1) // (p - 1)
    return s

def subset_sum_reachable(nums, target):
    """Bitset DP: is target a sum of distinct elements of nums? (exact)"""
    mask = (1 << (target + 1)) - 1
    bits = 1
    for d in nums:
        if d > target: continue
        bits |= (bits << d) & mask
        if (bits >> target) & 1: return True
    return bool((bits >> target) & 1)

def is_weird_bruteforce(n):
    s = sigma(n)
    if s < 2 * n: return False
    if s == 2 * n: return False  # perfect -> pseudoperfect
    delta = s - 2 * n
    props = divisors(n)[:-1]
    return not subset_sum_reachable(props, delta)

def representable_2kpq(k, p, q, x):
    """Exact: is x a sum of distinct proper divisors of n = 2^k p q (p, q distinct odd primes)?
    Sums are r + h p + h' q + g pq, r,h,h' in [0, 2^{k+1}-1], g in [0, 2^k - 1]."""
    M = 1 << (k + 1)
    pq = p * q
    for g in range(0, min(M // 2 - 1, x // pq) + 1):
        x1 = x - g * pq
        for h in range(0, min(M - 1, x1 // p) + 1):
            x2 = x1 - h * p
            # need h' in [0, M-1] with 0 <= x2 - h' q <= M - 1
            lo = max(0, -(-(x2 - (M - 1)) // q))
            hi = min(M - 1, x2 // q)
            if lo <= hi: return True
    return False

def weird_2kpq(k, p, q):
    """Returns (abundant, primitive_abundant, weird) exactly for n = 2^k p q."""
    M = 1 << (k + 1)
    s = (M - 1) * (p + 1) * (q + 1)
    n = (M // 2) * p * q
    delta = s - 2 * n
    if delta <= 0: return (delta >= 0, False, False)
    # primitive abundant: n/2, n/p, n/q deficient
    prim = True
    for (num, den) in ((n // 2, None), (n // p, None), (n // q, None)):
        pass
    def sig_parts(kk, ps):
        t = (1 << (kk + 1)) - 1
        for x in ps: t *= (x + 1)
        return t
    if k >= 1 and sig_parts(k - 1, (p, q)) >= 2 * (n // 2): prim = False
    if sig_parts(k, (q,)) >= 2 * (n // p): prim = False
    if sig_parts(k, (p,)) >= 2 * (n // q): prim = False
    w = not representable_2kpq(k, p, q, delta)
    return (True, prim, w)
