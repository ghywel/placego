/* records_fast.c: records.c's search, faster on ARM64 (Local, 2026-10-05). The same definition, the same outputs:
 * "R D best count", the "H D r count" histogram, and up to 64 "W D e" witnesses (their order, like records.c's, depends
 * on the thread schedule; R and H do not).
 *
 * BUILD (macOS, Homebrew libomp):
 *   cc -O3 -mcpu=apple-m1 -Xpreprocessor -fopenmp -I/opt/homebrew/opt/libomp/include -L/opt/homebrew/opt/libomp/lib \
 *      -lomp -o records_fast tests/probes/lexicon/records_fast.c
 * BUILD (Linux, gcc): cc -O3 -march=armv8-a+crypto -fopenmp -o records_fast tests/probes/lexicon/records_fast.c
 *   (without PMULL, e.g. on x86, the running XOR falls back to records.c's log-shifts)
 * USAGE:   ./records_fast D [THREADS] [SPLIT]          as records.c
 *
 * Three changes, nothing else:
 * 1. The running XOR along a diagonal (records.c: 8 rounds of 256-bit shifts) is one carry-less multiply per 64-bit
 *    word: the low half of clmul(x, 2^64 - 1) has bit n = x_0 XOR ... XOR x_n, and a word whose lower words have odd
 *    parity is inverted.
 * 2. A diagonal A_k has bits 0 .. k only, so step k works on k/64 + 1 words, not 4.
 * 3. Each prefix's run is measured without carrying a witness (run_len), and a child whose new cell is 1 is rejected
 *    from a parity before its diagonal is built; records.c's dfs_zero then finds the witness only for a prefix that
 *    reaches its thread's running record, so the witnesses are the same ones.
 * VALIDATION (Local, 2026-10-05, the M5): against records.c at every depth 1 .. 57 (4 threads each), the R line and
 *   every H line are identical, and wherever the record has at most 64 prefixes (so both list every witness) the W
 *   lines are the same set. Counterfactual: records.c at depth 40 against this at depth 41, relabelled, differs.
 *   The check is not idle: a first cut of change 3 cleared bit 1 of X (it carries P's bit 0) and failed at every
 *   depth. Speed: 1.35x records.c (depth 53, 2 threads, interleaved, with M4 loading the machine). The zero-run
 *   search at the leaves is about 75% of the time; the prefix tree 25%.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _OPENMP
#include <omp.h>
#endif
#if defined(__aarch64__) && (defined(__ARM_FEATURE_AES) || defined(__ARM_FEATURE_CRYPTO))
#include <arm_neon.h>
#define HAVE_PMULL 1
#endif

#define NW 4
#define KMAX 255
typedef struct { uint64_t w[NW]; } V;

static inline uint64_t prefix_xor64(uint64_t x) {
#ifdef HAVE_PMULL
    poly128_t p = vmull_p64((poly64_t)x, (poly64_t)~0ULL);
    return (uint64_t)p;                                       /* the low 64 bits of the carry-less product */
#else
    x ^= x << 1; x ^= x << 2; x ^= x << 4; x ^= x << 8; x ^= x << 16; x ^= x << 32;
    return x;
#endif
}

/* A_k from P = A_{k-1}, Q = A_{k-2}: A_k[j] = A_k[j-1] XOR (P[j-1] OR Q[j-2]), A_k[0] = tau(k), c = c(k-1) at j = 1 */
static inline V next_diag(const V *P, const V *Q, int c, int k) {
    V X;
    int nw = (k >> 6) + 1;                                    /* bits 0 .. k */
    uint64_t pc = 0, qc = 0;
    for (int i = 0; i < nw; i++) {
        uint64_t p = P->w[i], q = Q->w[i];
        X.w[i] = (p << 1 | pc) | (q << 2 | qc);
        pc = p >> 63; qc = q >> 62;
    }
    for (int i = nw; i < NW; i++) X.w[i] = 0;
    if (c) X.w[0] |= 2;
    X.w[0] = (X.w[0] & ~1ULL) | (uint64_t)(k & 1);
    uint64_t carry = 0;                                       /* all ones if the bits below this word XOR to 1 */
    for (int i = 0; i < nw; i++) {
        uint64_t y = prefix_xor64(X.w[i]) ^ carry;
        carry = (uint64_t)0 - (y >> 63);
        X.w[i] = y;
    }
    int top = k & 63;                                         /* keep bits 0 .. k */
    if (top < 63) X.w[nw - 1] &= (2ULL << top) - 1;
    return X;
}

static inline int bit(const V *a, int j) { return (int)((a->w[j >> 6] >> (j & 63)) & 1); }

typedef struct {
    int best;
    long long hist[KMAX + 2];
    long long count_best;
    int nwit;
    V wit[64];
    int witend[64];
} Acc;

static int D;

static int dfs_zero(int k, const V *P, const V *Q, V col1, V *bestcol, int *bestend) {
    int best = k - D;
    if (k > KMAX) { *bestcol = col1; *bestend = k; return best; }
    int free_bit = ((k - 1) % 2 == 0);
    *bestcol = col1; *bestend = k;
    for (int c = 0; c <= free_bit; c++) {
        V A = next_diag(P, Q, c, k);
        if (bit(&A, k) == 0) {
            V col = col1;
            if (c) col.w[(k - 1) >> 6] |= 1ULL << ((k - 1) & 63);
            V bc; int be;
            int r = dfs_zero(k + 1, &A, P, col, &bc, &be);
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

/* The same search as dfs_zero, for the length only: no witness is carried, and a child whose new cell is 1 is
 * rejected from the parity of its shifted bits (the cell A_k[k] is the XOR of X's bits 0 .. k, and X has no bits above
 * k) before its diagonal is built. */
static int run_len(int k, const V *P, const V *Q) {
    int best = k - D;
    if (k > KMAX) return best;
    int free_bit = ((k - 1) % 2 == 0);
    int nw = (k >> 6) + 1;
    V X;
    uint64_t pc = 0, qc = 0, par = 0;
    for (int i = 0; i < nw; i++) {
        uint64_t p = P->w[i], q = Q->w[i];
        X.w[i] = (p << 1 | pc) | (q << 2 | qc);
        pc = p >> 63; qc = q >> 62;
    }
    X.w[0] = (X.w[0] & ~1ULL) | (uint64_t)(k & 1);             /* c = 0 first, as dfs_zero */
    for (int i = 0; i < nw; i++) par ^= X.w[i];
    int cell0 = __builtin_parityll(par);
    int b1 = (int)((X.w[0] >> 1) & 1);
    for (int c = 0; c <= free_bit; c++) {
        int cell = cell0 ^ (c & !b1);                           /* c ORs bit 1 of X: it flips the parity if that bit was 0 */
        if (cell) continue;
        V A;
        uint64_t carry = 0;
        for (int i = 0; i < nw; i++) {
            uint64_t x = X.w[i];
            if (i == 0 && c) x |= 2;
            uint64_t y = prefix_xor64(x) ^ carry;
            carry = (uint64_t)0 - (y >> 63);
            A.w[i] = y;
        }
        for (int i = nw; i < NW; i++) A.w[i] = 0;
        int top = k & 63;
        if (top < 63) A.w[nw - 1] &= (2ULL << top) - 1;
        int r = run_len(k + 1, &A, P);
        if (r > best) best = r;
    }
    return best;
}

static void dfs_prefix(int k, const V *P, const V *Q, V col1, Acc *acc) {
    if (k == D) {
        int r = run_len(k, P, Q);
        acc->hist[r]++;
        if (r >= acc->best) {                                   /* a record for this thread: find its witness */
            V bc; int be;
            dfs_zero(k, P, Q, col1, &bc, &be);
            acc->hist[r]--;
            record(acc, r, bc, be);
        }
        return;
    }
    int free_bit = ((k - 1) % 2 == 0);
    for (int c = 0; c <= free_bit; c++) {
        V col = col1;
        if (c) col.w[(k - 1) >> 6] |= 1ULL << ((k - 1) & 63);
        V A = next_diag(P, Q, c, k);
        dfs_prefix(k + 1, &A, P, col, acc);
    }
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: records_fast D [THREADS] [SPLIT]\n"); return 2; }
    D = atoi(argv[1]);
    int threads = argc > 2 ? atoi(argv[2]) : 1;
    int split = argc > 3 ? atoi(argv[3]) : 12;
    int nfree = (D >= 2) ? (D - 2) / 2 + 1 : 0;
    if (split > nfree) split = nfree;
    if (D < 1 || D > KMAX - 8) { fprintf(stderr, "D out of range\n"); return 2; }
#ifdef _OPENMP
    if (threads > 0) omp_set_num_threads(threads);
#endif
    long long ntask = 1LL << split;
    Acc total; memset(&total, 0, sizeof total);
    int kstart = (split == 0) ? 1 : 2 * (split - 1) + 2;
    #pragma omp parallel
    {
        Acc acc; memset(&acc, 0, sizeof acc);
        #pragma omp for schedule(dynamic, 1)
        for (long long task = 0; task < ntask; task++) {
            V P, Q, col; memset(&P, 0, sizeof P); memset(&Q, 0, sizeof Q); memset(&col, 0, sizeof col);
            int k = 1;
            for (; k < kstart && k < D; k++) {
                int c = 0;
                if ((k - 1) % 2 == 0) {
                    int i = (k - 1) / 2;
                    c = (int)((task >> i) & 1);
                    if (c) col.w[(k - 1) >> 6] |= 1ULL << ((k - 1) & 63);
                }
                V A = next_diag(&P, &Q, c, k);
                Q = P; P = A;
            }
            dfs_prefix(k, &P, &Q, col, &acc);
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
        for (int t = 0; t < total.witend[i]; t += 2) putchar('0' + bit(&total.wit[i], t));
        putchar('\n');
    }
    return 0;
}
