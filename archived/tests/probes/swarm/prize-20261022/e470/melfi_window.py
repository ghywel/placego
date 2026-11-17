# Test: for n = 2^k p q, p = N - a, q = N + b (N = 2^{k+2}, a,b odd, a > b+3),
# PREDICTION: n primitive weird  <=>  a(a+b) <= N + 2b   (Melfi's sufficient window: a < 2^{(k-1)/2}).
import sys
sys.path.insert(0, 'e470')
from wlib import *
kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 16
for k in range(4, kmax + 1):
    budget()
    N = 1 << (k + 2)
    amax = int(2.0 * math.isqrt(N)) + 20
    tot = agree = 0; viol_suff = []; viol_nec = []; nw_pred = nw_melfi = nw_true = 0
    primes_below = [a for a in range(1, amax + 1, 2) if is_prime(N - a)]
    primes_above = [b for b in range(1, amax + 1, 2) if is_prime(N + b)]
    for a in primes_below:
        for b in primes_above:
            if not (b + 3 < a): break
            ab, prim, w = weird_2kpq(k, N - a, N + b)
            truth = ab and prim and w
            pred = a * (a + b) <= N + 2 * b
            melfi = a < 2 ** ((k - 1) / 2)
            tot += 1
            nw_true += truth; nw_pred += pred; nw_melfi += melfi
            if pred and not truth: viol_suff.append((a, b, ab, prim, w))
            if truth and not pred: viol_nec.append((a, b))
            if melfi and not truth: print("  MELFI VIOLATION?", k, a, b)
    print(f"k={k:2d} N={N} pairs={tot} primweird={nw_true} predicted={nw_pred} melfi_window={nw_melfi} "
          f"pred-but-not-weird={len(viol_suff)} weird-but-not-pred={len(viol_nec)}", viol_suff[:3], viol_nec[:3], flush=True)
