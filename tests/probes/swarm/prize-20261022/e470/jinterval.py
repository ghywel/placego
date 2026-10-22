# (1) PREDICTION: for fixed a (p = N-a prime), the odd b satisfying the exact criterion form <= 2 runs, total
#     length between N/(8a) and N/(2a) (in units of b), for sqrt(N) <= a <= N/8.  Counterfactual: many fragments,
#     or length << N/a.  Product barrier: a * |J(a)| ~ c*N, so BHP (needs both >= N^0.525) cannot be applied directly.
# (2) UNEXPECTED CHECK: does the single 2-adic bit "bit k+1 of (a-1)(b+1) is 0" (i.e. v < M) predict weirdness in
#     the band?  Prediction: it is necessary (exactly, by the criterion) and agrees in >= 80% of band pairs with
#     sqrt(N) < a < N^0.6; the failures sit where L(a+b) is comparable to M.
import sys
sys.path.insert(0, 'e470')
from wlib import *

def crit(N, a, b):
    M = N // 2
    u, v = divmod((a - 1) * (b + 1), N)
    L = (a - b - 4) // 2 + u
    return L >= 0 and L * b <= v <= M - (L + 1) * a - 1

for k in (14, 18, 22, 26):
    budget()
    N = 1 << (k + 2); M = N // 2
    rows = []
    for frac in (0.5, 0.55, 0.6, 0.65, 0.7, 0.8, 0.9):
        a = int(N ** frac) | 1
        if a >= N // 8: continue
        # scan odd b in a generous window
        lo = max(1, a - 3 * N // a - 10); hi = min(M - a, a + 8 * a * a // N + 3 * N // a + 10)
        runs = []; prev = None
        for b in range(lo | 1, hi + 1, 2):
            if crit(N, a, b):
                if prev is not None and b == prev + 2: runs[-1][1] = b
                else: runs.append([b, b])
                prev = b
        tot = sum(r[1] - r[0] + 2 for r in runs)
        rows.append((frac, a, len(runs), tot, round(tot * a / N, 3)))
    print(f"k={k} N={N}: (exponent, a, #runs, total length of J(a), length*a/N):", rows, flush=True)

# (2) unexpected check on prime pairs, k = 16..18
for k in (16, 17, 18):
    N = 1 << (k + 2); M = N // 2
    agree = tot = bitonly = 0
    A0, A1 = math.isqrt(N), int(N ** 0.6)
    for a in range(A0 | 1, A1, 2 * max(1, (A1 - A0) // 300)):
        if not is_prime(N - a): continue
        for b in range(max(1, a - 2 * N // a) | 1, min(M - a, a + 4 * a * a // N + 2 * N // a), 2):
            if not is_prime(N + b): continue
            ab, prim, w = weird_2kpq(k, N - a, N + b)
            truth = ab and w
            u, v = divmod((a - 1) * (b + 1), N)
            L = (a - b - 4) // 2 + u
            bit = (v < M) and L >= 0
            tot += 1; agree += (bit == truth)
            if truth and not bit: bitonly += 1
    print(f"k={k}: band prime pairs={tot}, bit-predictor agreement={agree/tot:.3f}, weird-but-bit-says-no={bitonly}", flush=True)
