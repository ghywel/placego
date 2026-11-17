/* ladder_deep.c: ladder.c's R(M, S), deeper and in parallel (Local, 2026-10-05; RULE30-PRIZE.md section 8.56).
 * The same definition and the same numbers as ladder.c: R(M, S) is the longest run of zeros the forced left half for
 * 0101... can be held to, starting at depth S, over every start of a width-M layer (cells 1..M) and every input
 * sequence in column M + 1. A finite R(M, S) for one M proves that no configuration, with any right half at all, has
 * column 0 = 0101... from time 0 and its leftmost black cell less than S cells to the left of column 0.
 *
 * BUILD (macOS, Homebrew libomp):
 *   cc -O3 -mcpu=apple-m1 -Xpreprocessor -fopenmp -I/opt/homebrew/opt/libomp/include -L/opt/homebrew/opt/libomp/lib \
 *      -lomp -o ladder_deep tests/probes/lexicon/ladder_deep.c           (add -DNW=6 for depths to 382)
 * BUILD (Linux): cc -O3 -fopenmp -o ladder_deep tests/probes/lexicon/ladder_deep.c
 * USAGE:  ./ladder_deep M S [THREADS]
 *         prints "H M S length groups" lines, then
 *         "R M S = best (at_best of groups start groups reach it); nodes N; members K; cap C [CAPPED]"
 *
 * What differs from ladder.c, and nothing else:
 * 1. Depth. The anti-diagonals are NW 64-bit words (default 4: depths to 254), not one 128-bit word (126).
 * 2. No table of start groups. A start group is a visible prefix of column 1 together with the set of layer states
 *    that can show it. Each group has exactly one parent (its prefix without the last bit), so the groups form a
 *    tree, and a depth-first walk visits every group once and holds one branch in memory. ladder.c builds the same
 *    tree level by level in a hash table, which is what limited its depth by memory.
 * 3. Threads. The tree is walked breadth-first to a level with enough groups, and those subtrees are shared out.
 * The layer step is computed from the state's bits, not from a table: cell i's next value is its left neighbour XOR
 * (itself OR its right neighbour), with column 0's value on the left and the input bit on the right.
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

#ifndef NW
#define NW 4
#endif
#define CAP (64 * NW - 2)                      /* deepest depth representable: a_t has bits 1 .. t + 1 */
typedef struct { uint64_t w[NW]; } V;

static inline int tau(int t) { return t < 0 ? 0 : (t & 1); }

static inline uint64_t prefix_xor64(uint64_t x) {
#ifdef HAVE_PMULL
    return (uint64_t)vmull_p64((poly64_t)x, (poly64_t)~0ULL);
#else
    x ^= x << 1; x ^= x << 2; x ^= x << 4; x ^= x << 8; x ^= x << 16; x ^= x << 32;
    return x;
#endif
}

/* a_t from a1 = a_{t-1}, a2 = a_{t-2} and sigma(t): ladder.c's left_step, on NW words */
static inline V left_step(const V *a1, const V *a2, int t, int sigma) {
    V r;
    int nw = ((t + 1) >> 6) + 1;                              /* bits 0 .. t + 1 */
    if (nw > NW) nw = NW;
    uint64_t c1 = 0, c2 = 0;
    for (int i = 0; i < nw; i++) {
        uint64_t p = a1->w[i], q = a2->w[i];
        r.w[i] = (p << 1 | c1) | (q << 2 | c2);
        c1 = p >> 63; c2 = q >> 62;
    }
    for (int i = nw; i < NW; i++) r.w[i] = 0;
    r.w[0] |= (uint64_t)tau(t - 1) << 2;
    r.w[0] &= ~3ULL;
    r.w[0] |= (uint64_t)(tau(t + 1) ^ (tau(t) | sigma)) << 1;
    uint64_t carry = 0;
    for (int i = 0; i < nw; i++) {
        uint64_t y = prefix_xor64(r.w[i]) ^ carry;
        carry = (uint64_t)0 - (y >> 63);
        r.w[i] = y;
    }
    int top = (t + 1) & 63;                                   /* keep bits 0 .. t + 1, clear bit 0 */
    if (top < 63) r.w[nw - 1] &= (2ULL << top) - 1;
    r.w[0] &= ~1ULL;
    return r;
}
static inline int vbit(const V *a, int j) { return (int)((a->w[j >> 6] >> (j & 63)) & 1); }

static int M, S;
static uint32_t MMASK;
static inline uint32_t layer_next(uint32_t s, int tv, int u) {
    uint32_t l = (s << 1) | (uint32_t)tv;
    uint32_t r = (s >> 1) | ((uint32_t)u << (M - 1));
    return (l ^ (s | r)) & MMASK;
}

typedef struct {
    uint32_t *stamp; uint32_t gen;                 /* per-thread duplicate filter over the 2^M states */
    uint32_t **lvl; size_t *lvl_cap;               /* the member lists of the branch being walked, one per level */
    uint32_t *ra, *rb;                             /* scratch for the run */
    long long hist[CAP + 2], groups, nodes, members, at_best;
    int best, capped;
} Ctx;

static void ctx_init(Ctx *c) {
    memset(c, 0, sizeof *c);
    size_t n = (size_t)1 << M;
    c->stamp = calloc(n, 4); c->ra = malloc(n * 4 + 4); c->rb = malloc(n * 4 + 4);
    c->lvl = calloc((size_t)S + 2, sizeof(uint32_t *)); c->lvl_cap = calloc((size_t)S + 2, sizeof(size_t));
    if (!c->stamp || !c->ra || !c->rb || !c->lvl || !c->lvl_cap) { fprintf(stderr, "out of memory\n"); exit(3); }
}

/* the image of src[0..n) under one layer step with column 0 = tv and both inputs, without duplicates, into dst */
static inline size_t image(Ctx *c, const uint32_t *src, size_t n, int tv, uint32_t *dst) {
    if (++c->gen == 0) { memset(c->stamp, 0, ((size_t)1 << M) * 4); c->gen = 1; }
    size_t k = 0;
    for (size_t i = 0; i < n; i++)
        for (int u = 0; u < 2; u++) {
            uint32_t x = layer_next(src[i], tv, u);
            if (c->stamp[x] != c->gen) { c->stamp[x] = c->gen; dst[k++] = x; }
        }
    return k;
}

/* the run from depth S for one start group: ladder.c's second loop */
static void run_group(Ctx *c, V a1, V a2, const uint32_t *set, size_t n) {
    uint32_t *cur = c->ra, *nxt = c->rb;
    if (M > 0) memcpy(cur, set, n * 4);
    int runlen = 0;
    for (int t = S - 1; t + 1 <= CAP; t++) {
        int sg = 0;
        if (t % 2 == 0) {
            V a0 = left_step(&a1, &a2, t, 0);
            sg = vbit(&a0, t + 1);
            if (M > 0) {
                size_t k = 0;
                for (size_t i = 0; i < n; i++) if ((int)(cur[i] & 1) == sg) cur[k++] = cur[i];
                n = k;
                if (!n) break;
            }
        }
        V a = left_step(&a1, &a2, t, sg);
        if (vbit(&a, t + 1)) break;
        a2 = a1; a1 = a;
        runlen++;
        if (M > 0) { n = image(c, cur, n, tau(t), nxt); uint32_t *sw = cur; cur = nxt; nxt = sw; }
    }
    if (S - 1 + runlen >= CAP) c->capped = 1;
    c->groups++;
    c->hist[runlen]++;
    if (runlen > c->best) { c->best = runlen; c->at_best = 0; }
    if (runlen == c->best) c->at_best++;
}

/* the tree of start groups, depth first, from time t with the group's layer states in set[0..n) */
static void dfs(Ctx *c, int t, V a1, V a2, const uint32_t *set, size_t n) {
    c->nodes++; c->members += (long long)n;
    if (t == S - 1) { run_group(c, a1, a2, set, n); return; }
    size_t need = 2 * n + 2, full = ((size_t)1 << M) + 2;      /* an image has at most min(2n, 2^M) states */
    if (need > full) need = full;
    if (c->lvl_cap[t + 1] < need) {                            /* this level's list is free: its users have returned */
        free(c->lvl[t + 1]);
        c->lvl[t + 1] = malloc(need * 4); c->lvl_cap[t + 1] = need;
        if (!c->lvl[t + 1]) { fprintf(stderr, "out of memory\n"); exit(3); }
    }
    uint32_t *sub = c->lvl[t + 1];
    if (t % 2 == 0) {
        for (int sg = 0; sg < 2; sg++) {
            size_t k;
            if (M == 0) k = 1;
            else {                                             /* the states that show sg in column 1, stepped */
                size_t m = 0;
                uint32_t *tmp = c->ra;                         /* free here: the run uses it only at the leaves */
                for (size_t i = 0; i < n; i++) if ((int)(set[i] & 1) == sg) tmp[m++] = set[i];
                if (!m) continue;
                k = image(c, tmp, m, tau(t), sub);
            }
            V a = left_step(&a1, &a2, t, sg);
            dfs(c, t + 1, a, a1, sub, k);
        }
    } else {
        size_t k = (M == 0) ? 1 : image(c, set, n, tau(t), sub);
        V a = left_step(&a1, &a2, t, 0);
        dfs(c, t + 1, a, a1, sub, k);
    }
}

typedef struct { int t; V a1, a2; uint32_t *set; size_t n; } Task;

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: ladder_deep M S [THREADS]\n"); return 2; }
    M = atoi(argv[1]); S = atoi(argv[2]);
    int threads = argc > 3 ? atoi(argv[3]) : 1;
    if (M < 0 || M > 24 || S < 2 || S > CAP - 2) { fprintf(stderr, "M or S out of range (cap %d)\n", CAP); return 2; }
    MMASK = M ? ((1u << M) - 1) : 0;
#ifdef _OPENMP
    omp_set_num_threads(threads);
#endif
    /* breadth-first to a level with enough groups (or to the leaves) */
    size_t nstates = (size_t)1 << M, ntask = 1, want = 4096;
    Task *tasks = malloc(sizeof(Task));
    memset(tasks, 0, sizeof(Task));
    tasks[0].t = 0; tasks[0].n = M ? nstates : 1;
    tasks[0].set = malloc(tasks[0].n * 4);
    for (size_t i = 0; i < tasks[0].n; i++) tasks[0].set[i] = (uint32_t)i;
    Ctx seq; ctx_init(&seq);
    long long pre_nodes = 0, pre_members = 0;
    while (ntask < want && tasks[0].t < S - 1) {
        int t = tasks[0].t;
        Task *nt = malloc(sizeof(Task) * (2 * ntask + 1));
        size_t k = 0;
        for (size_t i = 0; i < ntask; i++) {
            Task *p = &tasks[i];
            pre_nodes++; pre_members += (long long)p->n;
            for (int sg = 0; sg < ((t % 2 == 0) ? 2 : 1); sg++) {
                uint32_t *dst = malloc((2 * p->n + 2) * 4);
                size_t m;
                if (M == 0) m = 1;
                else if (t % 2 == 0) {
                    size_t q = 0;
                    for (size_t j = 0; j < p->n; j++) if ((int)(p->set[j] & 1) == sg) seq.ra[q++] = p->set[j];
                    if (!q) { free(dst); continue; }
                    m = image(&seq, seq.ra, q, tau(t), dst);
                } else m = image(&seq, p->set, p->n, tau(t), dst);
                nt[k].t = t + 1; nt[k].a1 = left_step(&p->a1, &p->a2, t, (t % 2 == 0) ? sg : 0); nt[k].a2 = p->a1;
                nt[k].set = dst; nt[k].n = m; k++;
            }
            free(p->set);
        }
        free(tasks); tasks = nt; ntask = k;
    }
    long long hist[CAP + 2]; memset(hist, 0, sizeof hist);
    long long groups = 0, nodes = pre_nodes, members = pre_members, at_best = 0;
    int best = 0, capped = 0;
    #pragma omp parallel
    {
        Ctx c; ctx_init(&c);
        #pragma omp for schedule(dynamic, 1)
        for (size_t i = 0; i < ntask; i++) dfs(&c, tasks[i].t, tasks[i].a1, tasks[i].a2, tasks[i].set, tasks[i].n);
        #pragma omp critical
        {
            for (int r = 0; r <= CAP + 1; r++) hist[r] += c.hist[r];
            groups += c.groups; nodes += c.nodes; members += c.members; capped |= c.capped;
            if (c.best > best) { best = c.best; at_best = 0; }
            if (c.best == best) at_best += c.at_best;
        }
    }
    for (int r = 0; r <= best; r++) printf("H %d %d %d %lld\n", M, S, r, hist[r]);
    printf("R M %d S %d = %d%s (%lld of %lld start groups reach it); nodes %lld; members %lld; cap %d\n", M, S, best,
           capped ? " CAPPED" : "", at_best, groups, nodes, members, CAP);
    return 0;
}
