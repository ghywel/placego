/* L1296 T24 (Local, 2026-11-02): the orbit tree T_P of defect_orbits_par.c, split at the H = P/2 layer.
   reports/rule30-genealogy.md section 29.12.
   Usage: ./defect_layer P THREADS ROOTCAP [ROOTFILE]
   Phase 1 (one thread) walks the copy of T_(P/2): nodes with H < P/2. Each doubling to H = P/2 is a root, numbered
   in DFS order. Phase 2 runs each root's subtree (every node has H = P/2: split if |u | v| is even, die if odd) to
   completion or to ROOTCAP nodes, on THREADS threads; with ROOTFILE only the root numbers listed there (one per line).
   Checks the two-type fact s0 + s1 = |v| (mod 2) at every split of the layer. Progress goes to stderr every 30 s;
   capped roots are printed to stdout as they occur. On SIGTERM (run_capped's cap) the workers stop, and the summary
   covers the completed roots and lists the roots to resume (L1296: a stop at the cap had lost the summary).
   Throughput uses CLOCK_UPTIME_RAW, which stops while the machine sleeps. */
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
#define DEPTHCAP 10000000L
typedef uint64_t u64;
typedef struct { u64 u[MW], v[MW]; int32_t depth, H; } node;
static int P, NW, NT; static u64 CAP;
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
/* stacks */
typedef struct { node *a; size_t n, cap; } stk;
static void spush(stk *s, const node *x) {
  if (s->n == s->cap) { s->cap = s->cap ? 2 * s->cap : 4096; s->a = realloc(s->a, s->cap * sizeof(node)); if (!s->a) { fprintf(stderr, "oom\n"); exit(3); } }
  s->a[s->n++] = *x;
}
/* phase 1 */
static node *roots; static size_t nroots, roots_cap;
static unsigned long long c_nodes, c_splits, c_doublings, c_deaths, c_rain; static long c_longest;
/* phase 2 */
static long *todo; static size_t ntodo, next_i;
static u64 *rsize; static int *rcapped; static long *rlong;
typedef struct { unsigned long long nodes, deaths, splits, rain, viol, depthhit, work; long longest; } st2;
static st2 S2[256];
static pthread_mutex_t mu = PTHREAD_MUTEX_INITIALIZER;
static volatile unsigned long long done_roots;
static volatile sig_atomic_t stop_flag;
static void on_term(int sig) { (void)sig; stop_flag = 1; }
static int *rinterrupted;
static void *worker(void *arg) {
  st2 *S = &S2[(long)arg];
  stk s = {0};
  for (;;) {
    pthread_mutex_lock(&mu);
    size_t i = (!stop_flag && next_i < ntodo) ? next_i++ : (size_t)-1;
    pthread_mutex_unlock(&mu);
    if (i == (size_t)-1) break;
    long r = todo[i];
    s.n = 0; spush(&s, &roots[r]);
    u64 cnt = 0; long lg = 0; int capped = 0;
    unsigned long long dth = 0, spl = 0, rn = 0, vl = 0, dh = 0;
    while (s.n) {
      if (cnt >= CAP) { capped = 1; break; }
      if ((cnt & 0xFFFFF) == 0 && stop_flag) break;
      node n = s.a[--s.n];
      cnt++;
      if (n.depth > lg) lg = n.depth;
      if (n.depth >= DEPTHCAP) { dh++; continue; }
      u64 d[MW], w0[MW], w1[MW], e0[MW], e1[MW];
      for (int k = 0; k < NW; k++) d[k] = n.u[k] | n.v[k];
      if (parity_block(d, P)) { dth++; continue; }
      spl++;
      integ(d, w0);
      for (int k = 0; k < NW; k++) { w1[k] = w0[k] ^ MASK[k]; e0[k] = n.v[k] | w0[k]; e1[k] = n.v[k] | w1[k]; }
      if (((parity_block(e0, P) + parity_block(e1, P)) & 1) != parity_block(n.v, P)) vl++;
      for (int k = 0; k < 2; k++) {
        u64 *w = k ? w1 : w0;
        if (is_rain(n.v, w)) { rn++; continue; }
        node c; memcpy(c.u, n.v, sizeof c.u); memcpy(c.v, w, sizeof c.v); c.depth = n.depth + 1; c.H = n.H;
        spush(&s, &c);
      }
    }
    if (s.n && !capped) { rinterrupted[r] = 1; continue; }   /* stopped mid-root: not counted */
    rsize[r] = cnt; rcapped[r] = capped; rlong[r] = lg;
    S->work += cnt;
    if (!capped) { S->nodes += cnt; S->deaths += dth; S->splits += spl; if (lg > S->longest) S->longest = lg; }
    S->rain += rn; S->viol += vl; S->depthhit += dh;
    if (capped) {
      pthread_mutex_lock(&mu);
      printf("capped root %ld after %llu nodes (deepest so far %ld)\n", r, (unsigned long long)cnt, lg);
      fflush(stdout);
      pthread_mutex_unlock(&mu);
    }
    __sync_fetch_and_add(&done_roots, 1);
  }
  free(s.a);
  return NULL;
}
static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + 1e-9 * t.tv_nsec; }
static double awake(void) { struct timespec t; clock_gettime(CLOCK_UPTIME_RAW, &t); return t.tv_sec + 1e-9 * t.tv_nsec; }
static volatile int finished;
static void *reporter(void *arg) {
  double t0 = *(double *)arg, last = t0;
  while (!finished) {
    struct timespec ts = {0, 200000000}; nanosleep(&ts, NULL);
    double t = now();
    if (t - last >= 30) {
      last = t;
      unsigned long long w = 0; for (int i = 0; i < NT; i++) w += S2[i].work;
      fprintf(stderr, "progress %.0f s: roots done %llu of %zu; nodes in finished roots %llu\n", t - t0, done_roots, ntodo, w);
    }
  }
  return NULL;
}
static int cmpu(const void *a, const void *b) { u64 x = rsize[*(const long *)a], y = rsize[*(const long *)b]; return x < y ? 1 : x > y ? -1 : 0; }
int main(int argc, char **argv) {
  if (argc < 4) { fprintf(stderr, "usage: %s P THREADS ROOTCAP [ROOTFILE]\n", argv[0]); return 2; }
  P = atoi(argv[1]); NT = atoi(argv[2]); CAP = strtoull(argv[3], NULL, 10);
  if (P < 4 || P > 64 * MW || (P & (P - 1)) || NT < 1 || NT > 256 || CAP < 1) { fprintf(stderr, "bad args\n"); return 2; }
  NW = (P + 63) / 64;
  for (int t = 0; t < P; t++) { MASK[t >> 6] |= 1ULL << (t & 63); if (t & 1) A[t >> 6] |= 1ULL << (t & 63); }
  for (int i = 0; i < NW; i++) ABAR[i] = MASK[i] ^ A[i];
  /* phase 1 */
  stk s = {0}; node r0; memset(&r0, 0, sizeof r0);
  memcpy(r0.u, A, sizeof A); memcpy(r0.v, A, sizeof A); r0.depth = 1; r0.H = 1;
  spush(&s, &r0);
  while (s.n) {
    node n = s.a[--s.n];
    c_nodes++; if (n.depth > c_longest) c_longest = n.depth;
    u64 d[MW], w0[MW], w1[MW];
    for (int k = 0; k < NW; k++) d[k] = n.u[k] | n.v[k];
    int sp = parity_block(d, 2 * n.H);
    if (sp && 2 * n.H == P) { c_deaths++; continue; }   /* cannot happen for H < P/2 */
    integ(d, w0);
    for (int k = 0; k < NW; k++) w1[k] = w0[k] ^ MASK[k];
    int nk = sp ? 1 : 2, H2 = sp ? 2 * n.H : n.H;
    if (sp) c_doublings++; else c_splits++;
    for (int k = 0; k < nk; k++) {
      u64 *w = k ? w1 : w0;
      if (is_rain(n.v, w)) { c_rain++; continue; }
      node c; memcpy(c.u, n.v, sizeof c.u); memcpy(c.v, w, sizeof c.v); c.depth = n.depth + 1; c.H = H2;
      if (H2 == P / 2) {
        if (nroots == roots_cap) { roots_cap = roots_cap ? 2 * roots_cap : 1024; roots = realloc(roots, roots_cap * sizeof(node)); }
        roots[nroots++] = c;
      } else spush(&s, &c);
    }
  }
  free(s.a);
  printf("p=%d phase 1 (copy of T_%d): nodes %llu splits %llu doublings %llu deaths %llu into_rain %llu longest %ld roots %zu\n",
         P, P / 2, c_nodes, c_splits, c_doublings, c_deaths, c_rain, c_longest, nroots);
  fflush(stdout);
  /* phase 2 */
  todo = malloc(nroots * sizeof(long));
  if (argc > 4) {
    FILE *f = fopen(argv[4], "r"); if (!f) { fprintf(stderr, "no rootfile\n"); return 2; }
    long x; while (fscanf(f, "%ld", &x) == 1) { if (x < 0 || (size_t)x >= nroots) { fprintf(stderr, "bad root %ld\n", x); return 2; } todo[ntodo++] = x; }
    fclose(f);
  } else for (size_t i = 0; i < nroots; i++) todo[ntodo++] = (long)i;
  rsize = calloc(nroots, sizeof(u64)); rcapped = calloc(nroots, sizeof(int)); rlong = calloc(nroots, sizeof(long));
  rinterrupted = calloc(nroots, sizeof(int));
  signal(SIGTERM, on_term);
  double t0 = now(), a0 = awake();
  pthread_t th[256], rep;
  pthread_create(&rep, NULL, reporter, &t0);
  for (long i = 0; i < NT; i++) pthread_create(&th[i], NULL, worker, (void *)i);
  for (int i = 0; i < NT; i++) pthread_join(th[i], NULL);
  finished = 1; pthread_join(rep, NULL);
  double el = now() - t0, ael = awake() - a0;
  size_t nrun = next_i;   /* roots dispatched */
  if (stop_flag) {
    size_t ni = 0; for (size_t i = 0; i < nrun; i++) ni += rinterrupted[todo[i]];
    printf("STOPPED by SIGTERM: %zu of %zu roots dispatched, %zu interrupted (not counted); to resume, run the interrupted roots and roots",
           nrun, ntodo, ni);
    for (size_t i = 0; i < nrun; i++) if (rinterrupted[todo[i]]) printf(" %ld", todo[i]);
    printf(" and every listed root from position %zu on\n", nrun);
    size_t k = 0; for (size_t i = 0; i < nrun; i++) if (!rinterrupted[todo[i]]) todo[k++] = todo[i];
    ntodo = k;
  }
  st2 T; memset(&T, 0, sizeof T);
  for (int i = 0; i < NT; i++) {
    T.nodes += S2[i].nodes; T.deaths += S2[i].deaths; T.splits += S2[i].splits; T.rain += S2[i].rain; T.viol += S2[i].viol;
    T.depthhit += S2[i].depthhit; T.work += S2[i].work; if (S2[i].longest > T.longest) T.longest = S2[i].longest;
  }
  size_t ncap = 0; for (size_t i = 0; i < ntodo; i++) ncap += rcapped[todo[i]];
  printf("p=%d phase 2: roots run %zu, cap %llu nodes per root: completed %zu, capped %zu\n", P, ntodo, (unsigned long long)CAP, ntodo - ncap, ncap);
  printf("completed roots: nodes %llu deaths %llu splits %llu longest (absolute depth) %ld\n", T.nodes, T.deaths, T.splits, T.longest);
  printf("all roots: into_rain %llu depth-cap hits %llu two-type violations %llu\n", T.rain, T.depthhit, T.viol);
  if (ntodo == nroots && ncap == 0)
    printf("T_%d complete: orbits %llu (copy %llu + layer %llu)\n", P, c_nodes + T.nodes, c_nodes, T.nodes);
  printf("tail: k, roots with N >= 2^k, C_k = share * 2^(k/2)\n");
  for (int k = 0; k < 64 && (1ULL << k) <= CAP; k++) {
    size_t c = 0; for (size_t i = 0; i < ntodo; i++) if (rsize[todo[i]] >= (1ULL << k)) c++;
    if (c == 0) break;
    printf("  %2d %zu %.3f\n", k, c, (double)c / ntodo * __builtin_sqrt((double)(1ULL << k)));
  }
  long *ord = malloc(ntodo * sizeof(long)); memcpy(ord, todo, ntodo * sizeof(long));
  qsort(ord, ntodo, sizeof(long), cmpu);
  printf("largest subtrees (root, nodes, capped, deepest):");
  for (size_t i = 0; i < ntodo && i < 12; i++) printf(" (%ld, %llu, %d, %ld)", ord[i], (unsigned long long)rsize[ord[i]], rcapped[ord[i]], rlong[ord[i]]);
  printf("\n");
  fprintf(stderr, "timing: phase 2 %.1f s wall, %.1f s awake, %llu nodes, %.3g nodes per awake second per thread\n", el, ael, T.work,
          T.work / ael / NT);
  return 0;
}
