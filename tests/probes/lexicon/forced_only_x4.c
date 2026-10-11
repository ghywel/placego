/* forced_only_x4.c: the forced-only records R^F(d) of the check-free conjecture (RULE30-PRIZE.md 8.88), exact, by a
 * breadth-first walk over visible prefixes with the record's masked-pair merging (8.38, MG0b), finished by a
 * depth-first tail without merging once the merged levels would exceed memory.  Intel, 2026-10-11.
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
 * same A_{m-1} off those positions and the same language state have the same future. States are merged on that key,
 * keeping the longest streak of white forced cells ending at m and one representative prefix.
 *
 * Languages: x4 = {no 11, no 00000} (the width-4 layer language), gm = {no 11} (the control: infinite in phase 1),
 * maw12 = the twelve minimal absent words of lengths 2..12 of the real visible language, dfa=FILE = a deterministic
 * automaton on visible words (a text file: n, then per state "next0 next1", -1 for no edge; all states accepting;
 * start 0), for the width-8 and width-12 layer languages.
 *
 * usage: forced_only_x4 PHASE LANG MAXM MAXSTATES [NODEDUP] [DFSMAX]
 *   PHASE 0|1; LANG as above; MAXM: last forced index of the merged (breadth-first) stage; MAXSTATES: stop merging
 *   before a level whose children would exceed this many records; NODEDUP 1 disables merging (a control); DFSMAX: if
 *   given and larger than the last merged index, every remaining state is extended depth-first (no merging) to this
 *   forced index, with the path evaluated at every node. Depths are reported to (last index)+1.
 * output: "L m states children seconds" per merged level, "BFSSTOP m states" when merging stops, "D d R cens witness"
 *   per depth, "K m k11 kother kcap" cumulative death kinds (11; other forbidden word; capped), "DONE".
 * Compile with the OpenMP line of COMMON rule 3 (Apple clang needs libomp).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <omp.h>

#define MAXW 16                      /* anti-diagonal words for the forced path: up to 1024 bits */
typedef uint64_t u64;

static int PHASE, LANG;              /* LANG: 0 x4, 1 gm, 2 maw12, 3 dfa */
static const char *MAW[12] = {"11","00000","101001","0100101","010010001","0101000101","0101010000",
                              "01010001001","10010001001","010010000101","010100010001","100100010000"};
static int MAWLEN[12]; static u64 MAWVAL[12];
static int DFAN = 0; static int *DFA = NULL;   /* DFA[2*s + b] */

static inline int wall(int t) { return PHASE == 0 ? (t & 1) : 1 - (t & 1); }

/* language state ls: for x4/gm/maw12 the last 12 visible bits (most recent at bit 0) with k = count; for dfa the state id.
 * allowed(ls, k, y) -> 1 if y may follow; next_ls(ls, y) -> the new language state */
static inline int allowed(u64 ls, int k, int y) {
    if (LANG == 3) return DFA[2 * (int)ls + y] >= 0;
    u64 s = (ls << 1) | (u64)y;
    if (LANG == 1) return !(k >= 1 && (s & 3) == 3);
    if (LANG == 0) { if (k >= 1 && (s & 3) == 3) return 0; if (k >= 4 && (s & 31) == 0) return 0; return 1; }
    for (int i = 0; i < 12; i++) { int L = MAWLEN[i]; if (k + 1 >= L && (s & ((1ULL << L) - 1)) == MAWVAL[i]) return 0; }
    return 1;
}
static inline u64 next_ls(u64 ls, int y) { return LANG == 3 ? (u64)DFA[2 * (int)ls + y] : (((ls << 1) | (u64)y) & 0xFFF); }
static inline int death_kind(u64 ls, int k, int y) {
    if (LANG == 3) return 2;
    u64 s = (ls << 1) | (u64)y; return (k >= 1 && (s & 3) == 3) ? 1 : 2;
}

static inline void prefix_xor(u64 *v, int nw) {
    u64 carry = 0;
    for (int i = 0; i < nw; i++) {
        u64 x = v[i];
        x ^= x << 1; x ^= x << 2; x ^= x << 4; x ^= x << 8; x ^= x << 16; x ^= x << 32;
        x ^= carry; carry = (u64)0 - (x >> 63); v[i] = x;
    }
}
/* A_m from A_{m-1} (a1) and A_{m-2} (a2); bits above m cleared */
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

/* ---- per-thread result arrays ---- */
typedef struct { int *R, *C, *Wk; u64 *W; long long k11, k00, kcap; } res_t;
static int NREP;
static void res_init(res_t *r) { r->R = calloc(NREP, sizeof(int)); r->C = calloc(NREP, sizeof(int)); r->Wk = calloc(NREP, sizeof(int)); r->W = calloc(NREP, 8); r->k11 = r->k00 = r->kcap = 0; }
static void res_merge(res_t *g, const res_t *t) {
    for (int d = 0; d < NREP; d++) if (t->R[d] > g->R[d] || (t->R[d] == g->R[d] && t->C[d] && t->R[d] > 0)) { g->R[d] = t->R[d]; g->C[d] = t->C[d]; g->W[d] = t->W[d]; g->Wk[d] = t->Wk[d]; }
    g->k11 += t->k11; g->k00 += t->k00; g->kcap += t->kcap;
}

/* the forced-only path from (A = A_m, B = masked A_{m-1}); contributes to depths m-2*streak+1 .. m+1 */
static void eval_path(const u64 *Ain, const u64 *Bin, int nw, int m, u64 ls, int k, int streak, u64 rep, res_t *r) {
    u64 A[MAXW], B[MAXW], C[MAXW];
    int nwp = (4 * m + 400) / 64 + 1; if (nwp > MAXW) nwp = MAXW;
    int cap = 3 * m + 300;
    memset(A, 0, sizeof A); memset(B, 0, sizeof B); memcpy(A, Ain, nw * 8); memcpy(B, Bin, nw * 8);
    int mm = m, steps = 0, E, censored = 0, kind = 0;
    while (1) {
        next_diag(A, B, nwp, mm + 1, 0, C);           /* check index */
        next_diag(C, A, nwp, mm + 2, 0, B);           /* forced index, y = 0 */
        int y = getbit(B, mm + 2);                    /* whitening bit */
        if (!allowed(ls, k, y)) { E = mm + 2; kind = death_kind(ls, k, y); break; }
        if (y) { int top = mm + 2; for (int i = 0; i < nwp; i++) B[i] ^= ~0ULL; B[0] ^= 1ULL;
                 int tw = top >> 6; if (tw < nwp) { B[tw] &= ((top & 63) == 63) ? ~0ULL : ((1ULL << ((top & 63) + 1)) - 1); for (int i = tw + 1; i < nwp; i++) B[i] = 0; } }
        ls = next_ls(ls, y); k++;
        memcpy(A, B, sizeof A); memcpy(B, C, sizeof B);
        mm += 2; steps += 2;
        if (steps >= cap) { E = mm + 1; censored = 1; break; }
    }
    if (censored) r->kcap++; else if (kind == 1) r->k11++; else r->k00++;
    int dlo = m - 2 * streak + 1; if (dlo < 1) dlo = 1; int dhi = m + 1;
    for (int d = dlo; d <= dhi && d < NREP; d++) {
        int rr = E - d;
        if (rr > r->R[d] || (rr == r->R[d] && censored)) { r->R[d] = rr; r->C[d] = censored; r->W[d] = rep; r->Wk[d] = k; }
    }
}

/* depth-first tail: from a node at forced index m, expand to DFSMAX, evaluating every node */
static int DFSMAX;
static void dfs(const u64 *A, const u64 *B, int nw, int m, u64 ls, int k, int streak, u64 rep, res_t *r) {
    eval_path(A, B, nw, m, ls, k, streak, rep, r);
    if (m + 2 > DFSMAX) return;
    int nw2 = (m + 2) / 64 + 1;
    u64 C[MAXW], D[MAXW], Bm[MAXW];
    memset(C, 0, sizeof C);
    next_diag(A, B, nw2, m + 1, 0, C);
    for (int y = 0; y < 2; y++) {
        if (!allowed(ls, k, y)) continue;
        next_diag(C, A, nw2, m + 2, y, D);
        int white = !getbit(D, m + 2);
        for (int i = 0; i < nw2; i++) { u64 sh = (D[i] >> 1) | (i + 1 < nw2 ? D[i + 1] << 63 : 0); Bm[i] = C[i] & ~sh; }
        dfs(D, Bm, nw2, m + 2, next_ls(ls, y), k + 1, white ? streak + 1 : 0, (k < 64) ? (rep | ((u64)y << k)) : rep, r);
    }
}

/* ---- state records for the merged stage: [A_m (nw)] [A_{m-1} masked (nw)] [rep] [meta] ; meta = ls | streak<<16 | k<<32 */
typedef struct { u64 *buf; size_t n, cap; } vec;
static void vpush(vec *v, const u64 *rec, int stride) {
    if (v->n + stride > v->cap) { v->cap = v->cap ? v->cap * 2 : (size_t)stride * 1024; v->buf = realloc(v->buf, v->cap * 8); if (!v->buf) { fprintf(stderr, "out of memory\n"); exit(2); } }
    memcpy(v->buf + v->n, rec, stride * 8); v->n += stride;
}
static int G_KEYW; static const u64 *G_BASE; static int G_STRIDE;
typedef struct { u64 h; uint32_t idx; } hi;
static int cmp_hi(const void *pa, const void *pb) {
    const hi *a = pa, *b = pb;
    if (a->h != b->h) return a->h < b->h ? -1 : 1;
    const u64 *ra = G_BASE + (size_t)a->idx * G_STRIDE, *rb = G_BASE + (size_t)b->idx * G_STRIDE;
    for (int i = 0; i < G_KEYW; i++) if (ra[i] != rb[i]) return ra[i] < rb[i] ? -1 : 1;
    u64 la = ra[G_KEYW + 1] & 0xFFFF, lb = rb[G_KEYW + 1] & 0xFFFF;
    return la == lb ? 0 : (la < lb ? -1 : 1);
}
static inline u64 hash_rec(const u64 *r, int keywords) {
    u64 h = 0x9E3779B97F4A7C15ULL ^ (r[keywords + 1] & 0xFFFF);
    for (int i = 0; i < keywords; i++) { h ^= r[i]; h *= 0xBF58476D1CE4E5B9ULL; h ^= h >> 31; }
    return h;
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: %s PHASE LANG MAXM MAXSTATES [NODEDUP] [DFSMAX]\n", argv[0]); return 1; }
    PHASE = atoi(argv[1]);
    if (!strcmp(argv[2], "x4")) LANG = 0; else if (!strcmp(argv[2], "gm")) LANG = 1; else if (!strcmp(argv[2], "maw12")) LANG = 2;
    else if (!strncmp(argv[2], "dfa=", 4)) {
        LANG = 3; FILE *f = fopen(argv[2] + 4, "r"); if (!f) { fprintf(stderr, "cannot open %s\n", argv[2] + 4); return 1; }
        if (fscanf(f, "%d", &DFAN) != 1) return 1; DFA = malloc(2 * DFAN * sizeof(int));
        for (int i = 0; i < DFAN; i++) if (fscanf(f, "%d %d", &DFA[2 * i], &DFA[2 * i + 1]) != 2) return 1;
        fclose(f);
    } else { fprintf(stderr, "unknown language\n"); return 1; }
    int MAXM = atoi(argv[3]); size_t MAXSTATES = strtoull(argv[4], 0, 10);
    int NODEDUP = argc > 5 ? atoi(argv[5]) : 0; DFSMAX = argc > 6 ? atoi(argv[6]) : 0;
    for (int i = 0; i < 12; i++) { MAWLEN[i] = strlen(MAW[i]); u64 v = 0; for (int j = 0; j < MAWLEN[i]; j++) v = (v << 1) | (MAW[i][j] - '0'); MAWVAL[i] = v; }
    int nthreads = omp_get_max_threads();
    int m0 = (PHASE == 0) ? 1 : 2;
    int nw = 1, stride = 2 * nw + 2;
    NREP = (DFSMAX > MAXM ? DFSMAX : MAXM) + 4;
    vec cur = {0};
    {   /* initial states at the first forced index */
        u64 A0[MAXW] = {0}, Am1[MAXW] = {0}, A1[MAXW] = {0}, A2[MAXW] = {0}, rec[64];
        A0[0] = wall(0);
        if (PHASE == 0) {
            for (int y = 0; y < 2; y++) {
                if (!allowed(0, 0, y)) continue;
                next_diag(A0, Am1, nw, 1, y, A1);
                int white = !getbit(A1, 1);
                memset(rec, 0, sizeof rec); rec[0] = A1[0]; rec[1] = A0[0] & ~(A1[0] >> 1); rec[2] = (u64)y; rec[3] = next_ls(0, y) | ((u64)white << 16) | (1ULL << 32);
                vpush(&cur, rec, stride);
            }
        } else {
            next_diag(A0, Am1, nw, 1, 0, A1);
            for (int y = 0; y < 2; y++) {
                if (!allowed(0, 0, y)) continue;
                next_diag(A1, A0, nw, 2, y, A2);
                int white = !getbit(A2, 2);
                memset(rec, 0, sizeof rec); rec[0] = A2[0]; rec[1] = A1[0] & ~(A2[0] >> 1); rec[2] = (u64)y; rec[3] = next_ls(0, y) | ((u64)white << 16) | (1ULL << 32);
                vpush(&cur, rec, stride);
            }
        }
    }
    res_t G; res_init(&G);
    res_t *T = malloc(nthreads * sizeof(res_t)); for (int t = 0; t < nthreads; t++) res_init(&T[t]);
    double t0 = omp_get_wtime();
    int m = m0, lastm = m0;
    for (; m <= MAXM; m += 2) {
        size_t nstates = cur.n / stride; lastm = m;
        #pragma omp parallel
        {
            int tid = omp_get_thread_num();
            #pragma omp for schedule(dynamic, 2048)
            for (size_t s = 0; s < nstates; s++) {
                const u64 *rec = cur.buf + s * stride; u64 meta = rec[2 * nw + 1];
                eval_path(rec, rec + nw, nw, m, meta & 0xFFFF, (int)(meta >> 32), (int)((meta >> 16) & 0xFFFF), rec[2 * nw], &T[tid]);
            }
        }
        if (m + 2 > MAXM) break;
        if (2 * nstates > MAXSTATES) { printf("BFSSTOP %d %zu\n", m, nstates); break; }
        int nw2 = (m + 2) / 64 + 1, stride2 = 2 * nw2 + 2;
        vec *tb = calloc(nthreads, sizeof(vec));
        #pragma omp parallel
        {
            int tid = omp_get_thread_num();
            u64 A[MAXW], B[MAXW], C[MAXW], D[MAXW], rec2[2 * MAXW + 2];
            #pragma omp for schedule(dynamic, 2048)
            for (size_t s = 0; s < nstates; s++) {
                const u64 *rec = cur.buf + s * stride;
                memset(A, 0, sizeof A); memset(B, 0, sizeof B); memcpy(A, rec, nw * 8); memcpy(B, rec + nw, nw * 8);
                u64 rep = rec[2 * nw], meta = rec[2 * nw + 1], ls = meta & 0xFFFF; int streak = (meta >> 16) & 0xFFFF, k = (int)(meta >> 32);
                next_diag(A, B, nw2, m + 1, 0, C);
                for (int y = 0; y < 2; y++) {
                    if (!allowed(ls, k, y)) continue;
                    next_diag(C, A, nw2, m + 2, y, D);
                    int white = !getbit(D, m + 2), ns = white ? streak + 1 : 0;
                    for (int i = 0; i < nw2; i++) rec2[i] = D[i];
                    for (int i = 0; i < nw2; i++) { u64 sh = (D[i] >> 1) | (i + 1 < nw2 ? D[i + 1] << 63 : 0); rec2[nw2 + i] = C[i] & ~sh; }
                    rec2[2 * nw2] = (k < 64) ? (rep | ((u64)y << k)) : rep;
                    rec2[2 * nw2 + 1] = next_ls(ls, y) | ((u64)ns << 16) | ((u64)(k + 1) << 32);
                    vpush(&tb[tid], rec2, stride2);
                }
            }
        }
        size_t total = 0; for (int t = 0; t < nthreads; t++) total += tb[t].n / stride2;
        vec nxt = {0};
        if (NODEDUP) {
            for (int t = 0; t < nthreads; t++) { for (size_t i = 0; i < tb[t].n; i += stride2) vpush(&nxt, tb[t].buf + i, stride2); free(tb[t].buf); }
        } else {
            u64 *all = malloc(total * (size_t)stride2 * 8); if (!all) { fprintf(stderr, "out of memory (children)\n"); return 2; }
            size_t off = 0; for (int t = 0; t < nthreads; t++) { memcpy(all + off, tb[t].buf, tb[t].n * 8); off += tb[t].n; free(tb[t].buf); }
            hi *idx = malloc(total * sizeof(hi)); G_KEYW = 2 * nw2; G_BASE = all; G_STRIDE = stride2;
            #pragma omp parallel for schedule(static)
            for (size_t i = 0; i < total; i++) { idx[i].h = hash_rec(all + i * stride2, 2 * nw2); idx[i].idx = (uint32_t)i; }
            const int NB = 1024; size_t *cnt = calloc(NB + 1, sizeof(size_t));
            for (size_t i = 0; i < total; i++) cnt[(idx[i].h >> 54) + 1]++;
            for (int b = 0; b < NB; b++) cnt[b + 1] += cnt[b];
            hi *sorted = malloc(total * sizeof(hi)); size_t *pos = malloc(NB * sizeof(size_t)); memcpy(pos, cnt, NB * sizeof(size_t));
            for (size_t i = 0; i < total; i++) sorted[pos[idx[i].h >> 54]++] = idx[i];
            free(idx);
            #pragma omp parallel for schedule(dynamic, 1)
            for (int b = 0; b < NB; b++) qsort(sorted + cnt[b], cnt[b + 1] - cnt[b], sizeof(hi), cmp_hi);
            size_t i = 0;
            while (i < total) {
                size_t j = i + 1; u64 *best = all + (size_t)sorted[i].idx * stride2;
                while (j < total && sorted[j].h == sorted[i].h && cmp_hi(&sorted[i], &sorted[j]) == 0) {
                    u64 *r = all + (size_t)sorted[j].idx * stride2;
                    if (((r[2 * nw2 + 1] >> 16) & 0xFFFF) > ((best[2 * nw2 + 1] >> 16) & 0xFFFF)) best = r;
                    j++;
                }
                vpush(&nxt, best, stride2); i = j;
            }
            free(sorted); free(cnt); free(pos); free(all);
        }
        free(tb); free(cur.buf); cur = nxt; nw = nw2; stride = stride2;
        printf("L %d %zu %zu %.1f\n", m + 2, cur.n / stride, total, omp_get_wtime() - t0); fflush(stdout);
    }
    /* depth-first tail from the last merged level */
    if (DFSMAX > lastm) {
        size_t nstates = cur.n / stride;
        printf("DFS from %d to %d over %zu states\n", lastm, DFSMAX, nstates); fflush(stdout);
        #pragma omp parallel
        {
            int tid = omp_get_thread_num();
            #pragma omp for schedule(dynamic, 64)
            for (size_t s = 0; s < nstates; s++) {
                const u64 *rec = cur.buf + s * stride; u64 meta = rec[2 * nw + 1];
                u64 A[MAXW], B[MAXW]; memset(A, 0, sizeof A); memset(B, 0, sizeof B); memcpy(A, rec, nw * 8); memcpy(B, rec + nw, nw * 8);
                /* the node itself was evaluated in the merged stage; expand its children */
                int m2 = lastm + 2, nw2 = m2 / 64 + 1; u64 C[MAXW], D[MAXW], Bm[MAXW]; memset(C, 0, sizeof C);
                u64 ls = meta & 0xFFFF; int k = (int)(meta >> 32), streak = (int)((meta >> 16) & 0xFFFF); u64 rep = rec[2 * nw];
                next_diag(A, B, nw2, lastm + 1, 0, C);
                for (int y = 0; y < 2; y++) {
                    if (!allowed(ls, k, y)) continue;
                    next_diag(C, A, nw2, m2, y, D);
                    int white = !getbit(D, m2);
                    for (int i = 0; i < nw2; i++) { u64 sh = (D[i] >> 1) | (i + 1 < nw2 ? D[i + 1] << 63 : 0); Bm[i] = C[i] & ~sh; }
                    dfs(D, Bm, nw2, m2, next_ls(ls, y), k + 1, white ? streak + 1 : 0, (k < 64) ? (rep | ((u64)y << k)) : rep, &T[tid]);
                }
            }
        }
        lastm = DFSMAX;
    }
    for (int t = 0; t < nthreads; t++) res_merge(&G, &T[t]);
    printf("K %d %lld %lld %lld\n", lastm, G.k11, G.k00, G.kcap);
    for (int d = 1; d <= lastm + 1 && d < NREP; d++) {
        if (G.R[d] <= 0 && !G.C[d]) continue;
        printf("D %d %d %d ", d, G.R[d], G.C[d]);
        for (int i = 0; i < G.Wk[d] && i < 64; i++) putchar('0' + ((G.W[d] >> i) & 1));
        putchar('\n');
    }
    printf("DONE %.1f s, %d threads\n", omp_get_wtime() - t0, nthreads);
    return 0;
}
