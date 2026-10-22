# Numerical kill test of the PROOF-SKETCH: for 84 < n <= X, tau(n-k) <= k+2 for k in {1,...,6,12}
# should force 2520 | n and aN-1 prime for a in {210,420,630,840,1260,2520} (N = n/2520).
import numpy as np
X = 3_000_000
tau = np.zeros(X+1, dtype=np.int32)
for d in range(1, X+1):
    tau[d::d] += 1
isprime = (tau == 2)
B = [n for n in range(85, X+1) if all(tau[n-k] <= k+2 for k in (1,2,3,4,5,6,12))]
bad = []
for n in B:
    if n % 2520: bad.append((n, 'not 2520|n')); continue
    N = n // 2520
    for a in (210, 420, 630, 840, 1260, 2520):
        if not isprime[a*N-1]: bad.append((n, a)); break
print('X =', X, '| #B =', len(B), '| violations =', len(bad), bad[:10])
print('B (first 30):', B[:30])
# how many 2520N <= X have all six forms prime (the reduction's candidate set)
cand = [2520*N for N in range(1, X//2520+1) if all(isprime[a*N-1] for a in (210,420,630,840,1260,2520))]
print('#candidates 2520N<=X with six primes =', len(cand), cand[:12])
