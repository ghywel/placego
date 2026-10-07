/* rule30_aw5d.c: AW5d, a depth-first cycle search for a periodic right continuation of one pair of columns (Local's run,
 * after AW5 and AW5c; claimed in CLOUD-LOCAL.md with these predictions pushed before the program was run).
 *
 * BUILD:   cc -O2 -o rule30_aw5d tests/probes/lexicon/rule30_aw5d.c          (binary outside Git)
 * COMMAND: ./rule30_aw5d P C0 C1 [H=1]      (searches period P*H with the pair repeated H times)
 * COST:    seconds to minutes; caps 30,000,000 visited pairs (about 0.9 GiB) and 900 CPU s per search.
 *
 * Graph as in rule30_aw5.py: from the pair (u, v) of period-Q words (Q = P*H), the next column w must satisfy
 * v(t + 1) = u(t) XOR (v(t) OR w(t)); where v(t) = 1 this needs v(t + 1) = u(t) XOR 1 and leaves w(t) free, and where
 * v(t) = 0 it fixes w(t). A depth-first search from the start colours pairs grey on the stack and black when finished;
 * an edge to a grey pair closes a cycle, which is reachable from the start, so the start has a real right continuation
 * (a path into a cycle of Q-periodic columns). The witness columns are printed and every consecutive triple is checked
 * by the literal equation in the program. Exhausting the search without a grey edge proves there is no Q-periodic
 * continuation (and nothing about other periods).
 *
 * PREDICTIONS, Local's, published before the run (blind unless marked):
 *   D-C1 (control): the P = 5 pair (1, 25) is certified at period 5.
 *   D-C2 (control): AW5's exhausted case (146, 155) at period 10 is exhausted here too, with no cycle.
 *   D-P1 (blind, uncertain): at least one of AW4's ten P = 10 survivors gets a cycle at period 20 within the caps.
 *   D-P2 (blind, uncertain): if none at period 20, at least one at period 30.
 * A cap hit leaves the pair undecided. Every certificate is checked literally before it is reported.
 * OUTCOME: not yet run.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define TBITS 26
#define TSIZE (1u << TBITS)
#define MAXV 30000000u

static int Q;
static uint32_t FULL;
static uint64_t *keys;
static uint8_t *col;                 /* 0 empty, 1 grey, 2 black */

static inline uint32_t rotr1(uint32_t w) { return ((w >> 1) | (w << (Q - 1))) & FULL; }

static uint32_t slot(uint64_t k) {
    uint64_t h = k * 0x9E3779B97F4A7C15ULL;
    uint32_t i = (uint32_t)(h >> (64 - TBITS));
    while (col[i] && keys[i] != k) i = (i + 1) & (TSIZE - 1);
    return i;
}

static int literal(uint32_t u, uint32_t v, uint32_t w) {
    for (int t = 0; t < Q; t++) {
        int vt1 = (v >> ((t + 1) % Q)) & 1, ut = (u >> t) & 1, vt = (v >> t) & 1, wt = (w >> t) & 1;
        if (vt1 != (ut ^ (vt | wt))) return 0;
    }
    return 1;
}

typedef struct { uint32_t u, v, base, sub; int first; } frame;

/* returns 1 certified, 0 exhausted, -1 cap */
static int search(uint32_t c0, uint32_t c1, long long *visited) {
    memset(col, 0, TSIZE);
    frame *st = malloc(sizeof(frame) * (size_t)MAXV);
    long long top = 0, nvis = 0;
    clock_t t0 = clock();
    uint64_t k0 = ((uint64_t)c0 << 32) | c1;
    uint32_t s0 = slot(k0);
    keys[s0] = k0; col[s0] = 1; nvis = 1;
    st[0] = (frame){c0, c1, 0, 0, 1};
    while (top >= 0) {
        frame *f = &st[top];
        if (f->first) {
            uint32_t need = rotr1(f->v) ^ f->u;
            f->first = 0;
            if (f->v & ~need & FULL) {          /* no successor */
                col[slot(((uint64_t)f->u << 32) | f->v)] = 2; top--; continue;
            }
            f->base = need & ~f->v & FULL;
            f->sub = f->v;                       /* iterate subsets of v downward, ending after 0 */
        } else {
            if (f->sub == 0) { col[slot(((uint64_t)f->u << 32) | f->v)] = 2; top--; continue; }
            f->sub = (f->sub - 1) & f->v;
        }
        uint32_t w = f->base | f->sub;
        uint64_t k = ((uint64_t)f->v << 32) | w;
        uint32_t s = slot(k);
        if (col[s] == 1) {                       /* back edge: a cycle reachable from the start */
            int ok = 1;
            printf("CYCLE: path of %lld columns from the start, closing at the pair (%u, %u)\n", top + 2, f->v, w);
            printf("  columns:");
            for (long long i = 0; i <= top; i++) printf(" %u", st[i].u);
            printf(" %u %u\n", st[top].v, w);
            for (long long i = 0; i < top; i++) ok &= literal(st[i].u, st[i].v, st[i + 1].v);
            ok &= literal(st[top].u, st[top].v, w);
            /* the closing pair (v, w) is grey: it lies on the stack, so the cycle is the stack segment from it */
            printf("  literal equation along the path: %s\n", ok ? "PASS" : "FAIL");
            *visited = nvis; free(st);
            return ok ? 1 : -2;
        }
        if (col[s] == 2) continue;
        if (nvis >= MAXV || (double)(clock() - t0) / CLOCKS_PER_SEC > 900) { *visited = nvis; free(st); return -1; }
        keys[s] = k; col[s] = 1; nvis++;
        st[++top] = (frame){f->v, w, 0, 0, 1};
    }
    *visited = nvis; free(st);
    return 0;
}

int main(int argc, char **argv) {
    int P = atoi(argv[1]), H = argc > 4 ? atoi(argv[4]) : 1;
    uint32_t c0 = (uint32_t)atoi(argv[2]), c1 = (uint32_t)atoi(argv[3]);
    Q = P * H;
    FULL = Q == 32 ? 0xFFFFFFFFu : ((1u << Q) - 1);
    uint32_t r0 = 0, r1 = 0;
    for (int i = 0; i < H; i++) { r0 |= c0 << (P * i); r1 |= c1 << (P * i); }
    keys = malloc(sizeof(uint64_t) * TSIZE); col = malloc(TSIZE);
    long long nv = 0;
    int r = search(r0, r1, &nv);
    printf("pair (%u, %u) at period %d: %s; visited %lld\n", c0, c1, Q,
           r == 1 ? "CERTIFIED (a reachable cycle)" : r == 0 ? "exhausted: no continuation of this period"
           : r == -1 ? "CAP: undecided" : "LITERAL FAILURE", nv);
    return 0;
}
