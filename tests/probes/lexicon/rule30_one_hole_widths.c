/* rule30_one_hole_widths.c: OHC, the one-hole channel relaxation (OH, rule30_one_hole_widths.py) in C, so that
 * widths past 13 fit in memory. Local's run (chat L480); predictions in the .py header's OHC block, pushed first.
 *
 * Build:  clang -O2 -o ~/np-scratch-int/rule30-oh/ohc tests/probes/lexicon/rule30_one_hole_widths.c
 * Run:    ohc K P [MAXNODES] [MAXMEM_MB]
 *
 * The model is OH's exactly. State bit j holds x_(j+1), j = 0 .. K-1. One step with wall bit w and outside bit u is
 * x' = left XOR (x OR right), with left = (x << 1 | w) and right = (x >> 1 | u << (K-1)), both masked to K bits.
 * The macro is one white step (w = 0), then P - 1 black steps (w = 1), with u free at every step. The visible symbol
 * is x1 (bit 0) before the macro. Sets of states are bitsets of 2^K bits, stepped one update at a time; no relation
 * table is stored. The subset construction runs from the full set by BFS. Each subset is identified by two
 * independent 64-bit hashes (a 128-bit key; a collision would merge two subsets silently, with probability about
 * n^2 / 2^128). Only the frontier's bitsets are kept. Output: the reachable subset count, whether the empty set is
 * reached (a forbidden word), and the growth of the language. Growth is the ratio of word counts at n and n - 1
 * for n = 1500 (and at 750, to show convergence), in long double with rescaling, from the transition graph. Caps: MAXNODES subsets and MAXMEM_MB of
 * frontier bitsets; a capped run prints CAPPED and no growth.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int K, P;
static size_t NW;                 /* 64-bit words per bitset */

static void step_set(const uint64_t *in, uint64_t *out, int wall) {
    uint64_t mask = (K == 64) ? ~0ULL : ((1ULL << K) - 1);
    memset(out, 0, NW * 8);
    for (size_t w = 0; w < NW; w++) {
        uint64_t b = in[w];
        while (b) {
            int t = __builtin_ctzll(b);
            b &= b - 1;
            uint64_t x = (uint64_t)w * 64 + t;
            uint64_t left = ((x << 1) | (uint64_t)wall) & mask;
            for (uint64_t u = 0; u < 2; u++) {
                uint64_t right = ((x >> 1) | (u << (K - 1))) & mask;
                uint64_t y = (left ^ (x | right)) & mask;
                out[y >> 6] |= 1ULL << (y & 63);
            }
        }
    }
}

static uint64_t *tmpa, *tmpb;

/* advance: keep states with x1 == bit, then one white step and P - 1 black steps */
static int advance(const uint64_t *S, int bit, uint64_t *out) {
    uint64_t sel = bit ? 0xAAAAAAAAAAAAAAAAULL : 0x5555555555555555ULL;
    int any = 0;
    for (size_t w = 0; w < NW; w++) {
        tmpa[w] = S[w] & sel;
        if (NW == 1 && K < 6) tmpa[w] &= (1ULL << (1 << K)) - 1;
        any |= tmpa[w] != 0;
    }
    if (!any) { memset(out, 0, NW * 8); return 0; }
    step_set(tmpa, tmpb, 0);
    uint64_t *a = tmpb, *b = tmpa;
    for (int s = 1; s < P; s++) { step_set(a, b, 1); uint64_t *c = a; a = b; b = c; }
    memcpy(out, a, NW * 8);
    for (size_t w = 0; w < NW; w++) if (out[w]) return 1;
    return 0;
}

static void hash2(const uint64_t *S, uint64_t *h1, uint64_t *h2) {
    uint64_t a = 1469598103934665603ULL, b = 0x9E3779B97F4A7C15ULL;
    for (size_t w = 0; w < NW; w++) {
        uint64_t v = S[w];
        for (int i = 0; i < 8; i++) { a ^= (v >> (8 * i)) & 255; a *= 1099511628211ULL; }
        b ^= v + 0x9E3779B97F4A7C15ULL + (b << 6) + (b >> 2);
        b = (b ^ (b >> 31)) * 0xBF58476D1CE4E5B9ULL;
    }
    *h1 = a; *h2 = b;
}

/* open-addressing table of 128-bit keys -> node id */
static uint64_t *tk1, *tk2; static int64_t *tid; static size_t tcap;
static int64_t tfind(uint64_t h1, uint64_t h2, int64_t newid, int *isnew) {
    size_t i = (size_t)(h1 ^ (h2 * 31)) & (tcap - 1);
    while (tid[i] >= 0) {
        if (tk1[i] == h1 && tk2[i] == h2) { *isnew = 0; return tid[i]; }
        i = (i + 1) & (tcap - 1);
    }
    tk1[i] = h1; tk2[i] = h2; tid[i] = newid; *isnew = 1; return newid;
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s K P [MAXNODES] [MAXMEM_MB]\n", argv[0]); return 2; }
    K = atoi(argv[1]); P = atoi(argv[2]);
    long maxnodes = argc > 3 ? atol(argv[3]) : 2000000;
    long maxmem = argc > 4 ? atol(argv[4]) : 1500;
    if (K < 1 || K > 24 || P < 2) { fprintf(stderr, "K must be 1 .. 24, P >= 2\n"); return 2; }
    NW = ((1ULL << K) + 63) / 64;
    size_t bsz = NW * 8;
    tmpa = malloc(bsz); tmpb = malloc(bsz);
    tcap = 1; while (tcap < (size_t)maxnodes * 2) tcap <<= 1;
    tk1 = malloc(tcap * 8); tk2 = malloc(tcap * 8); tid = malloc(tcap * 8);
    for (size_t i = 0; i < tcap; i++) tid[i] = -1;
    int64_t *trans = malloc((size_t)maxnodes * 2 * sizeof(int64_t));   /* -1 = empty edge */
    /* frontier: a FIFO of bitsets with ids */
    size_t fcap = 1024, fhead = 0, ftail = 0;
    uint64_t **fq = malloc(fcap * sizeof(uint64_t *)); int64_t *fid = malloc(fcap * sizeof(int64_t));
    uint64_t *full = malloc(bsz);
    for (size_t w = 0; w < NW; w++) full[w] = ~0ULL;
    if ((1ULL << K) % 64) full[NW - 1] = (1ULL << ((1ULL << K) % 64)) - 1;
    uint64_t h1, h2; int isnew; int64_t n = 0;
    hash2(full, &h1, &h2); tfind(h1, h2, n++, &isnew);
    fq[ftail] = full; fid[ftail] = 0; ftail++;
    int empty_edge = 0, capped = 0;
    long peak_frontier_mb = 0;
    while (fhead < ftail) {
        uint64_t *S = fq[fhead]; int64_t sid = fid[fhead]; fhead++;
        for (int bit = 0; bit < 2; bit++) {
            uint64_t *T = malloc(bsz);
            if (!advance(S, bit, T)) { free(T); trans[sid * 2 + bit] = -1; empty_edge = 1; continue; }
            hash2(T, &h1, &h2);
            int64_t id = tfind(h1, h2, n, &isnew);
            trans[sid * 2 + bit] = id;
            if (!isnew) { free(T); continue; }
            n++;
            if (n >= maxnodes) { capped = 1; free(T); break; }
            if (ftail == fcap) {
                if (fhead > fcap / 2) {          /* compact the queue */
                    memmove(fq, fq + fhead, (ftail - fhead) * sizeof(uint64_t *));
                    memmove(fid, fid + fhead, (ftail - fhead) * sizeof(int64_t));
                    ftail -= fhead; fhead = 0;
                } else {
                    fcap *= 2; fq = realloc(fq, fcap * sizeof(uint64_t *)); fid = realloc(fid, fcap * sizeof(int64_t));
                }
            }
            fq[ftail] = T; fid[ftail] = id; ftail++;
            long mb = (long)((ftail - fhead) * bsz >> 20);
            if (mb > peak_frontier_mb) peak_frontier_mb = mb;
            if (mb > maxmem) { capped = 1; break; }
        }
        free(S);
        if (capped) break;
    }
    if (capped) {
        printf("K %d P %d CAPPED nodes %lld frontier_mb %ld\n", K, P, (long long)n, peak_frontier_mb);
        return 0;
    }
    /* growth by counting words: v_(m+1)[T] += v_m[S] along nonempty edges, rescaled */
    long double *v = calloc(n, sizeof(long double)), *w = calloc(n, sizeof(long double));
    v[0] = 1.0L;
    long double prev = 1.0L, ratio = 0.0L, half = 0.0L;
    int NSTEP = 1500;
    for (int m = 1; m <= NSTEP; m++) {
        memset(w, 0, n * sizeof(long double));
        for (int64_t s = 0; s < n; s++) {
            if (v[s] == 0.0L) continue;
            for (int b = 0; b < 2; b++) { int64_t t = trans[s * 2 + b]; if (t >= 0) w[t] += v[s]; }
        }
        long double tot = 0.0L;
        for (int64_t s = 0; s < n; s++) tot += w[s];
        ratio = tot / prev;
        if (tot == 0.0L) { ratio = 0.0L; break; }
        if (m == NSTEP / 2) half = ratio;
        for (int64_t s = 0; s < n; s++) w[s] /= tot;     /* rescale so the next total is the ratio */
        prev = 1.0L;
        long double *c = v; v = w; w = c;
    }
    printf("K %d P %d nodes %lld empty_edge %d growth %.12Lf (at n/2 %.12Lf) frontier_mb %ld\n", K, P, (long long)n,
           empty_edge, ratio, half, peak_frontier_mb);
    return 0;
}
