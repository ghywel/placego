/* bottleneck.c: how much of a right half's information has reached column 1 by time t?
 *
 * BUILD:   cc -O2 -o bottleneck tests/probes/lexicon/bottleneck.c      (driven by rule30_bottleneck.py)
 * USAGE:   ./bottleneck W T t1 t2 ...    for every right half of at most W cells (cells 1..W, column 0 clamped to
 *                                        0101...), the number of distinct visible histories of column 1 (its bits at
 *                                        even times below t), for each checkpoint t <= T (T <= 512, t even)
 *          prints "I W t distinct"
 *
 * Column 1 at odd times never reaches the left side (Lemma 1), so the visible history is what the left side can see.
 * Two right halves with the same visible history up to t force the same left half to depth t (Lemma 4). The count is
 * exact up to collisions of a 128-bit hash, which at a few million histories are negligible.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct { uint64_t a, b; } h128;

static int cmp(const void *x, const void *y) {
    const h128 *p = x, *q = y;
    if (p->a != q->a) return p->a < q->a ? -1 : 1;
    if (p->b != q->b) return p->b < q->b ? -1 : 1;
    return 0;
}

static h128 hash_bits(const uint64_t *vb, int nbits) {
    uint64_t a = 0x243F6A8885A308D3ULL ^ (uint64_t)nbits, b = 0x13198A2E03707344ULL + (uint64_t)nbits;
    int nw = (nbits + 63) / 64;
    for (int i = 0; i < nw; i++) {
        uint64_t w = vb[i];
        if (i == nw - 1 && nbits % 64) w &= (1ULL << (nbits % 64)) - 1;
        a ^= w; a *= 0x9E3779B97F4A7C15ULL; a ^= a >> 29;
        b += w * 0xC2B2AE3D27D4EB4FULL; b ^= b >> 31; b *= 0x165667B19E3779F9ULL;
    }
    h128 h = { a, b };
    return h;
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: bottleneck W T t1 t2 ...\n"); return 2; }
    int W = atoi(argv[1]), T = atoi(argv[2]), nc = argc - 3;
    int *ck = malloc(sizeof(int) * nc);
    for (int i = 0; i < nc; i++) ck[i] = atoi(argv[3 + i]);
    if (T > 512 || W > 26) { fprintf(stderr, "T <= 512 and W <= 26\n"); return 2; }
    int NW = (W + T + 66) / 64;
    uint64_t n = (1ULL << W) - 1;
    h128 *H = malloc(sizeof(h128) * n * nc);
    if (!H) { fprintf(stderr, "out of memory\n"); return 3; }
    uint64_t *row = malloc(8 * NW), *nr = malloc(8 * NW);
    for (uint64_t R = 1; R <= n; R++) {
        memset(row, 0, 8 * NW);
        row[0] = R << 1;                         /* bit 0 = column 0 = tau(0) = 0; bit i = cell i */
        if (W >= 63) row[1] = R >> 63;
        uint64_t vb[4] = { 0, 0, 0, 0 };
        int c = 0;
        for (int t = 0; t < T && c < nc; t++) {
            if (t % 2 == 0) { int j = t / 2; vb[j >> 6] |= ((row[0] >> 1) & 1ULL) << (j & 63); }
            /* x'(i) = x(i-1) XOR (x(i) OR x(i+1)); bit i-1 is the left neighbour of bit i */
            for (int k = 0; k < NW; k++) {
                uint64_t L = (row[k] << 1) | (k ? row[k - 1] >> 63 : 0);
                uint64_t Rt = (row[k] >> 1) | (k + 1 < NW ? row[k + 1] << 63 : 0);
                nr[k] = L ^ (row[k] | Rt);
            }
            nr[0] = (nr[0] & ~1ULL) | (uint64_t)((t + 1) & 1);      /* clamp column 0 to tau(t+1) */
            uint64_t *tmp = row; row = nr; nr = tmp;
            while (c < nc && ck[c] == t + 1) { H[(uint64_t)c * n + (R - 1)] = hash_bits(vb, (t + 2) / 2); c++; }
        }
    }
    for (int c = 0; c < nc; c++) {
        h128 *a = H + (uint64_t)c * n;
        qsort(a, n, sizeof(h128), cmp);
        uint64_t d = n ? 1 : 0;
        for (uint64_t i = 1; i < n; i++) d += cmp(a + i - 1, a + i) != 0;
        printf("I %d %d %llu\n", W, ck[c], (unsigned long long)d);
    }
    return 0;
}
