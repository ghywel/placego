/* rule30_intel_carry.c: Intel's engine for probe CAR (KIMI-QUESTIONS-5, the carry of Rule 30).
 * Rule: x'(i) = x(i-1) XOR (x(i) OR x(i+1)); carry c(i) = (1 - x(i)) x(i+1); d(i) = x(i) x(i+1).
 *
 * ring NMIN NMAX   every row of a ring of n cells (bit i = cell i): joint counts of (K_0, K_1, K_2), (D_0, D_1, D_2),
 *                  (B_0, B_1, B_2) with K = #carries, D = #adjacent black pairs, B = #black cells.
 *                  Output "J n q a b c count" for q in K, D, B.
 * cone T           the single black cell on the line, T steps: for t = 1..T the centre x_t(0), the Pascal-masked carry
 *                  count n_t = sum_{s<t} sum_{j subset of t-1-s} c_s(-j) (a subset-sum transform of each row's left
 *                  carries), its parity P_t, the mask size m_t = sum_{k<t} 2^popcount(k), and mcone_t, the mask cells
 *                  inside the light cone (j <= s + 1). Output "C t x_t(0) P_t n_t m_t mcone_t".
 * column R STEPS   R rings of 4096 cells from splitmix64 rows (seed = ring index); the carry at the middle cell m and
 *                  along the diagonals m + t and m - t for t < STEPS: counts of every 16-bit window (overlapping) and
 *                  the sums for correlations at lags 0..64. Output "W q pattern count" and "S q lag sum_xy sum_x n".
 * block K          every row of the 2K cells at sites -(K-1)..K: exact counts of the column-carry blocks c_t(0),
 *                  t = 0..K-1 (bit t of the pattern). Output "B K pattern count" (rows per pattern; 2^(2K) rows in all).
 * Compile with the OpenMP flags of COMMON rule 3 (Apple clang needs libomp).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <omp.h>
typedef uint64_t u64;

/* ---------------- ring ---------------- */
static inline u64 rotl(u64 x, int n, u64 m) { return ((x << 1) | (x >> (n - 1))) & m; }   /* bit i <- bit i-1 */
static inline u64 rotr(u64 x, int n, u64 m) { return ((x >> 1) | (x << (n - 1))) & m; }   /* bit i <- bit i+1 */
static inline u64 step(u64 x, int n, u64 m) { return rotl(x, n, m) ^ (x | rotr(x, n, m)); }
static void ring(int n) {
    u64 m = (n == 64) ? ~0ULL : ((1ULL << n) - 1); int S = n + 1; size_t cells = (size_t)S * S * S;
    int nth = omp_get_max_threads(); u64 *H = calloc((size_t)nth * 3 * cells, 8);
    double t0 = omp_get_wtime();
    #pragma omp parallel
    {
        u64 *h = H + (size_t)omp_get_thread_num() * 3 * cells;
        #pragma omp for schedule(static)
        for (long long r = 0; r < (1LL << n); r++) {
            u64 x0 = (u64)r, x1 = step(x0, n, m), x2 = step(x1, n, m);
            int k0 = __builtin_popcountll(~x0 & rotr(x0, n, m) & m);
            int k1 = __builtin_popcountll(~x1 & rotr(x1, n, m) & m);
            int k2 = __builtin_popcountll(~x2 & rotr(x2, n, m) & m);
            int d0 = __builtin_popcountll(x0 & rotr(x0, n, m)), d1 = __builtin_popcountll(x1 & rotr(x1, n, m)),
                d2 = __builtin_popcountll(x2 & rotr(x2, n, m));
            int b0 = __builtin_popcountll(x0), b1 = __builtin_popcountll(x1), b2 = __builtin_popcountll(x2);
            h[((size_t)k0 * S + k1) * S + k2]++; h[cells + ((size_t)d0 * S + d1) * S + d2]++;
            h[2 * cells + ((size_t)b0 * S + b1) * S + b2]++;
        }
    }
    const char *Q = "KDB";
    for (int q = 0; q < 3; q++)
        for (size_t i = 0; i < cells; i++) {
            u64 v = 0; for (int t = 0; t < nth; t++) v += H[(size_t)t * 3 * cells + q * cells + i];
            if (v)
                printf("J %d %c %zu %zu %zu %llu\n", n, Q[q], i / (S * S), (i / S) % S, i % S, (unsigned long long)v);
        }
    fprintf(stderr, "ring n = %d: %.1f s\n", n, omp_get_wtime() - t0);
    free(H);
}

/* ---------------- cone ---------------- */
static void cone(int T) {
    int a = 0; while ((1 << a) < T) a++;
    int K = 1 << a, OFF = T + 2, W = 2 * T + 6, nw = W / 64 + 2;
    u64 *x = calloc(nw, 8), *y = calloc(nw, 8);
    size_t rw = (size_t)K / 64 + 1; u64 *rows = calloc((size_t)T * rw, 8);   /* r_s(j) = c_s(-j), j < K */
    char *cen = malloc(T + 1);
    x[OFF >> 6] |= 1ULL << (OFF & 63);
    #define GB(v, p) ((int)(((v)[(p) >> 6] >> ((p) & 63)) & 1))
    for (int s = 0; s <= T; s++) {
        cen[s] = (char)GB(x, OFF);
        if (s == T) break;
        u64 *r = rows + (size_t)s * rw;
        for (int j = 0; j < K && j <= s + 2; j++) {
            int p = OFF - j; if (!GB(x, p) && GB(x, p + 1)) r[j >> 6] |= 1ULL << (j & 63);
        }
        for (int i = 0; i < nw; i++) {                     /* y(p) = x(p-1) ^ (x(p) | x(p+1)) */
            u64 L = (x[i] << 1) | (i ? x[i - 1] >> 63 : 0), R = (x[i] >> 1) | (i + 1 < nw ? x[i + 1] << 63 : 0);
            y[i] = L ^ (x[i] | R);
        }
        u64 *tmp = x; x = y; y = tmp;
    }
    int nth = omp_get_max_threads();
    u64 *NT = calloc((size_t)nth * (T + 2), 8), *MC = calloc((size_t)nth * (T + 2), 8);
    double t0 = omp_get_wtime();
    #pragma omp parallel
    {
        int tid = omp_get_thread_num(); uint32_t *Z = malloc((size_t)K * 4), *U = malloc((size_t)K * 4);
        u64 *nt = NT + (size_t)tid * (T + 2), *mc = MC + (size_t)tid * (T + 2);
        #pragma omp for schedule(dynamic, 16)
        for (int s = 0; s < T; s++) {
            const u64 *r = rows + (size_t)s * rw; int kmax = T - 1 - s;      /* k = t - 1 - s ranges over 0..kmax */
            for (int j = 0; j < K; j++) { Z[j] = (uint32_t)((r[j >> 6] >> (j & 63)) & 1); U[j] = (j <= s + 1); }
            for (int b = 0; b < a; b++)
                for (int j = 0; j < K; j++) if (j & (1 << b)) { Z[j] += Z[j ^ (1 << b)]; U[j] += U[j ^ (1 << b)]; }
            for (int k = 0; k <= kmax; k++) { nt[s + 1 + k] += Z[k]; mc[s + 1 + k] += U[k]; }
        }
        free(Z); free(U);
    }
    u64 m = 0; long long bad = 0;
    for (int t = 1; t <= T; t++) {
        u64 n = 0, mcone = 0;
        for (int i = 0; i < nth; i++) { n += NT[(size_t)i * (T + 2) + t]; mcone += MC[(size_t)i * (T + 2) + t]; }
        m += 1ULL << __builtin_popcount((unsigned)(t - 1));
        int P = (int)(n & 1); if (cen[t] != (1 ^ P)) bad++;
        printf("C %d %d %d %llu %llu %llu\n", t, cen[t], P, (unsigned long long)n, (unsigned long long)m,
               (unsigned long long)mcone);
    }
    fprintf(stderr, "cone T = %d: identity failures %lld; transforms %.1f s\n", T, bad, omp_get_wtime() - t0);
    printf("IDENTITY %s %lld\n", bad ? "FAIL" : "PASS", bad);
}

/* ---------------- column ---------------- */
static inline u64 splitmix(u64 *s) {
    u64 z = (*s += 0x9E3779B97F4A7C15ULL); z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL; return z ^ (z >> 31);
}
static void column(long long R, int STEPS) {
    enum { NW = 64, NC = 4096, MID = 2048, LAGS = 64 };
    int nth = omp_get_max_threads();
    size_t LG = (size_t)3 * (LAGS + 1);
    u64 *Wc = calloc((size_t)nth * 3 * 65536, 8);
    u64 *Sxy = calloc(nth * LG, 8), *Sx = calloc(nth * LG, 8), *Sn = calloc(nth * LG, 8);
    double t0 = omp_get_wtime();
    #pragma omp parallel
    {
        int tid = omp_get_thread_num(); u64 x[NW], y[NW]; unsigned char *seq = malloc(3 * (size_t)STEPS);
        u64 *w = Wc + (size_t)tid * 3 * 65536, *sxy = Sxy + tid * LG, *sx = Sx + tid * LG, *sn = Sn + tid * LG;
        #pragma omp for schedule(dynamic, 64)
        for (long long ring_i = 0; ring_i < R; ring_i++) {
            u64 seed = (u64)ring_i * 0x2545F4914F6CDD1DULL + 12345;
            for (int i = 0; i < NW; i++) x[i] = splitmix(&seed);
            for (int t = 0; t < STEPS; t++) {
                int pos[3] = {MID, MID + t, MID - t};
                for (int q = 0; q < 3; q++) {
                    int p = pos[q], p1 = (p + 1) % NC;
                    int xp = (int)((x[p >> 6] >> (p & 63)) & 1), xq = (int)((x[p1 >> 6] >> (p1 & 63)) & 1);
                    seq[q * STEPS + t] = (unsigned char)(!xp && xq);
                }
                for (int i = 0; i < NW; i++) {                 /* ring of 4096: bit p's left neighbour is p-1 */
                    u64 L = (x[i] << 1) | (x[(i + NW - 1) % NW] >> 63), Rr = (x[i] >> 1) | (x[(i + 1) % NW] << 63);
                    y[i] = L ^ (x[i] | Rr);
                }
                memcpy(x, y, sizeof x);
            }
            for (int q = 0; q < 3; q++) {
                const unsigned char *c = seq + q * STEPS; unsigned pat = 0;
                for (int t = 0; t < STEPS; t++) {
                    pat = (pat >> 1) | ((unsigned)c[t] << 15);
                    if (t >= 15) w[q * 65536 + pat]++;         /* bit 0 = c_{t-15}, bit 15 = c_t */
                }
                for (int L = 0; L <= LAGS; L++) {
                    u64 a = 0, b = 0; for (int t = 0; t + L < STEPS; t++) { a += (u64)(c[t] & c[t + L]); b += c[t]; }
                    sxy[q * (LAGS + 1) + L] += a; sx[q * (LAGS + 1) + L] += b;
                    sn[q * (LAGS + 1) + L] += (u64)(L < STEPS ? STEPS - L : 0);
                }
            }
        }
        free(seq);
    }
    const char *Q[3] = {"col", "diag+", "diag-"};
    for (int q = 0; q < 3; q++) {
        for (int p = 0; p < 65536; p++) {
            u64 v = 0; for (int t = 0; t < nth; t++) v += Wc[(size_t)t * 3 * 65536 + q * 65536 + p];
            if (v) printf("W %s %d %llu\n", Q[q], p, (unsigned long long)v);
        }
        for (int L = 0; L <= LAGS; L++) {
            u64 a = 0, b = 0, n = 0;
            for (int t = 0; t < nth; t++) {
                size_t o = t * LG + q * (LAGS + 1) + L; a += Sxy[o]; b += Sx[o]; n += Sn[o];
            }
            printf("S %s %d %llu %llu %llu\n", Q[q], L, (unsigned long long)a, (unsigned long long)b,
                   (unsigned long long)n);
        }
    }
    fprintf(stderr, "column R = %lld, STEPS = %d: %.1f s\n", R, STEPS, omp_get_wtime() - t0);
}

/* ---------------- block ---------------- */
/* the column carry c_t(0), t = 0..K-1, from every row of the 2K cells at sites -(K-1)..K (its light cone): exact counts
 * of every K-bit block (bit t = c_t(0)), 64 rows at a time, bit-sliced */
static void transpose64b(u64 a[64]) {
    u64 m = 0x00000000FFFFFFFFULL;
    for (int j = 32; j; j >>= 1, m ^= m << j)
        for (int k = 0; k < 64; k = ((k | j) + 1) & ~j) { u64 t = ((a[k] >> j) ^ a[k | j]) & m; a[k] ^= t << j; a[k | j] ^= t; }
}
static void block(int K) {
    static const u64 LANE[6] = {0xAAAAAAAAAAAAAAAAULL, 0xCCCCCCCCCCCCCCCCULL, 0xF0F0F0F0F0F0F0F0ULL,
                                0xFF00FF00FF00FF00ULL, 0xFFFF0000FFFF0000ULL, 0xFFFFFFFF00000000ULL};
    int C = 2 * K, nth = omp_get_max_threads(); long long nblocks = 1LL << (C - 6);
    u64 *H = calloc((size_t)nth << K, 8); double t0 = omp_get_wtime();
    #pragma omp parallel
    {
        u64 *h = H + ((size_t)omp_get_thread_num() << K);
        #pragma omp for schedule(dynamic, 4096)
        for (long long B = 0; B < nblocks; B++) {
            u64 x[72], y[64];
            for (int u = 0; u < C; u++) x[u] = (u < 6) ? LANE[u] : (((B >> (u - 6)) & 1) ? ~0ULL : 0);
            x[C] = 0;
            for (int t = 0; t < 64; t++) y[t] = 0;
            for (int t = 0; t < K; t++) {
                y[t] = ~x[K - 1] & x[K];                         /* c_t(0): site 0 white, site 1 black */
                u64 left = 0;
                for (int u = 0; u < C; u++) { u64 old = x[u]; x[u] = left ^ (old | x[u + 1]); left = old; }
            }
            transpose64b(y);
            for (int ln = 0; ln < 64; ln++) h[y[ln] & ((1ULL << K) - 1)]++;
        }
    }
    for (u64 p = 0; p < (1ULL << K); p++) {
        u64 v = 0; for (int t = 0; t < nth; t++) v += H[((size_t)t << K) + p];
        if (v) printf("B %d %llu %llu\n", K, (unsigned long long)p, (unsigned long long)v);
    }
    fprintf(stderr, "block K = %d: 2^%d rows, %.1f s\n", K, C, omp_get_wtime() - t0);
    free(H);
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s ring NMIN NMAX | cone T | column R STEPS | block K\n", argv[0]); return 1; }
    if (!strcmp(argv[1], "ring")) { for (int n = atoi(argv[2]); n <= atoi(argv[3]); n++) ring(n); }
    else if (!strcmp(argv[1], "cone")) cone(atoi(argv[2]));
    else if (!strcmp(argv[1], "column")) column(atoll(argv[2]), atoi(argv[3]));
    else if (!strcmp(argv[1], "block")) block(atoi(argv[2]));
    else { fprintf(stderr, "unknown mode\n"); return 1; }
    return 0;
}
