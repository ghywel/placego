// Claim A: enumerate all hole sets, all ordered partitions of the pool into bins of given sizes,
// mark every achievable ordered target vector; then enumerate every admitted ordered target vector
// and report those not marked (failures).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define D 128
static int M, h, k, c[8], n;
static int pool[64];
static int *stamp; // indexed by u1..u_{k-1} (k<=4 -> 3 dims)
static int cur;
static int u[8];
static long long leaves;

static int idx(int *v) { int r = 0; for (int i = 0; i < k - 1; i++) { r = r * D + v[i]; } return r; }

static void choose(int bin, unsigned mask, int start, int left, int sum, unsigned remaining);
static void place(int bin, unsigned remaining) {
  if (bin == k - 1) { // last bin gets everything left; size check
    int cnt = __builtin_popcount(remaining);
    if (cnt != c[bin]) { fprintf(stderr, "size mismatch\n"); exit(1); }
    leaves++;
    for (int i = 0; i < k - 1; i++) if (u[i] >= D) { fprintf(stderr, "D too small\n"); exit(1); }
    stamp[idx(u)] = cur;
    return;
  }
  choose(bin, 0, 0, c[bin], 0, remaining);
}
static void choose(int bin, unsigned mask, int start, int left, int sum, unsigned remaining) {
  if (left == 0) { u[bin] = sum; place(bin + 1, remaining & ~mask); return; }
  for (int i = start; i < n; i++) {
    if (!(remaining >> i & 1)) continue;
    choose(bin, mask | (1u << i), i + 1, left - 1, sum + pool[i], remaining);
  }
}

static int L(int r) { return r * (r - 1) / 2; }
static int floordiv(int a, int b) { int q = a / b; if ((a % b != 0) && ((a < 0) != (b < 0))) q--; return q; }

static int admitted(int *v) {
  int mu = 1 << 30;
  for (int J = 1; J < (1 << k) - 1; J++) {
    int rJ = 0, uJ = 0;
    for (int i = 0; i < k; i++) if (J >> i & 1) { rJ += c[i]; uJ += v[i]; }
    int key = (uJ < L(rJ)) ? -1 : floordiv(uJ - L(rJ), rJ);
    if (key < mu) mu = key;
  }
  return mu >= h;
}

static int total;
static long long nadm, nfail, nholesets;
static int holes[64];
static int v[8];
static int lo[8], hi[8];

static void targets(int i, int partial) {
  if (i == k - 1) {
    v[i] = total - partial;
    if (!admitted(v)) return;
    nadm++;
    int ok = 1;
    for (int j = 0; j < k - 1; j++) if (v[j] < 0 || v[j] >= D) ok = 0;
    int feas = ok && stamp[idx(v)] == cur;
    if (!feas) {
      nfail++;
      printf("FAIL holes={");
      for (int j = 0; j < h; j++) printf("%s%d", j ? "," : "", holes[j]);
      printf("} targets=(");
      for (int j = 0; j < k; j++) printf("%s%d", j ? "," : "", v[j]);
      printf(")\n");
    }
    return;
  }
  // necessary condition from single-bin J={i} and its complement; full check in admitted()
  for (int x = lo[i]; x <= hi[i]; x++) { v[i] = x; targets(i + 1, partial + x); }
}

static void holeset(int start, int cnt) {
  if (cnt == h) {
    int isH[64] = {0};
    for (int j = 0; j < h; j++) isH[holes[j]] = 1;
    n = 0; total = 0;
    for (int x = 0; x <= M; x++) if (!isH[x]) { pool[n++] = x; total += x; }
    cur++;
    place(0, (n == 32) ? 0xffffffffu : ((1u << n) - 1));
    for (int i = 0; i < k; i++) {
      lo[i] = L(c[i]) + h * c[i];
      hi[i] = total - (L(n - c[i]) + h * (n - c[i]));
    }
    nholesets++;
    targets(0, 0);
    return;
  }
  for (int x = start; x <= M; x++) { holes[cnt] = x; holeset(x + 1, cnt + 1); }
}

int main(int argc, char **argv) {
  M = atoi(argv[1]); h = atoi(argv[2]); k = argc - 3;
  int s = 0;
  for (int i = 0; i < k; i++) { c[i] = atoi(argv[3 + i]); s += c[i]; }
  if (s != M + 1 - h) { fprintf(stderr, "sizes must sum to n\n"); return 1; }
  if (k != 4) { fprintf(stderr, "k=4 only\n"); return 1; }
  stamp = calloc((size_t)D * D * D, sizeof(int));
  holeset(0, 0);
  printf("M=%d h=%d sizes=", M, h);
  for (int i = 0; i < k; i++) printf("%d ", c[i]);
  printf(": holesets=%lld leaves=%lld admitted_ordered=%lld failures=%lld\n", nholesets, leaves, nadm, nfail);
  return 0;
}
