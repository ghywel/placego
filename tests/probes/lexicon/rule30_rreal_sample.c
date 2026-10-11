/* rule30_rreal_sample.c: lower bounds on R_real(d) by sampling random right halves (CL260's instrument change).
 *
 * BUILD:   cc -O3 $(OMP flags) -o rreal_sample tests/probes/lexicon/rule30_rreal_sample.c   (rule30_rreal_sample.py)
 * USAGE:   ./rreal_sample PHASE T NROUNDS SEED DMIN DMAX WITNESS_FILE
 *          Column 0 is clamped to (t + PHASE) mod 2 for t = 0 .. T. Each sample is a uniformly random right half,
 *          sites 1 .. T + 1. The right half runs forward against the clamp, which gives column 1 at times 0 .. T - 1;
 *          the forced left half follows sideways, x_t(-k) = x_{t+1}(-k+1) XOR (x_t(-k+1) OR x_t(-k+2)), so row 0
 *          is known to depth T and column 0 follows the clamp through T. For each depth d in DMIN .. DMAX the sample
 *          gives R_real(d) >= L when row 0 is white at depths d .. d + L - 1 (d + L - 1 <= T): the clock holds
 *          through d + L - 1, which is the definition (rule30_witness_check.py, L596).
 *          Samples are bit-sliced, 256 to a batch; round r runs 2^(r-1) batches (round 0 runs one), so the
 *          cumulative count doubles each round. After every round: "C samples" then "R d best" for each depth.
 *          Each improvement keeps its witness; at the end WITNESS_FILE gets lines "W d L PHASE LEFT RIGHT" with
 *          LEFT = cells -(d+L-1) .. 0 and RIGHT = sites 1 .. d+L-1, the checker's format.
 *          The batch's random bits depend only on (SEED, batch index), so a run is reproducible at any thread count.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _OPENMP
#include <omp.h>
#endif

typedef uint64_t V __attribute__((vector_size(32)));     /* 4 x 64 = 256 samples */
#define LANES 4
#define NS (64 * LANES)

static inline uint64_t splitmix64(uint64_t *s) {
    uint64_t z = (*s += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL; z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static inline int vzero(V v) { return (v[0] | v[1] | v[2] | v[3]) == 0; }
static inline int vbit(V v, int s) { return (int)((v[s >> 6] >> (s & 63)) & 1); }
static inline int vfirst(V v) {
    for (int l = 0; l < LANES; l++) if (v[l]) return 64 * l + __builtin_ctzll(v[l]);
    return -1;
}

typedef struct { int L; char *left, *right; } Wit;

int main(int argc, char **argv) {
    if (argc != 8) { fprintf(stderr, "usage: PHASE T NROUNDS SEED DMIN DMAX WITNESS_FILE\n"); return 2; }
    int ph = atoi(argv[1]), T = atoi(argv[2]), NR = atoi(argv[3]);
    uint64_t seed = strtoull(argv[4], 0, 10);
    int DMIN = atoi(argv[5]), DMAX = atoi(argv[6]);
    if (DMIN < 1 || DMAX > T || DMIN > DMAX || NR < 1 || NR > 40) { fprintf(stderr, "bad arguments\n"); return 2; }
    int ND = DMAX - DMIN + 1;
    Wit *best = calloc(ND, sizeof(Wit));
    for (int i = 0; i < ND; i++) best[i].L = 0;
    long long done = 0;
    for (int r = 0; r < NR; r++) {
        long long nb = r == 0 ? 1 : (1LL << (r - 1));
        long long b0 = done;
#pragma omp parallel
        {
            V *rr = malloc(sizeof(V) * (T + 3)), *r0 = malloc(sizeof(V) * (T + 3)), *c1 = malloc(sizeof(V) * (T + 2));
            V *ap = malloc(sizeof(V) * (T + 2)), *aq = malloc(sizeof(V) * (T + 2)), *an = malloc(sizeof(V) * (T + 2));
            V *row = malloc(sizeof(V) * (T + 2));            /* row[k] = x_0(-k), k = 0 .. T */
            Wit *mine = calloc(ND, sizeof(Wit));
            V one = {~0ULL, ~0ULL, ~0ULL, ~0ULL}, zero = {0, 0, 0, 0};
#pragma omp for schedule(dynamic, 1)
            for (long long b = b0; b < b0 + nb; b++) {
                uint64_t s = seed * 0xD1342543DE82EF95ULL + (uint64_t)b * 0x9E3779B97F4A7C15ULL + 1;
                for (int i = 1; i <= T + 1; i++)
                    for (int l = 0; l < LANES; l++) r0[i][l] = splitmix64(&s);
                memcpy(rr, r0, sizeof(V) * (T + 3));
                rr[T + 2] = zero;
                for (int t = 0; t <= T; t++) {                   /* right half against the clamp; column 1 */
                    c1[t] = rr[1];
                    if (t == T) break;
                    V prev = ((t + ph) & 1) ? one : zero;        /* x_t(0) */
                    int w = T + 1 - t;                           /* sites still needed at time t + 1: 1 .. w - 1 */
                    for (int i = 1; i < w; i++) {
                        V cur = rr[i];
                        rr[i] = prev ^ (cur | rr[i + 1]);
                        prev = cur;
                    }
                }
                for (int t = 0; t <= T; t++) aq[t] = c1[t];      /* a_{-1} */
                for (int t = 0; t <= T; t++) ap[t] = ((t + ph) & 1) ? one : zero;   /* a_0 */
                row[0] = ap[0];
                for (int k = 1; k <= T; k++) {                   /* a_k(t) = a_{k-1}(t+1) ^ (a_{k-1}(t) | a_{k-2}(t)) */
                    for (int t = 0; t <= T - k; t++) an[t] = ap[t + 1] ^ (ap[t] | aq[t]);
                    row[k] = an[0];
                    V *tmp = aq; aq = ap; ap = an; an = tmp;
                }
                for (int d = DMIN; d <= DMAX; d++) {
                    V M = one;
                    int L = 0;
                    while (d + L <= T) {
                        V M2 = M & ~row[d + L];
                        if (vzero(M2)) break;
                        M = M2; L++;
                    }
                    Wit *w = &mine[d - DMIN];
                    if (L > w->L) {
                        int sidx = vfirst(M), Tw = d + L - 1;
                        free(w->left); free(w->right);
                        w->L = L; w->left = malloc(Tw + 2); w->right = malloc(Tw + 1);
                        for (int k = Tw; k >= 0; k--) w->left[Tw - k] = '0' + vbit(row[k], sidx);
                        w->left[Tw + 1] = 0;
                        for (int i = 1; i <= Tw; i++) w->right[i - 1] = '0' + vbit(r0[i], sidx);
                        w->right[Tw] = 0;
                    }
                }
            }
#pragma omp critical
            {
                for (int i = 0; i < ND; i++)
                    if (mine[i].L > best[i].L) {
                        free(best[i].left); free(best[i].right);
                        best[i] = mine[i];
                    } else { free(mine[i].left); free(mine[i].right); }
            }
            free(mine); free(rr); free(r0); free(c1); free(ap); free(aq); free(an); free(row);
        }
        done += nb;
        printf("C %lld\n", done * NS);
        for (int i = 0; i < ND; i++) printf("R %d %d\n", DMIN + i, best[i].L);
        fflush(stdout);
    }
    FILE *f = fopen(argv[7], "w");
    if (!f) { perror(argv[7]); return 1; }
    for (int i = 0; i < ND; i++)
        if (best[i].L) fprintf(f, "W %d %d %d %s %s\n", DMIN + i, best[i].L, ph, best[i].left, best[i].right);
    fclose(f);
    return 0;
}
