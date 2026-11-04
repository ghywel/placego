/* Backward top-window game (Local, L1521). A node is a window of w bits ending at the top wall pair, rain above. A move: the adversary names the two output
   bits below the window; one backward tick follows. Prints the robust set B (every move gives top + 3 and stays in B), then the set A of windows from which the
   adversary can avoid B for ever, its strongly connected components, and for each the extreme mean drift of the top. Usage: ./game w */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned u32; typedef unsigned long long u64;
static int w; static u32 N; static u32 *S; static signed char *Dl; /* S[4*i+s], Dl[4*i+s] */
static void build(void) { N = 1u << (w - 1); S = malloc(sizeof(u32) * 4 * (size_t)N); Dl = malloc(4 * (size_t)N);
  for (u32 m = 0; m < N; m++) { /* window bits 0..w-1 low..high, top pair = bits w-2, w-1 equal; index m holds bits 0..w-2 */
    int in[96]; for (int i = 0; i < w - 1; i++) in[i] = (m >> i) & 1; in[w - 1] = in[w - 2]; int L = w; { int b = in[w - 1]; for (int i = 0; i < 24; i++) { b ^= 1; in[L++] = b; } }
    for (int s = 0; s < 4; s++) { int p1 = s & 1, p2 = s >> 1; int e[100]; e[0] = p2; e[1] = p1; int a = p1, c = p2; for (int i = 0; i < L; i++) { int o = in[i] ^ (a | c); e[i + 2] = o; c = a; a = o; }
      int k = L + 2 - 2; while (k >= 0 && e[k] != e[k + 1]) k--; /* top pair at e[k], e[k+1] */
      int delta = k - 2 - (w - 2); int lo = k + 2 - w; if (lo < 0) { fprintf(stderr, "window underflow\n"); exit(1); }
      u32 nm = 0; for (int i = 0; i < w - 1; i++) nm |= (u32)e[lo + i] << i; S[4 * (size_t)m + s] = nm; Dl[4 * (size_t)m + s] = delta; } } }
int main(int c, char **v) { w = atoi(v[1]); build();
  unsigned char *inB = malloc(N); memset(inB, 1, N); int ch = 1, rounds = 0; while (ch) { ch = 0; rounds++; for (u32 i = 0; i < N; i++) if (inB[i]) for (int s = 0; s < 4; s++) if (Dl[4 * (size_t)i + s] != 3 || !inB[S[4 * (size_t)i + s]]) { inB[i] = 0; ch = 1; break; } }
  u32 nb = 0; for (u32 i = 0; i < N; i++) nb += inB[i];
  unsigned char *A = malloc(N); for (u32 i = 0; i < N; i++) A[i] = !inB[i]; ch = 1; while (ch) { ch = 0; for (u32 i = 0; i < N; i++) if (A[i]) { int ok = 0; for (int s = 0; s < 4; s++) if (A[S[4 * (size_t)i + s]]) ok = 1; if (!ok) { A[i] = 0; ch = 1; } } }
  u32 na = 0; for (u32 i = 0; i < N; i++) na += A[i];
  /* also trim backward: keep nodes on a bi-infinite A path */
  unsigned char *C = malloc(N); memcpy(C, A, N); ch = 1; unsigned char *hp = malloc(N); while (ch) { ch = 0; memset(hp, 0, N); for (u32 i = 0; i < N; i++) if (C[i]) for (int s = 0; s < 4; s++) { u32 j = S[4 * (size_t)i + s]; if (C[j]) hp[j] = 1; } for (u32 i = 0; i < N; i++) if (C[i]) { int ok = 0; for (int s = 0; s < 4; s++) if (C[S[4 * (size_t)i + s]]) ok = 1; if (!ok || !hp[i]) { C[i] = 0; ch = 1; } } }
  u32 nc = 0; for (u32 i = 0; i < N; i++) nc += C[i];
  /* Tarjan on C */
  int *idx = malloc(sizeof(int) * N), *low = malloc(sizeof(int) * N), *comp = malloc(sizeof(int) * N); memset(idx, -1, sizeof(int) * N); memset(comp, -1, sizeof(int) * N); u32 *stk = malloc(sizeof(u32) * N), *cs = malloc(sizeof(u32) * N); unsigned char *ci = malloc(N), *on = calloc(N, 1); int counter = 0, ncomp = 0; u32 sp = 0;
  for (u32 r = 0; r < N; r++) if (C[r] && idx[r] < 0) { u32 cp = 0; cs[cp] = r; ci[r] = 0; idx[r] = low[r] = counter++; stk[sp++] = r; on[r] = 1; cp = 1;
      while (cp) { u32 x = cs[cp - 1]; if (ci[x] < 4) { int s = ci[x]++; u32 y = S[4 * (size_t)x + s]; if (!C[y]) continue; if (idx[y] < 0) { idx[y] = low[y] = counter++; stk[sp++] = y; on[y] = 1; ci[y] = 0; cs[cp++] = y; } else if (on[y]) { if (idx[y] < low[x]) low[x] = idx[y]; } }
        else { cp--; if (cp) { u32 p = cs[cp - 1]; if (low[x] < low[p]) low[p] = low[x]; } if (low[x] == idx[x]) { for (;;) { u32 y = stk[--sp]; on[y] = 0; comp[y] = ncomp; if (y == x) break; } ncomp++; } } } }
  int *sz = calloc(ncomp + 1, sizeof(int)); for (u32 i = 0; i < N; i++) if (C[i]) sz[comp[i]]++;
  int nontriv = 0; for (u32 i = 0; i < N; i++) if (C[i]) { int self = 0; for (int s = 0; s < 4; s++) { u32 j = S[4 * (size_t)i + s]; if (j == i) self = 1; } if (sz[comp[i]] == 1 && self) sz[comp[i]] = -1; }
  for (int k = 0; k < ncomp; k++) if (sz[k] > 1 || sz[k] == -1) nontriv++;
  printf("w=%d windows %u |B|=%u (%u rounds) |A|=%u core %u SCCs %d nontrivial %d\n", w, N, nb, rounds, na, nc, ncomp, nontriv);
  /* per nontrivial SCC: size and extreme drift by value iteration on the SCC (min and max mean over T steps) */
  for (int k = 0; k < ncomp; k++) if (sz[k] > 1 || sz[k] == -1) { int size = 0; u32 *nodes = malloc(sizeof(u32) * N); for (u32 i = 0; i < N; i++) if (C[i] && comp[i] == k) nodes[size++] = i; int T = 400; int *v0 = calloc(N, sizeof(int)), *v1 = calloc(N, sizeof(int)), *u0 = calloc(N, sizeof(int)), *u1 = calloc(N, sizeof(int));
      for (int t = 0; t < T; t++) { for (int a = 0; a < size; a++) { u32 i = nodes[a]; int mx = -1000000, mn = 1000000; for (int s = 0; s < 4; s++) { u32 j = S[4 * (size_t)i + s]; if (C[j] && comp[j] == k) { int d = Dl[4 * (size_t)i + s]; if (v0[j] + d > mx) mx = v0[j] + d; if (u0[j] + d < mn) mn = u0[j] + d; } } v1[i] = mx; u1[i] = mn; } int *q = v0; v0 = v1; v1 = q; q = u0; u0 = u1; u1 = q; }
      int mx = -1000000, mn = 1000000; for (int a = 0; a < size; a++) { u32 i = nodes[a]; if (v0[i] > mx) mx = v0[i]; if (u0[i] < mn) mn = u0[i]; }
      if (nontriv <= 40 || size > 200) { printf("  SCC size %d mean drift in [%.3f, %.3f]", size, (double)mn / T, (double)mx / T); if (size <= 6) { printf(" e.g."); for (int a = 0; a < size && a < 2; a++) { printf(" "); for (int b = 0; b < w - 1; b++) putchar((nodes[a] >> b) & 1 ? '#' : '.'); } } printf("\n"); }
      free(nodes); free(v0); free(v1); free(u0); free(u1); }
  return 0; }
