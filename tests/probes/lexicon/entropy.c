/* entropy.c: the exact entropy of the visible language of column 1 next to column 0 = 0101..., for a layer of width m
 * fed any input (ladder.c's model). It bounds, rigorously, how much information column 1 can carry from any right side.
 *
 * BUILD:   cc -O2 -o entropy tests/probes/lexicon/entropy.c      (driven by rule30_entropy.py)
 * USAGE:   ./entropy M ITER [WORD [free]]
 *          column 0 = WORD repeated (default 01). Column 1 is visible only at times where column 0 is 0 (Lemma 1).
 *          prints "S M states", the number of reachable subset states of the deterministic automaton, and
 *          "E M lambda lower upper k", the growth factor per period of WORD from ITER rounds of power iteration (with
 *          the min and max componentwise ratios over the states still carrying weight), and k, the visible bits per
 *          period; the entropy per visible bit is log2(lambda) / k. With "free", column 0 is not clamped at all (both
 *          values allowed at every step, every time visible): the counterfactual, whose answer is 1 bit.
 *
 * The automaton. A state is the set of layer states (cells 1..M, cell i = bit i-1) consistent with the visible bits so
 * far, at an even time. Reading visible bit b: keep the states whose cell 1 is b, then step twice (once with column 0 =
 * 0, once with column 0 = 1), each time with either input bit in column M + 1. The number of visible words of length
 * n is the number of paths of length n from the start state (all 2^M states) through nonempty sets; its growth rate is
 * the spectral radius of the reachable part. The start group counts G(M, s) of ladder.c are these word counts.
 */
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int M, NS, WORDS, FREE;
static const char *WORD = "01";
static int *NXT;

static void build_layer(void) {
    NS = 1 << M;
    NXT = malloc(sizeof(int) * NS * 4);
    for (int s = 0; s < NS; s++)
        for (int tv = 0; tv < 2; tv++)
            for (int u = 0; u < 2; u++) {
                int out = 0;
                for (int i = 1; i <= M; i++) {
                    int l = (i == 1) ? tv : (s >> (i - 2)) & 1;
                    int c = (s >> (i - 1)) & 1;
                    int r = (i == M) ? u : (s >> i) & 1;
                    out |= (l ^ (c | r)) << (i - 1);
                }
                NXT[(s * 2 + tv) * 2 + u] = out;
            }
}

/* hash set of bitsets */
static uint64_t *SETS; static int *IDX; static size_t CAP, N;
static uint64_t hset(const uint64_t *b) {
    uint64_t h = 0x9E3779B97F4A7C15ULL;
    for (int w = 0; w < WORDS; w++) { h ^= b[w]; h *= 0xBF58476D1CE4E5B9ULL; h ^= h >> 29; }
    return h;
}
static int find_or_add(const uint64_t *b, int *added) {
    if (2 * (N + 1) > CAP) {
        size_t oc = CAP; int *oi = IDX;
        CAP = CAP ? CAP * 2 : 1 << 12;
        IDX = malloc(sizeof(int) * CAP);
        for (size_t i = 0; i < CAP; i++) IDX[i] = -1;
        SETS = realloc(SETS, sizeof(uint64_t) * WORDS * CAP / 2 + 64);
        for (size_t i = 0; i < oc; i++) if (oi && oi[i] >= 0) {
            size_t h = hset(SETS + (size_t)oi[i] * WORDS) & (CAP - 1);
            while (IDX[h] >= 0) h = (h + 1) & (CAP - 1);
            IDX[h] = oi[i];
        }
        free(oi);
    }
    size_t h = hset(b) & (CAP - 1);
    while (IDX[h] >= 0) {
        if (!memcmp(SETS + (size_t)IDX[h] * WORDS, b, 8 * WORDS)) { *added = 0; return IDX[h]; }
        h = (h + 1) & (CAP - 1);
    }
    memcpy(SETS + N * WORDS, b, 8 * WORDS);
    IDX[h] = (int)N; *added = 1;
    return (int)N++;
}

/* successors of a set over one period of WORD: leaves of the branching on visible bits */
static uint64_t **LEAF; static int NLEAF;
static void expand(const uint64_t *cur, int j, int len) {
    if (j == len) { memcpy(LEAF[NLEAF++], cur, 8 * WORDS); return; }
    uint64_t *nx = calloc(WORDS, 8);
    int tv0 = FREE ? 0 : WORD[j] - '0';
    if (FREE || tv0 == 0) {
        for (int bit = 0; bit < 2; bit++) {
            memset(nx, 0, 8 * WORDS);
            int any = 0;
            for (int w = 0; w < WORDS; w++) for (uint64_t v = cur[w]; v; v &= v - 1) {
                int s = w * 64 + __builtin_ctzll(v);
                if ((s & 1) != bit) continue;
                for (int tv = 0; tv < 2; tv++) {
                    if (!FREE && tv != tv0) continue;
                    for (int u = 0; u < 2; u++) { int s1 = NXT[(s * 2 + tv) * 2 + u]; nx[s1 >> 6] |= 1ULL << (s1 & 63); any = 1; }
                }
            }
            if (any) expand(nx, j + 1, len);
            else { memset(LEAF[NLEAF], 0, 8 * WORDS); NLEAF++; }   /* an empty leaf keeps the branch count fixed */
        }
    } else {
        int any = 0;
        for (int w = 0; w < WORDS; w++) for (uint64_t v = cur[w]; v; v &= v - 1) {
            int s = w * 64 + __builtin_ctzll(v);
            for (int u = 0; u < 2; u++) { int s1 = NXT[(s * 2 + 1) * 2 + u]; nx[s1 >> 6] |= 1ULL << (s1 & 63); any = 1; }
        }
        if (any) expand(nx, j + 1, len);
    }
    free(nx);
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: entropy M ITER [WORD [free]]\n"); return 2; }
    M = atoi(argv[1]);
    int iter = atoi(argv[2]);
    if (argc >= 4) WORD = argv[3];
    FREE = argc >= 5 && strcmp(argv[4], "free") == 0;
    build_layer();
    WORDS = (NS + 63) / 64;
    uint64_t *b = calloc(WORDS, 8), *x = calloc(WORDS, 8), *y = calloc(WORDS, 8);
    for (int s = 0; s < NS; s++) b[s >> 6] |= 1ULL << (s & 63);
    int added;
    find_or_add(b, &added);
    int len = FREE ? 1 : (int)strlen(WORD), k = 0;
    for (int q = 0; q < len; q++) k += FREE || WORD[q] == '0';
    int BR = 1 << k;                                  /* branches per period */
    LEAF = malloc(sizeof(uint64_t *) * BR);
    for (int q = 0; q < BR; q++) LEAF[q] = calloc(WORDS, 8);
    int *succ = NULL; size_t succcap = 0;          /* succ[BR*i + leaf] = index or -1 */
    for (size_t q = 0; q < N; q++) {
        NLEAF = 0;
        expand(SETS + q * WORDS, 0, len);
        if ((size_t)BR * (N + 1) > succcap) { succcap = (size_t)BR * (2 * N + 64); succ = realloc(succ, sizeof(int) * succcap); }
        for (int l = 0; l < BR; l++) {
            int any = 0;
            if (l < NLEAF) for (int w = 0; w < WORDS; w++) any |= LEAF[l][w] != 0;
            if (!any) { succ[(size_t)BR * q + l] = -1; continue; }
            int jj = find_or_add(LEAF[l], &added);
            if ((size_t)BR * (N + 1) > succcap) { succcap = (size_t)BR * (2 * N + 64); succ = realloc(succ, sizeof(int) * succcap); }
            succ[(size_t)BR * q + l] = jj;
        }
    }
    printf("S %d %zu\n", M, N);
    /* power iteration on word counts: v'(j) = sum over edges i -> j of v(i), starting from the start state */
    double *v = calloc(N, sizeof(double)), *w2 = calloc(N, sizeof(double));
    for (size_t i = 0; i < N; i++) v[i] = 1.0;     /* positive start: converges to the dominant eigenvalue */
    double lam = 0, lo = 0, hi = 0;
    for (int k = 0; k < iter; k++) {
        memset(w2, 0, sizeof(double) * N);
        for (size_t i = 0; i < N; i++) for (int l = 0; l < BR; l++) {
            int j = succ[(size_t)BR * i + l];
            if (j >= 0) w2[j] += v[i];
        }
        double s = 0, sv = 0; lo = INFINITY; hi = 0;
        for (size_t i = 0; i < N; i++) {
            s += w2[i]; sv += v[i];
            if (v[i] > 1e-300 && w2[i] > 0) { double r = w2[i] / v[i]; if (r < lo) lo = r; if (r > hi) hi = r; }
        }
        lam = s / sv;
        for (size_t i = 0; i < N; i++) v[i] = w2[i] / s;
    }
    printf("E %d %.9f %.9f %.9f %d\n", M, lam, lo, hi, k);
    return 0;
}
