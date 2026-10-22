/* e711_sweep.c: exact f(n,m) for every m in [m0, m0+count) by a sliding-window incremental bipartite matching.
   f(n,m) = least H such that (m, m+H) holds distinct a_1..a_n with k | a_k.
   Window [lo,hi] = [m+1, m+H-1]; end(m) = m+f(n,m)-1 is non-decreasing in m, so a two-pointer sweep is exact.
   usage: e711_sweep n m0 count [time_limit_s] [print_each(0/1)] */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#define BUF 16384
#define MASK (BUF-1)
#define NONE (-1)
static int n;
static int64_t matchL[65];
static int matchR[BUF];
static uint64_t divm[BUF];
static int64_t lo, hi;
static int visL[65]; static int stampL = 0;
static int visR[BUF]; static int stampR = 0;
static int64_t res[65];
static int tryR(int64_t x) {
  uint64_t mm = divm[x & MASK];
  while (mm) {
    int b = __builtin_ctzll(mm); mm &= mm - 1;
    int k = b + 1;
    if (visL[k] == stampL) continue;
    visL[k] = stampL;
    if (matchL[k] == NONE || tryR(matchL[k])) { matchL[k] = x; matchR[x & MASK] = k; return 1; }
  }
  return 0;
}
static int tryL(int k) {
  int64_t x = ((lo + k - 1) / k) * k;
  for (; x <= hi; x += k) {
    int idx = (int)(x & MASK);
    if (visR[idx] == stampR) continue;
    visR[idx] = stampR;
    if (matchR[idx] == NONE || tryL(matchR[idx])) { matchR[idx] = k; matchL[k] = x; return 1; }
  }
  return 0;
}
int main(int argc, char **argv) {
  if (argc < 4) { fprintf(stderr, "usage\n"); return 1; }
  n = atoi(argv[1]);
  int64_t m0 = atoll(argv[2]), count = atoll(argv[3]);
  double tlimit = argc > 4 ? atof(argv[4]) : 540.0;
  int pe = argc > 5 ? atoi(argv[5]) : 0;
  if (n < 1 || n > 64 || m0 < 0) return 1;
  clock_t t0 = clock();
  for (int k = 0; k <= 64; k++) matchL[k] = NONE;
  for (int i = 0; i < BUF; i++) { matchR[i] = NONE; visR[i] = 0; divm[i] = 0; }
  lo = m0 + 1; hi = m0; int size = 0;
  for (int k = 1; k <= n; k++) res[k] = (m0 + 1) % k;
  static int64_t hist[BUF]; int64_t best = -1, bestm = -1, nbest = 0;
  int64_t firstbest[20]; int64_t m;
  for (m = m0; m < m0 + count; m++) {
    if (m > m0) {
      int idx = (int)(m & MASK);
      int k = matchR[idx];
      matchR[idx] = NONE; divm[idx] = 0;
      lo = m + 1;
      if (k != NONE) { matchL[k] = NONE; size--; stampR++; if (tryL(k)) size++; }
    }
    while (size < n) {
      hi++;
      if (hi - lo + 1 >= BUF - 1) { fprintf(stderr, "window overflow\n"); return 2; }
      int idx = (int)(hi & MASK);
      uint64_t dm = 0;
      for (int k = 1; k <= n; k++) { if (res[k] == 0) dm |= 1ULL << (k - 1); if (++res[k] == k) res[k] = 0; }
      divm[idx] = dm; matchR[idx] = NONE;
      stampL++;
      if (tryR(hi)) size++;
    }
    int64_t f = hi - m + 1;
    hist[f]++;
    if (pe) printf("m %lld f %lld\n", (long long)m, (long long)f);
    if (f > best) { best = f; bestm = m; nbest = 0; }
    if (f == best) { if (nbest < 20) firstbest[nbest] = m; nbest++; }
    if (((m - m0) & 0xFFFFF) == 0 && (double)(clock() - t0) / CLOCKS_PER_SEC > tlimit) { m++; break; }
  }
  if (m > m0 + count) m = m0 + count;
  double el = (double)(clock() - t0) / CLOCKS_PER_SEC;
  printf("n %d m0 %lld swept %lld time %.1f best %lld count_best %lld first_best_m", n, (long long)m0,
         (long long)(m - m0), el, (long long)best, (long long)nbest);
  for (int i = 0; i < nbest && i < 20; i++) printf(" %lld", (long long)firstbest[i]);
  printf("\nhist");
  for (int f = 0; f < BUF; f++) if (hist[f]) printf(" %d:%lld", f, (long long)hist[f]);
  printf("\n");
  return 0;
}
