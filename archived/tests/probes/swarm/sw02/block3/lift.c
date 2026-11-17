/* Block 3: sparse lift of the double-step window graph beside the alternating centre.
 *
 * A node is a window of columns 1..W of the driven right half at an odd tick (bit i is column i + 1).
 * An edge is a double step, centre white then black, under the moves of MODE:
 *   xx  the next two columns at the tick are free: every real right half is a path, at most three distinct moves.
 *   pq  column W + 1 is free at each of the two steps: rule30-open's game, which also allows the pair that no real
 *       cell can make (column W + 1 black, then equal to column W).
 * Certified targets T(W), each closed or proved to leave column 1 harmless at that width, nested in W:
 *   gate    column 1 black and the low 16 columns good at count 0 (greatest fixed point, computed here for MODE)
 *   family  ether on columns 1..k and a kit wall state on k + 1..k + 13, k = 6 mod 7, k + 13 <= W, ether phase 0 or 2
 *   lock7   the 66 windows of 30 columns (xx), or SevenLock's 195 of 32 (pq), from that width on
 *   lock7b  the 33 windows of 45 columns, from W = 45 on
 * core(W) is the set of windows on a bi-infinite path that avoids T(W). Because T(W) lifts into T(W + 1), core(W + 1)
 * projects into core(W), so the program lifts one column at a time and peels. A forward-infinite play that avoids T(W)
 * ends inside one strongly connected component of core(W) that holds a cycle: only those components matter.
 * At each width it also deletes the windows that are cuts of the deep targets (family at any depth, including pure
 * ether; cuts of locks wider than W), peels again and reports what remains: the OVER residual. These cuts are not
 * closed sets and OVER is not nested in W, so it is computed fresh from core(W) at each width.
 *
 * Each component with a cycle gets a kind. LOCKED: column 1 is a function of the class modulo the gcd of the cycle
 * lengths, so a half that stays for ever has u eventually periodic. GAP35: every gap of column 1 is 3 or 5, the case
 * of Q01Gap. UNRESOLVED: neither. A cycle of core(W + 1) projects to a cycle of core(W), so a component at W + 1 lies
 * over one component at W: its parent. With --prune-from P only the windows of UNRESOLVED components are lifted from
 * width P on; this is exact for the UNRESOLVED lineage, because no component over a LOCKED or GAP35 one can be other
 * than LOCKED or GAP35, and it is what lets the run reach 45 columns.
 *
 * Usage: lift --targets FILE --mode xx|pq --wmax N [--wreport N] [--out DIR] [--max-nodes N] [--dump] [--dense W]
 *             [--no-lock7] [--r02] [--prune-from P] [--over-max W] [--gapn N] [--gap-limit NODES] [--resume W FILE]
 *             [--rows B T LATEFILE] [--dfa-from W] [--dfa-max STATES] [--drop-largest-at W]
 * GC2742: --resume-parts W PREFIX, --save-at W, --export-at W --export-ranks i,j, --stop-closed.
 * Checkpoints/components use 16-MiB parts, with exact count manifests.
 * --r02: targets are the kit's 829 trap windows alone, every colour, no family and no lock (R-02's graph, a control).
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/resource.h>

typedef uint64_t u64;
typedef uint32_t u32;
typedef uint16_t u16;
typedef uint8_t u8;
#define GW 16
#define NIL 0xFFFFFFFFu
#define MAXW 62

static int MODE = 0; /* 0 xx, 1 pq */
/* GC2742: checkpoint/export support for the owner-authorized width job. */
static int SAVEW = 0, EXPORTW = 0, STOPCLOSED = 0, FOUND_CLOSED = 0;
static int EXPORT_RANKS[32], NEXPORT = 0;
#define CHUNK_WORDS ((size_t)2097152) /* 16 MiB, inherited file cap */
static int R02 = 0, GAPN = 6, DFAW = 0, DFAMAX = 2000000, DROPW = 0;
static u64 GAPLIM = 40000000;
static u8 *trap16;
static const char *ETHER[7] = {"0011", "0110", "1101", "0101", "0011", "0001", "0001"};

static u8 *entry16;           /* 2^16: gate entry windows */
static u8 wallb[4][1 << 13];  /* wall states by ether phase */
static u8 wallcut[4][14][1 << 13];
static u64 *trapc, *l7, *l7b, *l5, *s7;
static int ntrap, nl7, nl7b, nl5, ns7;
static int lockw = 30, use_lock7 = 1;
static u64 *lockset; static int nlock;
static u64 pat[4]; /* ether on columns 1..62 at phases 0, 2 */

static void *xalloc(size_t n) {
    void *p = malloc(n ? n : 1);
    if (!p) { fprintf(stderr, "out of memory for %zu bytes\n", n); printf("STOP memory\n"); exit(3); }
    return p;
}
static void *xcalloc(size_t n) {
    void *p = calloc(n ? n : 1, 1);
    if (!p) { fprintf(stderr, "out of memory for %zu bytes\n", n); printf("STOP memory\n"); exit(3); }
    return p;
}
static double cpu(void) { return (double)clock() / CLOCKS_PER_SEC; }
static double rss_mib(void) {
    struct rusage r; getrusage(RUSAGE_SELF, &r);
#ifdef __APPLE__
    return r.ru_maxrss / 1048576.0;
#else
    return r.ru_maxrss / 1024.0;
#endif
}
static inline u64 st(u64 a, u64 b) { return ((a << 1) | b) ^ (a | (a >> 1)); }

/* The distinct successors of window w at width W. */
static inline int moves(u64 w, int W, u64 *out) {
    u64 mask = (1ULL << W) - 1;
    int m = 0;
    for (u64 x = 0; x < 4; x++) {
        u64 t;
        if (!MODE) {
            t = st(st(w | (x << W), 0), 1) & mask;
        } else {
            u64 x1 = x >> 1, x2 = x & 1;
            u64 a = ((w << 1) & mask) ^ (w | (w >> 1) | (x1 << (W - 1)));
            t = (((a << 1) | 1) & mask) ^ (a | (a >> 1) | (x2 << (W - 1)));
        }
        int dup = 0;
        for (int i = 0; i < m; i++) if (out[i] == t) dup = 1;
        if (!dup) out[m++] = t;
    }
    return m;
}

static int cmp64(const void *a, const void *b) {
    u64 x = *(const u64 *)a, y = *(const u64 *)b;
    return x < y ? -1 : x > y;
}
static int inset(const u64 *s, int n, u64 v) {
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int m = (lo + hi) / 2;
        if (s[m] == v) return 1;
        if (s[m] < v) lo = m + 1; else hi = m - 1;
    }
    return 0;
}

static u64 *read_list(FILE *f, int *n) {
    if (fscanf(f, "%d", n) != 1) { fprintf(stderr, "bad targets file\n"); exit(2); }
    u64 *a = xalloc(sizeof(u64) * (size_t)*n);
    for (int i = 0; i < *n; i++) if (fscanf(f, "%llu", (unsigned long long *)&a[i]) != 1) exit(2);
    qsort(a, (size_t)*n, sizeof(u64), cmp64);
    return a;
}
static void load_targets(const char *path) {
    FILE *f = fopen(path, "r");
    if (!f) { perror(path); exit(2); }
    char tag[64];
    while (fscanf(f, "%63s", tag) == 1) {
        int width;
        if (tag[0] == '#') { int c; while ((c = fgetc(f)) != '\n' && c != EOF) {} continue; }
        if (!strcmp(tag, "trap")) trapc = read_list(f, &ntrap);
        else if (!strcmp(tag, "wall")) {
            int n; if (fscanf(f, "%d", &n) != 1) exit(2);
            for (int i = 0; i < n; i++) {
                int ph, code; if (fscanf(f, "%d %d", &ph, &code) != 2) exit(2);
                wallb[ph][code] = 1;
                for (int c = 1; c <= 13; c++) wallcut[ph][c][code & ((1 << c) - 1)] = 1;
            }
        }
        else if (!strcmp(tag, "lock7")) { if (fscanf(f, "%d", &width) != 1) exit(2); l7 = read_list(f, &nl7); }
        else if (!strcmp(tag, "lock7b")) { if (fscanf(f, "%d", &width) != 1) exit(2); l7b = read_list(f, &nl7b); }
        else if (!strcmp(tag, "lock5")) { if (fscanf(f, "%d", &width) != 1) exit(2); l5 = read_list(f, &nl5); }
        else if (!strcmp(tag, "sevenlock")) { if (fscanf(f, "%d", &width) != 1) exit(2); s7 = read_list(f, &ns7); }
        else { fprintf(stderr, "unknown tag %s\n", tag); exit(2); }
    }
    fclose(f);
    for (int q = 0; q < 4; q += 2) {
        pat[q] = 0;
        for (int p = 1; p <= MAXW; p++)
            if (ETHER[(3 + p) % 7][q] == '1') pat[q] |= 1ULL << (p - 1);
    }
}

/* The gate: greatest fixed point of pairs (window of 16 columns, count), every later gap 3 or 5. */
static void make_gate(void) {
    int n = 1 << GW;
    u8 *bad = xcalloc((size_t)n * 6);
    int changed = 1, rounds = 0;
    while (changed) {
        changed = 0; rounds++;
        for (int w = 0; w < n; w++) {
            u64 mv[4]; int m = moves((u64)w, GW, mv);
            for (int d = 0; d < 6; d++) {
                if (bad[w * 6 + d]) continue;
                for (int i = 0; i < m; i++) {
                    int b = (int)(mv[i] & 1), ok, nx;
                    if (d == 5) { ok = 1; nx = b ? 0 : 5; }
                    else {
                        int gap = d + 1;
                        ok = b ? (gap == 3 || gap == 5) : gap < 5;
                        nx = b ? 0 : (gap < 4 ? gap : 4);
                    }
                    if (!ok || bad[(size_t)mv[i] * 6 + nx]) { bad[w * 6 + d] = 1; changed = 1; break; }
                }
            }
        }
    }
    entry16 = xcalloc((size_t)n);
    int ne = 0;
    for (int w = 1; w < n; w += 2) if (!bad[w * 6]) { entry16[w] = 1; ne++; }
    int kitin = 0;
    for (int i = 0; i < ntrap; i++) {
        int any = 0;
        for (int d = 0; d < 6; d++) if (!bad[trapc[i] * 6 + d]) any = 1;
        kitin += any;
    }
    int l5in = 0, l5b = 0;
    for (int i = 0; i < nl5; i++) if (l5[i] & 1) { l5b++; l5in += entry16[l5[i] & 0xFFFF]; }
    printf("gate rounds %d entry windows %d; kit trap windows good for some count %d of %d; lock-5 black windows in entry %d of %d\n",
           rounds, ne, kitin, ntrap, l5in, l5b);
    free(bad);
}

/* Family with the wall inside the window. */
static inline int fam_under(u64 w, int W) {
    for (int q = 0; q < 4; q += 2)
        for (int k = 6; k + 13 <= W; k += 7) {
            if ((w ^ pat[q]) & ((1ULL << k) - 1)) break;
            if (wallb[q][(w >> k) & 0x1FFF]) return 1;
        }
    return 0;
}
/* Cut of a family member at any depth, pure ether included. */
static inline int fam_cut(u64 w, int W) {
    u64 mask = (1ULL << W) - 1;
    for (int q = 0; q < 4; q += 2) {
        if (((w ^ pat[q]) & mask) == 0) return 1;
        for (int k = 6; k < W; k += 7) {
            if ((w ^ pat[q]) & ((1ULL << k) - 1)) break;
            int cells = W - k < 13 ? W - k : 13;
            if (wallcut[q][cells][(w >> k) & ((1ULL << cells) - 1)]) return 1;
        }
    }
    return 0;
}
static inline int is_target(u64 w, int W) {
    if (R02) return trap16[w & 0xFFFF] ? 1 : 0;
    if ((w & 1) && entry16[w & 0xFFFF]) return 1;
    if (fam_under(w, W)) return 2;
    if (use_lock7 && W >= lockw && inset(lockset, nlock, w & ((1ULL << lockw) - 1))) return 3;
    /* lock-7b has two exits under the extra, nonphysical pq moves. */
    if (!MODE && W >= 45 && inset(l7b, nl7b, w & ((1ULL << 45) - 1))) return 4;
    return 0;
}

/* Sorted-array lookup with a bucket index on the top bits. */
static u32 *bucket; static int bbits; static int bshift;
static void make_bucket(const u64 *core, size_t n, int W) {
    bbits = W < 24 ? W : 24; bshift = W - bbits;
    free(bucket);
    size_t nb = (size_t)1 << bbits;
    bucket = xalloc(sizeof(u32) * (nb + 1));
    size_t i = 0;
    for (size_t b = 0; b < nb; b++) {
        bucket[b] = (u32)i;
        while (i < n && (core[i] >> bshift) == b) i++;
    }
    bucket[nb] = (u32)i;
}
static inline u32 find(const u64 *core, u64 v) {
    u64 b = v >> bshift;
    u32 lo = bucket[b], hi = bucket[b + 1];
    while (lo < hi) {
        u32 m = lo + (hi - lo) / 2;
        if (core[m] == v) return m;
        if (core[m] < v) lo = m + 1; else hi = m;
    }
    return NIL;
}

/* Peel to the windows on a bi-infinite path. Returns the new size; succ (4 per node, NIL padded) is rebuilt. */
static size_t peel(u64 *core, size_t n, int W, u32 **succ_out) {
    make_bucket(core, n, W);
    u32 *succ = xalloc(sizeof(u32) * 4 * n);
    u8 *outd = xalloc(n);
    u32 *pstart = xcalloc(sizeof(u32) * (n + 2));
    for (size_t i = 0; i < n; i++) {
        u64 mv[4]; int m = moves(core[i], W, mv), c = 0;
        for (int j = 0; j < m; j++) {
            u32 t = find(core, mv[j]);
            if (t != NIL) { succ[4 * i + c++] = t; pstart[t + 2]++; }
        }
        for (int j = c; j < 4; j++) succ[4 * i + j] = NIL;
        outd[i] = (u8)c;
    }
    for (size_t i = 2; i < n + 2; i++) pstart[i] += pstart[i - 1];
    u32 *pred = xalloc(sizeof(u32) * (size_t)(pstart[n + 1] + 1));
    for (size_t i = 0; i < n; i++)
        for (int j = 0; j < 4 && succ[4 * i + j] != NIL; j++) pred[pstart[succ[4 * i + j] + 1]++] = (u32)i;
    /* pstart[t] .. pstart[t + 1] now holds the predecessors of t */
    u16 *ind = xalloc(sizeof(u16) * n);
    for (size_t i = 0; i < n; i++) ind[i] = (u16)(pstart[i + 1] - pstart[i]);
    u8 *dead = xcalloc(n);
    u32 *q = xalloc(sizeof(u32) * n);
    size_t qh = 0, qt = 0;
    for (size_t i = 0; i < n; i++) if (!outd[i] || !ind[i]) { dead[i] = 1; q[qt++] = (u32)i; }
    while (qh < qt) {
        u32 v = q[qh++];
        for (int j = 0; j < 4 && succ[4 * (size_t)v + j] != NIL; j++) {
            u32 t = succ[4 * (size_t)v + j];
            if (!dead[t] && --ind[t] == 0) { dead[t] = 1; q[qt++] = t; }
        }
        for (u32 e = pstart[v]; e < pstart[v + 1]; e++) {
            u32 p = pred[e];
            if (!dead[p] && --outd[p] == 0) { dead[p] = 1; q[qt++] = p; }
        }
    }
    free(pred); free(ind); free(outd); free(q);
    u32 *map = pstart; /* reuse */
    size_t m = 0;
    for (size_t i = 0; i < n; i++) map[i] = dead[i] ? NIL : (u32)m++;
    for (size_t i = 0; i < n; i++) {
        if (dead[i]) continue;
        size_t d = map[i];
        int c = 0;
        u32 row[4];
        for (int j = 0; j < 4 && succ[4 * i + j] != NIL; j++) {
            u32 t = map[succ[4 * i + j]];
            if (t != NIL) row[c++] = t;
        }
        for (int j = c; j < 4; j++) row[j] = NIL;
        core[d] = core[i];
        memcpy(&succ[4 * d], row, sizeof(row));
    }
    free(dead); free(map);
    if (m) make_bucket(core, m, W);
    *succ_out = succ;
    return m;
}

static u64 gcd64(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }

/* Cheap sweeps before peel: drop windows with no surviving successor or predecessor, without building the lists. */
static size_t prefilter(u64 *core, size_t n, int W) {
    for (int sweep = 0; sweep < 6; sweep++) {
        make_bucket(core, n, W);
        u8 *fl = xcalloc(n); /* bit 0 has a successor, bit 1 has a predecessor */
        for (size_t i = 0; i < n; i++) {
            u64 mv[4]; int m = moves(core[i], W, mv);
            for (int j = 0; j < m; j++) {
                u32 t = find(core, mv[j]);
                if (t != NIL) { fl[i] |= 1; fl[t] |= 2; }
            }
        }
        size_t k = 0;
        for (size_t i = 0; i < n; i++) if (fl[i] == 3) core[k++] = core[i];
        free(fl);
        int done = k == n || (double)(n - k) < 0.01 * (double)n;
        n = k;
        if (done || !n) break;
    }
    return n;
}

enum { LOCKED = 1, GAP35 = 2, UNRESOLVED = 3 };
static const char *KIND[4] = {"?", "LOCKED", "GAP35", "UNRESOLVED"};
typedef struct {
    u64 nodes, edges, states, gcd, leak_core, leak_out, black, proj16, famcut, l7, l7b, s7cut;
    u64 primitive_period;
    u32 gaps, id; int locked, ether, closed, whitecycle, kind, parent; u64 first;
    char word[72];
    char primitive_word[72];
} Comp;

static void save_parts(const char *prefix, const u64 *a, size_t n) {
    char path[1200];
    size_t offset = 0; int part = 0;
    while (offset < n) {
        size_t count = n - offset < CHUNK_WORDS ? n - offset : CHUNK_WORDS;
        snprintf(path, sizeof path, "%s.part%03d.bin", prefix, part++);
        FILE *f = fopen(path, "wb");
        if (!f || fwrite(a + offset, 8, count, f) != count || fclose(f)) { perror(path); exit(2); }
        offset += count;
    }
    snprintf(path, sizeof path, "%s.count", prefix);
    FILE *f = fopen(path, "w");
    if (!f) { perror(path); exit(2); }
    fprintf(f, "%zu %d\n", n, part);
    if (fclose(f)) exit(2);
}

static u64 *read_parts(const char *prefix, size_t *n) {
    char path[1200]; int parts;
    snprintf(path, sizeof path, "%s.count", prefix);
    FILE *f = fopen(path, "r");
    if (!f || fscanf(f, "%zu %d", n, &parts) != 2) { perror(path); exit(2); }
    fclose(f);
    if (*n > 120000000 || parts != (int)((*n + CHUNK_WORDS - 1) / CHUNK_WORDS)) exit(2);
    u64 *a = xalloc(8 * *n); size_t offset = 0;
    for (int k = 0; k < parts; k++) {
        snprintf(path, sizeof path, "%s.part%03d.bin", prefix, k);
        size_t count = *n - offset < CHUNK_WORDS ? *n - offset : CHUNK_WORDS;
        f = fopen(path, "rb");
        if (!f || fread(a + offset, 8, count, f) != count || fgetc(f) != EOF) { perror(path); exit(2); }
        fclose(f); offset += count;
    }
    for (size_t k = 1; k < *n; k++) if (a[k-1] >= a[k]) { fprintf(stderr, "unsorted resume\n"); exit(2); }
    return a;
}
/* the components of the previous width, for parents */
static u64 *pw; static int *pc; static size_t npw;
static int parent_of(u64 w, int W) {
    if (!npw) return -1;
    u64 v = w & ((1ULL << (W - 1)) - 1);
    size_t lo = 0, hi = npw;
    while (lo < hi) {
        size_t m = lo + (hi - lo) / 2;
        if (pw[m] == v) return pc[m];
        if (pw[m] < v) lo = m + 1; else hi = m;
    }
    return -1;
}
static int cmpcomp(const void *a, const void *b) {
    const Comp *x = a, *y = b;
    return x->nodes < y->nodes ? 1 : x->nodes > y->nodes ? -1 : 0;
}
static void gapstr(u32 g, int wc, char *s) {
    int p = 0; s[p++] = '[';
    for (int i = 1; i < 32; i++) if (g >> i & 1) p += sprintf(s + p, p > 1 ? ",%d" : "%d", i);
    s[p++] = ']'; s[p] = 0;
    if (wc) strcat(s, "+white");
}

/* The gap words of column 1 inside one component: every word of gaps up to length GAPN on a path of the component. */
static u32 *gmark; static u32 gstamp;
static const u32 *gcomp; static u32 gc; static const u32 *gsucc; static const u64 *gcore;
static u64 gcount[40]; static FILE *gfile; static char gw[64];
static void gaprec(const u32 *set, size_t m, int depth) {
    gcount[depth]++;
    if (depth == GAPN) { if (gfile) fprintf(gfile, "%.*s\n", depth, gw); return; }
    u32 *cur = xalloc(sizeof(u32) * m), *nxt = NULL;
    size_t nc = m;
    memcpy(cur, set, sizeof(u32) * m);
    for (int g = 1; g <= 9 && nc; g++) {
        size_t capn = nc * 4, n2 = 0, nb = 0;
        nxt = xalloc(sizeof(u32) * capn);
        u32 *bl = xalloc(sizeof(u32) * capn);
        u32 s1 = ++gstamp, s2 = ++gstamp;
        for (size_t i = 0; i < nc; i++) {
            u32 v = cur[i];
            for (int j = 0; j < 4 && gsucc[4 * (size_t)v + j] != NIL; j++) {
                u32 x = gsucc[4 * (size_t)v + j];
                if (gcomp[x] != gc) continue;
                if (gcore[x] & 1) { if (gmark[x] != s1) { gmark[x] = s1; bl[nb++] = x; } }
                else if (gmark[x] != s2) { gmark[x] = s2; nxt[n2++] = x; }
            }
        }
        if (nb) { gw[depth] = (char)('0' + g); gaprec(bl, nb, depth + 1); }
        free(bl); free(cur);
        cur = nxt; nc = n2;
    }
    free(cur);
}

/* The exact gap language of one component: subset construction on its gap automaton, from all black windows.
 * A DFA state is a set of black windows, kept only until it is expanded, and named by an order-free 128-bit hash. */
static inline u64 mix64(u64 x) {
    x += 0x9E3779B97F4A7C15ULL; x = (x ^ (x >> 30)) * 0xBF58476D1CE4E5B9ULL;
    x = (x ^ (x >> 27)) * 0x94D049BB133111EBULL; return x ^ (x >> 31);
}
typedef struct { u64 a, b; u32 size; int id; } DKey;
typedef struct { u32 *set; u32 size; int id; } DItem;
static DKey *dtab; static size_t dcap, dcount;
static int dfind(u64 a, u64 b, u32 size) {
    size_t i = (size_t)(a % dcap);
    for (;;) {
        if (dtab[i].id < 0) { dtab[i].a = a; dtab[i].b = b; dtab[i].size = size; dtab[i].id = (int)dcount++; return -1 - dtab[i].id; }
        if (dtab[i].a == a && dtab[i].b == b && dtab[i].size == size) return dtab[i].id;
        if (++i == dcap) i = 0;
    }
}
static void gapdfa(const u32 *comp, const u32 *succ, const u64 *core, u32 c, const u32 *bl, size_t nb, size_t n, const char *path, int maxstates) {
    dcap = (size_t)maxstates * 4 + 7; dtab = xalloc(sizeof(DKey) * dcap); dcount = 0;
    for (size_t i = 0; i < dcap; i++) dtab[i].id = -1;
    u32 *mark = xcalloc(sizeof(u32) * n); u32 stamp = 0;
    FILE *f = fopen(path, "w");
    size_t qcap = (size_t)maxstates + 1, qh = 0, qt = 0;
    DItem *q = xalloc(sizeof(DItem) * qcap);
    u64 ha = 0, hb = 0;
    for (size_t i = 0; i < nb; i++) { ha += mix64(bl[i]); hb += mix64((u64)bl[i] ^ 0xABCDEF0123456789ULL); }
    (void)dfind(ha, hb, (u32)nb);
    q[qt].set = xalloc(sizeof(u32) * nb); memcpy(q[qt].set, bl, sizeof(u32) * nb); q[qt].size = (u32)nb; q[qt].id = 0; qt++;
    int overflow = 0;
    while (qh < qt) {
        DItem it = q[qh++];
        if (f) fprintf(f, "%d %u", it.id, it.size);
        u32 *cur = it.set; size_t nc = it.size;
        for (int g = 1; g <= 9 && nc; g++) {
            size_t capn = nc * 4, n2 = 0, nbk = 0;
            u32 *nxt = xalloc(sizeof(u32) * capn), *bk = xalloc(sizeof(u32) * capn);
            u32 s1 = ++stamp, s2 = ++stamp;
            for (size_t i = 0; i < nc; i++) {
                u32 v = cur[i];
                for (int j = 0; j < 4 && succ[4 * (size_t)v + j] != NIL; j++) {
                    u32 x = succ[4 * (size_t)v + j];
                    if (comp[x] != c) continue;
                    if (core[x] & 1) { if (mark[x] != s1) { mark[x] = s1; bk[nbk++] = x; } }
                    else if (mark[x] != s2) { mark[x] = s2; nxt[n2++] = x; }
                }
            }
            if (nbk) {
                u64 a = 0, b = 0;
                for (size_t i = 0; i < nbk; i++) { a += mix64(bk[i]); b += mix64((u64)bk[i] ^ 0xABCDEF0123456789ULL); }
                int id = -1;
                if (dcount < (size_t)maxstates) {
                    id = dfind(a, b, (u32)nbk);
                    if (id < 0) {
                        id = -1 - id;
                        q[qt].set = xalloc(sizeof(u32) * nbk); memcpy(q[qt].set, bk, sizeof(u32) * nbk);
                        q[qt].size = (u32)nbk; q[qt].id = id; qt++;
                    }
                } else overflow = 1;
                if (f) fprintf(f, " %d:%d", g, id);
            }
            free(bk); free(cur);
            cur = nxt; nc = n2;
        }
        free(cur);
        if (f) fprintf(f, "\n");
    }
    if (f) fclose(f);
    printf(" GAPDFA W %d states %zu%s\n", (int)0, dcount, overflow ? " OVERFLOW" : "");
    free(q); free(dtab); free(mark);
}

/* Strongly connected components with a cycle, and what each one holds. With keep, the UNRESOLVED windows are returned. */
static void analyse(const u64 *core, size_t n, const u32 *succ, int W, const char *label, FILE *js, int track,
                    const char *dir, u64 **keep, size_t *nkeep) {
    u32 *idx = xcalloc(sizeof(u32) * n), *low = xalloc(sizeof(u32) * n), *comp = xalloc(sizeof(u32) * n);
    u32 *stk = xalloc(sizeof(u32) * n), *cs = xalloc(sizeof(u32) * n);
    u8 *ce = xalloc(n), *onst = xcalloc(n);
    u32 counter = 0, nc = 0; size_t sp = 0;
    for (size_t r = 0; r < n; r++) {
        if (idx[r]) continue;
        size_t top = 0; cs[0] = (u32)r; ce[0] = 0;
        idx[r] = low[r] = ++counter; stk[sp++] = (u32)r; onst[r] = 1;
        while (1) {
            u32 v = cs[top];
            if (ce[top] < 4 && succ[4 * (size_t)v + ce[top]] != NIL) {
                u32 t = succ[4 * (size_t)v + ce[top]++];
                if (!idx[t]) {
                    idx[t] = low[t] = ++counter; stk[sp++] = t; onst[t] = 1;
                    top++; cs[top] = t; ce[top] = 0;
                } else if (onst[t] && idx[t] < low[v]) low[v] = idx[t];
            } else {
                if (low[v] == idx[v]) {
                    u32 t;
                    do { t = stk[--sp]; onst[t] = 0; comp[t] = nc; } while (t != v);
                    nc++;
                }
                if (top == 0) break;
                top--;
                u32 p = cs[top];
                if (low[v] < low[p]) low[p] = low[v];
            }
        }
    }
    free(stk); free(cs); free(ce); free(onst); free(idx);
    /* group members */
    u32 *cstart = xcalloc(sizeof(u32) * ((size_t)nc + 2));
    for (size_t i = 0; i < n; i++) cstart[comp[i] + 1]++;
    for (size_t c = 1; c <= nc; c++) cstart[c] += cstart[c - 1];
    u32 *mem = xalloc(sizeof(u32) * n);
    u32 *pos = xalloc(sizeof(u32) * ((size_t)nc + 1));
    memcpy(pos, cstart, sizeof(u32) * ((size_t)nc + 1));
    for (size_t i = 0; i < n; i++) mem[pos[comp[i]]++] = (u32)i;
    free(pos);
    u32 *lev = low; /* reuse */
    u8 *dm = xcalloc(n), *mark = xcalloc(n);
    u32 *fr = xalloc(sizeof(u32) * n), *fr2 = xalloc(sizeof(u32) * n);
    u8 *seen16 = xalloc(1 << 16);
    Comp *out = NULL; size_t no = 0, cap = 0;
    /* cuts of the wide sets at this width */
    int wl7 = lockw, nb7 = 0, n7c = 0, nsc = 0;
    u64 *c7b = xalloc(sizeof(u64) * (size_t)(nl7b + 1)), *c7 = xalloc(sizeof(u64) * (size_t)(nl7 + 1));
    u64 *cs7 = xalloc(sizeof(u64) * (size_t)(ns7 + 1));
    u64 mask = (1ULL << W) - 1;
    for (int i = 0; i < nl7b; i++) c7b[nb7++] = l7b[i] & mask;
    for (int i = 0; i < nl7; i++) c7[n7c++] = l7[i] & mask;
    for (int i = 0; i < ns7; i++) cs7[nsc++] = s7[i] & mask;
    qsort(c7b, (size_t)nb7, sizeof(u64), cmp64); qsort(c7, (size_t)n7c, sizeof(u64), cmp64); qsort(cs7, (size_t)nsc, sizeof(u64), cmp64);
    (void)wl7;
    for (u32 c = 0; c < nc; c++) {
        u32 a = cstart[c], b = cstart[c + 1], sz = b - a;
        int cyc = sz > 1;
        if (sz == 1) {
            u32 v = mem[a];
            for (int j = 0; j < 4 && succ[4 * (size_t)v + j] != NIL; j++) if (succ[4 * (size_t)v + j] == v) cyc = 1;
        }
        if (!cyc) continue;
        Comp C; memset(&C, 0, sizeof(C));
        C.nodes = sz; C.first = core[mem[a]]; C.id = c; C.parent = track ? parent_of(C.first, W) : -1;
        memset(seen16, 0, 1 << 16);
        for (u32 i = a; i < b; i++) {
            u32 v = mem[i]; u64 w = core[v], mv[4];
            int m = moves(w, W, mv), s = 0;
            for (int j = 0; j < 4 && succ[4 * (size_t)v + j] != NIL; j++) {
                s++;
                if (comp[succ[4 * (size_t)v + j]] == c) C.edges++; else C.leak_core++;
            }
            C.leak_out += (u64)(m - s);
            C.black += w & 1;
            if (!seen16[w & 0xFFFF]) { seen16[w & 0xFFFF] = 1; C.proj16++; }
            if (w == (pat[0] & mask) || w == (pat[2] & mask)) C.ether = 1;
            if (fam_cut(w, W)) C.famcut++;
            if (W < lockw && inset(c7, n7c, w)) C.l7++;
            if (W < 45 && inset(c7b, nb7, w)) C.l7b++;
            if (W < 32 && inset(cs7, nsc, w)) C.s7cut++;
        }
        C.closed = C.leak_core == 0 && C.leak_out == 0;
        /* gcd of cycle lengths, and whether column 1 is a function of the class */
        for (u32 i = a; i < b; i++) lev[mem[i]] = NIL;
        size_t h = 0, t = 0; fr[t++] = mem[a]; lev[mem[a]] = 0;
        u64 g = 0;
        while (h < t) {
            u32 v = fr[h++];
            for (int j = 0; j < 4 && succ[4 * (size_t)v + j] != NIL; j++) {
                u32 x = succ[4 * (size_t)v + j];
                if (comp[x] != c) continue;
                if (lev[x] == NIL) { lev[x] = lev[v] + 1; fr[t++] = x; }
                else { u64 dlt = lev[v] + 1 > lev[x] ? lev[v] + 1 - lev[x] : lev[x] - lev[v] - 1; g = gcd64(g, dlt); }
            }
        }
        C.gcd = g;
        C.locked = 1;
        if (g == 0) C.locked = 0;
        else {
            int8_t *cl = xalloc((size_t)g);
            memset(cl, -1, (size_t)g);
            for (u32 i = a; i < b; i++) {
                u32 v = mem[i]; int col = (int)(core[v] & 1); u64 k = lev[v] % g;
                if (cl[k] < 0) cl[k] = (int8_t)col; else if (cl[k] != col) C.locked = 0;
            }
            if (C.locked && g < 64) { for (u64 k = 0; k < g; k++) C.word[k] = (char)('0' + (cl[k] > 0)); }
            if (C.locked) {
                /* Least output-word period; gcd is the graph period. */
                u32 *pi = xcalloc(sizeof(u32) * (size_t)g);
                for (u64 k = 0; k < g; k++) if (cl[k] < 0) { fprintf(stderr, "empty cyclic phase\n"); exit(2); }
                for (u32 k = 1; k < g; k++) {
                    u32 j = pi[k-1];
                    while (j && cl[k] != cl[j]) j = pi[j-1];
                    if (cl[k] == cl[j]) j++;
                    pi[k] = j;
                }
                u64 p = g - pi[g-1];
                if (g % p) p = g;
                C.primitive_period = p;
                for (u64 k = 0; k < p && k < 64; k++) C.primitive_word[k] = (char)('0' + cl[k]);
                free(pi);
            }
            free(cl);
        }
        /* gaps between black cells of column 1, as a layered search */
        size_t nf = 0;
        for (u32 i = a; i < b; i++) if (core[mem[i]] & 1) fr[nf++] = mem[i];
        if (nf == 0) C.whitecycle = 1;
        for (int gp = 1; gp < 31 && nf; gp++) {
            size_t n2 = 0;
            for (size_t i = 0; i < nf; i++) {
                u32 v = fr[i];
                for (int j = 0; j < 4 && succ[4 * (size_t)v + j] != NIL; j++) {
                    u32 x = succ[4 * (size_t)v + j];
                    if (comp[x] != c) continue;
                    if (core[x] & 1) C.gaps |= 1u << gp;
                    else if (!mark[x]) { mark[x] = 1; fr2[n2++] = x; }
                }
            }
            for (size_t i = 0; i < n2; i++) mark[fr2[i]] = 0;
            u32 *tmp = fr; fr = fr2; fr2 = tmp; nf = n2;
            if (gp == 30 && nf) C.whitecycle = 1;
        }
        /* consistent states (window, count): counts reachable from the black windows inside the component */
        for (u32 i = a; i < b; i++) dm[mem[i]] = (core[mem[i]] & 1) ? 1 : 0;
        h = 0; t = 0;
        for (u32 i = a; i < b; i++) if (core[mem[i]] & 1) { fr[t++] = mem[i]; mark[mem[i]] = 1; }
        size_t capq = n;
        while (h != t) {
            u32 v = fr[h]; h = h + 1 == capq ? 0 : h + 1; mark[v] = 0;
            for (int j = 0; j < 4 && succ[4 * (size_t)v + j] != NIL; j++) {
                u32 x = succ[4 * (size_t)v + j];
                if (comp[x] != c || (core[x] & 1)) continue;
                u8 add = 0;
                for (int d = 0; d < 5; d++) if (dm[v] >> d & 1) { int e = d + 1 < 4 ? d + 1 : 4; add |= (u8)(1 << e); }
                if (add & ~dm[x]) {
                    dm[x] |= add;
                    if (!mark[x]) { mark[x] = 1; fr[t] = x; t = t + 1 == capq ? 0 : t + 1; }
                }
            }
        }
        for (u32 i = a; i < b; i++) {
            u8 d = dm[mem[i]];
            while (d) { C.states += d & 1; d >>= 1; }
        }
        C.kind = C.locked ? LOCKED : (!C.whitecycle && !(C.gaps & ~((1u << 3) | (1u << 5)))) ? GAP35 : UNRESOLVED;
        if (no == cap) { cap = cap ? 2 * cap : 64; out = realloc(out, sizeof(Comp) * cap); }
        out[no++] = C;
    }
    qsort(out, no, sizeof(Comp), cmpcomp);
    int *rank = xalloc(sizeof(int) * ((size_t)nc + 1));
    memset(rank, -1, sizeof(int) * ((size_t)nc + 1));
    for (size_t i = 0; i < no; i++) rank[out[i].id] = (int)i;
    if (track) {
        free(pw); free(pc); npw = 0;
        size_t cnt = 0;
        for (size_t i = 0; i < n; i++) if (rank[comp[i]] >= 0) cnt++;
        pw = xalloc(8 * cnt); pc = xalloc(sizeof(int) * cnt);
        for (size_t i = 0; i < n; i++) if (rank[comp[i]] >= 0) { pw[npw] = core[i]; pc[npw++] = rank[comp[i]]; }
    }
    if (keep) {
        /* --drop-largest-at W: leave out the largest UNRESOLVED component at that width, with all its descendants */
        int drop = -1;
        if (W == DROPW) for (size_t i = 0; i < no; i++) if (out[i].kind == UNRESOLVED) { drop = (int)i; break; }
        size_t cnt = 0;
        for (size_t i = 0; i < n; i++) if (rank[comp[i]] >= 0 && rank[comp[i]] != drop && out[rank[comp[i]]].kind == UNRESOLVED) cnt++;
        *keep = xalloc(8 * cnt); *nkeep = 0;
        for (size_t i = 0; i < n; i++) if (rank[comp[i]] >= 0 && rank[comp[i]] != drop && out[rank[comp[i]]].kind == UNRESOLVED) (*keep)[(*nkeep)++] = core[i];
    }
    free(rank);
    u64 tot = 0; for (size_t i = 0; i < no; i++) tot += out[i].nodes;
    printf(" %s W %d nodes %zu cyclic-components %zu in-cycles %llu\n", label, W, n, no, (unsigned long long)tot);
    for (size_t i = 0; i < no; i++) {
        Comp *C = &out[i]; char gs[160]; gapstr(C->gaps, C->whitecycle, gs);
        int selected = 0;
        if (W == EXPORTW) for (int k = 0; k < NEXPORT; k++) selected |= (int)i == EXPORT_RANKS[k];
        if (selected || (STOPCLOSED && C->closed)) {
            size_t count = 0;
            u64 *members = xalloc(8 * (size_t)C->nodes);
            for (size_t v = 0; v < n; v++) if (comp[v] == C->id) members[count++] = core[v];
            if (count != C->nodes) exit(2);
            char prefix[1024];
            snprintf(prefix, sizeof prefix, "%s/%s_W%d_r%zu", dir, C->closed ? "closed" : "selected", W, i);
            save_parts(prefix, members, count);
            printf(" EXPORT W %d rank %zu nodes %zu closed %d prefix %s\n", W, i, count, C->closed, prefix);
            free(members);
            if (STOPCLOSED && C->closed) FOUND_CLOSED = 1;
        }
        if (i < 24)
            printf("  %s #%zu %s parent %d nodes %llu states %llu edges %llu gcd %llu word %s gaps %s leaks %llu core %llu out%s%s famcut %llu l7cut %llu sevencut %llu l7bcut %llu proj16 %llu black %.3f first %llu\n",
                   label, i, KIND[C->kind], C->parent, (unsigned long long)C->nodes, (unsigned long long)C->states, (unsigned long long)C->edges,
                   (unsigned long long)C->gcd, C->word[0] ? C->word : "-", gs,
                   (unsigned long long)C->leak_core, (unsigned long long)C->leak_out,
                   C->closed ? " CLOSED" : "", C->ether ? " ETHER" : "",
                   (unsigned long long)C->famcut, (unsigned long long)C->l7, (unsigned long long)C->s7cut, (unsigned long long)C->l7b,
                   (unsigned long long)C->proj16, (double)C->black / (double)C->nodes, (unsigned long long)C->first);
        if (js)
            fprintf(js, "{\"W\":%d,\"stage\":\"%s\",\"rank\":%zu,\"kind\":\"%s\",\"parent\":%d,\"word\":\"%s\",\"nodes\":%llu,\"states\":%llu,\"edges\":%llu,\"gcd\":%llu,\"locked\":%d,\"gaps\":\"%s\",\"leak_core\":%llu,\"leak_out\":%llu,\"closed\":%d,\"ether\":%d,\"famcut\":%llu,\"l7cut\":%llu,\"sevencut\":%llu,\"l7bcut\":%llu,\"proj16\":%llu,\"black\":%llu,\"first\":%llu,\"primitive_period\":%llu,\"primitive_word\":\"%s\",\"primitive_word_truncated\":%d}\n",
                    W, label, i, KIND[C->kind], C->parent, C->word, (unsigned long long)C->nodes, (unsigned long long)C->states, (unsigned long long)C->edges,
                    (unsigned long long)C->gcd, C->locked, gs, (unsigned long long)C->leak_core, (unsigned long long)C->leak_out,
                    C->closed, C->ether, (unsigned long long)C->famcut, (unsigned long long)C->l7, (unsigned long long)C->s7cut,
                    (unsigned long long)C->l7b, (unsigned long long)C->proj16, (unsigned long long)C->black, (unsigned long long)C->first,
                    (unsigned long long)C->primitive_period, C->primitive_word, C->primitive_period > 64);
    }
    if (no > 24) printf("  %s ... %zu more components, in the jsonl\n", label, no - 24);
    fflush(stdout); if (js) fflush(js);
    if (track && DFAW && W >= DFAW) {
        for (size_t i = 0; i < no; i++) {
            if (out[i].kind != UNRESOLVED) continue;
            u32 c = out[i].id, a = cstart[c], b = cstart[c + 1];
            u32 *bl = xalloc(sizeof(u32) * (b - a)); size_t nb = 0;
            for (u32 j = a; j < b; j++) if (core[mem[j]] & 1) bl[nb++] = mem[j];
            char p[1024]; snprintf(p, sizeof p, "%s/dfa_%s_W%d_c%zu.txt", dir, MODE ? "pq" : "xx", W, i);
            gapdfa(comp, succ, core, c, bl, nb, n, p, DFAMAX);
            free(bl);
        }
    }
    /* gap words of the UNRESOLVED components */
    if (track && GAPN > 0) {
        gmark = xcalloc(sizeof(u32) * n); gstamp = 0; gcomp = comp; gsucc = succ; gcore = core;
        for (size_t i = 0; i < no; i++) {
            if (out[i].kind != UNRESOLVED || out[i].nodes > GAPLIM) continue;
            u32 c = out[i].id, a = cstart[c], b = cstart[c + 1];
            u32 *bl = xalloc(sizeof(u32) * (b - a)); size_t nb = 0;
            for (u32 j = a; j < b; j++) if (core[mem[j]] & 1) bl[nb++] = mem[j];
            char p[1024]; snprintf(p, sizeof p, "%s/gapwords_%s_W%d_c%zu.txt", dir, MODE ? "pq" : "xx", W, i);
            gfile = fopen(p, "w"); memset(gcount, 0, sizeof gcount); gc = c;
            gaprec(bl, nb, 0);
            if (gfile) fclose(gfile);
            free(bl);
            printf(" GAPWORDS W %d component %zu counts by length", W, i);
            for (int d = 1; d <= GAPN; d++) printf(" %llu", (unsigned long long)gcount[d]);
            printf("\n");
        }
        free(gmark); gmark = NULL;
    }
    free(out); free(c7b); free(c7); free(cs7); free(seen16); free(fr); free(fr2); free(dm); free(mark);
    free(mem); free(cstart); free(comp); free(low);
}

/* How far the core still shrinks when cut to fewer columns. */
static void projections(const u64 *core, size_t n, int W) {
    printf(" PROJ W %d", W);
    for (int w = 16; w <= 32 && w <= W; w += 4) {
        size_t bytes = ((size_t)1 << w) / 8;
        u8 *b = xcalloc(bytes);
        u64 m = (1ULL << w) - 1, c = 0;
        for (size_t i = 0; i < n; i++) {
            u64 v = core[i] & m;
            if (!(b[v >> 3] >> (v & 7) & 1)) { b[v >> 3] |= (u8)(1 << (v & 7)); c++; }
        }
        free(b);
        printf(" w%d=%llu", w, (unsigned long long)c);
    }
    printf("\n");
}

/* OVER: delete the cuts of the deep targets from core(W), peel, report. */
static void over_stage(const u64 *core, size_t n, int W, FILE *js, const char *dir, int dump) {
    u64 mask = (1ULL << W) - 1;
    int nb7 = 0, n7c = 0;
    u64 *c7b = xalloc(sizeof(u64) * (size_t)(nl7b + 1)), *c7 = xalloc(sizeof(u64) * (size_t)(nl7 + 1));
    if (W < 45) for (int i = 0; i < nl7b; i++) c7b[nb7++] = l7b[i] & mask;
    if (W < lockw) for (int i = 0; i < nl7; i++) c7[n7c++] = l7[i] & mask;
    qsort(c7b, (size_t)nb7, sizeof(u64), cmp64); qsort(c7, (size_t)n7c, sizeof(u64), cmp64);
    u64 *o = xalloc(sizeof(u64) * n); size_t m = 0, nf = 0, nl = 0;
    for (size_t i = 0; i < n; i++) {
        int f = fam_cut(core[i], W), l = inset(c7b, nb7, core[i]) || inset(c7, n7c, core[i]);
        nf += (size_t)f; nl += (size_t)(l && !f);
        if (!f && !l) o[m++] = core[i];
    }
    u32 *succ = NULL;
    size_t k = m ? peel(o, m, W, &succ) : 0;
    printf(" OVER W %d famcut %zu lockcut %zu left %zu after peel %zu\n", W, nf, nl, m, k);
    if (k) { analyse(o, k, succ, W, "OVER", js, 0, dir, NULL, NULL); }
    if (dump && k) {
        char p[1024]; snprintf(p, sizeof p, "%s/over_%d_%s.bin", dir, W, MODE ? "pq" : "xx");
        FILE *f = fopen(p, "wb"); if (f) { fwrite(o, 8, k, f); fclose(f); }
    }
    free(succ); free(o); free(c7b); free(c7);
}

/* Dense forced basin at one width, for the outside baseline. Weights: black 1, white 5 consistent states. */
static void dense(int W) {
    size_t n = (size_t)1 << W;
    u8 *in = xalloc(n);
    u64 tw = 0, tgate = 0, tfam = 0;
    for (size_t w = 0; w < n; w++) {
        int g = (w & 1) && entry16[w & 0xFFFF], f = fam_under((u64)w, W);
        in[w] = (u8)(g || f);
        if (in[w]) tw += (w & 1) ? 1 : 5;
        if (g) tgate++;
        if (f) tfam += (w & 1) ? 1 : 5;
    }
    int sweeps = 0, ch = 1;
    while (ch) {
        ch = 0; sweeps++;
        u8 *nx = xalloc(n); memcpy(nx, in, n);
        for (size_t w = 0; w < n; w++) {
            if (in[w]) continue;
            u64 mv[4]; int m = moves((u64)w, W, mv), all = 1;
            for (int j = 0; j < m; j++) if (!in[mv[j]]) { all = 0; break; }
            if (all) { nx[w] = 1; ch = 1; }
        }
        free(in); in = nx;
    }
    u64 basin = 0;
    for (size_t w = 0; w < n; w++) if (in[w]) basin += (w & 1) ? 1 : 5;
    u64 cons = 3ULL << W;
    printf("DENSE W %d target %llu (gate windows %llu, family states %llu) basin %llu share %.4f outside %llu sweeps %d\n", W,
           (unsigned long long)tw, (unsigned long long)tgate, (unsigned long long)tfam, (unsigned long long)basin,
           (double)basin / (double)cons, (unsigned long long)(cons - basin), sweeps - 1);
    free(in);
}

/* Real rows: every R < 2^B driven by the alternating column, to its first entry into T(62) at an odd tick. */
static void rows_mode(int B, int T, const char *late) {
    int L = (T + B) / 64 + 3;
    u64 *row = xalloc(8 * (size_t)L), *nw = xalloc(8 * (size_t)L);
    long cnt[5] = {0, 0, 0, 0, 0}, last[5] = {0, 0, 0, 0, 0};
    /* Crossings: gap histories in hex digits, newest last. X: 2525 E 2525; Y: 2222 45 2222 and 2222 4525 2222. */
    const u64 PX = 0x2525335355552525ULL;
    const u64 PY1 = 0x2222452222ULL, MY1 = 0xFFFFFFFFFFULL, PY2 = 0x222245252222ULL, MY2 = 0xFFFFFFFFFFFFULL;
    long xrows = 0, yrows = 0, xmax = 0, ymax = 0, xhist[16], yhist[16];
    u64 xbest = 0, ybest = 0;
    memset(xhist, 0, sizeof xhist); memset(yhist, 0, sizeof yhist);
    u64 lastR[5] = {0, 0, 0, 0, 0};
    FILE *f = late ? fopen(late, "w") : NULL;
    u64 M = (1ULL << 62) - 1;
    for (u64 R = 0; R < (1ULL << B); R++) {
        memset(row, 0, 8 * (size_t)L);
        row[0] = R;
        int len = 1, cls = 0, tick = -1, sinceb = -1;
        u64 hist = 0; long xc = 0, yc = 0;
        for (int t = 0; t <= T; t++) {
            if (t & 1) {
                int c = is_target(row[0] & M, 62);
                if (c) { cls = c; tick = t; break; }
                if (row[0] & 1) {
                    if (sinceb >= 0) {
                        int g = sinceb + 1 > 15 ? 15 : sinceb + 1;
                        hist = (hist << 4) | (u64)g;
                        if (hist == PX) xc++;
                        if ((hist & MY1) == PY1 || (hist & MY2) == PY2) yc++;
                    }
                    sinceb = 0;
                } else if (sinceb >= 0) sinceb++;
            }
            u64 carry = (t & 1) ? 0 : 1;
            for (int i = 0; i <= len && i < L; i++) {
                u64 a = row[i], nx = i + 1 < L ? row[i + 1] : 0;
                nw[i] = ((a << 1) | carry) ^ (a | (a >> 1) | (nx << 63));
                carry = a >> 63;
            }
            for (int i = 0; i <= len && i < L; i++) row[i] = nw[i];
            if (len < L - 1 && row[len]) len++;
        }
        cnt[cls]++;
        if (xc) { xrows++; if (xc > xmax) { xmax = xc; xbest = R; } xhist[xc > 15 ? 15 : xc]++; }
        if (yc) { yrows++; if (yc > ymax) { ymax = yc; ybest = R; } yhist[yc > 15 ? 15 : yc]++; }
        if (cls && tick > last[cls]) { last[cls] = tick; lastR[cls] = R; }
        if (!cls) printf("ROW-NOT-ENTERED R %llu by tick %d low window %llu\n", (unsigned long long)R, T, (unsigned long long)(row[0] & M));
        if (f && (tick >= 2048 || !cls)) fprintf(f, "%llu %d %d\n", (unsigned long long)R, tick, cls);
    }
    if (f) fclose(f);
    const char *nm[5] = {"none", "gate", "family", "lock7", "lock7b"};
    for (int c = 1; c < 5; c++) printf("ROWS B %d %s %ld latest tick %ld R %llu\n", B, nm[c], cnt[c], last[c], (unsigned long long)lastR[c]);
    printf("ROWS B %d none %ld by tick %d\n", B, cnt[0], T);
    printf("CROSSINGS X rows %ld most %ld at R %llu; Y rows %ld most %ld at R %llu\n", xrows, xmax, (unsigned long long)xbest, yrows, ymax, (unsigned long long)ybest);
    printf("CROSSINGS X by count:"); for (int i = 1; i < 16; i++) printf(" %ld", xhist[i]);
    printf("\nCROSSINGS Y by count:"); for (int i = 1; i < 16; i++) printf(" %ld", yhist[i]);
    printf("\n");
}

int main(int argc, char **argv) {
    const char *tf = NULL, *dir = ".", *resume = NULL, *resume_parts = NULL;
    int wmax = 22, wreport = 16, dump = 0, densew = 0, resumew = 0, prune = 0, overmax = 36, rowsB = 0, rowsT = 0;
    const char *rowsfile = NULL;
    size_t maxnodes = 120000000;
    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "--targets")) tf = argv[++i];
        else if (!strcmp(argv[i], "--mode")) MODE = !strcmp(argv[++i], "pq");
        else if (!strcmp(argv[i], "--wmax")) wmax = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--wreport")) wreport = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--out")) dir = argv[++i];
        else if (!strcmp(argv[i], "--max-nodes")) maxnodes = (size_t)atoll(argv[++i]);
        else if (!strcmp(argv[i], "--dump")) dump = 1;
        else if (!strcmp(argv[i], "--dense")) densew = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--no-lock7")) use_lock7 = 0;
        else if (!strcmp(argv[i], "--r02")) R02 = 1;
        else if (!strcmp(argv[i], "--rows")) { rowsB = atoi(argv[++i]); rowsT = atoi(argv[++i]); rowsfile = argv[++i]; }
        else if (!strcmp(argv[i], "--prune-from")) prune = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--over-max")) overmax = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--gapn")) GAPN = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--dfa-from")) DFAW = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--drop-largest-at")) DROPW = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--dfa-max")) DFAMAX = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--gap-limit")) GAPLIM = (u64)atoll(argv[++i]);
        else if (!strcmp(argv[i], "--resume")) { resumew = atoi(argv[++i]); resume = argv[++i]; }
        else if (!strcmp(argv[i], "--resume-parts")) { resumew = atoi(argv[++i]); resume_parts = argv[++i]; }
        else if (!strcmp(argv[i], "--save-at")) SAVEW = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--stop-closed")) STOPCLOSED = 1;
        else if (!strcmp(argv[i], "--export-at")) EXPORTW = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--export-ranks")) {
            const char *s = argv[++i];
            for (;;) {
                char *end; long r = strtol(s, &end, 10);
                if (end == s || r < 0 || r > 1000000 || NEXPORT == 32) return 2;
                EXPORT_RANKS[NEXPORT++] = (int)r;
                if (!*end) break;
                if (*end != ',') return 2;
                s = end + 1;
            }
        }
        else { fprintf(stderr, "unknown argument %s\n", argv[i]); return 2; }
    }
    if (!tf || wmax > 60) { fprintf(stderr, "need --targets; wmax at most 60\n"); return 2; }
    load_targets(tf);
    if (MODE) { lockset = s7; nlock = ns7; lockw = 32; } else { lockset = l7; nlock = nl7; lockw = 30; }
    printf("mode %s lock width %d wmax %d max-nodes %zu\n", MODE ? "pq" : "xx", lockw, wmax, maxnodes);
    make_gate();
    trap16 = xcalloc(1 << GW);
    for (int i = 0; i < ntrap; i++) trap16[trapc[i]] = 1;
    /* closure of the fixed locks under this mode's moves */
    {
        int bad = 0;
        for (int i = 0; i < nlock; i++) {
            u64 mv[4]; int m = moves(lockset[i], lockw, mv);
            for (int j = 0; j < m; j++) bad += !inset(lockset, nlock, mv[j]);
        }
        int bad7b = 0;
        for (int i = 0; i < nl7b; i++) {
            u64 mv[4]; int m = moves(l7b[i], 45, mv);
            for (int j = 0; j < m; j++) bad7b += !inset(l7b, nl7b, mv[j]);
        }
        printf("closure failures: lock-7 set %d, lock-7b set %d\n", bad, bad7b);
        if (bad || (!MODE && bad7b)) { fprintf(stderr, "fixed-lock control failed\n"); return 2; }
        if (!MODE) {
            int count = 0;
            for (int i = 0; i < nl7b; i++) count += is_target(l7b[i], 45) == 4;
            printf("target45 lock7b %d of %d\n", count, nl7b);
            if (count != nl7b) return 2;
        }
    }
    if (densew) { dense(densew); return 0; }
    if (rowsB) { rows_mode(rowsB, rowsT, rowsfile); return 0; }
    char jp[1024]; snprintf(jp, sizeof jp, "%s/scc_%s%s%s.jsonl", dir, MODE ? "pq" : "xx", R02 ? "_r02" : "", prune ? "_pruned" : "");
    FILE *js = fopen(jp, resume || resume_parts ? "a" : "w");
    if (!js) { perror(jp); return 2; }
    int W = GW;
    u64 *core; size_t n;
    if (resume_parts) {
        core = read_parts(resume_parts, &n); W = resumew;
    } else if (resume) {
        FILE *f = fopen(resume, "rb");
        if (!f) { perror(resume); return 2; }
        fseek(f, 0, SEEK_END); n = (size_t)ftell(f) / 8; fseek(f, 0, SEEK_SET);
        core = xalloc(8 * n);
        if (fread(core, 8, n, f) != n) return 2;
        fclose(f); W = resumew;
    } else {
        n = 0; core = xalloc(8 << GW);
        for (u64 w = 0; w < (1 << GW); w++) if (!is_target(w, GW)) core[n++] = w;
    }
    u32 *succ = NULL;
    n = peel(core, n, W, &succ);
    for (;;) {
        printf("W %d core %zu cpu %.1f rss %.0f MiB\n", W, n, cpu(), rss_mib()); fflush(stdout);
        if (W == SAVEW) {
            char prefix[1024]; snprintf(prefix, sizeof prefix, "%s/checkpoint_W%d", dir, W);
            save_parts(prefix, core, n);
        }
        if (dump) {
            char p[1024]; snprintf(p, sizeof p, "%s/core_%d_%s.bin", dir, W, MODE ? "pq" : "xx");
            FILE *f = fopen(p, "wb"); if (f) { fwrite(core, 8, n, f); fclose(f); }
        }
        if (W >= wreport) {
            u64 *keep = NULL; size_t nk = 0;
            analyse(core, n, succ, W, "CORE", js, 1, dir, (prune && W >= prune) ? &keep : NULL, &nk);
            free(succ); succ = NULL;
            projections(core, n, W);
            if (W <= overmax && !R02) over_stage(core, n, W, js, dir, dump);
            if (keep) { free(core); core = keep; n = nk; printf(" PRUNE W %d keeps %zu windows of UNRESOLVED components\n", W, n); }
            printf("W %d analysed cpu %.1f rss %.0f MiB\n", W, cpu(), rss_mib()); fflush(stdout);
        } else { free(succ); succ = NULL; }
        if (FOUND_CLOSED) { printf("STOP discovery CLOSED W %d\n", W); break; }
        if (W >= wmax) break;
        if (2 * n > maxnodes) { printf("STOP max-nodes at W %d: lift would hold %zu windows\n", W, 2 * n); break; }
        u64 *nx = xalloc(8 * 2 * n);
        size_t m = 0, removed[5] = {0, 0, 0, 0, 0};
        W++;
        for (int hi = 0; hi < 2; hi++)
            for (size_t i = 0; i < n; i++) {
                u64 w = core[i] | ((u64)hi << (W - 1));
                int t = is_target(w, W);
                if (t) removed[t]++; else nx[m++] = w;
            }
        free(core); core = nx;
        printf("lift to W %d windows %zu removed gate %zu family %zu lock7 %zu lock7b %zu\n", W, m, removed[1], removed[2], removed[3], removed[4]);
        if (m > 20000000) { m = prefilter(core, m, W); printf(" prefilter leaves %zu\n", m); }
        n = peel(core, m, W, &succ);
    }
    printf("DONE W %d core %zu cpu %.1f rss %.0f MiB\n", W, n, cpu(), rss_mib());
    if (js) fclose(js);
    return 0;
}
