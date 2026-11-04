/* T-D (Local, L1520): clouds in the rain. A row is odd, with its top wall (highest k >= 1 with R_k = R_(k+1)) at most TOP and rain above,
   held in 64 bits. Checks that Phi and Phi^-1 keep a rain tail inside the window, and tallies how far the top moves. */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static u64 phi(u64 x) { return x ^ ((x << 1) | (x << 2)); }
static u64 inv(u64 y) { u64 x = y & 1; for (int j = 1; j < 64; j++) { u64 a = (x >> (j - 1)) & 1, b = j >= 2 ? (x >> (j - 2)) & 1 : 0; x |= (((y >> j) & 1) ^ (a | b)) << j; } return x; }
static int top(u64 x) { /* highest k in 1..61 with equal adjacent bits, or 0 if none */
  u64 e = ~(x ^ (x >> 1)); e &= ((1ULL << 62) - 1); e &= ~1ULL; return e ? 63 - __builtin_clzll(e) : 0; }
int main(int argc, char **argv) { int TOP = atoi(argv[1]); long hf[16] = {0}, hb[16] = {0}; long bad = 0, none = 0; int mn = 99, mx = -99, mnb = 99, mxb = -99;
  for (u64 m = 0; m < (1ULL << TOP); m++) { /* bits 1..TOP free, bit TOP+1 onward alternate after bit TOP */
    u64 x = 1 | (m << 1); int b = (m >> (TOP - 1)) & 1; for (int j = TOP + 1; j < 64; j++) { b ^= 1; if (b) x |= 1ULL << j; }
    /* make sure a wall may sit at TOP by also trying both continuations */
    for (int c = 0; c < 2; c++) { u64 z = c ? (x ^ (~0ULL << (TOP + 1))) : x; int d = top(z); if (d == 0) { none++; continue; }
      if (d > TOP) continue;
      /* the top three window bits are polluted by truncation only above bit 61 */
      int f = top(phi(z)), g = top(inv(z));
      if (f > TOP + 8 || g > TOP + 8) bad++;
      int df = f - d, dg = g - d; if (df < mn) mn = df; if (df > mx) mx = df; if (dg < mnb) mnb = dg; if (dg > mxb) mxb = dg;
      if (df >= -7 && df <= 8) hf[df + 7]++; if (dg >= -7 && dg <= 8) hb[dg + 7]++; } }
  printf("clouds with top <= %d: tail left the window %ld times; no wall (rain) %ld rows\n", TOP, bad, none);
  printf("forward top change min %d max %d; backward top change min %d max %d\n", mn, mx, mnb, mxb);
  printf("forward:"); for (int i = 0; i < 16; i++) if (hf[i]) printf(" %+d:%ld", i - 7, hf[i]); printf("\nbackward:"); for (int i = 0; i < 16; i++) if (hb[i]) printf(" %+d:%ld", i - 7, hb[i]); printf("\n");
  return 0; }
