/* certificate_conditional.c: with the oldest three diary entries fixed, are the next tock's witnesses in the remaining entries still shorter
   than a balanced coin-flip table's? (Local, 2026-10-26, L993, after GC1928; FROZEN SPEC FOR GPT'S LAUNCH REVIEW; nothing built or run.)

STAGE (proposed): build  run_capped.py --out <fresh>/build --cpu 30 --wall 60 --rss-mib 512 --file-mib 16 --disk-mib 64 --launch-free-mib 4096
          --min-free-mib 1024 --swap-growth-mib 256 -- /usr/bin/cc -O2 -Wall -Wextra -o <fresh>/build/certificate_conditional certificate_conditional.c
          run    run_capped.py --out <fresh>/run --cpu 300 --wall 600 --rss-mib 1024 --file-mib 16 --disk-mib 64 --launch-free-mib 4096
          --min-free-mib 1024 --swap-growth-mib 256 -- <fresh>/build/certificate_conditional
          Sequential, one process, one thread, no network, no GPU, no files written. stdout: one CSHUF line per (W, class, permutation), one CLASS
          and one REAL line per class, the summaries: about 1,600 lines, under 250 KiB. CAPPED_TEST_* unset; warnings retained in the build receipt.
CONTEXT:  L991 (Rule 30's ALL diary witnesses are shorter than all 64 sampled shuffles at W16..28); L992 (the influence deficit sits in the
          oldest three entries; I_j = (1 - mu_j) q_j); GC1928 (equal influence vectors do not determine mean certificate size: A = z XOR Maj XOR Maj
          versus B = z XOR AND XOR AND XOR AND, means 5 and 19/4; Local carried this by hand in L993). So the influence picture cannot close the line;
          this stage asks the certificate question directly, inside each class of the oldest three entries.
If this holds, it changes DQ-015/016: whether the witness shortcut over chance survives once the forgotten entries are fixed. No prize or proof status.

MODEL. As certificate_witness.c: zero wall, lanes W = 2n, trace a(2i) = 1, a(2i+1) = bit i of l, start = outward reconstruction, target
Y = x(W+1,1). Population ALL only (GC1928: the influence argument was for ALL; no PASS widening). Widths W = 24, 26, 28.
CLASSES. p in [0,8): the lanes with (l & 7) == p, i.e. the oldest three free tocks fixed. Within a class the coordinates are the remaining
n - 3 diary bits (key = l >> 3). C_p(l) = the exact minimum certificate of l within its class, by the same increasing-cardinality group method.
C(l) = the exact minimum certificate in the full cube (all n bits, all 2^n lanes), as before.
NULL. Within each class, 64 count-preserving label permutations (Fisher-Yates with modulo-bias rejection, splitmix64; seed from (W, p, s) and a
tag distinct from certificate_shuffle.c's). Statistic: the integer sum of C_p over the class. Rank r = number of permutation sums strictly
below Rule 30's sum + half the number equal. A sampled comparison, not the exact null distribution.
PURE CLASSES (frozen before any run): a class whose Y is constant has every C_p = 0 and every permutation identical; it is reported as PURE,
excluded from both the match count and the counterfactual count (it counts as neither), and listed separately.
Record searched (record_find.py, 2026-10-26): "conditional certificate" 6 hits (SAT/backward-certificate transfers GC549, GC1193, GC1853 and
GC1928's own design; none a subcube-conditional minimum of this kind); "fixed prefix" 37 (prefix-tree and lexicon work; none for certificates).
No novelty claim: conditional certificate complexity on subcubes is standard.

PREDICTIONS, written 2026-10-26 before any run.
Controls (must hold; the run STOPS, exit 2, at the first failure, with the failing line retained):
  K1  replay (C1): lanes reproduce their trace below W; supports <= W.
  K2  identity: full-cube mean C reproduces certificate_witness.c's recorded ALL means 8.291, 9.171, 9.960 at W24, 26, 28 to 3 decimals.
  K3  accounting (GC1928): C_p(l) <= C(l) <= 3 + C_p(l) for every lane.
  K4  every permutation keeps the class size and its count of 1s.
  K5  determinism: permutation 0 of each class recomputed from its seed gives the same labels and the same sum.
  K6  brute force: at W = 24, for classes 0 and 7, Rule 30's labels and permutation 0, an independent brute force over all subsets of the 9
      coordinates gives exactly the group method's C_p, lane by lane.
Blind (GC1928's thresholds, as proposed in L991):
  M   (match: the shortcut is the forgotten entries) at each W = 24, 26, 28, rank r in [2, 62] in >= 6 of the 8 classes.
  CF  (counterfactual: residual structure) rank r <= 1 in >= 5 of the 8 classes at >= 2 of the 3 widths.
      Neither M nor CF is a mixed outcome, reported as such.
  PU  (unexpected: what the forgotten entries cost a full witness) at W = 28 the mean slack C(l) - C_p(l) over all lanes is < 1.5.
      Counterfactual: >= 2.0.
Scope (GC1928): a match says this conditional mean-size statistic shows no residual separation from these sampled permutations; it does not
prove that forgetting is the whole mechanism. A residual gap asks for a mechanism; it certifies no survival statement. Conditional
certificates exclude the cost of learning the three fixed bits.
CAPS: as STAGE; no width or population beyond those listed; no second run. Estimated work: at W28 each class has 2,048 lanes and 2^11 subsets,
at most about 8.4 million group updates per certificate computation, 8 x 65 of them; the 600 s wall is the stop.
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

/* ---- exact minimum certificates by the group method (as certificate_shuffle.c) ---- */
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
static u64 sumv(const int *v, int n) { u64 s = 0; for (int i = 0; i < n; i++) s += (u64)v[i]; return s; }
static int brute(int M, const u64 *key, const int *Y, int nbits, int i) {
  int best = 99;
  for (u64 S = 0; S < (1ULL << nbits); S++) { int ok = 1;
    for (int j = 0; j < M && ok; j++) if (Y[j] != Y[i] && ((key[j] ^ key[i]) & S) == 0) ok = 0;
    if (ok) { int k = __builtin_popcountll(S); if (k < best) best = k; } }
  return best;
}

static u64 sm_state;
static u64 splitmix(void) { u64 z = (sm_state += 0x9E3779B97F4A7C15ULL); z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL; z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL; return z ^ (z >> 31); }
static u64 perm_seed(int W, int p, int s) { return ((u64)W << 40) ^ ((u64)p << 32) ^ (u64)s ^ 0xC0DD17105EEDULL; }
static u64 bounded(u64 b) { u64 x, threshold = (0ULL - b) % b; do { x = splitmix(); } while (x < threshold); return x % b; }
static void permute(int *Y, int M, int W, int p, int s) {
  sm_state = perm_seed(W, p, s);
  for (int i = M - 1; i > 0; i--) { int j = (int)bounded((u64)(i + 1)); int t = Y[i]; Y[i] = Y[j]; Y[j] = t; }
}

#define K 64
int main(void) {
  setvbuf(stdout, NULL, _IOLBF, 0);
  stampA = calloc((size_t)1 << 21, sizeof(int)); cnt0 = calloc((size_t)1 << 21, sizeof(int)); cnt1 = calloc((size_t)1 << 21, sizeof(int));
  CHECK(stampA && cnt0 && cnt1, "allocation");
  const double rec[3] = { 8.291, 9.171, 9.960 };
  int inM[3] = {0}, lowCF[3] = {0}, pure[3] = {0}; double pu_slack = -1;
  for (int wi = 0; wi < 3; wi++) {
    int W = 24 + 2 * wi, n = W / 2, N = 1 << n, nc = n - 3, MC = N >> 3;
    int *Yall = malloc(N * sizeof(int)), *Cfull = malloc(N * sizeof(int)); u64 *kfull = malloc(N * 8);
    CHECK(Yall && Cfull && kfull, "allocation rows W=%d", W);
    int c1 = 1;
    for (int l = 0; l < N; l++) {
      u64 a = lane_trace(l, n), F = reconstruct(a, W);
      if (F >> (W + 1)) c1 = 0;
      u64 r = F; int x = 0;
      for (int t = 0; t <= W + 1; t++) { int b = (int)((r >> 1) & 1);
        if (t < W && b != (int)((a >> t) & 1)) c1 = 0;
        if (t == W + 1) x = b;
        r = stepr(r); }
      Yall[l] = x; kfull[l] = (u64)l;
    }
    CHECK(c1, "K1 (C1) W=%d", W);
    mincert(N, kfull, Yall, n, Cfull);
    double fm = (double)sumv(Cfull, N) / N;
    CHECK(fabs(fm - rec[wi]) < 0.0005, "K2 W=%d: %.4f vs recorded %.3f", W, fm, rec[wi]);
    printf("FULL W=%d ALL N=%d sum=%llu mean %.4f\n", W, N, (unsigned long long)sumv(Cfull, N), fm);
    u64 slack = 0;
    for (int p = 0; p < 8; p++) {
      u64 *key = malloc(MC * 8); int *idx = malloc(MC * sizeof(int)), *Y0 = malloc(MC * sizeof(int)), *Y = malloc(MC * sizeof(int)),
          *Yc = malloc(MC * sizeof(int)), *m = malloc(MC * sizeof(int)), *m2 = malloc(MC * sizeof(int));
      CHECK(key && idx && Y0 && Y && Yc && m && m2, "allocation class W=%d p=%d", W, p);
      int M = 0, ones = 0;
      for (int l = 0; l < N; l++) if ((l & 7) == p) { idx[M] = l; key[M] = (u64)(l >> 3); Y0[M] = Yall[l]; ones += Y0[M]; M++; }
      CHECK(M == MC, "class size W=%d p=%d", W, p);
      mincert(M, key, Y0, nc, m);
      u64 real_sum = sumv(m, M);
      for (int i = 0; i < M; i++) {                                                                  /* K3 */
        int cf = Cfull[idx[i]];
        CHECK(m[i] <= cf && cf <= 3 + m[i], "K3 W=%d lane %d: C_p %d C %d", W, idx[i], m[i], cf);
        slack += (u64)(cf - m[i]); }
      if (W == 24 && (p == 0 || p == 7)) for (int i = 0; i < M; i++)                                  /* K6, Rule 30 labels */
        CHECK(brute(M, key, Y0, nc, i) == m[i], "K6 W=%d p=%d lane %d (Rule 30)", W, p, idx[i]);
      int isPure = (ones == 0 || ones == M);
      printf("REAL W=%d p=%d N=%d Y1=%d sum=%llu mean %.4f%s\n", W, p, M, ones, (unsigned long long)real_sum, (double)real_sum / M, isPure ? " PURE" : "");
      if (isPure) { pure[wi]++; printf("CLASS W=%d p=%d PURE (excluded from M and CF counts)\n", W, p);
        free(key); free(idx); free(Y0); free(Y); free(Yc); free(m); free(m2); continue; }
      double below = 0; u64 lo = ~0ULL, hi = 0, tot = 0;
      for (int s = 0; s < K; s++) {
        memcpy(Y, Y0, M * sizeof(int)); permute(Y, M, W, p, s);
        int o = 0; for (int i = 0; i < M; i++) o += Y[i];
        CHECK(o == ones, "K4 W=%d p=%d permutation %d", W, p, s);
        mincert(M, key, Y, nc, m); u64 ps = sumv(m, M);
        if (s == 0) {
          memcpy(Yc, Y0, M * sizeof(int)); permute(Yc, M, W, p, 0);                                    /* K5 */
          CHECK(memcmp(Yc, Y, M * sizeof(int)) == 0, "K5 labels W=%d p=%d", W, p);
          mincert(M, key, Yc, nc, m2); CHECK(sumv(m2, M) == ps, "K5 sum W=%d p=%d", W, p);
          if (W == 24 && (p == 0 || p == 7)) for (int i = 0; i < M; i++)                              /* K6, permutation 0 */
            CHECK(brute(M, key, Y, nc, i) == m[i], "K6 W=%d p=%d lane %d (permutation 0)", W, p, idx[i]);
        }
        if (ps < real_sum) below += 1; else if (ps == real_sum) below += 0.5;
        if (ps < lo) lo = ps; if (ps > hi) hi = ps; tot += ps;
        printf("CSHUF W=%d p=%d s=%d N=%d Y1=%d seed=%llx sum=%llu\n", W, p, s, M, o, (unsigned long long)perm_seed(W, p, s), (unsigned long long)ps);
      }
      if (below >= 2 && below <= 62) inM[wi]++;
      if (below <= 1) lowCF[wi]++;
      printf("CLASS W=%d p=%d N=%d Y1=%d | Rule30 sum %llu | permutations mean %.2f min %llu max %llu | rank %.1f of %d\n", W, p, M, ones,
             (unsigned long long)real_sum, (double)tot / K, (unsigned long long)lo, (unsigned long long)hi, below, K);
      free(key); free(idx); free(Y0); free(Y); free(Yc); free(m); free(m2);
    }
    double ms = (double)slack / N;
    printf("SLACK W=%d mean C - C_p %.4f (sum %llu)\n", W, ms, (unsigned long long)slack);
    if (W == 28) pu_slack = ms;
    printf("SUMMARY W=%d in-range %d of 8 | rank<=1 %d of 8 | pure %d\n", W, inM[wi], lowCF[wi], pure[wi]);
    free(Yall); free(Cfull); free(kfull);
  }
  int mHeld = 1, cfW = 0;
  for (int wi = 0; wi < 3; wi++) { if (inM[wi] < 6) mHeld = 0; if (lowCF[wi] >= 5) cfW++; }
  printf("M (in-range >= 6 of 8 at each of W24, 26, 28): %s (%d, %d, %d)\n", mHeld ? "HELD" : "FAILED", inM[0], inM[1], inM[2]);
  printf("CF (rank<=1 in >= 5 of 8 at >= 2 widths): %s (%d, %d, %d)\n", cfW >= 2 ? "MET" : "not met", lowCF[0], lowCF[1], lowCF[2]);
  if (!mHeld && cfW < 2) printf("MIXED OUTCOME: neither M nor CF\n");
  printf("PU mean slack C - C_p at W=28: %.4f (< 1.5): %s; counterfactual (>= 2.0): %s\n", pu_slack, pu_slack < 1.5 ? "HELD" : "FAILED", pu_slack >= 2.0 ? "MET" : "not met");
  printf("CONTROLS: %s (%d failures)\n", fails ? "FAIL" : "ALL PASS", fails);
  return fails ? 1 : 0;
}
