/* races.c: Rule 30 with rare race conditions. A synchronous run and a "fuzzy" run start from the same fair row on a
 * ring of W cells. In the fuzzy run each cell, with probability EPS per step, reads one neighbour's NEW value (the
 * neighbour finished first) instead of its old one: MODE L reads the left neighbour (sweep left to right), MODE R the
 * right neighbour (sweep right to left). Local, 2026-10-06; CONSTELLATION row 19 (the owner's question: an await that
 * is almost always kept, with a little fuzz at the last moment); driver rule30_races.py.
 *
 * BUILD:   cc -O3 -o races tests/probes/lexicon/races.c -lm
 * USAGE:   ./races W T EPS MODE SEED CHECKS    MODE is L or R; prints "INJ races injected" for the first step (how many
 *          races changed the cell against the synchronous value), then "F t differing" at CHECKS times spread over
 *          1..T, and at the end "D density" (the fuzzy row's density of black) and "P pairs01" (its fraction of
 *          unequal neighbours).
 */
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static uint64_t s;
static uint64_t rnd(void) { s ^= s >> 12; s ^= s << 25; s ^= s >> 27; return s * 0x2545F4914F6CDD1DULL; }
static double unif(void) { return ((rnd() >> 11) + 0.5) * (1.0 / 9007199254740992.0); }

int main(int argc, char **argv) {
    if (argc < 7) { fprintf(stderr, "usage: races W T EPS MODE SEED CHECKS\n"); return 2; }
    long W = atol(argv[1]), T = atol(argv[2]), CH = atol(argv[6]);
    double eps = atof(argv[3]);
    char mode = argv[4][0];
    s = strtoull(argv[5], 0, 10) * 0x9E3779B97F4A7C15ULL + 12345;
    unsigned char *a = malloc(W), *a2 = malloc(W), *b = malloc(W), *b2 = malloc(W), *race = calloc(W, 1);
    for (long i = 0; i < W; i++) a[i] = b[i] = (unsigned char)(rnd() >> 63);
    double lq = eps > 0 ? log(1.0 - eps) : 0;
    long next_check = 1, ci = 1;
    for (long t = 1; t <= T; t++) {
        /* synchronous */
        for (long i = 0; i < W; i++) {
            unsigned char l = a[(i + W - 1) % W], c = a[i], r = a[(i + 1) % W];
            a2[i] = l ^ (c | r);
        }
        /* races this step: geometric gaps */
        memset(race, 0, W);
        long nr = 0;
        if (eps > 0) {
            long pos = (long)floor(log(unif()) / lq);
            while (pos < W) { race[pos] = 1; nr++; pos += 1 + (long)floor(log(unif()) / lq); }
        }
        long inj = 0;
        if (mode == 'L') {
            for (long i = 0; i < W; i++) {
                int rc = race[i] && i > 0;
                unsigned char l = rc ? b2[i - 1] : b[(i + W - 1) % W], c = b[i], r = b[(i + 1) % W];
                b2[i] = l ^ (c | r);
                if (rc && t == 1) inj += b2[i] != (unsigned char)(b[i - 1] ^ (c | r));
            }
        } else {
            for (long i = W - 1; i >= 0; i--) {
                int rc = race[i] && i < W - 1;
                unsigned char l = b[(i + W - 1) % W], c = b[i], r = rc ? b2[i + 1] : b[(i + 1) % W];
                b2[i] = l ^ (c | r);
                if (rc && t == 1) inj += b2[i] != (unsigned char)(l ^ (c | b[i + 1]));
            }
        }
        if (t == 1) printf("INJ %ld %ld\n", nr, inj);
        unsigned char *x = a; a = a2; a2 = x; x = b; b = b2; b2 = x;
        if (t == next_check || t == T) {
            long d = 0;
            for (long i = 0; i < W; i++) d += a[i] != b[i];
            printf("F %ld %ld\n", t, d);
            ci++;
            next_check = (long)ceil((double)T * ci / CH);
            if (next_check <= t) next_check = t + 1;     /* when T < CHECKS the schedule must still advance */
        }
    }
    long ones = 0, un = 0;
    for (long i = 0; i < W; i++) { ones += b[i]; un += b[i] != b[(i + 1) % W]; }
    printf("D %.6f\nP %.6f\n", (double)ones / W, (double)un / W);
    return 0;
}
