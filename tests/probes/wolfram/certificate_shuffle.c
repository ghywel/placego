/* certificate_shuffle.c: are the next tock's case-by-case witnesses in diary coordinates any shorter than a coin-flip table's with the
   same balance? (Local, 2026-10-26, L989; FROZEN SPEC FOR GPT'S AGREEMENT; nothing run.)

STAGE (proposed): python3 tests/probes/wolfram/run_capped.py --out <fresh> --cpu 300 --wall 600 --rss-mib 1024 --file-mib 16 --disk-mib 64
          --launch-free-mib 4096 --min-free-mib 1024 --swap-growth-mib 256 -- <built binary>     (cc -O2 -o certificate_shuffle certificate_shuffle.c)
          Build separately under CPU 30 / wall 60 / RSS 512, as GC1926. One process, one thread, no network, no GPU, no files written.
          stdout: one SHUF line per (W, population, shuffle) and the summaries, about 1,500 lines, under 200 KiB.
CONTEXT:  certificate_witness.c OUTCOME (L989): DIARY minimum certificates grow with W (PASS median 3 at W14, 9 at W28), and a crude
          Poisson estimate for a uniformly random function of the n diary bits lands within 0-1 of the observed medians. The estimate is
          not exact and ignores balance; this stage replaces it with an exact null on the same lanes.
If this holds, it changes DQ-015/016: whether a case-by-case witness for the next tock finds any shortcut a balanced coin-flip table lacks.
No prize or proof status.

MODEL. As certificate_witness.c (same lanes, start rows, target Y = x(W+1,1), populations ALL and PASS = lanes with x(W,1) = 1, the same
exact increasing-cardinality group method). DIARY coordinates only: the key is the lane index itself (bit i = free tock i).
NULL. For each W = 8..28 and population P, K = 64 shuffles: Y is permuted uniformly within P (Fisher-Yates, splitmix64 seeded by
(W, population, shuffle)), which keeps the population, the coordinates and the count of 1s, and destroys which lanes share an outcome.
Statistic: the mean DIARY mincert over P (real-valued; integer medians are too coarse to rank).
Rank r = the number of the 64 shuffle means strictly below the Rule 30 mean, plus half the number equal (ties split).
Record searched (record_find.py, 2026-10-26): "shuffle" 63 hits (balance and kick-gap shuffle nulls; none for certificates);
"shuffle certificate" 2 (unrelated); "null" 234 (the next-bit iid null of GPU-METAL-JOBS J.3; none for certificates); "random function" 1 (CDP 186, unrelated).
No novelty claim: the certificate complexity of random Boolean functions is standard.

PREDICTIONS, written 2026-10-26 before any run.
Controls (must hold; the run STOPS, exit 2, at the first failure):
  X1  identity: the Rule 30 mean DIARY mincert reproduces certificate_witness.c's recorded means to 3 decimals at W = 20..28, both
      populations (ALL 6.763 7.618 8.291 9.171 9.960; PASS 5.504 6.314 6.907 7.853 8.647).
  X2  every shuffle keeps the population size and the count of 1s.
  X3  for W <= 12, an independent brute force gives exactly the group method's mincert on shuffle 0 of each population.
  X4  determinism: shuffle 0 recomputed from its seed gives the same permutation and the same mean.
  X5  C1 as before (lanes replay their trace below W; supports <= W).
Blind:
  R1  (the coin-flip table, ALL) at each W = 20, 22, 24, 26, 28 the Rule 30 rank r lies in [2, 62]; holds at >= 4 of the 5 widths.
      Counterfactual (a structured shortcut): r <= 1 at >= 3 of the 5 widths.
  R2  (the same, PASS) as R1 for PASS.
  PU  (unexpected: does the newest entry matter? GC1923's card counting) at W = 28, ALL, the Rule 30 mean mincert of lanes whose newest
      free tock is 1 differs from that of lanes whose newest free tock is 0 by at least 0.3 (either sign).
Scope: offline, population-relative minima as before; a match with the null says the witness sizes look like chance at these widths, not that
the tock is random, and a gap says some sharing exists, not where.
CAPS: as STAGE; no width beyond 28; no second run.
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef uint64_t u64;

static int fails = 0;
#define CHECK(c, ...) do { if (!(c)) { fails++; printf("CONTROL FAIL: " __VA_ARGS__); printf("\nSTOPPED at first control failure\n"); fflush(stdout); exit(2); } } while (0)

static u64 stepr(u64 r) { return ((r >> 1) ^ (r | (r << 1))) & ~1ULL; }        /* bit d = depth d; bit 0 = wall, kept 0 */
static u64 reconstruct(u64 a, int T) {                                          /* start row bits 1..T from trace bits a(0..T-1) */
  u64 cm1 = 0, c = a, row = (c & 1) << 1;
  for (int d = 1; d < T; d++) { u64 nx = (c >> 1) ^ (c | cm1); cm1 = c; c = nx; row |= (c & 1ULL) << (d + 1); }
  return row;
}
static u64 lane_trace(u64 l, int n) { u64 a = 0; for (int i = 0; i < n; i++) { a |= 1ULL << (2*i); a |= ((l >> i) & 1ULL) << (2*i+1); } return a; }

/* ---- exact minimum certificates by the group method (as certificate_witness.c, without the chosen mask) ---- */
static int *stampA; static int *cnt0, *cnt1; static int epoch = 0;
static void mincert(int N, const u64 *key, const int *Y, int nbits, int *out) {
  for (int i = 0; i < N; i++) out[i] = -1;
  int left = N;
  u64 full = (1ULL << nbits) - 1;
  for (int k = 0; k <= nbits && left; k++) {
    u64 S = k == 0 ? 0 : (1ULL << k) - 1;
    while (1) {
      epoch++;
      for (int i = 0; i < N; i++) { u64 h = key[i] & S;
        if (stampA[h] != epoch) { stampA[h] = epoch; cnt0[h] = cnt1[h] = 0; }
        if (Y[i]) cnt1[h]++; else cnt0[h]++; }
      for (int i = 0; i < N; i++) if (out[i] < 0) { u64 h = key[i] & S; if ((Y[i] ? cnt0[h] : cnt1[h]) == 0) { out[i] = k; left--; } }
      if (k == 0 || !left) break;
      u64 c = S & -S, r = S + c; S = (((r ^ S) >> 2) / c) | r;               /* Gosper's next subset of the same size */
      if (S > full) break;
    }
  }
}
static double meanv(const int *v, int n) { double s = 0; for (int i = 0; i < n; i++) s += v[i]; return s / n; }

static u64 sm_state;
static u64 splitmix(void) { u64 z = (sm_state += 0x9E3779B97F4A7C15ULL); z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL; z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL; return z ^ (z >> 31); }
static void shuffle(int *Y, int M, int W, int pop, int s) {
  sm_state = ((u64)W << 40) ^ ((u64)pop << 32) ^ (u64)s ^ 0x5EEDC0DEULL;
  for (int i = M - 1; i > 0; i--) { int j = (int)(splitmix() % (u64)(i + 1)); int t = Y[i]; Y[i] = Y[j]; Y[j] = t; }
}

#define K 64
int main(void) {
  setvbuf(stdout, NULL, _IOLBF, 0);
  stampA = calloc((size_t)1 << 21, sizeof(int)); cnt0 = calloc((size_t)1 << 21, sizeof(int)); cnt1 = calloc((size_t)1 << 21, sizeof(int));
  CHECK(stampA && cnt0 && cnt1, "allocation");
  const double rec[2][5] = { {6.763, 7.618, 8.291, 9.171, 9.960}, {5.504, 6.314, 6.907, 7.853, 8.647} };
  double rank[32][2]; double pu_diff = 0;
  for (int W = 8; W <= 28; W += 2) {
    int n = W / 2, N = 1 << n;
    int *Yall = malloc(N * sizeof(int)), *pass = malloc(N * sizeof(int));
    CHECK(Yall && pass, "allocation rows W=%d", W);
    int c1 = 1;
    for (int l = 0; l < N; l++) {
      u64 a = lane_trace(l, n), F = reconstruct(a, W);
      if (F >> (W + 1)) c1 = 0;
      u64 r = F; int x = 0;
      for (int t = 0; t <= W + 1; t++) { int b = (int)((r >> 1) & 1);
        if (t < W && b != (int)((a >> t) & 1)) c1 = 0;
        if (t == W) pass[l] = b; if (t == W + 1) x = b;
        r = stepr(r); }
      Yall[l] = x;
    }
    CHECK(c1, "X5 (C1) W=%d", W);
    for (int pop = 0; pop < 2; pop++) {            /* 0 = ALL, 1 = PASS */
      int M = 0; int *idx = malloc(N * sizeof(int));
      CHECK(idx, "allocation population W=%d pop=%d", W, pop);
      for (int l = 0; l < N; l++) if (pop == 0 || pass[l]) idx[M++] = l;
      CHECK(M > 0, "empty population W=%d pop=%d", W, pop);
      u64 *key = malloc(M * 8); int *Y0 = malloc(M * sizeof(int)), *Y = malloc(M * sizeof(int)), *Yc = malloc(M * sizeof(int)), *m = malloc(M * sizeof(int));
      CHECK(key && Y0 && Y && Yc && m, "allocation certificates W=%d pop=%d", W, pop);
      int ones = 0;
      for (int i = 0; i < M; i++) { key[i] = (u64)idx[i]; Y0[i] = Yall[idx[i]]; ones += Y0[i]; }
      mincert(M, key, Y0, n, m);
      double r30 = meanv(m, M);
      if (W >= 20) CHECK(fabs(r30 - rec[pop][(W - 20) / 2]) < 0.0005, "X1 W=%d pop=%d: %.4f vs recorded %.3f", W, pop, r30, rec[pop][(W - 20) / 2]);
      if (pop == 0 && W == 28) { double s1 = 0, s0 = 0; int n1 = 0, n0 = 0;
        for (int i = 0; i < M; i++) { if ((idx[i] >> (n - 1)) & 1) { s1 += m[i]; n1++; } else { s0 += m[i]; n0++; } }
        pu_diff = s1 / n1 - s0 / n0;
        printf("NEWEST W=28 ALL newest tock 1: n=%d mean %.3f | newest tock 0: n=%d mean %.3f | diff %.3f\n", n1, s1 / n1, n0, s0 / n0, pu_diff); }
      double sm[K]; double below = 0;
      for (int s = 0; s < K; s++) {
        memcpy(Y, Y0, M * sizeof(int)); shuffle(Y, M, W, pop, s);
        int o = 0; for (int i = 0; i < M; i++) o += Y[i];
        CHECK(o == ones, "X2 W=%d pop=%d shuffle %d", W, pop, s);
        mincert(M, key, Y, n, m); sm[s] = meanv(m, M);
        if (s == 0) {
          memcpy(Yc, Y0, M * sizeof(int)); shuffle(Yc, M, W, pop, 0);         /* X4 */
          CHECK(memcmp(Yc, Y, M * sizeof(int)) == 0, "X4 permutation W=%d pop=%d", W, pop);
          int *m2 = malloc(M * sizeof(int)); CHECK(m2, "allocation X4"); mincert(M, key, Yc, n, m2);
          CHECK(fabs(meanv(m2, M) - sm[0]) < 1e-12, "X4 mean W=%d pop=%d", W, pop); free(m2);
          if (W <= 12) for (int i = 0; i < M; i++) { int best = 99;                                    /* X3 */
            for (u64 S = 0; S < (1ULL << n); S++) { int ok = 1;
              for (int j = 0; j < M && ok; j++) if (Y[j] != Y[i] && ((key[j] ^ key[i]) & S) == 0) ok = 0;
              if (ok) { int k = __builtin_popcountll(S); if (k < best) best = k; } }
            CHECK(best == m[i], "X3 W=%d pop=%d lane %d: brute %d vs group %d", W, pop, idx[i], best, m[i]); }
        }
        if (sm[s] < r30) below += 1; else if (sm[s] == r30) below += 0.5;
        printf("SHUF W=%d %s s=%d mean %.4f\n", W, pop ? "PASS" : "ALL", s, sm[s]);
      }
      double lo = sm[0], hi = sm[0], tot = 0; for (int s = 0; s < K; s++) { if (sm[s] < lo) lo = sm[s]; if (sm[s] > hi) hi = sm[s]; tot += sm[s]; }
      rank[W][pop] = below;
      printf("SUMMARY W=%d %s N=%d Y1=%d | Rule30 mean %.4f | shuffles mean %.4f min %.4f max %.4f | rank %.1f of %d\n",
             W, pop ? "PASS" : "ALL ", M, ones, r30, tot / K, lo, hi, below, K);
      free(idx); free(key); free(Y0); free(Y); free(Yc); free(m);
    }
    free(Yall); free(pass);
  }
  for (int pop = 0; pop < 2; pop++) {
    int in = 0, low = 0;
    for (int W = 20; W <= 28; W += 2) { if (rank[W][pop] >= 2 && rank[W][pop] <= 62) in++; if (rank[W][pop] <= 1) low++; }
    printf("R%d (%s) rank in [2,62] at %d of 5 widths (>= 4): %s; counterfactual rank <= 1 at %d of 5 (>= 3): %s\n", pop + 1,
           pop ? "PASS" : "ALL", in, in >= 4 ? "HELD" : "FAILED", low, low >= 3 ? "MET" : "not met");
  }
  printf("PU newest-tock mean difference at W=28 ALL: %.3f (|diff| >= 0.3): %s\n", pu_diff, fabs(pu_diff) >= 0.3 ? "HELD" : "FAILED");
  printf("CONTROLS: %s (%d failures)\n", fails ? "FAIL" : "ALL PASS", fails);
  return fails ? 1 : 0;
}
