/* ladder.c: the first rungs of the LR_m ladder (PRIZE-PROBLEMS.md section 8.11), for the trace 0101...
 *
 * BUILD:   cc -O2 -o ladder tests/probes/lexicon/ladder.c      (driven by rule30_ladder.py, which builds it itself)
 * USAGE:   ./ladder run M S        R(M, S): the longest run of zeros the forced left half can be held to, starting at
 *                                  depth S, over every start of cells 1..M and every input sequence in column M + 1
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

static int run(int S) {
    int nstates = 1 << M;
    WORDS = (nstates + 63) / 64;
    int nbits = S / 2;                                   /* even times 0, 2, ..., < S - 1 */
    if (S - 1 > 0) nbits = (S - 1 + 1) / 2;
    size_t ngroups = (size_t)1 << nbits;
    uint64_t *cur = calloc(ngroups * WORDS, 8), *nxt = calloc(ngroups * WORDS, 8);
    char *used = calloc(ngroups, 1), *nused = calloc(ngroups, 1);
    if (M == 0) { cur[0] = 1; } else { for (int s = 0; s < nstates; s++) bs_set(cur, s); }
    used[0] = 1;
    for (int t = 0; t <= S - 2; t++) {                  /* phase A: the starts, grouped by visible column-1 bits */
        memset(nxt, 0, ngroups * WORDS * 8);
        memset(nused, 0, ngroups);
        for (size_t p = 0; p < ngroups; p++) if (used[p]) {
            uint64_t *b = cur + p * WORDS;
            if (M == 0) {
                if (t % 2 == 0) {
                    for (int sg = 0; sg < 2; sg++) { size_t q = p | ((size_t)sg << (t / 2)); nxt[q * WORDS] = 1; nused[q] = 1; }
                } else { nxt[p * WORDS] = 1; nused[p] = 1; }
                continue;
            }
            for (int w = 0; w < WORDS; w++) for (uint64_t x = b[w]; x; x &= x - 1) {
                int s = w * 64 + __builtin_ctzll(x);
                int sg = s & 1;
                size_t q = (t % 2 == 0) ? (p | ((size_t)sg << (t / 2))) : p;
                for (int u = 0; u < 2; u++) bs_set(nxt + q * WORDS, NXT[(s * 2 + tau(t)) * 2 + u]);
                nused[q] = 1;
            }
        }
        uint64_t *tmp = cur; cur = nxt; nxt = tmp;
        char *tu = used; used = nused; nused = tu;
    }
    int best = 0;
    long long at_best = 0, groups = 0;
    uint64_t *set = malloc(WORDS * 8), *nset = malloc(WORDS * 8);
    for (size_t p = 0; p < ngroups; p++) if (used[p]) {
        groups++;
        u128 a1 = 0, a2 = 0;
        for (int t = 0; t <= S - 2; t++) {               /* the left side up to depth S - 1 */
            int sg = (t % 2 == 0) ? (int)((p >> (t / 2)) & 1) : 0;
            u128 a = left_step(a1, a2, t, sg);
            a2 = a1; a1 = a;
        }
        memcpy(set, cur + p * WORDS, WORDS * 8);
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
    }
    printf("R M %d S %d = %d%s (%lld of %lld start groups reach it)\n", M, S, best,
           (S - 1 + best >= CAP) ? " CAPPED" : "", at_best, groups);
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
    if (argc >= 4 && strcmp(argv[1], "run") == 0) {
        M = atoi(argv[2]);
        int S = atoi(argv[3]);
        build_layer();
        return run(S);
    }
    fprintf(stderr, "usage: ladder run M S | ladder left BITS\n");
    return 2;
}
