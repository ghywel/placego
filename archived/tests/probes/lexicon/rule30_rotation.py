#!/usr/bin/env python3
"""rule30_rotation.py: is column 1 for trace 0101... a coding of a circle rotation? And do its spectral lines sit on
the lattice of multiples of 1/56?

RUN-ON:     cpu (pure Python 3, standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_rotation.py [T=4096] [SAMPLES=200]
            python3 tests/probes/lexicon/rule30_rotation.py 4096 200 calibrate   (the instrument's floor only)
            python3 tests/probes/lexicon/rule30_rotation.py 4096 200 domain      (the 56-step domain, a measurement)
COST:       several minutes on one core.

Where this comes from. Column 1 for 0101... has a strong spectral line at f = 0.30365 (rule30_spectrum_fine.py), and
its mirror at 1/2 - f; the mirror is the trace's half-turn per step, (-1)^t = e^{i pi t}. The owner's lead: "anytime
someone mentions rotation I think quaternions. Extending the number line with i has interesting properties." A line
at f is a point turning by f of a turn per step on the unit circle in C, z(t) = e^{2 pi i f t}. If column 1 is a
coding of that rotation, its bit at time t is decided by where z(t) is (and, through the trace, by the parity of t).
If one rotation is not enough, a second independent turn makes a torus, C x C, which the quaternions write as one
number z1 + z2 j; that is the next question, asked only if this one fails.

One arithmetic fact, noticed while setting this up: if f = 17/56 exactly, then 2f + 1/4 = 6/7 = -1/7 (mod 1), so the
7-cell ring's lines (section 8.3) would be this rotation combined with the trace's quarter-turn, and every line would
lie on multiples of 1/56.

Method.
  Phase prediction. Each sequence is cut into windows of w steps. In each window the phase phi of the line is read
  from the complex amplitude A = sum_t s(t) e^{-2 pi i f t} (s = 2 sigma - 1), and each step gets the rotation's
  position theta(t) = (f t + arg(A) / 2 pi) mod 1, in 16 bins, together with t mod 2: 32 cells. The error is the
  share of steps that the best rule "sigma = the majority value of its cell" gets wrong, pooled over windows and
  sequences. 0 means column 1 is exactly a coding of the rotation; about 0.5 means the rotation says nothing.
  Lines. The spectrum is the Wiener-Khinchin estimate of rule30_spectrum_fine.py (M = T/4 lags, Hann window), on a
  grid of step 0.0001; the 8 highest local maxima with 0 < f < 1/2.

PREDICTIONS, written 2026-10-04 before this script's first run:
  R1 (blind): at w = 64, column 1 is mostly a rotation coding: phase-prediction error <= 0.15.
  R2 (blind): the coherence decays: the error at w = 1024 exceeds the error at w = 64 by at least 0.05.
  R3 (partly informed): each of column 1's 8 highest spectral lines lies within 0.0005 of a multiple of 1/56. Not
     blind: at T = 512 four lines were already seen near the lattice (0.303, 0.197, 1/4, 2/7). The test is the fine
     position of all 8 at T = 4096.
  C1 (control): a planted rotation coding (sigma = 1 when (0.30365 t + random phase) mod 1 < 0.3, 10% of bits flipped)
     gives an error <= 0.13 at w = 64.
  C2 (control): coin flips give an error >= 0.40 at w = 64.
  CF (counterfactual): with the wrong frequency, f = 0.27, column 1's error at w = 64 is at least 0.10 above R1's.
  C3 (control): a planted 56-periodic random word, 10% of bits flipped, has its 8 highest lines within 0.0005 of
     multiples of 1/56.
REFUTED-BY: C1, C2, CF or C3 failing (the instrument); R1, R2 or R3 failing.

FIRST RUN, 2026-10-04: VOID. The instrument failed its controls: C1 (a planted rotation gave an error of 0.340), C3
and CF, and every window and frequency gave the same error, 0.314. Two bugs, both fixed before the second run: the
phase was subtracted instead of added (theta = f t - arg(A)/2 pi, which scrambles the alignment from window to window,
so only the parity carried information), and C3's planted word drew its random offset at every step instead of once
per sequence. R1 and R2 stay blind (no correct phase error had been seen). R3's spectrum code was not affected; that
run's lines were 0.3037 (17/56), 0.2500 (14/56), 0.1963 (11/56), 0.1094, 0.2857 (16/56), 0.1058, 0.3905, 0.1038, 4 of 8
on the lattice.

SECOND RUN, 2026-10-04 (bugs fixed): C2, C3 and CF passed (CF: 0.311 against 0.082). C1 FAILED its threshold by 0.009
(0.139 against 0.13): the threshold was set too tight, as the calibration mode then showed (planted codings: error 0.049
with no flips, 0.094 with 5%, 0.140 with 10%, the same at w = 64 and w = 1024). R1 HELD (0.082: about 3% of bits off
the rotation, against the floor of 0.049). R2 HELD (0.082, 0.185, 0.269 at w = 64, 256, 1024), and the planted codings
show the instrument itself does not decay with w. R3 was REFUTED (4 of 8). The four misses are the rotation's second
harmonic, broadened (0.3905 near 2f folded, and 0.1038 to 0.1094 near 2f + 1/2 folded). The domain mode: 42 of the 1,024
right halves up to 10 cells lock column 1 exactly (28 to period 4, 14 to period 14). The other 982 match themselves 56
steps later 81.3% of the time, against 39.0% and 40.0% at lags 55 and 57.
"""
import cmath, math, random, sys, pathlib

T = int(sys.argv[1]) if len(sys.argv) > 1 else 4096
SAMPLES = int(sys.argv[2]) if len(sys.argv) > 2 else 200
F = 0.30365
BINS = 16
M = T // 4

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_twosided as ts                           # noqa: E402
sys.argv = _argv
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def phase_error(seqs, f, w):
    ones = [[0] * 2 for _ in range(BINS)]
    tot = [[0] * 2 for _ in range(BINS)]
    for b in seqs:
        for a in range(0, len(b) - w + 1, w):
            A = sum((2 * b[t] - 1) * cmath.exp(-2j * math.pi * f * t) for t in range(a, a + w))
            phi = cmath.phase(A) / (2 * math.pi)
            for t in range(a, a + w):
                k = int(((f * t + phi) % 1.0) * BINS) % BINS
                ones[k][t % 2] += b[t]
                tot[k][t % 2] += 1
    wrong = sum(min(ones[k][p], tot[k][p] - ones[k][p]) for k in range(BINS) for p in range(2))
    return wrong / sum(tot[k][p] for k in range(BINS) for p in range(2))


def autocov(seqs):
    agree, ones, N = [0] * (M + 1), 0, len(seqs)
    for b in seqs:
        x = sum(v << k for k, v in enumerate(b))
        ones += bin(x).count("1")
        for j in range(M + 1):
            agree[j] += T - j - bin((x ^ (x >> j)) & ((1 << (T - j)) - 1)).count("1")
    mean = (2 * ones - N * T) / (N * T)
    return [(2 * a - N * (T - j)) / (N * (T - j)) - mean * mean for j, a in enumerate(agree)]


def lines(C, top=8, step=0.0001):
    win = [(1 + math.cos(math.pi * j / (M + 1))) / 2 * C[j] for j in range(M + 1)]
    n = int(0.5 / step)
    S = []
    for i in range(n + 1):
        f = i * step
        S.append(C[0] + 2 * sum(win[j] * math.cos(2 * math.pi * f * j) for j in range(1, M + 1)))
    peaks = [i for i in range(1, n) if S[i] > S[i - 1] and S[i] >= S[i + 1]]
    peaks.sort(key=lambda i: -S[i])
    return [(i * step, S[i]) for i in peaks[:top]]


def off56(f):
    return abs(f * 56 - round(f * 56)) / 56


def calibrate():
    """Added after the second run, where C1 missed its threshold (0.139 against 0.13): the instrument's own floor.
    Planted rotation codings at f = F with 0%, 5% and 10% of bits flipped, at w = 64 and w = 1024. A measurement, not a
    prediction."""
    rng = random.Random(9)
    for flip in (0.0, 0.05, 0.10):
        seqs = []
        for _ in range(40):
            ph = rng.random()
            seqs.append([int(((F * t + ph) % 1.0) < 0.3) ^ (rng.random() < flip) for t in range(T)])
        print(f"   calibration: planted rotation coding, {flip:.0%} flipped: error at w = 64 "
              f"{phase_error(seqs, F, 64):.3f}, at w = 1024 {phase_error(seqs, F, 1024):.3f}", flush=True)


def domain(steps=2000, lag=56, wmax=10):
    """A measurement. For every right half up to `wmax` cells: is column 1 eventually exactly periodic with a period
    dividing 56 (and with which minimal period), and, for the others, how often does column i (1..6) equal itself 56
    steps later? Lags 55 and 57 are the control (off the period)."""
    locked, share, n_free = {}, [0.0] * 7, 0
    off = {55: 0.0, 57: 0.0}
    for R in range(1 << wmax):
        mask = (1 << (R.bit_length() + steps + 3)) - 1
        row, cols = R << 1, [[] for _ in range(7)]
        for t in range(steps):
            for i in range(1, 7):
                cols[i].append((row >> i) & 1)
            row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
        c = cols[1]
        last_bad = max([t for t in range(steps - lag) if c[t] != c[t + lag]], default=-1)
        if last_bad < steps - lag - 400:
            tail = c[last_bad + 1:]
            per = next(q for q in range(1, lag + 1) if all(tail[t] == tail[t + q] for t in range(len(tail) - q)))
            locked[per] = locked.get(per, 0) + 1
            continue
        n_free += 1
        for i in range(1, 7):
            share[i] += sum(cols[i][t] == cols[i][t + lag] for t in range(steps - lag)) / (steps - lag)
        for q in off:
            off[q] += sum(c[t] == c[t + q] for t in range(steps - q)) / (steps - q)
    print(f"   domain, every right half up to {wmax} cells, {steps} steps:")
    print(f"      column 1 eventually exactly periodic (period dividing {lag}), by minimal period: {dict(sorted(locked.items()))}"
          f" of {1 << wmax}")
    print(f"      the other {n_free}: column i equal to itself {lag} steps later: "
          + ", ".join(f"col {i}: {share[i] / n_free:.3f}" for i in range(1, 7)))
    print(f"      control, column 1 at lags 55 and 57: {off[55] / n_free:.3f}, {off[57] / n_free:.3f}", flush=True)


def main():
    if len(sys.argv) > 3 and sys.argv[3] == "calibrate":
        calibrate()
        return
    if len(sys.argv) > 3 and sys.argv[3] == "domain":
        domain()
        return
    rng = random.Random(7)
    planted = []
    for _ in range(40):
        ph = rng.random()
        planted.append([int(((F * t + ph) % 1.0) < 0.3) ^ (rng.random() < 0.1) for t in range(T)])
    e = phase_error(planted, F, 64)
    report("C1 a planted rotation coding is predicted from its phase", e <= 0.13, f"error {e:.3f}")
    coin = [[rng.getrandbits(1) for _ in range(T)] for _ in range(40)]
    e = phase_error(coin, F, 64)
    report("C2 coin flips are not", e >= 0.40, f"error {e:.3f}")
    word = [rng.getrandbits(1) for _ in range(56)]
    p56 = []
    for _ in range(40):
        off = rng.randrange(56)
        p56.append([word[(t + off) % 56] ^ (rng.random() < 0.1) for t in range(T)])
    ln = lines(autocov(p56))
    report("C3 a planted 56-periodic word: its 8 highest lines on multiples of 1/56",
           all(off56(f) <= 0.0005 for f, _ in ln), "largest offset " + f"{max(off56(f) for f, _ in ln):.5f}")

    rng = random.Random(5)
    seqs = [ts.column1(rng.getrandbits(14), (0, 1), T) for _ in range(SAMPLES)]
    errs = {w: phase_error(seqs, F, w) for w in (64, 256, 1024)}
    print("\n   column 1, trace 0101...: phase-prediction error by window: "
          + ", ".join(f"w = {w}: {e:.3f}" for w, e in errs.items()))
    wrongf = phase_error(seqs, 0.27, 64)
    report("CF the wrong frequency (0.27) predicts column 1 much worse", wrongf >= errs[64] + 0.10,
           f"error {wrongf:.3f} against {errs[64]:.3f}")
    verdict("R1 at w = 64 column 1 is mostly a rotation coding (error <= 0.15)", errs[64] <= 0.15, f"{errs[64]:.3f}")
    verdict("R2 the coherence decays (error at w = 1024 at least 0.05 above w = 64)", errs[1024] >= errs[64] + 0.05,
            f"{errs[1024]:.3f} against {errs[64]:.3f}")
    ln = lines(autocov(seqs))
    print("   column 1's 8 highest lines: " + "; ".join(
        f"{f:.4f} ({round(f * 56)}/56, off {off56(f):.4f}, S {s:.1f})" for f, s in ln))
    verdict("R3 all 8 highest lines within 0.0005 of a multiple of 1/56", all(off56(f) <= 0.0005 for f, _ in ln),
            f"{sum(off56(f) <= 0.0005 for f, _ in ln)} of 8")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
