/* collatz_blocks.c: the state after the free bits, y = T^(W-1)(n) = 3^a + T^(W-1)(n - 2^(W-1)) (collatz_blocks.py).
 * Usage: collatz_blocks W JMAX. For every n in [2^(W-1), 2^W): runs W - 1 steps of T, checks the affine formula
 * (Terras) against a separate run from r = n - 2^(W-1), notes whether the orbit stayed >= n (a survivor), and
 * histograms y mod 2^JMAX and y mod 3, over all n and over survivors. Then, for j = 1 .. JMAX, prints
 *   B j M_all TV_all F_all M_surv TV_surv F_surv
 * TV: total-variation distance of y mod 2^j from uniform; F: max over odd h of |sum e(h y / 2^j)| / M.
 * And: M3 TV3_all TV3_surv (y mod 3) and AFFINE ok|BROKEN. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned __int128 u128;
static u128 step(u128 x, int *a) { if (x & 1) { (*a)++; return (3 * x + 1) >> 1; } return x >> 1; }
static void stats(long long *h, int JMAX, int j, double *tv, double *F, long long *Mout) {
    int K = 1 << j;
    long long *c = calloc(K, sizeof(long long)), M = 0;
    for (int i = 0; i < (1 << JMAX); i++) c[i & (K - 1)] += h[i];
    for (int i = 0; i < K; i++) M += c[i];
    double t = 0;
    for (int i = 0; i < K; i++) t += fabs((double)c[i] / M - 1.0 / K);
    *tv = t / 2;
    double best = 0;
    for (int hh = 1; hh < K; hh += 2) {
        double re = 0, im = 0;
        for (int i = 0; i < K; i++) if (c[i]) { double ang = 2 * M_PI * (double)hh * i / K; re += c[i] * cos(ang); im += c[i] * sin(ang); }
        double m = sqrt(re * re + im * im) / M;
        if (m > best) best = m;
    }
    *F = best; *Mout = M;
    free(c);
}
int main(int argc, char **argv) {
    int W = atoi(argv[1]), JMAX = atoi(argv[2]);
    long long *ha = calloc(1 << JMAX, sizeof(long long)), *hs = calloc(1 << JMAX, sizeof(long long));
    long long h3a[3] = {0}, h3s[3] = {0};
    int ok = 1;
    unsigned long long lo = 1ULL << (W - 1), hi = 1ULL << W;
    for (unsigned long long n = lo; n < hi; n++) {
        u128 x = n, r = n - lo;
        int a = 0, a2 = 0, surv = 1;
        for (int t = 1; t <= W - 1; t++) { x = step(x, &a); r = step(r, &a2); if (x < n) surv = 0; }
        u128 p = 1; for (int i = 0; i < a; i++) p *= 3;
        if (a != a2 || x != p + r) ok = 0;
        unsigned long long m = (unsigned long long)(x & ((1ULL << JMAX) - 1));
        ha[m]++; h3a[(int)(x % 3)]++;
        if (surv) { hs[m]++; h3s[(int)(x % 3)]++; }
    }
    for (int j = 1; j <= JMAX; j++) {
        double ta, fa, ts, fs; long long Ma, Ms;
        stats(ha, JMAX, j, &ta, &fa, &Ma);
        stats(hs, JMAX, j, &ts, &fs, &Ms);
        printf("B %d %lld %.6g %.6g %lld %.6g %.6g\n", j, Ma, ta, fa, Ms, ts, fs);
    }
    long long Ma = h3a[0] + h3a[1] + h3a[2], Ms = h3s[0] + h3s[1] + h3s[2];
    double t3a = 0, t3s = 0;
    for (int i = 0; i < 3; i++) { t3a += fabs((double)h3a[i] / Ma - 1.0 / 3); t3s += fabs((double)h3s[i] / Ms - 1.0 / 3); }
    printf("M3 %.6g %.6g\nAFFINE %s\n", t3a / 2, t3s / 2, ok ? "ok" : "BROKEN");
    return 0;
}
