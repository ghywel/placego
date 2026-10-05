/* forced_deep.c: forced.c to depth 250, with multi-word bit arrays (rule30_debt.py, mode depth).
 * Usage: forced_deep BMIN BMAX D WORD P. Same output as forced.c: H b j L count. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define NW 5
#define DM 250
typedef struct { uint64_t w[NW]; } bv;
static long long H[32][DM + 1][DM + 1];
static inline bv shl1(bv a) { bv r; uint64_t c = 0; for (int i = 0; i < NW; i++) { r.w[i] = (a.w[i] << 1) | c; c = a.w[i] >> 63; } return r; }
static inline bv shr1(bv a) { bv r; uint64_t c = 0; for (int i = NW - 1; i >= 0; i--) { r.w[i] = (a.w[i] >> 1) | c; c = a.w[i] << 63; } return r; }
static inline bv bxor(bv a, bv b) { for (int i = 0; i < NW; i++) a.w[i] ^= b.w[i]; return a; }
static inline bv bor(bv a, bv b) { for (int i = 0; i < NW; i++) a.w[i] |= b.w[i]; return a; }
static inline int getb(const bv *a, int k) { return (a->w[k >> 6] >> (k & 63)) & 1; }
static inline void setb(bv *a, int k, int v) { if (v) a->w[k >> 6] |= 1ULL << (k & 63); else a->w[k >> 6] &= ~(1ULL << (k & 63)); }
int main(int argc, char **argv) {
    int bmin = atoi(argv[1]), bmax = atoi(argv[2]), D = atoi(argv[3]);
    const char *word = argv[4];
    int per = atoi(argv[5]);
    if (D > DM || bmax + D + 3 > 64 * NW) { fprintf(stderr, "too large\n"); return 1; }
    memset(H, 0, sizeof H);
    for (int b = bmin; b <= bmax; b++) {
        unsigned long long nr = b == 0 ? 1ULL : 1ULL << (b - 1);
        for (int ph = 0; ph < per; ph++) {
            int e0 = word[ph] == '1';
            if (b == 0 && !e0) continue;
            bv c0; memset(&c0, 0, sizeof c0);
            for (int t = 0; t <= D + 1; t++) setb(&c0, t, word[ph + t] == '1');
            for (unsigned long long q = 0; q < nr; q++) {
                bv x; memset(&x, 0, sizeof x);
                if (b >= 1) { unsigned long long r = q | (1ULL << (b - 1)); for (int i = 0; i < b; i++) setb(&x, i + 1, (r >> i) & 1); }
                setb(&x, 0, e0);
                bv c1; memset(&c1, 0, sizeof c1);
                for (int t = 0; t <= D; t++) {
                    setb(&c1, t, getb(&x, 1));
                    x = bxor(shl1(x), bor(x, shr1(x)));
                    setb(&x, 0, getb(&c0, t + 1));
                }
                unsigned char F[DM + 1];
                F[0] = e0;
                bv right = c1, cur = c0;
                for (int k = 1; k <= D; k++) {
                    bv nxt = bxor(shr1(cur), bor(cur, right));
                    F[k] = nxt.w[0] & 1;
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
