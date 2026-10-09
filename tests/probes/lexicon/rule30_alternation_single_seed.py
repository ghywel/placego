#!/usr/bin/env python3
"""rule30_alternation_single_seed.py: the single seed against CL078's fair-row null for window alternation. Cloud's
offered run (CL078, item 2), taken by Local (chat L414), with Cloud's predictions pushed in CL078 before any run and
Local's operational choices and descriptive items pushed here before the run.

RUN-ON:     cpu (Python 3, numpy); under a minute
COMMAND:    python3 tests/probes/lexicon/rule30_alternation_single_seed.py

The null (Cloud's `rule30_cloud_alternation.py`, RULE30-PRIZE.md §8.70 third addendum, G.GPT255): on fair rows the
correlation of a fixed 63-cell window's density k rows apart is rho_k (63 - k)/63, with rho_1 .. rho_8 = -1/2, 1/4,
-1/4, 5/32, -5/64, 77/1024, -141/2048, 39/512; a window flips between denser and sparser than half at N consecutive
steps with frequencies 0.668, 0.459, 0.328, 0.236, 0.168, 0.120, 0.087, 0.063 (N = 1 .. 8; Cloud's Monte Carlo).

The single seed: one black cell at x = 0, row 0, Rule 30 on the line (exact, bit-sliced). Operational choices (Local's,
fixed before the run): windows are the fixed tiles [63j, 63j + 62]; a (row, window) sample uses rows t .. t + k (or
t .. t + N for a streak) of one window, and is counted when the window lies inside the named x-range at its first row
t. Rows t run over [2^12, 2^13). The centring is the null's own (mean 31.5, variance 63/4, as in Cloud's Monte Carlo),
not the sample's. Batches are 64 consecutive first rows (64 batches); a batch's statistic pools its samples, and the
standard error is the batch values' standard deviation over 8.

PREDICTIONS (Cloud's, CL078, pushed before any run):
  AL1: core windows (x in [-0.1t, 0.8t]): rho_1 .. rho_6 each within 3 batch standard errors of rho_k (63 - k)/63.
  AL2: core windows: the flip-streak fractions for N = 1 .. 8 each within 3 batch standard errors of the table.
  AL3 (control): windows inside the ordered left band (x < -0.4t, and inside the light cone x >= -t): some k <= 6
       departs from rho_k (63 - k)/63 by more than 5 standard errors.
  Counterfactual (Cloud's): AL1 failing in the core would be the single seed's first departure from fair rows in a
  two-cell linear statistic; AL3 not departing would mean the statistic cannot see the band.
Local's additions, before the run:
  AL2-F (fresh null, registered because the table is itself a Monte Carlo quoted to three places): the streak
       fractions on 2^12 + 9 rows evolved from one random fair row of 2^18 cells (seed 414; fair rows are stationary
       under Rule 30, so the row index does not matter), the same tiles and 64-row batches; AL2-F
       reports each N's z-score against this fresh null as well as against the table. The verdict on AL2 is the
       table's, as Cloud registered it.
  D1 (descriptive): rho_7, rho_8 in the core against the null.
  D2 (descriptive): the AL1 z-scores in eight x/t bins from -1 to 1 (where along the row the statistic departs).
OUTCOME, 2026-10-09 14:22 BST (M5, 1.2 s, run at commit 46696d3f): AL1 HELD, AL2 HELD, AL3 HELD.
  AL1, core (355,384 samples): rho_1 .. rho_6 = -0.4905, +0.2418, -0.2374, +0.1458, -0.0720, +0.0680 (batch standard
    errors 0.002), |z| <= 0.66 against rho_k (63 - k)/63. D1: rho_7, rho_8 at z -0.41, +0.85.
  AL2, core: streak fractions 0.6670, 0.4575, 0.3268, 0.2345, 0.1671, 0.1195, 0.0860, 0.0625 for N = 1 .. 8, z -0.44 to
    -1.18 against the table. AL2-F: the fresh null gives 0.6678 .. 0.0625, z -0.05 to -0.78. The streaks are nested
    (an N + 1 run contains an N run), so the common sign is one fluctuation, not eight.
  AL3, band (x in [-t, -0.4t], 235,664 samples): rho_1 -0.4558 (z +20.5), rho_2 +0.1957 (z -21.3); every lag's
    alternation is weaker than the null's, and five of six lags depart by more than 11 standard errors.
  D2: the departure is confined to x/t < -1/4 (z up to 36 in [-1, -0.75], up to 7.2 in [-0.5, -0.25]); the four bins
    from -0.25 to 1 have |z| <= 1.9 at every lag.
  Exploratory, after the run (no predictions): bins of 0.03 from -0.5 to -0.2. At rows 2^13 .. 2^14 the departure
    reaches |z| 4.1 to 5.1 in [-0.38, -0.26] and falls to 1.8 and 1.1 in [-0.26, -0.20]. At rows 2^12 .. 2^13 the thin
    bins are too small to show it (|z| <= 3.1). The edge sits at the left front's measured -0.245t (RULE30-PRIZE.md
    §8.74: the band's boundary leaves the edge at 0.755 cells a row).
  So in this two-cell linear statistic the single seed's rows are fair-row-like from the left front to the right
    edge, and the ordered band is visible up to the front. This is evidence on one seed over 2^12 .. 2^14 rows, not a
    law.
"""
import numpy as np

W, T0, T1, BATCH = 63, 1 << 12, 1 << 13, 64
KMAX, NMAX = 8, 8
RHO = [-1 / 2, 1 / 4, -1 / 4, 5 / 32, -5 / 64, 77 / 1024, -141 / 2048, 39 / 512]
STREAK = [0.668, 0.459, 0.328, 0.236, 0.168, 0.120, 0.087, 0.063]
MEAN, VAR = W / 2, W / 4


def evolve_densities(row0, nrows, off, width):
    """Window densities dens[t, j] for tiles [63 (j + j0), ...]; row0 is a big integer, bit x + off is cell x."""
    j0 = -(off // W)
    nwin = (width - off) // W - j0
    mask = (1 << width) - 1
    V, dens = row0, np.zeros((nrows, nwin), dtype=np.int16)
    nbytes = (width + 7) // 8
    for t in range(nrows):
        bits = np.unpackbits(np.frombuffer(V.to_bytes(nbytes, 'little'), dtype=np.uint8), bitorder='little')
        start = off + W * j0
        dens[t] = bits[start: start + W * nwin].reshape(nwin, W).sum(axis=1)
        V = ((V << 1) ^ (V | (V >> 1))) & mask
    return dens, j0


def samples(dens, j0, lo, hi):
    """For first rows t in [T0, T1): a boolean array over (t, j), true when tile j lies in [lo t, hi t] at row t."""
    t = np.arange(T0, T1)[:, None]
    x0 = (np.arange(dens.shape[1]) + j0)[None, :] * W
    return (x0 >= np.ceil(lo * t)) & (x0 + W - 1 <= np.floor(hi * t))


def batch_stat(values, ok):
    """values, ok: arrays over (t, j) for t in [T0, T1); returns the per-batch pooled means."""
    out = []
    for b in range(0, T1 - T0, BATCH):
        v, m = values[b: b + BATCH], ok[b: b + BATCH]
        out.append(v[m].mean())
    return np.array(out)


def stats(dens, j0, lo, hi):
    side = dens > MEAN
    flips = side[1:] != side[:-1]                                   # flips[t] is the step t -> t + 1
    ok = samples(dens, j0, lo, hi)
    res = {'n': int(ok.sum())}
    z = (dens - MEAN) / np.sqrt(VAR)
    for k in range(1, KMAX + 1):
        bs = batch_stat(z[T0: T1] * z[T0 + k: T1 + k], ok)
        res['rho%d' % k] = (bs.mean(), bs.std(ddof=1) / np.sqrt(len(bs)), RHO[k - 1] * (W - k) / W)
    for N in range(1, NMAX + 1):
        run = np.ones((T1 - T0, dens.shape[1]), dtype=bool)
        for u in range(N):
            run &= flips[T0 + u: T1 + u]
        bs = batch_stat(run.astype(float), ok)
        res['N%d' % N] = (bs.mean(), bs.std(ddof=1) / np.sqrt(len(bs)), STREAK[N - 1])
    return res


def main():
    nrows = T1 + max(KMAX, NMAX) + 1
    off = nrows + W + 1
    width = 2 * off + 1
    dens, j0 = evolve_densities(1 << off, nrows, off, width)
    core = stats(dens, j0, -0.1, 0.8)
    band = stats(dens, j0, -1.0, -0.4)
    # the fresh fair-row null: a random row stays fair under Rule 30 on the line; 2^18 cells, 2^12 + 9 rows
    rng = np.random.default_rng(414)
    frows = T1 - T0 + max(KMAX, NMAX) + 1
    fw = (1 << 18) + 2 * frows
    R = int.from_bytes(rng.integers(0, 256, (fw + 7) // 8, dtype=np.uint8).tobytes(), 'little') & ((1 << fw) - 1)
    fdens, fj0 = evolve_densities(R, frows, fw // 2, fw)
    # tiles inside the cells the truncated ends cannot reach in frows steps
    lo_x, hi_x = -(fw // 2) + frows + 1, fw - fw // 2 - frows - 2
    keep = np.zeros(fdens.shape[1], dtype=bool)
    for j in range(fdens.shape[1]):
        x0 = (j + fj0) * W
        keep[j] = x0 >= lo_x and x0 + W - 1 <= hi_x
    fdens = fdens[:, keep]
    fside = fdens > MEAN
    fflips = fside[1:] != fside[:-1]
    fresh = []
    for N in range(1, NMAX + 1):
        run = np.ones((T1 - T0, fdens.shape[1]), dtype=bool)
        for u in range(N):
            run &= fflips[u: T1 - T0 + u]
        bs = np.array([run[b: b + BATCH].mean() for b in range(0, T1 - T0, BATCH)])
        fresh.append((bs.mean(), bs.std(ddof=1) / np.sqrt(len(bs))))

    def zline(res, key):
        m, se, ref = res[key]
        return m, se, ref, (m - ref) / se

    print('core samples %d; band samples %d; fresh-null tiles %d' % (core['n'], band['n'], fdens.shape[1]))
    al1 = True
    for k in range(1, 7):
        m, se, ref, z = zline(core, 'rho%d' % k)
        al1 &= abs(z) <= 3
        print('core rho_%d %+.4f +- %.4f, null %+.4f, z %+.2f' % (k, m, se, ref, z))
    print('AL1', 'HELD' if al1 else 'REFUTED')
    al2 = True
    for N in range(1, NMAX + 1):
        m, se, ref, z = zline(core, 'N%d' % N)
        fm, fse = fresh[N - 1]
        al2 &= abs(z) <= 3
        print('core N=%d %.4f +- %.4f, table %.3f, z %+.2f; fresh null %.4f +- %.4f, z %+.2f' % (
            N, m, se, ref, z, fm, fse, (m - fm) / np.hypot(se, fse)))
    print('AL2', 'HELD' if al2 else 'REFUTED')
    al3 = False
    for k in range(1, 7):
        m, se, ref, z = zline(band, 'rho%d' % k)
        al3 |= abs(z) > 5
        print('band rho_%d %+.4f +- %.4f, null %+.4f, z %+.2f' % (k, m, se, ref, z))
    print('AL3', 'HELD' if al3 else 'REFUTED')
    for k in (7, 8):
        m, se, ref, z = zline(core, 'rho%d' % k)
        print('D1 core rho_%d %+.4f +- %.4f, null %+.4f, z %+.2f' % (k, m, se, ref, z))
    for b in range(8):
        lo, hi = -1 + 0.25 * b, -0.75 + 0.25 * b
        r = stats(dens, j0, lo, hi)
        zs = ' '.join('%+.1f' % zline(r, 'rho%d' % k)[3] for k in range(1, 7))
        print('D2 x/t in [%+.2f, %+.2f]: samples %d, z(rho_1 .. rho_6) %s' % (lo, hi, r['n'], zs))
    print('COMPLETE')


if __name__ == '__main__':
    main()
