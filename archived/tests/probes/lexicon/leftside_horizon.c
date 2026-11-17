// leftside_horizon.c: the LEFT half on its own, next to a periodic wall. Local, 2026-10-06; RULE30-PRIZE.md section
// 8.66; driver rule30_leftside_horizon.py.
//
// Given column 0 = a periodic word tau, the left half of a two-sided configuration evolves autonomously under Rule 30
// with tau as its boundary: x(i, t+1) = x(i-1, t) xor (x(i, t) or x(i+1, t)) for i <= -1, with x(0, t) = tau(t). The
// right half enters only through column 1's stream sigma, and column 0's own update, tau(t+1) = x(-1, t) xor
// (tau(t) or sigma(t)), puts two conditions on column -1 that no right half can lift:
//   (i)  at every black time t:  x(-1, t) = not tau(t+1)                       (sigma is invisible, Lemma 1);
//   (ii) at white times, sigma(t) = tau(t+1) xor x(-1, t), and inside one white stretch of the wall a real column 1
//        can only turn black (x(1, t+1) = sigma(t) or x(2, t) while tau(t) = 0), so sigma is non-decreasing there.
// For every finite left seed of width W (cells -W .. -1 at time 0, cell -W black) and every phase of the wall, the
// survival time is the first t at which (i) or (ii) fails. The left horizon H_L(W) is its maximum over seeds and
// phases. It bounds from above the lifetime of every two-sided configuration whose left half has width W.
//
// Usage: leftside_horizon WORD WMAX [T=100] [THREADS]      (W + T <= 128)
// Output per width: H W = h  phase p  seed s   (and CAPPED if h reached T)
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _OPENMP
#include <omp.h>
#endif
typedef unsigned __int128 u128;

static char WORD[64]; static int P, T;

static int survive(u128 x, int phase) {
    int prev = 0, in_white = 0;                     /* sigma at the previous time, if the previous time was white */
    for (int t = 0; t < T; t++) {
        int tau = WORD[(phase + t) % P] - '0', tau1 = WORD[(phase + t + 1) % P] - '0';
        int c = (int)(x & 1);
        if (tau) {
            if (c != !tau1) return t;               /* (i) */
            in_white = 0;
        } else {
            int sigma = tau1 ^ c;
            if (in_white && sigma < prev) return t; /* (ii) */
            prev = sigma; in_white = 1;
        }
        x = (x >> 1) ^ (x | ((x << 1) | (u128)tau));
    }
    return T;
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: leftside_horizon WORD WMAX [T] [THREADS]\n"); return 2; }
    strncpy(WORD, argv[1], 63); P = (int)strlen(WORD);
    int wmax = atoi(argv[2]); T = argc > 3 ? atoi(argv[3]) : 100;
#ifdef _OPENMP
    if (argc > 4) omp_set_num_threads(atoi(argv[4]));
#endif
    if (wmax + T > 128) { fprintf(stderr, "W + T must be at most 128\n"); return 2; }
    for (int W = 0; W <= wmax; W++) {
        uint64_t lo = W ? (uint64_t)1 << (W - 1) : 0, hi = W ? (uint64_t)1 << W : 1;
        int best = -1, bphase = 0; uint64_t bseed = 0;
        for (int phase = 0; phase < P; phase++) {
            int pb = -1; uint64_t ps = 0;
#pragma omp parallel
            {
                int tb = -1; uint64_t ts = 0;
#pragma omp for schedule(static)
                for (uint64_t s = lo; s < hi; s++) {
                    int h = survive((u128)s, phase);
                    if (h > tb) { tb = h; ts = s; }
                }
#pragma omp critical
                if (tb > pb || (tb == pb && ts < ps)) { pb = tb; ps = ts; }
            }
            if (pb > best) { best = pb; bphase = phase; bseed = ps; }
        }
        printf("H %s %d = %d  phase %d  seed %llx%s\n", WORD, W, best, bphase, (unsigned long long)bseed,
               best >= T ? "  CAPPED" : "");
        fflush(stdout);
    }
    return 0;
}
