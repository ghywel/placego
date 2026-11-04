/* Capture (Local, L1521): for every cloud with top <= W, the number of backward ticks until the top window lies in the robust set B_w.
   Row: bit 0 black, bits 1..W+1 free, rain above, 128 bits. Usage: ./capture W w Bfile limit */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned __int128 u128; typedef unsigned long long u64;
static unsigned char *B; static int w;
static u128 inv(u128 y) { u128 x = y & 1; int p1 = 1, p2 = 0; for (int j = 1; j < 128; j++) { int o = (int)((y >> j) & 1) ^ (p1 | p2); x |= (u128)o << j; p2 = p1; p1 = o; } return x; }
static int top(u128 x) { u128 e = ~(x ^ (x >> 1)); e &= (((u128)1 << 126) - 1); e &= ~(u128)1; u64 h = (u64)(e >> 64); if (h) return 127 - __builtin_clzll(h); u64 l = (u64)e; return l ? 63 - __builtin_clzll(l) : 0; }
int main(int c, char **v) { int W = atoi(v[1]); w = atoi(v[2]); B = calloc(1 << w, 1); FILE *f = fopen(v[3], "r"); unsigned m; long nb = 0; while (fscanf(f, "%u", &m) == 1) { B[m] = 1; nb++; } int L = atoi(v[4]);
  long hist[200] = {0}; int best = -1; u128 bx = 0; long total = 0, rain = 0, over = 0;
  for (u64 m0 = 0; m0 < (1ULL << (W + 1)); m0++) { u128 x = 1 | ((u128)m0 << 1); int b = (m0 >> W) & 1; for (int j = W + 2; j < 128; j++) { b ^= 1; if (b) x |= (u128)1 << j; }
    int d = top(x); if (d == 0) { rain++; continue; } if (d > W) continue; total++;
    u128 y = x; int t = 0; for (;;) { int dd = top(y); if (dd + 2 >= w) { unsigned win = (unsigned)((y >> (dd + 2 - w)) & ((1u << w) - 1)); if (B[win]) break; } if (t >= L || dd > 112) { over++; t = 199; break; } y = inv(y); t++; }
    hist[t]++; if (t > best && t < 199) { best = t; bx = x; } }
  printf("W=%d w=%d |B|=%ld clouds %ld rain rows %ld unresolved %ld; longest capture %d at row %llx\n", W, w, nb, total, rain, over, best, (u64)bx & ((1ULL<<(W+3))-1));
  printf("capture-time counts:"); for (int i = 0; i < 199; i++) if (hist[i]) printf(" %d:%ld", i, hist[i]); printf("\n"); return 0; }
