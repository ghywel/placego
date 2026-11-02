/* L1308 T30 (Local, 2026-11-02): rigid rotators of c^g, g = 1, 2, 4, as cycles of shift registers.
   reports/rule30-genealogy.md section 35. Build: cc -O2 -o rotators_g rotators_g.c
   Usage: ./rotators_g G DIR RMIN RMAX MAXBITS     (DIR: f = forward, b = backward)
   c(y)_i = y_i ^ (y_(i-1) | y_(i-2)); H_g(w) = bit 2g of c^g(w) for a (2g+1)-bit window w (bit j = y_(i-2g+j)),
   K_g = H_g ^ (bit 2g of w).
   forward  (c^g y)_n = y_(n-r):  y_n = y_(n-r) ^ K_g(y_(n-2g) .. y_(n-1)),  state = last r bits (a permutation).
   backward (c^g y)_n = y_(n+r):  y_n = H_g(y_(n-r-2g) .. y_(n-r)),           state = last r+2g bits (T22's form at g=1).
   Every cycle of length M is a ring of M cells on which c^g is a rotation. For cycles whose rotation order
   M/gcd(M, r mod M) is a power of two and M <= 4096, the ring is evolved under c to its least period P; if P >= 8, the
   tau-adic valuations of the M columns (time-rings of length P) are computed. A phase of least period P = 2L >= 8 is
   reported with its largest valuation and the number of columns of valuation exactly L/2 - 1 (the cycle lemma). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
static unsigned long gcdl(unsigned long a, unsigned long b) { while (b) { unsigned long t = a % b; a = b; b = t; } return a; }
static int Htab[1 << 9], Ktab[1 << 8];
static int val(uint8_t *c, int P) {          /* tau-adic valuation of a time-ring of length P (power of two) */
  static uint8_t e[1 << 15]; int k = 0;
  for (;;) {
    int any = 0, par = 0;
    for (int t = 0; t < P; t++) { any |= c[t]; par ^= c[t]; }
    if (!any) return P;
    if (par) return k;
    uint8_t acc = 0;
    for (int t = 0; t < P; t++) { e[t] = acc; acc ^= c[t]; }
    memcpy(c, e, P); k++;
  }
}
int main(int argc, char **argv) {
  int G = atoi(argv[1]); char DIR = argv[2][0]; int RMIN = atoi(argv[3]), RMAX = atoi(argv[4]), MAXB = atoi(argv[5]);
  int W = 2 * G + 1;
  for (int w = 0; w < (1 << W); w++) {
    uint32_t z = w;
    for (int s = 0; s < G; s++) z = (z ^ ((z << 1) | (z << 2))) & ((1u << W) - 1);
    Htab[w] = (z >> (2 * G)) & 1;
  }
  for (int w = 0; w < (1 << (2 * G)); w++) Ktab[w] = Htab[w] ^ 0;   /* window with y_n = 0: H = K */
  static uint8_t ring[4096], cur[4096], nxt[4096];
  static uint8_t hist[4096 * 64];                                    /* M * P <= 4096 * 64 entries kept */
  for (int r = RMIN; r <= RMAX; r++) {
    if (DIR == 'f' && r < 2 * G) continue;
    int B = (DIR == 'f') ? r : r + 2 * G;
    if (B > MAXB) break;
    uint32_t NS = 1u << B, mask = NS - 1;
    uint32_t *col = calloc(NS, sizeof(uint32_t)); uint32_t wid = 0;
    unsigned long ncyc = 0, npow = 0, nphase8 = 0; int printed = 0;
    for (uint32_t s0 = 0; s0 < NS; s0++) {
      if (col[s0]) continue;
      wid++; uint32_t s = s0;
#define STEP(st) ((DIR == 'f') ? ((((st) & 1) ^ Ktab[((st) >> (r - 2 * G)) & ((1u << (2 * G)) - 1)]) ) : (Htab[(st) & ((1u << W) - 1)]))
      while (!col[s]) { col[s] = wid; uint32_t y = STEP(s); s = ((s >> 1) | (y << (B - 1))) & mask; }
      if (col[s] != wid) continue;
      unsigned long M = 0; uint32_t z = s;
      do { uint32_t y = STEP(z); z = ((z >> 1) | (y << (B - 1))) & mask; M++; } while (z != s);
      ncyc++;
      unsigned long rr = r % M, ord = rr ? M / gcdl(M, rr) : 1;
      if (ord & (ord - 1)) continue;
      npow++;
      if (M > 4096) { printf("  g=%d %c r=%d: power-of-two rotation order %lu on a ring of %lu cells (too large to evolve)\n", G, DIR, r, ord, M); continue; }
      /* ring: the sequence y_0 .. y_(M-1) read off the cycle */
      z = s;
      for (unsigned long i = 0; i < M; i++) { ring[i] = z & 1; uint32_t y = STEP(z); z = ((z >> 1) | (y << (B - 1))) & mask; }
      /* the register reads bit 0 as the oldest cell; the ring index runs the same way */
      memcpy(cur, ring, M); int P = 0;
      for (int t = 1; t <= 64 * 4; t++) {
        for (unsigned long i = 0; i < M; i++) nxt[i] = cur[i] ^ (cur[(i + M - 1) % M] | cur[(i + M - 2) % M]);
        memcpy(cur, nxt, M);
        if (!memcmp(cur, ring, M)) { P = t; break; }
      }
      if (P == 0 || (P & (P - 1))) { printf("  g=%d %c r=%d M=%lu: rotation order %lu but period %d under c\n", G, DIR, r, M, ord, P); continue; }
      if (P < 8) continue;
      if ((unsigned long)P * M > sizeof hist) { printf("  g=%d %c r=%d M=%lu P=%d: too large to analyse\n", G, DIR, r, M, P); continue; }
      memcpy(cur, ring, M);
      for (int t = 0; t < P; t++) {
        for (unsigned long i = 0; i < M; i++) hist[i * P + t] = cur[i];
        for (unsigned long i = 0; i < M; i++) nxt[i] = cur[i] ^ (cur[(i + M - 1) % M] | cur[(i + M - 2) % M]);
        memcpy(cur, nxt, M);
      }
      int L = P / 2, vmax = -1, nfront = 0, nlow = 0; static uint8_t colbuf[1 << 15];
      for (unsigned long i = 0; i < M; i++) {
        memcpy(colbuf, hist + i * P, P); int v = val(colbuf, P);
        if (v < L) nlow++;
        if (v > vmax && v < P) vmax = v;
        if (v == L / 2 - 1) nfront++;
      }
      if (P == 8 && M % 4 == 0) { nphase8++; continue; }   /* G8 and its lifts, summarised */
      if (printed < 6) {
        printf("  g=%d %c r=%d PHASE: ring %lu cells, least period P=%d, columns of least period P: %d, largest valuation %d, columns at L/2-1=%d: %d %s\n",
               G, DIR, r, M, P, nlow, vmax, L / 2 - 1, nfront, nfront ? "" : "<- CYCLE LEMMA FAILS");
        if (M <= 512) { printf("    ring "); for (unsigned long i = 0; i < M; i++) putchar('0' + ring[i]); putchar('\n'); }
        printed++;
      }
    }
    printf("g=%d %c r=%2d: states 2^%d, cycles %lu, power-of-two rotation order %lu, G8-type (P=8, 4|M) %lu\n", G, DIR, r, B, ncyc, npow, nphase8);
    fflush(stdout); free(col);
  }
  return 0;
}
