/* forced_only_x4.c: the forced-only records R^F(d) of the check-free conjecture (RULE30-PRIZE.md 8.88), exact, by a
 * breadth-first walk over visible prefixes with the record's masked-pair merging (8.38, MG0b).  Intel, 2026-10-11.
 *
 * Object. Beside the alternating wall (phase 0: column 0 reads t mod 2; phase 1: (t+1) mod 2) the forced left half is a
 * function of the visible bits (column 1 at the wall's white times). Anti-diagonal m holds the cells with time + depth
 * = m: A_m[j] = x_{m-j}(-j), j = 0..m. From the leftward reading,
 *     A_m[0] = w_m,  A_m[1] = w_m XOR (w_{m-1} OR y_{m-1}),  A_m[j] = A_m[j-1] XOR (A_{m-1}[j-1] OR A_{m-2}[j-2]).
 * Row 0's depth-m cell is A_m[m]. The newest visible bit enters at a FORCED index m (w_{m-1} = 0) through A_m[1] = 1 XOR y
 * and then through every A_m[j] as a plain XOR, so the forced cell at depth m is white for exactly one value of y; at a
 * CHECK index (w_{m-1} = 1) no bit enters. The forced-only orbit of a prefix takes the whitening bit at every forced
 * index and dies when that bit leaves the language K; checks are ignored. R^F(d) is the longest run of depths from d on
 * with every forced cell white, over the prefixes in K (phase 0: forced indices odd; phase 1: even, depth 1 black).
 *
 * Merging (8.38): computing A_{m+1} reads A_{m-1}[i] only where A_m[i+1] = 0, so two prefixes with the same A_m, the
 * same A_{m-1} off those positions and the same recent visible bits (for the language) have the same future. States are
 * merged on that key, keeping the longest streak of white forced cells ending at m and one representative prefix.
 *
 * Languages: x4 = {no 11, no 00000} (the width-4 layer language), gm = {no 11} (the control: infinite in phase 1),
 * maw12 = the twelve minimal absent words of lengths 2..12 of the real visible language (standard phase).
 *
 * usage: forced_only_x4 PHASE LANG MAXM MAXSTATES [NODEDUP]
 *   PHASE 0|1; LANG x4|gm|maw12; MAXM: last forced index processed (depths reported to MAXM+1); MAXSTATES: stop before
 *   a level whose children would exceed this many records; NODEDUP 1 disables merging (a control for the mask).
 * output: one line per level "L m states children seconds", one per depth "D d R cens witness", and "K m k11 k0 cap"
 *   (deaths at 11, at 00000 or other maw, capped) for the unexpected check. Compile with the OpenMP line of COMMON rule 3.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#include <omp.h>

#define MAXW 16                      /* anti-diagonal words for the forced path: up to 1024 bits */
typedef uint64_t u64;

static int PHASE, LANG;
static const char *MAW[12] = {"11","00000","101001","0100101","010010001","0101000101","0101010000",
                              "01010001001","10010001001","010010000101","010100010001","100100010000"};
static int MAWLEN[12]; static u64 MAWVAL[12];

static inline int wall(int t) { return PHASE == 0 ? (t & 1) : 1 - (t & 1); }

/* language check: the new suffix after appending y; last holds the previous bits, most recent at bit 0; k = count */
static inline int allowed(u64 last, int k, int y) {
    u64 s = (last << 1) | (u64)y;                    /* suffix with y at bit 0 */
    if (LANG == 1) return !(k >= 1 && (s & 3) == 3);
    if (LANG == 0) {
        if (k >= 1 && (s & 3) == 3) return 0;
        if (k >= 4 && (s & 31) == 0) return 0;
        return 1;
    }
    for (int i = 0; i < 12; i++) {
        int L = MAWLEN[i];
        if (k + 1 >= L && (s & ((1ULL << L) - 1)) == MAWVAL[i]) return 0;
    }
    return 1;
}
static inline int death_kind(u64 last, int k, int y) {   /* 1: died at 11; 2: at 00000 or another maw */
    u64 s = (last << 1) | (u64)y;
    if (k >= 1 && (s & 3) == 3) return 1;
    return 2;
}

/* prefix XOR over a multiword bit vector (bit 0 first) */
static inline void prefix_xor(u64 *v, int nw) {
    u64 carry = 0;
    for (int i = 0; i < nw; i++) {
        u64 x = v[i];
        x ^= x << 1; x ^= x << 2; x ^= x << 4; x ^= x << 8; x ^= x << 16; x ^= x << 32;
        x ^= carry; carry = (u64)0 - (x >> 63);
        v[i] = x;
    }
}
/* A_m from A_{m-1} (a1), A_{m-2} (a2): V = (a1<<1)|(a2<<2), bit0 = w_m, bit1 = w_{m-1} | y; then prefix xor */
static inline void next_diag(const u64 *a1, const u64 *a2, int nw, int m, int y, u64 *out) {
    u64 c1 = 0, c2 = 0;
    for (int i = 0; i < nw; i++) {
        u64 s1 = (a1[i] << 1) | c1; c1 = a1[i] >> 63;
        u64 s2 = (a2[i] << 2) | c2; c2 = a2[i] >> 62;
        out[i] = s1 | s2;
    }
    out[0] &= ~3ULL;
    out[0] |= (u64)wall(m) | ((u64)(wall(m - 1) | y) << 1);
    prefix_xor(out, nw);
    int tw = m >> 6;
    if (tw < nw) { out[tw] &= ((m & 63) == 63) ? ~0ULL : ((1ULL << ((m & 63) + 1)) - 1); for (int i = tw + 1; i < nw; i++) out[i] = 0; }
}
static inline int getbit(const u64 *a, int j) { return (a[j >> 6] >> (j & 63)) & 1; }

/* ---- state records: [A_m (nw)] [A_{m-1} masked (nw)] [rep (1)] [meta (1)]: meta = last(12) | streak<<16 | k<<32 */
typedef struct { u64 *buf; size_t n, cap; } vec;
static void vpush(vec *v, const u64 *rec, int stride) {
    if (v->n + stride > v->cap) { v->cap = v->cap ? v->cap * 2 : (size_t)stride * 1024; v->buf = realloc(v->buf, v->cap * 8); if (!v->buf) { fprintf(stderr, "out of memory\n"); exit(2);} }
    memcpy(v->buf + v->n, rec, stride * 8); v->n += stride;
}
static inline u64 hash_rec(const u64 *r, int keywords) {
    u64 h = 0x9E3779B97F4A7C15ULL;
    for (int i = 0; i < keywords; i++) { h ^= r[i]; h *= 0xBF58476D1CE4E5B9ULL; h ^= h >> 31; }
    return h;
}
static int cmp_rec_words(const void *pa, const void *pb);   /* set via globals below */
static int G_KEYW; static const u64 *G_BASE; static int G_STRIDE;
typedef struct { u64 h; uint32_t idx; } hi;
static int cmp_hi(const void *pa, const void *pb) {
    const hi *a = pa, *b = pb;
    if (a->h != b->h) return a->h < b->h ? -1 : 1;
    const u64 *ra = G_BASE + (size_t)a->idx * G_STRIDE, *rb = G_BASE + (size_t)b->idx * G_STRIDE;
    for (int i = 0; i < G_KEYW; i++) if (ra[i] != rb[i]) return ra[i] < rb[i] ? -1 : 1;
    return 0;
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: %s PHASE LANG MAXM MAXSTATES [NODEDUP]\n", argv[0]); return 1; }
    PHASE = atoi(argv[1]);
    LANG = !strcmp(argv[2], "x4") ? 0 : !strcmp(argv[2], "gm") ? 1 : 2;
    int MAXM = atoi(argv[3]); size_t MAXSTATES = strtoull(argv[4], 0, 10); int NODEDUP = argc > 5 ? atoi(argv[5]) : 0;
    for (int i = 0; i < 12; i++) { MAWLEN[i] = strlen(MAW[i]); u64 v = 0; for (int j = 0; j < MAWLEN[i]; j++) v = (v << 1) | (MAW[i][j] - '0'); MAWVAL[i] = v; }
    int nthreads = omp_get_max_threads();
    int m0 = (PHASE == 0) ? 1 : 2;                     /* first forced index */
    int nw = 1;                                        /* words per anti-diagonal at the current level */
    int stride = 2 * nw + 2;
    vec cur = {0};
    /* initial states at m0 */
    {
        u64 A0[MAXW] = {0}, Am1[MAXW] = {0}, A1[MAXW] = {0}, A2[MAXW] = {0}, rec[64];
        A0[0] = wall(0);
        if (PHASE == 0) {
            for (int y = 0; y < 2; y++) {
                next_diag(A0, Am1, nw, 1, y, A1);      /* forced index 1 */
                int white = !getbit(A1, 1);
                u64 masked = A0[0] & ~(A1[0] >> 1);
                memset(rec, 0, sizeof rec); rec[0] = A1[0]; rec[1] = masked; rec[2] = (u64)y; rec[3] = (u64)y | ((u64)white << 16) | (1ULL << 32);
                vpush(&cur, rec, stride);
            }
        } else {
            next_diag(A0, Am1, nw, 1, 0, A1);          /* check index 1 */
            for (int y = 0; y < 2; y++) {
                next_diag(A1, A0, nw, 2, y, A2);       /* forced index 2 */
                int white = !getbit(A2, 2);
                u64 masked = A1[0] & ~(A2[0] >> 1);
                memset(rec, 0, sizeof rec); rec[0] = A2[0]; rec[1] = masked; rec[2] = (u64)y; rec[3] = (u64)y | ((u64)white << 16) | (1ULL << 32);
                vpush(&cur, rec, stride);
            }
        }
    }
    int NREP = MAXM + 4;
    int *R = calloc(NREP, sizeof(int)), *CENS = calloc(NREP, sizeof(int)); u64 *WIT = calloc(NREP, 8); int *WITK = calloc(NREP, sizeof(int));
    long long k11 = 0, k00 = 0, kcap = 0;
    double t0 = omp_get_wtime();
    for (int m = m0; m <= MAXM; m += 2) {
        size_t nstates = cur.n / stride;
        int nwp = (m + 3 * m + 400) / 64 + 1; if (nwp > MAXW) nwp = MAXW;   /* path words */
        int cap = 3 * m + 300;                                               /* path cap in anti-diagonal steps */
        /* ---- evaluate forced paths from every state (contributions to R) ---- */
        int **Rt = malloc(nthreads * sizeof(int*)); int **Ct = malloc(nthreads * sizeof(int*)); u64 **Wt = malloc(nthreads * sizeof(u64*)); int **Wk = malloc(nthreads * sizeof(int*));
        long long *t11 = calloc(nthreads, 8), *t00 = calloc(nthreads, 8), *tcap = calloc(nthreads, 8);
        for (int t = 0; t < nthreads; t++) { Rt[t] = calloc(NREP, sizeof(int)); Ct[t] = calloc(NREP, sizeof(int)); Wt[t] = calloc(NREP, 8); Wk[t] = calloc(NREP, sizeof(int)); }
        #pragma omp parallel
        {
            int tid = omp_get_thread_num();
            u64 A[MAXW], B[MAXW], C[MAXW];
            #pragma omp for schedule(dynamic, 4096)
            for (size_t s = 0; s < nstates; s++) {
                const u64 *rec = cur.buf + s * stride;
                memset(A, 0, sizeof A); memset(B, 0, sizeof B);
                memcpy(A, rec, nw * 8); memcpy(B, rec + nw, nw * 8);        /* A = A_m, B = masked A_{m-1} */
                u64 meta = rec[2 * nw + 1]; u64 last = meta & 0xFFF; int streak = (meta >> 16) & 0xFFFF; int k = (int)(meta >> 32);
                int mm = m, steps = 0, E = -1, censored = 0, kind = 0;
                while (1) {
                    next_diag(A, B, nwp, mm + 1, 0, C);                      /* check index */
                    next_diag(C, A, nwp, mm + 2, 0, B);                      /* forced index with y = 0 into B (temp) */
                    int cell = getbit(B, mm + 2);
                    int y = cell;                                            /* whitening bit */
                    if (!allowed(last, k, y)) { E = mm + 2; kind = death_kind(last, k, y); break; }
                    if (y) { /* flip bits 1..mm+2 */
                        for (int i = 0; i < nwp; i++) B[i] ^= ~0ULL;
                        B[0] ^= 1ULL;                                        /* bit 0 stays */
                        int top = mm + 2; int tw = top >> 6;                 /* clear above top */
                        if (tw < nwp) { B[tw] &= (top & 63) == 63 ? ~0ULL : ((1ULL << ((top & 63) + 1)) - 1); for (int i = tw + 1; i < nwp; i++) B[i] = 0; }
                    }
                    last = ((last << 1) | (u64)y) & 0xFFF; k++;
                    /* rotate: new A = B (A_{mm+2}), new B = C (A_{mm+1}) */
                    u64 tmp[MAXW]; memcpy(tmp, A, sizeof tmp); memcpy(A, B, sizeof A); memcpy(B, C, sizeof B);
                    mm += 2; steps += 2;
                    if (steps >= cap) { E = mm + 1; censored = 1; break; }
                }
                if (censored) tcap[tid]++; else if (kind == 1) t11[tid]++; else t00[tid]++;
                int dlo = m - 2 * streak + 1; if (dlo < 1) dlo = 1; int dhi = m + 1;
                for (int d = dlo; d <= dhi; d++) {
                    int r = E - d;
                    if (r > Rt[tid][d] || (r == Rt[tid][d] && censored)) { Rt[tid][d] = r; Ct[tid][d] = censored; Wt[tid][d] = rec[2 * nw]; Wk[tid][d] = k; }
                }
            }
        }
        for (int t = 0; t < nthreads; t++) { for (int d = 0; d < NREP; d++) if (Rt[t][d] > R[d] || (Rt[t][d] == R[d] && Ct[t][d])) { R[d] = Rt[t][d]; CENS[d] = Ct[t][d]; WIT[d] = Wt[t][d]; WITK[d] = Wk[t][d]; } k11 += t11[t]; k00 += t00[t]; kcap += tcap[t]; free(Rt[t]); free(Ct[t]); free(Wt[t]); free(Wk[t]); }
        free(Rt); free(Ct); free(Wt); free(Wk); free(t11); free(t00); free(tcap);
        printf("K %d %lld %lld %lld\n", m, k11, k00, kcap);
        if (m + 2 > MAXM) break;
        /* ---- expand to forced index m+2 ---- */
        int nw2 = (m + 2) / 64 + 1; int stride2 = 2 * nw2 + 2;
        if ((size_t)2 * nstates * stride2 * 8 > MAXSTATES * (size_t)stride2 * 8 * 1) { /* children bound */ }
        if (2 * nstates > MAXSTATES) { printf("STOP %d states %zu would exceed the cap\n", m + 2, 2 * nstates); break; }
        vec *tb = calloc(nthreads, sizeof(vec));
        #pragma omp parallel
        {
            int tid = omp_get_thread_num();
            u64 A[MAXW], B[MAXW], C[MAXW], D[MAXW], rec2[2 * MAXW + 2];
            #pragma omp for schedule(dynamic, 4096)
            for (size_t s = 0; s < nstates; s++) {
                const u64 *rec = cur.buf + s * stride;
                memset(A, 0, sizeof A); memset(B, 0, sizeof B);
                memcpy(A, rec, nw * 8); memcpy(B, rec + nw, nw * 8);
                u64 rep = rec[2 * nw]; u64 meta = rec[2 * nw + 1]; u64 last = meta & 0xFFF; int streak = (meta >> 16) & 0xFFFF; int k = (int)(meta >> 32);
                next_diag(A, B, nw2, m + 1, 0, C);                           /* A_{m+1} */
                for (int y = 0; y < 2; y++) {
                    if (!allowed(last, k, y)) continue;
                    next_diag(C, A, nw2, m + 2, y, D);                       /* A_{m+2} */
                    int white = !getbit(D, m + 2);
                    int ns = white ? streak + 1 : 0;
                    for (int i = 0; i < nw2; i++) rec2[i] = D[i];
                    for (int i = 0; i < nw2; i++) { u64 sh = (D[i] >> 1) | (i + 1 < nw2 ? D[i + 1] << 63 : 0); rec2[nw2 + i] = C[i] & ~sh; }
                    rec2[2 * nw2] = (k < 64) ? (rep | ((u64)y << k)) : rep;
                    rec2[2 * nw2 + 1] = (((last << 1) | (u64)y) & 0xFFF) | ((u64)ns << 16) | ((u64)(k + 1) << 32);
                    vpush(&tb[tid], rec2, stride2);
                }
            }
        }
        size_t total = 0; for (int t = 0; t < nthreads; t++) total += tb[t].n / stride2;
        vec nxt = {0};
        if (NODEDUP) {
            for (int t = 0; t < nthreads; t++) { for (size_t i = 0; i < tb[t].n; i += stride2) vpush(&nxt, tb[t].buf + i, stride2); free(tb[t].buf); }
        } else {
            /* gather, hash, sort by (hash, key), merge keeping the max streak */
            u64 *all = malloc(total * (size_t)stride2 * 8); if (!all) { fprintf(stderr, "out of memory (children)\n"); return 2; }
            size_t off = 0; for (int t = 0; t < nthreads; t++) { memcpy(all + off, tb[t].buf, tb[t].n * 8); off += tb[t].n; free(tb[t].buf); }
            hi *idx = malloc(total * sizeof(hi));
            G_KEYW = 2 * nw2; G_BASE = all; G_STRIDE = stride2;
            #pragma omp parallel for schedule(static)
            for (size_t i = 0; i < total; i++) { const u64 *r = all + i * stride2; u64 h = hash_rec(r, 2 * nw2) ^ (r[2 * nw2 + 1] & 0xFFF) * 0x9E3779B97F4A7C15ULL; idx[i].h = h; idx[i].idx = (uint32_t)i; }
            /* bucket by top 10 bits of the hash, sort buckets in parallel */
            const int NB = 1024; size_t *cnt = calloc(NB + 1, sizeof(size_t));
            for (size_t i = 0; i < total; i++) cnt[(idx[i].h >> 54) + 1]++;
            for (int b = 0; b < NB; b++) cnt[b + 1] += cnt[b];
            hi *sorted = malloc(total * sizeof(hi)); size_t *pos = malloc(NB * sizeof(size_t)); memcpy(pos, cnt, NB * sizeof(size_t));
            for (size_t i = 0; i < total; i++) sorted[pos[idx[i].h >> 54]++] = idx[i];
            free(idx);
            #pragma omp parallel for schedule(dynamic, 1)
            for (int b = 0; b < NB; b++) qsort(sorted + cnt[b], cnt[b + 1] - cnt[b], sizeof(hi), cmp_hi);
            /* merge runs of equal keys (equal hash and key, adjacent after the sort) */
            size_t i = 0;
            while (i < total) {
                size_t j = i + 1;
                u64 *best = all + (size_t)sorted[i].idx * stride2;
                while (j < total && sorted[j].h == sorted[i].h && cmp_hi(&sorted[i], &sorted[j]) == 0) {
                    u64 *r = all + (size_t)sorted[j].idx * stride2;
                    if (((r[2 * nw2 + 1] >> 16) & 0xFFFF) > ((best[2 * nw2 + 1] >> 16) & 0xFFFF)) best = r;
                    j++;
                }
                vpush(&nxt, best, stride2);
                i = j;
            }
            free(sorted); free(cnt); free(pos); free(all);
        }
        free(tb);
        free(cur.buf); cur = nxt; nw = nw2; stride = stride2;
        printf("L %d %zu %zu %.1f\n", m + 2, cur.n / stride, total, omp_get_wtime() - t0); fflush(stdout);
    }
    for (int d = 1; d <= MAXM + 1; d++) {
        if (R[d] <= 0 && !CENS[d]) continue;
        printf("D %d %d %d ", d, R[d], CENS[d]);
        for (int i = 0; i < WITK[d] && i < 64; i++) putchar('0' + ((WIT[d] >> i) & 1));
        putchar('\n');
    }
    printf("DONE %.1f s, %d threads\n", omp_get_wtime() - t0, nthreads);
    return 0;
}
