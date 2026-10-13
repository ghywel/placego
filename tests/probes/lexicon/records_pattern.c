/* records_pattern.c: the records of 8.82's exact coupling, in either wall phase: the longest zero run (R), run of ones
 * (Q) or 1, 0, 1, 1, ... pattern (P) that some column 1 forces in the left half beside the wall 0101.
 * Local, 2026-10-13; RULE30-PRIZE.md 8.95 (planned); driver rule30_black_run_records.py. A variant of records.c, which
 * stays frozen: the same anti-diagonal recurrence, with the wall phase as a parameter and a target pattern in place of
 * "all zero".
 *
 * BUILD:   cc -O3 -fopenmp -o records_pattern tests/probes/lexicon/records_pattern.c
 * USAGE:   ./records_pattern PHASE MODE D [THREADS] [SPLIT]
 *          PHASE 0: tau(t) = t mod 2 (white start, the standard phase S); PHASE 1: tau(t) = (t + 1) mod 2 (black start,
 *          the black-even phase B of 8.82 and GC1043). MODE Z: cells D, D+1, ... white; Q: cells D, D+1, ... black;
 *          P: cell D-1 black, cell D white, cells D+1, ... black. Prints "E PHASE MODE D end count": end is the largest
 *          exclusive end of the matched pattern over every column 1 (the first depth that cannot match), so for Z the
 *          record is R = end - D and 8.82's end depth is E = end; count is how many column-1 prefixes before the
 *          pattern's first cell attain it. "CAP" is printed if a run reaches the vector length.
 *
 * The forced left half (records.c's header): A_k[j] = x_{k-j}(-j), A_k[0] = tau(k), A_k[k] = row 0's cell at depth k,
 *     A_k[j] = A_k[j-1] XOR (A_{k-1}[j-1] OR A_{k-2}[j-2]),  j >= 1,  A_{k-2}[-1] = c(k-1),
 * a running XOR along j. Column 1's bit c(k-1) matters only when tau(k-1) = 0 (at a black time the OR is 1 whatever it
 * is: Lemma 1), so those are the free bits.
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

static int PH, D, START; static char MODE;

static inline int tau(int t) { return (t + PH) & 1; }

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
    X.w[0] = (X.w[0] & ~1ULL) | (uint64_t)tau(k);           /* bit 0 = tau(k) */
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

static inline int target(int k) {
    if (MODE == 'Z') return 0;
    if (MODE == 'Q') return 1;
    return k == D ? 0 : 1;                                   /* P: 1 at D-1, 0 at D, 1 beyond */
}

static int capped = 0;

/* constrained search from depth k: cells START .. k-1 already match; returns the largest exclusive end reachable */
static int dfs_match(int k, V P, V Q) {
    if (k > KMAX - 1) { capped = 1; return k; }
    int best = k;
    int free_bit = (tau(k - 1) == 0);
    for (int c = 0; c <= free_bit; c++) {
        V A = next_diag(P, Q, c, k);
        if (bit(A, k) == target(k)) {
            int r = dfs_match(k + 1, A, P);
            if (r > best) best = r;
        }
    }
    return best;
}

typedef struct { int best; long long count; } Acc;

static void dfs_prefix(int k, V P, V Q, Acc *acc) {
    if (k == START) {
        int r = dfs_match(k, P, Q);
        if (r > acc->best) { acc->best = r; acc->count = 0; }
        if (r == acc->best) acc->count++;
        return;
    }
    int free_bit = (tau(k - 1) == 0);
    for (int c = 0; c <= free_bit; c++) {
        V A = next_diag(P, Q, c, k);
        dfs_prefix(k + 1, A, P, acc);
    }
}

typedef struct { V P, Q; int k; } State;
static State *states; static long long nstates, capstates;

static void collect(int k, V P, V Q, int used, int split) {
    if (k == START || used == split) {
        if (nstates == capstates) { capstates = capstates ? 2 * capstates : 1024; states = realloc(states, capstates * sizeof(State)); }
        states[nstates].P = P; states[nstates].Q = Q; states[nstates].k = k; nstates++;
        return;
    }
    int free_bit = (tau(k - 1) == 0);
    for (int c = 0; c <= free_bit; c++) {
        V A = next_diag(P, Q, c, k);
        collect(k + 1, A, P, used + free_bit, split);
    }
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: records_pattern PHASE MODE D [THREADS] [SPLIT]\n"); return 2; }
    PH = atoi(argv[1]); MODE = argv[2][0]; D = atoi(argv[3]);
    int threads = argc > 4 ? atoi(argv[4]) : 1, split = argc > 5 ? atoi(argv[5]) : 14;
    if ((PH != 0 && PH != 1) || (MODE != 'Z' && MODE != 'Q' && MODE != 'P') || D < 1 || D > KMAX - 8 ||
        (MODE == 'P' && D < 2)) { fprintf(stderr, "bad arguments\n"); return 2; }
#ifdef _OPENMP
    if (threads > 0) omp_set_num_threads(threads);
#endif
    START = (MODE == 'P') ? D - 1 : D;
    V A0, Z; memset(&A0, 0, sizeof A0); memset(&Z, 0, sizeof Z);
    A0.w[0] = (uint64_t)tau(0);                              /* A_0 = (tau(0)); A_{-1} empty */
    collect(1, A0, Z, 0, split);
    Acc total = { -1, 0 };
    #pragma omp parallel
    {
        Acc acc = { -1, 0 };
        #pragma omp for schedule(dynamic, 1)
        for (long long i = 0; i < nstates; i++) dfs_prefix(states[i].k, states[i].P, states[i].Q, &acc);
        #pragma omp critical
        {
            if (acc.best > total.best) { total.best = acc.best; total.count = 0; }
            if (acc.best == total.best) total.count += acc.count;
        }
    }
    printf("E %d %c %d %d %lld%s\n", PH, MODE, D, total.best, total.count, capped ? " CAP" : "");
    return 0;
}
