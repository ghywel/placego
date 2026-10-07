/* rule30_hw32.c: HW32, where the reference clock's debt comes from on the actual rooted tree: pulse windows or the
 * edges between them (Local's run; the census offered in L215 and put first by the draw-and-work rule; claimed in
 * CLOUD-LOCAL.md with these predictions pushed before the program was run).
 *
 * RUN-ON:  cpu (C, pthreads, 8 threads)
 * BUILD:   cc -O2 -pthread -o rule30_hw32 tests/probes/lexicon/rule30_hw32.c   (binary and transcripts outside Git)
 * COMMAND: ./rule30_hw32 BOUND
 *          stage A: BOUND = 1048577 (the RD32 frontier 2^20 included, seconds); stage B: BOUND = 26424115200 (TM6b's
 *          frontier, under an hour), run only if stage A's controls pass.
 *
 * Walk as rule30_rs32.c (common period 32 from the root (0, all ones) at depth 0; histories up to rotation; branches
 * spawn sibling walks; each walk followed to its exit or BOUND, on a thread pool). The clock is RD32's, as written
 * independently in rule30_rd32_check.py: T = 0 at the root; at depth d the driver w_d has delay 0 if w_d = 0, else
 * 1 + the least i >= 0 with w_d(T + i mod 32) = 1, and T advances by it. With z_d = 2 T_d - 5 d (doubled units), the
 * debt of a history is D = max over a <= b of z_b - z_a. Every walk carries its history's clock, minimum, debt and
 * witness, so a sibling inherits them at its spawn.
 *
 * A pulse is a driver that is a single black cell at its own least period p (p = 32 / popcount, the word
 * p-periodic).
 * An interval [a, b] contains a pulse when some w_j with a <= j <= b - 1 is one. The program keeps, per history, the
 * debt D, its first witness and whether that witness contains a pulse, and the largest debt over pulse-free intervals,
 * D_free. At each period-32 pulse it reads the window B, C, D, E (GC340, GC342, GC347): the four delays, L and M
 * from C, the source weight w = popcount(A), and the window's own four-edge debt.
 *
 * PREDICTIONS, Local's, published before either stage was run (blind unless marked):
 *   HW-C0 (control): at depth 2^20 the sixteen histories' (D, h) equal RD32's table (rule30_rd32_check.py),
 *          with h = z - min z.
 *          At stage B the RS32 counters recur: 73 walks, 17 live, 56 exits, 72 branches, steps32 436,983,015,918,
 *          and 3,260 singleton drivers at p = 32.
 *   HW-C1 (control, GC347 on actual data): every period-32 pulse window completed below BOUND has delays (k, L, 1, M),
 *          with L and M read from its C, and a source of weight above 3.
 *   HW-C2 (control, GC349): every such window's debt is at most q - 5/2 + max(0, q - w - 1/2).
 *   HW-P1 (blind): the mean delay over all period-32 steps lies in [1.98, 2.02] (a coin bit gives 2).
 *   HW-P2 (blind, uncertain): the stage's largest debt is attained only on intervals that contain a pulse:
 *          the largest pulse-free debt over all histories is below the largest debt.
 *   HW-P3 (blind, uncertain): the largest pulse-free debt over all histories exceeds the largest period-32 window
 *          debt.
 * OUTCOME, stage A, 2026-10-07 20:05 (M5, one run at commit 796d876, under 1 s; transcript outside Git). HW-C0
 * PASS: all sixteen histories' (D, h) at depth 2^20 equal RD32's table, and every first witness is RD32's (for
 * example [725127, 725155] for N_5 = 770,532 and 894,235). No period-32 pulse yet, so HW-C1 and HW-C2 are vacuous
 * here. Mean delay over period-32 steps 2.0045. At 2^20 the largest debt, 60, lies on intervals containing a pulse
 * (GC326's period-16 start at 725,146); the largest pulse-free debt is 45 (N_5 = 667,052, witness [798744,
 * 798770]); eight of the sixteen histories' first witnesses contain a pulse.  OUTCOME, stage B, 2026-10-07 20:37
 * (M5, one run at commit 796d876, 1,919 s on 8 threads; transcript outside Git). HW-C0 FAIL as coded, by a bug in
 * the check, not in the data: walks spawned after depth 2^20 inherit their parent's 2^20 snapshot, so the count
 * compared 73 records against 16. All 73 agreed with RD32's table, and every stage counter reproduced RS32 exactly
 * (73 walks, 17 live, 56 exits, 72 branches, steps32 436,983,015,918, 3,260 singleton drivers). The counter is
 * fixed after the run (own-snapshot flag) and the FAIL stands as recorded. HW-C1 PASS: all 3,260 period-32 pulse
 * windows have delays (k, L, 1, M) and sources of weight above 3. HW-C2 PASS: every window within GC349's charge.
 * HW-P1 HELD: mean delay 2.004525. HW-P2 REFUTED: the largest debt, 78.5 (walk 51, witness [25,849,986,140,
 * 25,849,986,179], 39 steps), is pulse-free, and so is every one of the 73 histories' largest-debt witness; each
 * history's D equals its D_free. HW-P3 HELD: largest pulse-free debt 78.5 against largest period-32 window debt
 * 37.0. Per history D at the frontier runs 71.5 to 78.5 for the deepest (mean 69.1 over 73), against 32.5 to 60 at
 * 2^20: the debt grows slowly with depth, and on this tree it lives between the pulse windows, not in them.
 * QUALIFICATION (GPT's GC361, 2026-10-07): at stage B the loop never processed depth F = BOUND, so D, D_free and
 * the witnesses are over intervals with right end at most F - 1. The 78.5 witness ends earlier and is unaffected; a
 * history's debt including the endpoint can be larger. D_end, reported from now on, includes it; rule30_hw32w.c's
 * run gives the stage-B values.
 */
#include <pthread.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAXW 4096
#define NTH 8
#define SNAP (1LL << 20)
#define GAP_RESET (1LL << 60)

typedef struct {
    uint32_t x, y; int64_t d; int id, parent, p32;
    int64_t T, zmin, zmin_d, D, wa, wb, last_pulse, gap_lo, Dfree, n5;
    int wpulse, snapown;
    int64_t Dend;
    int64_t D20, h20;
} walk_t;

static walk_t W[MAXW];
static int nw = 0, head = 0, active = 0, cap_hit = 0;
static int64_t BOUND;
static pthread_mutex_t mu = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t cv = PTHREAD_COND_INITIALIZER;
static long long T_steps32, T_dsum32, T_lit, T_br, T_db, T_ex, T_sing32, T_win, T_c1fail, T_c2fail, T_lowsrc;
static int64_t T_maxwin = -1, T_maxwin_d = -1;
static int nsnap = 0;

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

static inline int64_t delay(uint32_t w, int64_t T) { return w ? __builtin_ctz(rotr(w, (int)(T & 31))) + 1 : 0; }

static inline int is_pulse(uint32_t y) {
    int pc = __builtin_popcount(y);
    if (pc == 0 || 32 % pc) return 0;
    int p = 32 / pc;
    if (p & (p - 1)) return 0;
    return p == 32 || rotr(y, p) == y;
}

static int64_t debt4(const int64_t *ds) {
    int64_t z = 0, lo = 0, best = 0;
    for (int i = 0; i < 4; i++) {
        z += 2 * ds[i] - 5;
        if (z - lo > best) best = z - lo;
        if (z < lo) lo = z;
    }
    return best;
}

static void run_walk(int i) {
    pthread_mutex_lock(&mu);
    walk_t w = W[i];
    pthread_mutex_unlock(&mu);
    long long steps32 = 0, dsum32 = 0, lit = 0, br = 0, db = 0, ex = 0, sing = 0, win = 0, c1f = 0, c2f = 0, low = 0;
    int64_t maxwin = -1, maxwin_d = -1;
    /* the pending window: stage 0 none; 1 waiting for C; 2 for D; 3 for E */
    int wst = 0, ws = 0, wsrc = 0;
    int64_t wds[4], wL = 0, wM = 0, wdep = 0;
    uint32_t x = w.x, y = w.y;
    int64_t d = w.d;
    while (d < BOUND) {
        int64_t z = 2 * w.T - 5 * d;
        if (z - w.zmin > w.D) { w.D = z - w.zmin; w.wa = w.zmin_d; w.wb = d; w.wpulse = w.last_pulse >= w.zmin_d; }
        if (z < w.zmin) { w.zmin = z; w.zmin_d = d; }
        if (z - w.gap_lo > w.Dfree) w.Dfree = z - w.gap_lo;
        if (z < w.gap_lo) w.gap_lo = z;
        if (d == SNAP) {
            w.D20 = w.D; w.h20 = z - w.zmin; w.snapown = 1;
            pthread_mutex_lock(&mu); nsnap++; pthread_mutex_unlock(&mu);
        }
        if (y) {
            int64_t dl = delay(y, w.T);
            if (w.p32) { steps32++; dsum32 += dl; }
            if (wst) {                                            /* inside a period-32 pulse window */
                if (wst == 1) {
                    uint32_t C = y;
                    wL = __builtin_ctz(rotr(C, (ws + 1) & 31)) + 1;
                    int t = (ws + (int)wL) & 31;
                    uint32_t zeros = ~rotr(C, (t + 1) & 31);
                    wM = zeros ? __builtin_ctz(zeros) + 1 : 99;
                }
                wds[wst] = dl;
                if (++wst == 4) {
                    int ok = wds[1] == wL && wds[2] == 1 && wds[3] == wM && wsrc > 3;
                    if (!ok) c1f++;
                    int64_t wd = debt4(wds), cap = 2 * 32 - 5 + (2 * (32 - wsrc) - 1 > 0 ? 2 * (32 - wsrc) - 1 : 0);
                    if (wd > cap) c2f++;
                    if (wd > maxwin) { maxwin = wd; maxwin_d = wdep; }
                    win++;
                    wst = 0;
                }
            }
            int pulse = is_pulse(y);
            if (pulse && w.p32 && __builtin_popcount(y) == 1) {
                sing++;
                if (__builtin_popcount(x) <= 3) low++;
                if (!wst) { wst = 1; ws = __builtin_ctz(y); wsrc = __builtin_popcount(x); wds[0] = dl; wdep = d; }
            }
            if (pulse) { w.last_pulse = d; w.gap_lo = GAP_RESET; }   /* a sentinel far above any z; no overflow */
            w.T += dl;
            uint32_t c = child_nonzero(x, y);
            if (rotr(c, 1) != (x ^ (y | c))) lit++;
            x = y; y = c; d++;
            continue;
        }
        wst = 0;                                                  /* a zero driver ends any window unfinished */
        if (__builtin_popcount(x) & 1) {
            ex++;
            break;
        }
        uint32_t c1 = 0, run = 0;
        for (int t = 0; t < 32; t++) { c1 |= run << t; run ^= (x >> t) & 1; }
        uint32_t c2 = ~c1;
        if (rotr(c1, 1) != (x ^ c1) || rotr(c2, 1) != (x ^ c2)) lit++;
        if (is_rot(c1, c2)) {
            db++;
            if (d > 399 && !w.p32) { w.p32 = 1; w.n5 = d + 1; }
        } else {
            br++;
            pthread_mutex_lock(&mu);
            if (nw >= MAXW) cap_hit = 1;
            else {
                walk_t s = w;
                s.x = 0; s.y = c2; s.d = d + 1; s.id = nw; s.parent = w.id; s.snapown = 0;
                W[nw++] = s;
                pthread_cond_broadcast(&cv);
            }
            pthread_mutex_unlock(&mu);
        }
        x = 0; y = c1; d++;
    }
    w.Dend = w.D;                                                 /* GC361: include the frontier endpoint itself */
    if (d == BOUND) {
        int64_t zF = 2 * w.T - 5 * d, lo = w.zmin < zF ? w.zmin : zF;
        if (zF - lo > w.Dend) w.Dend = zF - lo;
    }
    pthread_mutex_lock(&mu);
    w.x = x; w.y = y; w.d = d < BOUND ? -1 - d : d;               /* exited walks keep -(exit depth) - 1 */
    W[i] = w;
    T_steps32 += steps32; T_dsum32 += dsum32; T_lit += lit; T_br += br; T_db += db; T_ex += ex; T_sing32 += sing;
    T_win += win; T_c1fail += c1f; T_c2fail += c2f; T_lowsrc += low;
    if (maxwin > T_maxwin) { T_maxwin = maxwin; T_maxwin_d = maxwin_d; }
    pthread_mutex_unlock(&mu);
}

static void *worker(void *arg) {
    (void)arg;
    for (;;) {
        pthread_mutex_lock(&mu);
        while (head == nw && active > 0) pthread_cond_wait(&cv, &mu);
        if (head == nw) { pthread_cond_broadcast(&cv); pthread_mutex_unlock(&mu); return 0; }
        int i = head++;
        active++;
        pthread_mutex_unlock(&mu);
        run_walk(i);
        pthread_mutex_lock(&mu);
        active--;
        pthread_cond_broadcast(&cv);
        pthread_mutex_unlock(&mu);
    }
}

/* RD32's table at depth 2^20 (rule30_rd32_check.py): N_5 -> doubled D, doubled h */
static const int64_t RD[16][3] = {{87867, 65, 0}, {183184, 80, 0}, {196189, 81, 20}, {229338, 87, 4},
    {253537, 79, 8}, {271596, 79, 7}, {291257, 73, 0}, {527724, 79, 7}, {551910, 79, 7}, {555813, 79, 4},
    {575211, 85, 1}, {634886, 80, 0}, {645655, 79, 15}, {667052, 90, 0}, {770532, 120, 7}, {894235, 120, 0}};

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: rule30_hw32 BOUND\n"); return 1; }
    BOUND = atoll(argv[1]);
    time_t t0 = time(0);
    W[nw++] = (walk_t){.x = 0, .y = 0xFFFFFFFFu, .d = 0, .id = 0, .parent = -1, .p32 = 0, .T = 0, .zmin = 0,
                       .zmin_d = 0, .D = 0, .wa = 0, .wb = 0, .last_pulse = -1, .gap_lo = 0, .Dfree = 0, .n5 = 0,
                       .wpulse = 0, .snapown = 0, .D20 = -1, .h20 = -1};
    printf("HW32 start: BOUND %lld, %d threads\n", (long long)BOUND, NTH);
    fflush(stdout);
    pthread_t th[NTH];
    for (int k = 0; k < NTH; k++) pthread_create(&th[k], 0, worker, 0);
    for (int k = 0; k < NTH; k++) pthread_join(th[k], 0);
    int live = 0;
    for (int i = 0; i < nw; i++) live += W[i].d >= 0;
    printf("walks %d live %d exits %lld branches %lld doublings %lld steps32 %lld literal_fail %lld cap_hit %d "
           "elapsed %.0f s\n", nw, live, T_ex, T_br, T_db, T_steps32, T_lit, cap_hit, difftime(time(0), t0));
    /* HW-C0 */
    int c0 = T_lit == 0 && !cap_hit;
    if (BOUND > SNAP) {
        int matched = 0;
        for (int i = 0; i < nw; i++) {
            if (W[i].D20 < 0 || !W[i].snapown) continue;   /* fixed after stage B: own snapshots only */
            int hit = 0;
            for (int k = 0; k < 16; k++)
                if (W[i].n5 == RD[k][0]) hit = W[i].D20 == RD[k][1] && W[i].h20 == RD[k][2];
            matched += hit;
        }
        printf("RD32 table at 2^20: %d of 16 histories agree (snapshots %d)\n", matched, nsnap);
        c0 &= matched == 16 && nsnap == 16;
    }
    if (BOUND == 26424115200LL)
        c0 &= nw == 73 && live == 17 && T_ex == 56 && T_br == 72 && T_steps32 == 436983015918LL && T_sing32 == 3260;
    printf("HW-C0 %s\n", c0 ? "PASS" : "FAIL");
    printf("period-32 windows completed %lld; singleton drivers %lld (sources of weight <= 3: %lld)\n", T_win, T_sing32,
           T_lowsrc);
    printf("HW-C1 %s (%lld failures)\n", T_c1fail == 0 && T_lowsrc == 0 ? "PASS" : "FAIL", T_c1fail);
    printf("HW-C2 %s (%lld failures)\n", T_c2fail == 0 ? "PASS" : "FAIL", T_c2fail);
    double mean = T_steps32 ? (double)T_dsum32 / (double)T_steps32 : 0;
    printf("mean delay over period-32 steps %.6f\n", mean);
    int64_t Dmax = -1, Dfmax = -1;
    int arg = -1, pulsewit = 0;
    for (int i = 0; i < nw; i++) {
        walk_t *v = &W[i];
        printf("HIST walk %d parent %d N5 %lld end %s %lld D %.1f D_free %.1f witness [%lld, %lld] pulse %d "
               "D_end %.1f\n", v->id,
               v->parent, (long long)v->n5, v->d >= 0 ? "live" : "exit", (long long)(v->d >= 0 ? v->d : -1 - v->d),
               v->D / 2.0, v->Dfree / 2.0, (long long)v->wa, (long long)v->wb, v->wpulse, v->Dend / 2.0);
        if (v->D > Dmax) { Dmax = v->D; arg = i; }
        if (v->Dfree > Dfmax) Dfmax = v->Dfree;
    }
    for (int i = 0; i < nw; i++) pulsewit += W[i].D == Dmax && W[i].wpulse;
    printf("histories attaining the largest debt whose first witness contains a pulse: %d\n", pulsewit);
    printf("largest debt %.1f (walk %d, witness [%lld, %lld]); largest pulse-free debt %.1f; largest period-32 window "
           "debt %.1f (pulse at depth %lld)\n", Dmax / 2.0, W[arg].id, (long long)W[arg].wa, (long long)W[arg].wb,
           Dfmax / 2.0, T_maxwin / 2.0, (long long)T_maxwin_d);
    if (BOUND == 26424115200LL) {
        printf("HW-P1 %s\n", mean >= 1.98 && mean <= 2.02 ? "HELD" : "REFUTED");
        printf("HW-P2 %s\n", Dfmax < Dmax ? "HELD" : "REFUTED");
        printf("HW-P3 %s\n", Dfmax > T_maxwin ? "HELD" : "REFUTED");
    }
    return 0;
}
