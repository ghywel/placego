/* rule30_strip_c.c: SGC, the strip-graph certificate (entry 38's method; SG, RG) in C, so radius 10 .. 11 fits in
 * memory. Local's run (chat L501); predictions in rule30_rung3_strip.py's SGC block, pushed first.
 *
 * Build:  clang -O2 -o ~/np-scratch-int/rule30-oh/sgc tests/probes/lexicon/rule30_strip_c.c
 * Run:    sgc WORD RADIUS          (WORD: the column word, e.g. 10000000; RADIUS R >= 2)
 *
 * A vertex is a row on positions -R .. R with a phase ph in 0 .. p - 1, whose centre equals WORD[ph]. Bit k of the row
 * is position k - R. An edge applies Rule 30 exactly on -(R - 1) .. R - 1, leaves the two outer cells free, and
 * advances the phase; the new centre must equal WORD[ph + 1]. The graph is generated implicitly; vertices are indexed
 * by phase and the row with its centre bit removed.
 * Per cyclic strongly connected component (iterative Tarjan): the period P is the gcd of level differences along
 * internal edges from a BFS; column -1 (bit R - 1) or +1 (bit R + 1) is forced if it takes one value per class
 * (level mod P). PASS: every cyclic component forces a neighbour (then Theorem A, entry 5, excludes WORD for finite
 * seeds, as in entry 38). EXCLUDED-ACYCLIC: no cyclic component. FAIL otherwise.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int R, W, P_;
static const char *WORD;
static uint64_t ROWS;            /* 2^(W - 1): rows with the centre removed */
static uint64_t NV;

static inline uint64_t row_of(uint64_t id, int *ph) {
    *ph = (int)(id / ROWS);
    uint64_t c = id % ROWS;                         /* compressed row: bits below R, then bits above R shifted down */
    uint64_t lo = c & ((1ULL << R) - 1), hi = c >> R;
    uint64_t cb = (uint64_t)(WORD[*ph] - '0');
    return lo | (cb << R) | (hi << (R + 1));
}

static inline uint64_t id_of(uint64_t row, int ph) {
    uint64_t lo = row & ((1ULL << R) - 1), hi = row >> (R + 1);
    return (uint64_t)ph * ROWS + (lo | (hi << R));
}

/* successors: returns count (0 or 4) */
static inline int succ(uint64_t id, uint64_t out[4]) {
    int ph;
    uint64_t r = row_of(id, &ph);
    uint64_t full = (1ULL << W) - 1;
    uint64_t base = ((r << 1) ^ (r | (r >> 1))) & full & ~1ULL & ~(1ULL << (W - 1));   /* bits 1 .. W-2 updated */
    int nph = (ph + 1) % P_;
    if (((base >> R) & 1) != (uint64_t)(WORD[nph] - '0')) return 0;
    for (int o = 0; o < 4; o++) {
        uint64_t r2 = base | (uint64_t)(o & 1) | ((uint64_t)(o >> 1) << (W - 1));
        out[o] = id_of(r2, nph);
    }
    return 4;
}

static int64_t gcd64(int64_t a, int64_t b) { if (a < 0) a = -a; if (b < 0) b = -b; while (b) { int64_t t = a % b; a = b; b = t; } return a; }

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s WORD RADIUS\n", argv[0]); return 2; }
    WORD = argv[1]; R = atoi(argv[2]); W = 2 * R + 1; P_ = (int)strlen(WORD);
    ROWS = 1ULL << (W - 1); NV = (uint64_t)P_ * ROWS;
    int32_t *idx = malloc(NV * 4), *low = malloc(NV * 4), *comp = malloc(NV * 4);
    uint8_t *onst = calloc(NV, 1);
    int32_t *stk = malloc(NV * 4);
    int64_t *cs_v = malloc(NV * 8); int8_t *cs_e = malloc(NV);
    if (!idx || !low || !comp || !onst || !stk || !cs_v || !cs_e) { fprintf(stderr, "out of memory\n"); return 3; }
    for (uint64_t i = 0; i < NV; i++) { idx[i] = -1; comp[i] = -1; }
    int32_t counter = 0, sp = 0, ncomp = 0;
    uint64_t sb[4];
    /* iterative Tarjan */
    for (uint64_t s = 0; s < NV; s++) {
        if (idx[s] != -1) continue;
        int64_t cd = 0;
        cs_v[cd] = s; cs_e[cd] = 0; cd++;
        idx[s] = low[s] = counter++; stk[sp++] = (int32_t)s; onst[s] = 1;
        while (cd) {
            int64_t v = cs_v[cd - 1];
            int e = cs_e[cd - 1];
            int n = succ((uint64_t)v, sb);
            if (e < n) {
                cs_e[cd - 1] = (int8_t)(e + 1);
                uint64_t w = sb[e];
                if (idx[w] == -1) {
                    idx[w] = low[w] = counter++; stk[sp++] = (int32_t)w; onst[w] = 1;
                    cs_v[cd] = (int64_t)w; cs_e[cd] = 0; cd++;
                } else if (onst[w] && idx[w] < low[v]) low[v] = idx[w];
            } else {
                cd--;
                if (cd && low[v] < low[cs_v[cd - 1]]) low[cs_v[cd - 1]] = low[v];
                if (low[v] == idx[v]) {
                    int32_t w;
                    do { w = stk[--sp]; onst[w] = 0; comp[w] = ncomp; } while (w != v);
                    ncomp++;
                }
            }
        }
    }
    free(idx); free(onst); free(stk); free(cs_v); free(cs_e);
    /* per component: size, cyclicity, BFS levels, period, forcing */
    int32_t *csize = calloc(ncomp, 4), *croot = malloc((size_t)ncomp * 4);
    for (int c = 0; c < ncomp; c++) croot[c] = -1;
    for (uint64_t v = 0; v < NV; v++) { csize[comp[v]]++; if (croot[comp[v]] < 0) croot[comp[v]] = (int32_t)v; }
    int32_t *level = low;                       /* reuse */
    for (uint64_t v = 0; v < NV; v++) level[v] = -1;
    int32_t *queue = malloc(NV * 4);
    int ncyc = 0, nbad = 0;
    printf("word %s radius %d: %llu vertices, %d components\n", WORD, R, (unsigned long long)NV, ncomp);
    for (int c = 0; c < ncomp; c++) {
        int32_t root = croot[c];
        /* cyclic? size > 1, or a self-loop */
        int cyc = csize[c] > 1;
        if (!cyc) { int n = succ((uint64_t)root, sb); for (int e = 0; e < n; e++) if ((int32_t)sb[e] == root) cyc = 1; }
        if (!cyc) continue;
        ncyc++;
        int64_t qh = 0, qt = 0; queue[qt++] = root; level[root] = 0;
        int64_t P = 0;
        while (qh < qt) {
            int32_t v = queue[qh++];
            int n = succ((uint64_t)v, sb);
            for (int e = 0; e < n; e++) {
                uint64_t w = sb[e];
                if (comp[w] != c) continue;
                if (level[w] < 0) { level[w] = level[v] + 1; queue[qt++] = (int32_t)w; }
                else P = gcd64(P, (int64_t)level[v] + 1 - level[w]);
            }
        }
        if (P == 0) P = 1;
        /* forcing: one value per class for bit R-1 (column -1) and bit R+1 (column +1) */
        int8_t *cl = malloc(P), *cr = malloc(P);
        memset(cl, -1, P); memset(cr, -1, P);
        int fl = 1, fr = 1;
        for (int64_t i = 0; i < qt; i++) {
            int32_t v = queue[i]; int ph;
            uint64_t r = row_of((uint64_t)v, &ph);
            int64_t k = level[v] % P;
            int8_t bl = (int8_t)((r >> (R - 1)) & 1), br = (int8_t)((r >> (R + 1)) & 1);
            if (cl[k] < 0) cl[k] = bl; else if (cl[k] != bl) fl = 0;
            if (cr[k] < 0) cr[k] = br; else if (cr[k] != br) fr = 0;
        }
        free(cl); free(cr);
        if (!fl && !fr) nbad++;
        if (csize[c] >= 8 || (!fl && !fr))
            printf("  component size %d, P %lld, forces %s\n", csize[c], (long long)P,
                   fl && fr ? "-1/+1" : fl ? "-1" : fr ? "+1" : "NONE");
    }
    printf("verdict: %s (%d cyclic components, %d forcing neither)\n",
           ncyc == 0 ? "EXCLUDED-ACYCLIC" : (nbad == 0 ? "PASS" : "FAIL"), ncyc, nbad);
    return 0;
}
