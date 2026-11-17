/* L1294 T20 (Local, 2026-11-02): the bi-infinite core of the full pair graph at p = 16 (all 2^32 states).
   reports/rule30-genealogy.md section 29.3. Usage: ./lightspeed_core   (compile with -DP=8 for the p = 8 cross-check; P >= 8)
   State (u, v), 16-bit time-rings; edges (u, v) -> (v, w), w = running XOR of u | v from w(0) in {0, 1}, iff |u | v|
   is even. Storage: bit v of row u. Repeat until stable: forward trim (keep states with a kept successor; successors of
   (u, v) lie in row v) and backward trim (keep states with a kept predecessor). Then Tarjan on the core.
   Output: rounds, core size, each cyclic component (size, kind), and the acyclic core states. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#ifndef P
#define P 16
#endif
#define NR (1u << P)
#define RW (NR / 64)                               /* uint64 words per row */
#define MK (NR - 1)
typedef uint64_t u64;
static u64 *S, *T, *R;                             /* NR rows x RW words, 512 MiB each */
static inline int getb(const u64 *X, uint32_t r, uint32_t c) { return (X[(size_t)r * RW + (c >> 6)] >> (c & 63)) & 1; }
static inline void setb(u64 *X, uint32_t r, uint32_t c) { X[(size_t)r * RW + (c >> 6)] |= 1ULL << (c & 63); }
static inline uint32_t integ(uint32_t d) {
  uint32_t y = d; for (int s = 1; s < P; s <<= 1) y ^= (y << s) & MK; return (y << 1) & MK;
}
static void tr64(u64 a[64]) {                      /* in-place 64x64 bit transpose (Hacker's Delight style) */
  u64 m = 0x00000000ffffffffULL;
  for (int j = 32; j; j >>= 1, m ^= m << j)
    for (int k = 0; k < 64; k = ((k | j) + 1) & ~j) {
      u64 t = ((a[k] >> j) ^ a[k | j]) & m;
      a[k] ^= t << j; a[k | j] ^= t;
    }
}
static void transpose(const u64 *X, u64 *Y) {      /* Y[c][r] = X[r][c] */
  u64 blk[64];
  for (uint32_t rb = 0; rb < NR / 64; rb++)
    for (uint32_t cb = 0; cb < RW; cb++) {
      for (int i = 0; i < 64; i++) blk[i] = X[(size_t)(rb * 64 + i) * RW + cb];
      tr64(blk);
      for (int i = 0; i < 64; i++) Y[(size_t)(cb * 64 + i) * RW + rb] = blk[i];
    }
}
static unsigned long long count(const u64 *X) {
  unsigned long long c = 0; for (size_t i = 0; i < (size_t)NR * RW; i++) c += __builtin_popcountll(X[i]); return c;
}
int main(void) {
  size_t bytes = (size_t)NR * RW * sizeof(u64);
  S = malloc(bytes); T = malloc(bytes); R = malloc(bytes);
  if (!S || !T || !R) { fprintf(stderr, "oom\n"); return 3; }
  memset(S, 0, bytes);
  for (uint32_t u = 0; u < NR; u++) for (uint32_t v = 0; v < NR; v++) if (!(__builtin_popcount(u | v) & 1)) setb(S, u, v);
  unsigned long long n = count(S), prev = 0; int rounds = 0;
  printf("states with even OR: %llu\n", n); fflush(stdout);
  /* the check (popcount isolated self-test of the transpose) */
  transpose(S, T); transpose(T, R);
  if (memcmp(S, R, bytes)) { fprintf(stderr, "transpose self-test failed\n"); return 4; }
  while (n != prev) {
    prev = n; rounds++;
    /* forward: R[v][u] = (u, v) alive and some successor (v, w) alive */
    transpose(S, T); memset(R, 0, bytes);
    for (uint32_t v = 0; v < NR; v++) {
      const u64 *tr = T + (size_t)v * RW;
      for (uint32_t wd = 0; wd < RW; wd++) {
        u64 x = tr[wd];
        while (x) {
          uint32_t u = wd * 64 + __builtin_ctzll(x); x &= x - 1;
          uint32_t w0 = integ(u | v);
          if (getb(S, v, w0) | getb(S, v, w0 ^ MK)) setb(R, v, u);
        }
      }
    }
    transpose(R, S);                               /* S = forward-trimmed set */
    /* backward: keep (v, w) iff some alive (u, v) has it as a successor */
    transpose(S, T); memset(R, 0, bytes);
    for (uint32_t v = 0; v < NR; v++) {
      const u64 *tr = T + (size_t)v * RW;
      for (uint32_t wd = 0; wd < RW; wd++) {
        u64 x = tr[wd];
        while (x) {
          uint32_t u = wd * 64 + __builtin_ctzll(x); x &= x - 1;
          uint32_t w0 = integ(u | v);
          setb(R, v, w0); setb(R, v, w0 ^ MK);
        }
      }
    }
    for (size_t i = 0; i < (size_t)NR * RW; i++) S[i] &= R[i];
    n = count(S);
    printf("round %d: core candidates %llu\n", rounds, n); fflush(stdout);
  }
  /* extract the core and run Tarjan */
  uint32_t *st = malloc(n * sizeof(uint32_t)); size_t k = 0;
  for (uint32_t u = 0; u < NR; u++) for (uint32_t wd = 0; wd < RW; wd++) {
    u64 x = S[(size_t)u * RW + wd];
    while (x) { uint32_t v = wd * 64 + __builtin_ctzll(x); x &= x - 1; st[k++] = (u << P) | v; }
  }
  printf("core states: %zu\n", k);
  for (size_t i = 0; i < k; i++) {
    uint32_t u = st[i] >> P, v = st[i] & MK, w0 = integ(u | v);
    int a0 = getb(S, v, w0), a1 = getb(S, v, w0 ^ MK);
    printf("  (u, v) = (%05x, %05x) -> %s%s\n", u, v, a0 ? "w0 " : "", a1 ? "notw0" : "");
  }
  return 0;
}
