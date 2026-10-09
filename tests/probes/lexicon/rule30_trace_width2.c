/* rule30_trace_width2.c: TWX, exact counts of Rule 30's width-2 trace words (columns 0 and 1, physical frame) by
 * enumerating every light cone, for n beyond rule30_trace_widths.py's n = 14. Cloud's CL086 (RULE30-PRIZE.md §8.77)
 * shows that the width-2 trace's entropy is Rule 30's topological entropy, so each count gives the upper bound
 * h_top <= log2(N(n)) / n. Driven by rule30_trace_width2.py, which carries the predictions.
 *
 * A cone row x_0(-(n-1) .. n) is one word, bit k being cell k - (n-1); the plain step w' = (w << 1) ^ (w | (w >> 1))
 * is exact inside the cone, and columns 0 and 1 at time t are bits n-1 and n. Each trace word (2n bits) marks one bit
 * of a bitmap (atomic OR), and the marked bits are counted.
 *
 * usage: rule30_trace_width2 N THREADS      prints "N count"
 */
#include <pthread.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static int N;
static uint64_t *MAP;

typedef struct { uint64_t lo, hi; } job;

static void *work(void *arg) {
    job *J = arg;
    const uint64_t mask = (1ULL << (2 * N)) - 1;
    for (uint64_t w0 = J->lo; w0 < J->hi; w0++) {
        uint64_t w = w0, code = 0;
        for (int t = 0; t < N; t++) {
            code = (code << 2) | (((w >> (N - 1)) & 1) << 1) | ((w >> N) & 1);
            w = ((w << 1) ^ (w | (w >> 1))) & mask;
        }
        __atomic_fetch_or(&MAP[code >> 6], 1ULL << (code & 63), __ATOMIC_RELAXED);
    }
    return NULL;
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s N THREADS\n", argv[0]); return 2; }
    N = atoi(argv[1]);
    int T = atoi(argv[2]);
    if (N < 4 || N > 17) { fprintf(stderr, "N must be 4 .. 17 (the bitmap is 4^N bits)\n"); return 2; }
    uint64_t words = (1ULL << (2 * N)) / 64;
    MAP = calloc(words, 8);
    if (!MAP) { fprintf(stderr, "out of memory\n"); return 1; }
    uint64_t total = 1ULL << (2 * N);
    pthread_t th[64];
    job jobs[64];
    if (T > 64) T = 64;
    for (int i = 0; i < T; i++) {
        jobs[i].lo = total * i / T;
        jobs[i].hi = total * (i + 1) / T;
        pthread_create(&th[i], NULL, work, &jobs[i]);
    }
    for (int i = 0; i < T; i++) pthread_join(th[i], NULL);
    uint64_t count = 0;
    for (uint64_t i = 0; i < words; i++) count += (uint64_t)__builtin_popcountll(MAP[i]);
    printf("%d %llu\n", N, (unsigned long long)count);
    return 0;
}
