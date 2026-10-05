/* realruns.c: the zero runs of the forced left half for every real right half of at most W cells, next to column 0
 * = 0101..., at given depths. Exhaustive, sharded over processes.
 *
 * BUILD:   cc -O2 -o realruns tests/probes/lexicon/realruns.c      (driven by rule30_realruns.py)
 * USAGE:   ./realruns W SHARD NSHARDS s1 s2 ...
 *          For every right half R = 1 .. 2^W - 1 with R % NSHARDS == SHARD: column 1 to time 125 (the right side run
 *          with column 0 clamped), the forced left half L(1..126) by ladder.c's anti-diagonal recursion, and for each
 *          depth s the zero run L(s), L(s+1), ... (capped at depth 126). Prints "Z W s length count" for every run
 *          length that occurs, so the shards' histograms can be added.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned __int128 u128;
#define CAP 126

static inline int tau(int t) { return t < 0 ? 0 : (t & 1); }
static inline u128 prefix_xor(u128 v) {
    v ^= v << 1; v ^= v << 2; v ^= v << 4; v ^= v << 8; v ^= v << 16; v ^= v << 32; v ^= v << 64;
    return v;
}
static inline u128 left_step(u128 a1, u128 a2, int t, int sigma) {     /* as in ladder.c */
    u128 b1 = (u128)(tau(t + 1) ^ (tau(t) | sigma)) << 1;
    u128 X = (a2 << 2) | ((u128)tau(t - 1) << 2);
    u128 G = ((a1 << 1) | X) & ~(u128)3;
    u128 mask = (t + 2 >= 128) ? ~(u128)0 : (((u128)1 << (t + 2)) - 1);
    return prefix_xor(G | b1) & mask & ~(u128)1;
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: realruns W SHARD NSHARDS s1 s2 ...\n"); return 2; }
    int W = atoi(argv[1]), shard = atoi(argv[2]), nsh = atoi(argv[3]), ns = argc - 4;
    int S[16];
    for (int i = 0; i < ns && i < 16; i++) S[i] = atoi(argv[4 + i]);
    static long long H[16][CAP + 2];
    const int NW = (W + CAP + 66) / 64;
    uint64_t row[8], nr[8];
    for (uint64_t R = 1; R < (1ULL << W); R++) {
        if ((int)(R % (uint64_t)nsh) != shard) continue;
        memset(row, 0, sizeof row);
        row[0] = R << 1;
        if (W >= 63) row[1] = R >> 63;
        u128 a1 = 0, a2 = 0, L = 0;                       /* bit k of L = L(k) */
        for (int t = 0; t < CAP; t++) {
            int sg = (int)((row[0] >> 1) & 1);
            u128 a = left_step(a1, a2, t, sg);
            L |= ((a >> (t + 1)) & 1) << (t + 1);
            a2 = a1; a1 = a;
            for (int k = 0; k < NW; k++) {
                uint64_t lf = (row[k] << 1) | (k ? row[k - 1] >> 63 : 0);
                uint64_t rt = (row[k] >> 1) | (k + 1 < NW ? row[k + 1] << 63 : 0);
                nr[k] = lf ^ (row[k] | rt);
            }
            nr[0] = (nr[0] & ~1ULL) | (uint64_t)((t + 1) & 1);
            memcpy(row, nr, sizeof row);
        }
        for (int i = 0; i < ns; i++) {
            int n = 0;
            while (S[i] + n <= CAP && !((L >> (S[i] + n)) & 1)) n++;
            H[i][n]++;
        }
    }
    for (int i = 0; i < ns; i++)
        for (int n = 0; n <= CAP + 1; n++) if (H[i][n]) printf("Z %d %d %d %lld\n", W, S[i], n, H[i][n]);
    return 0;
}
