/* fringe_uniqueness.c: which finite seeds share the single black cell's centre column? (helper of
 * rule30_cloud_fringe_uniqueness.py, which holds the predictions)
 *
 * BUILD:   cc -O2 -o fringe_uniqueness tests/probes/lexicon/fringe_uniqueness.c
 * USAGE:   ./fringe_uniqueness A w part nparts T [all]   direct: (white, 1, key) for keys of exact width w
 *          ./fringe_uniqueness B W part nparts D T [all] decrypt: every key of width <= W, 64 at a time
 * A key is the right half x_0(1 .. w), cell j + 1 in bit j. Mode A runs Rule 30 from (white, 1, key) and stops at the
 * first time its centre column leaves the single cell's (tau; T if never). It prints "S key" for every key lasting
 * all T steps, "T key tau" for every key if "all" is given, and finally "M maxtau argkey" over the rest.
 * Mode B decrypts the single cell's column under each key: Rule 30 is left-permutive, so the left half is the unique
 * plaintext. On diagonals e = j - s, diag[e][s] = diag[e][s-1] ^ (diag[e+1][s-1] | diag[e+2][s-1]); the left cell
 * x_0(-d) starts diagonal -d and enters x_d(0) = diag[-d][d] by XOR, so it is chosen to match column bit d. Bit lane
 * l of every word carries key base + l. It prints "S key first" for every key whose plaintext has no black at
 * depths D + 1 .. T - 1 (first = depth of the shallowest black, -1 if none), and "F key first" for every key if
 * "all" is given.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static long T;
static uint8_t *col;

static void single_column(void) {
    long n = 2 * T + 8, c = T + 4;
    uint8_t *a = calloc(n, 1), *b = calloc(n, 1);
    col = malloc(T);
    a[c] = 1;
    for (long t = 0; t < T; t++) {
        col[t] = a[c];
        for (long i = 1; i < n - 1; i++) b[i] = a[i - 1] ^ (a[i] | a[i + 1]);
        uint8_t *x = a; a = b; b = x;
    }
    free(a); free(b);
}

static void mode_a(int w, long part, long nparts, int all) {
    long n = 2 * T + 2 * w + 8, c = T + 4, best = -1, arg = 0;
    uint8_t *a = calloc(n, 1), *b = calloc(n, 1);
    for (long key = (1L << (w - 1)) + part; key < (1L << w); key += nparts) {
        a[c] = 1;                                         /* a and b are all white here (cleared below) */
        for (int j = 0; j < w; j++) a[c + 1 + j] = (key >> j) & 1;
        long lo = c - 1, hi = c + w + 1, t = 0;
        for (; t < T; t++) {
            if (a[c] != col[t]) break;
            for (long i = lo; i <= hi; i++) b[i] = a[i - 1] ^ (a[i] | a[i + 1]);
            lo--; hi++;
            uint8_t *x = a; a = b; b = x;
        }
        memset(a + lo - 1, 0, hi - lo + 3);               /* clear only the cells this key touched */
        memset(b + lo - 1, 0, hi - lo + 3);
        if (all) printf("T %ld %ld\n", key, t);
        if (t == T) printf("S %ld\n", key);
        else if (t > best) { best = t; arg = key; }
    }
    printf("M %ld %ld\n", best, arg);
}

static void mode_b(int W, long part, long nparts, long D, int all) {
    long ne = T + W + 3;
    uint64_t *dg = calloc(ne * T, 8);
#define DG(e, s) dg[((e) + T) * T + (s)]
    static const uint64_t P[6] = {0xAAAAAAAAAAAAAAAAULL, 0xCCCCCCCCCCCCCCCCULL, 0xF0F0F0F0F0F0F0F0ULL,
                                  0xFF00FF00FF00FF00ULL, 0xFFFF0000FFFF0000ULL, 0xFFFFFFFF00000000ULL};
    long *first = malloc(64 * sizeof(long));
    for (long g = part; g < (1L << (W - 6)); g += nparts) {
        long base = g << 6;          /* no clearing needed: every diagonal read below is first written in this group,
                                        and diagonals W + 1, W + 2 stay white from calloc */
        for (int e = W; e >= 1; e--) {
            int j = e - 1;
            DG(e, 0) = j < 6 ? P[j] : (((base >> j) & 1) ? ~0ULL : 0);
            for (long s = 1; s < T; s++) DG(e, s) = DG(e, s - 1) ^ (DG(e + 1, s - 1) | DG(e + 2, s - 1));
        }
        DG(0, 0) = ~0ULL;
        for (long s = 1; s < T; s++) DG(0, s) = DG(0, s - 1) ^ (DG(1, s - 1) | DG(2, s - 1));
        uint64_t any = 0, deep = 0;
        for (int l = 0; l < 64; l++) first[l] = -1;
        for (long d = 1; d < T; d++) {
            DG(-d, 0) = 0;
            for (long s = 1; s < T; s++) DG(-d, s) = DG(-d, s - 1) ^ (DG(-d + 1, s - 1) | DG(-d + 2, s - 1));
            uint64_t v = DG(-d, d) ^ (col[d] ? ~0ULL : 0);
            if (v) {
                for (long s = 0; s < T; s++) DG(-d, s) ^= v;
                uint64_t nw = v & ~any;
                any |= v;
                while (nw) { int l = __builtin_ctzll(nw); first[l] = d; nw &= nw - 1; }
                if (d > D) deep |= v;
            }
            if (!all && deep == ~0ULL) break;            /* every key of the group already has a deep black */
        }
        for (int l = 0; l < 64; l++) {
            if (all) printf("F %ld %ld\n", base + l, first[l]);
            if (!((deep >> l) & 1)) printf("S %ld %ld\n", base + l, first[l]);
        }
    }
}

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: see the header\n"); return 2; }
    char mode = argv[1][0];
    int w = atoi(argv[2]);
    long part = atol(argv[3]), nparts = atol(argv[4]);
    if (mode == 'A') {
        T = atol(argv[5]);
        single_column();
        mode_a(w, part, nparts, argc > 6);
    } else {
        long D = atol(argv[5]);
        T = atol(argv[6]);
        single_column();
        mode_b(w, part, nparts, D, argc > 7);
    }
    return 0;
}
