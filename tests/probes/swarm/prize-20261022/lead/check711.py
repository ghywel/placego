# Lead's independent check of e711's K_{2,3} construction: f(n, m) >= 3K+1 at the CRT start, here n = 20 (K = 14, a = 3).
from math import gcd
def f(n, m):
    """least H such that (m, m+H) holds distinct a_1..a_n with k | a_k (augmenting-path matching, rebuilt per H)"""
    H = n
    while True:
        ints = range(m + 1, m + H)
        match = {}
        def aug(k, seen):
            for x in range(((m + 1 + k - 1) // k) * k, m + H, k):
                if x in seen: continue
                seen.add(x)
                if x not in match or aug(match[x], seen):
                    match[x] = k; return True
            return False
        if all(aug(k, set()) for k in range(n, 0, -1)):
            return H
        H += 1
def crt(congs):
    x, M = 0, 1
    for r, mod in congs:
        g = gcd(M, mod)
        assert (r - x) % g == 0, 'inconsistent'
        while x % mod != r % mod: x += M
        M = M * mod // g
    return x, M
for n in (20, 22, 25, 31):
    K = n - 6 if n % 3 else n - 7
    a = 3 if K % 5 else 1
    M2, M1 = [K, K + a, K + 4], [K + 2, K + 2 + a, K + 6]
    m, L = crt([(-K % k, k) for k in M2] + [(-(K - 2) % k, k) for k in M1])
    m += L  # any start in the class; keep m > n
    print(f"n={n} K={K} a={a} m={m}: f(n,m)={f(n, m)}  claimed lower bound 3K+1={3*K+1}  formula max(2n-1, 3n-17-3[3|n])={max(2*n-1, 3*n-17-3*(n%3==0))}")
# control: f(n,n) for small n against OEIS A390246's first terms as the agent reported via its control (n=4 -> 6)
print('control f(4,4) =', f(4, 4), '(OEIS example a(4) = 6)')
