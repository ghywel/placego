/* rule30_diagonal_bias.c: the exact count behind rho_k, the fair-row correlation of a cell and the cell k steps down the
 * rightward light-speed diagonal (CL078; rule30_diagonal_bias.py drives it, with its predictions).
 *
 * By left permutivity x_k(k) = x_0(0) xor g_k(x_0(1) .. x_0(2k)), with g_k = xor over s < k of (x_s(s+1) or x_s(s+2)),
 * and the cells right of the diagonal form a closed triangle: row s on cells s+1 .. 2k-s. So rho_k = 1 - 2 N / 4^k, where
 * N counts the inputs w in {0,1}^(2k) with g_k(w) = 1. Bit-sliced: inputs 1 .. 6 vary across the 64 lanes, the rest are
 * enumerated, split across threads.
 *
 * usage: rule30_diagonal_bias K THREADS      prints "K N" (N as an exact integer)
 */
#include <pthread.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static int K, NIN;
static uint64_t LANE[6];

typedef struct { uint64_t lo, hi, count; } job;

static void *work(void *arg) {
    job *J = arg;
    uint64_t row[80], nxt[80];
    uint64_t cnt = 0;
    for (uint64_t o = J->lo; o < J->hi; o++) {
        /* row 0: cells 1 .. 2k at index c */
        for (int c = 1; c <= NIN; c++)
            row[c] = c <= 6 ? LANE[c - 1] : (((o >> (c - 7)) & 1) ? ~0ULL : 0ULL);
        uint64_t g = 0;
        for (int s = 0; s < K; s++) {
            g ^= row[s + 1] | row[s + 2];
            if (s == K - 1) break;
            for (int c = s + 2; c <= NIN - s - 1; c++)
                nxt[c] = row[c - 1] ^ (row[c] | row[c + 1]);
            for (int c = s + 2; c <= NIN - s - 1; c++)
                row[c] = nxt[c];
        }
        cnt += (uint64_t)__builtin_popcountll(g);
    }
    J->count = cnt;
    return NULL;
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s K THREADS\n", argv[0]); return 2; }
    K = atoi(argv[1]);
    int T = atoi(argv[2]);
    NIN = 2 * K;
    if (K < 3 || NIN > 76) { fprintf(stderr, "K must be 3 .. 38\n"); return 2; }
    for (int b = 0; b < 6; b++) {
        uint64_t m = 0;
        for (int l = 0; l < 64; l++)
            if ((l >> b) & 1) m |= 1ULL << l;
        LANE[b] = m;
    }
    uint64_t outer = 1ULL << (NIN - 6);
    if ((uint64_t)T > outer) T = (int)outer;
    pthread_t th[256];
    job jobs[256];
    for (int i = 0; i < T; i++) {
        jobs[i].lo = outer * i / T;
        jobs[i].hi = outer * (i + 1) / T;
        pthread_create(&th[i], NULL, work, &jobs[i]);
    }
    uint64_t N = 0;
    for (int i = 0; i < T; i++) {
        pthread_join(th[i], NULL);
        N += jobs[i].count;
    }
    printf("%d %llu\n", K, (unsigned long long)N);
    return 0;
}
