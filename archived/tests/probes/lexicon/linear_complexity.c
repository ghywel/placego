/* linear_complexity.c: the linear complexity profile of a bit sequence (Berlekamp-Massey over GF(2), bit-packed), the
 * biases of its lag differences and of its time derivatives, and a ring generator for the counterfactual arm.
 * Local, 2026-10-06; RULE30-PRIZE.md section 8.70; CONSTELLATION.md row 17; driver rule30_linear_complexity.py.
 *
 * BUILD:   cc -O3 -o linear_complexity tests/probes/lexicon/linear_complexity.c
 * USAGE:   ./linear_complexity bm          stdin: the bits as the characters 0 and 1 (tilt.c's output). Prints
 *                                          "J n L" each time the linear complexity changes (L is the complexity of the
 *                                          first n bits) and "END N L" at the end.
 *          ./linear_complexity diff K J    stdin as above. Prints "LAG k ones len" for the lag differences
 *                                          x(t) XOR x(t+k), k = 1..K, and "DIFF j ones len" for the j-th time
 *                                          derivative (1 + S)^j x, j = 1..J (over GF(2): x(t) + x(t+1) taken j times).
 *          ./linear_complexity ring n N    the cell 0 of Rule 30 on the ring of n <= 63 cells from the single cell 1,
 *                                          N steps (ring_census.c's step), as characters.
 *
 * Berlekamp-Massey. C(z) = 1 + c_1 z + ... + c_L z^L is the shortest connection polynomial so far; the discrepancy at
 * bit n is s_n + sum_i c_i s_{n-i}. The sequence is stored reversed (r_k = s_{N-1-k}) so that the sum is the parity of
 * C AND a 64-bit window of r starting at N - 1 - n. Cost about N^2 / 128 word operations.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static unsigned char *read_bits(long *n_out) {
    long cap = 1 << 20, n = 0;
    unsigned char *s = malloc(cap);
    int c;
    while ((c = getchar()) != EOF) {
        if (c != '0' && c != '1') continue;
        if (n == cap) { cap *= 2; s = realloc(s, cap); }
        s[n++] = (unsigned char)(c - '0');
    }
    *n_out = n;
    return s;
}

static void bm(const unsigned char *s, long N) {
    long W = N / 64 + 6;
    uint64_t *R = calloc(W, 8), *C = calloc(W, 8), *B = calloc(W, 8), *T = calloc(W, 8);
    for (long k = 0; k < N; k++) if (s[N - 1 - k]) R[k >> 6] |= 1ULL << (k & 63);
    C[0] = 1; B[0] = 1;
    long L = 0, m = -1, LB = 0;
    for (long n = 0; n < N; n++) {
        long off = N - 1 - n, cw = (L >> 6) + 1;
        uint64_t acc = 0;
        for (long w = 0; w < cw; w++) {
            long p = off + 64 * w, q = p >> 6;
            int sh = (int)(p & 63);
            uint64_t v = R[q] >> sh;
            if (sh) v |= R[q + 1] << (64 - sh);
            acc ^= C[w] & v;
        }
        if (!__builtin_parityll(acc)) continue;
        int grow = 2 * L <= n;
        if (grow) memcpy(T, C, 8 * (size_t)cw);              /* the old C becomes the new B */
        long k = n - m, ks = k >> 6, bw = (LB >> 6) + 1;
        int kb = (int)(k & 63);
        for (long j = 0; j < bw; j++) {
            uint64_t b = B[j];
            C[j + ks] ^= b << kb;
            if (kb) C[j + ks + 1] ^= b >> (64 - kb);
        }
        if (grow) {
            LB = L; L = n + 1 - L; m = n;
            uint64_t *t = B; B = T; T = t;
            printf("J %ld %ld\n", n + 1, L);
        }
    }
    printf("END %ld %ld\n", N, L);
    free(R); free(C); free(B); free(T);
}

static void diffs(const unsigned char *s, long N, long K, long J) {
    for (long k = 1; k <= K && k < N; k++) {
        long ones = 0;
        for (long t = 0; t + k < N; t++) ones += s[t] ^ s[t + k];
        printf("LAG %ld %ld %ld\n", k, ones, N - k);
    }
    unsigned char *y = malloc(N);
    memcpy(y, s, N);
    long len = N;
    for (long j = 1; j <= J && len > 1; j++) {
        len--;
        long ones = 0;
        for (long t = 0; t < len; t++) { y[t] ^= y[t + 1]; ones += y[t]; }
        printf("DIFF %ld %ld %ld\n", j, ones, len);
    }
    free(y);
}

static void ring(int n, long N) {
    uint64_t mask = (1ULL << n) - 1, x = 1;
    char *out = malloc(N + 1);
    for (long t = 0; t < N; t++) {
        out[t] = (char)('0' + (int)(x & 1));
        uint64_t l = ((x << 1) | (x >> (n - 1))) & mask, r = ((x >> 1) | (x << (n - 1))) & mask;
        x = (l ^ (x | r)) & mask;
    }
    fwrite(out, 1, N, stdout);
    free(out);
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: linear_complexity bm | diff K J | ring n N\n"); return 2; }
    if (!strcmp(argv[1], "ring")) { ring(atoi(argv[2]), atol(argv[3])); return 0; }
    long N;
    unsigned char *s = read_bits(&N);
    if (!strcmp(argv[1], "bm")) bm(s, N);
    else if (!strcmp(argv[1], "diff")) diffs(s, N, atol(argv[2]), atol(argv[3]));
    else return 2;
    free(s);
    return 0;
}
