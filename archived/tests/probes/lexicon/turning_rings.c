/* turning_rings.c: Rule 30 rows that turn, F^p x = shift^s x with |s| > p, their walls, and damage fronts on them.
   Cloud, 2026-10-09; driven by rule30_cloud_turning_rings.py, which holds the predictions and the outcome.

   Conventions: x(i) is site i, site i + 1 is the right neighbour, F(x)(i) = x(i-1) XOR (x(i) OR x(i+1)), and
   shift^s x (i) = x(i - s), so s > 0 moves the pattern right.

   census P S NB   every x on the line with F^P x = shift^S x (|S| > P): the cycles of the window map. Prints
                   SUM, RING, CAN (rings of period <= NB, for the brute-force control), BITS (P = 1, N <= 1024)
                   and WIT (walls whose right neighbour shows an S/L word) lines.
   brute NB        every ring of least period N <= NB with F^q x = shift^r x on the ring, q = 1..3: BRU lines.
   damage T NF     reads "DMG id p s N bits" lines on stdin and prints the left damage front's speed: DV lines.
   damrand T NF SEED   post hoc control: the same measurement on NF random rows (DR lines).

   The window map. If s > p, F^p(x)(i) depends on x(i-p .. i+p) and equals x(i-s), which lies outside that window,
   so x(m) = G(x(m+s-p) .. x(m+s+p)): the s+p cells to the right of m fix x(m). If s < -p the same holds leftwards. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

static long mod(long a, long n) { a %= n; return a < 0 ? a + n : a; }
static long gcdl(long a, long b) { while (b) { long t = a % b; a = b; b = t; } return a < 0 ? -a : a; }

/* G[v] = F^p of a (2p+1)-cell window whose bit r (least significant first) is the cell at offset r - p */
static uint8_t *make_G(int p) {
  int n = 2 * p + 1; uint8_t *G = malloc(1u << n);
  for (uint32_t v = 0; v < (1u << n); v++) {
    int a[16] = {0}, len = n;
    for (int r = 0; r < n; r++) a[r] = (v >> r) & 1;
    while (len > 1) { for (int r = 0; r + 2 < len; r++) a[r] = a[r] ^ (a[r + 1] | a[r + 2]); len -= 2; }
    G[v] = (uint8_t)a[0];
  }
  return G;
}

static void step_ring(const uint8_t *x, uint8_t *y, long N) {
  for (long i = 0; i < N; i++) y[i] = x[mod(i - 1, N)] ^ (x[i] | x[(i + 1) % N]);
}

/* rows[r] = F^r x for r < q; returns 1 if F^q x = shift^u x on the ring */
static int turns(uint8_t **rows, int q, long N, long u) {
  uint8_t *y = malloc(N);
  step_ring(rows[q - 1], y, N);
  int ok = 1;
  for (long i = 0; i < N && ok; i++) ok = y[i] == rows[0][mod(i - u, N)];
  free(y); return ok;
}

static const char HS[] = "110100", HL[] = "1101000100";

/* analyse one ring: least turning period, walls, S/L words */
static void analyse(int p, int s, uint8_t *x, long N, int NB, long *nwall_tot, long *nvis_tot) {
  uint8_t *rows[4]; rows[0] = x;
  for (int r = 1; r <= p; r++) { rows[r] = malloc(N); step_ring(rows[r - 1], rows[r], N); }
  /* direct check of the defining relation */
  int ok = 1;
  for (long i = 0; i < N && ok; i++) ok = rows[p][i] == x[mod(i - s, N)];
  if (!ok) { printf("FAIL p=%d s=%d N=%ld relation\n", p, s, N); exit(1); }
  /* least turning period q | p and its shift u */
  int pq = p; long su = mod(s, N);
  for (int q = 1; q < p; q++) {
    if (p % q) continue;
    int found = 0;
    for (long u = 0; u < N && !found; u++)
      if (mod((long)q * u - s, N) == 0 && turns(rows, q, N, u)) { pq = q; su = u; found = 1; }
    if (found) break;
  }
  long g = gcdl(N, su), Pt = (long)pq * (su == 0 ? 1 : N / g);
  long sn = su > N / 2 ? su - N : su;                       /* shift per pq steps, in (-N/2, N/2] */
  long dens = 0; for (long i = 0; i < N; i++) dens += x[i];
  /* walls: alternating columns; then the right neighbour's word at the wall's white times */
  long nwall = 0, nvis = 0, nmark = 0;
  #define COL(j, t) rows[(t) % pq][mod((j) - ((t) / pq) * su, N)]
  for (long j = 0; j < N; j++) {
    if (Pt % 2) break;
    int c0 = COL(j, 0), alt = 1;
    for (long t = 1; t < Pt && alt; t++) alt = COL(j, t) == (c0 ^ (int)(t & 1));
    if (!alt) continue;
    nwall++;
    long nv = Pt / 2, first = -1, last = -1, nS = 0, nL = 0, bad = 0, ones = 0;
    for (long v = 0; v < nv; v++) {                           /* visible time t = 2v + c0 (the wall is white) */
      long t = 2 * v + c0;
      if (COL(j + 1, t)) {
        ones++;
        if (last >= 0) { long gap = v - last; if (gap == 3) nS++; else if (gap == 5) nL++; else bad = 1; }
        else first = v;
        last = v;
      }
    }
    if (!ones) continue;
    long gap = first + nv - last; if (gap == 3) nS++; else if (gap == 5) nL++; else bad = 1;
    if (bad) continue;
    nvis++;
    /* marker form: from the first visible 1, column j+1 is a cyclic concatenation of 110100 and 1101000100 */
    long t = 2 * first + c0, done = 0; int mark = 1;
    char *gaps = malloc(nS + nL + 1); long ng = 0;
    while (done < Pt && mark) {
      long v = (t - c0) / 2, vn = v + 1;
      while (!COL(j + 1, mod(2 * vn + c0, Pt))) vn++;
      long gl = vn - v; const char *h = gl == 3 ? HS : HL; long hl = gl == 3 ? 6 : 10;
      for (long q = 0; q < hl && mark; q++) mark = COL(j + 1, mod(t + q, Pt)) == h[q] - '0';
      gaps[ng++] = gl == 3 ? 'S' : 'L'; t += hl; done += hl;
    }
    gaps[ng] = 0;
    if (mark) nmark++;
    printf("WIT p=%d s=%d N=%ld pq=%d su=%ld Pt=%ld j=%ld c0=%d nS=%ld nL=%ld marker=%d gaps=%s bits=",
           p, s, N, pq, sn, Pt, j, c0, nS, nL, mark, gaps);
    for (long i = 0; i < N; i++) putchar('0' + x[i]);
    putchar('\n'); free(gaps);
  }
  printf("RING p=%d s=%d N=%ld pq=%d su=%ld Pt=%ld dens=%ld nwall=%ld nvis=%ld nmark=%ld\n",
         p, s, N, pq, sn, Pt, dens, nwall, nvis, nmark);
  if (N <= NB) {                                             /* canonical form for the brute-force control */
    uint32_t best = UINT32_MAX;
    for (long r = 0; r < N; r++) {
      uint32_t v = 0; for (long i = 0; i < N; i++) v |= (uint32_t)x[(i + r) % N] << i;
      if (v < best) best = v;
    }
    printf("CAN p=%d s=%d N=%ld canon=%u\n", p, s, N, best);
  }
  if (p == 1 && N <= 1024) {
    printf("BITS p=%d s=%d N=%ld pq=%d su=%ld bits=", p, s, N, pq, sn);
    for (long i = 0; i < N; i++) putchar('0' + x[i]);
    putchar('\n');
  }
  *nwall_tot += nwall; *nvis_tot += nvis;
  for (int r = 1; r <= p; r++) free(rows[r]);
}

static int census(int p, int s, int NB) {
  int L = abs(s) + p; uint32_t M = 1u << L, mask = M - 1, smask = (1u << (2 * p + 1)) - 1;
  uint8_t *G = make_G(p), *st = calloc(M, 1);
  size_t cap = 1 << 20, len; uint32_t *path = malloc(cap * sizeof *path);
  long cycles = 0, perpts = 0, maxN = 0, nwall = 0, nvis = 0;
  #define TW(w) (s > 0 ? (((w) << 1) & mask) | G[((w) >> (s - p - 1)) & smask] \
                      : ((w) >> 1) | ((uint32_t)G[(w) & smask] << (L - 1)))
  for (uint32_t s0 = 0; s0 < M; s0++) {
    if (st[s0]) continue;
    len = 0; uint32_t cur = s0;
    while (!st[cur]) {
      st[cur] = 1;
      if (len == cap) { cap *= 2; path = realloc(path, cap * sizeof *path); }
      path[len++] = cur; cur = TW(cur);
    }
    if (st[cur] == 1) {                                      /* a new cycle through cur */
      long N = 0; uint32_t w = cur;
      do { w = TW(w); N++; } while (w != cur);
      uint8_t *o = malloc(N), *x = malloc(N);
      w = cur;
      for (long t = 0; t < N; t++) { w = TW(w); o[t] = s > 0 ? (w & 1) : ((w >> (L - 1)) & 1); }
      /* s > 0: cur is x(1 .. L) and the outputs are x(0), x(-1), ..; s < 0: cur is x(0 .. L-1), outputs x(L), .. */
      for (long i = 0; i < N; i++) x[i] = s > 0 ? o[(N - i) % N] : o[mod(i - L, N)];
      cycles++; perpts += N; if (N > maxN) maxN = N;
      analyse(p, s, x, N, NB, &nwall, &nvis);
      free(o); free(x);
    }
    for (size_t i = 0; i < len; i++) st[path[i]] = 2;
  }
  printf("SUM p=%d s=%d L=%d cycles=%ld perpts=%ld maxN=%ld nwall=%ld nvis=%ld\n",
         p, s, L, cycles, perpts, maxN, nwall, nvis);
  free(st); free(path); free(G);
  return 0;
}

static int brute(int NB) {
  for (int N = 1; N <= NB; N++) {
    uint32_t mN = N == 32 ? UINT32_MAX : (1u << N) - 1;
    for (uint32_t x = 0; x <= mN; x++) {
      uint32_t best = x; int per = N;
      for (int r = 1; r < N; r++) {
        uint32_t v = ((x >> r) | (x << (N - r))) & mN;
        if (v < best) best = v;
        if (v == x && per == N) per = r;
      }
      if (best != x || per != N) continue;                   /* one canonical ring of least period N */
      uint32_t y = x;
      for (int q = 1; q <= 3; q++) {
        uint32_t z = 0;
        for (int i = 0; i < N; i++) {
          int l = (y >> ((i - 1 + N) % N)) & 1, c = (y >> i) & 1, rr = (y >> ((i + 1) % N)) & 1;
          z |= (uint32_t)(l ^ (c | rr)) << i;
        }
        y = z;
        for (int r = 0; r < N; r++) {                       /* shift^r x (i) = x(i - r) */
          uint32_t v = r ? ((x << r) | (x >> (N - r))) & mN : x;
          if (v == y) printf("BRU N=%d q=%d r=%d canon=%u\n", N, q, r, x);
        }
      }
      if (x == mN) break;
    }
  }
  return 0;
}

/* left damage front on a turning background, flips at NF sites spread over the ring */
static int damage(long T, long NF) {
  static char line[1 << 22];
  while (fgets(line, sizeof line, stdin)) {
    long id, N; int pq; long sn; char *bits = malloc(strlen(line));
    if (sscanf(line, "DMG %ld %d %ld %ld %s", &id, &pq, &sn, &N, bits) != 5) { free(bits); continue; }
    uint8_t *rows[4]; rows[0] = malloc(N);
    for (long i = 0; i < N; i++) rows[0][i] = bits[i] - '0';
    for (int r = 1; r < pq; r++) { rows[r] = malloc(N); step_ring(rows[r - 1], rows[r], N); }
    #define BG(t, i) rows[(t) % pq][mod((i) - ((t) / pq) * sn, N)]
    long W = 2 * T + 6, nf = NF < N ? NF : N, rightok = 1;
    uint8_t *d = malloc(W), *e = malloc(W);
    double sum = 0, mn = 1e9, mx = -1e9;
    for (long f = 0; f < nf; f++) {
      long c = (f * N) / nf, base = c - T - 3, k0 = T + 3;
      for (long k = 0; k < W; k++) d[k] = BG(0, base + k);
      d[k0] ^= 1;
      for (long t = 0; t < T; t++) {
        e[0] = BG(t + 1, base); e[W - 1] = BG(t + 1, base + W - 1);
        for (long k = 1; k < W - 1; k++) e[k] = d[k - 1] ^ (d[k] | d[k + 1]);
        uint8_t *tmp = d; d = e; e = tmp;
      }
      long kl = -1, kr = -1;
      for (long k = 0; k < W; k++) if (d[k] != BG(T, base + k)) { if (kl < 0) kl = k; kr = k; }
      if (kr != k0 + T) rightok = 0;
      double v = (double)(k0 - kl) / T;
      sum += v; if (v < mn) mn = v; if (v > mx) mx = v;
    }
    printf("DV id=%ld N=%ld mean=%.5f min=%.5f max=%.5f rightok=%ld\n", id, N, sum / nf, mn, mx, rightok);
    fflush(stdout);
    for (int r = 0; r < pq; r++) free(rows[r]);
    free(d); free(e); free(bits);
  }
  return 0;
}

/* POST HOC control (2026-10-09, after the first full run): the same left-front measurement on random rows, on a ring
   of 4T + 64 cells so that the damage cannot meet itself. Prints one DR line per flip. */
static int damrand(long T, long NF, unsigned seed) {
  long M = 4 * T + 64; uint8_t *a = malloc(M), *b = malloc(M), *na = malloc(M), *nb = malloc(M);
  uint64_t st = 0x9E3779B97F4A7C15ull ^ seed;
  for (long f = 0; f < NF; f++) {
    for (long i = 0; i < M; i++) { st ^= st << 13; st ^= st >> 7; st ^= st << 17; a[i] = b[i] = st & 1; }
    long c = M / 2; b[c] ^= 1;
    for (long t = 0; t < T; t++) {
      step_ring(a, na, M); step_ring(b, nb, M);
      uint8_t *x = a; a = na; na = x; x = b; b = nb; nb = x;
    }
    long kl = -1, kr = -1;
    for (long i = 0; i < M; i++) if (a[i] != b[i]) { if (kl < 0) kl = i; kr = i; }
    printf("DR f=%ld left=%.5f rightok=%d\n", f, (double)(c - kl) / T, kr == c + T);
  }
  return 0;
}

int main(int argc, char **argv) {
  if (argc >= 5 && !strcmp(argv[1], "damrand")) return damrand(atol(argv[2]), atol(argv[3]), (unsigned)atoi(argv[4]));
  if (argc >= 5 && !strcmp(argv[1], "census")) return census(atoi(argv[2]), atoi(argv[3]), atoi(argv[4]));
  if (argc >= 3 && !strcmp(argv[1], "brute")) return brute(atoi(argv[2]));
  if (argc >= 4 && !strcmp(argv[1], "damage")) return damage(atol(argv[2]), atol(argv[3]));
  fprintf(stderr, "usage: census P S NB | brute NB | damage T NF\n");
  return 2;
}
