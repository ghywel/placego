/* mahler_rung_search.c: the rung-g search of door 0 (L717; MAHLER.md section 2). For every start n in [0, 2^W) it
 * finds the rung-g horizon: the first number of T-code bits that contains two 1s closer than g apart. Here T(x) =
 * ceil(3x/2) and the code is b_j = T^j(n) mod 2. By G294, a positive n whose every two 1s stay >= g apart for ever is
 * the integer part of a Z-number with every fractional part below alpha_g. See mahler_rung_search.py for the
 * predictions and outcome.
 *
 * Method: a depth-first walk over the low bits of n, exactly as in mahler_census.c, without windows. The state at
 * depth T is v = T^T(n_low) mod 2^256, held as two 128-bit limbs. The true n_T is v + 3^T (n >> T), so the parity
 * is (v + bit_T(n)) mod 2. Only rung-g-admissible prefixes are walked, so the tree grows like lambda_g^T. v is exact
 * while 3^T 2^W < 2^256, which holds for T <= 100 at W <= 100, and the forced tail needs only low bits for parity
 * (GC1221's argument: each wrapped step keeps one bit fewer). A start still rung-pure at TMAX is printed for exact
 * replay.
 *
 * Usage: mahler_rung_search G W PREFIXBITS PREFIX
 * Output: "H h count" (count of starts with rung horizon exactly h, decimal), "S n" stragglers, "MAX h n". */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef unsigned __int128 u128;
typedef struct { u128 lo, hi; } u256;
static inline u256 add(u256 a, u256 b) { u256 r; r.lo = a.lo + b.lo; r.hi = a.hi + b.hi + (r.lo < a.lo); return r; }
static inline u256 shl1(u256 a) { u256 r; r.hi = (a.hi << 1) | (a.lo >> 127); r.lo = a.lo << 1; return r; }
static inline u256 shr1(u256 a) { u256 r; r.lo = (a.lo >> 1) | (a.hi << 127); r.hi = a.hi >> 1; return r; }
static inline u256 mul3(u256 a) { return add(a, shl1(a)); }
static inline u256 smallv(unsigned b) { u256 r; r.lo = b; r.hi = 0; return r; }

#define TMAX 250
#define HMAX 400
static int G, W;
static u256 pow3[TMAX + 2];
static u128 hist[HMAX];
static int maxh = 0;
static u128 argmax = 0;

static void u128str(u128 x, char *out) {            /* decimal */
    char buf[64]; int i = 63; buf[i] = 0;
    if (x == 0) { strcpy(out, "0"); return; }
    while (x) { buf[--i] = '0' + (int)(x % 10); x /= 10; }
    strcpy(out, buf + i);
}

static void record(int h, u128 n, u128 mult) {
    if (h >= HMAX) h = HMAX - 1;
    hist[h] += mult;
    if (h > maxh && mult == 1) { maxh = h; argmax = n; }
}

static void forced(u128 n, u256 v, int last1, int T) {
    if (n == 0) return;                              /* the zero start: code all 0, rung-pure for ever */
    while (T < TMAX) {
        int b = (int)(v.lo & 1);
        if (b) {
            if (T - last1 < G) { record(T + 1, n, 1); return; }
            last1 = T;
        }
        v = shr1(add(mul3(v), smallv(b)));
        T++;
    }
    char s[64]; u128str(n, s); printf("S %s\n", s);
}

static void dfs(int T, u128 n0low, u256 v, int last1) {
    if (T == W) { forced(n0low, v, last1, T); return; }
    for (int bit = 0; bit < 2; bit++) {
        int b = (int)((v.lo + (u128)bit) & 1);
        u128 nn = n0low | ((u128)bit << T);
        int l1 = last1;
        if (b) {
            if (T - last1 < G) { record(T + 1, nn, ((u128)1) << (W - T - 1)); continue; }
            l1 = T;
        }
        u256 x = bit ? add(v, pow3[T]) : v;
        u256 nv = shr1(add(mul3(x), smallv(b)));
        dfs(T + 1, nn, nv, l1);
    }
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: %s G W PREFIXBITS PREFIX\n", argv[0]); return 1; }
    G = atoi(argv[1]); W = atoi(argv[2]);
    int pb = atoi(argv[3]);
    unsigned long long prefix = strtoull(argv[4], 0, 10);
    if (W > 120 || pb > 30 || pb >= W) { fprintf(stderr, "W <= 120 and pb < W required\n"); return 1; }
    pow3[0] = smallv(1);
    for (int i = 1; i <= TMAX; i++) pow3[i] = mul3(pow3[i - 1]);
    u256 v = smallv(0); u128 n0low = 0; int last1 = -1000, T = 0;
    for (; T < pb; T++) {
        int bit = (int)((prefix >> T) & 1);
        int b = (int)((v.lo + (u128)bit) & 1);
        n0low |= (u128)bit << T;
        if (b) {
            if (T - last1 < G) { record(T + 1, n0low, ((u128)1) << (W - pb)); goto done; }
            last1 = T;
        }
        u256 x = bit ? add(v, pow3[T]) : v;
        v = shr1(add(mul3(x), smallv(b)));
    }
    dfs(T, n0low, v, last1);
done:;
    char s[64];
    for (int h = 0; h < HMAX; h++) if (hist[h]) { u128str(hist[h], s); printf("H %d %s\n", h, s); }
    u128str(argmax, s); printf("MAX %d %s\n", maxh, s);
    return 0;
}
