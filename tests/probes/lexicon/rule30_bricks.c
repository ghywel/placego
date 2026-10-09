/* rule30_bricks.c: the brick that the forced left half of a periodic column pair freezes into.
   Cloud, 2026-10-09; driven by rule30_cloud_bricks.py, which holds the predictions and the outcome.

   Column 0 is the wall 0101.. (white at even times) and column 1 a word w of length P (P even), both P-periodic.
   Rule 30 run sideways, x_t(i-1) = x_{t+1}(i) XOR (x_t(i) OR x_t(i+1)), maps the pair (c_i, c_{i+1}) of P-periodic
   columns to (c_{i-1}, c_i). That is a map on 2^(2P) states, so the left half is eventually periodic in i as well as
   in t: from some depth on it is a wallpaper of one P x Q brick. Brent's algorithm finds the transient mu (the depth
   where the wallpaper starts) and the cycle length Q. On the cycle we also find the least q with
   Phi^q(s) = (both columns turned by r steps in time), the staggered brick: Q' columns wide, the next one r steps
   lower, as in a brick wall.

   usage: rule30_bricks P [W]   all words of length P (or the single word W, in binary, bit t = time t)
   prints one line per word: w mu Q Qs r dens maxzero blank brick-id, then one BRICK line per distinct brick (up
   to time-rotation) and a summary. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

static int P; static uint32_t M;
static inline uint32_t rotr(uint32_t a, int r) { r %= P; return r ? ((a >> r) | (a << (P - r))) & M : a; }
/* state packs (a, b) = (c_i, c_{i+1}) as a | b << P */
static inline uint64_t phi(uint64_t s) {
  uint32_t a = s & M, b = (s >> P) & M;
  uint32_t l = rotr(a, 1) ^ (a | b);                         /* l_t = a_{t+1} XOR (a_t OR b_t) */
  return (uint64_t)l | ((uint64_t)a << P);
}

/* every state of every brick found so far, with all its time-rotations, maps to the brick's id */
static uint64_t *hk; static int *hv; static size_t hcap, hn; static int nbricks;
static uint64_t bq[1 << 16], blam[1 << 16], bmin[1 << 16]; static long bwords[1 << 16]; static int br_[1 << 16];
static double bdens[1 << 16];
static size_t hslot(uint64_t k) { size_t i = (size_t)((k * 0x9E3779B97F4A7C15ull) >> 20) & (hcap - 1);
  while (hk[i] != UINT64_MAX && hk[i] != k) i = (i + 1) & (hcap - 1);
  return i; }
static void hput(uint64_t k, int v);
static void hgrow(void) {
  uint64_t *ok = hk; int *ov = hv; size_t oc = hcap;
  hcap = hcap ? hcap * 2 : 1 << 16; hk = malloc(hcap * sizeof *hk); hv = malloc(hcap * sizeof *hv); hn = 0;
  for (size_t i = 0; i < hcap; i++) hk[i] = UINT64_MAX;
  for (size_t i = 0; i < oc; i++) if (ok[i] != UINT64_MAX) hput(ok[i], ov[i]);
  free(ok); free(ov);
}
static void hput(uint64_t k, int v) { if (2 * (hn + 1) > hcap) hgrow(); size_t i = hslot(k);
  if (hk[i] == UINT64_MAX) { hk[i] = k; hv[i] = v; hn++; } }
static int hget(uint64_t k) { if (!hcap) return -1; size_t i = hslot(k); return hk[i] == k ? hv[i] : -1; }
static inline uint64_t rotstate(uint64_t s, int r) {
  return (uint64_t)rotr(s & M, r) | ((uint64_t)rotr((s >> P) & M, r) << P);
}

static void one(uint32_t w, long *stats) {
  uint32_t wall = 0;
  for (int t = 0; t < P; t++) if (t & 1) wall |= 1u << t;
  uint64_t x0 = (uint64_t)wall | ((uint64_t)w << P);
  /* Brent */
  uint64_t pw = 1, lam = 1, tort = x0, hare = phi(x0);
  while (tort != hare) { if (pw == lam) { tort = hare; pw <<= 1; lam = 0; } hare = phi(hare); lam++; }
  tort = hare = x0;
  for (uint64_t k = 0; k < lam; k++) hare = phi(hare);
  uint64_t mu = 0;
  while (tort != hare) { tort = phi(tort); hare = phi(hare); mu++; }
  /* tort is the first state on the cycle, at depth mu (its a is column -mu) */
  uint64_t s = tort, best_q = lam; int best_r = 0;
  for (int m = 2; m <= P; m++) {                            /* candidate staggers q = lam / m */
    if (lam % m) continue;
    uint64_t q = lam / m, y = s;
    if (q >= best_q) continue;
    for (uint64_t k = 0; k < q; k++) y = phi(y);
    for (int r = 1; r < P; r++) {
      uint32_t a = s & M, b = (s >> P) & M;
      if (((uint64_t)rotr(a, r) | ((uint64_t)rotr(b, r) << P)) == y) { best_q = q; best_r = r; break; }
    }
  }
  /* density of the brick, blankness, and the longest zero run along any row, over depths 1 .. mu + 2 lam */
  long ones = 0; int blank = 1, run[64], maxz = 0;
  memset(run, 0, sizeof run);
  uint64_t y = phi(x0);                                     /* a = column -1 */
  for (uint64_t k = 1; k <= mu + 2 * lam; k++) {
    uint32_t a = y & M;
    for (int t = 0; t < P; t++) {
      if ((a >> t) & 1) run[t] = 0; else { run[t]++; if (run[t] > maxz) maxz = run[t]; }
    }
    if (k > mu && k <= mu + lam) { ones += __builtin_popcount(a); if (a) blank = 0; }
    y = phi(y);
  }
  for (int t = 0; t < P; t++) if ((uint64_t)run[t] >= 2 * lam) maxz = 1 << 30;   /* a row white for ever */
  int id = hget(s);
  if (id < 0) {                                              /* a new brick: record its states and rotations */
    id = nbricks++;
    uint64_t y2 = s, mn = UINT64_MAX;
    for (uint64_t k = 0; k < lam; k++) {
      for (int r = 0; r < P; r++) { uint64_t z = rotstate(y2, r); hput(z, id); if (z < mn) mn = z; }
      y2 = phi(y2);
    }
    bq[id] = best_q; blam[id] = lam; bmin[id] = mn; br_[id] = best_r; bdens[id] = (double)ones / (double)(lam * P);
  }
  bwords[id]++;
  printf("%u %llu %llu %llu %d %.4f %d %d %d\n", w, (unsigned long long)mu, (unsigned long long)lam,
         (unsigned long long)best_q, best_r, (double)ones / (double)(lam * P), maxz, blank, id);
  stats[0]++; if (blank) stats[1]++; if (maxz > 2 * P - 2) stats[2]++;
}

int main(int argc, char **argv) {
  if (argc < 2) { fprintf(stderr, "usage: rule30_bricks P [W]\n"); return 2; }
  P = atoi(argv[1]); M = P == 32 ? UINT32_MAX : (1u << P) - 1;
  if (P < 2 || P > 30 || P % 2) { fprintf(stderr, "P must be even, 2 .. 30\n"); return 2; }
  long stats[3] = {0, 0, 0};
  if (argc >= 3) {
    uint32_t w = 0; const char *b = argv[2];
    for (int t = 0; b[t] && t < P; t++) if (b[t] == '1') w |= 1u << t;
    one(w, stats);
  } else
    for (uint32_t w = 0; w <= M; w++) { one(w, stats); if (w == M) break; }
  for (int b = 0; b < nbricks; b++)
    printf("BRICK id=%d Q=%llu Qs=%llu r=%d dens=%.4f words=%ld a=%llx b=%llx\n", b, (unsigned long long)blam[b],
           (unsigned long long)bq[b], br_[b], bdens[b], bwords[b], (unsigned long long)(bmin[b] & M),
           (unsigned long long)(bmin[b] >> P));
  printf("SUM P=%d words=%ld blank=%ld zero_run_over_2P-2=%ld bricks=%d\n", P, stats[0], stats[1], stats[2],
         nbricks);
  return 0;
}
