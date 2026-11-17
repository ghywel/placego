/* rule30_silent_sources.c: SS, which edge events E_j of the forced left half can fire at time 0 (row Q6; CL054's ask (a),
 * Local's weigh-in L308; predictions in rule30_silent_sources.py, pushed before the run).
 *
 * Column 0 follows (t + ph) mod 2. Fix the right part, cells 0 .. J at time 0 with cell 0 = ph. As in ZR
 * (rule30_zero_runs.c), left permutivity names the forced cell f_t = x_0(-t) for t = 1 .. J. CL046's edge event is
 * E_j(t) = x_t(-j+2) AND NOT x_t(-j+1); at time 0 this is f_(j-2) AND NOT f_(j-1) for j >= 2 (with f_0 = ph), and
 * E_1(0) = x_0(1) AND NOT ph. The program counts, for every j <= J + 1 and each phase, the right parts (64 per machine
 * word, bit-sliced) with E_j(0) = 1. A zero count means E_j is silent at time 0 for EVERY right half in that phase,
 * hence silent at every later time too (a later row is again some right half), i.e. silent for every configuration
 * whose column 0 follows 0101 long enough.
 *
 * usage: rule30_silent_sources J     prints "E j ph count" for j = 1 .. J + 1, ph = 0, 1
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define MAXJ 40

static const uint64_t PAT[6] = {0xAAAAAAAAAAAAAAAAULL, 0xCCCCCCCCCCCCCCCCULL, 0xF0F0F0F0F0F0F0F0ULL,
                                0xFF00FF00FF00FF00ULL, 0xFFFF0000FFFF0000ULL, 0xFFFFFFFF00000000ULL};

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
    if (argc < 2) { fprintf(stderr, "usage: %s J\n", argv[0]); return 2; }
    int J = atoi(argv[1]);
    if (J < 7 || J > MAXJ) { fprintf(stderr, "need 7 <= J <= %d\n", MAXJ); return 2; }
    static unsigned long long E[2][MAXJ + 3];
    uint64_t words = 1ULL << (J - 6);
    #pragma omp parallel
    {
    unsigned long long El[2][MAXJ + 3] = {{0}};
    for (int ph = 0; ph < 2; ph++) {
        #pragma omp for schedule(dynamic, 4096)
        for (uint64_t w = 0; w < words; w++) {
            uint64_t store[2 * MAXJ + 3] = {0}, *c = store + MAXJ + 1, f[MAXJ + 1];
            c[0] = ph ? ~0ULL : 0;
            for (int i = 1; i <= J; i++) c[i] = i <= 6 ? PAT[i - 1] : (((w >> (i - 7)) & 1) ? ~0ULL : 0);
            f[0] = c[0];
            for (int t = 1; t <= J; t++) {
                c[-t] = 0;
                uint64_t v = centre(c, t), word = ((t + ph) & 1) ? ~0ULL : 0;
                f[t] = v ^ word;
                c[-t] = f[t];
            }
            El[ph][1] += __builtin_popcountll(c[1] & ~c[0]);
            for (int j = 2; j <= J + 1; j++) El[ph][j] += __builtin_popcountll(f[j - 2] & ~f[j - 1]);
        }
    }
    #pragma omp critical
    {
        for (int p = 0; p < 2; p++) for (int j = 0; j <= MAXJ + 2; j++) E[p][j] += El[p][j];
    }
    }
    for (int j = 1; j <= J + 1; j++)
        for (int ph = 0; ph < 2; ph++) printf("E %d %d %llu\n", j, ph, E[ph][j]);
    return 0;
}
