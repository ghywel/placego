/* CL502: four bins on [0, M] minus h interior holes; exact.  For every hole set, every spectrum-feasible target
   vector (all 14 groups in their scalar spectra) is tested against the enumerated feasible set.  Infeasible ones are
   tallied by least group margin, by whether two equal-size bins have equal targets ("rep"), and by the longest run
   of adjacent holes.  C port of khole_fourbin.py / khole_runs.py (CL501), validated against them at M = 14, h = 3.
   OUTCOME (CL502): 333X, h = 3, isolated holes: top non-repeat margin 4 at M = 15..19 (count, not density); ladder
   h = 1..4: none, 2, 4, 6 (isolated), none, 2, 5, 8 (all).
   Build: cc -O2 -o khole khole.c      Run: ./khole M h c0 c1 c2 c3 [shard nshards]
   With shards, raw lines "H run rep margin count" and "E run rep margin holes... | targets" are printed for merging.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 24
#define MAXS 128
#define MAXM 64

static int n, pool[MAXN], C[4];
static unsigned *F;            /* F[(a*MAXS+b)*MAXS+c] == stamp  <=>  (a, b, c) achievable */
static unsigned stamp = 0;
static long long hist[MAXN][2][MAXM * 8];
static int exQ[MAXN][2][MAXM * 8][8], exT[MAXN][2][MAXM * 8][4], exSet[MAXN][2][MAXM * 8];
static int h;

static void enum_feasible(void) {
    int idx[MAXN], used[MAXN];
    memset(used, 0, sizeof used);
    /* recursive-free: three nested combination loops over unused indices */
    int a[8], b[8], c[8];
    int k0 = C[0], k1 = C[1], k2 = C[2];
    (void)idx;
    for (int i = 0; i < k0; i++) a[i] = i;
    while (1) {
        int sa = 0; for (int i = 0; i < k0; i++) { sa += pool[a[i]]; used[a[i]] = 1; }
        int r1[MAXN], m1 = 0; for (int i = 0; i < n; i++) if (!used[i]) r1[m1++] = i;
        for (int i = 0; i < k1; i++) b[i] = i;
        while (1) {
            int sb = 0, u2[MAXN]; memset(u2, 0, sizeof u2);
            for (int i = 0; i < k1; i++) { sb += pool[r1[b[i]]]; u2[b[i]] = 1; }
            int r2[MAXN], m2 = 0; for (int i = 0; i < m1; i++) if (!u2[i]) r2[m2++] = r1[i];
            for (int i = 0; i < k2; i++) c[i] = i;
            while (1) {
                int sc = 0; for (int i = 0; i < k2; i++) sc += pool[r2[c[i]]];
                F[((size_t)sa * MAXS + sb) * MAXS + sc] = stamp;
                int j = k2 - 1; while (j >= 0 && c[j] == m2 - k2 + j) j--;
                if (j < 0) break;
                c[j]++; for (int i = j + 1; i < k2; i++) c[i] = c[i - 1] + 1;
            }
            int j = k1 - 1; while (j >= 0 && b[j] == m1 - k1 + j) j--;
            if (j < 0) break;
            b[j]++; for (int i = j + 1; i < k1; i++) b[i] = b[i - 1] + 1;
        }
        for (int i = 0; i < k0; i++) used[a[i]] = 0;
        int j = k0 - 1; while (j >= 0 && a[j] == n - k0 + j) j--;
        if (j < 0) break;
        a[j]++; for (int i = j + 1; i < k0; i++) a[i] = a[i - 1] + 1;
    }
}

int main(int argc, char **argv) {
    if (argc < 7) { fprintf(stderr, "usage: khole M h c0 c1 c2 c3\n"); return 1; }
    int M = atoi(argv[1]); h = atoi(argv[2]);
    for (int i = 0; i < 4; i++) C[i] = atoi(argv[3 + i]);
    int shard = argc > 8 ? atoi(argv[7]) : 0, nsh = argc > 8 ? atoi(argv[8]) : 1;
    n = M + 1 - h;
    if (C[0] + C[1] + C[2] + C[3] != n) { fprintf(stderr, "sizes must sum to M+1-h\n"); return 1; }
    F = calloc((size_t)MAXS * MAXS * MAXS, sizeof(unsigned));
    long long spec = 0, pools = 0;
    int Q[8]; for (int i = 0; i < h; i++) Q[i] = 1 + i;
    while (1) {
        if ((pools++) % nsh != shard) goto next;
        stamp++;
        int m = 0, hole[MAXM + 1]; memset(hole, 0, sizeof hole);
        for (int i = 0; i < h; i++) hole[Q[i]] = 1;
        for (int x = 0; x <= M; x++) if (!hole[x]) pool[m++] = x;
        int run = 0, cur = 0; for (int i = 0; i < h; i++) { cur = (i && Q[i] == Q[i - 1] + 1) ? cur + 1 : 1; if (cur > run) run = cur; }
        int tot = 0; for (int i = 0; i < n; i++) tot += pool[i];
        enum_feasible();
        /* spectra */
        static unsigned char sp[MAXN + 1][MAXS * 4];
        memset(sp, 0, sizeof sp); sp[0][0] = 1;
        for (int i = 0; i < n; i++) for (int k = i; k >= 0; k--) for (int s = MAXS * 4 - 1 - pool[i]; s >= 0; s--) if (sp[k][s]) sp[k + 1][s + pool[i]] = 1;
        int mins[MAXN + 1], maxs[MAXN + 1]; mins[0] = maxs[0] = 0;
        for (int k = 1; k <= n; k++) { mins[k] = mins[k - 1] + pool[k - 1]; maxs[k] = maxs[k - 1] + pool[n - k]; }
        int t[4];
        for (t[0] = mins[C[0]]; t[0] <= maxs[C[0]]; t[0]++)
        for (t[1] = mins[C[1]]; t[1] <= maxs[C[1]]; t[1]++)
        for (t[2] = mins[C[2]]; t[2] <= maxs[C[2]]; t[2]++) {
            t[3] = tot - t[0] - t[1] - t[2];
            int ok = 1, mg = 1 << 30;
            for (int J = 1; J < 15 && ok; J++) {
                int cj = 0, tj = 0; for (int i = 0; i < 4; i++) if (J >> i & 1) { cj += C[i]; tj += t[i]; }
                if (tj < 0 || tj >= MAXS * 4 || !sp[cj][tj]) { ok = 0; break; }
                int a = tj - mins[cj], b = maxs[cj] - tj; if (a < mg) mg = a; if (b < mg) mg = b;
            }
            if (!ok) continue;
            spec++;
            if (F[((size_t)t[0] * MAXS + t[1]) * MAXS + t[2]] == stamp) continue;
            int rep = 0; for (int i = 0; i < 4; i++) for (int j = i + 1; j < 4; j++) if (C[i] == C[j] && t[i] == t[j]) rep = 1;
            hist[run][rep][mg]++;
            if (!exSet[run][rep][mg]) { exSet[run][rep][mg] = 1; memcpy(exQ[run][rep][mg], Q, sizeof Q); memcpy(exT[run][rep][mg], t, sizeof t); }
        }
        next:;
        int j = h - 1; while (j >= 0 && Q[j] == M - h + j) j--;
        if (j < 0) break; Q[j]++; for (int i = j + 1; i < h; i++) Q[i] = Q[i - 1] + 1;
        if (h == 0) break;
    }
    if (nsh > 1) {
        for (int r = 0; r <= h; r++) for (int rep = 0; rep < 2; rep++) for (int g = 0; g < MAXM * 8; g++) if (hist[r][rep][g]) {
            printf("H %d %d %d %lld\n", r, rep, g, hist[r][rep][g]);
            printf("E %d %d %d", r, rep, g); for (int i = 0; i < h; i++) printf(" %d", exQ[r][rep][g][i]);
            printf(" | %d %d %d %d\n", exT[r][rep][g][0], exT[r][rep][g][1], exT[r][rep][g][2], exT[r][rep][g][3]);
        }
        printf("S %lld\n", spec);
        return 0;
    }
    printf("M %d holes %d sizes %d%d%d%d pools %lld spectrum-feasible %lld\n", M, h, C[0], C[1], C[2], C[3], pools, spec);
    for (int r = 0; r <= h; r++) for (int rep = 0; rep < 2; rep++) {
        int any = 0; for (int g = 0; g < MAXM * 8; g++) if (hist[r][rep][g]) any = 1;
        if (!any) continue;
        printf("  run %d %s:", r, rep ? "rep" : "nonrep");
        int top = 0; for (int g = 0; g < MAXM * 8; g++) if (hist[r][rep][g]) { printf(" %d:%lld", g, hist[r][rep][g]); top = g; }
        printf("  | top example holes");
        for (int i = 0; i < h; i++) printf(" %d", exQ[r][rep][top][i]);
        printf(" targets %d %d %d %d\n", exT[r][rep][top][0], exT[r][rep][top][1], exT[r][rep][top][2], exT[r][rep][top][3]);
    }
    return 0;
}
