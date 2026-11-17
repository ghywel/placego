#!/usr/bin/env python3
"""rule30_uniform.py: is "total width plus a constant" one law for every centre word? (lead 1, uniform over periods)

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_uniform.py [WMAX=16]
COST:       about fifteen minutes on one core.

Background (RULE30-PRIZE.md sections 8.24, 8.40, 8.41). rule30_complement.py measured, for the centre word 0101...,
how long a finite seed keeps its centre column on the word. Take a right half R of exact width W and its forced left
half (rule30_periodic.forced_left), and cut the left half at depth d. That makes a seed of w = d + 1 + W cells whose
centre column follows the word until time P, the depth of the first 1 beyond the cut. The excess E = P - w,
maximised over cuts, is (the longest zero run of the forced left half) - W. For 0101 it never exceeded +9, at any
width up to 32 cells.
If every condition at the wall costs one bit, a seed's w bits buy about w steps whatever the word, so the largest
excess should stay a small constant for every word. That is a uniform law, the shape the prize table says would win
(a uniform argument over all periods). Any finite bound proves Problem 1 for that word, since an eventually
periodic centre column would need a seed that keeps the word for ever.

PREDICTIONS, written 2026-10-05 before this script's first run (widths W = 0 .. 16, cuts to depth 126):
  UW0 (control, must hold): for 01 the largest excess by exact width reproduces rule30_complement.py's outcome:
      +5, +8, +7, +6, +5, +9, +8, +7, +6, +5, +4, +3, +2, +1, +3, +2, +1 at W = 0 .. 16.
  UW1 (blind; one law for every word): for each two-colour word of period up to 4 (001, 011, 0001, 0011, 0111), the
      largest excess at every width is at most +12.
  UW2 (blind; wider is worse): for each two-colour word, the largest excess over widths 12 .. 16 is below the
      largest over widths 0 .. 8. The bits of a wide right half arrive too late (section 8.17).
  UW3 (blind; the one-colour walls, from Condrey's explicit fibres): for w = 1 the largest excess is at most +2 at
      every width; for w = 0, over nonzero right halves, at most +2 at every width from 1 to 16.
  UW4 (random-chaos: does the law need a period?): a random wall (4096 random bits) obeys UW1's +12 at every width.
REFUTED-BY: UW0 failing (the instrument); UW1 to UW4 failing.

OUTCOME, 2026-10-05 (the first run, horizon 126, about 15 minutes):
  UW0 PASSED: 01 reproduces rule30_complement.py at every width 0 .. 16.
  UW1 HELD: the largest excess is +10 (001, at width 1), +9 (011), +7 (0001, 0011, 0111); 01 has +9.
  UW2 REFUTED by 0011 alone (+5 at widths 12 .. 16 against +4 at 0 .. 8; its +7 is at width 10). For the other
     four words the wide right halves do worse (001: +1 vs +10, 011: +7 vs +9, 0001: +2 vs +7, 0111: +3 vs +7).
  UW3 HELD, exactly: for w = 1 the excess is 1 - W at every width (the stripes: no zero run longer than 1); for w = 0
     it is 0 at W = 1 and -1 from W = 2 (Condrey's alternating tail).
  UW4 HELD: the random wall's largest excess is +6.
  Many entries had a run that reached depth 126. The addendum (mode deep) recomputed those right halves to depth
  320. The maxima moved by at most one (001 at widths 12 .. 16, 0011 at 15 and 16, and the random wall at 16, from -3
  to +1), and no verdict changed.
  A second check, after both (post hoc): 01 and the random wall recomputed at depth 320, with every run that reached
  320 followed to 640. Among those runs the largest excess is +4 for 01, but +10 for the random wall's empty right
  half (W = 0), from a run of 10 zeros at depth 562 (against +4 for W = 0 to depth 126). So the excess depends on how
  deep the cuts may go. That is the coin model's prediction: the longest zero run up to depth K grows like log2 K,
  so the law would be "total width plus a logarithm", not plus a constant. Mode horizon tests that.

MODE horizon. The largest excess over right halves of widths 0 .. 10, with cuts to depth K = 64, 128, 256 and 512.
PREDICTIONS for horizon, written 2026-10-05 after the outcome above and before horizon's first run. Seen: the
excesses at K = 126 for every width, the deep addendum's values to 320 for the runs that reached 126, and the
640-check above (01 and the random wall only, runs that reached 320).
  UH1 (blind; Cramer's shape): for every two-colour word and the random wall, the largest excess over widths 0 .. 10
      at K = 512 exceeds the value at K = 64 by 2 to 5: about one step per doubling of the horizon.
  UH2 (blind; the one-colour walls): for w = 0 (nonzero right halves) and w = 1 it does not grow at all.

OUTCOME of horizon, 2026-10-05 (4 seconds): largest excess over widths 0 .. 10 at K = 64, 128, 256, 512:
  01 +9 +9 +9 +9; 001 +10 +10 +10 +10; 011 +9 +9 +9 +10; 0001 +5 +7 +8 +10; 0011 +4 +7 +7 +7; 0111 +6 +7 +7 +7;
  random +5 +6 +9 +9; 1 +1 throughout; 0 +0 throughout.
  UH1 REFUTED: the random wall grows (+4), as a coin would, and so do 0001 (+5) and 0011 (+3); but 01 and 001 do not
     grow at all, and 011 and 0111 by one. For those words the champions sit at shallow depth, and looking eight
     times deeper finds no longer run.
  UH2 HELD.

MODE windows. If the periodic wall holds the deep zero runs down, that is a property of periodic words that random
words lack, and the kind of property a proof could use. The test: the longest zero run of the forced row 0 inside
each depth window [K/2, K), maximised over every right half of width up to 10, for K = 128 .. 2048.
PREDICTIONS for windows, written 2026-10-05 after horizon's outcome and before windows' first run. Seen: everything
above (no window has been computed).
  UV1 (blind; structure): for 01 the longest run in the window does not grow: at K = 2048 it is at most its value at
      K = 128 plus 1. Under the coin model, with 16 times as many cells, it would grow by about 4.
  UV2 (blind; the control the other way): for the random wall it grows by at least 2 from K = 128 to K = 2048.
  UV3 (blind): 001 behaves like 01 (UV1's bound), and 0001 like the random wall (UV2's growth).

OUTCOME of windows, 2026-10-05 (11 seconds): the longest zero run in [K/2, K], over every right half of width up to
10, at K = 128, 256, 512, 1024, 2048: 01 14 14 15 17 21; 001 11 13 15 16 19; 0001 13 13 15 12 18; random 13 16 15
17 17.
  UV1 REFUTED: for 01 the deep runs grow, by 7, faster than the random wall's 4. UV2 HELD. UV3 REFUTED (001 grows by
     8).
  So the periodic wall does not hold the deep runs down. Horizon's flat excess for 01 and 001 came from the
  definition: the excess is (run - width), and a small right half's champion at shallow depth (01: width 5, depth 21)
  stays ahead of the longer deep runs, which need wider right halves. With coin cells, the longest run among N
  sequences over n cells is about log2(n N): for n = 1024 and N = 2047 that is 21, as measured for 01 at K = 2048.
  The law across words is the coin's, total width plus a logarithm of the depth. The hypothesis raised after horizon
  (periodicity suppresses deep zero runs) was refuted the same hour.
"""
import pathlib, random, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
WMAX = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 16
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
sys.argv = _argv
K = 126
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def excess_by_width(tau, skip_zero=False):
    out = {}
    for W in range(0, WMAX + 1):
        lo, hi = (0, 1) if W == 0 else (1 << (W - 1), 1 << W)
        best, arg, capped = None, None, False
        for R in range(lo, hi):
            if skip_zero and R == 0:
                continue
            L = r30.forced_left(R, tau, K)
            run, longest, start = 0, 0, 1
            for k in range(1, K + 1):
                if L[k - 1]:
                    run = 0
                else:
                    run += 1
                    if run > longest:
                        longest, start = run, k - run + 1
            capped |= start + longest - 1 == K
            e = longest - W
            if best is None or e > best:
                best, arg = e, (R, start, longest)
        if best is not None:
            out[W] = (best, arg, capped)
    return out


# ADDENDUM, written 2026-10-06 before the run (python3 rule30_uniform.py slow [WMAX=12]): the slow walls of section 8.63
# on the B side. Does "total width plus a constant" hold next to 0^a 1^a for a = 4, 8, 16, where a real right half's
# column 1 is latched (monotone through each white stretch) and the black stretches force the checkerboard?
#   US0 (control, must hold): the 01 wall reproduces rule30_complement.py's excesses for W <= WMAX (the UW0 list), and
#       the same list is NOT reproduced when the wall's phase is shifted by one step (the instrument sees the wall).
#   US1 (blind): the largest excess by width stays at most +12 for each slow wall, as for every two-colour word (UW1).
#   US2 (blind): the largest excess does not grow with a: a = 16's is at most a = 4's plus 2.
#   US3 (blind): no run reaches depth 126 (no capped width) for any slow wall at W <= WMAX.
# REFUTED-BY: US0 failing (the instrument); US1 to US3 the other way (a slow wall that lets a finite seed keep its
#   centre far beyond its width would be the first wall to break the law of section 8.42).
# OUTCOME of the slow run, 2026-10-06 (WMAX stayed at its default 16, the mode word having taken the argument's place; 18 s):
# US0 PASSED. Largest excess by width: 0^4 1^4: +5, +4, +4, +4, +6, +5, +4, +3, then +2 .. +9 .. +5 (W = 8 to 16); 0^8 1^8:
# +7, +5, +4, +3, +2, +1, 0, -1, +1, 0, -1, ..., -7; 0^16 1^16: +15 at W = 0 (the empty right half), then +6, +5, ..., -1, +1.
# US1 REFUTED by the empty right half alone (a = 16, W = 0: +15; every W >= 1 is within +9). US2 REFUTED by the same
# value. US3 REFUTED by the flag's semantics: it marks any right half whose longest run ends at the window's edge,
# which a short run at depth 124 does; the champion runs at width 8 next to 0^4 1^4 are 10 cells (K = 126) and 18
# cells (K = 400 and 1200) from depth 215, reaching no edge. So no slow wall breaks the law: for real right halves the
# excess is at most +9 (a = 4), +7 (a = 8) and +6 (a = 16, W >= 1), and it falls below zero for wide seeds at a = 8
# and 16, where the latch leaves the right half little to say.


def slow():
    want = [5, 8, 7, 6, 5, 9, 8, 7, 6, 5, 4, 3, 2, 1, 3, 2, 1]
    tau01 = [t % 2 for t in range(K + 2)]
    res01 = excess_by_width(tau01)
    shifted = excess_by_width([(t + 1) % 2 for t in range(K + 2)])
    got = [res01[W][0] for W in range(min(17, WMAX + 1))]
    report("US0 the 01 wall reproduces the recorded excesses, and the phase-shifted wall does not",
           got == want[:len(got)] and [shifted[W][0] for W in range(len(got))] != want[:len(got)], f"{got}")
    res = {}
    for a in (4, 8, 16):
        w = [0] * a + [1] * a
        tau = [w[t % len(w)] for t in range(K + 2)]
        res[a] = excess_by_width(tau)
        print(f"   0^{a} 1^{a}: largest excess by width: " + " ".join(f"{W}:{v[0]:+d}{'*' if v[2] else ''}" for W, v in res[a].items()),
              flush=True)
    big = {a: max(v[0] for v in res[a].values()) for a in res}
    verdict("US1 the largest excess is at most +12 for each slow wall", all(b <= 12 for b in big.values()),
            ", ".join(f"a = {a}: {b:+d}" for a, b in big.items()))
    verdict("US2 the largest excess does not grow with a (a = 16 at most a = 4 plus 2)", big[16] <= big[4] + 2)
    verdict("US3 no run reaches depth 126", not any(v[2] for a in res for v in res[a].values()))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def main():
    rng = random.Random(4096)
    words = {"01": [0, 1], "001": [0, 0, 1], "011": [0, 1, 1], "0001": [0, 0, 0, 1], "0011": [0, 0, 1, 1],
             "0111": [0, 1, 1, 1], "1": [1], "0": [0], "random": [rng.getrandbits(1) for _ in range(4096)]}
    res = {}
    for n, w in words.items():
        tau = [w[t % len(w)] for t in range(K + 2)]
        res[n] = excess_by_width(tau, skip_zero=(n == "0"))
        print(f"   {n:6s}: largest excess by width: "
              + " ".join(f"{W}:{v[0]:+d}{'*' if v[2] else ''}" for W, v in res[n].items()), flush=True)
        top = max(res[n].values(), key=lambda v: v[0])
        print(f"           champion: R = {top[1][0]}, a run of {top[1][2]} zeros from depth {top[1][1]}", flush=True)
    want = [5, 8, 7, 6, 5, 9, 8, 7, 6, 5, 4, 3, 2, 1, 3, 2, 1]
    report("UW0 01 reproduces rule30_complement.py", [res["01"][W][0] for W in range(min(17, WMAX + 1))]
           == want[:min(17, WMAX + 1)])
    two = ["001", "011", "0001", "0011", "0111"]
    capped = [n for n in res if any(v[2] for v in res[n].values())]
    print(f"   (* = the run reached depth 126, so the excess is a lower bound; words affected: {capped or 'none'})")
    verdict("UW1 the largest excess is at most +12 for every two-colour word",
            all(v[0] <= 12 for n in two for v in res[n].values()),
            ", ".join(f"{n}: {max(v[0] for v in res[n].values()):+d}" for n in two))
    late = {n: max(res[n][W][0] for W in range(12, WMAX + 1)) for n in two}
    early = {n: max(res[n][W][0] for W in range(0, 9)) for n in two}
    verdict("UW2 wider is worse: the best over widths 12 .. 16 is below the best over 0 .. 8",
            all(late[n] < early[n] for n in two), ", ".join(f"{n}: {late[n]:+d} vs {early[n]:+d}" for n in two))
    verdict("UW3 the one-colour walls stay within +2",
            all(v[0] <= 2 for v in res["1"].values()) and all(v[0] <= 2 for W, v in res["0"].items() if W >= 1),
            f"1: {max(v[0] for v in res['1'].values()):+d}, 0: "
            f"{max(v[0] for W, v in res['0'].items() if W >= 1):+d}")
    verdict("UW4 the random wall stays within +12", all(v[0] <= 12 for v in res["random"].values()),
            f"largest {max(v[0] for v in res['random'].values()):+d}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def longest_run(L, K):
    run, longest, start = 0, 0, 1
    for k in range(1, K + 1):
        if L[k - 1]:
            run = 0
        else:
            run += 1
            if run > longest:
                longest, start = run, k - run + 1
    return longest, start


def deep(K2=320):
    """The addendum: every right half whose zero run reaches depth 126 is recomputed to depth K2."""
    rng = random.Random(4096)
    words = {"01": [0, 1], "001": [0, 0, 1], "011": [0, 1, 1], "0001": [0, 0, 0, 1], "0011": [0, 0, 1, 1],
             "0111": [0, 1, 1, 1], "random": [rng.getrandbits(1) for _ in range(4096)]}
    for n, w in words.items():
        tau = [w[t % len(w)] for t in range(K2 + 2)]
        best, still = {}, 0
        for W in range(0, WMAX + 1):
            lo, hi = (0, 1) if W == 0 else (1 << (W - 1), 1 << W)
            e_best = None
            for R in range(lo, hi):
                lg, st = longest_run(r30.forced_left(R, tau[:K + 2], K), K)
                if st + lg - 1 == K:
                    lg, st = longest_run(r30.forced_left(R, tau, K2), K2)
                    still += st + lg - 1 == K2
                e = lg - W
                e_best = e if e_best is None or e > e_best else e_best
            best[W] = e_best
        print(f"   {n:6s} to depth {K2}: largest excess by width: " + " ".join(f"{W}:{e:+d}" for W, e in best.items())
              + f"; runs still reaching {K2}: {still}", flush=True)


def horizon(Ks=(64, 128, 256, 512), wmax=10):
    rng = random.Random(4096)
    words = {"01": [0, 1], "001": [0, 0, 1], "011": [0, 1, 1], "0001": [0, 0, 0, 1], "0011": [0, 0, 1, 1],
             "0111": [0, 1, 1, 1], "random": [rng.getrandbits(1) for _ in range(4096)], "1": [1], "0": [0]}
    grow = {}
    for n, w in words.items():
        Kmax = max(Ks)
        tau = [w[t % len(w)] for t in range(Kmax + 2)]
        best = {K: None for K in Ks}
        for W in range(0, wmax + 1):
            lo, hi = (0, 1) if W == 0 else (1 << (W - 1), 1 << W)
            for R in range(lo, hi):
                if n == "0" and R == 0:
                    continue
                L = r30.forced_left(R, tau, Kmax)
                for K in Ks:
                    lg, _ = longest_run(L, K)
                    e = lg - W
                    best[K] = e if best[K] is None or e > best[K] else best[K]
        grow[n] = best[max(Ks)] - best[min(Ks)]
        print(f"   {n:6s}: largest excess over widths 0 .. {wmax} by horizon: "
              + " ".join(f"K {K}: {best[K]:+d}" for K in Ks) + f"; growth {grow[n]:+d}", flush=True)
    two = ["01", "001", "011", "0001", "0011", "0111", "random"]
    verdict("UH1 the excess grows by 2 to 5 from K = 64 to 512 for every two-colour word and the random wall",
            all(2 <= grow[n] <= 5 for n in two), ", ".join(f"{n}: {grow[n]:+d}" for n in two))
    verdict("UH2 the one-colour walls do not grow", grow["0"] == 0 and grow["1"] == 0,
            f"0: {grow['0']:+d}, 1: {grow['1']:+d}")


def windows(Ks=(128, 256, 512, 1024, 2048), wmax=10):
    rng = random.Random(4096)
    words = {"01": [0, 1], "001": [0, 0, 1], "0001": [0, 0, 0, 1], "random": [rng.getrandbits(1) for _ in range(4096)]}
    res = {}
    for n, w in words.items():
        Kmax = max(Ks)
        tau = [w[t % len(w)] for t in range(Kmax + 2)]
        best = {K: 0 for K in Ks}
        for W in range(0, wmax + 1):
            lo, hi = (0, 1) if W == 0 else (1 << (W - 1), 1 << W)
            for R in range(lo, hi):
                L = r30.forced_left(R, tau, Kmax)
                for K in Ks:
                    run, longest = 0, 0
                    for k in range(K // 2, K + 1):           # depths K/2 .. K; a run may start before the window
                        run = 0 if L[k - 1] else run + 1
                        longest = max(longest, run)
                    best[K] = max(best[K], longest)
        res[n] = best
        print(f"   {n:6s}: longest zero run in the window [K/2, K], over widths 0 .. {wmax}: "
              + " ".join(f"K {K}: {best[K]}" for K in Ks), flush=True)
    g = {n: res[n][max(Ks)] - res[n][min(Ks)] for n in res}
    verdict("UV1 for 01 the deep runs do not grow (at most +1 from K = 128 to 2048)", g["01"] <= 1, f"{g['01']:+d}")
    verdict("UV2 for the random wall they grow by at least 2", g["random"] >= 2, f"{g['random']:+d}")
    verdict("UV3 001 like 01 (at most +1), 0001 like the random wall (at least +2)", g["001"] <= 1 and g["0001"] >= 2,
            f"001 {g['001']:+d}, 0001 {g['0001']:+d}")


if __name__ == "__main__":
    {"deep": deep, "horizon": horizon, "windows": windows, "slow": slow}.get(sys.argv[1] if len(sys.argv) > 1 else "", main)()
