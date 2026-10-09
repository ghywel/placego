/* rule30_rooted_walk.c: RW, rooted walks at dyadic periods q = 8, 16, 32 in C, one source orbit at a time, to their
 * first return to zero (S84's walk; rule30_r88_census.py does q = 8, 16 exhaustively in Python). Local's run (chat
 * L487); predictions in rule30_r88_census.py's RW block, pushed first.
 *
 * Build:  clang -O2 -o ~/np-scratch-int/rule30-oh/rw tests/probes/lexicon/rule30_rooted_walk.c
 * Run:    rw Q MAXSTEPS [FIRST_ORBIT] [N_ORBITS]
 *
 * A profile is a q-bit word, bit t = time t. The children of (a, b) are the words c with c(t + 1) = a(t) XOR (b(t) OR
 * c(t)) for t = 0 .. q - 2 and the closing condition a(q - 1) XOR (b(q - 1) OR c(q - 1)) = c(0); c(0) is tried as 0
 * and 1. The walk starts at (a, 0) with a = blk | blk << q/2 for an odd-weight q/2-bit block, one block per rotation
 * orbit (the least rotation). The live set of pair states is followed exactly (it never exceeded 2 at q <= 16); the
 * first depth at which a child is 0 is the return. Output per orbit: block, return depth or "alive at MAXSTEPS", and
 * the largest live set.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static int Q;
static uint64_t MASK;

static int children(uint64_t a, uint64_t b, uint64_t out[2]) {
    int n = 0;
    for (uint64_t c0 = 0; c0 < 2; c0++) {
        uint64_t c = c0, ct = c0;
        for (int t = 0; t < Q - 1; t++) {
            ct = ((a >> t) & 1) ^ (((b >> t) & 1) | ct);
            c |= ct << (t + 1);
        }
        if ((((a >> (Q - 1)) & 1) ^ (((b >> (Q - 1)) & 1) | ct)) == c0) out[n++] = c;
    }
    return n;
}

static uint64_t rotl(uint64_t x, int d, int w) {
    uint64_t m = (w == 64) ? ~0ULL : ((1ULL << w) - 1);
    d %= w;
    return d ? (((x << d) | (x >> (w - d))) & m) : x;
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s Q MAXSTEPS [FIRST_ORBIT] [N_ORBITS]\n", argv[0]); return 2; }
    Q = atoi(argv[1]);
    long long MAXS = atoll(argv[2]);
    int first = argc > 3 ? atoi(argv[3]) : 0, norb = argc > 4 ? atoi(argv[4]) : 1 << 30;
    if (Q < 4 || Q > 32 || (Q & (Q - 1))) { fprintf(stderr, "Q must be 4, 8, 16 or 32\n"); return 2; }
    MASK = (1ULL << Q) - 1;
    int h = Q / 2;
    int k = 0, done = 0;
    for (uint64_t blk = 1; blk < (1ULL << h) && done < norb; blk++) {
        if (!(__builtin_popcountll(blk) & 1)) continue;
        int least = 1;                                   /* keep the least rotation of each orbit */
        for (int d = 1; d < h; d++) if (rotl(blk, d, h) < blk) { least = 0; break; }
        if (!least) continue;
        if (k++ < first) continue;
        done++;
        uint64_t a = blk | (blk << h);
        uint64_t L[8][2]; int nl = 0, maxl = 0;          /* live pairs (x, y) */
        uint64_t ch[2];
        int nc = children(a, 0, ch);
        for (int i = 0; i < nc; i++) if (ch[i]) { L[nl][0] = 0; L[nl][1] = ch[i]; nl++; }
        long long depth = 1, ret = -1;
        while (nl && depth < MAXS) {
            uint64_t N[8][2]; int nn = 0;
            for (int i = 0; i < nl && ret < 0; i++) {
                nc = children(L[i][0], L[i][1], ch);
                for (int j = 0; j < nc; j++) {
                    if (ch[j] == 0) { ret = depth + 1; break; }
                    int dup = 0;
                    for (int u = 0; u < nn; u++) if (N[u][0] == L[i][1] && N[u][1] == ch[j]) dup = 1;
                    if (!dup) {
                        if (nn == 8) { printf("block %llx: live set exceeded 8 at depth %lld\n", (unsigned long long)blk, depth); return 3; }
                        N[nn][0] = L[i][1]; N[nn][1] = ch[j]; nn++;
                    }
                }
            }
            if (ret >= 0) break;
            for (int u = 0; u < nn; u++) { L[u][0] = N[u][0]; L[u][1] = N[u][1]; }
            nl = nn; if (nl > maxl) maxl = nl;
            depth++;
        }
        if (ret >= 0) printf("q %d block %0*llx: return %lld (max live %d)\n", Q, (h + 3) / 4, (unsigned long long)blk, ret, maxl);
        else if (!nl) printf("q %d block %0*llx: died without a zero child at depth %lld\n", Q, (h + 3) / 4, (unsigned long long)blk, depth);
        else printf("q %d block %0*llx: alive at %lld (max live %d)\n", Q, (h + 3) / 4, (unsigned long long)blk, depth, maxl);
        fflush(stdout);
    }
    return 0;
}
