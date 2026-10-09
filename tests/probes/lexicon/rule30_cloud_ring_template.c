/* rule30_cloud_ring_template.c: RD, does any ring of up to 30 cells carry GC828's template D as a moving-frame column?

RUN-ON:     cpu, one core; memory 2^n bytes (1 GB at n = 30)
COMMAND:    gcc -O2 -o /tmp/rd tests/probes/lexicon/rule30_cloud_ring_template.c && /tmp/rd NMIN NMAX [WORD]
COST:       expected well under an hour for n up to 30, at low priority beside RR3.

Why. The critical bridge lead of Q6 (PERIOD-TWO.md section 6) has narrowed to GC828's retained template
D = (00000001011)(01011)^4, a 31-tick profile in the moving frame G(x)(i) = x(i) xor (x(i+1) OR x(i+2)) (Rule 30
followed by a shift, RULE30-GPT.md). GC839 and GC840 prove that a ring carrying D with the joint least-155 pair needs at
least 19 cells. Local's scratch enumeration (L463) found that no G-cycle on rings of 14 .. 20 cells has any column
equal to D, in any rotation, with no joint-period premise. A ring is a periodic world, so a ring carrying D would be
a counter-model: it would show that D is consistent with every local law, and that excluding it needs the finite
left support. This probe extends the exhaustive search to 30 cells with Cloud's ring enumerator (ring_walls.c's
functional-graph colouring, with G in place of F). GPT asked for no computation (GC843); this is Cloud's own bounded
check of the lead's ring status, claimed in CLOUD-LOCAL.md before the run.

Method. Every G-cycle on the n-cell ring is found once. A site's column over a cycle of length P matches when 31
divides P, the column repeats with period 31 over the whole cycle, and its first 31 ticks are a rotation of D. With
the optional WORD argument, any 0/1 word replaces D (the positive control).

PREDICTIONS, written 2026-10-09 19:16 BST, before any run of this script.
  RD-C0 (control): rings of 14 .. 20 cells carry no column equal to D, as Local found (L463).
  RD-C1 (positive control): a 0/1 word read from a G-cycle on an 11-cell ring by separate Python code (site 3, one
        period of the cycle reached from row 0b10110010011) is found on the 11-cell ring by this program.
  RD-P1 (0.75): no ring of 21 .. 30 cells carries D.
  RD-U, the unexpected check (0.5): some n in 21 .. 30 has a G-cycle whose length is divisible by 31 (31 is prime,
        so such cycles are rare on small rings; none of them may exist up to 30, which would make RD-P1 automatic).
  Counterfactual. A ring carrying D makes D a ring counter-model: local laws alone cannot exclude it, and the lead
  must use the finite left support. None to 30 cells extends Local's null by ten ring sizes. It does not exclude an
  infinite tail or a background after a bridge.

OUTCOME of the first run, 2026-10-09 (n = 2 .. 30, one core at low priority beside RR3, a few minutes).
  RD-C1 PASS, after one instrument fix. The first control run aborted ("stack smashing"): the word buffer was a fixed
    64 bytes and the control word has 154 ticks. With the buffer allocated to the word's length, the control word is
    found on the 11-cell ring (11 matching columns, every site of its 154-tick cycle), and its complement, run as a
    negative twin, is not found (0).
  RD-C0 PASS: rings of 14 .. 20 cells carry no column equal to D, as Local found.
  RD-P1 HELD: no ring of 21 .. 30 cells carries D. So no ring of up to 30 cells carries it.
  RD-U REFUTED (the unexpected check): no ring of 21 .. 30 cells has a G-cycle whose length 31 divides. Among all
    rings of up to 30 cells only the 18-cell ring has such cycles (2 of its 11), and neither carries D. So a G-column
    of least period 31 exists on no ring of 2 .. 30 cells except 18, and RD-P1 held for that reason.
*/
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int n;
static uint32_t mask;

static inline uint32_t G(uint32_t x) {                 /* G(x)(i) = x(i) xor (x(i+1) OR x(i+2)), ring of n sites */
    uint32_t r1 = ((x >> 1) | (x << (n - 1))) & mask;   /* bit i holds site i + 1 */
    uint32_t r2 = ((x >> 2) | (x << (n - 2))) & mask;   /* bit i holds site i + 2 */
    return x ^ (r1 | r2);
}

int main(int argc, char **argv) {
    int nmin = argc > 1 ? atoi(argv[1]) : 2, nmax = argc > 2 ? atoi(argv[2]) : 20;
    const char *word = argc > 3 ? argv[3] : "0000000101101011010110101101011";
    int L = (int)strlen(word);
    uint8_t *w = malloc(L);
    for (int i = 0; i < L; i++) w[i] = word[i] == '1';
    for (n = nmin; n <= nmax; n++) {
        mask = (n == 32) ? 0xffffffffu : ((1u << n) - 1);
        uint64_t N = (uint64_t)1 << n;
        uint8_t *col = calloc(N, 1);
        if (!col) { fprintf(stderr, "no memory at n = %d\n", n); return 1; }
        uint64_t cycles = 0, divisible = 0, matches = 0;
        uint32_t *buf = NULL; uint64_t cap = 0;
        uint32_t wit = 0; int witsite = -1; uint64_t witP = 0;
        for (uint64_t s = 0; s < N; s++) {
            if (col[s]) continue;
            uint32_t x = (uint32_t)s;
            while (col[x] == 0) { col[x] = 1; x = G(x); }
            if (col[x] == 1) {
                uint64_t P = 0; uint32_t y = x;
                do {
                    if (P == cap) { cap = cap ? 2 * cap : 1024; buf = realloc(buf, cap * sizeof *buf); }
                    buf[P++] = y; y = G(y);
                } while (y != x);
                cycles++;
                if (P % L == 0) {
                    divisible++;
                    for (int i = 0; i < n; i++) {
                        int ok = 1;
                        for (uint64_t t = L; t < P && ok; t++)
                            if (((buf[t] >> i) & 1) != ((buf[t - L] >> i) & 1)) ok = 0;
                        if (!ok) continue;
                        int rot = -1;
                        for (int r = 0; r < L && rot < 0; r++) {
                            int eq = 1;
                            for (int t = 0; t < L && eq; t++) if ((int)((buf[t] >> i) & 1) != w[(t + r) % L]) eq = 0;
                            if (eq) rot = r;
                        }
                        if (rot >= 0) {
                            if (!matches) { wit = buf[0]; witsite = i; witP = P; }
                            matches++;
                        }
                    }
                }
            }
            x = (uint32_t)s;
            while (col[x] == 1) { col[x] = 2; x = G(x); }
        }
        printf("n = %2d: G-cycles %llu, with length divisible by %d: %llu, matching columns %llu", n,
               (unsigned long long)cycles, L, (unsigned long long)divisible, (unsigned long long)matches);
        if (matches) {
            printf(" (e.g. row ");
            for (int i = 0; i < n; i++) putchar('0' + ((wit >> i) & 1));
            printf(", site %d, cycle length %llu)", witsite, (unsigned long long)witP);
        }
        printf("\n");
        fflush(stdout);
        free(col);
    }
    return 0;
}
