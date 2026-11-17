// leftside_dump.c: list every left seed of width W whose survival time beside a periodic wall is at least THRESH.
// Local, 2026-10-13; RULE30-PRIZE.md 8.94 (the 13-tick jumps); driver rule30_leftside_jump.py. Same survive() and seed
// encoding as leftside_horizon.c (frozen): bit k = cell -(k+1); cell -W black.
// Usage: leftside_dump WORD W PHASE THRESH [T=90] [THREADS]      Output: D W phase h seedhex
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _OPENMP
#include <omp.h>
#endif
typedef unsigned __int128 u128;

static char WORD[64]; static int P, T;

static int survive(u128 x, int phase) {               /* copied verbatim from leftside_horizon.c */
    int prev = 0, in_white = 0;
    for (int t = 0; t < T; t++) {
        int tau = WORD[(phase + t) % P] - '0', tau1 = WORD[(phase + t + 1) % P] - '0';
        int c = (int)(x & 1);
        if (tau) {
            if (c != !tau1) return t;
            in_white = 0;
        } else {
            int sigma = tau1 ^ c;
            if (in_white && sigma < prev) return t;
            prev = sigma; in_white = 1;
        }
        x = (x >> 1) ^ (x | ((x << 1) | (u128)tau));
    }
    return T;
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: leftside_dump WORD W PHASE THRESH [T] [THREADS]\n"); return 2; }
    strncpy(WORD, argv[1], 63); P = (int)strlen(WORD);
    int W = atoi(argv[2]), phase = atoi(argv[3]), th = atoi(argv[4]); T = argc > 5 ? atoi(argv[5]) : 90;
#ifdef _OPENMP
    if (argc > 6) omp_set_num_threads(atoi(argv[6]));
#endif
    if (W < 1 || W > 62 || W + T > 128) { fprintf(stderr, "need 1 <= W <= 62 and W + T <= 128\n"); return 2; }
    uint64_t lo = (uint64_t)1 << (W - 1), hi = (uint64_t)1 << W;
#pragma omp parallel for schedule(static)
    for (uint64_t s = lo; s < hi; s++) {
        int h = survive((u128)s, phase);
        if (h >= th) {
#pragma omp critical
            { printf("D %d %d %d %llx\n", W, phase, h, (unsigned long long)s); fflush(stdout); }
        }
    }
    return 0;
}
