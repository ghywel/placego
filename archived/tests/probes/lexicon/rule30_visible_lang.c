/* rule30_visible_lang.c: the exact visible language of column 1 beside the 0101 wall, all words of length K.
 *
 * RLK's helper (rule30_relaxed_records_k.py). Mirrors rule30_cloud_visible_gaps.py's visible(right, K) bit for bit:
 * bit 0 of a row is the wall (white at even times), bit i is column i; one step is
 * new = (row << 1) ^ (row | (row >> 1)), then the wall is set to (t + 1) mod 2; the visible word is column 1 at times
 * 0, 2, .., 2K - 2. A length-K word depends only on the initial sites 1 .. 2K - 1 (GC500), so every right word of
 * that length is enumerated (2^(2K - 1) of them), with the row masked to the light cone of column 1 at time 2K - 2.
 * Output: one line per visible word, as a 0/1 string (first symbol = time 0), sorted.
 * Build: cc -O3 -o rule30_visible_lang rule30_visible_lang.c -lpthread ; run: ./rule30_visible_lang K [THREADS]
 */
#include <pthread.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int K, NT;
static uint8_t *seen;                       /* 2^K flags, one per visible code */

static void *work(void *arg) {
    long id = (long)arg;
    uint64_t total = 1ULL << (2 * K - 1);
    uint8_t *loc = calloc(1ULL << K, 1);
    for (uint64_t r = id; r < total; r += NT) {
        uint64_t row = r << 1;              /* sites 1 .. 2K - 1; wall white at t = 0 */
        uint32_t code = 0;
        for (int t = 0; t <= 2 * K - 2; t++) {
            if ((t & 1) == 0) code = (code << 1) | ((row >> 1) & 1);
            if (t == 2 * K - 2) break;
            uint64_t nw = (row << 1) ^ (row | (row >> 1));
            nw = (nw & ~1ULL) | (uint64_t)((t + 1) & 1);
            int keep = 2 * K - 2 - t;       /* sites 0 .. keep at time t + 1 */
            row = nw & ((keep >= 63) ? ~0ULL : ((1ULL << (keep + 1)) - 1));
        }
        loc[code] = 1;
    }
    for (uint64_t c = 0; c < (1ULL << K); c++)
        if (loc[c]) seen[c] = 1;            /* benign race: only 0 -> 1 writes */
    free(loc);
    return NULL;
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: %s K [THREADS]\n", argv[0]); return 2; }
    K = atoi(argv[1]);
    NT = argc > 2 ? atoi(argv[2]) : 1;
    if (K < 1 || K > 31) { fprintf(stderr, "K out of range\n"); return 2; }
    seen = calloc(1ULL << K, 1);
    pthread_t th[64];
    for (long i = 0; i < NT; i++) pthread_create(&th[i], NULL, work, (void *)i);
    for (int i = 0; i < NT; i++) pthread_join(th[i], NULL);
    char buf[40];
    for (uint64_t c = 0; c < (1ULL << K); c++) {
        if (!seen[c]) continue;
        for (int k = 0; k < K; k++) buf[k] = ((c >> (K - 1 - k)) & 1) ? '1' : '0';
        buf[K] = 0;
        puts(buf);
    }
    return 0;
}
