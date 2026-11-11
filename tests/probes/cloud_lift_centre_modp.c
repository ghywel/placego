/* Cloud CL776/CL777: centre column of the integer lift of rule 30 modulo a small prime P (compile with -DP=7).
   A' = l + c + r + c*r (mod P) from a single 1.  Only the cone that can reach the centre is updated.
   Prints residue counts on the segments [0,2^16), [2^16,2^18), [2^18,2^20), [2^20,N) and pair counts
   (c(t), c(t+1)) on [2^18, N).  Usage: prog LOGN   (second code; the first is cloud_integer_lift_primes.py).
   Compile with -fopenmp to update each row on several threads (added for N1j); the output is unchanged. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#ifndef P
#define P 7
#endif
int main(int argc, char **argv) {
    int logn = argc > 1 ? atoi(argv[1]) : 18;
    long N = 1L << logn, W = 2 * N + 8, c = N + 4;
    uint8_t *a = calloc(W, 1), *b = calloc(W, 1), *out = malloc(N);
    if (!a || !b || !out) return 3;
    a[c] = 1;
    for (long t = 0; t < N; t++) {
        out[t] = a[c];
        long r = t + 1 < N - 1 - t ? t + 1 : N - 1 - t;
        if (r < 0) break;
        long lo = c - r - 1, hi = c + r + 1;          /* update cells lo..hi */
        const uint8_t *restrict x = a; uint8_t *restrict y = b;
        #pragma omp parallel for schedule(static) if (hi - lo > 262144)   /* added for N1j (CL778): threads, same arithmetic */
        for (long j = lo; j <= hi; j++) {
#if P == 5 && defined(FAST5)
            /* added for N1j (CL778): the same value in byte arithmetic only, so that the compiler can use byte lanes.
               c*r by shifted adds (r <= 4), then v <= 28 reduced by three conditional subtractions.               */
            uint8_t cc = x[j], rr = x[j + 1];
            uint8_t m = (uint8_t)((cc & (uint8_t)(0 - (rr & 1))) + ((uint8_t)(cc + cc) & (uint8_t)(0 - ((rr >> 1) & 1)))
                                  + ((uint8_t)(4 * cc) & (uint8_t)(0 - ((rr >> 2) & 1))));
            uint8_t v = (uint8_t)(x[j - 1] + cc + rr + m), w;
            w = (uint8_t)(v - 20); v = w < v ? w : v;
            w = (uint8_t)(v - 10); v = w < v ? w : v;
            w = (uint8_t)(v - 5);  v = w < v ? w : v;
            y[j] = v;
#else
            unsigned v = (unsigned)x[j - 1] + x[j] + x[j + 1] + (unsigned)x[j] * x[j + 1];
            y[j] = (uint8_t)(v % P);
#endif
        }
        y[lo - 1] = 0; y[hi + 1] = 0;
        uint8_t *tmp = a; a = b; b = tmp;
    }
    long bounds[5] = {0, 1L << 16, 1L << 18, 1L << 20, N};
    for (int s = 0; s < 4; s++) {
        long lo = bounds[s], hi = bounds[s + 1] < N ? bounds[s + 1] : N;
        if (lo >= hi) continue;
        long cnt[P]; memset(cnt, 0, sizeof cnt);
        for (long t = lo; t < hi; t++) cnt[out[t]]++;
        printf("segment %ld %ld counts", lo, hi);
        for (int k = 0; k < P; k++) printf(" %ld", cnt[k]);
        printf("\n");
        static long sp[P * P]; memset(sp, 0, sizeof sp);      /* added after the 2^21 run: pair table per segment */
        for (long t = lo; t + 1 < hi; t++) sp[out[t] * P + out[t + 1]]++;
        printf("segpairs %ld %ld counts", lo, hi);
        for (int k = 0; k < P * P; k++) printf(" %ld", sp[k]);
        printf("\n");
    }
    if (N > (1L << 18)) {
        static long pc[P * P];
        for (long t = 1L << 18; t + 1 < N; t++) pc[out[t] * P + out[t + 1]]++;
        printf("pairs %ld %ld counts", 1L << 18, N);
        for (int k = 0; k < P * P; k++) printf(" %ld", pc[k]);
        printf("\n");
    }
    if (argc > 2) {                                  /* added for N1h: save the whole sequence, one byte per tick */
        FILE *f = fopen(argv[2], "wb");
        if (f) { fwrite(out, 1, N, f); fclose(f); }
    }
    printf("first40");
    for (int t = 0; t < 40; t++) printf(" %d", out[t]);
    printf("\n");
    return 0;
}
