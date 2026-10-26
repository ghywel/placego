/* tock_twins.c: do the free tocks of a zero-wall start get forgotten, and by what rule? (Local, 2026-10-26, L955)

RUN-ON:   cpu, one process, one thread (cc -O2 -o tock_twins tock_twins.c -lm; ./tock_twins > out.txt)
COST:     under a minute on the M5, under 300 MB; caps below.
CONTEXT:  the owner, 2026-10-26: "I am relaxing the no compute requirement now, feel free to use the M5 in such a way as to
          reveal useful structure about the lines of enquiry". DEEP-QUESTIONS.md DQ-001, DQ-004, DQ-009, DQ-012, DQ-013; GPT's
          GC1891 (joint checks) and GC1892 (a replacement may forget tocks); Local's L954 (the conductor k_m, the checks c_m).
If this holds, it changes: DQ-001 and DQ-009 (what a start may forget and what the referee must remember) and the mechanism
          question under the all-width D(W) row; it is structure, not a bound, and changes no prize or proof status.

MODEL (the DEEP-QUESTIONS auxiliary, not the full-line prize system). Depth d >= 1, x(t,0) = 0,
  x(t+1,d) = x(t,d+1) XOR (x(t,d) OR x(t,d-1)); the test: x(2i,1) = 1 for every i.
Lanes (CL632/L942's convention): width W = 2n, lane l in [0, 2^n) has trace a(2i) = 1, a(2i+1) = b_i = bit i of l for
i < n; its start F_1..F_W is the outward reconstruction x(t,d+1) = x(t+1,d) XOR (x(t,d) OR x(t,d-1)), zeros beyond W.
Death D(l) = the first even t with x(t,1) = 0. A b_j-twin pair is (l, l XOR 2^j). Two lanes MERGE at tick k if their rows at
time 2k are identical and both passed every tick before 2k; from then on they are one history (L954 Proposition 2).

THE QUESTION. L942 measured that flipping the first free tock changes the death in 1% of pairs at W = 40 (pair correlation
0.83, 0.88, 0.92, 0.95, 0.975, 0.985 at W = 20..40), and the last in two of three. Three readings of "which tocks are
forgotten": by LAG from the end of the free chapter (lambda = n - 1 - j; a fading memory), by POSITION j (only the first
few, as rule30_influence.py found in lead 1, RULE30-PRIZE.md 8.38), or by FRACTION j/n. The rising first-bit correlation
suggests lag; 8.38 suggests position. PT2 decides it.

Record searched (record_find.py, runs made 2026-10-26): "merge" 540 hits/133 files; "twin" 157/59; "funnel" 11/6;
"preimage" 226/78; "ancestor" 195/55; "influence lag" 0; "fading memory" 0; "twin merge" 0; "conductor" 37/13;
"first free bit" 4/4; "footprint" 26/17. Read: RULE30-PRIZE.md 8.37-8.38 (lead-1 merges, 6% per step, influence 0.63-0.69
from time 12); rule30_wall.py and rule30_influence.py headers; L942 (the first/last-bit table above); GC1891, GC1892.
The zero-wall twin-merge profile, its lag dependence and the footprint are not in the record that these searches reach.

PREDICTIONS, written 2026-10-26 before this file's first run (no exploratory run).
Controls (must hold; any failure is an instrument failure and stops the reading):
  C1  replay: each lane's simulated trace equals its construction at t < W; no lane is censored (all D <= 4W).
  C2  the 2^n start rows are pairwise distinct (the lane bijection).
  C3  merged pairs have equal deaths; b_(n-1)-twins never merge (F_W differs, so the supports differ forever).
  C4  a b_j-twin pair is never identical before tick j+1 (rows at tick k are determined by the tocks from k on).
  C5  universal tables equal L954's hand formulas: k_0 = k_1 = 1, k_2 = XNOR(b0,b1), k_3 = XNOR(b1,b2) XOR (b0 AND NOT b1),
      c_0 = c_1 = b0, c_2 = b2 OR (NOT b0 AND b1); and GC1891's k_4(0,0,0,1) = 1.
  C6  counterfactual: with XOR in place of the OR, no two lanes ever share a row (W = 8..24, ticks 1..2W).
  C7  for b_j-twins, j <= 3: identical at tick j+1 iff their traces agree on [W, W+4j+3] (a finite window, Prop. 2).
  C8  a lane with a two-step passing ancestor P: P is the width-(W-2) lane it names, and that lane's death is D + 2;
      every reducible lane (its merge class at some tick holds a lane with an ancestor) has D <= maxD(W-2) - 2.
  C9  the start with an extra black cell at the death tick T has the same trace before T-1 and a different one at T-1.
  C10 GC1889: d_i = x(2i+1,3) XOR x(2i+1,5) equals b_(i+2) XOR (b_i OR b_(i+1)) whenever the ticks through 2i+6 pass.
  C11 L942 at W = 40: 5,228 b_0-pairs and 349,146 b_19-pairs change the death; D(47284) = 66, D(180) = 40, D(47104) = 42.
  C12 merged b_j-twins' starts agree at every depth below 2j+2 (the cells there depend on a(0..2j) only).
Blind:
  PT1 (the packaging, DQ-001): at W = 40, b_0-twins merge in a fraction mu in [0.975, 0.990] of pairs, and at least 95% of
      those merges happen at tick 1 (a four-bit window).
  PT2 (decisive, DQ-009): mu_W(j) depends on the lag lambda = n-1-j, not on j or j/n. For each lambda in 2..9 with
      j >= 2, over W in {24, 28, 32, 36, 40}, the spread max - min of mu is <= 0.04. Contrast: at fixed j = 2 the spread
      over the same widths is >= 0.10; at j = n/2 it is >= 0.10. Within a width mu rises with lambda (dips <= 0.02 allowed);
      mu(1) <= 0.5; mu(9) >= 0.75; (1 - mu) falls between lambda = 3 and 9 by a ratio per unit lag in [0.65, 0.90].
      Counterfactual (position): if the spread at fixed j <= 0.04 and at fixed lambda >= 0.10, the memory is positional.
  PT3 (footprint, GC1886's caveat): at W = 40, merged b_j-twins (j = 2..12) differ only in [2j+2, 2j+2+E]; the median E is
      <= 10 at each j and the medians span <= 4 across j. Unmerged pairs: median E >= W - 2j - 6 (they reach the edge).
  PT4 (the funnel, DQ-004): at tick n, N_W distinct rows and H_W bits of entropy (lanes as weights). The count keeps growing:
      (log2 N_40 - log2 N_24)/8 in [0.60, 0.95] per free tock; the entropy does not: H_40 - H_24 <= 5 bits.
      Counterfactual (no concentration): H_40 - H_24 >= 7.
  PT5 (GC1891): of deaths at T >= W+2, the fraction "decided" (the other tock fails too) is in [0.3, 0.7] at each
      W = 24..40; universally, P(c_m ignores b_m) is in [0.3, 0.7] at m = 20..24.
  PT6 (shortening, the handoff's second shape): lanes with a two-step passing ancestor: a fraction in [0.08, 0.20] at
      W = 24..40; reducible by death: [0.2, 0.8].
  PT7 (the referee's memory, DQ-009): universal influence Inf_j(k_m) over uniform prefixes, lag l = m-1-j: l = 0 gives
      >= 0.75 for every m >= 2; at m = 24 every l >= 12 gives <= 0.05; stationarity: for m, m' in 16..24, j, j' >= 4 and
      equal l <= 11, |Inf - Inf'| <= 0.03. Counterfactual (no fading): Inf >= 0.25 at every l <= 20 at m = 24.
  PU  (the unexpected check, DQ-013, the uneven metronome): along the 64 longest-lived lanes at W = 40 the gaps between
      GPT's discrepancies (in tocks) have mean in [1.6, 2.6], and successive gaps have |Spearman| <= 0.15, within 0.10 of a
      within-lane shuffle (fixed seed).
CAPS: widths 8..40 (even); time to 4W+4; m <= 24; one process; ulimit -t 900; RSS checked by time -l after the run.
REFUTED-BY: any control failing (stop); each blind prediction stands or falls on its stated numbers.
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

#define NW 4                 /* row words: depths 0..255 */
#define TW 3                 /* trace words: times 0..191 */
#define WMIN 8
#define WMAX 40
#define MMAX 24
typedef uint64_t u64;

static int RULE_XOR = 0;
static int fails = 0;
#define CHECK(cond, ...) do { if (!(cond)) { fails++; printf("CONTROL FAIL: " __VA_ARGS__); printf("\n"); } } while (0)

static inline int gb(const u64 *r, int d) { return (int)((r[d >> 6] >> (d & 63)) & 1); }
static inline void sb(u64 *r, int d) { r[d >> 6] |= 1ULL << (d & 63); }
static inline int req(const u64 *a, const u64 *b) { for (int i = 0; i < NW; i++) if (a[i] != b[i]) return 0; return 1; }
static int support(const u64 *r) { for (int i = NW - 1; i >= 0; i--) if (r[i]) return i * 64 + 63 - __builtin_clzll(r[i]); return 0; }

static void step(const u64 *w, u64 *o) {
  u64 r[NW], l[NW];
  for (int i = 0; i < NW; i++) {
    r[i] = (w[i] >> 1) | (i + 1 < NW ? (w[i + 1] << 63) : 0);
    l[i] = (w[i] << 1) | (i > 0 ? (w[i - 1] >> 63) : 0);
  }
  for (int i = 0; i < NW; i++) o[i] = RULE_XOR ? (r[i] ^ w[i] ^ l[i]) : (r[i] ^ (w[i] | l[i]));
  o[0] &= ~1ULL;
}

/* outward reconstruction from trace bits a(0..T-1), T <= 63: row bit d = F_d, d = 1..T */
static void reconstruct(u64 a, int T, u64 *row) {
  u64 cm1 = 0, c = a;
  memset(row, 0, NW * 8);
  if (c & 1) sb(row, 1);
  for (int d = 1; d < T; d++) {
    u64 nx = RULE_XOR ? ((c >> 1) ^ c ^ cm1) : ((c >> 1) ^ (c | cm1));
    cm1 = c; c = nx;
    if (c & 1) sb(row, d + 1);
  }
}
static int recon_last(u64 a, int T) {        /* F_T only */
  u64 cm1 = 0, c = a;
  for (int d = 1; d < T; d++) { u64 nx = (c >> 1) ^ (c | cm1); cm1 = c; c = nx; }
  return (int)(c & 1);
}
static u64 lane_trace(u64 l, int n) { u64 a = 0; for (int i = 0; i < n; i++) { a |= 1ULL << (2 * i); a |= ((l >> i) & 1ULL) << (2 * i + 1); } return a; }

/* one backward step: Q with forward(Q) = R, finite, support(R)-1; returns 1 if valid */
static int back1(const u64 *R, int x1, u64 *Q) {
  int r = support(R);
  memset(Q, 0, NW * 8);
  if (r < 1) return 0;
  int qm1 = 0, qc = x1;
  if (x1) sb(Q, 1);
  for (int j = 1; j <= r; j++) { int nx = gb(R, j) ^ (qc | qm1); qm1 = qc; qc = nx; if (nx) { if (j + 1 >= 255) return 0; sb(Q, j + 1); } }
  return gb(Q, r) == 0 && gb(Q, r + 1) == 0;
}

/* ---------- universal conductor tables ---------- */
static uint8_t *ktab[MMAX + 1], *ctab[MMAX + 1];   /* bit arrays */
static inline int tget(const uint8_t *t, u64 i) { return (t[i >> 3] >> (i & 7)) & 1; }
static double infl(const uint8_t *t, int nin, int j) {
  u64 N = 1ULL << nin, cnt = 0;
  for (u64 b = 0; b < N; b++) if (!((b >> j) & 1)) cnt += tget(t, b) != tget(t, b | (1ULL << j));
  return (double)cnt / (double)(N >> 1);
}
static void universal(void) {
  for (int m = 0; m <= MMAX; m++) {
    u64 N = 1ULL << m;
    ktab[m] = calloc((N >> 3) + 1, 1);
    for (u64 b = 0; b < N; b++) {
      u64 a = 0;
      for (int i = 0; i <= m; i++) a |= 1ULL << (2 * i);
      for (int i = 0; i < m; i++) a |= ((b >> i) & 1ULL) << (2 * i + 1);
      if (recon_last(a, 2 * m + 2)) ktab[m][b >> 3] |= 1 << (b & 7);
    }
    u64 N2 = 1ULL << (m + 1);
    ctab[m] = calloc((N2 >> 3) + 1, 1);
    for (u64 b = 0; b < N2; b++) {
      u64 a = 0;
      for (int i = 0; i <= m + 1; i++) a |= 1ULL << (2 * i);
      for (int i = 0; i <= m; i++) a |= ((b >> i) & 1ULL) << (2 * i + 1);
      if (recon_last(a, 2 * m + 3)) ctab[m][b >> 3] |= 1 << (b & 7);
    }
  }
  /* C5 */
  int ok = 1;
  for (u64 b = 0; b < 16; b++) {
    int b0 = b & 1, b1 = (b >> 1) & 1, b2 = (b >> 2) & 1;
    if (tget(ktab[0], 0) != 1 || tget(ktab[1], b & 1) != 1) ok = 0;
    if (tget(ktab[2], b & 3) != !(b0 ^ b1)) ok = 0;
    if (tget(ktab[3], b & 7) != (!(b1 ^ b2) ^ (b0 & !b1))) ok = 0;
    if (tget(ctab[0], b & 1) != b0 || tget(ctab[1], b & 3) != b0) ok = 0;
    if (tget(ctab[2], b & 7) != (b2 | ((!b0) & b1))) ok = 0;
  }
  CHECK(ok, "C5 universal tables differ from L954's hand formulas");
  CHECK(tget(ktab[4], 8) == 1, "C5 k_4(0,0,0,1) != 1 (GC1891)");
  printf("C5 universal tables vs hand formulas and GC1891's k_4(0001): %s\n", ok && tget(ktab[4], 8) == 1 ? "PASS" : "FAIL");

  /* PT7: influence profile */
  printf("\nPT7 universal influence Inf_j(k_m), by lag l = m-1-j (rows m, columns l = 0..m-1)\n");
  double inf[MMAX + 1][MMAX + 1];
  for (int m = 1; m <= MMAX; m++) {
    printf("INF m=%2d", m);
    for (int l = 0; l < m; l++) { int j = m - 1 - l; inf[m][l] = infl(ktab[m], m, j); printf(" %.4f", inf[m][l]); }
    printf("\n");
  }
  int a_ok = 1; for (int m = 2; m <= MMAX; m++) if (inf[m][0] < 0.75) a_ok = 0;
  int b_ok = 1; for (int l = 12; l < MMAX; l++) if (inf[MMAX][l] > 0.05) b_ok = 0;
  double stat = 0; for (int m = 16; m <= MMAX; m++) for (int m2 = 16; m2 <= MMAX; m2++) for (int l = 0; l <= 11; l++) {
    if (m - 1 - l < 4 || m2 - 1 - l < 4) continue;
    double d = fabs(inf[m][l] - inf[m2][l]); if (d > stat) stat = d; }
  int cf = 1; for (int l = 0; l <= 20; l++) if (inf[MMAX][l] < 0.25) cf = 0;
  printf("PT7a lag 0 >= 0.75 for all m >= 2: %s\n", a_ok ? "HELD" : "FAILED");
  printf("PT7b m=24, every lag >= 12 <= 0.05: %s\n", b_ok ? "HELD" : "FAILED");
  printf("PT7c stationarity max |diff| = %.4f (<= 0.03): %s\n", stat, stat <= 0.03 ? "HELD" : "FAILED");
  printf("PT7 counterfactual (no fading, all lags <= 20 >= 0.25 at m=24): %s\n", cf ? "MET" : "not met");

  /* PT5 universal: c_m ignores its newest tock */
  printf("\nPT5u P(c_m ignores b_m):");
  int u_ok = 1;
  for (int m = 0; m <= MMAX; m++) {
    double p = 1.0 - infl(ctab[m], m + 1, m);
    printf(" m%d=%.4f", m, p);
    if (m >= 20 && (p < 0.3 || p > 0.7)) u_ok = 0;
  }
  printf("\nPT5u in [0.3,0.7] at m = 20..24: %s\n", u_ok ? "HELD" : "FAILED");
}

/* ---------- lanes ---------- */
static u64 *g_rows;
static int cmp_rows(const void *A, const void *B) {
  const u64 *a = g_rows + (u64)(*(const uint32_t *)A) * NW, *b = g_rows + (u64)(*(const uint32_t *)B) * NW;
  for (int i = NW - 1; i >= 0; i--) { if (a[i] < b[i]) return -1; if (a[i] > b[i]) return 1; }
  return 0;
}
static int cmp_pair(const void *A, const void *B) {
  const int *a = A, *b = B;
  if (a[0] != b[0]) return (a[0] > b[0]) - (a[0] < b[0]);
  return (a[1] > b[1]) - (a[1] < b[1]);
}
static int cmp_dbl(const void *A, const void *B) { double a = *(const double *)A, b = *(const double *)B; return (a > b) - (a < b); }

static int *Dprev = NULL; static int Wprev = 0, maxDprev = 0;
static double MU[WMAX + 1][WMAX / 2 + 1];
static double LOGN[WMAX + 1], HENT[WMAX + 1];
static double DECIDED[WMAX + 1], ANCF[WMAX + 1], REDF[WMAX + 1], T1SHARE[WMAX + 1];

static void xor_world(int W) {
  RULE_XOR = 1;
  int n = W / 2; u64 L = 1ULL << n;
  u64 *rows = malloc(L * NW * 8), *tmp = malloc(NW * 8);
  uint32_t *idx = malloc(L * 4);
  for (u64 l = 0; l < L; l++) reconstruct(lane_trace(l, n), W, rows + l * NW);
  int collide = 0;
  for (int t = 1; t <= 4 * W; t++) {
    for (u64 l = 0; l < L; l++) { step(rows + l * NW, tmp); memcpy(rows + l * NW, tmp, NW * 8); }
    if (t % 2) continue;
    for (u64 l = 0; l < L; l++) idx[l] = (uint32_t)l;
    g_rows = rows; qsort(idx, L, 4, cmp_rows);
    for (u64 i = 1; i < L; i++) if (req(rows + (u64)idx[i] * NW, rows + (u64)idx[i - 1] * NW)) collide++;
  }
  CHECK(collide == 0, "C6 XOR world W=%d: %d coincident rows", W, collide);
  printf("C6 XOR world W=%d: coincident rows over ticks 1..2W = %d\n", W, collide);
  free(rows); free(tmp); free(idx);
  RULE_XOR = 0;
}

static void run_width(int W) {
  int n = W / 2; u64 L = 1ULL << n; int tmax = 4 * W + 4;
  u64 *start = calloc(L * NW, 8), *rows = calloc(L * NW, 8), *tr = calloc(L * TW, 8), *tmp = malloc(NW * 8);
  u64 *dbits = calloc(L * TW, 8);
  int *D = calloc(L, sizeof(int));
  uint8_t *ft = calloc(L * n, 1);               /* first identical tick of (l, l^2^j), l with bit j clear; 0 = never */
  uint8_t *anc = calloc(L, 1), *red = calloc(L, 1);
  uint32_t *idx = malloc(L * 4), *cls = malloc(L * 4);
  printf("\n=== W=%d n=%d lanes=%llu\n", W, n, (unsigned long long)L);

  for (u64 l = 0; l < L; l++) { reconstruct(lane_trace(l, n), W, start + l * NW); memcpy(rows + l * NW, start + l * NW, NW * 8); }

  /* C2 */
  for (u64 l = 0; l < L; l++) idx[l] = (uint32_t)l;
  g_rows = start; qsort(idx, L, 4, cmp_rows);
  int dup = 0; for (u64 i = 1; i < L; i++) if (req(start + (u64)idx[i] * NW, start + (u64)idx[i - 1] * NW)) dup++;
  CHECK(dup == 0, "C2 W=%d duplicate start rows %d", W, dup);

  /* ancestors (two backward steps, P_1 = 1) and C8 first half */
  int ancN = 0, c8a = 1;
  for (u64 l = 0; l < L; l++) {
    u64 Q[NW], P[NW], B[NW];
    for (int x = 0; x < 2; x++) {
      if (!back1(start + l * NW, x, Q)) continue;
      for (int y = 0; y < 2; y++) {
        if (!back1(Q, y, P)) continue;
        if (!gb(P, 1)) continue;
        if (!anc[l]) ancN++;
        anc[l] = 1;
        if (Dprev && Wprev == W - 2) {   /* B's tocks: Q's cell 1 at time 1, then b_0 .. b_(n-3) */
          u64 ib = (u64)gb(Q, 1) | ((l & ((1ULL << (n - 2)) - 1)) << 1);
          reconstruct(lane_trace(ib, n - 1), W - 2, B);
          if (!req(B, P)) c8a = 0;
        }
      }
    }
  }

  /* lockstep */
  for (int t = 0; t <= tmax; t++) {
    for (u64 l = 0; l < L; l++) {
      u64 *r = rows + l * NW;
      int a = gb(r, 1);
      if (a) tr[l * TW + (t >> 6)] |= 1ULL << (t & 63);
      if (!(t & 1) && !a && D[l] == 0) D[l] = t ? t : -1;
      if (t & 1) { int dd = gb(r, 3) ^ gb(r, 5); if (dd) dbits[l * TW + ((t >> 1) >> 6)] |= 1ULL << ((t >> 1) & 63); }
    }
    if (!(t & 1) && t >= 2) {
      int k = t / 2;
      for (u64 l = 0; l < L; l++) for (int j = 0; j < n; j++) {
        if ((l >> j) & 1) continue;
        if (ft[l * n + j]) continue;
        if (req(rows + l * NW, rows + (l ^ (1ULL << j)) * NW)) ft[l * n + j] = (uint8_t)(k > 255 ? 255 : k);
      }
      /* classes among lanes that passed every tick before t */
      u64 na = 0;
      for (u64 l = 0; l < L; l++) if (D[l] == 0 || D[l] >= t) idx[na++] = (uint32_t)l;
      g_rows = rows; qsort(idx, na, 4, cmp_rows);
      u64 i = 0; int ncls = 0; double H = 0;
      while (i < na) {
        u64 e = i + 1;
        while (e < na && req(rows + (u64)idx[e] * NW, rows + (u64)idx[i] * NW)) e++;
        int has = 0; for (u64 q = i; q < e; q++) if (anc[idx[q]]) has = 1;
        if (has) for (u64 q = i; q < e; q++) red[idx[q]] = 1;
        double p = (double)(e - i) / (double)na; H -= p * log2(p);
        ncls++; i = e;
      }
      if (k == n) { LOGN[W] = log2((double)ncls); HENT[W] = H; }
      if (k <= n + 2 || k % 4 == 0) printf("FUNNEL W=%d tick=%d alive=%llu classes=%d log2=%.3f H=%.3f\n", W, k, (unsigned long long)na, ncls, log2((double)ncls), H);
    }
    if (t < tmax) for (u64 l = 0; l < L; l++) { step(rows + l * NW, tmp); memcpy(rows + l * NW, tmp, NW * 8); }
  }
  for (u64 l = 0; l < L; l++) if (D[l] == -1) D[l] = 0;   /* not possible for lanes: tick 0 is black */

  /* C1 */
  int c1 = 1, cens = 0, maxD = 0;
  for (u64 l = 0; l < L; l++) {
    u64 want = lane_trace(l, n);
    for (int t = 0; t < W; t++) if ((int)((tr[l * TW + (t >> 6)] >> (t & 63)) & 1) != (int)((want >> t) & 1)) c1 = 0;
    if (D[l] == 0) cens++;
    if (D[l] > maxD) maxD = D[l];
  }
  CHECK(c1, "C1 W=%d replay", W); CHECK(cens == 0, "C1 W=%d censored %d", W, cens);
  printf("C1 replay %s, censored %d, maxD %d\n", c1 ? "PASS" : "FAIL", cens, maxD);

  /* C8: deaths of ancestors, reducible bound */
  if (Dprev && Wprev == W - 2) {
    int c8b = 1;
    for (u64 l = 0; l < L; l++) {
      if (!anc[l]) continue;
      u64 Q[NW], P[NW];
      for (int x = 0; x < 2; x++) { if (!back1(start + l * NW, x, Q)) continue;
        for (int y = 0; y < 2; y++) { if (!back1(Q, y, P) || !gb(P, 1)) continue;
          u64 ib = (u64)gb(Q, 1) | ((l & ((1ULL << (n - 2)) - 1)) << 1);
          if (Dprev[ib] != D[l] + 2) c8b = 0; } }
    }
    int c8c = 1; for (u64 l = 0; l < L; l++) if (red[l] && D[l] > maxDprev - 2) c8c = 0;
    CHECK(c8a, "C8 W=%d ancestor is not the named lane", W); CHECK(c8b, "C8 W=%d ancestor death != D+2", W);
    CHECK(c8c, "C8 W=%d reducible lane outlives maxD(W-2)-2", W);
    printf("C8 ancestor=lane %s, death D+2 %s, reducible bound %s\n", c8a ? "PASS" : "FAIL", c8b ? "PASS" : "FAIL", c8c ? "PASS" : "FAIL");
  }
  int redN = 0; for (u64 l = 0; l < L; l++) redN += red[l];
  ANCF[W] = (double)ancN / L; REDF[W] = (double)redN / L;
  int elig = 0, eligred = 0; for (u64 l = 0; l < L; l++) if (D[l] <= maxDprev - 2) { elig++; eligred += red[l]; }
  printf("PT6 W=%d ancestors %.4f reducible %.4f (eligible D<=maxD(W-2)-2: %d lanes, reducible among them %.4f)\n",
         W, ANCF[W], REDF[W], elig, elig ? (double)eligred / elig : 0.0);

  /* twins: C3, C4, C7, C12, mu, merge ticks */
  int c3 = 1, c4 = 1, c7 = 1, c12 = 1;
  printf("MU W=%d", W);
  for (int j = 0; j < n; j++) {
    u64 pairs = 0, merged = 0, tick1 = 0;
    for (u64 l = 0; l < L; l++) {
      if ((l >> j) & 1) continue;
      u64 l2 = l ^ (1ULL << j); pairs++;
      int k = ft[l * n + j];
      if (k && k <= j) c4 = 0;
      int both = k && (D[l] >= 2 * k) && (D[l2] >= 2 * k);
      if (both) { merged++; if (k == j + 1) tick1++; if (D[l] != D[l2]) c3 = 0;
        for (int d = 1; d < 2 * j + 2; d++) if (gb(start + l * NW, d) != gb(start + l2 * NW, d)) c12 = 0; }
      if (j <= 3) {
        int eq = 1; for (int t = W; t <= W + 4 * j + 3; t++) if (((tr[l * TW + (t >> 6)] ^ tr[l2 * TW + (t >> 6)]) >> (t & 63)) & 1) eq = 0;
        if (eq != (k == j + 1)) c7 = 0;
      }
    }
    MU[W][j] = (double)merged / pairs;
    if (j == 0) T1SHARE[W] = merged ? (double)tick1 / merged : 0.0;
    printf(" j%d=%.4f(t1 %.3f)", j, MU[W][j], merged ? (double)tick1 / merged : 0.0);
  }
  printf("\n");
  CHECK(c3, "C3 W=%d merged with unequal deaths", W); CHECK(MU[W][n - 1] == 0.0, "C3 W=%d b_(n-1) twins merged", W);
  CHECK(c4, "C4 W=%d early identity", W); CHECK(c7, "C7 W=%d window equivalence", W); CHECK(c12, "C12 W=%d inner cells differ", W);
  printf("C3 %s C4 %s C7 %s C12 %s\n", c3 && MU[W][n - 1] == 0.0 ? "PASS" : "FAIL", c4 ? "PASS" : "FAIL", c7 ? "PASS" : "FAIL", c12 ? "PASS" : "FAIL");

  /* PT1 detail at W = 40 and C11 */
  if (W == 40) {
    u64 ch0 = 0, chl = 0;
    for (u64 l = 0; l < L; l++) { if (!(l & 1) && D[l] != D[l ^ 1]) ch0++; if (!((l >> (n - 1)) & 1) && D[l] != D[l ^ (1ULL << (n - 1))]) chl++; }
    int c11 = ch0 == 5228 && chl == 349146 && D[47284] == 66 && D[180] == 40 && D[47104] == 42;
    CHECK(c11, "C11 L942 counts: %llu %llu %d %d %d", (unsigned long long)ch0, (unsigned long long)chl, D[47284], D[180], D[47104]);
    printf("C11 L942 b0 changes %llu, b19 changes %llu, D(47284,180,47104) = %d %d %d: %s\n", (unsigned long long)ch0,
           (unsigned long long)chl, D[47284], D[180], D[47104], c11 ? "PASS" : "FAIL");

    /* PT3 footprint */
    printf("PT3 footprint E (deepest differing depth - (2j+2)): j: merged median [p90] | unmerged median\n");
    double *buf = malloc(L * sizeof(double)), *buf2 = malloc(L * sizeof(double));
    int pt3a = 1; double medlo = 1e9, medhi = -1e9; int pt3b = 1;
    for (int j = 0; j <= n - 2; j++) {
      int nm = 0, nu = 0;
      for (u64 l = 0; l < L; l++) {
        if ((l >> j) & 1) continue;
        u64 l2 = l ^ (1ULL << j);
        int deep = 0; for (int d = 255; d >= 1; d--) if (gb(start + l * NW, d) != gb(start + l2 * NW, d)) { deep = d; break; }
        int k = ft[l * n + j]; int both = k && D[l] >= 2 * k && D[l2] >= 2 * k;
        if (both) buf[nm++] = deep - (2 * j + 2); else buf2[nu++] = deep - (2 * j + 2);
      }
      qsort(buf, nm, sizeof(double), cmp_dbl); qsort(buf2, nu, sizeof(double), cmp_dbl);
      double med = nm ? buf[nm / 2] : -1, p90 = nm ? buf[(int)(nm * 0.9)] : -1, medu = nu ? buf2[nu / 2] : -1;
      printf("FOOT j=%d merged %d med %.0f p90 %.0f | unmerged %d med %.0f\n", j, nm, med, p90, nu, medu);
      if (j >= 2 && j <= 12) { if (med > 10) pt3a = 0; if (med < medlo) medlo = med; if (med > medhi) medhi = med;
        if (nu && medu < W - 2 * j - 6) pt3b = 0; }
    }
    printf("PT3 merged medians <= 10 (j=2..12): %s; span %.0f (<= 4): %s; unmerged reach the edge: %s\n",
           pt3a ? "HELD" : "FAILED", medhi - medlo, medhi - medlo <= 4 ? "HELD" : "FAILED", pt3b ? "HELD" : "FAILED");
    free(buf); free(buf2);
    double mu0 = MU[40][0];
    printf("PT1 mu_40(0) = %.4f in [0.975, 0.990]: %s; share at tick 1 %.4f (>= 0.95): %s\n", mu0,
           (mu0 >= 0.975 && mu0 <= 0.990) ? "HELD" : "FAILED", T1SHARE[40], T1SHARE[40] >= 0.95 ? "HELD" : "FAILED");

    /* C10 and PU */
    int c10 = 1; u64 c10n = 0;
    for (u64 l = 0; l < L; l++) for (int i = 0; 2 * i + 6 < D[l] && 2 * i + 5 < 192; i++) {
      int bi = (tr[l * TW + ((2 * i + 1) >> 6)] >> ((2 * i + 1) & 63)) & 1;
      int bi1 = (tr[l * TW + ((2 * i + 3) >> 6)] >> ((2 * i + 3) & 63)) & 1;
      int bi2 = (tr[l * TW + ((2 * i + 5) >> 6)] >> ((2 * i + 5) & 63)) & 1;
      int di = (dbits[l * TW + (i >> 6)] >> (i & 63)) & 1;
      if (di != (bi2 ^ (bi | bi1))) c10 = 0; c10n++;
    }
    CHECK(c10, "C10 GC1889 discrepancy formula");
    printf("C10 GC1889 d formula on %llu samples: %s\n", (unsigned long long)c10n, c10 ? "PASS" : "FAIL");

    /* top 64 lanes by death, ties by index */
    int top[64];
    int *order = malloc(L * 2 * sizeof(int));     /* (-D, l) pairs: longest-lived first, ties by index */
    for (u64 l = 0; l < L; l++) { order[2 * l] = -D[l]; order[2 * l + 1] = (int)l; }
    qsort(order, L, 2 * sizeof(int), cmp_pair);
    for (int s = 0; s < 64; s++) top[s] = order[2 * s + 1];
    free(order);
    static double gx[4096], gy[4096], sx[4096], sy[4096]; int ng = 0, ns = 0; double gsum = 0; int gcount = 0;
    u64 seed = 0x9E3779B97F4A7C15ULL;
    for (int s = 0; s < 64; s++) {
      int l = top[s]; int g[128], nG = 0, last = -1;
      for (int i = 0; 2 * i + 1 < D[l]; i++) { int di = (dbits[(u64)l * TW + (i >> 6)] >> (i & 63)) & 1; if (di) { if (last >= 0) g[nG++] = i - last; last = i; } }
      for (int q = 0; q < nG; q++) { gsum += g[q]; gcount++; }
      for (int q = 0; q + 1 < nG && ng < 4096; q++) { gx[ng] = g[q]; gy[ng] = g[q + 1]; ng++; }
      int h[128]; memcpy(h, g, sizeof(int) * nG);
      for (int q = nG - 1; q > 0; q--) { seed ^= seed << 13; seed ^= seed >> 7; seed ^= seed << 17; int r = (int)(seed % (u64)(q + 1)); int tt = h[q]; h[q] = h[r]; h[r] = tt; }
      for (int q = 0; q + 1 < nG && ns < 4096; q++) { sx[ns] = h[q]; sy[ns] = h[q + 1]; ns++; }
      if (s == 63) {
        /* Spearman via average ranks */
        double rho[2]; double *X[2] = {gx, sx}, *Y[2] = {gy, sy}; int NN[2] = {ng, ns};
        for (int z = 0; z < 2; z++) {
          int N = NN[z]; double *rx = malloc(N * sizeof(double)), *ry = malloc(N * sizeof(double));
          for (int a = 0; a < N; a++) { double lt = 0, eq = 0, ltY = 0, eqY = 0;
            for (int b = 0; b < N; b++) { if (X[z][b] < X[z][a]) lt++; else if (X[z][b] == X[z][a]) eq++; if (Y[z][b] < Y[z][a]) ltY++; else if (Y[z][b] == Y[z][a]) eqY++; }
            rx[a] = lt + (eq + 1) / 2.0; ry[a] = ltY + (eqY + 1) / 2.0; }
          double mx = 0, my = 0; for (int a = 0; a < N; a++) { mx += rx[a]; my += ry[a]; } mx /= N; my /= N;
          double sxy = 0, sxx = 0, syy = 0; for (int a = 0; a < N; a++) { sxy += (rx[a] - mx) * (ry[a] - my); sxx += (rx[a] - mx) * (rx[a] - mx); syy += (ry[a] - my) * (ry[a] - my); }
          rho[z] = sxy / sqrt(sxx * syy); free(rx); free(ry);
        }
        double mg = gsum / gcount;
        printf("PU top-64 lanes (deaths %d..%d): gaps %d, mean gap %.3f tocks, Spearman successive %.4f, shuffled %.4f\n",
               D[top[63]], D[top[0]], gcount, mg, rho[0], rho[1]);
        printf("PU mean in [1.6,2.6]: %s; |rho| <= 0.15: %s; within 0.10 of shuffle: %s\n", (mg >= 1.6 && mg <= 2.6) ? "HELD" : "FAILED",
               fabs(rho[0]) <= 0.15 ? "HELD" : "FAILED", fabs(rho[0] - rho[1]) <= 0.10 ? "HELD" : "FAILED");
      }
    }
  }

  /* PT5: decided vs conflict at the death tick */
  {
    u64 nT = 0, dec = 0; int c9 = 1; u64 atW = 0;
    u64 M[NW], M2[NW];
    for (u64 l = 0; l < L; l++) {
      int T = D[l];
      if (T == W) { atW++; continue; }
      if (T < W + 2) continue;
      memcpy(M, start + l * NW, NW * 8); sb(M, T);
      for (int t = 0; t <= T; t++) {
        int a = gb(M, 1), o = (int)((tr[l * TW + (t >> 6)] >> (t & 63)) & 1);
        if (t < T - 1 && a != o) c9 = 0;
        if (t == T - 1 && a == o) c9 = 0;
        if (t == T) { nT++; if (!a) dec++; }
        if (t < T) { step(M, M2); memcpy(M, M2, NW * 8); }
      }
    }
    CHECK(c9, "C9 W=%d first-arrival", W);
    DECIDED[W] = nT ? (double)dec / nT : -1;
    printf("PT5 W=%d deaths at W: %.4f; at T>=W+2: %llu, decided %.4f; C9 %s\n", W, (double)atW / L, (unsigned long long)nT, DECIDED[W], c9 ? "PASS" : "FAIL");
  }

  /* death histogram (short) */
  {
    int h[256] = {0}; for (u64 l = 0; l < L; l++) h[D[l] < 255 ? D[l] : 255]++;
    printf("DEATHS W=%d:", W); for (int t = 0; t < 256; t++) if (h[t]) printf(" %d:%d", t, h[t]); printf("\n");
  }

  free(Dprev); Dprev = D; Wprev = W; maxDprev = maxD;
  free(start); free(rows); free(tr); free(tmp); free(dbits); free(ft); free(anc); free(red); free(idx); free(cls);
}

int main(void) {
  setvbuf(stdout, NULL, _IOLBF, 0);
  printf("tock_twins.c (L955): zero-wall lanes W = %d..%d, universal tables m <= %d\n", WMIN, WMAX, MMAX);
  universal();
  for (int W = 8; W <= 24; W += 2) xor_world(W);
  for (int W = WMIN; W <= WMAX; W += 2) run_width(W);

  /* PT2: lag collapse */
  printf("\nPT2 mu by lag (rows W, columns lambda = 0..n-1)\n");
  for (int W = 24; W <= 40; W += 4) { int n = W / 2; printf("LAG W=%d", W); for (int la = 0; la < n; la++) printf(" %.4f", MU[W][n - 1 - la]); printf("\n"); }
  int Ws[5] = {24, 28, 32, 36, 40};
  double worstLag = 0; for (int la = 2; la <= 9; la++) { double lo = 1, hi = 0; for (int q = 0; q < 5; q++) { int n = Ws[q] / 2, j = n - 1 - la; if (j < 2) continue; double v = MU[Ws[q]][j]; if (v < lo) lo = v; if (v > hi) hi = v; }
    printf("PT2 lag %d spread %.4f\n", la, hi - lo); if (hi - lo > worstLag) worstLag = hi - lo; }
  double lo = 1, hi = 0; for (int q = 0; q < 5; q++) { double v = MU[Ws[q]][2]; if (v < lo) lo = v; if (v > hi) hi = v; } double spreadJ2 = hi - lo;
  lo = 1; hi = 0; for (int q = 0; q < 5; q++) { int n = Ws[q] / 2; double v = MU[Ws[q]][n / 2]; if (v < lo) lo = v; if (v > hi) hi = v; } double spreadHalf = hi - lo;
  printf("PT2 worst lag spread %.4f (<= 0.04): %s; fixed j=2 spread %.4f (>= 0.10): %s; fixed j=n/2 spread %.4f (>= 0.10): %s\n",
         worstLag, worstLag <= 0.04 ? "HELD" : "FAILED", spreadJ2, spreadJ2 >= 0.10 ? "HELD" : "FAILED", spreadHalf, spreadHalf >= 0.10 ? "HELD" : "FAILED");
  int mono = 1, m1 = 1, m9 = 1; double ratio_lo = 1e9, ratio_hi = -1;
  for (int q = 0; q < 5; q++) { int W = Ws[q], n = W / 2;
    for (int la = 1; la < n - 1; la++) if (MU[W][n - 1 - (la + 1)] < MU[W][n - 1 - la] - 0.02) mono = 0;
    if (MU[W][n - 2] > 0.5) m1 = 0;
    if (n - 1 - 9 >= 0 && MU[W][n - 1 - 9] < 0.75) m9 = 0;
    double u3 = 1 - MU[W][n - 1 - 3], u9 = 1 - MU[W][n - 1 - 9];
    if (u3 > 0 && u9 > 0) { double r = pow(u9 / u3, 1.0 / 6.0); if (r < ratio_lo) ratio_lo = r; if (r > ratio_hi) ratio_hi = r; } }
  printf("PT2 monotone: %s; mu(1) <= 0.5: %s; mu(9) >= 0.75: %s; per-lag ratio of (1-mu), lambda 3..9: %.3f..%.3f (in [0.65,0.90]): %s\n",
         mono ? "HELD" : "FAILED", m1 ? "HELD" : "FAILED", m9 ? "HELD" : "FAILED", ratio_lo, ratio_hi,
         (ratio_lo >= 0.65 && ratio_hi <= 0.90) ? "HELD" : "FAILED");
  int posCF = spreadJ2 <= 0.04 && worstLag >= 0.10;
  printf("PT2 positional counterfactual: %s\n", posCF ? "MET" : "not met");

  /* PT4 */
  double rate = (LOGN[40] - LOGN[24]) / 8.0, dH = HENT[40] - HENT[24];
  printf("\nPT4 log2 N at tick n:"); for (int W = WMIN; W <= WMAX; W += 2) printf(" W%d=%.3f", W, LOGN[W]);
  printf("\nPT4 H at tick n:"); for (int W = WMIN; W <= WMAX; W += 2) printf(" W%d=%.3f", W, HENT[W]);
  printf("\nPT4 count rate %.3f per free tock (in [0.60,0.95]): %s; H_40 - H_24 = %.3f (<= 5): %s; counterfactual (>= 7): %s\n",
         rate, (rate >= 0.60 && rate <= 0.95) ? "HELD" : "FAILED", dH, dH <= 5 ? "HELD" : "FAILED", dH >= 7 ? "MET" : "not met");

  /* PT5, PT6 */
  int p5 = 1; for (int W = 24; W <= 40; W += 2) if (DECIDED[W] < 0.3 || DECIDED[W] > 0.7) p5 = 0;
  printf("PT5 decided in [0.3,0.7] at W = 24..40: %s\n", p5 ? "HELD" : "FAILED");
  int p6a = 1, p6b = 1; for (int W = 24; W <= 40; W += 2) { if (ANCF[W] < 0.08 || ANCF[W] > 0.20) p6a = 0; if (REDF[W] < 0.2 || REDF[W] > 0.8) p6b = 0; }
  printf("PT6 ancestors in [0.08,0.20]: %s; reducible in [0.2,0.8]: %s\n", p6a ? "HELD" : "FAILED", p6b ? "HELD" : "FAILED");

  printf("\nCONTROLS: %s (%d failures)\n", fails ? "FAIL" : "ALL PASS", fails);
  return fails ? 1 : 0;
}
