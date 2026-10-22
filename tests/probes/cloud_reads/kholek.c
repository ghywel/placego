/* CL504: k-bin H(h) census (k = 3..6) on [0, M] minus h holes anywhere, exact.
   H(h) admits a target vector iff u_J >= L(r) + h*r for every proper nonempty group J (L(r) = r(r-1)/2).  For each
   admitted vector (key mu = min_J floor((u_J - L(r_J)) / r_J) >= h) feasibility is decided against the enumerated set
   of achievable (k-1)-sum vectors; every failure is printed with the largest multiplicity of a (size, target).
   Also prints the histogram of keys over all failing vectors (spectrum-infeasible or not), so sharpness is visible.
   Generalises khole.c (CL503); validated against it at k = 4.
   OUTCOME (CL504): k = 3 reproduces CL443 T(h) (1, 3, 5 failures at h = 3, 4, 5); k = 4 reproduces khole.c; five bins
   33333 h <= 3, 33334 h <= 2, 33344 h = 1: no failures; key h - 1 attained (sharp).
   OUTCOME (CL506): hole-aware families are FALSE.  AWARE=1 (lower only): 3,620 non-equal failures at 3333 h = 2 (holes
   0, 10; targets 10, 11, 25, 35).  AWARE=2 (both sides): 24 at h = 2 (holes 2, 11; targets 6, 15, 24, 33), 4,457 at h = 3.
   AWARE=1 (with SEARCH): admission u_J >= L(r) + r*max(d_r, 1), d_r = holes below the r-th smallest; key h means admitted.
   SEARCH=1: test only vectors with key >= h - 1, by backtracking (no enumeration); failing keys then start at h - 1.
   Build: cc -O2 -o kholek kholek.c      Run: ./kholek M h c0 .. c(k-1) shard nshards
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 24
#define MAXK 6

static int k, n, M, h, C[MAXK], pool[MAXN], D;   /* D: radix for sums */
static unsigned *F, stamp;
static long long fails_by_key[64];
static int T[MAXK], search_mode;
static long long dump_every;
static int aware, need_r[64], needu_r[64], top_r[64];   /* AWARE=1: admitted iff u_J >= L(r) + r*max(d_r,1) for every proper J */

/* SEARCH mode: backtracking, bin by bin; pick c values (ascending indices) from avail summing to T[bin] */
static int place(int bin, unsigned avail);
static int pick(int bin, unsigned avail, int start, int cnt, int need, unsigned chosen) {
    if (cnt == 0) return need == 0 && place(bin + 1, avail & ~chosen);
    for (int i = start; i < n; i++) {
        if (!(avail >> i & 1)) continue;
        if (pool[i] * cnt > need) break;            /* ascending pool: the rest are too big */
        /* largest possible: cnt largest available from i on */
        int big = 0, c = 0; for (int j = n - 1; j >= i && c < cnt; j--) if (avail >> j & 1) { big += pool[j]; c++; }
        if (c < cnt || big < need) return 0;
        if (pick(bin, avail, i + 1, cnt - 1, need - pool[i], chosen | 1u << i)) return 1;
    }
    return 0;
}
static int place(int bin, unsigned avail) {
    if (bin == k - 1) return 1;                    /* the remainder has the right size and sum */
    return pick(bin, avail, 0, C[bin], T[bin], 0);
}

static void rec(int bin, unsigned avail, int *sums) {
    if (bin == k - 1) {
        size_t idx = 0; for (int i = 0; i < k - 1; i++) idx = idx * D + sums[i];
        F[idx] = stamp; return;
    }
    int idx[MAXN], m = 0; for (int i = 0; i < n; i++) if (avail >> i & 1) idx[m++] = i;
    int c = C[bin], a[8]; for (int i = 0; i < c; i++) a[i] = i;
    if (c > m) return;
    while (1) {
        unsigned used = 0; int s = 0; for (int i = 0; i < c; i++) { used |= 1u << idx[a[i]]; s += pool[idx[a[i]]]; }
        sums[bin] = s; rec(bin + 1, avail & ~used, sums);
        int j = c - 1; while (j >= 0 && a[j] == m - c + j) j--;
        if (j < 0) break;
        a[j]++; for (int i = j + 1; i < c; i++) a[i] = a[i - 1] + 1;
    }
}

int main(int argc, char **argv) {
    M = atoi(argv[1]); h = atoi(argv[2]); k = argc - 5;
    if (k < 3 || k > MAXK) { fprintf(stderr, "usage: kholek M h c0..c(k-1) shard nshards\n"); return 1; }
    for (int i = 0; i < k; i++) C[i] = atoi(argv[3 + i]);
    int shard = atoi(argv[3 + k]), nsh = atoi(argv[4 + k]);
    n = M + 1 - h; int cs = 0; for (int i = 0; i < k; i++) cs += C[i];
    if (cs != n) { fprintf(stderr, "sizes must sum to M+1-h\n"); return 1; }
    int maxc = 0; for (int i = 0; i < k; i++) if (C[i] > maxc) maxc = C[i];
    D = maxc * M + 1;
    size_t FS = 1; for (int i = 0; i < k - 1; i++) FS *= D;
    aware = getenv("AWARE") ? atoi(getenv("AWARE")) : 0;   /* 2: also upper u_J <= T_r(M) - r*max(e_r,1) */
    dump_every = getenv("DUMPEVERY") ? atoll(getenv("DUMPEVERY")) : 0;
    search_mode = getenv("SEARCH") != NULL;   /* only vectors with key >= h - 1, by backtracking */
    F = search_mode ? NULL : calloc(FS, sizeof(unsigned));
    int ng = (1 << k) - 2, gc[64], gl[64];
    for (int J = 1; J <= ng; J++) { gc[J] = 0; for (int i = 0; i < k; i++) if (J >> i & 1) gc[J] += C[i]; gl[J] = gc[J] * (gc[J] - 1) / 2; }
    long long pools = 0, admitted = 0, failures = 0;
    int Q[16]; for (int i = 0; i < h; i++) Q[i] = i;
    while (1) {
        if (h == 0 || (pools++) % nsh == shard) {   /* h = 0: one pool, shards split the targets instead */
            stamp++;
            int hole[64] = {0}, m = 0; for (int i = 0; i < h; i++) hole[Q[i]] = 1;
            for (int x = 0; x <= M; x++) if (!hole[x]) pool[m++] = x;
            int tot = 0; for (int i = 0; i < n; i++) tot += pool[i];
            if (aware) for (int r = 1; r <= n; r++) {
                int d = pool[r - 1] - (r - 1); need_r[r] = d > 1 ? d : (h > 0 ? 1 : 0);
                int e = (M - pool[n - r]) - (r - 1); needu_r[r] = aware == 2 ? (e > 1 ? e : (h > 0 ? 1 : 0)) : -1000000;
                top_r[r] = 0; for (int j = 0; j < r; j++) top_r[r] += M - j;
            }
            int sums[MAXK]; if (!search_mode) rec(0, (n == 32 ? ~0u : (1u << n) - 1), sums);
            /* targets: t_i >= L(c_i) (key >= 0 needs u_J >= L(r)); t_i <= maxc*M */
            int t[MAXK], lo[MAXK], hi[MAXK];
            for (int i = 0; i < k - 1; i++) { lo[i] = C[i] * (C[i] - 1) / 2; hi[i] = 0; for (int j = 0; j < C[i]; j++) hi[i] += pool[n - 1 - j]; }
            for (int i = 0; i < k - 1; i++) t[i] = lo[i];
            while (1) {
                if (h == 0 && t[0] % nsh != shard) goto nextvec;
                int s = 0; for (int i = 0; i < k - 1; i++) s += t[i];
                t[k - 1] = tot - s;
                if (t[k - 1] >= C[k - 1] * (C[k - 1] - 1) / 2) {
                    int mu = 1 << 30;
                    for (int J = 1; J <= ng; J++) {
                        int u = 0; for (int i = 0; i < k; i++) if (J >> i & 1) u += t[i];
                        int a = u < gl[J] ? -1 : (u - gl[J]) / gc[J];
                        if (aware) a = (u - gl[J] >= gc[J] * need_r[gc[J]] && top_r[gc[J]] - u >= gc[J] * needu_r[gc[J]]) ? h : (u < gl[J] ? -1 : (h > 0 ? h - 1 : -1));   /* key h iff admitted */
                        if (a < mu) mu = a;
                        if (mu < 0) break;
                    }
                    if (mu >= (search_mode && h > 0 ? h - 1 : 0)) {
                        int feas;
                        if (search_mode) { memcpy(T, t, sizeof T); feas = place(0, (1u << n) - 1); }
                        else { size_t idx = 0; for (int i = 0; i < k - 1; i++) idx = idx * D + t[i]; feas = t[k - 1] <= maxc * M && F[idx] == stamp; }
                        if (!feas) {
                            fails_by_key[mu < 63 ? mu : 63]++;
                            if (mu >= h) {
                                admitted++; failures++;
                                int mult = 1; for (int i = 0; i < k; i++) { int c = 0; for (int j = 0; j < k; j++) if (C[i] == C[j] && t[i] == t[j]) c++; if (c > mult) mult = c; }
                                printf("X key %d mult %d holes", mu, mult); for (int i = 0; i < h; i++) printf(" %d", Q[i]);
                                printf(" |"); for (int i = 0; i < k; i++) printf(" %d", t[i]); printf("\n");
                            }
                        } else if (mu >= h) {
                            admitted++;
                            if (dump_every && admitted % dump_every == 0) {   /* DUMPEVERY=N: every Nth admitted feasible vector */
                                printf("V holes"); for (int i = 0; i < h; i++) printf(" %d", Q[i]);
                                printf(" |"); for (int i = 0; i < k; i++) printf(" %d", t[i]); printf("\n");
                            }
                        }
                    }
                }
                nextvec:;
                int j = k - 2; while (j >= 0 && t[j] == hi[j]) { t[j] = lo[j]; j--; }
                if (j < 0) break;
                t[j]++;
            }
        }
        if (h == 0) break;
        int j = h - 1; while (j >= 0 && Q[j] == M - h + 1 + j) j--;
        if (j < 0) break;
        Q[j]++; for (int i = j + 1; i < h; i++) Q[i] = Q[i - 1] + 1;
    }
    for (int g = 0; g < 64; g++) if (fails_by_key[g]) printf("K %d %lld\n", g, fails_by_key[g]);
    printf("A %lld %lld\n", admitted, failures);
    return 0;
}
