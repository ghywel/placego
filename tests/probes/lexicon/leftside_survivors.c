// leftside_survivors.c: the survival-time distribution of every finite left seed beside a periodic wall. Local,
// 2026-10-13; RULE30-PRIZE.md 8.94 (planned); driver rule30_leftside_survivors.py.
//
// A variant of leftside_horizon.c (section 8.69), which stays frozen: the same autonomous left half, the same two
// conditions on column -1 that no right half can lift, the same seed encoding (bit k = cell -(k+1); seeds of width W
// have cell -W black). Where leftside_horizon prints only the best survival time H_L(W), this prints, for each width
// and phase, how many seeds survive exactly h observations, so that the survivor curve N_W(t) = #(h >= t) can be read:
// exact halving while each condition's fresh cell lies inside the seed, then whatever the post-fresh phase does.
//
// Usage: leftside_survivors WORD WMIN WMAX [T=90] [THREADS]        (W + T <= 128)
// Output: one line per width and phase:  S WORD W phase : h0 count0, h1 count1, ...   (nonzero counts only)
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
    if (argc < 4) { fprintf(stderr, "usage: leftside_survivors WORD WMIN WMAX [T] [THREADS]\n"); return 2; }
    strncpy(WORD, argv[1], 63); P = (int)strlen(WORD);
    int wmin = atoi(argv[2]), wmax = atoi(argv[3]); T = argc > 4 ? atoi(argv[4]) : 90;
#ifdef _OPENMP
    if (argc > 5) omp_set_num_threads(atoi(argv[5]));
#endif
    if (wmax + T > 128 || wmax > 62) { fprintf(stderr, "W + T must be at most 128 and W at most 62\n"); return 2; }
    for (int W = wmin; W <= wmax; W++) {
        uint64_t lo = W ? (uint64_t)1 << (W - 1) : 0, hi = W ? (uint64_t)1 << W : 1;
        for (int phase = 0; phase < P; phase++) {
            uint64_t *hist = calloc((size_t)T + 1, sizeof(uint64_t));
#pragma omp parallel
            {
                uint64_t *loc = calloc((size_t)T + 1, sizeof(uint64_t));
#pragma omp for schedule(static)
                for (uint64_t s = lo; s < hi; s++) loc[survive((u128)s, phase)]++;
#pragma omp critical
                for (int h = 0; h <= T; h++) hist[h] += loc[h];
                free(loc);
            }
            printf("S %s %d %d :", WORD, W, phase);
            for (int h = 0; h <= T; h++) if (hist[h]) printf(" %d %llu,", h, (unsigned long long)hist[h]);
            printf("\n"); fflush(stdout);
            free(hist);
        }
    }
    return 0;
}
