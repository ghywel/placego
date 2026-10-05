/* jenclock.c: the longest zero run of the forced left half's row 0, for column 0 = 0101... and EVERY column 1 whose
 * visible bits (even times) have period q. Engine for rule30_jenclock.py (Local, 2026-10-05), which holds the
 * predictions.
 *
 * BUILD:  cc -O2 -o jenclock tests/probes/lexicon/jenclock.c
 * USAGE:  ./jenclock Q [BUDGET=2^31]        one line per q-periodic word class, then a SUMMARY line
 *         ./jenclock zero                   the control: columns 0 and 1 both zero (must report an infinite run)
 *
 * With P = 2q, columns 0 and 1 are P-periodic in time, so every column to the left is too (Jen), and the pair map
 * (b, c) -> (c, rot(c) XOR (c OR b)) of periodic_kill.c runs on 2^(2P) states. The cell of row 0 at depth k is bit 0
 * of column -k. Brent's algorithm finds the tail mu and the cycle lambda in depth; the longest run of zero cells is
 * then read over the tail and twice round the cycle (a run may wrap). A cycle of zero cells only is an infinite run.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int P;
static uint64_t MASK;
static inline uint64_t rot(uint64_t x) { return ((x >> 1) | ((x & 1) << (P - 1))) & MASK; }

/* returns the longest zero run of bit 0 over depths 1, 2, ...; -1 = infinite; -2 = budget exceeded */
static long long longest(uint64_t col0, uint64_t col1, uint64_t budget, uint64_t *mu_out, uint64_t *lam_out) {
    uint64_t b0 = col0, c0 = (rot(col0) ^ (col0 | col1)) & MASK;      /* (column 0, column -1) */
    /* Brent */
    uint64_t tb = b0, tc = c0, hb = c0, hc = (rot(c0) ^ (c0 | b0)) & MASK, power = 1, lam = 1, steps = 1;
    while (!(tb == hb && tc == hc)) {
        if (steps >= budget) return -2;
        if (power == lam) { tb = hb; tc = hc; power <<= 1; lam = 0; }
        uint64_t n = (rot(hc) ^ (hc | hb)) & MASK; hb = hc; hc = n; lam++; steps++;
    }
    uint64_t mu = 0; tb = b0; tc = c0; hb = b0; hc = c0;
    for (uint64_t i = 0; i < lam; i++) { uint64_t n = (rot(hc) ^ (hc | hb)) & MASK; hb = hc; hc = n; }
    while (!(tb == hb && tc == hc)) {
        uint64_t n = (rot(tc) ^ (tc | tb)) & MASK; tb = tc; tc = n;
        n = (rot(hc) ^ (hc | hb)) & MASK; hb = hc; hc = n; mu++;
    }
    *mu_out = mu; *lam_out = lam;
    /* walk depths 1 .. mu + 2 lam; the state (b, c) holds columns -(k-1), -k, so the depth-k cell is bit 0 of c */
    uint64_t b = b0, c = c0, total = mu + 2 * lam;
    long long best = 0, cur = 0;
    int cycle_has_one = 0;
    for (uint64_t k = 1; k <= total; k++) {
        if (c & 1) { cur = 0; if (k > mu) cycle_has_one = 1; }
        else { cur++; if (cur > best) best = cur; }
        uint64_t n = (rot(c) ^ (c | b)) & MASK; b = c; c = n;
    }
    return cycle_has_one ? best : -1;
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: jenclock Q [BUDGET] | zero\n"); return 2; }
    if (strcmp(argv[1], "zero") == 0) {
        P = 4; MASK = 15;
        uint64_t mu, lam;
        long long r = longest(0, 0, 1000, &mu, &lam);
        printf("CONTROL zero columns: run %lld (-1 = infinite)\n", r);
        return 0;
    }
    int q = atoi(argv[1]);
    uint64_t budget = argc > 2 ? strtoull(argv[2], NULL, 10) : (1ULL << 31);
    P = 2 * q;
    if (P > 62) { fprintf(stderr, "q too large\n"); return 2; }
    MASK = (1ULL << P) - 1;
    uint64_t col0 = 0;
    for (int t = 0; t < P; t++) if (t & 1) col0 |= 1ULL << t;
    long long worst = 0, undecided = 0, infinite = 0, words = 0, worst_slack = 1LL << 40;
    uint64_t worst_word = 0, maxlam = 0, maxmu = 0;
    int worst_qmin = 0;
    for (uint64_t w = 0; w < (1ULL << q); w++) {
        /* the word's least period q' divides q; only words of least period exactly q are run (others at their own q') */
        int qmin = q;
        for (int d = 1; d < q; d++) if (q % d == 0) {
            int ok = 1;
            for (int i = 0; i < q && ok; i++) if (((w >> i) & 1) != ((w >> ((i + d) % q)) & 1)) ok = 0;
            if (ok) { qmin = d; break; }
        }
        if (qmin != q) continue;
        words++;
        uint64_t col1 = 0;
        for (int t = 0; t < P; t += 2) if ((w >> ((t / 2) % q)) & 1) col1 |= 1ULL << t;   /* hidden (odd) bits 0 */
        uint64_t mu = 0, lam = 0;
        long long r = longest(col0, col1, budget, &mu, &lam);
        if (r == -2) { undecided++; continue; }
        if (r == -1) { infinite++; printf("INFINITE q %d word %llu\n", q, (unsigned long long)w); continue; }
        if (lam > maxlam) maxlam = lam;
        if (mu > maxmu) maxmu = mu;
        long long slack = (long long)(2 * P - 2) - r;
        if (r > worst) { worst = r; worst_word = w; worst_qmin = qmin; }
        if (slack < worst_slack) worst_slack = slack;
    }
    printf("SUMMARY q %d (P %d): %lld words of least period q; longest zero run %lld (word %llu, bound 2P-2 = %d); "
           "least slack %lld; infinite %lld; undecided %lld; longest tail %llu, longest cycle %llu\n",
           q, P, words, worst, (unsigned long long)worst_word, 2 * P - 2, worst_slack, infinite, undecided,
           (unsigned long long)maxmu, (unsigned long long)maxlam);
    (void)worst_qmin;
    return 0;
}
