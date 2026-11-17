/* T-C (Local, L1520). A(n): longest run of ones in V_n off the pair, at width n. M*(k): the longest stretch for which columns k and k+1 stay rain
   (opposite and both toggling) on a row that is not rain, at width k + 2. Maximisers are followed: least top wall during the episode.
   Usage: ./twopair_episode n0 n1 */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static int top(u64 x, int w) { u64 e = ~(x ^ (x >> 1)); e &= ((1ULL << (w - 1)) - 1); e &= ~1ULL; return e ? 63 - __builtin_clzll(e) : 0; }
int main(int argc, char **argv) { int n0 = atoi(argv[1]), n1 = atoi(argv[2]);
  for (int n = n0; n <= n1; n++) { u64 M = (1ULL << n) - 1;
    u64 q = 0x5555555555555555ULL & M, p = 0xAAAAAAAAAAAAAAABULL & M; int A = 0; u64 ax = 0;
    for (u64 x0 = 1; x0 <= M; x0 += 2) { if (x0 == p || x0 == q) continue; u64 x = x0; int r = 0;
      while ((((x >> (n - 1)) | (x >> (n - 2))) & 1)) { r++; x = (x ^ ((x << 1) | (x << 2))) & M; if (r > 100000) break; }
      if (r > A) { A = r; ax = x0; } }
    int k = n - 2; int Ms = 0; u64 mx = 0; /* width n = k + 2 */
    for (u64 x0 = 1; x0 <= M; x0 += 2) { if (x0 == p || x0 == q) continue; if ((((x0 >> k) ^ (x0 >> (k + 1))) & 1) == 0) continue;
      u64 x = x0; int r = 0;
      for (;;) { u64 y = (x ^ ((x << 1) | (x << 2))) & M; u64 c = x ^ y; if (!((c >> k) & 1) || !((c >> (k + 1)) & 1)) break; r++; x = y; if (r > 100000) break; }
      if (r > Ms) { Ms = r; mx = x0; } }
    /* follow the maximiser */
    int tmin = 99, tat = -1, lowest = 99; { u64 x = mx; for (int t = 0; t <= Ms; t++) { int d = top(x, k + 1); if (d < tmin) { tmin = d; tat = t; } x = (x ^ ((x << 1) | (x << 2))) & M; } }
    printf("n=%d A=%d A/(n-1)=%.3f | k=%d M*=%d M*/k=%.3f start=%llx least top %d at t=%d\n", n, A, (double)A / (n - 1), k, Ms, (double)Ms / k, mx, tmin, tat); fflush(stdout); }
  return 0; }
