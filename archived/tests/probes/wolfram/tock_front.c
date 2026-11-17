/* tock_front.c: does the forgetting front keep moving out? (Local, 2026-10-26, L955 part 2; frozen before its run)

RUN-ON:   cpu, one process (cc -O2 -o tock_front tock_front.c -lm; ./tock_front > front.txt)
COST:     about a minute on the M5, under 1 GB.
WHY:      tock_twins.c (frozen e343a4eb, run once at 09:46 GMT) refuted a lag-stationary fading memory (PT2, PT7) and found
          forgetting by POSITION: only the earliest free tocks merge with their twins, always at tick j+1 (never later, every
          W <= 40), with each fixed j's merge fraction rising with W; the universal conductor's influence Inf_j(k_m) is a coin
          (0.50) except for the first few tocks, whose influence decays as m grows, the onset delayed with j. Read from the
          W <= 40 and m <= 24 tables after that run, the front (the j where Inf_j(k_m) = 0.25, interpolated) sits at 0.75,
          1.4, 1.9, 2.5 for m = 12, 16, 20, 24, about 0.145 tocks per step; the twin half-merge point at 0.9, 1.6, 2.1 for
          W = 24, 32, 40. These readings are post hoc; this file tests them on unseen widths and steps.
If this holds, it changes: DQ-009 (the referee forgets a slowly growing oldest part of its history and nothing else) and
          DQ-001/DQ-012 (the forgettable surplus of a start grows with its width); no prize or proof status.

Model and lanes exactly as tock_twins.c. Twins (l, l XOR 2^j) are identical at tick j+1 iff their traces agree on
[W, W+4j+3] (L954 Proposition 2; tock_twins.c's C7 checked it for j <= 3 at every W <= 40). mu1_W(j) is that fraction.
Record searched: as tock_twins.c (same day); no further run.

PREDICTIONS, written 2026-10-26 before this file's first run.
Controls:
  F1  replay: every lane at W = 42..48 reproduces its construction at t < W.
  F2  the window method reproduces tock_twins.c's merge fractions at W = 40: j0..j4 = 0.9872, 0.8534, 0.5345, 0.2599,
      0.1106 (to 4 decimals), and its universal influences at m = 24: j0..j3 = 0.0025, 0.0391, 0.1666, 0.3178.
Blind (extrapolated from the W <= 40 and m <= 24 trends, ranges set before the run):
  FT1 twin merges keep rising at every fixed early j: mu1 at W = 44 / 48:
        j0 in [0.990, 0.995] / [0.993, 0.998];  j1 in [0.88, 0.92] / [0.91, 0.95];  j2 in [0.58, 0.66] / [0.63, 0.73];
        j3 in [0.30, 0.38] / [0.36, 0.46];  j4 in [0.13, 0.19] / [0.17, 0.26];  every j >= 12 at most 0.0001.
  FT2 the half-merge point (interpolated j with mu1 = 0.5) at W = 48 lies in [2.4, 3.0].
  FT3 the conductor's front advances: the interpolated j with Inf_j(k_m) = 0.25 at m = 28 lies in [2.7, 3.5];
      Inf_0(k_28) in [0.0005, 0.0015]; Inf_1(k_28) in [0.010, 0.025]; Inf_6(k_28) <= 0.48.
  FCF counterfactual (the front stalls): mu1_48(2) <= 0.56 and the m = 28 front <= 2.6.
CAPS: W <= 48, m <= 28, one process, ulimit -t 900.

OUTCOME, 2026-10-26 (the single run, 09:54 GMT, 20.2 s, 268 MB; frozen source sha256 3f7b3670..., commit 540e5b12; raw
output front.txt sha256 d0a4b028..., cited/tock-twins-20261026/). Added after the run.
  F1, F2 PASS. FT1 HELD (W = 44: 0.9927, 0.9011, 0.6290, 0.3396, 0.1574; W = 48: 0.9958, 0.9341, 0.7118, 0.4236, 0.2130;
  j12 = 0). FT2 HELD (half-merge point 2.13, 2.29, 2.45, 2.59, 2.74 at W = 40..48). FT3 HELD (front 2.55, 2.69, 2.84, 2.98,
  3.16 at m = 24..28; Inf0(k_28) = 0.00079, Inf1 = 0.0166, Inf6 = 0.4701). FCF not met: the front does not stall. Both fronts
  advance about 0.15 tocks per tock: measured to W = 48 and m = 28, no all-width claim.
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef uint64_t u64;
#define NW 4
static int fails = 0;
#define CHECK(c, ...) do { if (!(c)) { fails++; printf("CONTROL FAIL: " __VA_ARGS__); printf("\n"); } } while (0)

static inline int gb(const u64 *r, int d) { return (int)((r[d >> 6] >> (d & 63)) & 1); }
static inline void sb(u64 *r, int d) { r[d >> 6] |= 1ULL << (d & 63); }
static void step(const u64 *w, u64 *o) {
  u64 r[NW], l[NW];
  for (int i = 0; i < NW; i++) { r[i] = (w[i] >> 1) | (i + 1 < NW ? (w[i + 1] << 63) : 0); l[i] = (w[i] << 1) | (i > 0 ? (w[i - 1] >> 63) : 0); }
  for (int i = 0; i < NW; i++) o[i] = r[i] ^ (w[i] | l[i]);
  o[0] &= ~1ULL;
}
static void reconstruct(u64 a, int T, u64 *row) {
  u64 cm1 = 0, c = a; memset(row, 0, NW * 8); if (c & 1) sb(row, 1);
  for (int d = 1; d < T; d++) { u64 nx = (c >> 1) ^ (c | cm1); cm1 = c; c = nx; if (c & 1) sb(row, d + 1); }
}
static int recon_last(u64 a, int T) { u64 cm1 = 0, c = a; for (int d = 1; d < T; d++) { u64 nx = (c >> 1) ^ (c | cm1); cm1 = c; c = nx; } return (int)(c & 1); }
static u64 spread8[256];   /* bit i of a byte -> bit 2i+1 */
static u64 odd_spread(u64 b) { u64 a = 0; for (int k = 0; b; k++, b >>= 8) a |= spread8[b & 255] << (16 * k); return a; }
static u64 evens(int upto) { u64 a = 0; for (int i = 0; 2 * i <= upto; i++) a |= 1ULL << (2 * i); return a; }

static double MU1[49][25];
static void twins(int W) {
  int n = W / 2; u64 L = 1ULL << n; int jmax = n - 1 < 12 ? n - 1 : 12; int tend = W + 4 * jmax + 3;
  u64 *win = malloc(L * 8); u64 row[NW], tmp[NW]; int f1 = 1; u64 ev = evens(W - 2);
  for (u64 l = 0; l < L; l++) {
    u64 a = ev | odd_spread(l);
    reconstruct(a, W, row);
    u64 w = 0;
    for (int t = 0; t <= tend; t++) {
      int x = gb(row, 1);
      if (t < W && x != (int)((a >> t) & 1)) f1 = 0;
      if (t >= W && x) w |= 1ULL << (t - W);
      step(row, tmp); memcpy(row, tmp, NW * 8);
    }
    win[l] = w;
  }
  CHECK(f1, "F1 replay W=%d", W);
  printf("MU1 W=%d", W);
  for (int j = 0; j <= jmax; j++) {
    u64 mask = (4 * j + 4 >= 64) ? ~0ULL : ((1ULL << (4 * j + 4)) - 1), m = 0, p = 0;
    for (u64 l = 0; l < L; l++) { if ((l >> j) & 1) continue; p++; if (((win[l] ^ win[l ^ (1ULL << j)]) & mask) == 0) m++; }
    MU1[W][j] = (double)m / p; printf(" j%d=%.4f", j, MU1[W][j]);
  }
  printf("\n");
  free(win);
}
static double halfpoint(double *v, int nj, double level) {
  for (int j = 0; j + 1 < nj; j++) if (v[j] >= level && v[j + 1] < level) return j + (v[j] - level) / (v[j] - v[j + 1]);
  return -1;
}
int main(void) {
  setvbuf(stdout, NULL, _IOLBF, 0);
  for (int x = 0; x < 256; x++) { u64 a = 0; for (int i = 0; i < 8; i++) if ((x >> i) & 1) a |= 1ULL << (2 * i + 1); spread8[x] = a; }
  /* conductor influences, j <= 8, m = 24..28 */
  double INF[29][9];
  for (int m = 24; m <= 28; m++) {
    u64 N = 1ULL << m; uint8_t *t = calloc(N / 8 + 1, 1); u64 ev = evens(2 * m);
    for (u64 b = 0; b < N; b++) if (recon_last(ev | odd_spread(b), 2 * m + 2)) t[b >> 3] |= 1 << (b & 7);
    printf("INF m=%d", m);
    for (int j = 0; j <= 8; j++) { u64 c = 0; for (u64 b = 0; b < N; b++) if (!((b >> j) & 1)) c += ((t[b >> 3] >> (b & 7)) & 1) != ((t[(b | (1ULL << j)) >> 3] >> ((b | (1ULL << j)) & 7)) & 1);
      INF[m][j] = (double)c / (double)(N >> 1); printf(" j%d=%.4f", j, INF[m][j]); }
    printf("\n");
    free(t);
  }
  /* the front is where influence RISES through 0.25: interpolate on the increasing sequence */
  double fr[29];
  for (int m = 24; m <= 28; m++) { fr[m] = -1; for (int j = 0; j < 8; j++) if (INF[m][j] <= 0.25 && INF[m][j + 1] > 0.25) fr[m] = j + (0.25 - INF[m][j]) / (INF[m][j + 1] - INF[m][j]);
    printf("FRONT m=%d %.3f\n", m, fr[m]); }
  for (int W = 40; W <= 48; W += 2) twins(W);

  int f2 = fabs(MU1[40][0] - 0.9872) < 5e-5 && fabs(MU1[40][1] - 0.8534) < 5e-5 && fabs(MU1[40][2] - 0.5345) < 5e-5 &&
           fabs(MU1[40][3] - 0.2599) < 5e-5 && fabs(MU1[40][4] - 0.1106) < 5e-5 &&
           fabs(INF[24][0] - 0.0025) < 5e-5 && fabs(INF[24][1] - 0.0391) < 5e-5 && fabs(INF[24][2] - 0.1666) < 5e-5 && fabs(INF[24][3] - 0.3178) < 5e-5;
  CHECK(f2, "F2 reproduction of tock_twins.c");
  printf("F2 reproduces tock_twins.c at W=40 and m=24: %s\n", f2 ? "PASS" : "FAIL");

  double lo44[5] = {0.990, 0.88, 0.58, 0.30, 0.13}, hi44[5] = {0.995, 0.92, 0.66, 0.38, 0.19};
  double lo48[5] = {0.993, 0.91, 0.63, 0.36, 0.17}, hi48[5] = {0.998, 0.95, 0.73, 0.46, 0.26};
  int ft1 = 1; for (int j = 0; j < 5; j++) { if (MU1[44][j] < lo44[j] || MU1[44][j] > hi44[j]) ft1 = 0; if (MU1[48][j] < lo48[j] || MU1[48][j] > hi48[j]) ft1 = 0; }
  int ft1z = MU1[44][12] <= 0.0001 && MU1[48][12] <= 0.0001;
  printf("FT1 ranges at W=44/48 for j=0..4: %s; j=12 at most 0.0001: %s\n", ft1 ? "HELD" : "FAILED", ft1z ? "HELD" : "FAILED");
  for (int W = 40; W <= 48; W += 2) printf("HALF W=%d %.3f\n", W, halfpoint(MU1[W], 13, 0.5));
  double h48 = halfpoint(MU1[48], 13, 0.5);
  printf("FT2 half-merge point at W=48 = %.3f in [2.4,3.0]: %s\n", h48, (h48 >= 2.4 && h48 <= 3.0) ? "HELD" : "FAILED");
  int ft3 = fr[28] >= 2.7 && fr[28] <= 3.5 && INF[28][0] >= 0.0005 && INF[28][0] <= 0.0015 && INF[28][1] >= 0.010 && INF[28][1] <= 0.025 && INF[28][6] <= 0.48;
  printf("FT3 front(28) = %.3f, Inf0 = %.5f, Inf1 = %.4f, Inf6 = %.4f: %s\n", fr[28], INF[28][0], INF[28][1], INF[28][6], ft3 ? "HELD" : "FAILED");
  printf("FCF stall counterfactual: %s\n", (MU1[48][2] <= 0.56 && fr[28] <= 2.6) ? "MET" : "not met");
  printf("CONTROLS: %s (%d failures)\n", fails ? "FAIL" : "ALL PASS", fails);
  return fails ? 1 : 0;
}
