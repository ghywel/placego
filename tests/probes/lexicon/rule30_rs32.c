/* rule30_rs32.c: RS32, the census of named pulse starts (RS16, rule30_rs16.py) carried into the rooted period-32
 * stage along TM6b's walks (Local's run, after RS16; claimed in CLOUD-LOCAL.md with these predictions pushed before
 * the program was run).
 *
 * RUN-ON:  cpu (C, pthreads, 8 threads)
 * BUILD:   cc -O2 -pthread -o rule30_rs32 tests/probes/lexicon/rule30_rs32.c   (binary and transcripts outside Git)
 * COMMAND: ./rule30_rs32 BOUND [TM6B_TRANSCRIPT]
 *          stage A: BOUND = 134217728 (2^27, minutes); stage B: BOUND = 26424115200 (TM6b's certified frontier,
 *          about half an hour on 8 threads), run only if stage A's controls pass.
 *
 * Walk exactly as rule30_tm6b.c (common period Q = 32 from the root (0, all ones) at depth 0; nonzero drivers have a
 * unique child; a zero driver with odd parity exits to period 64; with even parity its two children are followed,
 * once if they are rotations of each other (doubling), both ways otherwise (branch, spawning a sibling walk at depth
 * d + 1 from (0, c2)); the literal equation checked on every transition). Each walk is followed until its exit or
 * depth BOUND. Walks are independent, so they run on a pool of threads; walk ids differ from TM6b's, so events are
 * compared as (depth, kind, driver), ignoring ids.
 *
 * At every state (x, y) with y nonzero the start test of RS16 is made at the pair's least period p (p divides 32): a
 * start is (e_s + e_(s+r), e_s) on the p-bit words, 1 <= r <= p - 1. Each walk carries the (p, r) classes seen on its
 * whole history (inherited by a sibling at its spawn). The program also counts singleton-driver states at p = 32
 * (popcount(y) = 1 after the walk's entry to period 32) with their predecessor weights.
 *
 * PREDICTIONS, Local's, published before either stage was run (blind unless marked):
 *   RS32-C0 (control): with TM6b's transcript given, its EVENT lines below BOUND (exits, branches, doublings above
 *           depth 399) are reproduced exactly as (depth, kind, driver); literal failures 0. At stage B the totals
 *           equal TM6b's STOP and last PROGRESS lines: steps32 436,983,015,918, zeros32 113, exits 56, branches 72,
 *           doublings 20, 73 walks, 17 live.
 *   RS32-C1 (control, RS16): the two starts of the period-16 stage recur, (p 2, r 1) at depth 5 and (p 16, r 2) at
 *           depth 725,146, and no other start with p < 32 occurs.
 *   RS32-C2 (control, G156): no (p, r) class twice on any walk's history.
 *   RS32-P1 (blind): stage A finds no start at p = 32.
 *   RS32-P2 (blind, uncertain): stage B finds at least 1 and at most 10 start nodes at p = 32.
 *   RS32-P3 (blind, uncertain): at stage B the singleton-driver count at p = 32 lies between 1/4 and 1 times the
 *           uniform expectation 32 * steps32 / 2^32 (about 3,256 at TM6b's steps32).
 *   RS32-P4 (blind, uncertain): at stage B the median predecessor weight over those singleton-driver states lies
 *           between 12 and 20 (RS16's post hoc count put most at 6 to 10 of 16 bits, near q/2).
 * OUTCOME, stage A, 2026-10-07 19:07 (M5, one run at commit 7b05961, 8 s on 8 threads; transcript outside Git).
 * RS32-C0 PASS: 16 walks, the 33 TM6b events below 2^27 reproduced exactly as (depth, kind, driver), literal
 * failures 0, steps32 2,043,501,457. RS32-C1 PASS: (p 2, r 1) at depth 5 and (p 16, r 2) at 725,146, no other start
 * below p = 32. RS32-C2 PASS. RS32-P1 HELD: no start at p = 32. Singleton-driver states at p = 32: 13 against a
 * uniform 15.2; predecessor weights 8, 12, 13, 15 (3), 17 (2), 18 (3), 19, 20, median 17; the driver inside the
 * predecessor at 8 of 13. Stage B: running.
 */
#include <pthread.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAXW 4096
#define MAXEV 20000
#define MAXST 4096
#define NTH 8

typedef struct { uint32_t x, y; int64_t d; int id, parent, p32; uint32_t seen[6]; } walk_t;
typedef struct { int64_t d; int kind; uint32_t driver; } event_t;          /* kind: 0 exit, 1 branch, 2 doubling */
typedef struct { int64_t d; int p, r, walk; uint32_t x, y; } start_t;

static walk_t W[MAXW];
static int nw = 0, head = 0, active = 0, cap_hit = 0;
static int64_t BOUND;
static pthread_mutex_t mu = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t cv = PTHREAD_COND_INITIALIZER;
static event_t EV[MAXEV];
static int nev = 0;
static start_t ST[MAXST];
static int nst = 0;
static long long T_steps32, T_zeros32, T_literal, T_branches, T_doublings, T_exits, T_sing32, T_g156;
static long long T_wt[33], T_wt_in[33];

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

static int lg(int p) { int k = 0; while ((1 << k) < p) k++; return k; }

/* 1 if (x, y) is a named start at its least pair period; sets p and r */
static int start_test(uint32_t x, uint32_t y, int *pp, int *rr) {
    int py = __builtin_popcount(y), px = __builtin_popcount(x);
    if (px != 2 * py || py == 0 || 32 % py) return 0;
    int p = 32 / py;
    if (p & (p - 1)) return 0;
    if (p < 32 && (rotr(x, p) != x || rotr(y, p) != y)) return 0;
    uint32_t m = p == 32 ? 0xFFFFFFFFu : ((1u << p) - 1);
    uint32_t xs = x & m, ys = y & m;
    if (__builtin_popcount(ys) != 1 || __builtin_popcount(xs) != 2 || (xs & ys) != ys) return 0;
    int s = __builtin_ctz(ys), o = __builtin_ctz(xs ^ ys);
    *pp = p;
    *rr = ((o - s) % p + p) % p;
    return 1;
}

static void add_event(int64_t d, int kind, uint32_t driver) {
    if (nev < MAXEV) EV[nev++] = (event_t){d, kind, driver}; else cap_hit = 1;
}

static void run_walk(int i) {
    pthread_mutex_lock(&mu);
    walk_t w = W[i];
    pthread_mutex_unlock(&mu);
    long long steps32 = 0, zeros32 = 0, lit = 0, br = 0, db = 0, ex = 0, sing = 0, g156 = 0;
    long long wt[33] = {0}, wt_in[33] = {0};
    uint32_t x = w.x, y = w.y;
    int64_t d = w.d;
    while (d < BOUND) {
        if (y) {
            int p, r;
            if (w.p32 && __builtin_popcount(y) == 1) {
                sing++;
                wt[__builtin_popcount(x)]++;
                if (x & y) wt_in[__builtin_popcount(x)]++;
            }
            if (start_test(x, y, &p, &r)) {
                uint32_t bitr = 1u << r;
                if (w.seen[lg(p)] & bitr) g156++;
                w.seen[lg(p)] |= bitr;
                pthread_mutex_lock(&mu);
                if (nst < MAXST) ST[nst++] = (start_t){d, p, r, w.id, x, y}; else cap_hit = 1;
                pthread_mutex_unlock(&mu);
            }
            if (w.p32) steps32++;
            uint32_t c = child_nonzero(x, y);
            if (rotr(c, 1) != (x ^ (y | c))) lit++;
            x = y; y = c; d++;
            continue;
        }
        if (w.p32) zeros32++;
        if (__builtin_popcount(x) & 1) {
            ex++;
            pthread_mutex_lock(&mu);
            add_event(d, 0, x);
            pthread_mutex_unlock(&mu);
            break;
        }
        uint32_t c1 = 0, run = 0;
        for (int t = 0; t < 32; t++) { c1 |= run << t; run ^= (x >> t) & 1; }
        uint32_t c2 = ~c1;
        if (rotr(c1, 1) != (x ^ c1) || rotr(c2, 1) != (x ^ c2)) lit++;
        if (is_rot(c1, c2)) {
            db++;
            if (d > 399) {
                w.p32 = 1;
                pthread_mutex_lock(&mu);
                add_event(d, 2, 0);
                pthread_mutex_unlock(&mu);
            }
        } else {
            br++;
            pthread_mutex_lock(&mu);
            add_event(d, 1, x);
            if (nw >= MAXW) cap_hit = 1;
            else {
                walk_t s = w;
                s.x = 0; s.y = c2; s.d = d + 1; s.id = nw; s.parent = w.id;
                W[nw++] = s;
                pthread_cond_broadcast(&cv);
            }
            pthread_mutex_unlock(&mu);
        }
        x = 0; y = c1; d++;
    }
    pthread_mutex_lock(&mu);
    W[i].x = x; W[i].y = y; W[i].d = d < BOUND ? -1 : d;      /* -1: exited */
    T_steps32 += steps32; T_zeros32 += zeros32; T_literal += lit; T_branches += br; T_doublings += db;
    T_exits += ex; T_sing32 += sing; T_g156 += g156;
    for (int k = 0; k <= 32; k++) { T_wt[k] += wt[k]; T_wt_in[k] += wt_in[k]; }
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

static int cmp_ev(const void *a, const void *b) {
    const event_t *u = a, *v = b;
    if (u->d != v->d) return u->d < v->d ? -1 : 1;
    if (u->kind != v->kind) return u->kind - v->kind;
    return u->driver < v->driver ? -1 : u->driver > v->driver;
}

static int cmp_st(const void *a, const void *b) {
    const start_t *u = a, *v = b;
    if (u->d != v->d) return u->d < v->d ? -1 : 1;
    return u->x < v->x ? -1 : u->x > v->x;
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: rule30_rs32 BOUND [TM6B_TRANSCRIPT]\n"); return 1; }
    BOUND = atoll(argv[1]);
    time_t t0 = time(0);
    W[nw++] = (walk_t){0, 0xFFFFFFFFu, 0, 0, -1, 0, {0}};
    printf("RS32 start: Q = 32, BOUND %lld, %d threads\n", (long long)BOUND, NTH);
    fflush(stdout);
    pthread_t th[NTH];
    for (int k = 0; k < NTH; k++) pthread_create(&th[k], 0, worker, 0);
    for (int k = 0; k < NTH; k++) pthread_join(th[k], 0);
    double el = difftime(time(0), t0);
    int live = 0;
    for (int i = 0; i < nw; i++) live += W[i].d >= 0;
    printf("walks %d live %d exits %lld branches %lld doublings %lld zeros32 %lld steps32 %lld literal_fail %lld "
           "cap_hit %d elapsed %.0f s\n", nw, live, T_exits, T_branches, T_doublings, T_zeros32, T_steps32, T_literal,
           cap_hit, el);
    qsort(EV, nev, sizeof(event_t), cmp_ev);
    qsort(ST, nst, sizeof(start_t), cmp_st);
    int c0 = T_literal == 0 && !cap_hit;
    if (argc > 2) {
        FILE *f = fopen(argv[2], "r");
        if (!f) { printf("RS32-C0 FAIL: cannot open the TM6b transcript\n"); c0 = 0; }
        else {
            static event_t R[MAXEV];
            int nr = 0;
            char line[512];
            while (fgets(line, sizeof line, f)) {
                long long d; char kind[16];
                if (sscanf(line, "EVENT %lld %15s", &d, kind) != 2 || d >= BOUND) continue;
                unsigned drv = 0;
                char *q = strstr(line, "driver ");
                if (q) sscanf(q, "driver %u", &drv);
                int k = !strcmp(kind, "exit") ? 0 : !strcmp(kind, "branch") ? 1 : 2;
                if (nr < MAXEV) R[nr++] = (event_t){d, k, k == 2 ? 0 : drv};
            }
            fclose(f);
            qsort(R, nr, sizeof(event_t), cmp_ev);
            int same = nr == nev;
            for (int i = 0; same && i < nr; i++) same = !cmp_ev(&R[i], &EV[i]);
            printf("events below BOUND: this run %d, TM6b %d, %s\n", nev, nr, same ? "identical" : "DIFFERENT");
            c0 &= same;
        }
    } else c0 = 0;
    if (BOUND == 26424115200LL)
        c0 &= T_steps32 == 436983015918LL && T_zeros32 == 113 && T_exits == 56 && T_branches == 72 && T_doublings == 20
              && nw == 73 && live == 17;
    printf("RS32-C0 %s\n", c0 ? "PASS" : "FAIL");
    int c1 = 0, low_other = 0, n32 = 0;
    for (int i = 0; i < nst; i++) {
        start_t *s = &ST[i];
        printf("START depth %lld p %d r %d walk %d (%u, %u)\n", (long long)s->d, s->p, s->r, s->walk, s->x, s->y);
        if (s->p == 32) n32++;
        else if ((s->d == 5 && s->p == 2 && s->r == 1) || (s->d == 725146 && s->p == 16 && s->r == 2)) c1++;
        else low_other++;
    }
    printf("RS32-C1 %s\n", c1 == 2 && !low_other ? "PASS" : "FAIL");
    printf("RS32-C2 %s\n", T_g156 == 0 ? "PASS" : "FAIL");
    printf("start nodes at p = 32: %d\n", n32);
    double unif = 32.0 * (double)T_steps32 / 4294967296.0;
    printf("singleton-driver states at p = 32: %lld; uniform expectation %.1f; ratio %.3f\n", T_sing32, unif,
           unif > 0 ? T_sing32 / unif : 0.0);
    long long half = (T_sing32 + 1) / 2, acc = 0;
    int med = -1;
    printf("predecessor weights (weight: count, of which the driver lies inside):");
    for (int k = 0; k <= 32; k++) {
        if (T_wt[k]) printf(" %d:%lld/%lld", k, T_wt[k], T_wt_in[k]);
        acc += T_wt[k];
        if (med < 0 && T_sing32 && acc >= half) med = k;
    }
    printf("\nmedian predecessor weight %d\n", med);
    if (BOUND == 134217728LL) printf("RS32-P1 %s\n", n32 == 0 ? "HELD" : "REFUTED");
    if (BOUND == 26424115200LL) {
        printf("RS32-P2 %s\n", n32 >= 1 && n32 <= 10 ? "HELD" : "REFUTED");
        printf("RS32-P3 %s\n", T_sing32 >= unif / 4 && T_sing32 <= unif ? "HELD" : "REFUTED");
        printf("RS32-P4 %s\n", med >= 12 && med <= 20 ? "HELD" : "REFUTED");
    }
    return 0;
}
