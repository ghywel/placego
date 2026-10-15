#!/usr/bin/env python3
"""rule30_cloud_coin_shape.py: is the centre column's coin fair only on average, or fair in shape? And does it know the primes?

RUN-ON:     cpu (a C generator compiled with cc at run time; numpy for the counting)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_coin_shape.py [LOGN=20]
COST:       about a minute at LOGN = 20 (the generator is quadratic in N: N^2/128 word operations).

The owner, 2026-10-15: "In the centre column is the coin toss really fair. Are we saying it averages 50/50 over time,
or given a real coin toss run, let's say 1 million, what does the shape of the statistic occurrence of 00, 000, 0000
... / 11, 111, 1111 ... look like and does our coin test reveal this distribution as much as its fairness, or is it a
different shape." And: "my gut instinct is the primes are important here in a way we haven't identified."

What the record's coin tests measure (RULE30-PRIZE.md 8.34): the density over 2^17 steps (0.49947) and the block
entropy at block length 10 (0.9972 against a coin's 0.9971). The run-length distribution up to length 8 is a function
of the length-10 block frequencies, so h_10 already constrains it; runs of 9 and more are not covered, and no probe
has printed the run-length histogram itself. The linear complexity profile (8.70) and the flat spectrum (8.3) are
other faces of the same coin.

What a fair coin's shape is. In a fair iid sequence of length N, the maximal runs of each symbol have iid geometric
lengths: a share 2^-k of the runs has length exactly k, about N/4 runs per symbol, and the longest run of a symbol is
about log2(N) - 1 with a spread of about two. So the test of shape is: the histogram of run lengths against 2^-k, for
both symbols, judged against pseudo-random coins of the same length.

Setting. The single seed on the infinite line, centre column c(t) for t < N = 2^LOGN, from a C generator (shrinking
window: cells outside distance N - t at time t cannot reach the centre by time N, so stale values there are harmless).
Control C0: the first 102 bits equal OEIS A051023 (the string stored in tests/probes/lexicon/lexicon_check.py).
Twenty pseudo-random coins of length N (numpy's default generator, seeds 1 .. 20) give the reference spread.

PREDICTIONS, written 2026-10-15 before any run and pushed before it.
  C0 (exact control): the generator reproduces A051023; density within 3/sqrt(N) of 1/2.
  C1 (control of the method): the twenty coins' run histograms fit 2^-k: their chi-square values (k = 1..12 plus a
     pooled tail) have a median near the degrees of freedom (12), and none is above 40.
  P1 (0.8): the column's run histograms, for 0 and for 1, each sit inside the coins' spread: chi-square percentile
     between 5 and 95 among the twenty coins, for both symbols.
  P2 (0.7): the longest runs of 0 and of 1 both lie in [16, 24] at LOGN = 20, and inside the coins' min .. max.
  P3 (0.6): the geometric ratio, estimated as the mean of count(k+1)/count(k) over k = 1..10, is within 0.500 +- 0.01
     for both symbols.
  K, the kill test for the direct reading of the primes hunch (0.85 that it kills): with x(n) = 2c(n) - 1, the three
     sums S_p = sum over primes p < N of x(p), S_lambda = sum x(n) lambda(n) (Liouville), S_mu = sum x(n) mu(n)
     (Möbius) all have |S| / sigma below 3, where sigma is the coin's standard deviation (sqrt of the number of
     terms with nonzero weight). Any |S| / sigma above 4 would mean the column is correlated with the primes' parity
     structure, and the hunch would have a direct handle. Inconclusive (3 .. 4) tips to repeating at LOGN = 22 before
     any claim. A kill here kills only the DIRECT reading (the column at prime times, or against Möbius); it says
     nothing about prime structure in another dimension of the problem (RULE30-PRIZE.md 8.114).
  U, the unexpected check (0.7): the velocity column c(t) XOR c(t+1), which is Rule 210's column (8.70), has the same
     coin shape: chi-square percentile between 5 and 95 for both symbols.
  Counterfactual. A histogram outside the coins' spread, especially a deficit of long runs, would be the first shape
  statistic to separate the column from a coin, and it would bear on the zero-run records (8.36) directly.

OUTCOME at LOGN = 20, 2026-10-15 11:57 BST (predictions pushed in a398197; 17 s).
  C0 PASS (A051023; density 0.50066). C1 PASS (coins' chi2 median 12.7, max 20.0).
  P1 REFUTED at the edge: the 0-runs' chi2 is 20.8, above all twenty coins (p about 0.05 at 12 degrees of freedom),
    with +755 single zeros (about +2.9 sigma) and a deficit of runs of 11 or more (103 against 128 at k = 11); the
    1-runs sit at the 55th percentile (chi2 12.3).
  P2 REFUTED by one: the longest run of 1 is 22 against the coins' 16 .. 21 (twenty coins do not delimit a maximum;
    a calibration error in the prediction, not evidence). Longest 0-run 19.
  P3 REFUTED by calibration: the mean of ratios includes k = 10 and 11, whose counts are a few hundred, so +- 0.01 was
    far too tight; the values 0.4897 and 0.4969 are consistent with the histogram above.
  K HELD: |S/sigma| = 1.50 (prime times), 1.06 (Liouville), 1.92 (Möbius); the twenty coins' worst is 3.06. The
    direct reading of the primes hunch is killed at this length.
  U REFUTED at the edge, the other way: the velocity's 1-runs have chi2 18.2, above the coins' 17.7 (p about 0.11);
    its 0-runs sit at the 40th percentile.
  POST HOC prediction before the LOGN = 22 run (the same code, four times the length, twenty new coins): if the
    0-runs' deviation is real, its chi2 grows about fourfold, to above 40, and the k = 1 excess and k >= 11 deficit
    keep their signs; if it is a fluctuation, chi2 falls back inside the coins' spread. Probability that it is real:
    0.3. The velocity's 1-runs are judged the same way.

OUTCOME at LOGN = 22, 2026-10-15 12:05 BST (the post hoc prediction pushed in f7957fc before this run; 3 m 54 s).
  C0, C1 PASS. P1, P2 and P3 all HELD at this length (percentiles 90 and 95; longest 20 and 23 inside the coins'
    18 .. 26; ratios 0.4963 and 0.4958).
  The post hoc prediction's "real" branch is REFUTED: the 0-runs' chi2 is 19.2, not above 40, and on the fresh three
    quarters of the run (the bits the 2^20 run never saw) the k = 1 excess is +0.4 sigma and the k = 11 deficit -0.8
    sigma. The four fresh-part chi2 values are 13.8, 21.8, 18.5 and 15.7 at 12 degrees of freedom. A fluctuation.
  K HELD: |S/sigma| = 2.28 (prime times), 1.80 (Liouville), 2.76 (Möbius), all below 3, against a coins' worst of
    1.73. But all three keep their signs on the fresh three quarters (+1.76, -1.47, -2.08), and the three are
    correlated (mu = lambda on squarefree numbers). Killed by K's own rule at this length; the drift is handed to
    JOB CS-01 rather than dropped.
  U REFUTED at the edge again, in a different cell (the velocity's 0-runs, chi2 23.0; on the fresh part 18.5).
    Four cells at two lengths against twenty coins' maxima: one or two edge cases are expected.

JOB CS-01 (Cloud, 2026-10-15, for Local on the M5; low priority, one run).
  RUN-ON:   Local. The generator is single-threaded and quadratic: 2^24 is about sixteen times the 2^22 run.
  COMMAND:  python3 tests/probes/lexicon/rule30_cloud_coin_shape.py 24
  COST:     about an hour of one core, under a gigabyte.
  PREDICTION (written before the run; 0.25 that it holds): if the Möbius drift is a real relative bias, S_mu / sigma
            at 2^24 is about -5.5 (the sum grows like N, sigma like sqrt N); if it is noise, |S_mu / sigma| < 3. The
            same for S_p (about +4.5 if real) and S_lambda (about -3.6 if real). The three move together or not at all.
  OUTCOME:  append here and in RULE30-PRIZE.md 8.114. Above 4 on all three is a direct handle on the owner's hunch and
            goes to GPT at once; below 3 closes the direct reading at 2^24.
"""
import os
import pathlib
import subprocess
import sys
import tempfile

import numpy as np

LOGN = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 20
N = 1 << LOGN
A051023 = ("1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,"
           "0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1")
KMAX = 12          # histogram bins 1..KMAX, then a pooled tail

GEN_C = r"""
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
    long N = atol(argv[1]);
    long W = 2 * N + 256, words = W / 64 + 2;
    uint64_t *a = calloc(words, 8), *b = calloc(words, 8);
    long centre = N + 128;
    a[centre >> 6] |= 1ULL << (centre & 63);
    char *out = malloc(N + 1);
    for (long t = 0; t < N; t++) {
        out[t] = ((a[centre >> 6] >> (centre & 63)) & 1) ? '1' : '0';
        long lo = (centre - (N - t) - 2) >> 6, hi = (centre + (N - t) + 2) >> 6;
        if (lo < 1) lo = 1;
        if (hi > words - 2) hi = words - 2;
        for (long w = lo; w <= hi; w++) {
            uint64_t c = a[w];
            uint64_t l = (c << 1) | (a[w - 1] >> 63);
            uint64_t r = (c >> 1) | (a[w + 1] << 63);
            b[w] = l ^ (c | r);
        }
        uint64_t *s = a; a = b; b = s;
    }
    out[N] = 0;
    fputs(out, stdout);
    return 0;
}
"""


def generate(n):
    d = tempfile.mkdtemp(prefix='coinshape-')
    src = pathlib.Path(d) / 'gen.c'
    src.write_text(GEN_C)
    exe = pathlib.Path(d) / 'gen'
    subprocess.run(['cc', '-O3', '-o', str(exe), str(src)], check=True)
    out = subprocess.run([str(exe), str(n)], capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype=np.uint8) - ord('0')


def runs(bits):
    """Maximal run lengths of 0 and of 1."""
    change = np.flatnonzero(np.diff(bits)) + 1
    starts = np.concatenate(([0], change))
    ends = np.concatenate((change, [len(bits)]))
    lengths = ends - starts
    sym = bits[starts]
    return lengths[sym == 0], lengths[sym == 1]


def histogram(lengths):
    h = np.bincount(lengths, minlength=KMAX + 2)
    obs = np.concatenate((h[1:KMAX + 1], [h[KMAX + 1:].sum()]))
    return obs


def chi2(lengths):
    obs = histogram(lengths)
    R = len(lengths)
    exp = np.array([R * 2.0 ** -k for k in range(1, KMAX + 1)] + [R * 2.0 ** -KMAX])
    return float(((obs - exp) ** 2 / exp).sum()), obs, exp


def ratio(lengths):
    h = np.bincount(lengths, minlength=12)
    return float(np.mean([h[k + 1] / h[k] for k in range(1, 11)]))


def sieve_lambda_mu(n):
    """Liouville lambda and Möbius mu for 0..n-1 by a smallest-prime-factor sieve (lambda(0) = mu(0) = 0)."""
    spf = np.zeros(n, dtype=np.int64)
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == 0:
            idx = np.arange(p * p, n, p)
            m = spf[idx] == 0
            spf[idx[m]] = p
    primes_mask = (spf == 0)
    primes_mask[:2] = False
    spf[primes_mask] = np.flatnonzero(primes_mask)
    lam = np.zeros(n, dtype=np.int64)
    mu = np.zeros(n, dtype=np.int64)
    lam[1] = 1
    mu[1] = 1
    for m in range(2, n):            # multiplicative recursion; a Python loop over 10^6 is a few seconds
        p = spf[m]
        q = m // p
        lam[m] = -lam[q]
        mu[m] = 0 if q % p == 0 else -mu[q]
    return primes_mask, lam, mu


def report_shape(name, bits, coins):
    z, o = runs(bits)
    out = {}
    for sym, lengths, coin_chi in (('0', z, coins['chi0']), ('1', o, coins['chi1'])):
        c, obs, exp = chi2(lengths)
        pct = 100.0 * np.mean(np.array(coin_chi) < c)
        out[sym] = (c, pct, int(lengths.max()), ratio(lengths), obs, exp)
        print('  %s runs of %s: %d runs, chi2 %.1f (coins: median %.1f, max %.1f), percentile %.0f, longest %d '
              '(coins %d..%d), geometric ratio %.4f'
              % (name, sym, len(lengths), c, np.median(coin_chi), max(coin_chi), pct, lengths.max(),
                 coins['long' + sym][0], coins['long' + sym][1], ratio(lengths)))
    print('  %s run-length histogram (k = 1..%d, tail): observed 0 %s' % (name, KMAX, ' '.join(str(v) for v in out['0'][4])))
    print('  %s                                     expected %s' % (name, ' '.join('%.0f' % v for v in out['0'][5])))
    print('  %s                                     observed 1 %s' % (name, ' '.join(str(v) for v in out['1'][4])))
    return out


def main():
    bits = generate(N)
    ref = np.array([int(x) for x in A051023.split(',')], dtype=np.uint8)
    dens = bits.mean()
    print('C0 A051023 reproduced (%d terms): %s; density %.5f (3/sqrt N = %.5f)'
          % (len(ref), bool(np.array_equal(bits[:len(ref)], ref)), dens, 3 / N ** 0.5))
    coins = {'chi0': [], 'chi1': [], 'long0': [N, 0], 'long1': [N, 0], 'primes': []}
    for seed in range(1, 21):
        cb = np.random.default_rng(seed).integers(0, 2, N, dtype=np.uint8)
        cz, co = runs(cb)
        coins['chi0'].append(chi2(cz)[0])
        coins['chi1'].append(chi2(co)[0])
        coins['long0'] = [min(coins['long0'][0], cz.max()), max(coins['long0'][1], cz.max())]
        coins['long1'] = [min(coins['long1'][0], co.max()), max(coins['long1'][1], co.max())]
        coins['bits%d' % seed] = cb
    allchi = coins['chi0'] + coins['chi1']
    print('C1 coins (20 x 2 symbols): chi2 median %.1f, max %.1f (df %d)' % (np.median(allchi), max(allchi), KMAX))
    print('\nShape of the centre column, N = 2^%d' % LOGN)
    col = report_shape('column', bits, coins)
    print('P1 percentiles 5..95 for both symbols: %s' % all(5 <= col[s][1] <= 95 for s in '01'))
    print('P2 longest runs in [16, 24] and inside the coins: %s (0: %d, 1: %d)'
          % (all(16 <= col[s][2] <= 24 and coins['long' + s][0] <= col[s][2] <= coins['long' + s][1] for s in '01'),
             col['0'][2], col['1'][2]))
    print('P3 geometric ratio within 0.500 +- 0.01 for both: %s (%.4f, %.4f)'
          % (all(abs(col[s][3] - 0.5) <= 0.01 for s in '01'), col['0'][3], col['1'][3]))

    print('\nK: the column against the primes (direct reading)')
    primes_mask, lam, mu = sieve_lambda_mu(N)
    x = 2 * bits.astype(np.int64) - 1
    tests = {
        'S_p (x at prime times)': (x[primes_mask].sum(), primes_mask.sum()),
        'S_lambda (x . Liouville)': ((x * lam).sum(), int((lam != 0).sum())),
        'S_mu (x . Möbius)': ((x * mu).sum(), int((mu != 0).sum())),
    }
    worst = 0.0
    for name, (S, n_terms) in tests.items():
        z = S / n_terms ** 0.5
        worst = max(worst, abs(z))
        print('  %-28s S = %8d over %7d terms; S/sigma = %+.2f' % (name, S, n_terms, z))
    coin_worst = 0.0
    for seed in range(1, 21):
        xc = 2 * coins['bits%d' % seed].astype(np.int64) - 1
        for S, n_terms in ((xc[primes_mask].sum(), primes_mask.sum()), ((xc * lam).sum(), (lam != 0).sum()),
                           ((xc * mu).sum(), (mu != 0).sum())):
            coin_worst = max(coin_worst, abs(S / n_terms ** 0.5))
    print('  coins: the largest |S/sigma| over 20 coins x 3 sums = %.2f' % coin_worst)
    print('  density of c at prime times %.5f against overall %.5f' % (bits[primes_mask].mean(), dens))
    print('K  every |S/sigma| below 3: %s (worst %.2f); above 4 (a direct handle): %s' % (worst < 3, worst, worst > 4))

    print('\nU: the velocity column c(t) XOR c(t+1) (Rule 210\'s column)')
    vel = bits[:-1] ^ bits[1:]
    v = report_shape('velocity', vel, coins)
    print('U  percentiles 5..95 for both symbols: %s' % all(5 <= v[s][1] <= 95 for s in '01'))


if __name__ == '__main__':
    main()
