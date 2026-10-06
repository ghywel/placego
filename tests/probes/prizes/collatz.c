/* collatz.c: stopping times of every w-bit number (collatz_count.py).
 * Usage: collatz W TCAP. For each n in [2^(W-1), 2^W), with T(n) = n/2 (n even) or (3n+1)/2 (n odd):
 *   sigma(n) = the least t >= 1 with T^t(n) < n (the stopping time), capped at TCAP;
 *   tau(n)   = the least t >= 1 with 3^(a_t) < 2^t, a_t the number of odd steps among the first t (Terras's
 *              coefficient stopping time), capped at TCAP.
 * Output: S t count_sigma_greater_than_t count_tau_greater_than_t, for t = 0 .. TCAP. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned __int128 u128;
int main(int argc, char **argv) {
    int W = atoi(argv[1]), cap = atoi(argv[2]);
    long long *hs = calloc(cap + 2, sizeof(long long)), *ht = calloc(cap + 2, sizeof(long long));
    double l23 = log(3.0) / log(2.0);
    unsigned long long lo = 1ULL << (W - 1), hi = 1ULL << W;
    /* Parallel over n with per-thread histograms (Local, 2026-10-06); the counts are identical to the serial loop. */
#pragma omp parallel
    {
        long long *ls = calloc(cap + 2, sizeof(long long)), *lt = calloc(cap + 2, sizeof(long long));
#pragma omp for schedule(dynamic, 65536)
        for (unsigned long long n = lo; n < hi; n++) {
            u128 x = n;
            int a = 0, sig = 0, tau = 0;
            for (int t = 1; t <= cap; t++) {
                if (x & 1) { x = (3 * x + 1) >> 1; a++; } else x >>= 1;
                if (!tau && a * l23 < t) tau = t;
                if (!sig && x < n) sig = t;
                if (sig && tau) break;
            }
            ls[sig ? sig : cap + 1]++;
            lt[tau ? tau : cap + 1]++;
        }
#pragma omp critical
        for (int t = 0; t <= cap + 1; t++) { hs[t] += ls[t]; ht[t] += lt[t]; }
        free(ls); free(lt);
    }
    long long gs = 0, gt = 0;                 /* counts with sigma (tau) > t */
    for (int t = cap + 1; t >= 1; t--) { gs += hs[t]; gt += ht[t]; hs[t] = gs; ht[t] = gt; }
    for (int t = 0; t <= cap; t++)
        printf("S %d %lld %lld\n", t, t == 0 ? (long long)(hi - lo) : hs[t + 1], t == 0 ? (long long)(hi - lo) : ht[t + 1]);
    return 0;
}
