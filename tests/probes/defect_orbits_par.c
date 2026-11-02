/* L1294 T16 (Local, 2026-11-02): multithreaded form of defect_orbits.c (same graph, same counts), with word-wise
   integration and work sharing. reports/rule30-genealogy.md section 29.3.
   Usage: ./defect_orbits_par P THREADS [CAP]   (P a power of two, 2..64*MW; CAP default 10^7)
   Node (u, v, H): d = u | v; s = parity of d over [0, 2H); s = 0 -> children (v, w0, H), (v, NOT w0, H);
   s = 1, 2H < P -> child (v, w0, 2H); s = 1, 2H = P -> death. w0 = running XOR of d, w0(0) = 0. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <pthread.h>
#ifndef MW
#define MW 4
#endif
typedef uint64_t u64;
static int P, NW; static long CAP;
static u64 MASK[MW], A[MW], ABAR[MW];
typedef struct { u64 u[MW], v[MW]; int32_t depth, H; } node;
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
/* global work queue */
static node *gq; static size_t gq_n, gq_cap; static int busy, done, NT;
static pthread_mutex_t mu = PTHREAD_MUTEX_INITIALIZER; static pthread_cond_t cv = PTHREAD_COND_INITIALIZER;
typedef struct { unsigned long long orbits, into_rain, splits, doublings, deaths; unsigned __int128 sumH; long longest; int hitcap; } stats;
static stats ST[256];
static void gpush(const node *n) {
  if (gq_n == gq_cap) { gq_cap = gq_cap ? 2 * gq_cap : 1024; gq = realloc(gq, gq_cap * sizeof(node)); }
  gq[gq_n++] = *n;
}
static void *worker(void *arg) {
  stats *S = &ST[(long)arg];
  size_t cap = 1 << 16, base = 0, top = 0;
  node *st = malloc(cap * sizeof(node));
  for (;;) {
    pthread_mutex_lock(&mu);
    while (gq_n == 0 && !done) {
      if (busy == 0) { done = 1; pthread_cond_broadcast(&cv); break; }
      pthread_cond_wait(&cv, &mu);
    }
    if (done && gq_n == 0) { pthread_mutex_unlock(&mu); break; }
    st[0] = gq[--gq_n]; base = 0; top = 1; busy++;
    pthread_mutex_unlock(&mu);
    unsigned long long tick = 0;
    while (top > base) {
      node n = st[--top];
      S->orbits++; S->sumH += (unsigned)n.H;
      if (n.depth > S->longest) S->longest = n.depth;
      if (n.depth >= CAP) { S->hitcap = 1; continue; }
      u64 d[MW], w0[MW], w1[MW];
      for (int i = 0; i < NW; i++) d[i] = n.u[i] | n.v[i];
      int s = parity_block(d, 2 * n.H);
      if (s && 2 * n.H == P) { S->deaths++; continue; }
      integ(d, w0);
      for (int i = 0; i < NW; i++) w1[i] = w0[i] ^ MASK[i];
      int nk = s ? 1 : 2, H2 = s ? 2 * n.H : n.H;
      if (s) S->doublings++; else S->splits++;
      for (int k = 0; k < nk; k++) {
        u64 *w = k ? w1 : w0;
        if ((eq(n.v, A) && eq(w, ABAR)) || (eq(n.v, ABAR) && eq(w, A))) { S->into_rain++; continue; }
        if (top + 2 >= cap) {
          if (base > 0) { memmove(st, st + base, (top - base) * sizeof(node)); top -= base; base = 0; }
          if (top + 2 >= cap) { cap *= 2; st = realloc(st, cap * sizeof(node)); if (!st) { fprintf(stderr, "oom\n"); exit(3); } }
        }
        node *c = &st[top++];
        memcpy(c->u, n.v, sizeof c->u); memcpy(c->v, w, sizeof c->v); c->depth = n.depth + 1; c->H = H2;
      }
      if ((++tick & 1023) == 0 && top - base >= 2 && gq_n < (size_t)NT) {   /* share the shallowest work */
        pthread_mutex_lock(&mu);
        while (top - base >= 2 && gq_n < (size_t)(2 * NT)) gpush(&st[base++]);
        pthread_cond_broadcast(&cv);
        pthread_mutex_unlock(&mu);
      }
    }
    pthread_mutex_lock(&mu);
    busy--;
    if (busy == 0 && gq_n == 0) { done = 1; pthread_cond_broadcast(&cv); }
    pthread_mutex_unlock(&mu);
  }
  free(st);
  return NULL;
}
int main(int argc, char **argv) {
  P = atoi(argv[1]); NT = atoi(argv[2]); CAP = argc > 3 ? atol(argv[3]) : 10000000L;
  if (P < 2 || P > 64 * MW || (P & (P - 1)) || NT < 1 || NT > 256) { fprintf(stderr, "bad args\n"); return 2; }
  NW = (P + 63) / 64;
  for (int t = 0; t < P; t++) { MASK[t >> 6] |= 1ULL << (t & 63); if (t & 1) A[t >> 6] |= 1ULL << (t & 63); }
  for (int i = 0; i < NW; i++) ABAR[i] = MASK[i] ^ A[i];
  node r; memset(&r, 0, sizeof r);
  memcpy(r.u, A, sizeof A); memcpy(r.v, A, sizeof A); r.depth = 1; r.H = 1;
  gpush(&r);
  pthread_t th[256];
  for (long i = 0; i < NT; i++) pthread_create(&th[i], NULL, worker, (void *)i);
  for (int i = 0; i < NT; i++) pthread_join(th[i], NULL);
  stats T; memset(&T, 0, sizeof T);
  for (int i = 0; i < NT; i++) {
    T.orbits += ST[i].orbits; T.into_rain += ST[i].into_rain; T.splits += ST[i].splits; T.doublings += ST[i].doublings;
    T.deaths += ST[i].deaths; T.sumH += ST[i].sumH; if (ST[i].longest > T.longest) T.longest = ST[i].longest; T.hitcap |= ST[i].hitcap;
  }
  unsigned __int128 pts = 2 * T.sumH;
  printf("p=%d threads %d orbits %llu points %llu%s longest %ld into_rain %llu hitcap %d splits %llu doublings %llu deaths %llu\n",
         P, NT, T.orbits, (unsigned long long)pts, (pts >> 64) ? " (overflow)" : "", T.longest, T.into_rain, T.hitcap,
         T.splits, T.doublings, T.deaths);
  return 0;
}
