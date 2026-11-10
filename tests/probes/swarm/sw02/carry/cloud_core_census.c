/* Cloud CL771: the two-sided core of the pair graph at temporal period P (P <= 15), by full census.
   A vertex is a pair (c, d) of P-tick profiles at sites i+1, i+2; its children are (u, c) with
   u(t+1) = u(t) xor (c(t) or d(t)) cyclically.  Bit t of a word is tick t.  Index = c << P | d.
   Output: the vertices on two-sided infinite paths, one index per line. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

int main(int argc, char **argv) {
    int P = argc > 1 ? atoi(argv[1]) : 15;
    if (P < 1 || P > 15) return 2;
    uint32_t M = (1u << P) - 1;
    uint64_t N = 1ull << (2 * P);
    uint32_t *px = malloc(sizeof(uint32_t) << P);
    uint8_t *par = malloc(1u << P);
    for (uint32_t m = 0; m <= M; m++) {
        uint32_t w = 0, bit = 0;
        for (int t = 0; t < P - 1; t++) { bit ^= (m >> t) & 1; w |= bit << (t + 1); }
        px[m] = w; par[m] = __builtin_popcount(m) & 1;
    }
    uint8_t *A = malloc(N), *H = malloc(N);
    if (!A || !H) return 3;
    uint64_t even = 0;
    for (uint64_t n = 0; n < N; n++) { A[n] = !par[(n >> P) | (n & M)]; even += A[n]; }
    fprintf(stderr, "pairs %llu with an even drive %llu\n", (unsigned long long)N, (unsigned long long)even);
    int rounds = 0; uint64_t changed;
    do {                                    /* keep vertices with an infinite leftward path */
        changed = 0;
        for (uint64_t n = 0; n < N; n++) if (A[n]) {
            uint32_t c = n >> P, d = n & M, w = px[c | d];
            uint64_t a = ((uint64_t)w << P) | c, b = ((uint64_t)(w ^ M) << P) | c;
            if (!A[a] && !A[b]) { A[n] = 0; changed++; }
        }
        rounds++;
    } while (changed);
    uint64_t fwd = 0; for (uint64_t n = 0; n < N; n++) fwd += A[n];
    fprintf(stderr, "leftward-infinite %llu rounds %d\n", (unsigned long long)fwd, rounds);
    rounds = 0;
    do {                                    /* also require a parent and a child inside the set */
        changed = 0;
        memset(H, 0, N);
        for (uint64_t n = 0; n < N; n++) if (A[n]) {
            uint32_t c = n >> P, d = n & M, w = px[c | d];
            uint64_t a = ((uint64_t)w << P) | c, b = ((uint64_t)(w ^ M) << P) | c;
            if (A[a]) H[a] = 1;
            if (A[b]) H[b] = 1;
            if (!A[a] && !A[b]) { A[n] = 0; changed++; }
        }
        for (uint64_t n = 0; n < N; n++) if (A[n] && !H[n]) { A[n] = 0; changed++; }
        rounds++;
    } while (changed);
    uint64_t core = 0;
    for (uint64_t n = 0; n < N; n++) if (A[n]) { printf("%llu\n", (unsigned long long)n); core++; }
    fprintf(stderr, "core %llu rounds %d\n", (unsigned long long)core, rounds);
    return 0;
}
