/* tilt.c: the centre column of Rule 30 over N steps, from a single black cell or from a random row.
 *
 * BUILD:   cc -O2 -o tilt tests/probes/lexicon/tilt.c      (driven by rule30_tilt.py)
 * USAGE:   ./tilt N MODE [SEED]     MODE 0: a single black cell; MODE 1: a row of fair coins (xorshift64*, SEED).
 *          Writes the N bits of column 0 (times 0 .. N-1) to stdout as the characters 0 and 1.
 * Cells are bits of a 64-bit word array, cell x at bit x + OFF. Each step updates only the cells that can still
 * influence column 0 by time N (a random row) or that the light cone has reached (a single cell), so the cost is
 * about N^2 / 64 word operations, and column 0 is exact: the array's edges are never within reach of it.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static uint64_t xs;
static uint64_t rnd(void) { xs ^= xs >> 12; xs ^= xs << 25; xs ^= xs >> 27; return xs * 0x2545F4914F6CDD1DULL; }

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: tilt N MODE [SEED]\n"); return 2; }
    long N = atol(argv[1]);
    int mode = atoi(argv[2]);
    xs = argc > 3 ? strtoull(argv[3], 0, 10) * 0x9E3779B97F4A7C15ULL + 1 : 88172645463325252ULL;
    long OFF = N + 128, BITS = 2 * N + 256, NWORD = BITS / 64 + 2;
    uint64_t *a = calloc(NWORD, 8), *b = calloc(NWORD, 8);
    if (!a || !b) return 3;
    if (mode == 0) a[OFF >> 6] |= 1ULL << (OFF & 63);
    else for (long w = 1; w < NWORD - 1; w++) a[w] = rnd();
    char *out = malloc(N + 1);
    for (long t = 0; t < N; t++) {
        out[t] = '0' + (int)((a[OFF >> 6] >> (OFF & 63)) & 1);
        long reach = mode == 0 ? t + 2 : N - t + 1;            /* cells that matter: |x| <= reach */
        long lo = (OFF - reach) / 64 - 1, hi = (OFF + reach) / 64 + 1;
        if (lo < 1) lo = 1;
        if (hi > NWORD - 2) hi = NWORD - 2;
        for (long w = lo; w <= hi; w++) {
            uint64_t c = a[w], l = (c << 1) | (a[w - 1] >> 63), r = (c >> 1) | (a[w + 1] << 63);
            b[w] = l ^ (c | r);                                   /* bit i: left neighbour is bit i - 1 */
        }
        if (mode == 1) { b[lo - 1] = 0; b[hi + 1] = 0; }
        uint64_t *s = a; a = b; b = s;
        if (mode == 1) { a[lo - 1] = 0; a[hi + 1] = 0; }
    }
    out[N] = 0;
    fwrite(out, 1, N, stdout);
    return 0;
}
