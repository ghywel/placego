/* entropy2.c: entropy.c's automaton for column 0 = 0101..., with sparse subset states, so wider layers fit.
 *
 * BUILD:   cc -O2 -o entropy2 tests/probes/lexicon/entropy2.c -lm      (driven by rule30_entropy.py, deep2 mode)
 * USAGE:   ./entropy2 M ITER       prints "S M states meanpop" and "E M lambda"
 *
 * Same automaton as entropy.c (a state is the set of layer states consistent with the visible bits so far, at an
 * even time; reading visible bit b keeps the states whose cell 1 is b, then steps with column 0 = 0 and then 1, each
 * time with either input bit). Sets are stored as sorted arrays (they hold a few hundred layer states on average at
 * m = 18), and the layer's step is computed by bit operations rather than a table:
 *     next(s, tau, u) = (((s << 1) | tau) XOR (s OR ((s >> 1) | (u << (M - 1))))) AND (2^M - 1),
 * cell i being bit i - 1, so cell 1's left neighbour is column 0 and cell M's right neighbour is the input u.
 */
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int M;
static uint32_t MASK;
static inline uint32_t nxt(uint32_t s, uint32_t tv, uint32_t u) {
    return (((s << 1) | tv) ^ (s | ((s >> 1) | (u << (M - 1))))) & MASK;
}

static uint32_t *POOL; static size_t PCAP, PLEN;          /* all sets, back to back */
static size_t *OFF; static uint32_t *LEN; static size_t SCAP, N;
static int64_t *HT; static size_t HCAP;
static uint64_t hsh(const uint32_t *a, uint32_t n) {
    uint64_t h = 0x9E3779B97F4A7C15ULL ^ n;
    for (uint32_t i = 0; i < n; i++) { h ^= a[i]; h *= 0xBF58476D1CE4E5B9ULL; h ^= h >> 31; }
    return h;
}
static void rehash(void) {
    size_t nc = HCAP ? HCAP * 2 : 1 << 14;
    int64_t *nh = malloc(sizeof(int64_t) * nc);
    for (size_t i = 0; i < nc; i++) nh[i] = -1;
    for (size_t q = 0; q < N; q++) {
        size_t h = hsh(POOL + OFF[q], LEN[q]) & (nc - 1);
        while (nh[h] >= 0) h = (h + 1) & (nc - 1);
        nh[h] = (int64_t)q;
    }
    free(HT); HT = nh; HCAP = nc;
}
static int64_t find_or_add(const uint32_t *a, uint32_t n) {
    if (2 * (N + 1) > HCAP) rehash();
    size_t h = hsh(a, n) & (HCAP - 1);
    while (HT[h] >= 0) {
        size_t q = (size_t)HT[h];
        if (LEN[q] == n && !memcmp(POOL + OFF[q], a, 4 * (size_t)n)) return (int64_t)q;
        h = (h + 1) & (HCAP - 1);
    }
    if (N + 1 > SCAP) { SCAP = SCAP ? SCAP * 3 / 2 + 16 : 1024; OFF = realloc(OFF, sizeof(size_t) * SCAP); LEN = realloc(LEN, 4 * SCAP); }
    if (PLEN + n > PCAP) { PCAP = (PLEN + n) * 3 / 2 + (1 << 20); POOL = realloc(POOL, 4 * PCAP); }
    if (!POOL || !OFF || !LEN) { fprintf(stderr, "out of memory\n"); exit(3); }
    memcpy(POOL + PLEN, a, 4 * (size_t)n);
    OFF[N] = PLEN; LEN[N] = n; PLEN += n;
    HT[h] = (int64_t)N;
    return (int64_t)N++;
}

static int cmpu(const void *x, const void *y) {
    uint32_t a = *(const uint32_t *)x, b = *(const uint32_t *)y;
    return a < b ? -1 : a > b;
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: entropy2 M ITER\n"); return 2; }
    M = atoi(argv[1]);
    int iter = atoi(argv[2]);
    MASK = (M == 32) ? 0xFFFFFFFFu : ((1u << M) - 1);
    size_t NS = (size_t)1 << M;
    uint64_t *mark = calloc((NS + 63) / 64, 8);
    uint32_t *list1 = malloc(4 * NS), *list2 = malloc(4 * NS), *tmp = malloc(4 * NS);
    for (size_t s = 0; s < NS; s++) tmp[s] = (uint32_t)s;
    find_or_add(tmp, (uint32_t)NS);
    int64_t *succ = NULL; size_t succcap = 0;
    for (size_t q = 0; q < N; q++) {
        if (2 * (q + 1) > succcap) { succcap = 2 * (q + 1) * 2 + 64; succ = realloc(succ, sizeof(int64_t) * succcap); }
        for (int bit = 0; bit < 2; bit++) {
            size_t n1 = 0, n2 = 0;
            const uint32_t *cur = POOL + OFF[q];          /* POOL may move in find_or_add: re-read below */
            uint32_t len = LEN[q];
            for (uint32_t i = 0; i < len; i++) {
                uint32_t s = cur[i];
                if ((s & 1) != (uint32_t)bit) continue;
                for (uint32_t u = 0; u < 2; u++) {
                    uint32_t t = nxt(s, 0, u);
                    if (!(mark[t >> 6] >> (t & 63) & 1)) { mark[t >> 6] |= 1ULL << (t & 63); list1[n1++] = t; }
                }
            }
            for (size_t i = 0; i < n1; i++) mark[list1[i] >> 6] &= ~(1ULL << (list1[i] & 63));
            for (size_t i = 0; i < n1; i++)
                for (uint32_t u = 0; u < 2; u++) {
                    uint32_t t = nxt(list1[i], 1, u);
                    if (!(mark[t >> 6] >> (t & 63) & 1)) { mark[t >> 6] |= 1ULL << (t & 63); list2[n2++] = t; }
                }
            for (size_t i = 0; i < n2; i++) mark[list2[i] >> 6] &= ~(1ULL << (list2[i] & 63));
            if (!n2) { succ[2 * q + bit] = -1; continue; }
            qsort(list2, n2, 4, cmpu);
            succ[2 * q + bit] = find_or_add(list2, (uint32_t)n2);
        }
    }
    double pop = 0;
    for (size_t q = 1; q < N; q++) pop += LEN[q];
    printf("S %d %zu %.1f\n", M, N, N > 1 ? pop / (double)(N - 1) : 0.0);
    double *v = malloc(sizeof(double) * N), *w = malloc(sizeof(double) * N);
    for (size_t i = 0; i < N; i++) v[i] = 1.0;
    double lam = 0;
    for (int k = 0; k < iter; k++) {
        memset(w, 0, sizeof(double) * N);
        for (size_t i = 0; i < N; i++) for (int bit = 0; bit < 2; bit++) {
            int64_t j = succ[2 * i + bit];
            if (j >= 0) w[j] += v[i];
        }
        double s = 0, sv = 0;
        for (size_t i = 0; i < N; i++) { s += w[i]; sv += v[i]; }
        lam = s / sv;
        for (size_t i = 0; i < N; i++) v[i] = w[i] / s;
    }
    printf("E %d %.9f\n", M, lam);
    return 0;
}
