/* T-A (Local, L1520): Lemma U' and the two-pairs law on the whole p | P defect tree, one representative per orbit.
   A node is an orbit of width-n registers of least period Q | P with a defect, kept as its two top columns (u, v), P-bit rings
   with period Q, pinned at time 0. Driver d = u | v = V word. Even parity over Q: two children of period Q. Odd parity: one child,
   period 2Q (the other integral is its rotation by Q), or death if 2Q > P. Controls: sum over nodes of Q reproduces T13's path
   counts; the deepest node reproduces T13's longest path.
   Checks at every node: least period of d equals Q (within); d not all ones; rotation class of d not seen at any other node (cross).
   Usage: ./twopair_tree P */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned __int128 u128; typedef unsigned long long u64;
static int P; static u128 MASK;
static u128 rot(u128 x, int s) { s %= P; if (!s) return x; return ((x >> s) | (x << (P - s))) & MASK; }
static int parQ(u128 d, int Q) { u128 m = (Q == 128) ? ~(u128)0 : (((u128)1 << Q) - 1); u128 x = d & m;
  return (__builtin_popcountll((u64)x) + __builtin_popcountll((u64)(x >> 64))) & 1; }
static u128 integ(u128 d) { u128 y = d; for (int s = 1; s < P; s <<= 1) y ^= (y << s) & MASK; return (y << 1) & MASK; }
static int leastper(u128 d) { int q = P; while (q > 1 && !(q & 1) ? 0 : 0) {} q = P; while (q >= 2 && rot(d, q / 2) == d) q /= 2; return q; }
static u128 canon(u128 d, int q) { u128 b = d, x = d; for (int s = 1; s < q; s++) { x = rot(x, 1); if (x < b) b = x; } return b; }
typedef struct { u128 key; int depth, Q; } ent;
static ent *tab; static size_t tcap; static size_t tn;
static u64 h(u128 k) { u64 a = (u64)k * 0x9E3779B97F4A7C15ULL ^ (u64)(k >> 64) * 0xC2B2AE3D27D4EB4FULL; a ^= a >> 29; a *= 0xBF58476D1CE4E5B9ULL; return a ^ (a >> 32); }
static void grow(void);
static int ins(u128 k, int depth, int Q, int *od, int *oq) { /* returns 1 if already present */
  if (tn * 2 > tcap) grow();
  size_t i = h(k) & (tcap - 1);
  while (tab[i].Q) { if (tab[i].key == k) { *od = tab[i].depth; *oq = tab[i].Q; return 1; } i = (i + 1) & (tcap - 1); }
  tab[i] = (ent){k, depth, Q}; tn++; return 0; }
static void grow(void) { ent *o = tab; size_t oc = tcap; tcap *= 2; tab = calloc(tcap, sizeof(ent)); tn = 0;
  for (size_t i = 0; i < oc; i++) if (o[i].Q) { size_t j = h(o[i].key) & (tcap - 1); while (tab[j].Q) j = (j + 1) & (tcap - 1); tab[j] = o[i]; tn++; } free(o); }
typedef struct { u128 u, v; int depth, Q; } node;
int main(int argc, char **argv) {
  P = atoi(argv[1]); MASK = (P == 128) ? ~(u128)0 : (((u128)1 << P) - 1);
  u128 A = 0; for (int t = 1; t < P; t += 2) A |= (u128)1 << t; u128 AB = MASK ^ A;
  tcap = 1 << 20; tab = calloc(tcap, sizeof(ent));
  size_t cap = 1 << 16, sp = 0; node *st = malloc(cap * sizeof(node));
  st[sp++] = (node){A, A, 1, 2};
  u64 nodes = 0, sumQ = 0, within = 0, ones = 0, cross = 0, rain = 0; int longest = 0; u64 perQ[9] = {0}; int shown = 0;
  while (sp) {
    node n = st[--sp]; nodes++; sumQ += n.Q; if (n.depth > longest) longest = n.depth; perQ[__builtin_ctz(n.Q)]++;
    u128 d = n.u | n.v;
    int lp = leastper(d);
    if (d == MASK) { ones++; if (shown++ < 10) printf("constant driver at depth %d Q %d\n", n.depth, n.Q); }
    if (lp != n.Q) { within++; if (shown++ < 10) printf("period drop: depth %d Q %d least period of driver %d\n", n.depth, n.Q, lp); }
    int od, oq; u128 k = canon(d, lp);
    if (ins(k, n.depth, n.Q, &od, &oq)) { cross++; if (shown++ < 10) printf("repeat: depth %d Q %d and depth %d Q %d\n", n.depth, n.Q, od, oq); }
    int s = parQ(d, n.Q);
    if (s && 2 * n.Q > P) continue;
    u128 w = integ(d); int Q2 = s ? 2 * n.Q : n.Q; int m = s ? 1 : 2;
    for (int i = 0; i < m; i++) { u128 c = i ? (w ^ MASK) : w;
      if ((n.v == A && c == AB) || (n.v == AB && c == A)) { rain++; continue; }
      if (sp + 2 >= cap) { cap *= 2; st = realloc(st, cap * sizeof(node)); }
      st[sp++] = (node){n.v, c, n.depth + 1, Q2}; }
  }
  printf("P=%d orbit nodes %llu sum of Q %llu longest %d rain edges %llu | constant drivers %llu period drops %llu repeated drivers %llu\n", P, nodes, sumQ, longest, rain, ones, within, cross);
  printf("  nodes by lg Q:"); for (int i = 1; i < 9; i++) if (perQ[i]) printf(" %d:%llu", i, perQ[i]); printf("\n");
  return 0; }
