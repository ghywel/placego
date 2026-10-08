/* rule30_cloud_equivalent_seeds.c: decrypt the single seed's centre column under every right half of width W.
 *
 * BUILD:   cc -O2 -o eqseeds tests/probes/lexicon/rule30_cloud_equivalent_seeds.c
 * USAGE:   ./eqseeds T W      (T = 400, W = 16: about ten seconds)
 * The owner's reframing (2026-10-09): "if the centre column was an encrypted message, not just random but encoding
 * information, how might we decrypt it." Rule 30 is left-permutive, so the centre column is an autokey cipher of the
 * initial row: x_t(0) = x_0(-t) XOR F_t(x_0(-t+1 .. t)). Given the column (ciphertext) and the right half x_0(1 ..)
 * (key), the left half (plaintext) is recovered one cell per step. On diagonals e = j - s,
 * diag[e][s] = diag[e][s-1] ^ (diag[e+1][s-1] | diag[e+2][s-1]); x_0(-d) starts diagonal -d and is the unique value
 * making x_d(0) = diag[-d][d] equal the column bit c_d. Prints the keys whose plaintext has no black deeper than T/2.
 * EXPLORATORY, not pre-registered: written by Cloud on 2026-10-09 (00:40 BST) while checking the cipher reading,
 * after a smaller check had already shown the seed 11 matching for 30 steps. No prediction was written first.
 * RESULT (T = 400): of 4,096 keys of width 12, exactly 13 decrypt to a finite plaintext, and of 65,536 keys of width
 * 16 exactly 17. All have an empty left half, and they are exactly the seeds 1, 11, 101, 1011, 10101, .., that is
 * 1(01)^n and 1(01)^n 1. Every other key's plaintext has a black deeper than 200 (so no finite configuration with
 * such a right half and a left half of depth at most 200 has this column). That the family gives the single seed's
 * pattern at every cell x <= t - 1, for ever, is proved by hand in PROOFS.md (Cloud, 2026-10-09).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int T, W;
static unsigned char *D;                     /* diag index e + T, times 0 .. T-1 */
#define DG(e, s) D[(long)((e) + T) * T + (s)]
static void fill(int e) { for (int s = 1; s < T; s++) DG(e, s) = DG(e, s - 1) ^ (DG(e + 1, s - 1) | DG(e + 2, s - 1)); }
/* returns the deepest black of the decrypted left half; c == NULL: encrypt the plaintext "all white" instead */
static int run(long key, const unsigned char *c, unsigned char *col) {
    memset(D, 0, (long)(T + W + 3) * T);
    for (int e = W; e >= 1; e--) { DG(e, 0) = (key >> (e - 1)) & 1; fill(e); }
    DG(0, 0) = 1; fill(0);
    if (col) col[0] = 1;
    int deep = 0;
    for (int d = 1; d < T; d++) {
        DG(-d, 0) = 0; fill(-d);
        int v = c ? (DG(-d, d) ^ c[d]) : 0;
        if (v) { for (int s = 0; s < T; s++) DG(-d, s) ^= 1; deep = d; }
        if (col) col[d] = DG(-d, d);
    }
    return deep;
}
int main(int argc, char **argv) {
    T = atoi(argv[1]); W = atoi(argv[2]);
    D = calloc((long)(2 * T + W + 4) * T, 1);
    unsigned char *c = malloc(T);
    run(0, NULL, c);                         /* the single seed's column */
    printf("seed column: "); for (int t = 0; t < 32; t++) putchar('0' + c[t]); printf("...\n");
    long nfin = 0;
    for (long key = 0; key < (1L << W); key++) {
        int deep = run(key, c, NULL);
        if (deep <= T / 2) {
            nfin++;
            printf("key cells 1..%d = ", W); for (int e = 1; e <= W; e++) putchar('0' + ((key >> (e - 1)) & 1));
            printf("  decrypted left half: deepest black at depth %d\n", deep);
        }
    }
    printf("%ld of %ld keys decrypt to a left half with no black deeper than %d\n", nfin, 1L << W, T / 2);
    return 0;
}
