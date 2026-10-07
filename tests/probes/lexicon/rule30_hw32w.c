/* rule30_hw32w.c: HW32w, the drivers of HW32's largest debt witness (Local's run; offered in L218 and taken first
 * under draw-and-work; claimed in CLOUD-LOCAL.md with these predictions pushed before the program was run).
 *
 * RUN-ON:  cpu (C, pthreads, 8 threads)
 * BUILD:   cc -O2 -pthread -o rule30_hw32w tests/probes/lexicon/rule30_hw32w.c   (binary and transcript outside Git)
 * COMMAND: ./rule30_hw32w 26424115200 25849986140 25849986179
 *
 * rule30_hw32.c unchanged (its own-snapshot counter included), plus one thing: every walk that processes a depth d with
 * A <= d <= B (the second and third arguments) records (d, x, y, delay, z) there; at the end the program prints the
 * records of every walk whose largest-debt witness is exactly [A, B]. HW32's stage B found the largest debt, 78.5, on
 * the witness [25849986140, 25849986179] of the history with N_5 = 551,910 that is live at the frontier.
 *
 * PREDICTIONS, Local's, published before the run (blind unless marked):
 *   W-C0 (control): the run reproduces HW32 stage B: the same counters, the largest debt 78.5 with witness [A, B],
 *        and C0 now PASS (16 of 16 own snapshots).
 *   W-C1 (control): on the printed history, z(B) - z(A) = 157 (doubled units), and no driver in [A, B - 1] is a pulse.
 *   W-P1 (blind, uncertain): the 39 drivers' mean popcount is below 16 (long resets from lighter words).
 *   W-P2 (blind, uncertain): at least one driver in the witness has a reset delay of 10 or more.
 * OUTCOME: not yet run.
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
    int64_t D20, h20;
    int nrec; int64_t rec[64][5];
} walk_t;

static walk_t W[MAXW];
static int nw = 0, head = 0, active = 0, cap_hit = 0;
static int64_t BOUND, TA = -1, TB = -1;
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
        if (d >= TA && d <= TB && w.nrec < 64) {
            int64_t dl0 = y ? (int64_t)(__builtin_ctz(rotr(y, (int)(w.T & 31))) + 1) : 0;
            w.rec[w.nrec][0] = d; w.rec[w.nrec][1] = x; w.rec[w.nrec][2] = y; w.rec[w.nrec][3] = dl0;
            w.rec[w.nrec][4] = z; w.nrec++;
        }
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
    if (argc < 2) { fprintf(stderr, "usage: rule30_hw32w BOUND A B\n"); return 1; }
    BOUND = atoll(argv[1]);
    if (argc > 3) { TA = atoll(argv[2]); TB = atoll(argv[3]); }
    time_t t0 = time(0);
    W[nw++] = (walk_t){.x = 0, .y = 0xFFFFFFFFu, .d = 0, .id = 0, .parent = -1, .p32 = 0, .T = 0, .zmin = 0,
                       .zmin_d = 0, .D = 0, .wa = 0, .wb = 0, .last_pulse = -1, .gap_lo = 0, .Dfree = 0, .n5 = 0,
                       .wpulse = 0, .snapown = 0, .D20 = -1, .h20 = -1};
    printf("HW32w start: BOUND %lld, %d threads\n", (long long)BOUND, NTH);
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
        printf("HIST walk %d parent %d N5 %lld end %s %lld D %.1f D_free %.1f witness [%lld, %lld] pulse %d\n", v->id,
               v->parent, (long long)v->n5, v->d >= 0 ? "live" : "exit", (long long)(v->d >= 0 ? v->d : -1 - v->d),
               v->D / 2.0, v->Dfree / 2.0, (long long)v->wa, (long long)v->wb, v->wpulse);
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
    for (int i = 0; i < nw; i++) {
        walk_t *v = &W[i];
        if (v->wa != TA || v->wb != TB) continue;
        int pulses = 0;
        printf("WITNESS walk %d N5 %lld D %.1f records %d\n", v->id, (long long)v->n5, v->D / 2.0, v->nrec);
        for (int r = 0; r < v->nrec; r++) {
            uint32_t yy = (uint32_t)v->rec[r][2];
            if (v->rec[r][0] < TB) pulses += is_pulse(yy);
            printf("REC d %lld x %08x y %08x pc %d delay %lld z %lld\n", (long long)v->rec[r][0],
                   (unsigned)v->rec[r][1], yy, __builtin_popcount(yy), (long long)v->rec[r][3],
                   (long long)v->rec[r][4]);
        }
        if (v->nrec) printf("rise z(B) - z(A) = %lld; pulses in [A, B - 1]: %d\n",
                            (long long)(v->rec[v->nrec - 1][4] - v->rec[0][4]), pulses);
    }
    return 0;
}
