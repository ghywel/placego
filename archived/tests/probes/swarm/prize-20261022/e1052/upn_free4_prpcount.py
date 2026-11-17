#!/usr/bin/env python3
"""Box-free complete search for unitary perfect numbers with a FIXED power 2^a (small a).
Seed-driven closure (Lemma A).  No component bound: exponent ranges are closed by a tail prune:
for q pending with current supply r, all exponents e >= e0 are cut when
c * (1+q^-e0) * prod_{other pending}(1+s^-R[s]) * newmax_excl(rem-|U|) < T.
We branch on a pending q whose tail closes (TB(inf) < T); if none closes, the a is reported UNBOUNDED (incomplete).
Factoring: Pollard-Brent + Miller-Rabin (deterministic bases below 3.3e24, 24 random bases above).
Usage: upn_free.py amax per_a_seconds"""
import sys, time, math, random
AMAX = int(sys.argv[1]); PERA = float(sys.argv[2]); YMAX = float(sys.argv[3]) if len(sys.argv) > 3 else 150000.0
AMIN = int(sys.argv[4]) if len(sys.argv) > 4 else 1
random.seed(12345)
SMALLP = [p for p in range(3, 200000) if all(p % d for d in range(2, int(p ** 0.5) + 1))] if False else None
# sieve small primes
LIM = int(sys.argv[5]) if len(sys.argv) > 5 else 200000
import numpy as np
sv = np.ones(LIM + 1, dtype=bool); sv[:2] = False
for i in range(2, int(LIM ** 0.5) + 1):
    if sv[i]:
        sv[i * i::i] = False
PR = [int(x) for x in np.flatnonzero(sv)]
ODDP = PR[1:]
assert YMAX < LIM, 'YMAX must stay below the prime table'

BIGPRP = [0, 0]
def is_prp(n):
    r = _is_prp(n)
    if r and n >= 3317044064679887385961981:
        BIGPRP[0] += 1
        BIGPRP[1] = max(BIGPRP[1], n.bit_length())
    return r

def _is_prp(n):
    if n < 2:
        return False
    for p in PR[:25]:
        if n % p == 0:
            return n == p
    d = n - 1; s = 0
    while d % 2 == 0:
        d //= 2; s += 1
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n >= 3317044064679887385961981:
        bases = bases + [random.randrange(2, n - 1) for _ in range(24)]
    for b in bases:
        x = pow(b, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

class FactorFail(Exception):
    pass

def brent(n, deadline):
    if n % 2 == 0:
        return 2
    while True:
        y = random.randrange(1, n); c = random.randrange(1, n); m = 128
        g = r = q = 1
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = (y * y + c) % n
                    q = q * abs(x - y) % n
                g = math.gcd(q, n)
                k += m
            r *= 2
            if time.time() > deadline:
                raise FactorFail(n)
        if g == n:
            g = 1
            while g == 1:
                ys = (ys * ys + c) % n
                g = math.gcd(abs(x - ys), n)
        if g != n:
            return g

_fcache = {}
def factor(n, deadline):
    if n in _fcache:
        return dict(_fcache[n])
    f = {}
    m = n
    for p in PR[:2000]:
        if m % p == 0:
            c = 0
            while m % p == 0:
                m //= p; c += 1
            f[p] = c
        if p * p > m:
            break
    stack = [m] if m > 1 else []
    while stack:
        x = stack.pop()
        if x == 1:
            continue
        if is_prp(x):
            f[x] = f.get(x, 0) + 1
            continue
        r = math.isqrt(x)
        if r * r == x:
            stack += [r, r]; continue
        d = brent(x, deadline)
        stack += [d, x // d]
    _fcache[n] = dict(f)
    return f

def newmax_excl(m, excl):
    if m <= 0:
        return 1.0
    prod = 1.0; cnt = 0
    for r in ODDP:
        if r in excl:
            continue
        prod *= 1.0 + 1.0 / r
        cnt += 1
        if cnt == m:
            return prod
    return float('inf')

class Unbounded(Exception):
    pass
class Timeout(Exception):
    pass

solutions = []
UNB = []
def run_a(a):
    T = 2.0 ** (a + 1) / (2.0 ** a + 1)
    deadline = time.time() + PERA
    nodes = [0]
    def tail_ok(c, U, R, q, rem, excl, e0):
        """True if exponents e >= e0 of q are all prunable (bound < T)."""
        other = 1.0
        for s in U:
            if s != q:
                other *= 1.0 + float(s) ** (-R[s])
        tb = c * (1.0 + (float(q) ** (-e0) if e0 < 4000 else 0.0)) * other * newmax_excl(rem - len(U), excl)
        return tb < T * (1 - 1e-12)
    def dfs(assigned, R, used, logc):
        nodes[0] += 1
        if time.time() > deadline:
            raise Timeout
        U = [q for q in R if q not in assigned]
        if used + len(U) > a + 1:
            return
        for p, e in assigned.items():
            if R.get(p, 0) > e:
                return
        c = math.exp(logc)
        rem = a + 1 - used
        if not U:
            if used == a + 1 and all(R.get(p, 0) == e for p, e in assigned.items()):
                N = 2 ** a
                for p, e in assigned.items():
                    N *= p ** e
                solutions.append((a, dict(sorted(assigned.items())), N))
            return
        if c > T * (1 + 1e-12):
            return
        excl = assigned.keys() | set(U)
        up = c
        for q in U:
            up *= 1.0 + float(q) ** (-R[q])
        if up * newmax_excl(rem - len(U), excl) < T * (1 - 1e-12):
            return
        # choose a pending prime whose exponent tail closes; prefer the one closing soonest
        best = None
        for q in U:
            if not tail_ok(c, U, R, q, rem, excl, 10 ** 9):
                continue
            e0 = R[q]
            while not tail_ok(c, U, R, q, rem, excl, e0):
                e0 += 1
            span = e0 - R[q]
            if best is None or span < best[1]:
                best = (q, span, e0)
        if best is None:
            # Dickson gap step: prod_future (1+x_i) = T/c = 1+delta with at most rem factors,
            # so some future component is <= Y.  Branch over all of them (U primes and new primes).
            delta = T / c - 1.0
            Y = 1.0 / ((1.0 + delta) ** (1.0 / rem) - 1.0) * (1 + 1e-9) + 1e-9
            if Y > YMAX:
                UNB.append(Y)
                return
            cands = []
            for q in U:
                e = R[q]
                while q ** e <= Y:
                    cands.append((q, e)); e += 1
            for s in ODDP:
                if s > Y:
                    break
                if s in assigned or s in R:
                    continue
                e = 1
                while s ** e <= Y:
                    cands.append((s, e)); e += 1
            for (q, e) in cands:
                f = factor(q ** e + 1, deadline)
                w = f.pop(2, 0)
                R2 = dict(R)
                for r, c2 in f.items():
                    R2[r] = R2.get(r, 0) + c2
                A2 = dict(assigned); A2[q] = e
                dfs(A2, R2, used + w, logc + math.log1p(float(q) ** (-e)))
            return
        q, span, e0 = best
        for e in range(R[q], e0):
            f = factor(q ** e + 1, deadline)
            w = f.pop(2, 0)
            R2 = dict(R)
            for r, c2 in f.items():
                R2[r] = R2.get(r, 0) + c2
            A2 = dict(assigned); A2[q] = e
            dfs(A2, R2, used + w, logc + math.log1p(float(q) ** (-e)))
    seed = factor(2 ** a + 1, deadline)
    t0 = time.time()
    UNB.clear()
    try:
        dfs({}, seed, 0, 0.0)
        status = "COMPLETE" if not UNB else f"INCOMPLETE: {len(UNB)} node(s) with Y > YMAX (max Y = {max(UNB):.3g})"
    except Unbounded as ex:
        status = f"UNBOUNDED at {ex.args[0]}"
    except Timeout:
        status = "TIMEOUT"
    except FactorFail as ex:
        status = f"FACTOR-FAIL ({len(str(ex.args[0]))} digits)"
    print(f"[bigprp so far {BIGPRP[0]}] a={a}: seed={seed} nodes={nodes[0]} time={time.time()-t0:.2f}s status={status}", flush=True)

for a in range(AMIN, AMAX + 1):
    run_a(a)
for a, fac, N in solutions:
    s = 2 ** a + 1
    for p, e in fac.items():
        s *= p ** e + 1
    print(f"SOLUTION a={a} N={N} odd={fac} sigma*=2N:{s == 2 * N}")
print("#solutions", len(solutions))
print("probabilistic-prime declarations above 3.3e24:", BIGPRP[0], "max bits", BIGPRP[1])
