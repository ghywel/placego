// records_word.c: the exact record zero run R_w(d) of the forced left half for ANY periodic column 0 (a word w),
// over every column 1. Local, 2026-10-06; RULE30-PRIZE.md section 8.60; driver rule30_records_word.py.
//
// The wall form (section 8.39): column 0 is x(0, t) = w(t mod p); column 1 is x(1, t) = s(t), free where w(t) = 0
// and invisible where w(t) = 1 (Lemma 1 of section 8.2). The left half is forced, x(-m, t) = x(-m+1, t+1) XOR
// (x(-m+1, t) OR x(-m+2, t)), and L(k) = x(-k, 0) is the row at time 0. R_w(d) is the longest run of zeros
// L(d), L(d+1), ... over every choice of the free bits.
//
// Anti-diagonals. A_k[m] = x(-m, k-m), m = 0..k. A_k[0] = w(k) and for m >= 1
//     A_k[m] = A_k[m-1] XOR (A_{k-1}[m-1] OR C),  C = A_{k-2}[m-2] for m >= 2, C = s(k-1) for m = 1.
// As bit masks: b = (a_{k-1} << 1) | (a_{k-2} << 2) | (s(k-1) << 1); a_k = prefixXOR(b) XOR (w(k) ? ones : 0).
// L(k) is bit k of a_k. It is linear in s(k-1) when w(k-1) = 0 (Lemma 4): both choices give a_k's that differ in
// every bit but bit 0. So below depth d the search branches at every free bit; from depth d on each free bit is
// forced (the one choice that keeps L(k) = 0), and a run ends at the first forced cell (w(k-1) = 1) with L(k) = 1.
//
// Usage: records_word WORD D [THREADS] [SPLIT]   (SPLIT = number of leading free bits spread over the threads)
// Prints:  R w D = R (COUNT of LEAVES prefixes reach it); cap CAP   and CAPPED if any walk reaches the cap.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#ifdef _OPENMP
#include <omp.h>
#endif

#define NW 4
#define CAP (64 * NW - 3)
typedef struct { uint64_t w[NW]; } bits;

static char WORD[64];
static int P, D;

static inline int wbit(int t) { return WORD[t % P] - '0'; }

static inline bits shl(bits a, int s) {            // s = 1 or 2
    bits r;
    for (int i = NW - 1; i > 0; i--) r.w[i] = (a.w[i] << s) | (a.w[i - 1] >> (64 - s));
    r.w[0] = a.w[0] << s;
    return r;
}

static inline bits step(bits a1, bits a2, int s, int wk) {
    bits b = shl(a1, 1), c = shl(a2, 2), r;
    uint64_t carry = 0;
    for (int i = 0; i < NW; i++) b.w[i] |= c.w[i];
    b.w[0] |= (uint64_t)s << 1;
    for (int i = 0; i < NW; i++) {
        uint64_t x = b.w[i];
        x ^= x << 1; x ^= x << 2; x ^= x << 4; x ^= x << 8; x ^= x << 16; x ^= x << 32;
        x ^= carry;                                   // carry is 0 or all ones
        carry = (uint64_t)0 - (x >> 63);
        r.w[i] = wk ? ~x : x;
    }
    return r;
}

static inline int getbit(bits a, int k) { return (a.w[k >> 6] >> (k & 63)) & 1; }

// the forced walk from level k (>= D) with the run so far zero: returns the run length reached, CAP if capped
static int walk(int k, bits a1, bits a2) {
    while (k - D < CAP) {
        int free = wbit(k - 1) == 0;
        bits a = step(a1, a2, 0, wbit(k));
        if (getbit(a, k)) {
            if (!free) return k - D;
            a = step(a1, a2, 1, wbit(k));            // the other choice flips every bit but bit 0
            if (getbit(a, k)) return k - D;           // cannot happen (linear), kept as a guard
        }
        a2 = a1; a1 = a; k++;
    }
    return CAP;
}

typedef struct { int best; long long count, leaves; int capped; long long hist[CAP + 2]; } acc;

static void dfs(int k, bits a1, bits a2, acc *s) {
    if (k == D) {
        int r = walk(k, a1, a2);
        s->leaves++;
        s->hist[r]++;
        if (r >= CAP) s->capped = 1;
        if (r > s->best) { s->best = r; s->count = 1; } else if (r == s->best) s->count++;
        return;
    }
    int free = wbit(k - 1) == 0;
    for (int c = 0; c <= free; c++) {
        bits a = step(a1, a2, c, wbit(k));
        dfs(k + 1, a, a1, s);
    }
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: records_word WORD D [THREADS] [SPLIT]\n"); return 2; }
    strncpy(WORD, argv[1], 63); P = (int)strlen(WORD); D = atoi(argv[2]);
    int threads = argc > 3 ? atoi(argv[3]) : 1, split = argc > 4 ? atoi(argv[4]) : 10;
    if (D < 1 || D > CAP - 1) { fprintf(stderr, "D out of range\n"); return 2; }
#ifdef _OPENMP
    omp_set_num_threads(threads);
#endif
    // enumerate the first `split` free bits (or all free bits below D if fewer) as tasks
    int freepos[CAP], nfree = 0;
    for (int t = 0; t <= D - 2; t++) if (wbit(t) == 0) freepos[nfree++] = t;
    if (split > nfree) split = nfree;
    long long ntask = 1LL << split;
    acc total; memset(&total, 0, sizeof total); total.best = -1;
#pragma omp parallel
    {
        acc s; memset(&s, 0, sizeof s); s.best = -1;
#pragma omp for schedule(dynamic, 1)
        for (long long task = 0; task < ntask; task++) {
            // replay levels 1..k0 with the task's free bits, then dfs from there
            bits a1, a2; memset(&a1, 0, sizeof a1); memset(&a2, 0, sizeof a2);
            a1.w[0] = wbit(0);                         // a_0: A_0[0] = w(0)
            int used = 0, k = 1;
            for (; k <= D - 1 && used < split; k++) {
                int free = wbit(k - 1) == 0, c = 0;
                if (free) c = (task >> used) & 1, used++;
                bits a = step(a1, a2, c, wbit(k));
                a2 = a1; a1 = a;
            }
            dfs(k, a1, a2, &s);
        }
#pragma omp critical
        {
            total.leaves += s.leaves; total.capped |= s.capped;
            for (int i = 0; i <= CAP; i++) total.hist[i] += s.hist[i];
            if (s.best > total.best) { total.best = s.best; total.count = s.count; }
            else if (s.best == total.best) total.count += s.count;
        }
    }
    printf("R %s %d = %d (%lld of %lld prefixes reach it); cap %d%s\n", WORD, D, total.best, total.count,
           total.leaves, CAP, total.capped ? " CAPPED" : "");
    printf("H %s %d :", WORD, D);
    for (int i = 0; i <= total.best && i <= CAP; i++) if (total.hist[i]) printf(" %d:%lld", i, total.hist[i]);
    printf("\n");
    return 0;
}
