/* L1294 T16 (Local, 2026-11-02): the pair graph from the defect, one node per orbit under rotation by two time steps
   (one step of psi = Phi o c), carrying the history's psi-period H. reports/rule30-genealogy.md section 29.3.
   Usage: ./defect_orbits P [CAP]   (P a power of two, 2..512; CAP the depth cap, default 10^7)
   State (u, v) = (c_(k-1), c_k) as P-bit time-rings, bit t = time t. d = u | v; w0 = running XOR of d with w0(0) = 0.
   s = parity of d over times [0, 2H). s = 0: two child orbits (v, w0, H), (v, NOT w0, H). s = 1, 2H < P: one child
   orbit (v, w0, 2H). s = 1, 2H = P: death. Points = 2 * sum of H (two defect phases). Edges into the rain counted. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#ifndef MW
#define MW 8
#endif
typedef uint64_t u64;
static int P, NW;
static u64 MASK[MW], A[MW], ABAR[MW];
typedef struct { u64 u[MW], v[MW]; int32_t depth, H; } node;
static void shl(const u64 *x, int s, u64 *y) {           /* y = (x << s) & MASK, s < P */
  int ws = s >> 6, bs = s & 63;
  for (int i = NW - 1; i >= 0; i--) {
    u64 r = 0;
    if (i - ws >= 0) { r = x[i - ws] << bs; if (bs && i - ws - 1 >= 0) r |= x[i - ws - 1] >> (64 - bs); }
    y[i] = r & MASK[i];
  }
}
static void integ(const u64 *d, u64 *w) {
  u64 y[MW], t[MW]; memcpy(y, d, sizeof(y));
  for (int s = 1; s < P; s <<= 1) { shl(y, s, t); for (int i = 0; i < NW; i++) y[i] ^= t[i]; }
  shl(y, 1, w);
}
static int parity_block(const u64 *d, int n) {          /* parity of bits 0..n-1 */
  int c = 0;
  for (int i = 0; i < NW && n > 0; i++, n -= 64) {
    u64 m = n >= 64 ? ~0ULL : ((1ULL << n) - 1);
    c += __builtin_popcountll(d[i] & m);
  }
  return c & 1;
}
static int eq(const u64 *x, const u64 *y) { for (int i = 0; i < NW; i++) if (x[i] != y[i]) return 0; return 1; }
int main(int argc, char **argv) {
  P = atoi(argv[1]);
  long CAP = argc > 2 ? atol(argv[2]) : 10000000L;
  if (P < 2 || P > 64 * MW || (P & (P - 1))) { fprintf(stderr, "bad P\n"); return 2; }
  NW = (P + 63) / 64;
  for (int i = 0; i < MW; i++) { MASK[i] = 0; A[i] = 0; }
  for (int t = 0; t < P; t++) { MASK[t >> 6] |= 1ULL << (t & 63); if (t & 1) A[t >> 6] |= 1ULL << (t & 63); }
  for (int i = 0; i < NW; i++) ABAR[i] = MASK[i] ^ A[i];
  size_t cap = 1 << 16, sp = 0;
  node *st = malloc(cap * sizeof(node));
  node r; memset(&r, 0, sizeof r);
  memcpy(r.u, A, sizeof A); memcpy(r.v, A, sizeof A); r.depth = 1; r.H = 1;
  st[sp++] = r;
  unsigned long long orbits = 0, into_rain = 0, splits = 0, doublings = 0, deaths = 0;
  unsigned __int128 sumH = 0;
  long longest = 0; int hitcap = 0;
  while (sp) {
    node n = st[--sp];
    orbits++; sumH += (unsigned)n.H;
    if (n.depth > longest) longest = n.depth;
    if (n.depth >= CAP) { hitcap = 1; continue; }
    u64 d[MW], w0[MW], w1[MW];
    for (int i = 0; i < NW; i++) d[i] = n.u[i] | n.v[i];
    int s = parity_block(d, 2 * n.H);
    if (s && 2 * n.H == P) { deaths++; continue; }
    integ(d, w0);
    for (int i = 0; i < NW; i++) w1[i] = w0[i] ^ MASK[i];
    int nk = s ? 1 : 2, H2 = s ? 2 * n.H : n.H;
    if (s) doublings++; else splits++;
    for (int k = 0; k < nk; k++) {
      u64 *w = k ? w1 : w0;
      if ((eq(n.v, A) && eq(w, ABAR)) || (eq(n.v, ABAR) && eq(w, A))) { into_rain++; continue; }
      if (sp + 2 >= cap) { cap *= 2; st = realloc(st, cap * sizeof(node)); if (!st) { fprintf(stderr, "oom\n"); return 3; } }
      node c; memcpy(c.u, n.v, sizeof c.u); memcpy(c.v, w, sizeof c.v); c.depth = n.depth + 1; c.H = H2;
      st[sp++] = c;
    }
    if ((orbits & ((1ULL << 30) - 1)) == 0)
      fprintf(stderr, "progress p=%d orbits=%llu longest=%ld stack=%zu\n", P, orbits, longest, sp);
  }
  unsigned __int128 pts = 2 * sumH;
  printf("p=%d orbits %llu points %llu longest %ld into_rain %llu hitcap %d splits %llu doublings %llu deaths %llu\n",
         P, orbits, (unsigned long long)pts, longest, into_rain, hitcap, splits, doublings, deaths);
  return 0;
}
