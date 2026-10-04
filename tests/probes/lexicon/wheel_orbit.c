/* wheel_orbit.c: the pure wheel's left half as one exact orbit (PRIZE-PROBLEMS.md section 8.5, lead M2).
 *
 * RUN-ON:     cpu (C99; one core per process; the orbit is sequential, so a GPU does not help)
 * BUILD:      cc -O2 -o wheel_orbit tests/probes/lexicon/wheel_orbit.c
 * COMMAND:    ./wheel_orbit WORD PHASE MAXSTEPS        e.g. ./wheel_orbit U 0 200000000000
 *             ./wheel_orbit selftest                    the known answers below
 * COST:       about a billion steps a second; MAXSTEPS bounds the work.
 *
 * Column 0 = 0101... and column 1 = WORD delayed by PHASE (both exactly periodic, period P) force every left column to
 * be P-periodic in time. The pair (c_{-k+1}, c_{-k}) evolves by
 *     F(b, c) = (c, rot(c) XOR (c OR b)),   rot(x)(t) = x(t + 1) cyclically,
 * from the state at k = 1, and the left half is L(k) = bit 0 of c_{-k}. F is a map on a finite set, so the orbit has
 * a tail of length mu and then a cycle of length lambda; (0, 0) is a fixed point. Brent's algorithm finds mu and
 * lambda in constant memory. If the cycle is not (0, 0), the left half is never eventually zero: a computed theorem,
 * re-checkable by anyone from (mu, lambda) alone.
 *
 * The program also reports the longest zero run of L within the first 200,000 depths (to cross-check against
 * rule30_wheel_left.py) and over every depth it visits.
 *
 * PREDICTIONS, written 2026-10-04 before this program's first run (results go into PRIZE-PROBLEMS.md section 8.6):
 *   O1 (uncertain): for at least one of the 28 phases of U, the orbit cycles within 2 x 10^11 steps.
 *   O2 (blind): every cycle found for a phase of U is not the zero fixed point.
 *   SELFTEST (known answers, from rule30_wheel_left.py): U2 at phase 0 has mu = 0 and lambda = 728; the 7-ring's
 *     4-cycle (P = 4, column 1 = 0011) has mu = 0 and lambda = 7; U at phases 0 and 2 has longest zero runs 8 by
 *     depth 192 and 14 and 17 by depth 200,000.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const char *U  = "00010011010001001101000100110100010011010001001101001101";
static const char *U2 = "00010011001101000100110011010001001100110100010011001101";

static int P;
static uint64_t MASK;

static inline uint64_t rot(uint64_t x) { return ((x >> 1) | ((x & 1) << (P - 1))) & MASK; }

typedef struct { uint64_t b, c; } state;

static inline state F(state s) {
    state t = { s.c, (rot(s.c) ^ (s.c | s.b)) & MASK };
    return t;
}

static inline int eq(state x, state y) { return x.b == y.b && x.c == y.c; }

static state start(const char *word, int phase) {
    uint64_t a = 0, b = 0;
    P = (int)strlen(word);
    MASK = (P == 64) ? ~0ULL : ((1ULL << P) - 1);
    for (int t = 0; t < P; t++) {
        if (word[((t - phase) % P + P) % P] == '1') a |= 1ULL << t;     /* column 1, delayed by phase */
        if (t % 2 == 1) b |= 1ULL << t;                                 /* column 0 = 0101... */
    }
    state s = { b, (rot(b) ^ (b | a)) & MASK };                          /* the pair at k = 1 */
    return s;
}

/* Returns 1 and fills mu, lambda if a cycle is found within maxsteps applications of F. */
static int brent(state x0, uint64_t maxsteps, uint64_t *mu, uint64_t *lam, uint64_t *used) {
    uint64_t power = 1, l = 1, steps = 0;
    state tort = x0, hare = F(x0);
    steps++;
    while (!eq(tort, hare)) {
        if (steps >= maxsteps) { *used = steps; return 0; }
        if (power == l) { tort = hare; power <<= 1; l = 0; }
        hare = F(hare);
        l++;
        steps++;
    }
    *lam = l;
    tort = hare = x0;
    for (uint64_t i = 0; i < l; i++) hare = F(hare);
    uint64_t m = 0;
    while (!eq(tort, hare)) { tort = F(tort); hare = F(hare); m++; }
    *mu = m;
    *used = steps + l + 2 * m;
    return 1;
}

static void runs(state s, uint64_t depth, int *by192, int *by200k, int *best) {
    int run = 0, m = 0;
    for (uint64_t k = 1; k <= depth; k++) {
        if ((s.c & 1) == 0) { run++; if (run > m) m = run; } else run = 0;
        if (k == 192) *by192 = m;
        if (k == 200000) *by200k = m;
        s = F(s);
    }
    *best = m;
}

static int selftest(void) {
    int fails = 0;
    uint64_t mu, lam, used;
    if (!brent(start(U2, 0), 1000000, &mu, &lam, &used) || mu != 0 || lam != 728) {
        printf("FAIL  U2 phase 0: expected mu 0, lambda 728\n"); fails++;
    } else printf("PASS  U2 phase 0: mu %llu, lambda %llu\n", (unsigned long long)mu, (unsigned long long)lam);
    if (!brent(start("0011", 0), 1000, &mu, &lam, &used) || mu != 0 || lam != 7) {
        printf("FAIL  7-ring 4-cycle: expected mu 0, lambda 7 (got %llu, %llu)\n",
               (unsigned long long)mu, (unsigned long long)lam); fails++;
    } else printf("PASS  7-ring 4-cycle: mu %llu, lambda %llu\n", (unsigned long long)mu, (unsigned long long)lam);
    int r192, r200k, best;
    int expect192[2] = {8, 7}, expect200k[2] = {14, 17};
    for (int i = 0; i < 2; i++) {
        runs(start(U, 2 * i), 200000, &r192, &r200k, &best);
        if (r192 != expect192[i] || r200k != expect200k[i]) {
            printf("FAIL  U phase %d: longest runs %d by 192, %d by 200000 (expected %d, %d)\n", 2 * i, r192, r200k,
                   expect192[i], expect200k[i]); fails++;
        } else printf("PASS  U phase %d: longest runs %d by depth 192, %d by depth 200000\n", 2 * i, r192, r200k);
    }
    printf(fails ? "%d FAILURE(S)\n" : "ALL SELFTESTS PASS\n", fails);
    return fails ? 1 : 0;
}

int main(int argc, char **argv) {
    if (argc >= 2 && strcmp(argv[1], "selftest") == 0) return selftest();
    if (argc < 4) { fprintf(stderr, "usage: wheel_orbit U|U2 PHASE MAXSTEPS | selftest\n"); return 2; }
    const char *word = strcmp(argv[1], "U2") == 0 ? U2 : U;
    int phase = atoi(argv[2]);
    uint64_t maxsteps = strtoull(argv[3], NULL, 10), mu = 0, lam = 0, used = 0;
    state x0 = start(word, phase);
    int found = brent(x0, maxsteps, &mu, &lam, &used);
    if (found) {
        state s = x0;
        for (uint64_t i = 0; i < mu; i++) s = F(s);
        int zero = (s.b == 0 && s.c == 0);
        printf("%s phase %2d: CYCLE mu %llu lambda %llu, cycle is %s (steps %llu)\n", argv[1], phase,
               (unsigned long long)mu, (unsigned long long)lam, zero ? "THE ZERO FIXED POINT" : "not zero",
               (unsigned long long)used);
    } else {
        printf("%s phase %2d: no cycle within %llu steps (mu + lambda > about %llu)\n", argv[1], phase,
               (unsigned long long)maxsteps, (unsigned long long)(used / 3));
    }
    return 0;
}
