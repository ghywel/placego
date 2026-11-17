/* frames.c: Rule 30 from a single black cell, read along moving frames. For k = -K..K the frame of speed v = k / K
 * reads the cell at position floor(k t / K) at time t, t = 0 .. N-1 (v = 0 is the centre column, v = -1 and v = 1
 * the two edges of the light cone). Local, 2026-10-06; RULE30-PRIZE.md section 8.70 (the owner's temporal compass:
 * motion followed along a structure, not only change at a fixed cell); driver rule30_frames.py.
 *
 * BUILD:   cc -O3 -o frames tests/probes/lexicon/frames.c
 * USAGE:   ./frames N K      prints 2K + 1 lines, "k bits" (the bits as characters 0 and 1), k = -K..K.
 * Cells are bits of a 64-bit word array, cell x at bit x + OFF (tilt.c's layout: the left neighbour of bit i is bit
 * i - 1). Each step updates only the words the light cone has reached, so the cost is about N^2 / 64 word operations.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static long fl(long a, long b) { long q = a / b; if ((a % b) && ((a < 0) != (b < 0))) q--; return q; }

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: frames N K\n"); return 2; }
    long N = atol(argv[1]), K = atol(argv[2]);
    long OFF = N + 128, BITS = 2 * N + 256, NWORD = BITS / 64 + 2;
    uint64_t *a = calloc(NWORD, 8), *b = calloc(NWORD, 8);
    char **out = malloc((2 * K + 1) * sizeof(char *));
    for (long k = 0; k <= 2 * K; k++) out[k] = malloc(N + 1);
    if (!a || !b) return 3;
    a[OFF >> 6] |= 1ULL << (OFF & 63);
    for (long t = 0; t < N; t++) {
        for (long k = -K; k <= K; k++) {
            long x = fl(k * t, K) + OFF;
            out[k + K][t] = (char)('0' + (int)((a[x >> 6] >> (x & 63)) & 1));
        }
        long reach = t + 2, lo = (OFF - reach) / 64 - 1, hi = (OFF + reach) / 64 + 1;
        if (lo < 1) lo = 1;
        if (hi > NWORD - 2) hi = NWORD - 2;
        for (long w = lo; w <= hi; w++) {
            uint64_t c = a[w], l = (c << 1) | (a[w - 1] >> 63), r = (c >> 1) | (a[w + 1] << 63);
            b[w] = l ^ (c | r);
        }
        uint64_t *s = a; a = b; b = s;
    }
    for (long k = -K; k <= K; k++) { out[k + K][N] = 0; printf("%ld %s\n", k, out[k + K]); }
    return 0;
}
