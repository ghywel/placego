/* rule30_layer_product.c: LP, a layer automaton times a forbidden-word automaton (Cloud's CL113 suggestion). Local's
 * run (chat L503); predictions in rule30_layer_product.py, pushed first.
 *
 * Build:  clang -O2 -o ~/np-scratch-int/rule30-oh/lp tests/probes/lexicon/rule30_layer_product.c
 * Run:    lp DUMP FWORDS [MAXSTATES]
 *   DUMP:   OHC's transition table (OHC_DUMP=path ohc K P), or "-" for the one-node layer that allows every word.
 *   FWORDS: one 0/1 word per line ('#' lines ignored), or "-" for none.
 *
 * The product of the layer's subset automaton (node 0 = the full set) with the Aho-Corasick automaton of F, from
 * (0, root), accepts exactly the words the layer allows that contain no word of F. If F is a set of words forbidden
 * in the true language, every true word is accepted, so the true growth is at most the product's spectral radius.
 * The spectral radius is the largest over the strongly connected components (iterative Tarjan). Per component, a
 * power iteration of A + I (aperiodic, same Perron vector) gives a positive vector; it is scaled to integers u_i
 * (at most 2^50, at least 1), and R = max_i ceil(D (A u)_i / u_i) with D = 10^9, checked in 128-bit integers as
 * D (A u)_i <= R u_i for every i of the component, so its radius is at most R / D (Collatz-Wielandt).
 * Components without a cycle have radius 0 and are skipped. A word-count ratio from the start state is printed
 * beside it as a cross-check (not a certificate).
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef unsigned __int128 u128;

/* Aho-Corasick over {0, 1} */
static int32_t *g0, *g1, *fl; static uint8_t *outp; static int32_t na, acap;
static int32_t newnode(void) {
    if (na == acap) {
        acap = acap ? acap * 2 : 1024;
        g0 = realloc(g0, acap * 4); g1 = realloc(g1, acap * 4); fl = realloc(fl, acap * 4); outp = realloc(outp, acap);
    }
    g0[na] = g1[na] = -1; fl[na] = 0; outp[na] = 0; return na++;
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s DUMP FWORDS [MAXSTATES]\n", argv[0]); return 2; }
    long maxstates = argc > 3 ? atol(argv[3]) : 20000000;
    /* the layer */
    int64_t nl; int64_t *tr;
    if (!strcmp(argv[1], "-")) { nl = 1; tr = malloc(16); tr[0] = tr[1] = 0; }
    else {
        FILE *f = fopen(argv[1], "rb");
        if (!f || fread(&nl, 8, 1, f) != 1) { fprintf(stderr, "cannot read dump\n"); return 3; }
        tr = malloc((size_t)nl * 16);
        if (fread(tr, 8, (size_t)nl * 2, f) != (size_t)nl * 2) { fprintf(stderr, "short dump\n"); return 3; }
        fclose(f);
    }
    /* F */
    newnode();
    int nf = 0, maxlen = 0, layer_allows = 0, minallowed = 1 << 30;
    int lenhist[128] = {0}, allowhist[128] = {0};
    if (strcmp(argv[2], "-")) {
        FILE *f = fopen(argv[2], "r");
        if (!f) { fprintf(stderr, "cannot read F\n"); return 3; }
        char line[4096];
        while (fgets(line, sizeof line, f)) {
            if (line[0] == '#') continue;
            int L = 0; int32_t s = 0; int64_t ln = 0; int alive = 1;
            for (char *c = line; *c == '0' || *c == '1'; c++, L++) {
                int b = *c - '0';
                int32_t *g = b ? g1 : g0;
                if (g[s] < 0) { int32_t t = newnode(); g = b ? g1 : g0; g[s] = t; }
                s = (b ? g1 : g0)[s];
                if (alive) { ln = tr[ln * 2 + b]; if (ln < 0) alive = 0; }
            }
            if (!L) continue;
            outp[s] = 1; nf++; if (L > maxlen) maxlen = L;
            if (L < 128) lenhist[L]++;
            if (alive) { layer_allows++; if (L < 128) allowhist[L]++; if (L < minallowed) minallowed = L; }
        }
        fclose(f);
    }
    /* failure links and the full goto function, breadth first */
    {
        int32_t *q = malloc(na * 4); int qh = 0, qt = 0;
        for (int b = 0; b < 2; b++) {
            int32_t *g = b ? g1 : g0;
            if (g[0] < 0) g[0] = 0; else { fl[g[0]] = 0; q[qt++] = g[0]; }
        }
        while (qh < qt) {
            int32_t s = q[qh++];
            outp[s] |= outp[fl[s]];
            for (int b = 0; b < 2; b++) {
                int32_t *g = b ? g1 : g0;
                if (g[s] < 0) g[s] = g[fl[s]];
                else { fl[g[s]] = g[fl[s]]; q[qt++] = g[s]; }
            }
        }
        free(q);
    }
    printf("layer nodes %lld; F %d words, longest %d, AC states %d; F words the layer allows: %d", (long long)nl, nf,
           maxlen, na, layer_allows);
    if (layer_allows) printf(" (shortest %d)", minallowed);
    printf("\n");
    if (layer_allows) {
        printf("allowed by length:");
        for (int L = 1; L < 128; L++) if (allowhist[L]) printf(" %d:%d/%d", L, allowhist[L], lenhist[L]);
        printf("\n");
    }
    /* product by BFS; open addressing on the key layer * na + ac */
    size_t hcap = 1; while (hcap < (size_t)maxstates * 2) hcap <<= 1;
    uint64_t *hk = malloc(hcap * 8); int32_t *hv = malloc(hcap * 4);
    for (size_t i = 0; i < hcap; i++) hv[i] = -1;
    uint64_t *key = malloc((size_t)maxstates * 8); int32_t *suc = malloc((size_t)maxstates * 8);
    int64_t ns = 0;
#define LOOKUP(K_, OUT_) do { uint64_t k_ = (K_); size_t i_ = (size_t)((k_ * 0x9E3779B97F4A7C15ULL) >> 20) & (hcap - 1); \
        while (hv[i_] >= 0 && hk[i_] != k_) i_ = (i_ + 1) & (hcap - 1); \
        if (hv[i_] < 0) { if (ns >= maxstates) { printf("CAPPED at %lld states\n", (long long)ns); return 0; } \
            hk[i_] = k_; hv[i_] = (int32_t)ns; key[ns] = k_; ns++; } (OUT_) = hv[i_]; } while (0)
    int32_t s0; LOOKUP(0, s0); (void)s0;
    for (int64_t s = 0; s < ns; s++) {
        uint64_t k = key[s]; int64_t l = (int64_t)(k / (uint64_t)na); int32_t a = (int32_t)(k % (uint64_t)na);
        for (int b = 0; b < 2; b++) {
            int64_t l2 = tr[l * 2 + b]; int32_t a2 = (b ? g1 : g0)[a];
            if (l2 < 0 || outp[a2]) { suc[s * 2 + b] = -1; continue; }
            int32_t t; LOOKUP((uint64_t)l2 * (uint64_t)na + (uint64_t)a2, t);
            suc[s * 2 + b] = t;
        }
    }
    free(hk); free(hv); free(key);
    /* live states: those with an infinite future (iterative removal of states with no live successor) */
    int64_t nlive = ns;
    {
        int64_t *rs = calloc(ns + 1, 8); int32_t *rp = malloc((size_t)ns * 8); uint8_t *od = malloc(ns);
        for (int64_t s = 0; s < ns; s++) { od[s] = 0; for (int b = 0; b < 2; b++) if (suc[s * 2 + b] >= 0) { od[s]++; rs[suc[s * 2 + b] + 1]++; } }
        for (int64_t s = 0; s < ns; s++) rs[s + 1] += rs[s];
        int64_t *fill = malloc((ns + 1) * 8); memcpy(fill, rs, (ns + 1) * 8);
        for (int64_t s = 0; s < ns; s++) for (int b = 0; b < 2; b++) if (suc[s * 2 + b] >= 0) rp[fill[suc[s * 2 + b]]++] = (int32_t)s;
        int32_t *q = malloc(ns * 4); int64_t qh = 0, qt = 0;
        for (int64_t s = 0; s < ns; s++) if (!od[s]) q[qt++] = (int32_t)s;
        while (qh < qt) { int32_t v = q[qh++]; for (int64_t j = rs[v]; j < rs[v + 1]; j++) if (--od[rp[j]] == 0) q[qt++] = rp[j]; }
        nlive = ns - qt;
        free(rs); free(rp); free(od); free(q); free(fill);
    }
    printf("product states %lld, live (infinite future) %lld\n", (long long)ns, (long long)nlive);
    /* iterative Tarjan */
    int32_t *idx = malloc(ns * 4), *low = malloc(ns * 4), *comp = malloc(ns * 4), *stk = malloc(ns * 4);
    int32_t *cs_v = malloc(ns * 4); int8_t *cs_e = malloc(ns); uint8_t *onst = calloc(ns, 1);
    for (int64_t i = 0; i < ns; i++) { idx[i] = -1; comp[i] = -1; }
    int32_t counter = 0, sp = 0, ncomp = 0;
    for (int64_t r = 0; r < ns; r++) {
        if (idx[r] != -1) continue;
        int64_t cd = 0; cs_v[cd] = (int32_t)r; cs_e[cd] = 0; cd++;
        idx[r] = low[r] = counter++; stk[sp++] = (int32_t)r; onst[r] = 1;
        while (cd) {
            int32_t v = cs_v[cd - 1]; int e = cs_e[cd - 1];
            if (e < 2) {
                cs_e[cd - 1] = (int8_t)(e + 1);
                int32_t w = suc[v * 2 + e];
                if (w < 0) continue;
                if (idx[w] == -1) { idx[w] = low[w] = counter++; stk[sp++] = w; onst[w] = 1; cs_v[cd] = w; cs_e[cd] = 0; cd++; }
                else if (onst[w] && idx[w] < low[v]) low[v] = idx[w];
            } else {
                cd--;
                if (cd && low[v] < low[cs_v[cd - 1]]) low[cs_v[cd - 1]] = low[v];
                if (low[v] == idx[v]) { int32_t w; do { w = stk[--sp]; onst[w] = 0; comp[w] = ncomp; } while (w != v); ncomp++; }
            }
        }
    }
    free(idx); free(low); free(stk); free(cs_v); free(cs_e); free(onst);
    /* members of each component */
    int64_t *cstart = calloc(ncomp + 1, 8); int32_t *mem = malloc(ns * 4), *loc = malloc(ns * 4);
    for (int64_t i = 0; i < ns; i++) cstart[comp[i] + 1]++;
    for (int c = 0; c < ncomp; c++) cstart[c + 1] += cstart[c];
    { int64_t *fill = malloc((ncomp + 1) * 8); memcpy(fill, cstart, (ncomp + 1) * 8);
      for (int64_t i = 0; i < ns; i++) { loc[i] = (int32_t)(fill[comp[i]] - cstart[comp[i]]); mem[fill[comp[i]]++] = (int32_t)i; }
      free(fill); }
    /* per component: radius certificate */
    const uint64_t D = 1000000000ULL;
    uint64_t bestR = 0; int bestc = -1; int64_t bestsize = 0; int ncyc = 0;
    double *u = NULL, *w = NULL; size_t ucap = 0;
    for (int c = 0; c < ncomp; c++) {
        int64_t sz = cstart[c + 1] - cstart[c];
        int32_t *M = mem + cstart[c];
        int cyc = sz > 1;
        if (!cyc) { int32_t v = M[0]; cyc = suc[v * 2] == v || suc[v * 2 + 1] == v; }
        if (!cyc) continue;
        ncyc++;
        if ((size_t)sz > ucap) { ucap = sz; u = realloc(u, ucap * 8); w = realloc(w, ucap * 8); }
        for (int64_t i = 0; i < sz; i++) u[i] = 1.0;
        double lo = 0, hi = 0;
        for (int it = 0; it < 200000; it++) {
            double mx = 0;
            lo = 1e300; hi = 0;
            for (int64_t i = 0; i < sz; i++) {
                int32_t v = M[i]; double sacc = 0;
                for (int b = 0; b < 2; b++) { int32_t t = suc[v * 2 + b]; if (t >= 0 && comp[t] == c) sacc += u[loc[t]]; }
                double r = sacc / u[i]; if (r < lo) lo = r; if (r > hi) hi = r;
                w[i] = sacc + u[i]; if (w[i] > mx) mx = w[i];
            }
            for (int64_t i = 0; i < sz; i++) u[i] = w[i] / mx;
            if (hi - lo < 1e-12 && it > 50) break;
        }
        /* integer vector and certificate */
        uint64_t *ui = malloc(sz * 8);
        double umx = 0; for (int64_t i = 0; i < sz; i++) if (u[i] > umx) umx = u[i];
        for (int64_t i = 0; i < sz; i++) ui[i] = (uint64_t)ldexp(u[i] / umx, 50) + 1;
        uint64_t R = 0;
        for (int64_t i = 0; i < sz; i++) {
            int32_t v = M[i]; u128 au = 0;
            for (int b = 0; b < 2; b++) { int32_t t = suc[v * 2 + b]; if (t >= 0 && comp[t] == c) au += ui[loc[t]]; }
            u128 num = au * D, q = num / ui[i]; if (q * ui[i] < num) q++;
            if ((uint64_t)q > R) R = (uint64_t)q;
        }
        for (int64_t i = 0; i < sz; i++) {
            int32_t v = M[i]; u128 au = 0;
            for (int b = 0; b < 2; b++) { int32_t t = suc[v * 2 + b]; if (t >= 0 && comp[t] == c) au += ui[loc[t]]; }
            if (au * D > (u128)R * ui[i]) { printf("CERTIFICATE CHECK FAILED in component %d\n", c); return 5; }
        }
        free(ui);
        if (R > bestR) { bestR = R; bestc = c; bestsize = sz; }
        if (sz >= 1000) printf("  component %d: %lld states, power iteration %.12f .. %.12f, certified R/D = %llu/%llu\n",
                               c, (long long)sz, lo, hi, (unsigned long long)R, (unsigned long long)D);
    }
    printf("cyclic components %d; largest radius in component %d (%lld states)\n", ncyc, bestc, (long long)bestsize);
    /* cross-check: word-count ratio from the start state at n = 3000 */
    {
        long double *a = calloc(ns, sizeof(long double)), *b2 = calloc(ns, sizeof(long double)), ratio = 0;
        a[0] = 1;
        for (int m = 1; m <= 3000; m++) {
            memset(b2, 0, ns * sizeof(long double));
            for (int64_t s = 0; s < ns; s++) if (a[s] != 0) for (int b = 0; b < 2; b++) { int32_t t = suc[s * 2 + b]; if (t >= 0) b2[t] += a[s]; }
            long double tot = 0; for (int64_t s = 0; s < ns; s++) tot += b2[s];
            if (tot == 0) { ratio = 0; break; }
            ratio = tot; for (int64_t s = 0; s < ns; s++) b2[s] /= tot;
            long double *e = a; a = b2; b2 = e;
        }
        printf("word-count ratio at n = 3000: %.12Lf\n", ratio);
    }
    printf("CERTIFIED rho <= %llu/%llu = %.9f, log2 <= %.6f bits per symbol\n", (unsigned long long)bestR,
           (unsigned long long)D, (double)bestR / D, bestR ? log2((double)bestR / D) : -INFINITY);
    return 0;
}
