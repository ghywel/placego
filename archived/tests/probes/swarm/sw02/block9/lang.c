/* Block 9 (Local): the eventual column-1 language of the strip graph beside a periodic center.

Usage: lang WORD B R NMAX
  WORD  the center's period word, phases 0..P-1 (e.g. 001: white, white, black)
  B     strip width: columns 1..B; column B+1 is a free input at every tick
  R     the reading phase (a white phase of the center); the letter is column 1 at that phase
  NMAX  longest word length to enumerate

Graph: vertices (phase, columns 1..B), one edge per value of column B+1. Rows are naturals with bit
i = column i+1; one tick is s' = ((e<<1)|c) ^ (e|(e>>1)) with e = s | x<<B and c the center bit at the
current phase. Every actual right half beside a center that repeats WORD from time T is a walk here
from T on, so it ends in one cyclic SCC.

Labelled SCC: column 1 at every white phase is a function of the BFS level modulo the SCC's cycle gcd.
A walk that ends in a labelled SCC has column 1 eventually periodic at the white times, which masked
Jen (Rule30FiniteMaskedJen.masked_jen) excludes when the configuration has a leftmost black cell. So
for such configurations the eventual readings lie in the union, over UNLABELLED cyclic SCCs, of the
words read along paths inside one SCC. This program computes that union up to length NMAX, its counts,
growth ratios and minimal forbidden words. It prints NO UNLABELLED SCC if there is none.

Prediction, written 8 November 2026 18:54 UTC before any run:
 1. Control, word 01, B = 5, R = 0: the minimal forbidden words include the kit's col1Forbidden
    11, 00000, 100101, 10010001 (Rule30PeriodTwoWidth5).
 2. 001, R = 1, B = 14 and 16: the minimal forbidden words up to length 14 include all eleven of PE-1.2
    (010, 101, 1001, 11111, 000000, 0000111, 01110001, 11100000, 1110001110, 00000110001110,
    11100011000111); the counts at lengths 8, 10, 12, 14 are at most 27, 40, 61, 96 at B = 16.
 3. 011, R = 0, B = 20: exactly one unlabelled SCC; its forbidden words include 00, 010, 01110,
    011110 and 1^15, and at length 16 the count is at most 180.
 4. 0011, R = 0: at B = 13 seven of PE-2.1's eight words are forbidden (all but 10110), at B = 17 all
    eight. The growth per reading at B = 16 lies in [1.2274, 1.40], at or above rule30-open's channel
    value 1.2274 at W = 30 (channel-ladder.md), since entropy does not rise with width.
 5. The ladder (001 and 011 at B = 6..20; 0001, 0011, 0111 at B = 6..16) falls slowly with B and stays
    above growth 1 at every width; 001 at B = 20 has growth per reading in [1.15, 1.26], 011 in
    [1.25, 1.36].
Counterfactual: a control mismatch (1) or a missing PE word (2-4) means my model or theirs differs and
stops the comparison; a growth falling steadily toward 1 is a lead (wider strips changing the kind),
and NO UNLABELLED SCC at any width would exclude that period for left-finite configurations outright
and is to be rechecked before any word is said about it.
Record searched: see reports/LOCAL-BLOCK9-LANGUAGES-20261108.md.
*/
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int P, B, R, NMAX;
static int w[16];
static uint32_t NS, N;

static inline uint32_t succ(uint32_t id, int x) {
    uint32_t ph = id / NS, s = id % NS;
    uint64_t e = (uint64_t)s | ((uint64_t)x << B);
    uint64_t c = (uint64_t)w[ph];
    uint64_t ns = (((e << 1) | c) ^ (e | (e >> 1))) & (uint64_t)(NS - 1);
    return ((ph + 1) % P) * NS + (uint32_t)ns;
}
static inline int phase(uint32_t id) { return id / NS; }
static inline int bit0(uint32_t id) { return (id % NS) & 1; }
static long gcdl(long a, long b) { if (a < 0) a = -a; if (b < 0) b = -b; while (b) { long t = a % b; a = b; b = t; } return a; }

int main(int argc, char **argv) {
    if (argc != 5) { fprintf(stderr, "usage: lang WORD B R NMAX\n"); return 2; }
    P = (int)strlen(argv[1]);
    for (int i = 0; i < P; i++) w[i] = argv[1][i] == '1';
    B = atoi(argv[2]); R = atoi(argv[3]); NMAX = atoi(argv[4]);
    NS = 1u << B; N = (uint32_t)P * NS;
    printf("word %s P %d B %d R %d nodes %u\n", argv[1], P, B, R, N);
    int32_t *idx = malloc(sizeof(int32_t) * N), *low = malloc(sizeof(int32_t) * N), *comp = malloc(sizeof(int32_t) * N);
    int32_t *stk = malloc(sizeof(int32_t) * N), *cs = malloc(sizeof(int32_t) * N);
    int8_t *ce = malloc(N); uint8_t *onst = calloc(N, 1);
    for (uint32_t i = 0; i < N; i++) idx[i] = -1;
    int32_t counter = 0, sp = 0, ncomp = 0;
    for (uint32_t root = 0; root < N; root++) {
        if (idx[root] != -1) continue;
        int32_t csp = 0;
        cs[csp] = root; ce[csp] = 0; csp++;
        idx[root] = low[root] = counter++; stk[sp++] = root; onst[root] = 1;
        while (csp > 0) {
            uint32_t v = cs[csp - 1];
            if (ce[csp - 1] < 2) {
                int x = ce[csp - 1]++;
                uint32_t u = succ(v, x);
                if (idx[u] == -1) { idx[u] = low[u] = counter++; stk[sp++] = u; onst[u] = 1; cs[csp] = u; ce[csp] = 0; csp++; }
                else if (onst[u] && idx[u] < low[v]) low[v] = idx[u];
            } else {
                if (low[v] == idx[v]) {
                    uint32_t x;
                    do { x = stk[--sp]; onst[x] = 0; comp[x] = ncomp; } while (x != v);
                    ncomp++;
                }
                csp--;
                if (csp > 0) { uint32_t p = cs[csp - 1]; if (low[v] < low[p]) low[p] = low[v]; }
            }
        }
    }
    free(low); free(stk); free(cs); free(ce); free(onst);
    /* members by component */
    int64_t *start = calloc(ncomp + 1, sizeof(int64_t));
    for (uint32_t i = 0; i < N; i++) start[comp[i] + 1]++;
    for (int c = 0; c < ncomp; c++) start[c + 1] += start[c];
    uint32_t *mem = malloc(sizeof(uint32_t) * N); int64_t *fill = malloc(sizeof(int64_t) * ncomp);
    for (int c = 0; c < ncomp; c++) fill[c] = start[c];
    for (uint32_t i = 0; i < N; i++) mem[fill[comp[i]]++] = i;
    free(fill);
    int32_t *lvl = idx; for (uint32_t i = 0; i < N; i++) lvl[i] = -1;
    int32_t *loc = malloc(sizeof(int32_t) * N);
    uint8_t **present = calloc(NMAX + 1, sizeof(uint8_t *));
    for (int n = 1; n <= NMAX; n++) present[n] = calloc(((size_t)1 << n) / 8 + 1, 1);
    int ntriv = 0, nlab = 0, nun = 0; long labsz = 0; int reached = NMAX; int truncated = 0;
    uint32_t *queue = malloc(sizeof(uint32_t) * N);
    for (int c = 0; c < ncomp; c++) {
        int64_t sz = start[c + 1] - start[c];
        if (sz < 2) continue;
        ntriv++;
        uint32_t r0 = mem[start[c]];
        int64_t qh = 0, qt = 0; queue[qt++] = r0; lvl[r0] = 0;
        while (qh < qt) {
            uint32_t u = queue[qh++];
            for (int x = 0; x < 2; x++) { uint32_t v = succ(u, x); if (comp[v] == c && lvl[v] == -1) { lvl[v] = lvl[u] + 1; queue[qt++] = v; } }
        }
        long g = 0;
        for (int64_t k = start[c]; k < start[c + 1]; k++) {
            uint32_t u = mem[k];
            for (int x = 0; x < 2; x++) { uint32_t v = succ(u, x); if (comp[v] == c) g = gcdl(g, (long)lvl[u] + 1 - lvl[v]); }
        }
        int8_t *lab = malloc(g); memset(lab, -1, g);
        int labelled = 1;
        for (int64_t k = start[c]; k < start[c + 1] && labelled; k++) {
            uint32_t u = mem[k];
            if (w[phase(u)]) continue;
            int key = lvl[u] % g, b = bit0(u);
            if (lab[key] == -1) lab[key] = b; else if (lab[key] != b) labelled = 0;
        }
        free(lab);
        if (labelled) { nlab++; labsz += sz; continue; }
        nun++;
        /* local indices of phase-R nodes */
        int32_t m = 0;
        for (int64_t k = start[c]; k < start[c + 1]; k++) { uint32_t u = mem[k]; if (phase(u) == R) loc[u] = m++; }
        uint32_t *node = malloc(sizeof(uint32_t) * m);
        for (int64_t k = start[c]; k < start[c + 1]; k++) { uint32_t u = mem[k]; if (phase(u) == R) node[loc[u]] = u; }
        /* macro successors: P ticks inside the SCC */
        int K = 1 << P;
        int32_t *tg = malloc(sizeof(int32_t) * (size_t)m * K); int *ntg = calloc(m, sizeof(int));
        for (int32_t i = 0; i < m; i++) {
            for (int seq = 0; seq < K; seq++) {
                uint32_t u = node[i]; int ok = 1;
                for (int j = 0; j < P && ok; j++) { u = succ(u, (seq >> j) & 1); if (comp[u] != c) ok = 0; }
                if (!ok) continue;
                int32_t t = loc[u], dup = 0;
                for (int q = 0; q < ntg[i]; q++) if (tg[(size_t)i * K + q] == t) dup = 1;
                if (!dup) tg[(size_t)i * K + ntg[i]++] = t;
            }
        }
        int W64 = (m + 63) / 64;
        size_t cap = ((size_t)1 << 28) / ((size_t)W64 * 8); if (cap > 300000) cap = 300000; if (cap < 1024) cap = 1024;
        uint32_t *vals = malloc(sizeof(uint32_t) * cap), *nvals = malloc(sizeof(uint32_t) * cap);
        uint64_t *sets = calloc((size_t)cap * W64, 8), *nsets = calloc((size_t)cap * W64, 8);
        size_t nw = 0;
        for (int a = 0; a < 2; a++) {
            int any = 0;
            for (int32_t i = 0; i < m; i++) if (bit0(node[i]) == a) { sets[nw * W64 + i / 64] |= 1ull << (i % 64); any = 1; }
            if (any) vals[nw++] = a; else memset(sets + nw * W64, 0, 8 * W64);
        }
        int len = 1;
        for (size_t k = 0; k < nw; k++) present[1][vals[k] >> 3] |= 1 << (vals[k] & 7);
        while (len < NMAX) {
            if (nw * 2 > cap) { truncated = 1; if (len < reached) reached = len; break; }
            size_t nn = 0;
            memset(nsets, 0, (size_t)nw * 2 * W64 * 8);
            for (size_t k = 0; k < nw; k++) {
                uint64_t *Y0 = nsets + nn * W64, *Y1 = nsets + (nn + 1) * W64;
                int a0 = 0, a1 = 0;
                for (int q = 0; q < W64; q++) {
                    uint64_t word = sets[k * W64 + q];
                    while (word) {
                        int bt = __builtin_ctzll(word); word &= word - 1;
                        int32_t i = q * 64 + bt;
                        for (int z = 0; z < ntg[i]; z++) {
                            int32_t t = tg[(size_t)i * K + z];
                            if (bit0(node[t])) { Y1[t / 64] |= 1ull << (t % 64); a1 = 1; }
                            else { Y0[t / 64] |= 1ull << (t % 64); a0 = 1; }
                        }
                    }
                }
                if (a0 && a1) { nvals[nn] = vals[k] << 1; nvals[nn + 1] = (vals[k] << 1) | 1; nn += 2; }
                else if (a0) { nvals[nn] = vals[k] << 1; nn += 1; }
                else if (a1) { memcpy(Y0, Y1, 8 * W64); memset(Y1, 0, 8 * W64); nvals[nn] = (vals[k] << 1) | 1; nn += 1; }
            }
            uint32_t *tv = vals; vals = nvals; nvals = tv; uint64_t *ts = sets; sets = nsets; nsets = ts;
            nw = nn; len++;
            for (size_t k = 0; k < nw; k++) present[len][vals[k] >> 3] |= 1 << (vals[k] & 7);
        }
        printf("unlabelled SCC %d: size %lld, phase-%d nodes %d, gcd %ld, words to length %d%s\n",
               nun, (long long)sz, R, m, g, len, truncated ? " (TRUNCATED: word cap)" : "");
        free(node); free(tg); free(ntg); free(vals); free(nvals); free(sets); free(nsets);
    }
    printf("cyclic SCCs %d: labelled %d (%ld nodes), unlabelled %d\n", ntriv, nlab, labsz, nun);
    if (nun == 0) { printf("NO UNLABELLED SCC\n"); return 0; }
    long prev = 0;
    for (int n = 1; n <= reached; n++) {
        long cnt = 0; size_t sz = ((size_t)1 << n);
        for (size_t v = 0; v < sz; v++) if (present[n][v >> 3] >> (v & 7) & 1) cnt++;
        if (n == 1) printf("counts");
        printf(" %ld", cnt);
        if (n == reached) printf("\ngrowth per reading at length %d: %.4f\n", n, prev ? (double)cnt / prev : 0.0);
        prev = cnt;
    }
    printf("minimal forbidden words (length <= %d):", reached);
    int shown = 0;
    for (int n = 1; n <= reached; n++) {
        size_t sz = ((size_t)1 << n);
        for (size_t v = 0; v < sz; v++) {
            if (present[n][v >> 3] >> (v & 7) & 1) continue;
            int minimal;
            if (n == 1) minimal = 1;
            else {
                size_t pre = v >> 1, suf = v & ((sz >> 1) - 1);
                minimal = (present[n - 1][pre >> 3] >> (pre & 7) & 1) && (present[n - 1][suf >> 3] >> (suf & 7) & 1);
            }
            if (!minimal) continue;
            if (shown < 80) { printf(" "); for (int j = n - 1; j >= 0; j--) putchar('0' + (int)((v >> j) & 1)); }
            shown++;
        }
    }
    printf("\nminimal forbidden words: %d\n", shown);
    return 0;
}
