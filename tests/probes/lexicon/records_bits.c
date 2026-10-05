/* records_bits.c: records.c's search with 64 prefixes at once, bit-sliced (Local, 2026-10-05; the owner's Enigma lead:
 * the Bombe tested every hypothesis for a letter at once, electrically. Here a machine word's 64 bits are 64 prefixes).
 * The same definition and the same outputs as records.c ("R", "H", up to 64 "W" lines).
 *
 * BUILD (macOS, Homebrew libomp):
 *   cc -O3 -mcpu=apple-m1 -Xpreprocessor -fopenmp -I/opt/homebrew/opt/libomp/include -L/opt/homebrew/opt/libomp/lib \
 *      -lomp -o records_bits tests/probes/lexicon/records_bits.c          (it includes records_fast.c)
 * USAGE:   ./records_bits D [THREADS] [SPLIT]
 *
 * Why it can be done. Inside a zero run every free bit is forced: at a free step (k - 1 even) bit 0 of A_{k-1} is
 * tau(k-1) = 0, so c(k-1) is bit 1 of X exactly, and the running XOR spreads it over bits 1 .. k of A_k (Lemma 4). The
 * two children's cells at depth k are therefore complements, and exactly one continues. A prefix's run is one forced
 * walk, not a search, so 64 prefixes can walk in lockstep: at a free step the lanes whose cell came out 1 take c = 1
 * (their bits 1 .. k flip), and at the next step a lane whose cell is 1 stops, its run measured.
 * The layout. The scalar prefix tree of records_fast.c runs down to the last LB = 6 free bits of the prefix; there the
 * two diagonals are broadcast to bit-sliced form (word j holds bit j of the diagonal for all 64 lanes), lane l takes
 * bits l as those last six free bits, and the twelve remaining prefix steps and the walk run on words. A lane that
 * reaches its thread's running record has its witness found by records_fast.c's scalar dfs_zero, so the witnesses
 * are the same ones.
 * VALIDATION (Local, 2026-10-05, the M5). Against records.c at every depth 1 .. 57: the R line and every H line
 *   identical, and the W lines the same set wherever the record has at most 64 prefixes. At depths 69 and 73 against
 *   M4's own records.c output: R and all 28 and 30 H lines identical. Built in: every lane that reaches its thread's
 *   running record is replayed by the scalar search, and a disagreement stops the program (exit 3); it never has.
 *   Speed: about 12x records.c (depth 53, 2 threads, interleaved: 0.45 s against 5.55 s, with M4 loading the machine).
 */
#define main records_fast_main
#include "records_fast.c"
#undef main

#define LB 6
typedef uint64_t W;
static W LANEMASK[LB];
static int KLANE, NFREE;

/* the scalar diagonals of one lane, replayed from the lane level to D, then the witness as records_fast.c finds it */
static void lane_witness(int k, V P, V Q, V col1, int lane, Acc *acc, int r) {
    int b = 0;
    for (; k < D; k++) {
        int c = 0;
        if ((k - 1) % 2 == 0) {
            c = (lane >> b) & 1; b++;
            if (c) col1.w[(k - 1) >> 6] |= 1ULL << ((k - 1) & 63);
        }
        V A = next_diag(&P, &Q, c, k);
        Q = P; P = A;
    }
    V bc; int be;
    int rr = dfs_zero(k, &P, &Q, col1, &bc, &be);
    if (rr != r) { fprintf(stderr, "records_bits: lane run %d, scalar %d at D %d\n", r, rr, D); exit(3); }
    acc->hist[r]--;
    record(acc, r, bc, be);
}

static void lanes(int k0, const V *P0, const V *Q0, V col1, Acc *acc) {
    W buf[3][KMAX + 2];
    W *bq = buf[0], *bp = buf[1], *ba = buf[2];
    for (int j = 0; j <= KMAX; j++) { bp[j] = 0; bq[j] = 0; }
    for (int j = 0; j < k0; j++) bp[j] = bit(P0, j) ? ~0ULL : 0;          /* A_{k0-1}: bits 0 .. k0-1 */
    for (int j = 0; j + 1 < k0; j++) bq[j] = bit(Q0, j) ? ~0ULL : 0;      /* A_{k0-2}: bits 0 .. k0-2 */
    W alive = ~0ULL;
    int lb = 0;
    for (int k = k0; ; k++) {
        int free_bit = ((k - 1) % 2 == 0);
        W cm = 0;
        if (k < D && free_bit) cm = LANEMASK[lb++];
        ba[0] = (k & 1) ? ~0ULL : 0;
        ba[1] = ba[0] ^ (bp[0] | cm);
        for (int j = 2; j <= k; j++) ba[j] = ba[j - 1] ^ (bp[j - 1] | bq[j - 2]);
        if (k >= D) {
            W cell = ba[k];
            if (free_bit) {                                  /* the forced choice: lanes whose cell is 1 take c = 1 */
                for (int j = 1; j <= k; j++) ba[j] ^= cell;
            } else {
                W dead = alive & cell;
                while (dead) {
                    int l = __builtin_ctzll(dead); dead &= dead - 1;
                    int r = k - D;
                    acc->hist[r]++;
                    if (r >= acc->best) lane_witness(k0, *P0, *Q0, col1, l, acc, r);
                }
                alive &= ~cell;
                if (!alive) return;
            }
            if (k == KMAX) {                                 /* as records.c: a run past KMAX counts to KMAX + 1 */
                W a = alive;
                while (a) {
                    int l = __builtin_ctzll(a); a &= a - 1;
                    int r = KMAX + 1 - D;
                    acc->hist[r]++;
                    if (r >= acc->best) lane_witness(k0, *P0, *Q0, col1, l, acc, r);
                }
                return;
            }
        }
        W *t = bq; bq = bp; bp = ba; ba = t;
    }
}

static void prefix_to_lanes(int k, const V *P, const V *Q, V col1, Acc *acc) {
    if (k == KLANE) { lanes(k, P, Q, col1, acc); return; }
    int free_bit = ((k - 1) % 2 == 0);
    for (int c = 0; c <= free_bit; c++) {
        V col = col1;
        if (c) col.w[(k - 1) >> 6] |= 1ULL << ((k - 1) & 63);
        V A = next_diag(P, Q, c, k);
        prefix_to_lanes(k + 1, &A, P, col, acc);
    }
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: records_bits D [THREADS] [SPLIT]\n"); return 2; }
    D = atoi(argv[1]);
    int threads = argc > 2 ? atoi(argv[2]) : 1;
    int split = argc > 3 ? atoi(argv[3]) : 12;
    NFREE = (D >= 2) ? (D - 2) / 2 + 1 : 0;
    if (NFREE < LB + 1) return records_fast_main(argc, argv);   /* too shallow for lanes: the scalar search */
    if (D > KMAX - 8) { fprintf(stderr, "D out of range\n"); return 2; }
    if (split > NFREE - LB) split = NFREE - LB;
    KLANE = 2 * (NFREE - LB) + 1;                            /* free bit i (time 2i) is used at step 2i + 1 */
    for (int b = 0; b < LB; b++) {
        W m = 0;
        for (int l = 0; l < 64; l++) if ((l >> b) & 1) m |= 1ULL << l;
        LANEMASK[b] = m;
    }
#ifdef _OPENMP
    if (threads > 0) omp_set_num_threads(threads);
#endif
    long long ntask = 1LL << split;
    Acc total; memset(&total, 0, sizeof total);
    int kstart = (split == 0) ? 1 : 2 * (split - 1) + 2;
    #pragma omp parallel
    {
        Acc acc; memset(&acc, 0, sizeof acc);
        #pragma omp for schedule(dynamic, 1)
        for (long long task = 0; task < ntask; task++) {
            V P, Q, col; memset(&P, 0, sizeof P); memset(&Q, 0, sizeof Q); memset(&col, 0, sizeof col);
            int k = 1;
            for (; k < kstart && k < D; k++) {
                int c = 0;
                if ((k - 1) % 2 == 0) {
                    int i = (k - 1) / 2;
                    c = (int)((task >> i) & 1);
                    if (c) col.w[(k - 1) >> 6] |= 1ULL << ((k - 1) & 63);
                }
                V A = next_diag(&P, &Q, c, k);
                Q = P; P = A;
            }
            prefix_to_lanes(k, &P, &Q, col, &acc);
        }
        #pragma omp critical
        {
            for (int r = 0; r <= KMAX + 1; r++) total.hist[r] += acc.hist[r];
            if (acc.best > total.best) { total.best = acc.best; total.count_best = 0; total.nwit = 0; }
            if (acc.best == total.best) {
                total.count_best += acc.count_best;
                for (int i = 0; i < acc.nwit && total.nwit < 64; i++) {
                    total.wit[total.nwit] = acc.wit[i]; total.witend[total.nwit] = acc.witend[i]; total.nwit++;
                }
            }
        }
    }
    printf("R %d %d %lld\n", D, total.best, total.count_best);
    for (int r = 0; r <= KMAX + 1; r++) if (total.hist[r]) printf("H %d %d %lld\n", D, r, total.hist[r]);
    for (int i = 0; i < total.nwit; i++) {
        printf("W %d ", D);
        for (int t = 0; t < total.witend[i]; t += 2) putchar('0' + bit(&total.wit[i], t));
        putchar('\n');
    }
    return 0;
}
