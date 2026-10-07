/* rule30_tm6b.c: TM6b, N_6 on every rooted history, continuing TM6's lockstep search at common period Q = 32 past the
 * minimum until every live walk has entered period 64 or the wall cap fires (Local's run; claimed in CLOUD-LOCAL.md,
 * with these predictions pushed before the program was run).
 *
 * RUN-ON:  cpu (C, one thread)
 * BUILD:   cc -O2 -o rule30_tm6b tests/probes/lexicon/rule30_tm6b.c   (binary and transcript outside Git)
 * COMMAND: ./rule30_tm6b [WALL_SECONDS=10800] > transcript
 * COST:    hours expected; caps: WALL_SECONDS of wall time, checked at completed rounds, and 4,096 walks.
 *
 * Domain, walk, children, branch rule and literal check exactly as rule30_tm6.c (common period 32 from the root,
 * lockstep rounds of 2^24 depths). The difference: an exit no longer stops the run; each walk (one history up to
 * rotation; a genuine branch spawns a sibling walk) is followed to its own odd zero. Guards from GPT's GC288, in code:
 * certification requires literal_fail = 0 and the event controls; the only certified frontier is the end of the last
 * COMPLETED round (a walk-cap stop inside a round falls back to the previous round's end); exits observed in an
 * unfinished round are reported as provisional.
 *
 * PREDICTIONS, Local's, published before the run (blind unless marked):
 *   T6b-C1 (control): TM6's events recur: the 15 period-16 branches, the 16 entries to period 32 as doublings, and
 *          the first 32-bit zero anywhere at depth 65,821,412, an odd zero (exit) on the walk from 667,052.
 *   T6b-C2 (control): literal_fail = 0 (required for any certified number).
 *   T6b-P1 (blind, uncertain): within the cap, at least 12 of the 15 histories still in period 32 after TM6 reach
 *          period 64 (counting each original walk's own path, which follows the first child at its branches).
 *   T6b-P2 (blind): at least one genuine branch occurs at period 32 before the cap.
 *   T6b-U (the unexpected check, blind): the total number of 32-bit zeros met, divided by the total walk steps at
 *          period 32 (each walk counted from its own entry to period 32), lies within a factor 2 of 2^-32 (the rough
 *          return estimate behind TM6's prediction).
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

typedef struct { uint32_t x, y; int64_t d; int id, parent, p32; } walk_t;   /* p32: past its entry to period 32 */

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
    double wall_cap = argc > 1 ? atof(argv[1]) : 10800.0;
    time_t t_start = time(0);
    W[nw++] = (walk_t){0, 0xFFFFFFFFu, 0, next_id++, -1, 0};
    if (argc > 3) {                                 /* smoke tests only: a non-rooted start pair (X, Y) at depth 0 */
        W[0].x = (uint32_t)strtoul(argv[2], 0, 10);
        W[0].y = (uint32_t)strtoul(argv[3], 0, 10);
        printf("SMOKE start (%u, %u): not a rooted run\n", W[0].x, W[0].y);
    }
    int64_t round_end = 0;
    int64_t best = -1;
    long long branches = 0, doublings = 0;
    long long zeros32 = 0, steps32 = 0, exits = 0;
    int64_t last_complete = 0;
    printf("TM6b start: Q = 32, round %lld, wall cap %.0f s\n", (long long)ROUND, wall_cap);
    fflush(stdout);
    for (;;) {
        round_end += ROUND;
        for (int i = 0; i < nw; i++) {             /* nw may grow inside the round: spawned walks run to round_end */
            walk_t *w = &W[i];
            if (w->d < 0) continue;                 /* exited */
            uint32_t x = w->x, y = w->y;
            int64_t d = w->d;
            while (d < round_end) {
                if (y) {
                    if (w->p32) steps32++;
                    uint32_t c = child_nonzero(x, y);
                    if (rotr(c, 1) != (x ^ (y | c))) literal_fail++;
                    x = y; y = c; d++;
                    continue;
                }
                if (w->p32) zeros32++;
                if (__builtin_popcount(x) & 1) {    /* odd: no 32-periodic child; period 64 from d + 1 */
                    printf("EVENT %lld exit walk %d parent %d driver %u N_6 %lld\n", (long long)d, w->id, w->parent, x,
                           (long long)d + 1);
                    exits++;
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
                    if (d > 399) { printf("EVENT %lld doubling walk %d\n", (long long)d, w->id); w->p32 = 1; }
                } else {
                    branches++;
                    printf("EVENT %lld branch walk %d spawns %d driver %u\n", (long long)d, w->id, next_id, x);
                    if (nw >= MAXW) {
                        printf("STOP walk cap inside a round; certified frontier: N_6 > %lld on every live walk "
                               "(last completed round); exits in this round are provisional; literal_fail %lld\n",
                               (long long)last_complete, literal_fail);
                        fflush(stdout);
                        return 2;
                    }
                    W[nw++] = (walk_t){0, c2, d + 1, next_id++, w->id, w->p32};
                    w = &W[i];                      /* W is static; the pointer stays valid, refreshed for clarity */
                }
                x = 0; y = c1; d++;
            }
            w->x = x; w->y = y; w->d = d;
        }
        last_complete = round_end;
        int live = 0;
        for (int i = 0; i < nw; i++) live += W[i].d >= 0;
        double el = difftime(time(0), t_start);
        if ((round_end & ((1LL << 30) - 1)) == 0 || live == 0)
            printf("PROGRESS depth %lld live %d walks %d exits %lld branches %lld doublings %lld zeros32 %lld "
                   "steps32 %lld literal_fail %lld elapsed %.0f s\n", (long long)round_end, live, nw, exits, branches,
                   doublings, zeros32, steps32, literal_fail, el);
        fflush(stdout);
        if (live == 0) {
            printf("RESULT every walk entered period 64 by depth %lld; walks %d; zeros32 %lld; steps32 %lld; "
                   "literal_fail %lld (%s)\n", (long long)round_end, nw, zeros32, steps32, literal_fail,
                   literal_fail ? "INVALID: literal failures" : "certified if the event controls pass");
            return literal_fail ? 4 : 0;
        }
        if (el > wall_cap) {
            printf("STOP wall cap at a completed round: every live walk has N_6 > %lld; live %d of %d walks; exits "
                   "%lld; zeros32 %lld; steps32 %lld; literal_fail %lld (%s)\n", (long long)round_end, live, nw,
                   exits, zeros32, steps32, literal_fail,
                   literal_fail ? "INVALID: literal failures" : "certified if the event controls pass");
            for (int i = 0; i < nw; i++)
                if (W[i].d >= 0) printf("LIVE walk %d parent %d depth %lld\n", W[i].id, W[i].parent, (long long)W[i].d);
            return literal_fail ? 4 : 3;
        }
    }
}
