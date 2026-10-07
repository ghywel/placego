/* rule30_aw4.c: AW4, do entry 06's actual-wall run maxima stay at odd 7, even 6 beyond P = 9? (Local's run, after AW3
 * and AW3b and the question in chat L203; claimed in CLOUD-LOCAL.md with these predictions pushed before the run.)
 *
 * BUILD:   cc -O2 -o rule30_aw4 tests/probes/lexicon/rule30_aw4.c          (binary outside Git)
 * COMMAND: ./rule30_aw4 P [WMAX=18] [ODD=7] [EVEN=6]
 * COST:    the census is seconds; the strip tests dominate; cap one hour of CPU per P.
 *
 * Method. For every pair of P-periodic columns 0 (nonzero) and 1, build the forced left half by the inverse rule
 * x(-j, t) = x(-j + 1, t + 1) XOR (x(-j + 1, t) OR x(-j + 2, t)) to 40 columns, and find the bounded white runs in row 0
 * (strictly in x < 0, black at both ends). A pair is EXCESS if it has an odd run > ODD or an even run > EVEN. Every
 * excess pair gets GPT's strip test (GC313), exactly as rule30_aw3b.c, at widths 1 .. WMAX; a width with no cycle
 * certifies no right continuation. If every excess pair is refuted, the actual-wall maxima at that P are at most ODD and
 * EVEN, at every depth by GPT's GC316 re-anchoring (Theorem B's 2P - 2 < 40 keeps every run inside the census for P <= 20).
 * Upper bounds only: this does not show that ODD and EVEN are attained at the new P.
 *
 * PREDICTIONS, Local's, published before the run (blind unless marked):
 *   A4-C1 (control): at P = 8 the census finds AW3's 632 excess pairs, and all are refuted, (83, 157) at width 16.
 *   A4-C2 (control): at P = 9 the census finds AW3's 1,794 excess pairs, all refuted.
 *   A4-P1 (blind, uncertain): at P = 10 every excess pair is refuted by width 18 (actual maxima <= odd 7, even 6).
 *   A4-P2 (blind, uncertain): the same at P = 11.
 *   A4-U (the unexpected check, blind): some excess pair at P = 10 or 11 needs a refuting width above 16.
 * An excess pair alive at WMAX stays undecided and is printed; it is not called admissible.
 * OUTCOME, 2026-10-07 18:15 (M5, one run of the program at c20becb, P = 8, 9, 10, 11 in sequence; CPU 0.0, 0.0, 1.5,
 * 23.1 s; transcript outside Git). A4-C1 PASS (P = 8: 632 excess pairs, all refuted, widest at 16). A4-C2 PASS (P = 9:
 * 1,794, all refuted). A4-P1 REFUTED: at P = 10, of 29,058 excess pairs 29,048 are refuted and 10 survive width 18,
 * every one with an odd run of 9 (even runs 2). A4-P2 REFUTED: at P = 11, of 223,004 excess pairs 222,811 are refuted
 * and 193 survive width 18, with runs up to odd 9 and even 12. A4-U PASS (refuting widths 17 and 18 occur). So the
 * actual-wall maxima are at most odd 9, even 6 at P = 10 and at most odd 9, even 12 at P = 11; whether those survivors
 * are actual is open (this test only refutes). A guess made after the run, that the ten P = 10 survivors chain into a
 * spatially periodic configuration through 11 columns, was checked and is FALSE; it is recorded and not used.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static int P;
static unsigned FULLP;

static inline unsigned rotr1(unsigned w) { return ((w >> 1) | (w << (P - 1))) & FULLP; }   /* (S w)(t) = w(t + 1) */

static void runs(unsigned c0, unsigned c1, int *odd, int *even) {
    unsigned r2 = c1, r = c0;                       /* columns 1, 0 */
    int row[41];
    row[0] = c0 & 1;
    for (int k = 1; k <= 40; k++) {
        unsigned nc = rotr1(r) ^ (r | r2);
        r2 = r; r = nc;
        row[k] = nc & 1;
    }
    *odd = *even = 0;
    int k = 1;
    while (k <= 40) {
        if (row[k] == 0 && row[k - 1] == 1) {
            int e = k;
            while (e <= 40 && row[e] == 0) e++;
            if (e <= 40) {
                int n = e - k;
                if (n % 2) { if (n > *odd) *odd = n; } else { if (n > *even) *even = n; }
            }
            k = e;
        }
        k++;
    }
}

static long long alive_count(unsigned c0, unsigned c1, int n, unsigned char *alive) {
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
                        if (alive[(uint64_t)pn * S + ((X ^ ((X >> 1) | (X >> 2))) & mask)]) ok = 1;
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
    P = atoi(argv[1]);
    int wmax = argc > 2 ? atoi(argv[2]) : 18, ODD = argc > 3 ? atoi(argv[3]) : 7, EVEN = argc > 4 ? atoi(argv[4]) : 6;
    FULLP = (1u << P) - 1;
    unsigned char *alive = malloc((size_t)P << wmax);
    clock_t t0 = clock();
    long long excess = 0, refuted = 0, undecided = 0;
    int maxw = 0, maxodd = 0, maxeven = 0;
    for (unsigned c0 = 1; c0 <= FULLP; c0++)
        for (unsigned c1 = 0; c1 <= FULLP; c1++) {
            int o, e;
            runs(c0, c1, &o, &e);
            if (o <= ODD && e <= EVEN) continue;
            excess++;
            int w = 0;
            for (int n = 1; n <= wmax; n++)
                if (!alive_count(c0, c1, n, alive)) { w = n; break; }
            if (w) {
                refuted++;
                if (w > maxw) maxw = w;
                if (w > 16) printf("WIDE pair (%u, %u) runs odd %d even %d refuted at width %d\n", c0, c1, o, e, w);
            }
            else {
                undecided++;
                if (o > maxodd) maxodd = o;
                if (e > maxeven) maxeven = e;
                printf("UNDECIDED pair (%u, %u) runs odd %d even %d alive at width %d\n", c0, c1, o, e, wmax);
            }
            if ((double)(clock() - t0) / CLOCKS_PER_SEC > 3600) { printf("CAP at P = %d\n", P); fflush(stdout); return 3; }
            fflush(stdout);
        }
    printf("P = %d: excess pairs %lld (above odd %d / even %d); refuted %lld (max width %d); undecided %lld "
           "(their longest runs odd %d even %d); CPU %.1f s\n", P, excess, ODD, EVEN, refuted, maxw, undecided,
           maxodd, maxeven, (double)(clock() - t0) / CLOCKS_PER_SEC);
    return 0;
}
