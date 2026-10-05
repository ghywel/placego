/* count.c: exact counts of finite Rule 30 configurations whose column 0 follows a word (rule30_count.py).
 * Usage: count WMIN WMAX TMAX WORD   (WORD: a string of 0/1 of length >= TMAX + period, read cyclically by phase)
 *        count WMIN WMAX TMAX WORD P (P: the word's period; every rotation 0 .. P-1 is a phase)
 * Every pattern of exact hull width w (first and last cell black) is run once; every cell of its hull is tried as
 * column 0. For each phase, time t >= 1 is a "black" condition when the word's cell at t-1 is 1, else "white".
 * Output lines: C w T N_both N_black N_white N_neither, summed over phases and column-0 positions, where a game's
 * count holds the (pattern, position, phase) triples that meet the word at time 0 and at every condition of that
 * game up to time T - 1. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned __int128 u128;
static long long cnt[64][130][4], neither[64];
int main(int argc, char **argv) {
    int wmin = atoi(argv[1]), wmax = atoi(argv[2]), tmax = atoi(argv[3]);
    const char *word = argv[4];
    int per = argc > 5 ? atoi(argv[5]) : 1;
    memset(cnt, 0, sizeof cnt);
    memset(neither, 0, sizeof neither);
    for (int w = wmin; w <= wmax; w++) {
        int base = 64 - w / 2;
        unsigned long long npat = w == 1 ? 1ULL : 1ULL << (w - 2);
        unsigned int full = w >= 32 ? 0xffffffffu : ((1u << w) - 1u);
        for (unsigned long long q = 0; q < npat; q++) {
            unsigned long long pat = w == 1 ? 1ULL : (1ULL | (q << 1) | (1ULL << (w - 1)));
            for (int ph = 0; ph < per; ph++) {
                u128 x = (u128)pat << base;
                unsigned int a[4];
                for (int g = 0; g < 4; g++) a[g] = full;
                for (int t = 0; t < tmax; t++) {
                    unsigned int m = (unsigned int)(x >> base) & full;
                    int e = word[ph + t] == '1';
                    unsigned int ok = e ? m : (~m & full);
                    if (t == 0) { for (int g = 0; g < 4; g++) a[g] &= ok; }
                    else {
                        int prev = word[ph + t - 1] == '1';
                        a[0] &= ok;
                        if (prev) a[1] &= ok; else a[2] &= ok;
                    }
                    for (int g = 0; g < 3; g++) cnt[w][t + 1][g] += __builtin_popcount(a[g]);
                    if (t == 0) neither[w] += __builtin_popcount(a[3]);   /* neither: time 0 only, constant in T */
                    if (!a[0] && !a[1] && !a[2]) break;
                    x = (x << 1) ^ (x | (x >> 1));
                }
            }
        }
        for (int t = 1; t <= tmax; t++)
            printf("C %d %d %lld %lld %lld %lld\n", w, t, cnt[w][t][0], cnt[w][t][1], cnt[w][t][2], neither[w]);
        fflush(stdout);
    }
    return 0;
}
