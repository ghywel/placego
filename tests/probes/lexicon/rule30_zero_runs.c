/* rule30_zero_runs.c: ZR, the zero runs of Rule 30's forced left half after a black cell at depth j (row Q1; Local's
 * claim of 2026-10-07 22:20 BST in CLOUD-LOCAL.md, predictions pushed before the run; the outcome is in the header of
 * rule30_zero_runs.py, which builds and runs this file).
 *
 * Column 0 follows the word (t + ph) mod 2, ph = 0 or 1. Fix the right part, cells 0 .. J at time 0, with cell 0 =
 * ph. By left permutivity x_t(0) = x_0(-t) XOR g_t(cells -t+1 .. t), so each depth t names one value f_t of cell -t
 * that meets the condition at time t: the forced left half (L225). This program computes f_1 .. f_J for every right
 * part and both phases, 64 right parts per machine word (bit-sliced), and counts, for each j and k,
 *     N(j, k) = #{(right part, ph) : f_j = 1 and f_(j+1) = .. = f_(j+k) = 0}.
 * N(j, 0) / (2 * 2^J) is L224's rho_j, and N(j, k) / N(j, k - 1) is the k-th step of the white run after the black
 * cell at depth j. Width-free: a finite hull of width w >= 2(j + k) + 2 gives the same ratios (L224, L225).
 *
 * usage: rule30_zero_runs J KMAX   (prints "TOTAL t", then "R d L open|closed" for the longest white run of forced
 *        cells starting at depth d over every right part (open if it reaches depth J), then "N j k count" lines)
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define MAXJ 30

static const uint64_t PAT[6] = {0xAAAAAAAAAAAAAAAAULL, 0xCCCCCCCCCCCCCCCCULL, 0xF0F0F0F0F0F0F0F0ULL,
                                0xFF00FF00FF00FF00ULL, 0xFFFF0000FFFF0000ULL, 0xFFFFFFFF00000000ULL};

/* x_t(0) from row 0 cells c[-t .. t] (c is centred: c[i] is cell i) */
static uint64_t centre(const uint64_t *c, int t) {
    uint64_t row[2 * MAXJ + 3], nxt[2 * MAXJ + 3];
    for (int i = -t; i <= t; i++) row[i + t] = c[i];
    for (int s = 1; s <= t; s++) {
        for (int i = -t + s; i <= t - s; i++) nxt[i + t] = row[i - 1 + t] ^ (row[i + t] | row[i + 1 + t]);
        for (int i = -t + s; i <= t - s; i++) row[i + t] = nxt[i + t];
    }
    return row[t];
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s J KMAX\n", argv[0]); return 2; }
    int J = atoi(argv[1]), K = atoi(argv[2]);
    if (J < 7 || J > MAXJ || K < 0 || K >= J) { fprintf(stderr, "need 7 <= J <= %d, 0 <= KMAX < J\n", MAXJ); return 2; }
    static unsigned long long N[MAXJ + 1][MAXJ + 1];
    int Rr[MAXJ + 2] = {0};                         /* longest white run of forced cells starting at depth d */
    uint64_t words = 1ULL << (J - 6);
    for (int ph = 0; ph < 2; ph++) {
        for (uint64_t w = 0; w < words; w++) {
            uint64_t store[2 * MAXJ + 3] = {0}, *c = store + MAXJ + 1, f[MAXJ + 1];
            c[0] = ph ? ~0ULL : 0;
            for (int i = 1; i <= J; i++) c[i] = i <= 6 ? PAT[i - 1] : (((w >> (i - 7)) & 1) ? ~0ULL : 0);
            for (int t = 1; t <= J; t++) {
                c[-t] = 0;
                uint64_t v = centre(c, t), word = ((t + ph) & 1) ? ~0ULL : 0;
                f[t] = v ^ word;                     /* the value of cell -t that meets the condition at time t */
                c[-t] = f[t];
            }
            for (int d = 1; d <= J; d++) {
                uint64_t white = ~0ULL;
                for (int t = d; t <= J; t++) {
                    white &= ~f[t];
                    if (!white) break;
                    if (t - d + 1 > Rr[d]) Rr[d] = t - d + 1;
                }
            }
            for (int j = 1; j <= J; j++) {
                uint64_t alive = f[j];
                N[j][0] += __builtin_popcountll(alive);
                for (int k = 1; k <= K && j + k <= J; k++) {
                    alive &= ~f[j + k];
                    N[j][k] += __builtin_popcountll(alive);
                }
            }
        }
    }
    printf("TOTAL %llu\n", 2ULL << J);
    for (int d = 1; d <= J; d++) printf("R %d %d %s\n", d, Rr[d], Rr[d] == J - d + 1 ? "open" : "closed");
    for (int j = 1; j <= J; j++)
        for (int k = 0; k <= K && j + k <= J; k++) printf("N %d %d %llu\n", j, k, N[j][k]);
    return 0;
}
