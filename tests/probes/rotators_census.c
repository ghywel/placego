/* L1309 T31 (Local, 2026-11-02): extended census of rigid rotators c^g = rho^r (g = 1, 2, 4) as shift-register
   cycles, with bitsets. reports/rule30-genealogy.md section 36. Build: cc -O2 -o rotators_census rotators_census.c
   Usage: ./rotators_census G DIR RMIN RMAX MAXBITS OUTDIR
   Registers as in rotators_g.c (forward: a permutation of r-bit states when r > 2g, so r = 2g is left to rotators_g.c;
   backward: r+2g bits, not a permutation).
   Every cycle whose rotation order M/gcd(M, r mod M) is a power of two is evolved under c on its ring (up to 2^14
   steps and M*P <= 2^27 cell-steps) to its least period P. Rings with P >= 16 are written to OUTDIR as
   ring_g<G><DIR>_r<r>_M<M>_P<P>.txt (one line of 0/1, cell i = character i), for analysis by rotators_census.py. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
static unsigned long gcdl(unsigned long a, unsigned long b) { while (b) { unsigned long t = a % b; a = b; b = t; } return a; }
static int Htab[1 << 9], Ktab[1 << 8];
static int G, R, B, W; static char DIR; static uint64_t MASK;
static inline uint64_t step(uint64_t s) {
  uint64_t y = (DIR == 'f') ? ((s & 1) ^ Ktab[(s >> (R - 2 * G)) & ((1u << (2 * G)) - 1)]) : Htab[s & ((1u << W) - 1)];
  return ((s >> 1) | (y << (B - 1))) & MASK;
}
#define GETB(a, i) ((a[(i) >> 6] >> ((i) & 63)) & 1)
#define SETB(a, i) (a[(i) >> 6] |= 1ULL << ((i) & 63))
#define CLRB(a, i) (a[(i) >> 6] &= ~(1ULL << ((i) & 63)))
int main(int argc, char **argv) {
  G = atoi(argv[1]); DIR = argv[2][0]; int RMIN = atoi(argv[3]), RMAX = atoi(argv[4]), MAXB = atoi(argv[5]);
  const char *OUT = argv[6]; W = 2 * G + 1;
  for (int w = 0; w < (1 << W); w++) {
    uint32_t z = w;
    for (int s = 0; s < G; s++) z = (z ^ ((z << 1) | (z << 2))) & ((1u << W) - 1);
    Htab[w] = (z >> (2 * G)) & 1;
  }
  for (int w = 0; w < (1 << (2 * G)); w++) Ktab[w] = Htab[w];
  uint8_t *ring = malloc(1 << 20), *cur = malloc(1 << 20), *nxt = malloc(1 << 20);
  for (R = RMIN; R <= RMAX; R++) {
    if (DIR == 'f' && R < 2 * G + 1) continue;   /* the forward register is a permutation only for r > 2g */
    B = (DIR == 'f') ? R : R + 2 * G;
    if (B > MAXB) break;
    uint64_t NS = 1ULL << B; MASK = NS - 1;
    uint64_t *vis = calloc(NS / 64 + 1, 8), *onp = (DIR == 'f') ? NULL : calloc(NS / 64 + 1, 8);
    unsigned long ncyc = 0, npow = 0, nwritten = 0, nbig = 0;
    for (uint64_t s0 = 0; s0 < NS; s0++) {
      if (GETB(vis, s0)) continue;
      uint64_t s = s0, cyc_start; int newcycle = 0;
      if (DIR == 'f') {                                  /* permutation: s0 lies on a cycle */
        newcycle = 1; cyc_start = s0;
        do { SETB(vis, s); s = step(s); } while (s != s0);
      } else {
        while (!GETB(vis, s)) { SETB(vis, s); SETB(onp, s); s = step(s); }
        if (GETB(onp, s)) { newcycle = 1; cyc_start = s; }
        uint64_t t = s0; while (GETB(onp, t)) { CLRB(onp, t); t = step(t); }
      }
      if (!newcycle) continue;
      unsigned long M = 0; uint64_t z = cyc_start;
      do { z = step(z); M++; } while (z != cyc_start);
      ncyc++;
      unsigned long rr = R % M, ord = rr ? M / gcdl(M, rr) : 1;
      if (ord & (ord - 1)) continue;
      npow++;
      if (M > (1UL << 20)) { nbig++; printf("  g=%d %c r=%d: power-of-two rotation order %lu on a ring of %lu cells (not evolved)\n", G, DIR, R, ord, M); continue; }
      z = cyc_start;
      for (unsigned long i = 0; i < M; i++) { ring[i] = z & 1; z = step(z); }
      memcpy(cur, ring, M); long P = 0; long maxsteps = (1L << 27) / (long)M; if (maxsteps > 16384) maxsteps = 16384;
      for (long t = 1; t <= maxsteps; t++) {
        for (unsigned long i = 0; i < M; i++) nxt[i] = cur[i] ^ (cur[(i + M - 1) % M] | cur[(i + M - 2) % M]);
        memcpy(cur, nxt, M);
        if (!memcmp(cur, ring, M)) { P = t; break; }
      }
      if (P == 0) { printf("  g=%d %c r=%d M=%lu: period above %ld steps (rotation order %lu)\n", G, DIR, R, M, maxsteps, ord); nbig++; continue; }
      if (P & (P - 1)) { printf("  g=%d %c r=%d M=%lu: period %ld is not a power of two\n", G, DIR, R, M, P); continue; }
      if (P < 16) continue;
      char fn[512]; snprintf(fn, sizeof fn, "%s/ring_g%d%c_r%d_M%lu_P%ld.txt", OUT, G, DIR, R, M, P);
      FILE *f = fopen(fn, "w");
      for (unsigned long i = 0; i < M; i++) fputc('0' + ring[i], f);
      fputc('\n', f); fclose(f); nwritten++;
    }
    printf("g=%d %c r=%2d: states 2^%d, cycles %lu, power-of-two rotation order %lu, rings with P>=16 written %lu, not evolved %lu\n",
           G, DIR, R, B, ncyc, npow, nwritten, nbig);
    fflush(stdout); free(vis); free(onp);
  }
  return 0;
}
