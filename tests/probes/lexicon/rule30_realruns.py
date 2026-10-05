#!/usr/bin/env python3
"""rule30_realruns.py: do real zero runs follow the bottleneck? Every right half up to 28 cells, exhaustively.

RUN-ON:     cpu (C99 via cc, driven from Python 3 with the standard library; 4 processes)
COMMAND:    python3 tests/probes/lexicon/rule30_realruns.py
COST:       about five minutes on 4 cores.

The picture so far (PRIZE-PROBLEMS.md sections 8.14 and 8.16, rule30_bottleneck.py). A zero run of the forced left half
costs about one bit per cell, paid from the distinct visible histories of column 1. A right half's bits reach column
1 slowly: D(W, t), the number of distinct histories over every right half of at most W cells, stops depending on W
early on (the channel limits it) and keeps growing with W later (the seed limits it). If the picture is right, the
longest real zero run from a fixed depth s, R*(W, s), should stop growing with W at shallow depths and keep growing
at deep ones, and should track log2 D(W, s + 40) minus a constant.

The calibration, from the W = 16 runs already known (rule30_merge.py: 8, 10, 8, 11, 10 at s = 41, 57, 73, 89, 105) and
the bottleneck's log2 D(16, s + 40) (12.20, 12.66, 13.03, 13.33, 13.59): R* is log2 D less 3.56 on average.

PREDICTIONS, written 2026-10-05 before this script's first run:
  RC  (control): the W = 16 maxima are 8, 10, 8, 11, 10, and each depth's histogram sums to 2^W - 1.
  RR1 (blind; saturation at shallow depth): R*(W, 41) <= 12 for every W up to 28.
  RR2 (blind; growth at depth): R*(28, 105) >= 12, two more than at W = 16.
  RR3 (blind; the coin model with the bottleneck's counts): for W = 20 and 24 at the five depths, R*(W, s) lies within
      2.5 of log2 D(W, s + 40) - 3.56, with log2 D from rule30_bottleneck.py (W = 20: 13.25, 14.06, 14.66, 15.16, 15.58;
      W = 24: 13.62, 14.70, 15.56, 16.27, 16.88).
  RR4 (the random-chaos step): 2^20 seeded random right halves of exactly 40 cells, whose bits arrive later than a
      20-cell seed's: their longest run from depth 105 is at least R*(20, 105) + 1.
REFUTED-BY: RC failing (the instrument); RR1 to RR4 failing.
"""
import math, pathlib, re, subprocess, sys, tempfile
from collections import defaultdict

HERE = pathlib.Path(__file__).resolve().parent
DEPTHS = [41, 57, 73, 89, 105]
WS = [16, 18, 20, 22, 24, 26, 28]
LOG2D = {20: [13.25, 14.06, 14.66, 15.16, 15.58], 24: [13.62, 14.70, 15.56, 16.27, 16.88]}
C = 3.56
NPROC = 4
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def collect(outputs):
    H = defaultdict(lambda: defaultdict(int))
    for out in outputs:
        for w, s, n, c in re.findall(r"^Z (\d+) (\d+) (\d+) (\d+)$", out, re.M):
            H[int(s)][int(n)] += int(c)
    return H


def main():
    exe = pathlib.Path(tempfile.mkdtemp()) / "realruns"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "realruns.c")], check=True)
    best, sums = {}, {}
    for W in WS:
        procs = [subprocess.Popen([str(exe), str(W), str(k), str(NPROC)] + [str(s) for s in DEPTHS],
                                  stdout=subprocess.PIPE, text=True) for k in range(NPROC)]
        H = collect([p.communicate()[0] for p in procs])
        for s in DEPTHS:
            best[(W, s)] = max(n for n, c in H[s].items() if c)
            sums[(W, s)] = sum(H[s].values())
        print(f"   W {W:2d}: longest run from depths {DEPTHS}: " + " ".join(str(best[(W, s)]) for s in DEPTHS)
              + "   (halves with a run >= 12 from depth 105: " + str(sum(c for n, c in H[105].items() if n >= 12)) + ")",
              flush=True)
    rc = [best[(16, s)] for s in DEPTHS] == [8, 10, 8, 11, 10] and all(sums[(W, s)] == (1 << W) - 1 for W in WS
                                                                        for s in DEPTHS)
    report("RC the W = 16 maxima are 8, 10, 8, 11, 10, and every histogram sums to 2^W - 1", rc)
    r1 = [best[(W, 41)] for W in WS]
    verdict("RR1 saturation at shallow depth: R*(W, 41) <= 12 for every W up to 28", max(r1) <= 12,
            ", ".join(f"W {W}: {best[(W, 41)]}" for W in WS))
    verdict("RR2 growth at depth: R*(28, 105) >= 12", best[(28, 105)] >= 12, f"R*(28, 105) = {best[(28, 105)]}")
    dev = {(W, s): best[(W, s)] - (LOG2D[W][i] - C) for W in (20, 24) for i, s in enumerate(DEPTHS)}
    verdict("RR3 R* within 2.5 of log2 D - 3.56 at W = 20, 24", all(abs(v) <= 2.5 for v in dev.values()),
            "; ".join(f"W {W} s {s}: {best[(W, s)]} vs {LOG2D[W][DEPTHS.index(s)] - C:.1f}" for (W, s) in dev))
    out = subprocess.run([str(exe), "random", "40", str(1 << 20), "2026"] + [str(s) for s in DEPTHS],
                         capture_output=True, text=True).stdout
    Hr = collect([out])
    rb = {s: max(n for n, c in Hr[s].items() if c) for s in DEPTHS}
    verdict("RR4 the random-chaos step: 2^20 random 40-cell halves beat R*(20, 105) by at least 1",
            rb[105] >= best[(20, 105)] + 1,
            f"random 40-cell longest runs {[rb[s] for s in DEPTHS]} against W = 20: {[best[(20, s)] for s in DEPTHS]}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
