/* L1297 T25 (Local, 2026-11-02): the giant subtrees of the H = P/2 layer of T_P (defect_layer.c), run to completion
   with work sharing across threads and checkpoints. reports/rule30-genealogy.md section 29.13.
   Usage: ./defect_giants P THREADS ROOTFILE CKPT_OUT [CKPT_IN|-] [BUDGET]
   Roots are numbered as in defect_layer.c (phase 1, DFS order); ROOTFILE lists the ones to run. Without CKPT_IN the
   queue starts from those roots; with it, from the pending nodes and running totals saved there. On SIGTERM, or after
   BUDGET nodes in this chunk, every pending node is written to CKPT_OUT and the chunk ends; rerun with CKPT_IN to
   continue. A node of the layer splits if |u | v| is even over the whole ring and dies if odd. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <pthread.h>
#include <time.h>
#include <signal.h>
#ifndef MW
#define MW 4
#endif
#define MAXR 4096
typedef uint64_t u64;
typedef struct { u64 u[MW], v[MW]; int32_t depth, slot; } node;
typedef struct { u64 nodes, deaths, splits, rain, viol; int64_t longest; } rst;
static int P, NW, NT, R; static long rootidx[MAXR]; static u64 BUDGET;
static u64 MASK[MW], A[MW], ABAR[MW];
static void integ(const u64 *d, u64 *w) {
  u64 y[MW]; u64 carry = 0;
  for (int i = 0; i < NW; i++) {
    u64 x = d[i];
    x ^= x << 1; x ^= x << 2; x ^= x << 4; x ^= x << 8; x ^= x << 16; x ^= x << 32;
    if (carry) x = ~x;
    carry = x >> 63;
    y[i] = x;
  }
  for (int i = NW - 1; i >= 0; i--) w[i] = ((y[i] << 1) | (i ? y[i - 1] >> 63 : 0)) & MASK[i];
}
static int parity_block(const u64 *d, int n) {
  int c = 0;
  for (int i = 0; i < NW && n > 0; i++, n -= 64) c += __builtin_popcountll(d[i] & (n >= 64 ? ~0ULL : ((1ULL << n) - 1)));
  return c & 1;
}
static int eq(const u64 *x, const u64 *y) { for (int i = 0; i < NW; i++) if (x[i] != y[i]) return 0; return 1; }
static int is_rain(const u64 *u, const u64 *v) { return (eq(u, A) && eq(v, ABAR)) || (eq(u, ABAR) && eq(v, A)); }
/* global queue */
static node *gq; static size_t gq_n, gq_cap; static int busy, done;
static pthread_mutex_t mu = PTHREAD_MUTEX_INITIALIZER; static pthread_cond_t cv = PTHREAD_COND_INITIALIZER;
static void gpush(const node *n) {
  if (gq_n == gq_cap) { gq_cap = gq_cap ? 2 * gq_cap : 1024; gq = realloc(gq, gq_cap * sizeof(node)); if (!gq) { fprintf(stderr, "oom\n"); exit(3); } }
  gq[gq_n++] = *n;
}
static volatile sig_atomic_t stop_flag;
static void on_term(int sig) { (void)sig; stop_flag = 1; }
static rst (*ST)[MAXR];
static u64 work[256];
static void *worker(void *arg) {
  long id = (long)arg;
  rst *S = ST[id];
  size_t cap = 1 << 16, base = 0, top = 0;
  node *st = malloc(cap * sizeof(node));
  for (;;) {
    pthread_mutex_lock(&mu);
    while (gq_n == 0 && !done && !stop_flag) {
      if (busy == 0) { done = 1; pthread_cond_broadcast(&cv); break; }
      struct timespec ts; clock_gettime(CLOCK_REALTIME, &ts); ts.tv_nsec += 100000000; if (ts.tv_nsec >= 1000000000) { ts.tv_sec++; ts.tv_nsec -= 1000000000; }
      pthread_cond_timedwait(&cv, &mu, &ts);
    }
    if (stop_flag || (done && gq_n == 0)) { pthread_mutex_unlock(&mu); break; }
    st[0] = gq[--gq_n]; base = 0; top = 1; busy++;
    pthread_mutex_unlock(&mu);
    unsigned long long tick = 0;
    while (top > base) {
      if ((tick & 0xFFFF) == 0 && (stop_flag || (BUDGET && work[id] * (u64)NT >= BUDGET))) { stop_flag = 1; break; }
      node n = st[--top];
      tick++; work[id]++;
      rst *r = &S[n.slot];
      r->nodes++;
      if (n.depth > r->longest) r->longest = n.depth;
      u64 d[MW], w0[MW], w1[MW], e0[MW], e1[MW];
      for (int k = 0; k < NW; k++) d[k] = n.u[k] | n.v[k];
      if (parity_block(d, P)) { r->deaths++; continue; }
      r->splits++;
      integ(d, w0);
      for (int k = 0; k < NW; k++) { w1[k] = w0[k] ^ MASK[k]; e0[k] = n.v[k] | w0[k]; e1[k] = n.v[k] | w1[k]; }
      if (((parity_block(e0, P) + parity_block(e1, P)) & 1) != parity_block(n.v, P)) r->viol++;
      for (int k = 0; k < 2; k++) {
        u64 *w = k ? w1 : w0;
        if (is_rain(n.v, w)) { r->rain++; continue; }
        if (top + 2 >= cap) {
          if (base > 0) { memmove(st, st + base, (top - base) * sizeof(node)); top -= base; base = 0; }
          if (top + 2 >= cap) { cap *= 2; st = realloc(st, cap * sizeof(node)); if (!st) { fprintf(stderr, "oom\n"); exit(3); } }
        }
        node *c = &st[top++];
        memcpy(c->u, n.v, sizeof c->u); memcpy(c->v, w, sizeof c->v); c->depth = n.depth + 1; c->slot = n.slot;
      }
      if ((tick & 1023) == 0 && top - base >= 2 && gq_n < (size_t)NT) {   /* share the shallowest work */
        pthread_mutex_lock(&mu);
        while (top - base >= 2 && gq_n < (size_t)(2 * NT)) gpush(&st[base++]);
        pthread_cond_broadcast(&cv);
        pthread_mutex_unlock(&mu);
      }
    }
    pthread_mutex_lock(&mu);
    if (top > base) for (size_t i = base; i < top; i++) gpush(&st[i]);   /* stopped: hand the stack back */
    busy--;
    if (busy == 0 && gq_n == 0) done = 1;
    pthread_cond_broadcast(&cv);
    pthread_mutex_unlock(&mu);
    if (stop_flag) break;
  }
  free(st);
  return NULL;
}
static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + 1e-9 * t.tv_nsec; }
static double awake(void) { struct timespec t; clock_gettime(CLOCK_UPTIME_RAW, &t); return t.tv_sec + 1e-9 * t.tv_nsec; }
static volatile int finished;
static void *reporter(void *arg) {
  double a0 = *(double *)arg, last = a0;
  while (!finished) {
    struct timespec ts = {0, 200000000}; nanosleep(&ts, NULL);
    double t = awake();
    if (t - last >= 60) {
      last = t;
      u64 w = 0; for (int i = 0; i < NT; i++) w += work[i];
      fprintf(stderr, "progress %.0f awake s: nodes this chunk %llu, queue %zu\n", t - a0, (unsigned long long)w, gq_n);
    }
  }
  return NULL;
}
int main(int argc, char **argv) {
  if (argc < 5) { fprintf(stderr, "usage: %s P THREADS ROOTFILE CKPT_OUT [CKPT_IN|-] [BUDGET]\n", argv[0]); return 2; }
  P = atoi(argv[1]); NT = atoi(argv[2]);
  const char *ckin = argc > 5 && strcmp(argv[5], "-") ? argv[5] : NULL;
  BUDGET = argc > 6 ? strtoull(argv[6], NULL, 10) : 0;
  if (P < 4 || P > 64 * MW || (P & (P - 1)) || NT < 1 || NT > 256) { fprintf(stderr, "bad args\n"); return 2; }
  NW = (P + 63) / 64;
  for (int t = 0; t < P; t++) { MASK[t >> 6] |= 1ULL << (t & 63); if (t & 1) A[t >> 6] |= 1ULL << (t & 63); }
  for (int i = 0; i < NW; i++) ABAR[i] = MASK[i] ^ A[i];
  /* phase 1: the roots, numbered as in defect_layer.c */
  node *roots = NULL; size_t nroots = 0, rcap = 0;
  { size_t sn = 0, sc = 4096; struct { u64 u[MW], v[MW]; int32_t depth, H; } *s = malloc(sc * sizeof *s), x;
    memset(&x, 0, sizeof x); memcpy(x.u, A, sizeof A); memcpy(x.v, A, sizeof A); x.depth = 1; x.H = 1; s[sn++] = x;
    while (sn) {
      x = s[--sn];
      u64 d[MW], w0[MW], w1[MW];
      for (int k = 0; k < NW; k++) d[k] = x.u[k] | x.v[k];
      int sp = parity_block(d, 2 * x.H);
      integ(d, w0);
      for (int k = 0; k < NW; k++) w1[k] = w0[k] ^ MASK[k];
      int nk = sp ? 1 : 2, H2 = sp ? 2 * x.H : x.H;
      for (int k = 0; k < nk; k++) {
        u64 *w = k ? w1 : w0;
        if (is_rain(x.v, w)) continue;
        if (H2 == P / 2) {
          if (nroots == rcap) { rcap = rcap ? 2 * rcap : 1024; roots = realloc(roots, rcap * sizeof(node)); }
          node *c = &roots[nroots++]; memcpy(c->u, x.v, sizeof c->u); memcpy(c->v, w, sizeof c->v); c->depth = x.depth + 1; c->slot = -1;
        } else {
          if (sn + 2 >= sc) { sc *= 2; s = realloc(s, sc * sizeof *s); }
          memcpy(s[sn].u, x.v, sizeof x.u); memcpy(s[sn].v, w, sizeof x.v); s[sn].depth = x.depth + 1; s[sn].H = H2; sn++;
        }
      }
    }
    free(s);
  }
  FILE *f = fopen(argv[3], "r"); if (!f) { fprintf(stderr, "no rootfile\n"); return 2; }
  long xr; while (fscanf(f, "%ld", &xr) == 1) { if (xr < 0 || (size_t)xr >= nroots || R >= MAXR) { fprintf(stderr, "bad root %ld\n", xr); return 2; } rootidx[R++] = xr; }
  fclose(f);
  ST = calloc(NT + 1, sizeof *ST);
  rst *prev = ST[NT];                     /* totals carried in from earlier chunks */
  double prev_awake = 0; int chunk = 1;
  if (ckin) {
    FILE *g = fopen(ckin, "rb"); if (!g) { fprintf(stderr, "no checkpoint\n"); return 2; }
    char mg[8]; int p2, r2; u64 np;
    if (fread(mg, 1, 8, g) != 8 || memcmp(mg, "DGCK1\0\0\0", 8) || fread(&p2, sizeof p2, 1, g) != 1 || fread(&r2, sizeof r2, 1, g) != 1 ||
        p2 != P || r2 != R) { fprintf(stderr, "checkpoint mismatch\n"); return 2; }
    long ri[MAXR]; if (fread(ri, sizeof(long), R, g) != (size_t)R || memcmp(ri, rootidx, R * sizeof(long))) { fprintf(stderr, "root list mismatch\n"); return 2; }
    if (fread(prev, sizeof(rst), R, g) != (size_t)R || fread(&prev_awake, sizeof prev_awake, 1, g) != 1 || fread(&chunk, sizeof chunk, 1, g) != 1 ||
        fread(&np, sizeof np, 1, g) != 1) { fprintf(stderr, "bad checkpoint\n"); return 2; }
    chunk++;
    for (u64 i = 0; i < np; i++) { node n; if (fread(&n, sizeof n, 1, g) != 1) { fprintf(stderr, "short checkpoint\n"); return 2; } gpush(&n); }
    fclose(g);
    printf("p=%d chunk %d: resumed %llu pending nodes for %d roots\n", P, chunk, (unsigned long long)np, R);
  } else {
    for (int i = 0; i < R; i++) { node n = roots[rootidx[i]]; n.slot = i; gpush(&n); }
    printf("p=%d chunk 1: %d roots of %zu\n", P, R, nroots);
  }
  fflush(stdout);
  signal(SIGTERM, on_term);
  double t0 = now(), a0 = awake();
  pthread_t th[256], rep;
  pthread_create(&rep, NULL, reporter, &a0);
  for (long i = 0; i < NT; i++) pthread_create(&th[i], NULL, worker, (void *)i);
  for (int i = 0; i < NT; i++) pthread_join(th[i], NULL);
  finished = 1; pthread_join(rep, NULL);
  double el = now() - t0, ael = awake() - a0;
  rst tot[MAXR]; memset(tot, 0, sizeof tot);
  u64 cw = 0;
  for (int t = 0; t <= NT; t++) {
    if (t < NT) cw += work[t];
    for (int i = 0; i < R; i++) {
      rst *a = &ST[t][i];
      tot[i].nodes += a->nodes; tot[i].deaths += a->deaths; tot[i].splits += a->splits; tot[i].rain += a->rain; tot[i].viol += a->viol;
      if (a->longest > tot[i].longest) tot[i].longest = a->longest;
    }
  }
  fprintf(stderr, "timing: chunk %d, %.1f s wall, %.1f s awake, %llu nodes, %.3g nodes per awake second per thread\n", chunk, el, ael,
          (unsigned long long)cw, cw / ael / NT);
  rst G; memset(&G, 0, sizeof G);
  for (int i = 0; i < R; i++) {
    G.nodes += tot[i].nodes; G.deaths += tot[i].deaths; G.splits += tot[i].splits; G.rain += tot[i].rain; G.viol += tot[i].viol;
    if (tot[i].longest > G.longest) G.longest = tot[i].longest;
  }
  if (gq_n > 0) {
    FILE *g = fopen(argv[4], "wb"); if (!g) { fprintf(stderr, "cannot write checkpoint\n"); return 4; }
    double aw = prev_awake + ael; u64 np = gq_n;
    fwrite("DGCK1\0\0\0", 1, 8, g); fwrite(&P, sizeof P, 1, g); fwrite(&R, sizeof R, 1, g); fwrite(rootidx, sizeof(long), R, g);
    fwrite(tot, sizeof(rst), R, g); fwrite(&aw, sizeof aw, 1, g); fwrite(&chunk, sizeof chunk, 1, g); fwrite(&np, sizeof np, 1, g);
    size_t wr = fwrite(gq, sizeof(node), gq_n, g);
    if (fclose(g) || wr != gq_n) { fprintf(stderr, "checkpoint write failed\n"); return 4; }
    printf("CHECKPOINT after chunk %d: %llu pending nodes; running totals nodes %llu deaths %llu splits %llu longest %lld "
           "into_rain %llu two-type violations %llu; awake s %.0f\n", chunk, (unsigned long long)np, (unsigned long long)G.nodes,
           (unsigned long long)G.deaths, (unsigned long long)G.splits, (long long)G.longest, (unsigned long long)G.rain,
           (unsigned long long)G.viol, aw);
    return 0;
  }
  printf("COMPLETE after chunk %d (%.0f awake s in all): %d roots, nodes %llu deaths %llu splits %llu longest %lld into_rain %llu "
         "two-type violations %llu\n", chunk, prev_awake + ael, R, (unsigned long long)G.nodes, (unsigned long long)G.deaths,
         (unsigned long long)G.splits, (long long)G.longest, (unsigned long long)G.rain, (unsigned long long)G.viol);
  printf("per root (root, nodes, deaths, splits, longest):");
  for (int i = 0; i < R; i++) printf(" (%ld, %llu, %llu, %llu, %lld)", rootidx[i], (unsigned long long)tot[i].nodes,
                                      (unsigned long long)tot[i].deaths, (unsigned long long)tot[i].splits, (long long)tot[i].longest);
  printf("\n");
  return 0;
}
