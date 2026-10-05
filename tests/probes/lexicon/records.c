/* records.c: the longest zero run of the forced left half from depth d, over EVERY column 1, for column 0 = 0101...
 * (Conjecture LR for the word 01; RULE30-PRIZE.md sections 7 and 8.14, lead 1 of 2026-10-05).
 *
 * BUILD:   cc -O2 -fopenmp -o records tests/probes/lexicon/records.c      (driven by rule30_records.py)
 * USAGE:   ./records D [THREADS] [SPLIT]
 *          prints "R D best count" (the longest run of zero cells d, d+1, ... forced by some column 1, and how many
 *          of the 2^n prefixes of column 1 before depth d reach it), "H D r count" for the histogram of each prefix's
 *          own longest run, and "W D e" for up to 64 record witnesses: column 1's visible bits (times 0, 2, 4, ...)
 *          up to the end of the run. SPLIT (default 12) is the number of leading free bits enumerated as parallel
 *          tasks.
 *
 * The forced left half. Column 0 is tau(t) = t mod 2, column 1 is c(t); Rule 30 solved for the left parent,
 * x_t(i-1) = x_{t+1}(i) XOR (x_t(i) OR x_t(i+1)), gives every cell to the left. Index by anti-diagonals: A_k[j] =
 * x_{k-j}(-j), j = 0 .. k, so A_k[0] = tau(k) and A_k[k] = x_0(-k), the cell at depth k of the forced row at time 0.
 * The recurrence becomes
 *     A_k[j] = A_k[j-1] XOR (A_{k-1}[j-1] OR A_{k-2}[j-2]),  j >= 1,  with A_{k-2}[-1] = c(k-1),
 * a running XOR along j of B = (A_{k-1} << 1) OR (A_{k-2} << 2) OR (c(k-1) << 1), computed by log-shifts. So A_k, and
 * the depth-k cell, needs column 1 up to time k-1. Column 1 matters only at even times (Lemma 1; tau = 1 at odd
 * times hides it), so those are the free bits.
 * The search. For each prefix of free bits before depth d (times 0, 2, .., d-2; enumerated as a tree so prefixes share
 * work), a depth-first search forces cells d, d+1, ... to zero, branching on each new free bit, and records the
 * longest run. Vectors hold 256 bits, so runs may end anywhere up to depth 255.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _OPENMP
#include <omp.h>
#endif

#define NW 4
#define KMAX 255
typedef struct { uint64_t w[NW]; } V;

static inline V shl(V a, int s) {
    V r;
    int q = s >> 6, b = s & 63;
    for (int i = NW - 1; i >= 0; i--) {
        uint64_t x = 0;
        if (i - q >= 0) {
            x = a.w[i - q] << b;
            if (b && i - q - 1 >= 0) x |= a.w[i - q - 1] >> (64 - b);
        }
        r.w[i] = x;
    }
    return r;
}

static inline V next_diag(V P, V Q, int c, int k) {
    V B = shl(P, 1), Q2 = shl(Q, 2), X;
    for (int i = 0; i < NW; i++) X.w[i] = B.w[i] | Q2.w[i];
    if (c) X.w[0] |= 2;
    X.w[0] = (X.w[0] & ~1ULL) | (uint64_t)(k & 1);          /* bit 0 = tau(k) */
    for (int s = 1; s < 64 * NW; s <<= 1) {                  /* running XOR along j */
        V Y = shl(X, s);
        for (int i = 0; i < NW; i++) X.w[i] ^= Y.w[i];
    }
    for (int i = 0; i < NW; i++) {                           /* keep bits 0 .. k */
        int lo = 64 * i;
        if (k < lo) X.w[i] = 0;
        else if (k < lo + 63) X.w[i] &= (2ULL << (k - lo)) - 1;
    }
    return X;
}

static inline int bit(V a, int j) { return (int)((a.w[j >> 6] >> (j & 63)) & 1); }

typedef struct {
    int best;
    long long hist[KMAX + 2];
    long long count_best;
    int nwit;
    V wit[64];
    int witend[64];
} Acc;

static int D;

/* constrained search: cells k, k+1, ... must be 0; returns the longest run reached in this subtree */
static int dfs_zero(int k, V P, V Q, V col1, Acc *acc, V *bestcol, int *bestend) {
    int best = k - D;                                       /* cells D .. k-1 are zero */
    if (k > KMAX) { *bestcol = col1; *bestend = k; return best; }
    int free_bit = ((k - 1) % 2 == 0);
    *bestcol = col1; *bestend = k;
    for (int c = 0; c <= free_bit; c++) {
        V col = col1;
        if (c) col.w[(k - 1) >> 6] |= 1ULL << ((k - 1) & 63);
        V A = next_diag(P, Q, c, k);
        if (bit(A, k) == 0) {
            V bc; int be;
            int r = dfs_zero(k + 1, A, P, col, acc, &bc, &be);
            if (r > best) { best = r; *bestcol = bc; *bestend = be; }
        }
    }
    return best;
}

static void record(Acc *acc, int r, V col, int end) {
    acc->hist[r]++;
    if (r > acc->best) { acc->best = r; acc->count_best = 0; acc->nwit = 0; }
    if (r == acc->best) {
        acc->count_best++;
        if (acc->nwit < 64) { acc->wit[acc->nwit] = col; acc->witend[acc->nwit] = end; acc->nwit++; }
    }
}

/* unconstrained prefix: cells before depth D are free */
static void dfs_prefix(int k, V P, V Q, V col1, Acc *acc) {
    if (k == D) {
        V bc; int be;
        int r = dfs_zero(k, P, Q, col1, acc, &bc, &be);
        record(acc, r, bc, be);
        return;
    }
    int free_bit = ((k - 1) % 2 == 0);
    for (int c = 0; c <= free_bit; c++) {
        V col = col1;
        if (c) col.w[(k - 1) >> 6] |= 1ULL << ((k - 1) & 63);
        V A = next_diag(P, Q, c, k);
        dfs_prefix(k + 1, A, P, col, acc);
    }
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: records D [THREADS] [SPLIT]\n"); return 2; }
    D = atoi(argv[1]);
    int threads = argc > 2 ? atoi(argv[2]) : 1;
    int split = argc > 3 ? atoi(argv[3]) : 12;
    int nfree = (D >= 2) ? (D - 2) / 2 + 1 : 0;             /* free bits at times 0, 2, .., D-2 */
    if (split > nfree) split = nfree;
    if (D < 1 || D > KMAX - 8) { fprintf(stderr, "D out of range\n"); return 2; }
#ifdef _OPENMP
    if (threads > 0) omp_set_num_threads(threads);
#endif
    long long ntask = 1LL << split;
    Acc total; memset(&total, 0, sizeof total);
    /* a task fixes the first `split` free bits; the prefix search continues from the step after the last of them */
    int kstart = (split == 0) ? 1 : 2 * (split - 1) + 2;      /* free bit i sits at time 2i, used by A_{2i+1} */
    #pragma omp parallel
    {
        Acc acc; memset(&acc, 0, sizeof acc);
        #pragma omp for schedule(dynamic, 1)
        for (long long task = 0; task < ntask; task++) {
            V P, Q, col; memset(&P, 0, sizeof P); memset(&Q, 0, sizeof Q); memset(&col, 0, sizeof col);
            /* A_0 = tau(0) = 0 (all zero); A_{-1} empty; walk k = 1 .. kstart-1 with the task's bits */
            int k = 1;
            for (; k < kstart && k < D; k++) {
                int c = 0;
                if ((k - 1) % 2 == 0) {
                    int i = (k - 1) / 2;
                    c = (int)((task >> i) & 1);
                    if (c) col.w[(k - 1) >> 6] |= 1ULL << ((k - 1) & 63);
                }
                V A = next_diag(P, Q, c, k);
                Q = P; P = A;
            }
            dfs_prefix(k, P, Q, col, &acc);
        }
        #pragma omp critical
        {
            for (int r = 0; r <= KMAX + 1; r++) total.hist[r] += acc.hist[r];
            if (acc.best > total.best) { total.best = acc.best; total.count_best = 0; total.nwit = 0; }
            if (acc.best == total.best) {
                total.count_best += acc.count_best;
                for (int i = 0; i < acc.nwit && total.nwit < 64; i++) {
                    total.wit[total.nwit] = acc.wit[i]; total.witend[total.nwit] = acc.witend[i]; total.nwit++;
                }
            }
        }
    }
    printf("R %d %d %lld\n", D, total.best, total.count_best);
    for (int r = 0; r <= KMAX + 1; r++) if (total.hist[r]) printf("H %d %d %lld\n", D, r, total.hist[r]);
    for (int i = 0; i < total.nwit; i++) {
        printf("W %d ", D);
        for (int t = 0; t < total.witend[i]; t += 2) putchar('0' + bit(total.wit[i], t));
        putchar('\n');
    }
    return 0;
}
