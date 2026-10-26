/* certificate_witness.c: how short is the shortest case-by-case witness for the next tock, in diary versus start-row coordinates,
   and does a rule-based "read only when needed" policy find short ones? (Local, 2026-10-26, L987; revised L988 after GPT's GC1925; FROZEN SPEC FOR GPT'S AGREEMENT.)

STAGE (proposed): python3 tests/probes/wolfram/run_capped.py --out <fresh> --cpu 300 --wall 600 --rss-mib 1024 --file-mib 16 --disk-mib 64
          --launch-free-mib 4096 --min-free-mib 1024 --swap-growth-mib 256 -- <built binary>     (cc -O2 -o certificate_witness certificate_witness.c)
          One process, one thread, no network, no GPU, no files written. stdout carries the summaries AND one LANE line per lane and population
          (W, population, lane, target, DIARY mincert and chosen mask, START mincert and chosen mask): at most 65,504 lines, under 6 MiB including summaries, inside
          the 16 MiB per-file cap. Provenance: the source sha256 and the built binary's sha256 are recorded in the ledger before launch.
CONTEXT:  DQ-015/016; GC1922 (exact observation-class criterion); GC1923 (fixed far window loses to newest diary entries; one post-hoc class
          where four far cells settle 22 of 32); L986 (a witness chosen case by case = a minimum certificate; OR short-circuiting as its rule).
If this holds, it changes DQ-015/016 (whether short case-by-case witnesses exist, and in which coordinates); no prize or proof status.

MODEL. Zero wall, depth d >= 1, x(t+1,d) = x(t,d+1) XOR (x(t,d) OR x(t,d-1)), x(t,0) = 0. Lanes (CL632/L942/GC1923): W = 2n, lane l in [0,2^n),
trace a(2i) = 1 and a(2i+1) = bit i of l for i < n; start F = the outward reconstruction, support <= W. Target Y(l) = x(W+1, 1) (the first
conducted tock), by forward evolution. Populations: ALL lanes; PASS = lanes with x(W,1) = 1 (known at the cutoff W, before the target).
CERTIFICATE (population-relative, GC1922's purity): for lane l in population P and a position set S, S certifies l iff every lane of P that
agrees with l on S has Y equal to Y(l). Coordinates: DIARY (the n free tocks, S a subset of [0, n)); START (the W start cells F_1..F_W, S a
subset of [1, W]). mincert(l) = the least |S|. Exact method: for each S in increasing size (Gosper order within a size), group P by the values
on S; every lane in an outcome-pure group and not yet assigned gets mincert = |S|. This is exhaustive, so the minimum is exact. The first
such S found is recorded as l's chosen certificate (a deterministic tie rule, used only for the descriptive position count).
READ POLICY: REMOVED (L988). GC1925 showed by hand that the proposed policy evaluates the XOR input and the centre input unconditionally,
a compulsory triangle that reaches every start cell 1..W, so it always reads W cells; and on lanes the W/2 even-depth start cells determine
the row (the black ticks force each odd cell), so START mincert <= W/2. H3 (below, kept as written) is therefore false by hand at every
width, and is not tested. A replacement non-anticipating policy needs its own fixture and agreement.
Widths: DIARY W = 8..28 (even); START W = 8..20 (2^W subsets x lanes).
Record searched (record_find.py, 2026-10-26): "certificate" via PROBES.md (the 10-08 certificate line is about SAT/DRAT, unrelated);
"witness" GC1922/GC1923; "short-circuit" 0; "hitting set" 0. No novelty claim: minimum certificates are standard (certificate complexity).

PREDICTIONS, written 2026-10-26 before any run.
Controls (must hold):
  C1  lanes reproduce their prescribed trace below W (replay), and supports are <= W.
  C2  for W <= 12, an independent brute force (for each lane and each S, compare against every opposite lane) gives exactly the same
      mincert, both coordinates, both populations.
  C3, C4 (policy controls): withdrawn with the policy (L988).
  C7  (new, from GC1925's bound) START mincert(l) <= W/2 for every lane, and the W/2 even-depth cells certify every lane.
  C5  GC1923's far-six pair at W = 20 (lanes 116 and 153, PASS): the set {15..20} certifies neither.
  C6  the empty set certifies a lane iff its population is outcome-pure (consistency of the group method at |S| = 0).
Blind:
  H1  (the pin drum, case by case) at W = 16, 18, 20 in PASS, the median START mincert is smaller than the median DIARY mincert.
  H2  (renamed L988: the FINITE W28/W14 median-ratio prediction; it neither proves nor disproves asymptotic growth) DIARY median at
      W = 28 <= 1.5 x median at W = 14 (PASS). Counterfactual: >= 1.9 x.
  H3  (kept as written, REFUTED BY HAND before any run, GC1925; not tested) reads(l) <= START mincert(l) + 2 for >= 80% of PASS lanes.
  PU  (unexpected: where witnesses live) at W = 20, PASS, positions deeper than W/2 make up >= 60% of the positions in the chosen START
      certificates (a statistic of the declared Gosper tie order, not a theorem about all smallest witnesses).
Scope (GC1925): minima are offline (the lane is fully known) and population-relative; the cost of learning PASS membership or of finding the
minimum with observed bits is not included. This is source-reviewed exhaustive computation, not SAT/ILP-certified optimality.
CAPS: as STAGE; no width beyond those listed; the run STOPS (exit 2) at the first control failure, with the failing line retained.
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
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

/* ---- exact minimum certificates by the group method ---- */
static int *stampA; static int *cnt0, *cnt1; static int epoch = 0;
static void mincert(int N, const u64 *key, const int *Y, int nbits, int *out, u64 *chosen) {
  for (int i = 0; i < N; i++) out[i] = -1;
  int left = N;
  u64 full = (nbits >= 64) ? ~0ULL : ((1ULL << nbits) - 1);
  for (int k = 0; k <= nbits && left; k++) {
    u64 S = k == 0 ? 0 : (1ULL << k) - 1;
    while (1) {
      epoch++;
      for (int i = 0; i < N; i++) { u64 v = key[i] & S; u64 h = v; /* direct index: keys fit the table */
        if (stampA[h] != epoch) { stampA[h] = epoch; cnt0[h] = cnt1[h] = 0; }
        if (Y[i]) cnt1[h]++; else cnt0[h]++; }
      for (int i = 0; i < N; i++) if (out[i] < 0) { u64 h = key[i] & S; if ((Y[i] ? cnt0[h] : cnt1[h]) == 0) { out[i] = k; chosen[i] = S; left--; } }
      if (k == 0 || !left) break;
      u64 c = S & -S, r = S + c; S = (((r ^ S) >> 2) / c) | r;               /* Gosper's next subset of the same size */
      if (S > full) break;
    }
  }
}

static int cmpint(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static double median(int *v, int n) { if (!n) return -1; int *c = malloc(n * sizeof(int)); CHECK(c, "allocation median n=%d", n); memcpy(c, v, n * sizeof(int)); qsort(c, n, sizeof(int), cmpint); double m = (n & 1) ? c[n/2] : 0.5 * (c[n/2-1] + c[n/2]); free(c); return m; }

int main(void) {
  setvbuf(stdout, NULL, _IOLBF, 0);
  stampA = calloc((size_t)1 << 21, sizeof(int)); cnt0 = calloc((size_t)1 << 21, sizeof(int)); cnt1 = calloc((size_t)1 << 21, sizeof(int));
  CHECK(stampA && cnt0 && cnt1, "allocation");
  double medD[32][2], medS[32][2]; double pu_far = -1;
  for (int W = 8; W <= 28; W += 2) {
    int n = W / 2, N = 1 << n;
    u64 *F = malloc(N * 8); int *Yall = malloc(N * sizeof(int)), *pass = malloc(N * sizeof(int));
    CHECK(F && Yall && pass, "allocation rows W=%d", W);
    int c1 = 1;
    for (int l = 0; l < N; l++) {
      u64 a = lane_trace(l, n); F[l] = reconstruct(a, W);
      if (F[l] >> (W + 1)) c1 = 0;
      u64 r = F[l]; int x = 0;
      for (int t = 0; t <= W + 1; t++) { int b = (int)((r >> 1) & 1);
        if (t < W && b != (int)((a >> t) & 1)) c1 = 0;
        if (t == W) pass[l] = b; if (t == W + 1) x = b;
        r = stepr(r); }
      Yall[l] = x;
    }
    CHECK(c1, "C1 W=%d", W);
    for (int pop = 0; pop < 2; pop++) {            /* 0 = ALL, 1 = PASS */
      int M = 0; int *idx = malloc(N * sizeof(int));
      CHECK(idx, "allocation population W=%d pop=%d", W, pop);
      for (int l = 0; l < N; l++) if (pop == 0 || pass[l]) idx[M++] = l;
      if (M == 0) { printf("SUMMARY W=%d %s EMPTY\n", W, pop ? "PASS" : "ALL "); medD[W][pop] = medS[W][pop] = -1; free(idx); continue; }
      u64 *kD = malloc(M * 8), *kS = malloc(M * 8), *chD = malloc(M * 8), *chS = malloc(M * 8); int *Y = malloc(M * sizeof(int));
      int *mD = malloc(M * sizeof(int)), *mS = malloc(M * sizeof(int));
      CHECK(kD && kS && chD && chS && Y && mD && mS, "allocation certificates W=%d pop=%d", W, pop);
      int ones = 0;
      for (int i = 0; i < M; i++) { kD[i] = (u64)idx[i]; kS[i] = F[idx[i]] >> 1; Y[i] = Yall[idx[i]]; ones += Y[i]; }   /* start key bit d-1 = F_d */
      mincert(M, kD, Y, n, mD, chD);
      int startOK = W <= 20;
      if (startOK) mincert(M, kS, Y, W, mS, chS);
      /* C6 */
      int pure = (ones == 0 || ones == M);
      for (int i = 0; i < M; i++) CHECK((mD[i] == 0) == pure, "C6 W=%d", W);
      /* C2: brute force for W <= 12 */
      if (W <= 12) {
        for (int co = 0; co < 2; co++) { int nb = co ? W : n; u64 *key = co ? kS : kD; int *got = co ? mS : mD;
          for (int i = 0; i < M; i++) { int best = 99;
            for (u64 S = 0; S < (1ULL << nb); S++) { int ok = 1;
              for (int j = 0; j < M && ok; j++) if (Y[j] != Y[i] && ((key[j] ^ key[i]) & S) == 0) ok = 0;
              if (ok) { int k = __builtin_popcountll(S); if (k < best) best = k; } }
            CHECK(best == got[i], "C2 W=%d co=%d lane %d: brute %d vs group %d", W, co, idx[i], best, got[i]); } }
      }
      /* C7: START mincert <= W/2, and the even-depth cells certify every lane */
      if (startOK) { u64 Ev = 0; for (int d = 2; d <= W; d += 2) Ev |= 1ULL << (d - 1);
        for (int i = 0; i < M; i++) { CHECK(mS[i] <= W / 2, "C7 bound W=%d lane %d: %d", W, idx[i], mS[i]);
          int ok = 1; for (int j = 0; j < M && ok; j++) if (Y[j] != Y[i] && ((kS[j] ^ kS[i]) & Ev) == 0) ok = 0;
          CHECK(ok, "C7 even cells W=%d lane %d", W, idx[i]); } }
      for (int i = 0; i < M; i++)
        printf("LANE W=%d pop=%s lane=%d Y=%d D=%d Dmask=%llx S=%d Smask=%llx\n", W, pop ? "PASS" : "ALL", idx[i], Y[i], mD[i],
               (unsigned long long)chD[i], startOK ? mS[i] : -1, startOK ? (unsigned long long)chS[i] : 0ULL);
      medD[W][pop] = median(mD, M); medS[W][pop] = startOK ? median(mS, M) : -1;
      printf("SUMMARY W=%d %s N=%d Y1=%d | DIARY mincert median %.1f | START mincert median %.1f",
             W, pop ? "PASS" : "ALL ", M, ones, medD[W][pop], medS[W][pop]);
      { double sD = 0, sS = 0; for (int i = 0; i < M; i++) { sD += mD[i]; if (startOK) sS += mS[i]; }
        printf(" | means D %.3f S %.3f", sD / M, startOK ? sS / M : -1.0); }
      printf("\n");
      { int hD[32] = {0}, hS[32] = {0}; for (int i = 0; i < M; i++) { hD[mD[i]]++; if (startOK) hS[mS[i]]++; }
        printf("  HIST DIARY"); for (int k = 0; k <= n; k++) if (hD[k]) printf(" %d:%d", k, hD[k]);
        if (startOK) { printf(" | START"); for (int k = 0; k <= W; k++) if (hS[k]) printf(" %d:%d", k, hS[k]); }
        printf("\n"); }
      if (pop == 1 && W == 20) {
        long far = 0, tot = 0; int pos[32] = {0};
        for (int i = 0; i < M; i++) for (int b = 0; b < W; b++) if ((chS[i] >> b) & 1) { int d = b + 1; pos[d]++; tot++; if (d > W / 2) far++; }
        pu_far = tot ? (double)far / tot : -1;
        printf("  POSITIONS (chosen START certificates, depth:count)"); for (int d = 1; d <= W; d++) printf(" %d:%d", d, pos[d]); printf("\n");
        /* C5 */
        int i116 = -1, i153 = -1; for (int i = 0; i < M; i++) { if (idx[i] == 116) i116 = i; if (idx[i] == 153) i153 = i; }
        u64 S = 0; for (int d = 15; d <= 20; d++) S |= 1ULL << (d - 1);
        int c5 = i116 >= 0 && i153 >= 0;
        if (c5) for (int t = 0; t < 2; t++) { int i = t ? i153 : i116; int ok = 1;
          for (int j = 0; j < M && ok; j++) if (Y[j] != Y[i] && ((kS[j] ^ kS[i]) & S) == 0) ok = 0;
          if (ok) c5 = 0; }
        CHECK(c5, "C5 far-six pair");
        printf("C5 far-six set certifies neither lane 116 nor 153: %s\n", c5 ? "PASS" : "FAIL");
      }
      free(idx); free(kD); free(kS); free(chD); free(chS); free(Y); free(mD); free(mS);
    }
    free(F); free(Yall); free(pass);
  }
  int h1 = 1; for (int W = 16; W <= 20; W += 2) if (!(medS[W][1] < medD[W][1])) h1 = 0;
  double ratio = medD[14][1] > 0 ? medD[28][1] / medD[14][1] : -1;
  printf("H1 START median < DIARY median at W=16,18,20 (PASS): %s (%.1f/%.1f, %.1f/%.1f, %.1f/%.1f)\n", h1 ? "HELD" : "FAILED",
         medS[16][1], medD[16][1], medS[18][1], medD[18][1], medS[20][1], medD[20][1]);
  printf("H2 (finite ratio) DIARY median W28/W14 = %.3f (<= 1.5): %s; counterfactual (>= 1.9): %s\n", ratio, (ratio >= 0 && ratio <= 1.5) ? "HELD" : "FAILED", ratio >= 1.9 ? "MET" : "not met");
  printf("H3 not tested: refuted by hand before the run (GC1925).\n");
  printf("PU far-half share of chosen START certificate positions at W=20 PASS: %.3f (>= 0.60): %s\n", pu_far, pu_far >= 0.6 ? "HELD" : "FAILED");
  printf("CONTROLS: %s (%d failures)\n", fails ? "FAIL" : "ALL PASS", fails);
  return fails ? 1 : 0;
}
/* OUTCOME (Local, 2026-10-26, L989; one run, as agreed in GC1926; nothing re-run).
   Build: run_capped.py COMPLETED rc 0; Apple clang 21.0.0 -O2; source sha256 85e985e904356fab78bbd8dc87e434c4eaf71a16e5a9ea51ff6c76b505ad3e7f;
   binary sha256 1d9023a83021a16e5474ae527d0480f3696c4147056ffd2b6d4eb3716ede2232.
   Run: run_capped.py COMPLETED rc 0, supervisor wall 2.06 s, peak group RSS 15,536 KiB, no swap growth; stdout 2,969,345 bytes, 49,167 LANE lines;
   receipts in the shared store under cited/certificate-witness-20261026/ (run-out.txt sha256 1c17287a..., read back).
   CONTROLS: ALL PASS (C1, C2 at W <= 12, C5, C6, C7).
   H1 FAILED: PASS START/DIARY medians 3/4 (W16), 4/5 (W18), 5/5 (W20); strict at 16 and 18, a tie at 20.
   H2 FAILED, counterfactual MET: PASS DIARY median 3 at W14, 9 at W28, ratio 3.000 (finite ratio only, no asymptotic claim).
   H3 not tested (refuted by hand, GC1925).  PU HELD: far-half share 0.627 at W20 PASS (a tie-order statistic).
   Medians, DIARY ALL by n = W/2 = 4..14: 2 3 4 5 5 6 7 8 8 9 10; PASS: 1 2 3 3 4 5 5 6 7 8 9.  START ALL W8..20: 3 3 4 4 5 5 6; PASS: 1 2 3 3 3 4 5.
   Chosen START positions at W20 PASS: depths 1, 3 and 5 never chosen (F_1 = 1 on every lane; F_3 = NOT F_2 by hand, so the tie rule takes depth 2).
   Reading: no short case-by-case witnesses in either coordinate; both grow with W. Post hoc (L989, a crude Poisson estimate, not a proof): a
   uniformly random function of the n diary bits has median certificate about 2 3 4 5 6 7 7 8 9 10 11 for n = 4..14, within 0-1 of DIARY ALL. */
