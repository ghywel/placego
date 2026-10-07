/* rule30_aw3b.c: AW3b, GPT's width-n strip test (GC313) in C for one pair of P-periodic columns 0, 1, at widths beyond
 * Python's reach; aimed at AW3's single undecided pair at P = 8, (column 0, column 1) = (83, 157). Local's run, claimed in
 * CLOUD-LOCAL.md with these predictions pushed before the program was run.
 *
 * BUILD:   cc -O2 -o rule30_aw3b tests/probes/lexicon/rule30_aw3b.c          (binary outside Git)
 * COMMAND: ./rule30_aw3b P C0 C1 NMIN NMAX
 * COST:    seconds to minutes; memory P * 2^NMAX bytes (134 MiB at P = 8, NMAX = 24).
 *
 * The graph, exactly as GC313 and rule30_aw2.py: states (phase p mod P, cells 2 .. n + 1 as an n-bit word s); column 1's
 * equation x(1, p + 1) = x(0, p) XOR (x(1, p) OR x(2, p)) must hold; then for each free far-right bit b the new cells are
 * (X XOR ((X >> 1) OR (X >> 2))) masked to n bits, where X = x(1, p) | s << 1 | b << (n + 1). A state stays alive while a
 * successor is alive; passes repeat to a fixed point. Output per width: alive count (0 means no cycle: no right
 * continuation, so the pair is not admissible).
 *
 * PREDICTIONS, Local's, published before the run (blind unless marked):
 *   B-P1 (blind, uncertain): (83, 157) at P = 8 dies at some width n <= 24.
 *   B-C1 (control): this program reproduces rule30_aw2.py's refuting widths on the two P = 6 pairs that needed
 *        more than width 3 there, (19, 29) at width 5 and (29, 41) at width 4, and keeps a cycle at every width 1 .. 16
 *        for a pair with a periodic continuation, (c0, c1) = (1, 0) at P = 1.
 *   B-C2 (control): (83, 157) survives every width 1 .. 14 here too, as in Python.
 * OUTCOME, 2026-10-07 18:12 (M5, one run of the program at 28768cc; seconds). B-C1 PASS: (19, 29) dies at width 5 and
 * (29, 41) at width 4 at P = 6, as in rule30_aw2.py; (1, 0) at P = 1 keeps cycles at every width to 16. B-C2 PASS:
 * (83, 157) keeps cycles at widths 1 .. 15 (alive 13, 13, 17, 21, 32, 41, 51, 78, 108, 169, 276, 360, 417, 475, 525).
 * B-P1 HELD: at width 16 nothing is alive, so (83, 157) has no right continuation. With AW3, entry 06's exact actual-wall
 * maxima at P = 8 are odd 7 and even 6 (at every depth, by GC316's re-anchoring), and the table for P = 3 .. 9 reads
 * odd 1, 1, 5, 5, 5, 7, 7 and even 4, 6, 2, 4, 6, 6, 6: 2P - 5 is attained only at P = 5 among P = 4 .. 9.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static long long alive_count(int P, unsigned c0, unsigned c1, int n, unsigned char *alive) {
    uint64_t S = 1ULL << n, N = (uint64_t)P * S, mask = S - 1;
    for (uint64_t i = 0; i < N; i++) alive[i] = 1;
    int changed = 1;
    while (changed) {
        changed = 0;
        for (int p = 0; p < P; p++) {
            unsigned a0 = (c0 >> p) & 1, a1 = (c1 >> p) & 1, b1 = (c1 >> ((p + 1) % P)) & 1;
            int pn = (p + 1) % P;
            for (uint64_t s = 0; s < S; s++) {
                uint64_t idx = (uint64_t)p * S + s;
                if (!alive[idx]) continue;
                int ok = 0;
                if (b1 == (a0 ^ (a1 | (unsigned)(s & 1)))) {
                    for (uint64_t b = 0; b < 2 && !ok; b++) {
                        uint64_t X = (uint64_t)a1 | (s << 1) | (b << (n + 1));
                        uint64_t s2 = (X ^ ((X >> 1) | (X >> 2))) & mask;
                        if (alive[(uint64_t)pn * S + s2]) ok = 1;
                    }
                }
                if (!ok) { alive[idx] = 0; changed = 1; }
            }
        }
    }
    long long c = 0;
    for (uint64_t i = 0; i < N; i++) c += alive[i];
    return c;
}

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: P C0 C1 NMIN NMAX\n"); return 2; }
    int P = atoi(argv[1]), nmin = atoi(argv[4]), nmax = atoi(argv[5]);
    unsigned c0 = (unsigned)atoi(argv[2]), c1 = (unsigned)atoi(argv[3]);
    unsigned char *alive = malloc((size_t)P << nmax);
    if (!alive) { fprintf(stderr, "no memory\n"); return 2; }
    for (int n = nmin; n <= nmax; n++) {
        long long c = alive_count(P, c0, c1, n, alive);
        printf("P %d pair (%u, %u) width %d alive %lld%s\n", P, c0, c1, n, c, c ? "" : "  -> no cycle: not admissible");
        fflush(stdout);
        if (!c) break;
    }
    free(alive);
    return 0;
}
