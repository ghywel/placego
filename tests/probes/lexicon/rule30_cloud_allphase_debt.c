/* rule30_cloud_allphase_debt.c: AP, the exact slope-5/2 reference debt of EVERY rooted period-32 history to the RD32
 * frontier 2^20, every global rotation included (Cloud; GC940 review, an assist step for Q7).
 *
 * RUN-ON:  cpu, one core, about 1 s
 * BUILD:   cc -O2 -o rule30_cloud_allphase_debt tests/probes/lexicon/rule30_cloud_allphase_debt.c  (binary outside Git)
 * RUN:     ./rule30_cloud_allphase_debt
 *
 * Why. RD32 (rule30_debt32.c, GC325; recomputed by Local, L199) measures the debt of one representative per rotation
 * class of the sixteen histories: maximum 60. GC315 transfers this to the omitted global rotations with an allowance
 * D_phi <= D + P - 1, so GC940 uses 91 at P = 32 and the ratio bound 2^20/123 > 8525, and calls the denominator
 * 32 + 60 = 92 "not a justified all-phase denominator". This probe measures D_phi exactly. Rotating every pair of a
 * history by phi rotates every driver, and delay(rot(w, phi), T) = delay(w, T + phi): the rotated history's clock is
 * the original drivers' clock started at phi. Each walk therefore carries 32 clocks U_phi (U_0 = phi), with
 * z = 2 (U_phi - phi) - 5 d and D_phi = max over a <= b of z_b - z_a. The walk, the child constructor and the doubling
 * test are copied from rule30_debt32.c (shared in method; the clocks and debts here are written separately).
 *
 * Record searched: "D_phi|all-phase|every global phase" + "debt" -> 16 hits (G9, G143/G144, the GC315 note);
 *   "phase" + "RD32|debt32" -> 6 hits (map, the RD16 board row "finite phase/birth bound 75", RD32's preregistration,
 *   GC326/327). No exact all-phase debt measured anywhere: only GC315's transfer (75 at entry, 91 at the frontier).
 * PREDICTIONS, written 2026-10-10 03:47 BST (scratch copy first) before the program was compiled or run:
 *   C1 (control, 0.97): phi = 0 reproduces RD32's sixteen doubled debts.
 *   C2 (control, 0.97): D_phi = D_(phi+16) on every prefix through its N5 entry (period-16 drivers).
 *   G  (GC315 as a check, 0.97): every |D_phi - D_0| <= 31.
 *   P1 (0.6): the exact all-phase maximum is at most 75 (well inside GC940's 91).
 *   U  (unexpected, 0.7): some rotated history has debt above 60, the representatives' maximum.
 *   Counterfactual: a D_phi > D_0 + 31 refutes GC315 as applied; P1 failing means the 91 allowance is nearly needed.
 * OUTCOME, 2026-10-10 03:48 BST (one run, 1.2 s): C1 PASS, C2 PASS, G HELD, P1 HELD, U REFUTED.
 *   - D_phi = D_0 at every phi on all sixteen histories: the deviation is exactly 0. The exact all-phase maximum is 60,
 *     so at this frontier the all-phase ratio is 2^20/(32 + 60) = 11397.6: GC940's 92 is exact here, and the
 *     allowance 91 is unused. (A finite fact at 2^20; no later depth follows.)
 *   - Why (measured, walk 0): the 32 rotated clocks spread apart (T - phi takes 1, 2, 8, 16, then 32 values) but they
 *     coalesce modulo the current period: 32, 16, 4, then 2 classes mod 32 by depth 100 .. 429, and 1 class after the
 *     period-32 entry. After coalescence a rotation shifts z by a constant, so every late interval has the same debt,
 *     and the early, pre-coalescence intervals never carry the maximum. This is the clock merging of GC922 .. GC926
 *     seen in the debt.
 *
 * ADDENDUM CW (the coalescence window identity; CL157). Hand lemma: for P-periodic drivers F_w is nondecreasing and
 *   F_w(t + P) = F_w(t) + P, so U_0 <= U_phi <= U_0 + P at every depth. If every U_phi = U_0 mod P at depth c, then
 *   z_phi - z_0 is constant from c on, and exactly D_phi = max(L(c), Dpre_phi(c), H_phi(c) + R(c)): L(c) is the
 *   phase-0 debt over intervals starting at or after c, R(c) = max over b >= c of z_0(b) - z_0(c), both phase-free;
 *   Dpre_phi(c) is the debt through c and H_phi(c) = z_phi(c) - min over a <= c of z_phi(a).
 * Record searched: "coalesc|merge" + "debt" -> 9 hits (GC312's merge tuples, RD16, GC655, board G8/G9): no window
 *   identity; "monoton|order-preserving|nondecreasing" + "clock" + "F_w|F(w" -> no hit.
 * PREDICTIONS, written 2026-10-10 03:53 BST (scratch copy first) before the check was coded; c = the first depth after
 *   the N5 entry at which all 32 clocks agree mod 32:
 *   W1 (control, 0.97): the identity holds exactly on all sixteen walks and 32 phases.
 *   W2 (control, 0.99): once coalesced after the entry, the clocks stay coalesced to 2^20.
 *   W3 (0.6): c - N5 <= 10,000 on every walk.
 *   U  (unexpected, 0.6): L(c) = D_0 on every walk (the worst interval starts after coalescence).
 * OUTCOME, 2026-10-10 03:54 BST: W1 PASS, W2 PASS, W3 HELD (c - N5 = 17 .. 232), U REFUTED: L(c) < D_0 on 11 of 16
 *   walks (both debts of 60 sit before c; L there is 36.5 and 40). So the maxima are mostly inherited from the
 *   period-16 stage, where the same lemma at P = 16 (clocks agree mod 16 by depth 429 on walk 0) makes them
 *   phase-free too. Phase dependence lives only in the short split windows after doublings (at most 232 steps here)
 *   and the first few hundred steps; on these histories it never reaches the maximum.
 */
#include <stdint.h>
#include <stdio.h>
#include <assert.h>
#define END (1LL << 20)
#define NP 32
static uint32_t rot(uint32_t x, int k) { k &= 31; return k ? (x >> k) | (x << (32 - k)) : x; }
static uint32_t child(uint32_t a, uint32_t b) {            /* copied from rule30_debt32.c */
  int t0 = __builtin_ctz(b), t = (t0 + 1) & 31; uint32_t c = 0, bit = ((a >> t0) & 1) ^ 1;
  for (int i = 0; i < 32; i++) { c |= bit << t; bit = ((a >> t) & 1) ^ (((b >> t) | bit) & 1); t = (t + 1) & 31; }
  return c;
}
static int isrot(uint32_t a, uint32_t b) { for (int k = 1; k < 32; k++) if (rot(a, k) == b) return 1; return 0; }
static int period(uint32_t a) { for (int p = 1; p < 32; p *= 2) if (rot(a, p) == a) return p; return 32; }
static int delay(uint32_t y, int64_t T) { return y ? __builtin_ctz(rot(y, T & 31)) + 1 : 0; }
typedef struct {
  uint32_t x, y;
  int64_t d, entry, T[NP], m[NP], D[NP], De[NP];
  int64_t c, Dp[NP], H[NP], z0c, Rmax, Lm, L;               /* CW: snapshot at coalescence c, then L and R */
  int stay;
} Walk;
static Walk walks[32];
static const int64_t ns[16] = {87867, 183184, 196189, 229338, 253537, 271596, 291257, 527724, 551910, 555813,
                               575211, 634886, 645655, 667052, 770532, 894235};
static const int64_t rd32[16] = {65, 80, 81, 87, 79, 79, 73, 79, 79, 79, 85, 80, 79, 90, 120, 120};  /* doubled */
static const int64_t probe[] = {1, 2, 4, 8, 100, 429, 5000, 87867, 200000, END - 1};

static int distinct(const int64_t *v) {
  int n = 0;
  for (int p = 0; p < NP; p++) { int seen = 0; for (int q = 0; q < p; q++) seen |= v[q] == v[p]; n += !seen; }
  return n;
}

int main(void) {
  int nw = 1, c2 = 1;
  int64_t maxall = 0, maxdev = 0;
  walks[0].y = 0xffffffffu;
  for (int p = 0; p < NP; p++) walks[0].T[p] = p;          /* clock started at phi; z(0) = 0, m = D = 0 */
  for (int i = 0; i < nw; i++) {
    Walk w = walks[i];
    while (w.d < END) {
      uint32_t c = 0; int fork = 0;
      if (w.y) c = child(w.x, w.y);
      else {
        assert(!w.entry);                                  /* no period-32 zero below the frontier (TM6) */
        uint32_t bit = 0; for (int t = 0; t < 32; t++) { c |= bit << t; bit ^= (w.x >> t) & 1; }
        if (!isrot(c, ~c)) fork = 1;
      }
      w.d++;
      for (int p = 0; p < NP; p++) {
        w.T[p] += delay(w.y, w.T[p]);
        int64_t z = 2 * (w.T[p] - p) - 5 * w.d;
        if (z - w.m[p] > w.D[p]) w.D[p] = z - w.m[p];
        if (z < w.m[p]) w.m[p] = z;
      }
      for (unsigned k = 0; i == 0 && k < sizeof probe / sizeof probe[0]; k++)
        if (w.d == probe[k]) {
          int64_t a[NP], b[NP];
          for (int p = 0; p < NP; p++) { a[p] = w.T[p] & 31; b[p] = w.T[p] - p; }
          printf("  walk 0, d = %lld: %d classes of T mod 32, %d values of T - phi, driver period %d\n",
                 (long long)w.d, distinct(a), distinct(b), period(w.y));
        }
      if (w.entry && w.c) {                                /* after coalescence: L, R on phase 0, and W2 */
        int64_t z0 = 2 * w.T[0] - 5 * w.d;
        if (z0 - w.Lm > w.L) w.L = z0 - w.Lm;
        if (z0 < w.Lm) w.Lm = z0;
        if (z0 - w.z0c > w.Rmax) w.Rmax = z0 - w.z0c;
        for (int p = 1; p < NP; p++) w.stay &= ((w.T[p] - w.T[0]) & 31) == 0;
      }
      if (w.entry && !w.c) {
        int all = 1;
        for (int p = 1; p < NP; p++) all &= ((w.T[p] - w.T[0]) & 31) == 0;
        if (all) {
          w.c = w.d; w.stay = 1; w.z0c = w.Lm = 2 * w.T[0] - 5 * w.d; w.L = w.Rmax = 0;
          for (int p = 0; p < NP; p++) {
            int64_t z = 2 * (w.T[p] - p) - 5 * w.d;
            w.Dp[p] = w.D[p]; w.H[p] = z - w.m[p];
          }
        }
      }
      if (!w.y && !fork && period(c) == 32) {
        w.entry = w.d;
        for (int p = 0; p < NP; p++) w.De[p] = w.D[p];
        for (int p = 0; p < 16; p++) c2 &= w.D[p] == w.D[p + 16];
      }
      if (fork) { assert(nw < 32); Walk o = w; o.x = 0; o.y = ~c; walks[nw++] = o; }
      w.x = w.y; w.y = c;
    }
    walks[i] = w;
  }
  assert(nw == 16);
  int c1 = 1, g = 1, above60 = 0, cw = 1;
  for (int i = 0; i < 16; i++) {
    Walk *w = &walks[i];
    int k = -1, arg = 0;
    for (int j = 0; j < 16; j++) if (ns[j] == w->entry) k = j;
    assert(k >= 0);
    c1 &= w->D[0] == rd32[k];
    int64_t mx = 0, mn = 1 << 30, emx = 0;
    for (int p = 0; p < NP; p++) {
      int64_t dv = w->D[p] > w->D[0] ? w->D[p] - w->D[0] : w->D[0] - w->D[p];
      if (dv > maxdev) maxdev = dv;
      g &= dv <= 62;                                       /* 31 in ordinary units */
      if (w->D[p] > mx) { mx = w->D[p]; arg = p; }
      if (w->D[p] < mn) mn = w->D[p];
      if (w->De[p] > emx) emx = w->De[p];
    }
    int ident = w->c > 0;
    for (int p = 0; p < NP; p++) {
      int64_t r = w->L;
      if (w->Dp[p] > r) r = w->Dp[p];
      if (w->H[p] + w->Rmax > r) r = w->H[p] + w->Rmax;
      ident &= r == w->D[p];
    }
    cw &= ident && w->stay;
    printf("  CW: c - N5 = %lld, identity %s, stays coalesced %s, L = %.1f vs D_0 = %.1f\n",
           (long long)(w->c - w->entry), ident ? "PASS" : "FAIL", w->stay ? "yes" : "NO", w->L / 2.0, w->D[0] / 2.0);
    if (mx > maxall) maxall = mx;
    above60 += mx > 120;
    printf("N5 = %6lld: D_0 = %4.1f, all-phase max %4.1f (phi = %2d), min %4.1f; through the entry max %4.1f, "
           "D_0 %4.1f\n", (long long)w->entry, w->D[0] / 2.0, mx / 2.0, arg, mn / 2.0, emx / 2.0, w->De[0] / 2.0);
  }
  printf("C1 %s, C2 %s, G %s (largest |D_phi - D_0| = %.1f); all-phase max %.1f; histories above 60: %d; "
         "2^20/(32 + max) = %.1f\n", c1 ? "PASS" : "FAIL", c2 ? "PASS" : "FAIL", g ? "HELD" : "REFUTED",
         maxdev / 2.0, maxall / 2.0, above60, 1048576.0 / (32 + maxall / 2.0));
  printf("CW %s (W1 identity and W2 stay-coalesced on all sixteen walks)\n", cw ? "PASS" : "FAIL");
  return !(c1 && c2 && g && cw);
}
