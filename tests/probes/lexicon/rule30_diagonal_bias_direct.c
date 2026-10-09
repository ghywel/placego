/* rule30_diagonal_bias_direct.c: an independent replay of rule30_diagonal_bias.c's counts (DB's instrument check, added
 * after the run; chat L417). No left-permutivity reduction and no triangle: every row x_0(0 .. 2k) of 2k + 1 cells is
 * held as one machine word and stepped k times by the plain Rule 30 formula new = (w << 1) ^ (w | (w >> 1)) (bit i is
 * cell i; zeros enter at both ends but cannot reach cell k by time k). It counts the rows with x_k(k) != x_0(0); then
 * rho_k = 1 - 2 M / 2^(2k + 1), and M = 2 N_k if the reduction holds.
 *
 * usage: rule30_diagonal_bias_direct K THREADS      prints "K M"
 */
#include <pthread.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static int K;

typedef struct { uint64_t lo, hi, count; } job;

static void *work(void *arg) {
    job *J = arg;
    uint64_t cnt = 0;
    const uint64_t mask = (2ULL << (2 * K)) - 1;
    for (uint64_t w0 = J->lo; w0 < J->hi; w0++) {
        uint64_t w = w0;
        for (int s = 0; s < K; s++)
            w = ((w << 1) ^ (w | (w >> 1))) & mask;
        cnt += ((w >> K) ^ w0) & 1;
    }
    J->count = cnt;
    return NULL;
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s K THREADS\n", argv[0]); return 2; }
    K = atoi(argv[1]);
    int T = atoi(argv[2]);
    if (K < 1 || 2 * K + 1 > 62) { fprintf(stderr, "K must be 1 .. 30\n"); return 2; }
    uint64_t total = 2ULL << (2 * K);
    pthread_t th[256];
    job jobs[256];
    for (int i = 0; i < T; i++) {
        jobs[i].lo = total * i / T;
        jobs[i].hi = total * (i + 1) / T;
        pthread_create(&th[i], NULL, work, &jobs[i]);
    }
    uint64_t M = 0;
    for (int i = 0; i < T; i++) {
        pthread_join(th[i], NULL);
        M += jobs[i].count;
    }
    printf("%d %llu\n", K, (unsigned long long)M);
    return 0;
}
