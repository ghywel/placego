/* periodic_kill.c: can a periodic column 1 kill the left half? Conjecture LR (PRIZE-PROBLEMS.md section 7) says no
 * column 1 at all lets the forced left half become zero. For periodic columns 1 this is an exact finite question.
 *
 * RUN-ON:     cpu (C99, one core)
 * BUILD:      cc -O2 -o periodic_kill tests/probes/lexicon/periodic_kill.c
 * COMMAND:    ./periodic_kill TRACE QMAX BUDGET      e.g. ./periodic_kill 01 18 1000000
 * COST:       seconds to minutes.
 *
 * Column 0 = TRACE repeated, column 1 = every word of length q (q = 1..QMAX) repeated; P = lcm(|TRACE|, q) <= 62.
 * Both are P-periodic, so the left columns are too, and the pair map F(b, c) = (c, rot(c) XOR (c OR b)) of
 * wheel_orbit.c runs on a finite set. Brent's algorithm (at most BUDGET steps per word) finds the tail and the cycle;
 * a cycle equal to (0, 0) is a kill: the forced left half is eventually zero. A word whose orbit does not cycle within
 * BUDGET is counted as undecided.
 *
 * PREDICTIONS, written 2026-10-04 before this program's first run:
 *   K1 (blind; conjecture LR restricted to periodic columns 1): with column 0 = 0101..., no word of period q <= 18
 *      kills the left half. Every one of the 2^1 + ... + 2^18 words is decided within 10^6 steps or counted.
 *   K2 (blind): the same for column 0 = 0001... with q <= 14.
 *   C  (known answer, must be found): with column 0 = 000... (TRACE 0), column 1 = 000... kills (the zero row), and
 *      that is the only kill for q = 1 (column 1 = 111... with the zero trace is Condrey's case: not a kill).
 *
 * OUTCOME of the first run, 2026-10-04 (BUDGET 10^6): C passed (for TRACE 0 and q = 1..4 the only kill is the zero
 * column; column 1 = 111... gives the alternating tail, a cycle of 2). K1 HELD as worded: with column 0 = 0101..., 0
 * kills among 524,286 words of period 1..18. 394,848 were decided; the other 129,438 (all of period 17, P = 34) did
 * not cycle within the budget. K2 HELD as worded: with column 0 = 0001..., 0 kills among 32,766 words of period 1..14;
 * 22,162 were decided, and 10,604 (periods 9, 11, 13; P = 36, 44, 52) were undecided. The longest cycles found were
 * 396,525 (0101..., q = 15) and 363,832 (0001..., q = 7 and 14). Undecided words are not settled. Since rotating
 * column 1 together with the trace leaves the outcome unchanged, about 7,600 rotation classes would settle q = 17.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int P;
static uint64_t MASK;

static inline uint64_t rot(uint64_t x) { return ((x >> 1) | ((x & 1) << (P - 1))) & MASK; }

static int gcd(int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; }

/* 1 = kill, 0 = cycle not zero, -1 = undecided within budget */
static int decide(uint64_t col0, uint64_t col1, uint64_t budget, uint64_t *lam_out) {
    uint64_t b = col0, c = (rot(col0) ^ (col0 | col1)) & MASK;
    uint64_t tb = b, tc = c, hb = c, hc = (rot(c) ^ (c | b)) & MASK;
    uint64_t power = 1, lam = 1, steps = 1;
    while (!(tb == hb && tc == hc)) {
        if (steps >= budget) return -1;
        if (power == lam) { tb = hb; tc = hc; power <<= 1; lam = 0; }
        uint64_t nc = (rot(hc) ^ (hc | hb)) & MASK;
        hb = hc; hc = nc;
        lam++; steps++;
    }
    *lam_out = lam;
    /* the cycle contains (hb, hc); it is the zero fixed point iff that state is zero */
    return (hb == 0 && hc == 0) ? 1 : 0;
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: periodic_kill TRACE QMAX BUDGET\n"); return 2; }
    const char *trace = argv[1];
    int tl = (int)strlen(trace), qmax = atoi(argv[2]);
    uint64_t budget = strtoull(argv[3], NULL, 10);
    uint64_t total_kill = 0, total_undecided = 0, total = 0;
    for (int q = 1; q <= qmax; q++) {
        P = tl / gcd(tl, q) * q;
        if (P > 62) { printf("q %d: P = %d too large, skipped\n", q, P); continue; }
        MASK = (1ULL << P) - 1;
        uint64_t col0 = 0;
        for (int t = 0; t < P; t++) if (trace[t % tl] == '1') col0 |= 1ULL << t;
        uint64_t kills = 0, undecided = 0, maxlam = 0, first_kill = 0;
        int have_kill = 0;
        for (uint64_t w = 0; w < (1ULL << q); w++) {
            uint64_t col1 = 0;
            for (int t = 0; t < P; t++) if ((w >> (t % q)) & 1) col1 |= 1ULL << t;
            uint64_t lam = 0;
            int r = decide(col0, col1, budget, &lam);
            if (r == 1) { kills++; if (!have_kill) { first_kill = w; have_kill = 1; } }
            else if (r < 0) undecided++;
            else if (lam > maxlam) maxlam = lam;
        }
        printf("trace %s, q %2d (P %2d): %llu words, kills %llu%s, undecided %llu, longest cycle %llu\n", trace, q, P,
               (unsigned long long)(1ULL << q), (unsigned long long)kills,
               "", (unsigned long long)undecided, (unsigned long long)maxlam);
        if (have_kill) {
            printf("   first kill: column 1 = ");
            for (int t = 0; t < q; t++) putchar(((first_kill >> t) & 1) ? '1' : '0');
            printf(" repeated\n");
        }
        fflush(stdout);
        total += 1ULL << q; total_kill += kills; total_undecided += undecided;
    }
    printf("TOTAL trace %s: %llu words, %llu kills, %llu undecided\n", trace, (unsigned long long)total,
           (unsigned long long)total_kill, (unsigned long long)total_undecided);
    return 0;
}
