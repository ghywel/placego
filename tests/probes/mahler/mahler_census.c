/* mahler_census.c: exact survival horizons H(n) for Mahler's 3/2 problem, every start n in [0, 2^w), by a
 * depth-first walk over the low bits of n. See mahler_census.py for the method, predictions and outcome.
 *
 * State at depth T (T low bits of n chosen, n0low < 2^T):
 *   v  = T^T(n0low) mod 2^128, the T-th iterate of the truncated start under T(x) = ceil(3x/2); the true n_T is
 *        v + 3^T (n >> T), so the parity b_T of n_T is (v + bit_T(n)) mod 2.
 *   lo, hi = numerators over 2^(T+1) of the exact half-open window [lo, hi) of the current fractional part u_T.
 * Step with parity b: lo' = max(0, 3 lo - b 2^(T+1)), hi' = min(2^(T+1), 3 hi - b 2^(T+1)) over 2^(T+2); alive iff
 * lo' < hi'.  v' = (3 (v + 3^T bit) + b) / 2.
 * At T = w the start is complete and the orbit is forced (b = v mod 2) until the window empties.  128-bit numerators
 * are exact while T + 2 <= 127; a start still alive at T = TMAX is printed as a straggler for exact Python replay.
 *
 * Usage: mahler_census W PREFIXBITS PREFIX  (walks the starts whose low PREFIXBITS bits equal PREFIX)
 * Output: "H h count" lines (count of starts with horizon exactly h), "S n" straggler lines, "MAX h n". */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef unsigned __int128 u128;
#define TMAX 124
#define HMAX 512
static int W;
static u128 pow3[130];
static unsigned long long hist[HMAX];
static int maxh = 0;
static unsigned long long argmax = 0;

static void record(int h, unsigned long long n, unsigned long long mult) {
    if (h >= HMAX) h = HMAX - 1;
    hist[h] += mult;
    if (h > maxh && mult == 1) { maxh = h; argmax = n; }
}

/* one step of the window with parity b at depth T; returns 0 if the window empties */
static inline int wstep(u128 *lo, u128 *hi, int b, int T) {
    u128 D = ((u128)1) << (T + 1);
    u128 l3 = 3 * (*lo), h3 = 3 * (*hi);
    u128 nl, nh;
    if (b) { nl = (l3 > D) ? l3 - D : 0; nh = (h3 > D) ? h3 - D : 0; }
    else { nl = l3; nh = h3; }
    u128 cap = ((u128)1) << (T + 1);                 /* 1/2 over 2^(T+2) */
    if (nh > cap) nh = cap;
    *lo = nl; *hi = nh;
    return nl < nh;
}

static void forced(unsigned long long n, u128 v, u128 lo, u128 hi, int T) {
    if (n == 0) return;                              /* the excluded origin xi = 0 */
    while (T < TMAX) {
        int b = (int)(v & 1);
        if (!wstep(&lo, &hi, b, T)) { record(T + 1, n, 1); return; }
        v = (3 * v + b) >> 1;
        T++;
    }
    printf("S %llu\n", n);                          /* alive at TMAX: exact replay in Python */
}

static void dfs(int T, unsigned long long n0low, u128 v, u128 lo, u128 hi) {
    if (T == W) { forced(n0low, v, lo, hi, T); return; }
    for (int bit = 0; bit < 2; bit++) {
        int b = (int)((v + (u128)bit) & 1);
        u128 nlo = lo, nhi = hi;
        unsigned long long nn = n0low | ((unsigned long long)bit << T);
        if (!wstep(&nlo, &nhi, b, T)) {             /* every start with these T+1 low bits dies at step T+1 */
            unsigned long long mult = 1ULL << (W - T - 1);
            record(T + 1, nn, mult);
            continue;
        }
        u128 nv = (3 * (v + (bit ? pow3[T] : 0)) + b) >> 1;
        dfs(T + 1, nn, nv, nlo, nhi);
    }
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: %s W PREFIXBITS PREFIX\n", argv[0]); return 1; }
    W = atoi(argv[1]);
    int pb = atoi(argv[2]);
    unsigned long long prefix = strtoull(argv[3], 0, 10);
    pow3[0] = 1;
    for (int i = 1; i < 130; i++) pow3[i] = pow3[i - 1] * 3;
    /* replay the fixed prefix bits */
    u128 v = 0, lo = 0, hi = 1;                      /* [0, 1/2) over 2^1: lo = 0, hi = 1 */
    unsigned long long n0low = 0;
    int T = 0;
    for (; T < pb; T++) {
        int bit = (int)((prefix >> T) & 1);
        int b = (int)((v + (u128)bit) & 1);
        n0low |= (unsigned long long)bit << T;
        if (!wstep(&lo, &hi, b, T)) {
            record(T + 1, n0low, 1ULL << (W - pb));        /* this chunk's own starts only (first run overcounted) */
            goto done;
        }
        v = (3 * (v + (bit ? pow3[T] : 0)) + b) >> 1;
    }
    dfs(T, n0low, v, lo, hi);
done:
    for (int h = 0; h < HMAX; h++) if (hist[h]) printf("H %d %llu\n", h, hist[h]);
    printf("MAX %d %llu\n", maxh, argmax);
    return 0;
}
