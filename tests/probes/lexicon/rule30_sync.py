#!/usr/bin/env python3
"""rule30_sync.py: are the wheel's slips synchronised in time across right halves? The untested hint of section
8.10 (the window-by-window mean speed swings far more than independent right halves would give), a small item on
PERIOD-TWO.md's board. (Local, 2026-10-06; section 8.60.)

RUN-ON:     cpu, one core (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_sync.py [W=12] [T=4096]
COST:       a minute.

METHOD. As in rule30_wheelspeed.py: for every unlocked right half up to W cells, column 1 over T steps is cut into
windows of 56 steps; a window is exact when column 1 equals the wheel U at some phase, and a slip window otherwise.
Let s_h(k) = 1 when half h slips at window k, and N(k) = sum over halves. If halves slipped independently of one
another (whatever each one's own rate), N(k) would be a sum of independent indicators and its Fano factor
Var_k N / Mean_k N over a range of windows would be at most 1. A Fano factor well above 1 means the halves tend
to slip at the same windows: synchrony in time, whether from a common clock (all halves start at time 0 against
the same wall, so the wheel's formation is a shared event) or from anything else. The control: each half's slip
series is circularly shifted by its own random offset within the range, which keeps every half's rate and
pattern and destroys only the alignment across halves. The same is done for the mean excess speed v(k) of
section 8.10 (the summed kicks per window, averaged over halves): its spread over windows, real against shifted.
Three ranges: early (windows 2 to 11, the formation), middle (12 to 39), late (40 to 72).

SEEN BEFORE these predictions: section 8.10's run (the swings of v(k), from -0.21 to +0.15 notches per window;
+-0.04 was the back-of-envelope expectation for independent halves). No Fano factor has been computed.

PREDICTIONS, written 2026-10-06 before this script's first run.
  S0 (control, must hold): every phase change between exact windows is an even time shift (as in rule30_wheelspeed).
  S1 (blind): the halves slip together early: the Fano factor of N(k) over the early range is at least 3.
  S2 (blind): the synchrony fades: the Fano factor over the late range is at most 1.5.
  S3 (blind): the spread of v(k) over the early range is at least twice the shifted control's; over the late
      range it is less than twice the control's.
  CF  (counterfactual, must fail): the shifted control shows synchrony. It must not: its Fano factor lies in
      [0.8, 1.25] in every range.
REFUTED-BY: S0 or CF failing (the instrument); S1 to S3 the other way. If S2 is refuted the synchrony is not the
  formation's and is worth a section of its own.

OUTCOME: (to be recorded after the first run)
"""
import math, pathlib, random, statistics, sys

_nums = [a for a in sys.argv[1:]]
W = int(_nums[0]) if len(_nums) > 0 else 12
T = int(_nums[1]) if len(_nums) > 1 else 4096
P = 56
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_wheel_left as wl                         # noqa: E402
sys.argv = _argv
U = [int(c) for c in wl.U]
ROT = {tuple(U[(t - d) % P] for t in range(P)): d for d in range(P)}
FAILS = 0
RANGES = {"early": (2, 12), "middle": (12, 40), "late": (40, 73)}


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def column1(R, n):
    mask = (1 << (R.bit_length() + n + 3)) - 1
    row, out = R << 1, []
    for t in range(n):
        out.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
    return out


def fano(counts):
    m = statistics.fmean(counts)
    return statistics.pvariance(counts) / m if m > 0 else float("nan")


def main():
    nwin = T // P
    slips, kicks = [], []                                  # per half: slip indicator per window; kick per window
    odd = 0
    for R in range(1 << W):
        c = column1(R, T)
        last_bad = max([t for t in range(T - P) if c[t] != c[t + P]], default=-1)
        if last_bad < T - P - 400:
            continue                                       # locked
        ph = [ROT.get(tuple(c[k * P:(k + 1) * P])) for k in range(nwin)]
        slips.append([1 if d is None else 0 for d in ph])
        ex = [(k, d) for k, d in enumerate(ph) if d is not None]
        kick = [0.0] * nwin
        for (k, d), (k2, d2) in zip(ex, ex[1:]):
            delta = (d2 - d) % P
            odd += delta % 2
            nn = (-17 * delta) % P
            nn = nn - P if nn > P // 2 else nn
            nn //= 2
            for j in range(k, k2):
                kick[j] += nn / (k2 - k)
        kicks.append(kick)
    H = len(slips)
    report("S0 every phase change between exact windows is an even time shift", odd == 0,
           f"{odd} odd shifts; {H} unlocked halves, {nwin} windows")
    rng = random.Random(30)
    F, Fc, spread, spreadc = {}, {}, {}, {}
    for name, (a, b) in RANGES.items():
        n = b - a
        N = [sum(s[k] for s in slips) for k in range(a, b)]
        F[name] = fano(N)
        v = [sum(kk[k] for kk in kicks) / H for k in range(a, b)]
        spread[name] = statistics.pstdev(v)
        fc, sc = [], []
        for _ in range(5):                                  # five shifted controls, averaged
            Nc, vc = [0] * n, [0.0] * n
            for s, kk in zip(slips, kicks):
                off = rng.randrange(n)
                for j in range(n):
                    Nc[j] += s[a + (j + off) % n]
                    vc[j] += kk[a + (j + off) % n] / H
            fc.append(fano(Nc)); sc.append(statistics.pstdev(vc))
        Fc[name] = statistics.fmean(fc); spreadc[name] = statistics.fmean(sc)
        print(f"   {name} (windows {a}-{b - 1}): slips per window {statistics.fmean(N):.1f} of {H}; Fano {F[name]:.2f} "
              f"(shifted {Fc[name]:.2f}); spread of v {spread[name]:.4f} (shifted {spreadc[name]:.4f})", flush=True)
    verdict("S1 Fano factor of the slip counts over the early range at least 3", F["early"] >= 3, f"{F['early']:.2f}")
    verdict("S2 Fano factor over the late range at most 1.5", F["late"] <= 1.5, f"{F['late']:.2f}")
    verdict("S3 the spread of v(k): at least twice the control's early, less than twice late",
            spread["early"] >= 2 * spreadc["early"] and spread["late"] < 2 * spreadc["late"],
            f"early ratio {spread['early'] / spreadc['early']:.2f}, late ratio {spread['late'] / spreadc['late']:.2f}")
    report("CF  the shifted control shows no synchrony: Fano in [0.8, 1.25] in every range",
           all(0.8 <= x <= 1.25 for x in Fc.values()), ", ".join(f"{k} {x:.2f}" for k, x in Fc.items()))
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
