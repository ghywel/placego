/* collatz_fibres.c: every same-odd-count admitted collision of the halved Collatz map, found by enumerating ALL admitted
 * words, independently of GPT's residue tree (G83-G89). Local, 2026-10-06; PROOFS.md waiting room; driver
 * collatz_audit_g83_g89.py.
 *
 * BUILD:   cc -O3 -o collatz_fibres tests/probes/prizes/collatz_fibres.c
 * USAGE:   ./collatz_fibres AMIN AMAX [free]     (free: no admission, every word of length t_a with a ones; the
 *                                                positive control, checked against a direct scan by the driver)
 *
 * W_a: the parity words of length t_a = floor(a log2 3) with a ones that are admitted at every prefix
 * (3^(odd count) >= 2^(prefix length)), i.e. ones at positions 0 = p_0 < ... < p_(a-1) with p_i <= floor(i log2 3).
 * A start n with word w has T^t(n) = (3^a n + B_w) / 2^t, B_w = sum_i 3^(a-1-i) 2^(p_i). Two starts with words w, w'
 * meet at step t exactly when 3^a (n' - n) = B_w - B_w', so a collision needs B_w = B_w' mod 3^a (G81's code).
 * Pass 1 stores (B mod 3^a, B) for every word and sorts; pass 2 re-walks the words to recover those in a colliding
 * residue. Each colliding pair is then realized: n_w = -B_w / 3^a mod 2^t (the residue class of the word), and the
 * pair is a collision of actual starts only if n_w' - n_w = (B_w - B_w') / 3^a mod 2^t. Every realized pair is checked
 * by direct evolution (both parity words, both odd counts, the common terminal, 2^t T^t(n) = 3^a n + B exactly in
 * 128-bit integers) and by the starts' widths.
 * Prints "EXT a Bmin Bmax" (the extreme intercepts over W_a), "A a words N residues_colliding K pairs P realized R" and one "PAIR a n n' terminal delta width w ok" line
 * per realized pair (n the least start of the pair's residue class).
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct { uint64_t r, B; } rec;
static int a_, t_, caps[64], free_;
static uint64_t P3[64], A;
static rec *recs; static long nrec;
static uint64_t *hotB; static long nhot;
typedef struct { uint64_t B, mask; } word;
static word *found; static long nfound, capfound;

static int cmp_rec(const void *x, const void *y) {
    const rec *p = x, *q = y;
    if (p->r != q->r) return p->r < q->r ? -1 : 1;
    return p->B < q->B ? -1 : p->B > q->B;
}
static int cmp_u64(const void *x, const void *y) {
    uint64_t p = *(const uint64_t *)x, q = *(const uint64_t *)y;
    return p < q ? -1 : p > q;
}

static void dfs1(int i, int prev, uint64_t B) {
    if (i == a_) { recs[nrec].r = B % A; recs[nrec].B = B; nrec++; return; }
    for (int p = i == 0 ? 0 : prev + 1; p <= caps[i]; p++) dfs1(i + 1, p, B + P3[a_ - 1 - i] * (1ULL << p));
}
static void dfs2(int i, int prev, uint64_t B, uint64_t mask) {
    if (i == a_) {
        if (bsearch(&B, hotB, nhot, 8, cmp_u64)) {
            if (nfound == capfound) { capfound = capfound ? 2 * capfound : 64; found = realloc(found, capfound * sizeof(word)); }
            found[nfound].B = B; found[nfound].mask = mask; nfound++;
        }
        return;
    }
    for (int p = i == 0 ? 0 : prev + 1; p <= caps[i]; p++)
        dfs2(i + 1, p, B + P3[a_ - 1 - i] * (1ULL << p), mask | (1ULL << p));
}

static int bitlen(uint64_t x) { int b = 0; while (x) { b++; x >>= 1; } return b; }

/* evolve n for t steps of the halved map; return the parity word as a mask, the odd count, the terminal */
static void evolve(uint64_t n, int t, uint64_t *mask, int *odd, uint64_t *term) {
    *mask = 0; *odd = 0;
    for (int s = 0; s < t; s++) {
        if (n & 1) { *mask |= 1ULL << s; (*odd)++; n = (3 * n + 1) / 2; } else n /= 2;
    }
    *term = n;
}

int main(int argc, char **argv) {
    int amin = argc > 1 ? atoi(argv[1]) : 1, amax = argc > 2 ? atoi(argv[2]) : 22;
    free_ = argc > 3 && !strcmp(argv[3], "free");
    P3[0] = 1;
    for (int i = 1; i < 40; i++) P3[i] = 3 * P3[i - 1];
    for (int a = amin; a <= amax; a++) {
        a_ = a; A = P3[a];
        t_ = bitlen(P3[a]) - 1;
        for (int i = 0; i < a; i++) caps[i] = free_ ? t_ - a + i : bitlen(P3[i]) - 1;
        /* count first, then allocate exactly */
        long cnt[64] = {0};
        { long f[80] = {0}, g[80]; f[0] = 1; if (free_) for (int p = 1; p <= caps[0]; p++) f[p] = 1;
          for (int i = 1; i < a; i++) { memset(g, 0, sizeof g); for (int p = 0; p <= caps[i - 1]; p++) if (f[p]) for (int q = p + 1; q <= caps[i]; q++) g[q] += f[p]; memcpy(f, g, sizeof f); }
          for (int p = 0; p < 80; p++) cnt[0] += f[p]; if (a == 1) cnt[0] = 1; }
        recs = malloc(cnt[0] * sizeof(rec)); nrec = 0;
        dfs1(0, -1, 0);
        if (nrec != cnt[0]) { fprintf(stderr, "count mismatch %ld %ld\n", nrec, cnt[0]); return 3; }
        uint64_t bmin = ~0ULL, bmax = 0;
        for (long i = 0; i < nrec; i++) { if (recs[i].B < bmin) bmin = recs[i].B; if (recs[i].B > bmax) bmax = recs[i].B; }
        printf("EXT %d %llu %llu\n", a, (unsigned long long)bmin, (unsigned long long)bmax);
        qsort(recs, nrec, sizeof(rec), cmp_rec);
        nhot = 0; long kres = 0;
        hotB = malloc(1024 * 8); long caphot = 1024;
        for (long i = 0; i < nrec;) {
            long j = i; while (j < nrec && recs[j].r == recs[i].r) j++;
            if (j - i > 1) { kres++; for (long k = i; k < j; k++) { if (nhot == caphot) { caphot *= 2; hotB = realloc(hotB, caphot * 8); } hotB[nhot++] = recs[k].B; } }
            i = j;
        }
        free(recs);
        qsort(hotB, nhot, 8, cmp_u64);
        nfound = 0;
        if (nhot) dfs2(0, -1, 0, 0);
        /* realize each pair inside a residue group */
        uint64_t tmask = (t_ == 64) ? ~0ULL : (1ULL << t_) - 1, inv = P3[a];
        for (int k = 0; k < 6; k++) inv *= 2 - P3[a] * inv;          /* inverse of 3^a mod 2^64 */
        long pairs = 0, realized = 0;
        for (long i = 0; i < nfound; i++) for (long j = 0; j < nfound; j++) {
            if (found[i].B <= found[j].B || found[i].B % A != found[j].B % A) continue;
            pairs++;                                                     /* B_i > B_j: start j is larger */
            uint64_t d = (found[i].B - found[j].B) / A;
            uint64_t ni = (0 - found[i].B * inv) & tmask, nj = (0 - found[j].B * inv) & tmask;
            if (((ni + d) & tmask) != nj) continue;
            realized++;
            uint64_t n = ni, n2 = ni + d, m1, m2, T1, T2; int o1, o2;
            evolve(n, t_, &m1, &o1, &T1); evolve(n2, t_, &m2, &o2, &T2);
            __int128 L1 = (__int128)T1 << t_, R1 = (__int128)A * n + found[i].B;
            __int128 L2 = (__int128)T2 << t_, R2 = (__int128)A * n2 + found[j].B;
            int ok = m1 == found[i].mask && m2 == found[j].mask && o1 == a && o2 == a && T1 == T2 && L1 == R1 && L2 == R2;
            /* the first step at which the two values agree (the words differ at position meet - 1) */
            int meet = 0; uint64_t x = n, y = n2;
            while (x != y) { x = (x & 1) ? (3 * x + 1) / 2 : x / 2; y = (y & 1) ? (3 * y + 1) / 2 : y / 2; meet++; }
            printf("PAIR %d %llu %llu %llu %llu width %d %d ok %d meet %d\n", a, (unsigned long long)n,
                   (unsigned long long)n2, (unsigned long long)T1, (unsigned long long)d, bitlen(n), bitlen(n2), ok, meet);
        }
        printf("A %d t %d words %ld residues_colliding %ld pairs %ld realized %ld\n", a, t_, nrec, kres, pairs, realized);
        fflush(stdout);
        free(hotB);
    }
    return 0;
}
