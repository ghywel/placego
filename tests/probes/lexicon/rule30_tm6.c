/* rule30_tm6.c: TM6, the whole-tree minimum of N_6 (the first entry to period 64) over all rooted histories, by a
 * lockstep search at common period Q = 32 (Local's run, after TM5 and TM5b; claimed in CLOUD-LOCAL.md, with these
 * predictions pushed before the program was run).
 *
 * RUN-ON:  cpu (C, one thread)
 * BUILD:   cc -O2 -o /tmp/rule30_tm6 tests/probes/lexicon/rule30_tm6.c
 * COMMAND: /tmp/rule30_tm6 [WALL_SECONDS=14400] > transcript (outside Git); smoke tests only: ... WALL X Y
 * COST:    hours expected; caps: WALL_SECONDS of wall time and 4,096 live walks. The first cap hit stops the run, which
 *          then certifies only a lower bound: no rooted history reaches period 64 at or below the depth reached.
 *
 * Domain. 32-bit temporal words (bit t is time t; S c means c(t + 1)). The root (0, 1^32) is at depth 0; the state at
 * depth d is (w_(d-1), w_d). A nonzero driver b has one 32-periodic child (reset at a black cell of b, then
 * c(t + 1) = a(t) XOR (b(t) OR c(t)) round the cycle). At a zero driver (a, 0) the integration closes, with children
 * c and c XOR 1^32, exactly when a has even parity over 32 bits; then if the two children are rotations of each other
 * (a doubling from a shorter period) one is followed, and otherwise (a genuine branch) both are. With odd parity there
 * is no 32-periodic child: the history's period becomes 64 and N_6 = d + 1. Every transition is checked by the
 * literal equation rot(c, 1) == a XOR (b OR c), separately from the constructor. All live walks advance in lockstep
 * by rounds of 2^24 depths; a walk spawned at a branch inside a round is advanced to the round's end in the same
 * round. So when a round ends with any exit, the least exit depth in it is the whole-tree minimum (every other walk
 * has passed that depth without exiting). Events (every zero above depth 399) and progress lines are printed.
 *
 * PREDICTIONS, Local's, published before the run (blind unless marked):
 *   T6-C1 (control): the zeros at 2, 7, 28, 399 are doublings; the 15 genuine branch nodes of TM5b recur at the same
 *         depths; and TM5b's 16 entries to period 32 recur as doublings here, at depths 87,866 ... 894,234.
 *   T6-C2 (control): the literal equation holds on every transition.
 *   T6-P1 (blind, uncertain): the tree minimum N_6 lies between 10^8 and 10^10 (R_6 = N_6/64 between about 1.6 x
 *         10^6 and 1.6 x 10^8). Basis: zero drivers are 2^q of the 2^(2q) pairs, so a typical return should take
 *         about 2^q steps; measured mean returns fit at q = 4, 8, 16 (21, 371, about 50,000 against 16, 256,
 *         65,536); 2^32 is about 4.3 x 10^9, and the minimum over many walks is smaller.
 *   T6-P2 (blind): no history has a 32-bit zero within 10^6 depths of its entry to period 32 (known for the four
 *         sides realised by rule30_leftside_million.py, blind for the other twelve).
 *   T6-U (the unexpected check): the run is restartable in principle but is run once; if the wall cap fires first,
 *         the certified lower bound (the depth reached) is recorded as the result, with the live walk count, and no
 *         prediction about the minimum is scored as held.
 * Transcripts go outside Git; the outcome is written into this header by hand after the single run.
 *
 * OUTCOME: not yet run.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAXW 4096
#define ROUND (1LL << 24)

typedef struct { uint32_t x, y; int64_t d; int id, parent; } walk_t;

static walk_t W[MAXW];
static int nw = 0, next_id = 0;
static long long literal_fail = 0;

static inline uint32_t rotr(uint32_t w, int k) { k &= 31; return k ? (w >> k) | (w << (32 - k)) : w; }

static inline uint32_t child_nonzero(uint32_t a, uint32_t b) {
    int t0 = __builtin_ctz(b), t = (t0 + 1) & 31;
    uint32_t c = 0, ct = ((a >> t0) & 1) ^ 1;
    for (int i = 0; i < 32; i++) {
        c |= ct << t;
        uint32_t nt = ((a >> t) & 1) ^ (((b >> t) | ct) & 1);
        t = (t + 1) & 31;
        ct = nt;
    }
    return c;
}

static int is_rot(uint32_t u, uint32_t v) {
    for (int k = 1; k < 32; k++) if (rotr(u, k) == v) return 1;
    return 0;
}

int main(int argc, char **argv) {
    double wall_cap = argc > 1 ? atof(argv[1]) : 14400.0;
    time_t t_start = time(0);
    W[nw++] = (walk_t){0, 0xFFFFFFFFu, 0, next_id++, -1};
    if (argc > 3) {                                 /* smoke tests only: a non-rooted start pair (X, Y) at depth 0 */
        W[0].x = (uint32_t)strtoul(argv[2], 0, 10);
        W[0].y = (uint32_t)strtoul(argv[3], 0, 10);
        printf("SMOKE start (%u, %u): not a rooted run\n", W[0].x, W[0].y);
    }
    int64_t round_end = 0;
    int64_t best = -1;
    long long branches = 0, doublings = 0;
    printf("TM6 start: Q = 32, round %lld, wall cap %.0f s\n", (long long)ROUND, wall_cap);
    fflush(stdout);
    while (best < 0) {
        round_end += ROUND;
        for (int i = 0; i < nw; i++) {             /* nw may grow inside the round: spawned walks run to round_end */
            walk_t *w = &W[i];
            if (w->d < 0) continue;                 /* exited */
            uint32_t x = w->x, y = w->y;
            int64_t d = w->d;
            while (d < round_end) {
                if (y) {
                    uint32_t c = child_nonzero(x, y);
                    if (rotr(c, 1) != (x ^ (y | c))) literal_fail++;
                    x = y; y = c; d++;
                    continue;
                }
                if (__builtin_popcount(x) & 1) {    /* odd: no 32-periodic child; period 64 from d + 1 */
                    printf("EVENT %lld exit walk %d parent %d driver %u\n", (long long)d, w->id, w->parent, x);
                    if (best < 0 || d < best) best = d;
                    d = -1;
                    break;
                }
                uint32_t c1 = 0, run = 0;
                for (int t = 0; t < 32; t++) { c1 |= run << t; run ^= (x >> t) & 1; }
                uint32_t c2 = ~c1;
                if (rotr(c1, 1) != (x ^ c1) || rotr(c2, 1) != (x ^ c2)) literal_fail++;
                if (is_rot(c1, c2)) {
                    doublings++;
                    if (d > 399) printf("EVENT %lld doubling walk %d\n", (long long)d, w->id);
                } else {
                    branches++;
                    printf("EVENT %lld branch walk %d spawns %d driver %u\n", (long long)d, w->id, next_id, x);
                    if (nw >= MAXW) { printf("STOP walk cap at depth %lld\n", (long long)d); fflush(stdout); return 2; }
                    W[nw++] = (walk_t){0, c2, d + 1, next_id++, w->id};
                    w = &W[i];                      /* W is static; the pointer stays valid, refreshed for clarity */
                }
                x = 0; y = c1; d++;
            }
            w->x = x; w->y = y; w->d = d;
        }
        int live = 0;
        for (int i = 0; i < nw; i++) live += W[i].d >= 0;
        double el = difftime(time(0), t_start);
        if ((round_end & ((1LL << 30) - 1)) == 0 || best >= 0)
            printf("PROGRESS depth %lld live %d walks %d branches %lld doublings %lld literal_fail %lld elapsed %.0f s\n",
                   (long long)round_end, live, nw, branches, doublings, literal_fail, el);
        fflush(stdout);
        if (best < 0 && el > wall_cap) {
            printf("STOP wall cap: no rooted history reaches period 64 at depth <= %lld (N_6 > %lld); live %d\n",
                   (long long)round_end, (long long)round_end, live);
            return 3;
        }
    }
    printf("RESULT tree minimum N_6 = %lld (R_6 = %.2f); literal_fail %lld; walks %d\n",
           (long long)(best + 1), (double)(best + 1) / 64.0, literal_fail, nw);
    return 0;
}
