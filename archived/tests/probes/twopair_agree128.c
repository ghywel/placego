/* T-B (Local, L1520): T(n) = 1 + longest common prefix of V_n words over adjacent sorted words, off the pair. 128 ticks. Usage: ./twopair_agree128 n0 n1 */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
typedef struct { u64 hi, lo; unsigned x; } rec;
static int cmp(const void *a, const void *b) { const rec *p = a, *q = b; if (p->hi != q->hi) return p->hi < q->hi ? -1 : 1; if (p->lo != q->lo) return p->lo < q->lo ? -1 : 1; return 0; }
int main(int argc, char **argv) { int n0 = atoi(argv[1]), n1 = atoi(argv[2]);
  for (int n = n0; n <= n1; n++) { u64 M = (1ULL << n) - 1, N = 1ULL << (n - 1); rec *r = malloc(N * sizeof(rec));
    u64 q = 0x5555555555555555ULL & M, p = 0xAAAAAAAAAAAAAAABULL & M, c = 0;
    for (u64 x0 = 1; x0 <= M; x0 += 2) { if (x0 == p || x0 == q) continue; u64 x = x0, hi = 0, lo = 0;
      for (int t = 0; t < 64; t++) { hi = (hi << 1) | (((x >> (n - 1)) | (x >> (n - 2))) & 1); x = (x ^ ((x << 1) | (x << 2))) & M; }
      for (int t = 0; t < 64; t++) { lo = (lo << 1) | (((x >> (n - 1)) | (x >> (n - 2))) & 1); x = (x ^ ((x << 1) | (x << 2))) & M; }
      r[c++] = (rec){hi, lo, (unsigned)x0}; }
    qsort(r, c, sizeof(rec), cmp);
    int best = -1; u64 bi = 0; long hist[130] = {0};
    for (u64 i = 0; i + 1 < c; i++) { int l; u64 a = r[i].hi ^ r[i + 1].hi; if (a) l = __builtin_clzll(a); else { u64 b = r[i].lo ^ r[i + 1].lo; l = b ? 64 + __builtin_clzll(b) : 128; } hist[l]++; if (l > best) { best = l; bi = i; } }
    printf("n=%d T=%d model %.1f T-model %.1f pair %x %x; adjacent LCP top:", n, best + 1, 2.9526 * (n - 1), best + 1 - 2.9526 * (n - 1), r[bi].x, r[bi + 1].x);
    for (int l = best, s = 0; l >= 0 && s < 5; l--) if (hist[l]) { printf(" %d:%ld", l, hist[l]); s++; } printf("\n"); fflush(stdout); free(r); }
  return 0; }
