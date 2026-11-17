/* L1294 T18 (Local, 2026-11-02): every cycle of c_m(y) = y ^ ((y<<1) | (y<<2)) on m-bit rings (bits wrap), m = 1..MMAX.
   reports/rule30-genealogy.md section 29.3. Usage: ./ring_cycles MMAX   (MMAX <= 28; prints from m = MMIN, default 1)
   For each m: walk the functional graph from every state, colouring by walk; a walk that meets its own colour closes a
   cycle. Reports the number of cycles, the cycle lengths that are powers of two, and among those the primitive cycles
   (states with rotation period m), with a representative (bit i = cell i). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static int m; static uint32_t MK;
static inline uint32_t rotl(uint32_t y, int s) { s %= m; return s ? (((y << s) | (y >> (m - s))) & MK) : y; }
static inline uint32_t cm(uint32_t y) { return (y ^ (rotl(y, 1) | rotl(y, 2))) & MK; }
static int rotper(uint32_t y) { for (int d = 1; d < m; d++) if (m % d == 0 && rotl(y, d) == y) return d; return m; }
int main(int argc, char **argv) {
  int MMAX = atoi(argv[1]); int MMIN = argc > 2 ? atoi(argv[2]) : 1;
  for (m = MMIN; m <= MMAX; m++) {
    MK = (m == 32) ? 0xffffffffu : ((1u << m) - 1);
    uint32_t N = 1u << m;
    uint32_t *col = calloc(N, sizeof(uint32_t));             /* 0 = unvisited, else walk id */
    unsigned long ncyc = 0, n2 = 0, nprim2 = 0; unsigned long len2[33] = {0};
    uint32_t wid = 0;
    for (uint32_t s = 0; s < N; s++) {
      if (col[s]) continue;
      wid++;
      uint32_t y = s;
      while (!col[y]) { col[y] = wid; y = cm(y); }
      if (col[y] != wid) continue;                            /* ran into an older walk: no new cycle */
      uint32_t L = 1, z = cm(y);
      while (z != y) { L++; z = cm(z); }
      ncyc++;
      if ((L & (L - 1)) == 0) {
        n2++; int j = __builtin_ctz(L); len2[j]++;
        if (rotper(y) == m) {
          nprim2++;
          printf("  m=%d primitive cycle of length %u, representative ", m, L);
          for (int i = 0; i < m; i++) putchar('0' + ((y >> i) & 1));
          putchar('\n');
        }
      }
    }
    printf("m=%2d cycles %lu; of length 2^j: %lu (", m, ncyc, n2);
    int first = 1;
    for (int j = 0; j < 33; j++) if (len2[j]) { printf("%s2^%d:%lu", first ? "" : ", ", j, len2[j]); first = 0; }
    printf("); primitive of length 2^j: %lu\n", nprim2);
    fflush(stdout);
    free(col);
  }
  return 0;
}
