"""Adversarial re-check of result 1 (conditional theorem): numeric tests of the carrying inequalities.

T1  Pointwise Bonferroni: 1[r=0] >= sum_{j<=J} (-1)^j C(r,j) for odd J (all r up to 60).
T2  Model Bonferroni: for x_i in [0,1]: S_J <= prod(1-x) <= S_J + e_{J+1} for odd J  (random tests).
T3  Local factors: for p > k, with nu = #classes of S mod p:
      1 - k^2/p^2 <= f_p = (1 - nu/p)(1-1/p)^{-k} <= 1 if nu = k, and <= exp(2k/p) if nu < k.
T4  Tail singular series S_{>z}(S) = prod_{z<p<=PMAX} f_p versus the bounds
      1 - k^2/z <= S_{>z} <= exp(2k * sum_{p>z, p | Delta(S)} 1/p),
    for random S and adversarial S = {0, Q, 2Q, ...} with Q a product of the primes just above z.
T5  The asymptotic step: max over D <= (2X)^{k^2} of sum_{p|D, p>z} 1/p  vs  log(1/(1-eta)), z = (log X)^{1-eta}.
"""
import math, itertools, random
import numpy as np

def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]: s[p*p::p] = False
    return np.nonzero(s)[0]

PR = primes_upto(2_000_000)
ok = True
# T1
for J in (1, 3, 5, 7):
    for r in range(0, 61):
        lhs = 1 if r == 0 else 0
        rhs = sum((-1) ** j * math.comb(r, j) for j in range(J + 1))
        if lhs < rhs: ok = False; print('T1 FAIL', J, r)
print('T1 pointwise Bonferroni: ok' if ok else 'T1 FAIL')
# T2
rng = np.random.default_rng(7)
bad = 0
for trial in range(3000):
    n = rng.integers(1, 40)
    x = rng.random(n) * rng.choice([0.05, 0.3, 1.0])
    # elementary symmetric e_0..e_n
    e = np.zeros(n + 1); e[0] = 1.0
    for xi in x:
        e[1:] = e[1:] + xi * e[:-1]
    P = np.prod(1 - x)
    for J in (1, 3, 5, 7, 9):
        if J + 1 > n: break
        SJ = sum((-1) ** j * e[j] for j in range(J + 1))
        if not (SJ <= P + 1e-12 and P <= SJ + e[J + 1] + 1e-12): bad += 1
print('T2 model Bonferroni (S_J <= prod <= S_J + e_{J+1}, J odd):', 'ok' if bad == 0 else f'{bad} FAILS')
# T3
bad = 0
for k in range(1, 9):
    for p in PR[PR > k][:200]:
        p = int(p)
        for nu in range(1, k + 1):
            f = (1 - nu / p) / (1 - 1 / p) ** k
            lo = 1 - k * k / p ** 2
            hi = 1.0 if nu == k else math.exp(2 * k / p)
            if not (lo - 1e-15 <= f <= hi + 1e-15): bad += 1; print('T3 FAIL', k, p, nu, f, lo, hi)
print('T3 local factor bounds:', 'ok' if bad == 0 else f'{bad} FAILS')
# T4
def tail_ss(S, z, pmax=2_000_000):
    k = len(S); val = 1.0
    for p in PR[(PR > z) & (PR <= pmax)]:
        p = int(p)
        nu = len(set(a % p for a in S))
        val *= (1 - nu / p) / (1 - 1 / p) ** k
    return val
def delta_primes_sum(S, z):
    tot = 0.0
    D = set()
    for a, b in itertools.combinations(S, 2):
        d = abs(b - a)
        for p in PR[(PR > z) & (PR <= 10_000)]:
            if d % int(p) == 0: D.add(int(p))
    return sum(1.0 / p for p in D)
random.seed(3)
worst = 0.0
for X, eta in ((10 ** 12, 0.3), (10 ** 15, 0.2)):
    z = math.log(X) ** (1 - eta)
    for k in (2, 3, 5, 7):
        cases = []
        for _ in range(6):
            cases.append(('random', sorted(random.sample(range(0, 2 * X), k))))
        # adversarial: S = {0, Q, 2Q, ...}, Q = product of primes just above z with (k-1)Q <= 2X
        Q = 1
        for p in PR[PR > z]:
            if (k - 1) * Q * int(p) > 2 * X: break
            Q *= int(p)
        cases.append(('adversarial', [i * Q for i in range(k)]))
        for name, S in cases:
            s = tail_ss(S, z)
            hi = math.exp(2 * k * delta_primes_sum(S, z))
            lo = 1 - k * k / z
            flag = 'ok' if lo <= s <= hi * 1.000001 else 'FAIL'
            if name == 'adversarial' or flag == 'FAIL':
                print(f'T4 X=1e{round(math.log10(X))} eta={eta} z={z:.2f} k={k} {name}: S_>z={s:.4f}  bounds [{lo:.4f}, {hi:.4f}]  {flag}')
            worst = max(worst, s)
# T5
for X, eta in ((10 ** 12, 0.3), (10 ** 100, 0.3), (10 ** 1000, 0.3), (10 ** 1000, 0.1)):
    lX = math.log(X); z = lX ** (1 - eta)
    for k in (3,):
        budget = k * k * math.log(2 * X)
        s = 0.0; used = 0.0
        for p in PR[PR > z]:
            if used + math.log(p) > budget: break
            used += math.log(p); s += 1.0 / p
        print(f'T5 X=1e{round(math.log10(X))} eta={eta} k={k}: worst sum 1/p over p|D, p>z = {s:.4f}; '
              f'log(1/(1-eta)) = {math.log(1/(1-eta)):.4f}; 2*eta = {2*eta:.3f}')
