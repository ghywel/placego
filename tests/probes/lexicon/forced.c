/* forced.c: zero runs of the forced left half, right part by right part (rule30_debt.py).
 * Usage: forced BMIN BMAX D WORD P
 * For each right part (cells 1 .. b, cell b black; b = 0 means column 0 is the hull's right end) and each phase of
 * WORD (period P), column 0 is clamped to the phase for times 0 .. D, the right half is run, and the forced left
 * half is computed sideways to depth D: x_t(-1) = x_{t+1}(0) XOR (x_t(0) OR x_t(1)), and so on leftwards, with each
 * column held as a bitmask over time. F_0 is column 0 at time 0 and F_{-k} the forced cell at depth k, time 0.
 * For every depth j with F_{-j} = 1 (j = 0 needs the phase to start black), L is the number of zeros that follow
 * (to the next one, or to depth D, censored). Output lines: H b j L count, summed over right parts and phases.
 * By RULE30-PRIZE.md section 8.52, N_{w,j}(T) for T >= j + 1 and w = j + 1 + b is the number with L >= T - 1 - j. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned __int128 u128;
#define DM 120
static long long H[32][DM + 1][DM + 1];
int main(int argc, char **argv) {
    int bmin = atoi(argv[1]), bmax = atoi(argv[2]), D = atoi(argv[3]);
    const char *word = argv[4];
    int per = atoi(argv[5]);
    if (D > DM || bmax + D + 2 > 127) { fprintf(stderr, "too large\n"); return 1; }
    memset(H, 0, sizeof H);
    for (int b = bmin; b <= bmax; b++) {
        unsigned long long nr = b == 0 ? 1ULL : 1ULL << (b - 1);
        for (int ph = 0; ph < per; ph++) {
            int e0 = word[ph] == '1';
            u128 c0 = 0;
            for (int t = 0; t <= D + 1; t++) if (word[ph + t] == '1') c0 |= (u128)1 << t;
            if (b == 0 && !e0) continue;
            for (unsigned long long q = 0; q < nr; q++) {
                u128 x = 0;                                  /* cells 0 .. 126 at bits 0 .. 126 */
                if (b >= 1) x = ((u128)(q | (1ULL << (b - 1)))) << 1;
                x |= (u128)e0;
                u128 c1 = 0;
                for (int t = 0; t <= D; t++) {
                    if ((x >> 1) & 1) c1 |= (u128)1 << t;
                    x = (x << 1) ^ (x | (x >> 1));
                    x = (x & ~(u128)1) | (u128)((c0 >> (t + 1)) & 1);
                }
                unsigned char F[DM + 1];
                F[0] = e0;
                u128 right = c1, cur = c0;                   /* columns 1 and 0 */
                for (int k = 1; k <= D; k++) {
                    u128 nxt = (cur >> 1) ^ (cur | right);    /* column -k */
                    F[k] = (unsigned char)(nxt & 1);
                    right = cur; cur = nxt;
                }
                for (int j = 0; j <= D; j++) {
                    if (!F[j]) continue;
                    int L = 0;
                    while (j + L + 1 <= D && !F[j + L + 1]) L++;
                    H[b][j][L]++;
                }
            }
        }
        for (int j = 0; j <= D; j++) for (int L = 0; L <= D; L++) if (H[b][j][L])
            printf("H %d %d %d %lld\n", b, j, L, H[b][j][L]);
        fflush(stdout);
    }
    return 0;
}
