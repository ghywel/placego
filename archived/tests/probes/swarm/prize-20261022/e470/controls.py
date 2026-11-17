# Controls: reproduce known weird and primitive weird numbers; cross-check structure test vs bitset DP.
import sys
sys.path.insert(0, 'e470')
from wlib import *

# 1. weird numbers below 15000 by brute force
weird = [n for n in range(2, 15000) if is_weird_bruteforce(n)]
print("weird < 15000:", len(weird), weird[:25])
# 2. primitive weird = weird and primitive abundant (all n/p deficient)
def prim_abundant(n):
    if sigma(n) < 2 * n: return False
    return all(sigma(n // p) < 2 * (n // p) for p in factor(n))
pw = [n for n in weird if prim_abundant(n)]
print("primitive weird < 15000:", pw)
# 3. Melfi's example 4128448 = 2^6 * 251 * 257
print("4128448 weird (bitset):", is_weird_bruteforce(4128448), "structure test:", weird_2kpq(6, 251, 257))
# 4. cross-check structure test vs bitset for all 2^k p q < 3e5 (k>=1, p<q odd primes)
mism = 0; tested = 0
for k in range(1, 8):
    for p in range(3, 2000, 2):
        if not is_prime(p): continue
        for q in range(p + 2, 300000 // ((1 << k) * p) + 1, 2):
            if not is_prime(q): continue
            n = (1 << k) * p * q
            if n >= 300000: break
            a, pr, w = weird_2kpq(k, p, q)
            wb = is_weird_bruteforce(n)
            tested += 1
            if (a and w) != wb:
                mism += 1; print("MISMATCH", k, p, q, a, w, wb)
print("structure-vs-bitset tested", tested, "mismatches", mism)
