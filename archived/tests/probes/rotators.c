/* L1294 T22 (Local, 2026-11-02): every cycle of the shift register y_n = y_(n-r) ^ (y_(n-r-1) | y_(n-r-2)),
   r = RMIN..RMAX (<= 24). reports/rule30-genealogy.md section 29.10. Usage: ./rotators RMIN RMAX
   State s: bit i = y_(n-r-2+i), i = 0..r+1. A cycle of period m is a rigid rotator on m cells (c_m rotates it by r).
   Reported: per r, the number of cycles; and every cycle with L = m / gcd(m, r) a power of two (a light-speed glider),
   with m, L and the sequence for m <= 256. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static unsigned long gcdl(unsigned long a, unsigned long b) { while (b) { unsigned long t = a % b; a = b; b = t; } return a; }
int main(int argc, char **argv) {
  int RMIN = atoi(argv[1]), RMAX = atoi(argv[2]);
  for (int r = RMIN; r <= RMAX; r++) {
    int B = r + 2; uint32_t N = 1u << B;
    uint32_t *col = calloc(N, sizeof(uint32_t)); uint32_t wid = 0; unsigned long ncyc = 0, nglide = 0;
    for (uint32_t s0 = 0; s0 < N; s0++) {
      if (col[s0]) continue;
      wid++; uint32_t s = s0;
      while (!col[s]) {
        col[s] = wid;
        uint32_t y = ((s >> 2) & 1) ^ (((s >> 1) & 1) | (s & 1));
        s = (s >> 1) | (y << (B - 1));
      }
      if (col[s] != wid) continue;
      unsigned long m = 0; uint32_t z = s;
      do { uint32_t y = ((z >> 2) & 1) ^ (((z >> 1) & 1) | (z & 1)); z = (z >> 1) | (y << (B - 1)); m++; } while (z != s);
      ncyc++;
      unsigned long L = m / gcdl(m, r % m ? r % m : m);
      if (r % m == 0) L = 1;
      if ((L & (L - 1)) == 0) {
        nglide++;
        printf("  r=%d glider: m=%lu L=%lu", r, m, L);
        if (m <= 256) {
          printf(" seq=");
          uint32_t q = s;
          for (unsigned long i = 0; i < m; i++) { putchar('0' + (q & 1)); uint32_t y = ((q >> 2) & 1) ^ (((q >> 1) & 1) | (q & 1)); q = (q >> 1) | (y << (B - 1)); }
        }
        putchar('\n');
      }
    }
    printf("r=%2d cycles %lu, light-speed gliders %lu\n", r, ncyc, nglide);
    fflush(stdout);
    free(col);
  }
  return 0;
}
