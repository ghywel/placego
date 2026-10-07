/* records_bits_ckpt.c: records_bits.c made resumable (Local, 2026-10-07, under draw-and-work: row Q6 drawn, its next
 * step a multi-day run, and "if the program cannot resume from a checkpoint, making it resumable is the job").
 * Same search, same definitions and the same R, H and W outputs as records_bits.c (and records.c); the only change is
 * the bookkeeping. records_bits.c splits the prefixes into 2^SPLIT independent tasks; here each task gets its own
 * accumulator, and when it finishes its result is appended as one line to a checkpoint file and flushed. On start,
 * tasks already in the file are skipped; an optional deadline stops new tasks cleanly. The final R, H, W lines are
 * merged from the file in task order, and printed only when every task is in it ("COMPLETE"); otherwise "PARTIAL".
 *
 * BUILD (macOS, Homebrew libomp):
 *   cc -O3 -mcpu=apple-m1 -Xpreprocessor -fopenmp -I/opt/homebrew/opt/libomp/include -L/opt/homebrew/opt/libomp/lib \
 *      -lomp -o records_bits_ckpt tests/probes/lexicon/records_bits_ckpt.c        (it includes records_fast.c)
 * USAGE:   ./records_bits_ckpt D THREADS SPLIT CHECKPOINT_FILE [DEADLINE_SECONDS]
 * Checkpoint line: T task best count_best nh (r c){nh} nw (end w0 w1 w2 w3){nw}, words in hex.
 * Validation: see the probe that drives it (rule30_records_ckpt.py).
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


#include <time.h>

static void write_task(FILE *f, long long task, const Acc *a) {
    int nh = 0;
    for (int r = 0; r <= KMAX + 1; r++) nh += a->hist[r] != 0;
    fprintf(f, "T %lld %d %lld %d", task, a->best, a->count_best, nh);
    for (int r = 0; r <= KMAX + 1; r++) if (a->hist[r]) fprintf(f, " %d %lld", r, a->hist[r]);
    fprintf(f, " %d", a->nwit);
    for (int i = 0; i < a->nwit; i++) {
        fprintf(f, " %d", a->witend[i]);
        for (int q = 0; q < NW; q++) fprintf(f, " %llx", (unsigned long long)a->wit[i].w[q]);
    }
    fprintf(f, "\n");
}

/* parse one checkpoint line fully; returns 1 and fills *task and *a only for a complete, well-formed line */
static int parse_line(const char *line, long long ntask, long long *task, Acc *a) {
    long long t, cb; int best, nh, nw, n, pos = 0;
    memset(a, 0, sizeof *a);
    if (sscanf(line, "T %lld %d %lld %d%n", &t, &best, &cb, &nh, &n) != 4) return 0;
    if (t < 0 || t >= ntask || nh < 0 || nh > KMAX + 2) return 0;
    a->best = best; a->count_best = cb; pos = n;
    for (int i = 0; i < nh; i++) {
        int r; long long c;
        if (sscanf(line + pos, " %d %lld%n", &r, &c, &n) != 2 || r < 0 || r > KMAX + 1) return 0;
        a->hist[r] = c; pos += n;
    }
    if (sscanf(line + pos, " %d%n", &nw, &n) != 1 || nw < 0 || nw > 64) return 0;
    pos += n; a->nwit = nw;
    for (int i = 0; i < nw; i++) {
        if (sscanf(line + pos, " %d%n", &a->witend[i], &n) != 1) return 0;
        pos += n;
        for (int q = 0; q < NW; q++) {
            unsigned long long x;
            if (sscanf(line + pos, " %llx%n", &x, &n) != 1) return 0;
            a->wit[i].w[q] = x; pos += n;
        }
    }
    while (line[pos] == ' ') pos++;
    if (line[pos] != '\n' && line[pos] != '\0') return 0;      /* trailing garbage: a torn or merged line */
    *task = t;
    return 1;
}

int main(int argc, char **argv) {
    if (argc < 5) {
        fprintf(stderr, "usage: records_bits_ckpt D THREADS SPLIT CHECKPOINT [DEADLINE_SECONDS]\n");
        return 2;
    }
    D = atoi(argv[1]);
    int threads = atoi(argv[2]);
    int split = atoi(argv[3]);
    const char *ck = argv[4];
    double deadline = argc > 5 ? atof(argv[5]) : 0;
    NFREE = (D >= 2) ? (D - 2) / 2 + 1 : 0;
    if (NFREE < LB + 1) { fprintf(stderr, "too shallow for the bit-sliced search\n"); return 2; }
    if (D > KMAX - 8) { fprintf(stderr, "D out of range\n"); return 2; }
    if (split > NFREE - LB) split = NFREE - LB;
    KLANE = 2 * (NFREE - LB) + 1;
    for (int b = 0; b < LB; b++) {
        W m = 0;
        for (int l = 0; l < 64; l++) if ((l >> b) & 1) m |= 1ULL << l;
        LANEMASK[b] = m;
    }
#ifdef _OPENMP
    if (threads > 0) omp_set_num_threads(threads);
#endif
    long long ntask = 1LL << split;
    char *done = calloc((size_t)ntask, 1);
    /* pass 1: which tasks are already in the checkpoint */
    FILE *in = fopen(ck, "r");
    long long ndone = 0;
    if (in) {
        char *line = NULL; size_t cap = 0;
        while (getline(&line, &cap, in) > 0) {
            long long t; Acc tmp;
            if (parse_line(line, ntask, &t, &tmp) && !done[t]) { done[t] = 1; ndone++; }
        }
        free(line); fclose(in);
    }
    FILE *out = fopen(ck, "a+");
    if (!out) { fprintf(stderr, "cannot open checkpoint %s\n", ck); return 2; }
    if (fseek(out, -1, SEEK_END) == 0 && fgetc(out) != '\n') { fseek(out, 0, SEEK_END); fputc('\n', out); }
    fseek(out, 0, SEEK_END);
    fprintf(stderr, "records_bits_ckpt D %d split %d: %lld of %lld tasks already done\n", D, split, ndone, ntask);
    time_t t0 = time(0);
    int kstart = (split == 0) ? 1 : 2 * (split - 1) + 2;
    #pragma omp parallel
    {
        #pragma omp for schedule(dynamic, 1)
        for (long long task = 0; task < ntask; task++) {
            if (done[task]) continue;
            if (deadline > 0 && difftime(time(0), t0) > deadline) continue;
            Acc acc; memset(&acc, 0, sizeof acc);
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
            #pragma omp critical
            {
                write_task(out, task, &acc);
                fflush(out);
            }
        }
    }
    fclose(out);
    /* pass 2: merge every task line in task order */
    Acc total; memset(&total, 0, sizeof total);
    char *have = calloc((size_t)ntask, 1);
    in = fopen(ck, "r");
    long long nhave = 0;
    {
        char *line = NULL; size_t cap = 0;
        /* collect per-task results; a task can appear twice only if a run was killed mid-write: keep the first */
        Acc **slot = calloc((size_t)ntask, sizeof(Acc *));
        while (getline(&line, &cap, in) > 0) {
            long long t;
            Acc *a = calloc(1, sizeof(Acc));
            if (!parse_line(line, ntask, &t, a) || slot[t]) { free(a); continue; }   /* torn line or duplicate */
            slot[t] = a; have[t] = 1; nhave++;
        }
        free(line); fclose(in);
        for (long long t = 0; t < ntask; t++) {
            Acc *a = slot[t];
            if (!a) continue;
            for (int r = 0; r <= KMAX + 1; r++) total.hist[r] += a->hist[r];
            if (a->best > total.best) { total.best = a->best; total.count_best = 0; total.nwit = 0; }
            if (a->best == total.best) {
                total.count_best += a->count_best;
                for (int i = 0; i < a->nwit && total.nwit < 64; i++) {
                    total.wit[total.nwit] = a->wit[i]; total.witend[total.nwit] = a->witend[i]; total.nwit++;
                }
            }
            free(a);
        }
        free(slot);
    }
    if (nhave < ntask) {
        printf("PARTIAL D %d: %lld of %lld tasks in the checkpoint; best so far %d\n", D, nhave, ntask, total.best);
        return 4;
    }
    printf("R %d %d %lld\n", D, total.best, total.count_best);
    for (int r = 0; r <= KMAX + 1; r++) if (total.hist[r]) printf("H %d %d %lld\n", D, r, total.hist[r]);
    for (int i = 0; i < total.nwit; i++) {
        printf("W %d ", D);
        for (int t = 0; t < total.witend[i]; t += 2) putchar('0' + bit(&total.wit[i], t));
        putchar('\n');
    }
    printf("COMPLETE D %d: %lld tasks\n", D, ntask);
    return 0;
}
