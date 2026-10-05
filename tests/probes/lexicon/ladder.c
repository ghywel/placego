/* ladder.c: the first rungs of the LR_m ladder (PRIZE-PROBLEMS.md section 8.11), for the trace 0101...
 *
 * BUILD:   cc -O2 -o ladder tests/probes/lexicon/ladder.c      (driven by rule30_ladder.py, which builds it itself)
 * USAGE:   ./ladder run M S        R(M, S): the longest run of zeros the forced left half can be held to, starting at
 *                                  depth S, over every start of cells 1..M and every input sequence in column M + 1
 *          ./ladder hist M S       as run, and also the number of start groups whose run has each length
 *                                  (lines "H M S length groups"; used by rule30_ladder_budget.py)
 *          ./ladder keys M S MIN   as run, and also every start group whose run is at least MIN cells
 *                                  (lines "K M S key length"; bit j of key is column 1 at time 2j)
 *          ./ladder merge M S      as run, and also the number of distinct left-side states (a_{S-2}, a_{S-3}) the
 *                                  start groups lead to, and the run-length histogram over distinct states
 *                                  (lines "D M S distinct N", "DH M S length states", "DX M S conflicts N": at M = 0
 *                                  equal states must give equal runs, so conflicts must be 0)
 *          ./ladder left BITS      the forced left half L(1..n) for a given column 1 (a self-test of the recursion)
 *
 * The left half without columns. The cells x(-j, i) with j + i = t + 1 form an anti-diagonal a_t, a_t[j] =
 * x(-j, t + 1 - j), j = 1..t + 1, known once sigma(0..t) is. Inverting Rule 30 to the left,
 *     a_t[1] = tau(t+1) XOR (tau(t) OR sigma(t)),
 *     a_t[j] = a_t[j-1] XOR ( a_{t-1}[j-1] OR (j = 2 ? tau(t-1) : a_{t-2}[j-2]) ),   j >= 2,
 * so a_t is a prefix XOR, and L(t+1) = a_t[t+1].
 *
 * Why the search is small (Lemma 4). Inside a zero run, every linear cell (t even for 0101...) forces sigma(t): L(t+1)
 * = sigma(t) XOR (its value with sigma(t) = 0). The left side's state along the run is therefore fixed by where the
 * run starts. The only freedom left is which of the layer's 2^M states can still produce the demanded bits. A run is
 * a breadth-first search over at most 2^M states per step, and the starts are grouped by the column-1 bits the left
 * side can see (the even times before S).
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned __int128 u128;
#define CAP 126                              /* deepest depth representable (bits 1..127 of a u128) */

static inline int tau(int t) { return t < 0 ? 0 : (t & 1); }

static inline u128 prefix_xor(u128 v) {
    v ^= v << 1; v ^= v << 2; v ^= v << 4; v ^= v << 8; v ^= v << 16; v ^= v << 32; v ^= v << 64;
    return v;
}

/* a_t from a_{t-1} = a1, a_{t-2} = a2 and sigma(t) */
static inline u128 left_step(u128 a1, u128 a2, int t, int sigma) {
    u128 b1 = (u128)(tau(t + 1) ^ (tau(t) | sigma)) << 1;
    u128 X = (a2 << 2) | ((u128)tau(t - 1) << 2);
    u128 G = ((a1 << 1) | X) & ~(u128)3;              /* bits 2..t+1 */
    u128 mask = (t + 2 >= 128) ? ~(u128)0 : (((u128)1 << (t + 2)) - 1);
    return prefix_xor(G | b1) & mask & ~(u128)1;
}

static int M;
static int HIST;                              /* print the run-length histogram as well */
static int KEYMIN = -1;                       /* print the start groups whose run is at least this long */
static int MERGE;                             /* count distinct left-side states */
typedef struct { u128 a1, a2; int run; char used; } mslot;
static mslot *MS; static size_t MCAP, MN; static long long MCONFLICT;
static void m_add(u128 a1, u128 a2, int run) {
    if (2 * (MN + 1) > MCAP) {                 /* grow */
        size_t oc = MCAP; mslot *old = MS;
        MCAP = MCAP ? 2 * MCAP : 1024; MS = calloc(MCAP, sizeof(mslot)); MN = 0;
        if (!MS) { fprintf(stderr, "out of memory\n"); exit(3); }
        for (size_t i = 0; i < oc; i++) if (old[i].used) m_add(old[i].a1, old[i].a2, old[i].run);
        free(old);
    }
    uint64_t k = (uint64_t)a1 ^ (uint64_t)(a1 >> 64) * 31 ^ (uint64_t)a2 * 0x9E3779B97F4A7C15ULL ^ (uint64_t)(a2 >> 64);
    size_t h = (size_t)((k * 0x9E3779B97F4A7C15ULL) >> 11) & (MCAP - 1);
    while (MS[h].used && !(MS[h].a1 == a1 && MS[h].a2 == a2)) h = (h + 1) & (MCAP - 1);
    if (!MS[h].used) { MS[h].used = 1; MS[h].a1 = a1; MS[h].a2 = a2; MS[h].run = run; MN++; }
    else if (MS[h].run != run) { MCONFLICT++; if (run > MS[h].run) MS[h].run = run; }
}
static int *NXT;                              /* NXT[(s*2 + tau)*2 + u] */

static void build_layer(void) {
    int n = 1 << M;
    NXT = malloc(sizeof(int) * n * 4);
    for (int s = 0; s < n; s++)
        for (int tv = 0; tv < 2; tv++)
            for (int u = 0; u < 2; u++) {
                int out = 0;
                for (int i = 1; i <= M; i++) {          /* cell i of the layer is bit i-1 */
                    int l = (i == 1) ? tv : (s >> (i - 2)) & 1;
                    int c = (s >> (i - 1)) & 1;
                    int r = (i == M) ? u : (s >> i) & 1;
                    out |= (l ^ (c | r)) << (i - 1);
                }
                NXT[(s * 2 + tv) * 2 + u] = out;
            }
}

/* bitsets over 2^M states */
static int WORDS;
static inline void bs_set(uint64_t *b, int i) { b[i >> 6] |= 1ULL << (i & 63); }

/* A hash table of start groups: key = the visible column-1 bits so far, value = a bitset of layer states. Only the
 * groups the layer can produce are stored (a few hundred to a few million), so S is limited by CAP, not by 2^(S/2). */
typedef struct { uint64_t *keys; uint64_t *sets; char *used; size_t cap, n; } table;

static void t_init(table *T, size_t cap) {
    T->cap = cap; T->n = 0;
    T->keys = calloc(cap, 8); T->used = calloc(cap, 1); T->sets = calloc(cap * WORDS, 8);
    if (!T->keys || !T->used || !T->sets) { fprintf(stderr, "out of memory\n"); exit(3); }
}
static void t_free(table *T) { free(T->keys); free(T->used); free(T->sets); }
static uint64_t *t_get(table *T, uint64_t key);
static void t_grow(table *T) {
    table N; t_init(&N, T->cap * 2);
    for (size_t i = 0; i < T->cap; i++) if (T->used[i]) memcpy(t_get(&N, T->keys[i]), T->sets + i * WORDS, WORDS * 8);
    t_free(T); *T = N;
}
static uint64_t *t_get(table *T, uint64_t key) {
    if (2 * (T->n + 1) > T->cap) t_grow(T);
    size_t h = (size_t)((key * 0x9E3779B97F4A7C15ULL) >> 7) & (T->cap - 1);
    while (T->used[h] && T->keys[h] != key) h = (h + 1) & (T->cap - 1);
    if (!T->used[h]) { T->used[h] = 1; T->keys[h] = key; T->n++; }
    return T->sets + h * WORDS;
}

static int run(int S) {
    int nstates = 1 << M;
    WORDS = (nstates + 63) / 64;
    if (S / 2 > 63) { fprintf(stderr, "S too large\n"); return 2; }
    table cur, nxt;
    t_init(&cur, 1024);
    uint64_t *b0 = t_get(&cur, 0);
    if (M == 0) b0[0] = 1; else for (int s = 0; s < nstates; s++) bs_set(b0, s);
    for (int t = 0; t <= S - 2; t++) {                  /* phase A: the starts, grouped by visible column-1 bits */
        t_init(&nxt, 1024);
        for (size_t i = 0; i < cur.cap; i++) if (cur.used[i]) {
            uint64_t p = cur.keys[i];
            if (M == 0) {
                if (t % 2 == 0) for (int sg = 0; sg < 2; sg++) t_get(&nxt, p | ((uint64_t)sg << (t / 2)))[0] = 1;
                else t_get(&nxt, p)[0] = 1;
                continue;
            }
            uint64_t bset[WORDS];
            memcpy(bset, cur.sets + i * WORDS, WORDS * 8);
            for (int w = 0; w < WORDS; w++) for (uint64_t x = bset[w]; x; x &= x - 1) {
                int s = w * 64 + __builtin_ctzll(x);
                int sg = s & 1;
                uint64_t q = (t % 2 == 0) ? (p | ((uint64_t)sg << (t / 2))) : p;
                uint64_t *dst = t_get(&nxt, q);
                for (int u = 0; u < 2; u++) bs_set(dst, NXT[(s * 2 + tau(t)) * 2 + u]);
            }
        }
        t_free(&cur); cur = nxt;
    }
    int best = 0;
    long long at_best = 0, groups = 0;
    static long long hist[CAP + 2];
    uint64_t *set = malloc(WORDS * 8), *nset = malloc(WORDS * 8);
    for (size_t i = 0; i < cur.cap; i++) if (cur.used[i]) {
        uint64_t p = cur.keys[i];
        groups++;
        u128 a1 = 0, a2 = 0;
        for (int t = 0; t <= S - 2; t++) {               /* the left side up to depth S - 1 */
            int sg = (t % 2 == 0) ? (int)((p >> (t / 2)) & 1) : 0;
            u128 a = left_step(a1, a2, t, sg);
            a2 = a1; a1 = a;
        }
        memcpy(set, cur.sets + i * WORDS, WORDS * 8);
        u128 s1 = a1, s2 = a2;
        int runlen = 0;
        for (int t = S - 1; t + 1 <= CAP; t++) {
            int sg = 0;
            if (t % 2 == 0) {                            /* a linear cell: the demand fixes sigma(t) */
                u128 a0 = left_step(a1, a2, t, 0);
                int demand = (int)((a0 >> (t + 1)) & 1);
                sg = demand;
                if (M > 0) {                             /* keep the states that produce it */
                    int any = 0;
                    for (int w = 0; w < WORDS; w++) {
                        uint64_t keep = 0;
                        for (uint64_t x = set[w]; x; x &= x - 1) {
                            int s = w * 64 + __builtin_ctzll(x);
                            if ((s & 1) == sg) keep |= x & -x;
                        }
                        set[w] = keep; any |= keep != 0;
                    }
                    if (!any) break;
                }
            }
            u128 a = left_step(a1, a2, t, sg);
            if ((a >> (t + 1)) & 1) break;              /* a forced cell is 1: the run ends */
            a2 = a1; a1 = a;
            runlen++;
            if (M > 0) {
                memset(nset, 0, WORDS * 8);
                for (int w = 0; w < WORDS; w++) for (uint64_t x = set[w]; x; x &= x - 1) {
                    int s = w * 64 + __builtin_ctzll(x);
                    for (int u = 0; u < 2; u++) bs_set(nset, NXT[(s * 2 + tau(t)) * 2 + u]);
                }
                memcpy(set, nset, WORDS * 8);
            }
        }
        if (runlen > best) { best = runlen; at_best = 0; }
        if (runlen == best) at_best++;
        hist[runlen]++;
        if (MERGE) m_add(s1, s2, runlen);
        if (KEYMIN >= 0 && runlen >= KEYMIN) printf("K %d %d %llx %d\n", M, S, (unsigned long long)p, runlen);
    }
    if (HIST) for (int k = 0; k <= best; k++) printf("H %d %d %d %lld\n", M, S, k, hist[k]);
    if (MERGE) {
        static long long dh[CAP + 2];
        for (size_t i = 0; i < MCAP; i++) if (MS[i].used) dh[MS[i].run]++;
        printf("D %d %d distinct %zu\n", M, S, MN);
        for (int k = 0; k <= best; k++) if (dh[k]) printf("DH %d %d %d %lld\n", M, S, k, dh[k]);
        printf("DX %d %d conflicts %lld\n", M, S, MCONFLICT);
    }
    printf("R M %d S %d = %d%s (%lld of %lld start groups reach it)\n", M, S, best,
           (S - 1 + best >= CAP) ? " CAPPED" : "", at_best, groups);
    t_free(&cur);
    return 0;
}

int main(int argc, char **argv) {
    if (argc >= 3 && strcmp(argv[1], "left") == 0) {
        const char *bits = argv[2];
        int n = (int)strlen(bits);
        u128 a1 = 0, a2 = 0;
        for (int t = 0; t < n && t + 1 <= CAP; t++) {
            u128 a = left_step(a1, a2, t, bits[t] == '1');
            putchar(((a >> (t + 1)) & 1) ? '1' : '0');
            a2 = a1; a1 = a;
        }
        putchar('\n');
        return 0;
    }
    if (argc >= 5 && strcmp(argv[1], "keys") == 0) KEYMIN = atoi(argv[4]);
    if (argc >= 4 && strcmp(argv[1], "merge") == 0) MERGE = 1;
    if (argc >= 4 && (strcmp(argv[1], "run") == 0 || strcmp(argv[1], "hist") == 0 || KEYMIN >= 0 || MERGE)) {
        HIST = strcmp(argv[1], "hist") == 0;
        M = atoi(argv[2]);
        int S = atoi(argv[3]);
        build_layer();
        return run(S);
    }
    fprintf(stderr, "usage: ladder run M S | ladder left BITS\n");
    return 2;
}
