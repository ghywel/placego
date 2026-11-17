/* L1293 (Local, 2026-11-02): enumerate every path from the defect state in the pair graph of p-periodic time-rings
   (reports/rule30-genealogy.md sections 26 and 28.3). Usage: ./eternal_dfs P   (P a power of two, 2..128).
   State (u, v) = (c_(k-1), c_k); next w = running XOR of (u | v) from w(0) in {0, 1}, defined iff popcount(u|v) even.
   No visited set: if every path is finite, no cycle is reachable. Edges into the rain {(a, abar), (abar, a)} counted.
   Output: paths (states visited), longest path in vertices, edges into rain, and whether the depth cap was hit. */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned __int128 u128;
static int P; static u128 MASK, A, ABAR;
static int par(u128 x) { return (__builtin_popcountll((unsigned long long)x) + __builtin_popcountll((unsigned long long)(x >> 64))) & 1; }
static u128 integ(u128 d) {
  u128 y = d;
  for (int s = 1; s < P; s <<= 1) y ^= (y << s) & MASK;
  return (y << 1) & MASK;
}
typedef struct { u128 u, v; int depth; } node;
int main(int argc, char **argv) {
  P = atoi(argv[1]);
  MASK = (P == 128) ? ~(u128)0 : (((u128)1 << P) - 1);
  A = 0; for (int t = 1; t < P; t += 2) A |= (u128)1 << t;
  ABAR = MASK ^ A;
  const int CAP = 100000;
  size_t cap = 1 << 20, sp = 0;
  node *st = malloc(cap * sizeof(node));
  st[sp++] = (node){A, A, 1};
  st[sp++] = (node){ABAR, ABAR, 1};
  unsigned long long paths = 0, into_rain = 0; int longest = 0, hitcap = 0;
  while (sp) {
    node n = st[--sp];
    paths++;
    if (n.depth > longest) longest = n.depth;
    if (n.depth >= CAP) { hitcap = 1; continue; }
    u128 d = n.u | n.v;
    if (par(d)) continue;
    u128 w0 = integ(d);
    u128 ws[2] = {w0, w0 ^ MASK};
    for (int i = 0; i < 2; i++) {
      u128 w = ws[i];
      if ((n.v == A && w == ABAR) || (n.v == ABAR && w == A)) { into_rain++; continue; }
      if (sp + 2 >= cap) { cap *= 2; st = realloc(st, cap * sizeof(node)); }
      st[sp++] = (node){n.v, w, n.depth + 1};
    }
    if ((paths & ((1ULL << 26) - 1)) == 0) { fprintf(stderr, "progress p=%d paths=%llu longest=%d stack=%zu\n", P, paths, longest, sp); }
  }
  /* paths counts both defect roots, as the Python probe's states do */
  printf("p=%d paths %llu longest %d into_rain %llu hitcap %d\n", P, paths, longest, into_rain, hitcap);
  return 0;
}
