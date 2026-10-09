/* rule30_cloud_ring_walls.c: every Rule 30 ring orbit of n cells whose some column reads 0 1^q for ever.

RUN-ON:     cpu, one core; memory 2^n bytes (1 GB at n = 30)
COMMAND:    gcc -O2 -o /tmp/rw tests/probes/lexicon/rule30_cloud_ring_walls.c && /tmp/rw NMIN NMAX
COST:       expected minutes for n up to 30.

Why. Local's SGW run (L433) found ring orbits whose column 0 reads exactly 0 1^q (the black-end walls, PERIOD-TWO.md's
"two Condrey ends" row) for q = 1, 2, 3, 4 and 6, on rings of 2 .. 22 cells, and none for q = 5, 7 or 8. Rings are
infinite periodic configurations, so a ring model excludes nothing; it is a counter-model (CL084's library) showing
that an argument using only local laws cannot close that wall. For q = 7 and q >= 9 the walls are now closed for
finite seeds (GC806 with Local's SG and WT tables). The open walls are q = 1 .. 6 and 8. This probe extends the
exhaustive ring search to larger rings, looking above all for models of q = 5 and q = 8.

Method. For each ring size n, walk the functional graph of Rule 30 on all 2^n rows (site i's left neighbour is i - 1
mod n), colouring states unvisited, on the current path, or done. Each new cycle is extracted, and every site's column
along the cycle is tested: it is a model of wall q when the column has least period q + 1 and one white cell per
period. Rows are not reduced by rotation or reflection; every cycle is found once.

PREDICTIONS, written 2026-10-09 16:28 BST, before any run of this script (n = 2 .. 30).
  RM-C0 (control): for n <= 22 the minimal ring sizes reproduce L433: q = 1 at 7 (also 14, 21), q = 2 at 12, q = 3 at 7
         (also 14, 21), q = 4 at 15, q = 6 at 15, and no model for q = 5, 7 or 8.
  RM-P1 (0.4): q = 5 has a ring model at some n from 23 to 30.
  RM-P2 (0.3): q = 8 has a ring model at some n from 23 to 30.
  RM-P3 (0.7): q = 7 has no ring model up to n = 30.
  RM-P4, the unexpected check (0.6): on the 7-cell ring the q = 1 and q = 3 models lie on one cycle, as two columns of
         the same orbit (Local's witness rows 0001001 and 0000001 are both 7-cell rows).
  Counterfactual. A q = 5 or q = 8 model gives the counter-model library its missing open walls, and says local laws
  alone cannot close them. None up to 30 cells, with the strip method stalled (L433), would make q = 5 and q = 8 the
  open walls most likely to fall to a further finite argument, though a ring model could still exist on larger rings.

OUTCOME of the first run, 2026-10-09 (n = 2 .. 30, one core at low priority beside RR3).
  RM-C0 PASS. Every n <= 22 reproduces L433: q = 1 and q = 3 at 7, 14 and 21; q = 2 at 12; q = 4 and q = 6 at 15;
    nothing for q = 5, 7 or 8.
  RM-P1 REFUTED and RM-P2 REFUTED: no ring of 23 to 30 cells has a model of wall 5 or wall 8.
  RM-P3 HELD: none of wall 7 either. No ring up to 30 cells models q = 5, 7, 8 or any q from 9 to 15.
  RM-P4 HELD (the unexpected check): on the 7-cell ring all seven cycles carrying wall 1 are the seven carrying
    wall 3. Each is one period-4 orbit in which one column reads 0101 and another 0111.
  New sizes from 23 to 30: wall 4 at 25 cells (5 cycles; the one new primitive size) and at 30; wall 2 at 24; walls
    1 and 3 at 28; wall 6 at 30. Every other new size is a multiple of an old one.
  So the counter-model library holds rings for walls 1, 2, 3, 4 and 6 and none for walls 5 and 8 up to 30 cells.
    Those two are the open walls without a known model of any kind: no ring, and the strip method stalls on them
    (L433) because its large components force neither neighbour. That makes them, tentatively, the walls to try next
    with a finite argument. Rings beyond 30 cells could still hold models.
*/
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int n;
static uint32_t mask;

static inline uint32_t step(uint32_t x) {
    uint32_t l = ((x << 1) | (x >> (n - 1))) & mask;   /* bit i holds site i - 1 */
    uint32_t r = ((x >> 1) | (x << (n - 1))) & mask;   /* bit i holds site i + 1 */
    return l ^ (x | r);
}

int main(int argc, char **argv) {
    int nmin = argc > 1 ? atoi(argv[1]) : 2, nmax = argc > 2 ? atoi(argv[2]) : 22;
    static int first[16];
    for (int q = 0; q < 16; q++) first[q] = 0;
    for (n = nmin; n <= nmax; n++) {
        mask = (n == 32) ? 0xffffffffu : ((1u << n) - 1);
        uint64_t N = (uint64_t)1 << n;
        uint8_t *col = calloc(N, 1);                  /* 0 unvisited, 1 on path, 2 done */
        if (!col) { fprintf(stderr, "no memory at n = %d\n", n); return 1; }
        uint64_t cycles = 0, cyc_states = 0;
        int models[16] = {0};
        uint32_t witness[16] = {0};
        uint64_t wperiod[16] = {0};
        int wcol[16] = {0};
        uint32_t *buf = NULL; uint64_t cap = 0;
        for (uint64_t s = 0; s < N; s++) {
            if (col[s]) continue;
            uint32_t x = (uint32_t)s;
            while (col[x] == 0) { col[x] = 1; x = step(x); }
            if (col[x] == 1) {                         /* a new cycle through x */
                uint64_t P = 0; uint32_t y = x;
                do {
                    if (P == cap) { cap = cap ? 2 * cap : 1024; buf = realloc(buf, cap * sizeof *buf); }
                    buf[P++] = y; y = step(y);
                } while (y != x);
                cycles++; cyc_states += P;
                int carried = 0;                       /* bit q set when this cycle carries wall q */
                for (int q = 1; q < 16; q++) {
                    int p = q + 1;
                    if (P % p) continue;
                    for (int i = 0; i < n; i++) {
                        int ok = 1, whites = 0;
                        for (int t = 0; t < p && ok; t++) whites += !((buf[t] >> i) & 1);
                        if (whites != 1) continue;
                        for (uint64_t t = p; t < P && ok; t++)
                            if (((buf[t] >> i) & 1) != ((buf[t - p] >> i) & 1)) ok = 0;
                        if (ok) {
                            if (!models[q]) { witness[q] = buf[0]; wperiod[q] = P; wcol[q] = i; }
                            models[q]++;
                            carried |= 1 << q;
                            break;                     /* count each cycle once per q */
                        }
                    }
                }
                if (carried && n <= 8) {               /* RM-P4: which walls share a cycle */
                    printf("  n = %d cycle of period %llu carries walls:", n, (unsigned long long)P);
                    for (int q = 1; q < 16; q++) if (carried >> q & 1) printf(" %d", q);
                    printf("\n");
                }
            }
            /* mark the path done */
            x = (uint32_t)s;
            while (col[x] == 1) { col[x] = 2; x = step(x); }
        }
        printf("n = %2d: cycles %llu (states on cycles %llu)", n, (unsigned long long)cycles,
               (unsigned long long)cyc_states);
        for (int q = 1; q < 16; q++)
            if (models[q]) {
                printf("; q=%d: %d cycle(s), e.g. row ", q, models[q]);
                for (int i = 0; i < n; i++) putchar('0' + ((witness[q] >> i) & 1));
                printf(" column %d period %llu", wcol[q], (unsigned long long)wperiod[q]);
                if (!first[q]) first[q] = n;
            }
        printf("\n");
        fflush(stdout);
        free(col);
    }
    printf("smallest ring with a model of wall q (0 = none in range):");
    for (int q = 1; q < 16; q++) printf(" q%d:%d", q, first[q]);
    printf("\n");
    return 0;
}
