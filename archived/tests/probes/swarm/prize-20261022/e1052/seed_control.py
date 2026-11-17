#!/usr/bin/env python3
"""Independent control of upn_box.py's seed filter: direct trial division of 2^a+1 by all primes <= B."""
import sys, math, time
B = int(sys.argv[1]); AMAX = int(sys.argv[2])
t0 = time.time()
sieve = bytearray([1]) * (B + 1); sieve[0] = sieve[1] = 0
for i in range(2, math.isqrt(B) + 1):
    if sieve[i]:
        sieve[i*i::i] = bytearray(len(range(i*i, B+1, i)))
ps = [i for i in range(3, B + 1, 2) if sieve[i]]
good = []
for a in range(1, AMAX + 1):
    n = 2 ** a + 1
    ok = True
    for p in ps:
        if n % p == 0:
            pe = 1
            while n % p == 0:
                n //= p; pe *= p
            if pe > B:
                ok = False; break
        if n == 1:
            break
        if p * p > n:
            # remaining n is prime (or 1)
            if n > B:
                ok = False
            n = 1
            break
    if n != 1:
        ok = False
    if ok:
        good.append(a)
    if time.time() - t0 > 500:
        print("timeout at a", a); break
print("direct-trial-division smooth a:", good)
print(f"time {time.time()-t0:.1f}s")
