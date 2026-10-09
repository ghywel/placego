/* rule30_one_hole_direct.c: OHD, the one-hole hole language by plain forward simulation, with no relaxation. Local's
 * run (chat L480); predictions in rule30_one_hole_widths.py's OHD block, pushed first.
 *
 * Build:  clang -O2 -o ~/np-scratch-int/rule30-oh/ohd tests/probes/lexicon/rule30_one_hole_direct.c
 * Run:    ohd P N
 *
 * Rule 30 on the half-line x1, x2, ... with the wall as its left boundary: the wall is white at t = 0 mod P and
 * black otherwise. x1 at time T depends only on x1 .. x(T+1) at time 0 (radius one), so with T = (N - 1) P every
 * hole word of length N (x1 at t = 0, P, ..., T) is produced by some initial right half on M = T + 1 cells. Cells
 * beyond M start at 0, and they cannot reach x1 by time T. Every one of the 2^M initial rows is simulated, as one
 * machine word per row; the distinct N-bit words are counted. Each row's update is x' = left XOR (x OR right), with
 * left = (x << 1 | wall) and right = x >> 1; bit j holds x(j+1). One extra cell, M + 1 (always 0 at time 0), is
 * carried so that the cell M update is literal.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s P N\n", argv[0]); return 2; }
    int P = atoi(argv[1]), N = atoi(argv[2]);
    int T = (N - 1) * P, M = T + 1;
    if (M + 2 > 63 || M > 34) { fprintf(stderr, "M = %d too large\n", M); return 2; }
    int W = M + 2;                                       /* cells x1 .. x(M+2), the extra ones start at 0 */
    uint64_t mask = (W == 64) ? ~0ULL : ((1ULL << W) - 1);
    uint8_t *seen = calloc(1u << N, 1);
    uint64_t rows = 1ULL << M;
    for (uint64_t x0 = 0; x0 < rows; x0++) {
        uint64_t x = x0;
        unsigned word = 0;
        for (int t = 0; t <= T; t++) {
            if (t % P == 0) word |= (unsigned)(x & 1) << (t / P);
            if (t == T) break;
            uint64_t wall = (t % P == 0) ? 0 : 1;
            uint64_t left = ((x << 1) | wall) & mask, right = x >> 1;
            x = (left ^ (x | right)) & mask;
        }
        seen[word] = 1;
    }
    long cnt = 0;
    for (unsigned w = 0; w < (1u << N); w++) cnt += seen[w];
    printf("P %d N %d M %d words %ld\n", P, N, M, cnt);
    return 0;
}
