// ring_census.c: the complete functional graph of Rule 30 on the ring of n cells, n = 1 .. NMAX (<= 28). For each n:
// the number of cycles, the states on cycles, the maximum period, the period reached from the single cell, the
// longest transient, the number of gliding cycles (cycles mapped to themselves by rotation), and the cycle lengths
// with multiplicities. Every state is visited once; the cycles are found exactly (certificates: one state and the
// length per cycle, printed for the longest). Local, 2026-10-06; CONSTELLATION.md row 10; RULE30-PRIZE.md 8.67;
// driver rule30_ring_census.py.
// Usage: ring_census NMAX [NMIN=1]      (memory about 24 * 2^n bytes: 12 GB at n = 29)
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static inline uint32_t step(uint32_t x, int n, uint32_t mask) {
    uint32_t l = ((x << 1) | (x >> (n - 1))) & mask;     /* left neighbour of cell i is cell i-1: rotate */
    uint32_t r = ((x >> 1) | (x << (n - 1))) & mask;
    return (l ^ (x | r)) & mask;
}
static inline uint32_t rot(uint32_t x, int n, uint32_t mask) { return ((x << 1) | (x >> (n - 1))) & mask; }

int main(int argc, char **argv) {
    int nmax = argc > 1 ? atoi(argv[1]) : 24, nmin = argc > 2 ? atoi(argv[2]) : 1;
    for (int n = nmin; n <= nmax; n++) {
        uint32_t N = (uint32_t)1 << n, mask = N - 1;
        /* Two arrays per state (8 bytes, 4 GiB at n = 29; the first version used four and thrashed a 16 GB machine):
           A[x] = 0 unvisited; = the walk's tag (s + 1 < 2^31) while x is on the current walk; = FIN | cycle id once done.
           B[x] = position on the current walk, then the preperiod once done. */
        const uint32_t FIN = 0x80000000u;
        uint32_t *A = calloc(N, 4), *B = calloc(N, 4);
        uint32_t cap = 1024, *clen = malloc(4 * cap), *crep = malloc(4 * cap);
        uint32_t ncyc = 0, periodic = 0, maxper = 0, maxtr = 0, single = 0;
        for (uint32_t s = 0; s < N; s++) {
            if (A[s]) continue;
            uint32_t cur = s + 1, x = s, len = 0;
            while (!A[x]) { A[x] = cur; B[x] = len++; x = n == 1 ? step(x, 1, 1) : step(x, n, mask); }
            if (A[x] == cur) {                               /* a new cycle: walk positions B[x] .. len-1 */
                uint32_t posx = B[x], L = len - posx;
                if (ncyc == cap) { cap *= 2; clen = realloc(clen, 4 * cap); crep = realloc(crep, 4 * cap); }
                clen[ncyc] = L; crep[ncyc] = x; ncyc++;
                periodic += L; if (L > maxper) maxper = L;
                uint32_t y = x;
                for (uint32_t i = 0; i < L; i++) { B[y] = 0; A[y] = FIN | ncyc; y = step(y, n, mask); }
                uint32_t z = s;                              /* the walk's tail: positions 0 .. posx-1 */
                for (uint32_t i = 0; i < posx; i++) { B[z] = posx - i; A[z] = FIN | ncyc; if (B[z] > maxtr) maxtr = B[z]; z = step(z, n, mask); }
            } else {                                         /* the walk ran into a finished node */
                uint32_t base = B[x], c = A[x] & ~FIN, z = s;
                for (uint32_t i = 0; i < len; i++) { B[z] = base + len - i; A[z] = FIN | c; if (B[z] > maxtr) maxtr = B[z]; z = step(z, n, mask); }
            }
        }
        single = clen[(A[1] & ~FIN) - 1];
        /* gliding cycles: rotation by one maps the cycle to itself */
        uint32_t gliding = 0;
        for (uint32_t c = 0; c < ncyc; c++) if ((A[rot(crep[c], n, mask)] & ~FIN) == c + 1) gliding++;
        /* length histogram: distinct lengths with multiplicities, the five largest */
        printf("n %d cycles %u periodic %u maxper %u single %u maxtransient %u gliding %u\n", n, ncyc, periodic, maxper, single, maxtr, gliding);
        /* sort lengths descending (small arrays except for tiny n with many fixed points) */
        uint32_t *sorted = malloc(4 * ncyc); memcpy(sorted, clen, 4 * ncyc);
        for (uint32_t i = 1; i < ncyc; i++) { uint32_t v = sorted[i]; uint32_t j = i; while (j && sorted[j - 1] < v) { sorted[j] = sorted[j - 1]; j--; } sorted[j] = v; }
        printf("  lengths");
        uint32_t shown = 0;
        for (uint32_t i = 0; i < ncyc && shown < 8;) {
            uint32_t j = i; while (j < ncyc && sorted[j] == sorted[i]) j++;
            printf(" %u", sorted[i]); if (j - i > 1) printf("x%u", j - i);
            i = j; shown++;
        }
        if (shown == 8) printf(" ...");
        /* certificate of the longest cycle: one state on it */
        for (uint32_t c = 0; c < ncyc; c++) if (clen[c] == maxper) { printf("  longest from state %u", crep[c]); break; }
        printf("\n"); fflush(stdout);
        free(A); free(B); free(clen); free(crep); free(sorted);
    }
    return 0;
}
