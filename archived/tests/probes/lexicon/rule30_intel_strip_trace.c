/* rule30_intel_strip_trace.c: Intel's engine for door D4 (KIMI-QUESTIONS-4, Q1): the exactness threshold
 * L(W) = max { l : T^W(l) = T(l) } of the width-W strip for the full trace (column 1 at every time), both phases.
 *
 * Real traces: every row of sites 1..N is enumerated (2^N rows, 64 at a time, bit-sliced), the light cone is run for
 * N steps (a trace of length l depends only on sites 1..l), and the set of traces of length N is kept in hash sets;
 * T(l) for l < N is its set of length-l prefixes. Strip traces: the width-W strip (sites 1..W, the wall on the left,
 * a free input at site W+1 at every step) is walked depth-first over trace bits with its set of possible strip rows
 * as the state (a bitset over 2^W rows); only real prefixes are extended, so the walk counts at every length the real
 * strip traces (a control: it must equal |T(l)|, because T(l) is contained in T^W(l)) and the fresh extra traces
 * (strip traces whose prefix is real but which are not real). L(W) is the last length with no fresh extra.
 * Wall: x_t(0) = (t + PHASE) mod 2. Trace bits are y_t = x_t(1), t = 0 .. l-1; a trace is printed y_0 first.
 *
 * usage: rule30_intel_strip_trace PHASE N WMIN WMAX [LIST]
 *   prints "T l count" for l = 1..N, then per width "W w l=..: real r extra e" lines, "LW w L" and the extra traces at
 *   L(W)+1 ("X w l trace minimal|not-minimal": minimal when the trace without its first two symbols is real, the
 *   even shift that keeps the wall's phase); LIST > 0 also prints the real traces of length LIST ("R trace").
 * Compile: cc -O2 (OpenMP flags of COMMON rule 3) rule30_intel_strip_trace.c -o rule30_intel_strip_trace
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <omp.h>
typedef uint64_t u64;
static int PHASE, N;

static void transpose64(u64 a[64]) {   /* a[i] bit j <-> a[j] bit i */
    u64 m = 0x00000000FFFFFFFFULL;
    for (int j = 32; j; j >>= 1, m ^= m << j)
        for (int k = 0; k < 64; k = ((k | j) + 1) & ~j) {
            u64 t = ((a[k] >> j) ^ a[k | j]) & m;
            a[k] ^= t << j; a[k | j] ^= t;
        }
}

/* the real traces of length N, kept in one open-addressing hash set per thread (there are only thousands of them, so
 * memory does not grow with 2^N), merged and sorted at the end */
typedef struct { u64 *t; size_t cap, n; } hset;
static const u64 EMPTY = ~0ULL;
static inline u64 hmix(u64 x) { x ^= x >> 31; x *= 0x9E3779B97F4A7C15ULL; x ^= x >> 29; return x; }
static void hinit(hset *h, size_t cap) {
    h->cap = cap; h->n = 0; h->t = malloc(cap * 8); for (size_t i = 0; i < cap; i++) h->t[i] = EMPTY;
}
static void hput(hset *h, u64 v);
static void hgrow(hset *h) {
    hset g; hinit(&g, h->cap * 2);
    for (size_t i = 0; i < h->cap; i++) if (h->t[i] != EMPTY) hput(&g, h->t[i]);
    free(h->t); *h = g;
}
static void hput(hset *h, u64 v) {
    size_t m = h->cap - 1, i = hmix(v) & m;
    while (h->t[i] != EMPTY) { if (h->t[i] == v) return; i = (i + 1) & m; }
    h->t[i] = v; if (++h->n * 2 > h->cap) hgrow(h);
}
static u64 *TR; static size_t NTR;      /* sorted list of real traces of length N */
static void real_traces(void) {
    static const u64 LANE[6] = {0xAAAAAAAAAAAAAAAAULL, 0xCCCCCCCCCCCCCCCCULL, 0xF0F0F0F0F0F0F0F0ULL,
                                0xFF00FF00FF00FF00ULL, 0xFFFF0000FFFF0000ULL, 0xFFFFFFFF00000000ULL};
    long long nblocks = (N > 6) ? (1LL << (N - 6)) : 1, done = 0, step = nblocks / 16 + 1;
    int nth = omp_get_max_threads(); hset *H = malloc(nth * sizeof(hset));
    for (int i = 0; i < nth; i++) hinit(&H[i], 1 << 14);
    double t0 = omp_get_wtime();
    #pragma omp parallel for schedule(dynamic, 4096)
    for (long long B = 0; B < nblocks; B++) {
        u64 x[72], y[64]; hset *h = &H[omp_get_thread_num()];
        x[0] = 0;
        for (int i = 1; i <= N; i++) x[i] = (i <= 6) ? LANE[i - 1] : (((B >> (i - 7)) & 1) ? ~0ULL : 0);
        x[N + 1] = 0;
        for (int t = 0; t < 64; t++) y[t] = 0;
        for (int t = 0; t < N; t++) {
            y[t] = x[1];
            u64 left = ((t + PHASE) & 1) ? ~0ULL : 0;          /* x_t(0) */
            int top = N - 1 - t;                                 /* cells still needed at time t + 1 */
            for (int i = 1; i <= top; i++) { u64 old = x[i]; x[i] = left ^ (old | x[i + 1]); left = old; }
        }
        transpose64(y);                                          /* y[lane] = trace bits, bit t = y_t */
        u64 mask = (N >= 64) ? ~0ULL : ((1ULL << N) - 1);
        for (int ln = 0; ln < 64; ln++) hput(h, y[ln] & mask);
        long long dn;
        #pragma omp atomic capture
        dn = ++done;
        if (dn % step == 0)
            fprintf(stderr, "  real traces: %lld/%lld blocks, %.0f s\n", dn, nblocks, omp_get_wtime() - t0);
    }
    hset all; hinit(&all, 1 << 14);
    for (int i = 0; i < nth; i++) {
        for (size_t j = 0; j < H[i].cap; j++) if (H[i].t[j] != EMPTY) hput(&all, H[i].t[j]);
        free(H[i].t);
    }
    TR = malloc(all.n * 8); NTR = 0;
    for (size_t j = 0; j < all.cap; j++) if (all.t[j] != EMPTY) TR[NTR++] = all.t[j];
    free(all.t); free(H);
}

static u64 **TL; static size_t *NTL;    /* sorted lists of real traces of each length l */
static int cmpu(const void *a, const void *b) {
    u64 x = *(const u64 *)a, y = *(const u64 *)b; return x < y ? -1 : x > y;
}
static int is_real(u64 tr, int l) {
    size_t lo = 0, hi = NTL[l];
    while (lo < hi) { size_t mid = (lo + hi) / 2; if (TL[l][mid] < tr) lo = mid + 1; else hi = mid; }
    return lo < NTL[l] && TL[l][lo] == tr;
}
static void lists(void) {
    TL = calloc(N + 1, sizeof(u64 *)); NTL = calloc(N + 1, sizeof(size_t));
    for (int l = 1; l <= N; l++) {
        u64 mask = (l >= 64) ? ~0ULL : ((1ULL << l) - 1); TL[l] = malloc(NTR * 8);
        for (size_t i = 0; i < NTR; i++) TL[l][i] = TR[i] & mask;
        qsort(TL[l], NTR, 8, cmpu);
        size_t k = 0; for (size_t i = 0; i < NTR; i++) if (!k || TL[l][i] != TL[l][k - 1]) TL[l][k++] = TL[l][i];
        NTL[l] = k;
    }
}

/* strip walk */
typedef struct { long long real[72], extra[72]; u64 *xl; int nx, cx, firstx; } sres;
static void print_trace(FILE *f, u64 tr, int l) { for (int t = 0; t < l; t++) fputc('0' + (int)((tr >> t) & 1), f); }
static void walk(int W, int t, const u64 *S, u64 tr, sres *r, int LMAX) {
    int nw = ((1 << W) + 63) / 64; u64 mask = (W >= 64) ? ~0ULL : ((1ULL << W) - 1);
    u64 *T2 = malloc(nw * 8);
    int left = (t + PHASE) & 1;
    for (int b = 0; b < 2; b++) {
        int any = 0; memset(T2, 0, nw * 8);
        for (int i = 0; i < nw; i++) {
            u64 v = S[i] & (b ? 0xAAAAAAAAAAAAAAAAULL : 0x5555555555555555ULL);   /* rows with x_t(1) = b (bit 0) */
            while (v) { int k = __builtin_ctzll(v); v &= v - 1; u64 c = ((u64)i << 6) | k; any = 1;
                for (int e = 0; e < 2; e++) {
                    u64 L = ((c << 1) | (u64)left) & mask, R = (c >> 1) | ((u64)e << (W - 1));
                    u64 n2 = (L ^ (c | R)) & mask; T2[n2 >> 6] |= 1ULL << (n2 & 63);
                } }
        }
        if (W < 6) for (int i = 0; i < nw; i++) T2[i] &= (1ULL << (1 << W)) - 1;
        if (!any) continue;
        u64 tr2 = tr | ((u64)b << t); int l = t + 1;
        if (is_real(tr2, l)) {
            r->real[l]++;
            if (l < LMAX) walk(W, t + 1, T2, tr2, r, LMAX);
        } else {
            r->extra[l]++;
            if (r->firstx == 0 || l < r->firstx) { r->firstx = l; r->nx = 0; }
            if (l == r->firstx) {
                if (r->nx == r->cx) { r->cx = r->cx ? 2 * r->cx : 16; r->xl = realloc(r->xl, r->cx * 8); }
                r->xl[r->nx++] = tr2;
            }
        }
    }
    free(T2);
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: %s PHASE N WMIN WMAX [LIST]\n", argv[0]); return 1; }
    PHASE = atoi(argv[1]); N = atoi(argv[2]);
    int WMIN = atoi(argv[3]), WMAX = atoi(argv[4]), LIST = argc > 5 ? atoi(argv[5]) : 0;
    if (N < 6 || N > 40 || WMAX > 20) { fprintf(stderr, "need 6 <= N <= 40, W <= 20\n"); return 1; }
    double t0 = omp_get_wtime();
    real_traces(); lists();
    printf("REAL phase %d N %d: %zu traces of length N, %.1f s, %d threads\n", PHASE, N, NTR, omp_get_wtime() - t0,
           omp_get_max_threads());
    for (int l = 1; l <= N; l++) printf("T %d %zu\n", l, NTL[l]);
    if (LIST > 0 && LIST <= N)
        for (size_t i = 0; i < NTL[LIST]; i++) { printf("R "); print_trace(stdout, TL[LIST][i], LIST); printf("\n"); }
    int nwid = WMAX - WMIN + 1; sres *res = calloc(nwid, sizeof(sres));
    #pragma omp parallel for schedule(dynamic, 1)
    for (int W = WMAX; W >= WMIN; W--) {
        int nw = ((1 << W) + 63) / 64; u64 *S = calloc(nw, 8);
        for (u64 c = 0; c < (1ULL << W); c++) S[c >> 6] |= 1ULL << (c & 63);          /* every initial strip row */
        walk(W, 0, S, 0, &res[W - WMIN], N); free(S);
    }
    for (int W = WMIN; W <= WMAX; W++) {
        sres *r = &res[W - WMIN]; int ok = 1;
        for (int l = 1; l <= N; l++) { if (r->real[l] != (long long)NTL[l]) ok = 0;
            printf("W %d l %d: real %lld of %zu, fresh extra %lld\n", W, l, r->real[l], NTL[l], r->extra[l]); }
        printf("CONTAIN %d %s\n", W, ok ? "PASS" : "FAIL");
        if (r->firstx) { printf("LW %d %d\n", W, r->firstx - 1);
            for (int i = 0; i < r->nx; i++) {
                int l = r->firstx; printf("X %d %d ", W, l); print_trace(stdout, r->xl[i], l);
                printf(" %s\n", (l <= 2 || is_real(r->xl[i] >> 2, l - 2)) ? "minimal" : "not-minimal"); } }
        else printf("LW %d >=%d\n", W, N);
    }
    printf("DONE %.1f s\n", omp_get_wtime() - t0);
    return 0;
}
