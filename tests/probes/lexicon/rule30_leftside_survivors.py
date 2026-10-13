#!/usr/bin/env python3
"""rule30_leftside_survivors.py: does the edge supply the price? The left-only survivor curve beside 0101, to width 32.

Section 8.69's left horizon H_L(W) is the longest any finite left seed of width W (cell -W black) keeps the two
conditions on column -1 that no right half can lift; it bounds the lifetime of every two-sided configuration whose left
half has width W. So H_L(W) finite for every W gives period 2 for every finite configuration (the conditions it uses
are necessary), and a linear bound H_L(W) <= c W + b is GC637's uniform edge deadline, which gives Q1 with alpha = 1/c.
Beside 0101 the latch (ii) is vacuous (every white stretch has length 1), so the one condition is: column -1 black at
every black time of the wall.

The price picture (RULE30-PRIZE.md 8.92): while a black time's fresh cell, -(t+1), lies inside the seed (t <= W - 2), it
enters column -1 by XOR, so the condition halves the survivors exactly. After that the left half has no fresh bits and
runs deterministically from the seed. What happens then is the question. Two laws fit section 8.69's data to W = 20:
  edge:  H_L(W) = W + about 17 (8.69's own reading, "width plus a constant of about 17 from W = 11 on");
  coin:  the post-fresh phase costs about one bit per black-time condition, like a fair coin. About 2^(W/2) seeds
         survive the fresh phase, so they need about W/2 more conditions, W more ticks: H_L(W) = 2W + O(log W).
They agree near W = 19 (H_L(19) = 38, H_L(20) = 37) and part from W = 26 on. Both are linear, so neither outcome
refutes GC637's hypothesis; a superlinear H_L would. Which one holds says what a proof has to supply: a bounded kill
time after the edge's information arrives (edge), or a price paid by the deterministic phase itself (coin).

Tool: leftside_survivors.c, a variant of leftside_horizon.c (frozen) with the same survive() and seed encoding, printing
how many seeds survive exactly h observations.

RUN-ON:     cpu, 10 threads (OpenMP; ompflags.py), the M5
COMMAND:    python3 tests/probes/lexicon/rule30_leftside_survivors.py [WMAX=32] [T=90]
COST:       about a minute (2^31 seeds a phase at W = 32, a few ticks each).

Record searched: 'leftside_horizon' and 'H_L' -> 8.69 (W <= 20, LH0 to LH3), GC638 (finite-left deadlines, no rate),
GC640 (black-time tests keep nonlinear depth dependence); 'edge deadline' -> GC637 (proved, L345); 'H(j) - j' -> DL,
DL2, GC660 (exact hulls, H(j) - j <= 17 for j <= 22, measured); 'survivor curve' with 'left' -> no hit.

PREDICTIONS (written 2026-10-13 before the run; announced in CHAT-LEDGER L649 before it).
  S0 must hold (calibration against the frozen tool): the maxima for W = 0 .. 20 are 8.69's committed list
     1, 7, 6, 5, 6, 9, 10, 12, 17, 18, 17, 30, 29, 28, 32, 31, 30, 31, 33, 38, 37.
  S1 must hold (left permutivity): for every W >= 2, phase and tick t <= W - 2, the survivors halve exactly at a black
     time and are unchanged at a white time.
  S2 blind, the question. Edge law: H_L(W) <= W + 19 for every W = 21 .. 32. Coin law: H_L(W) >= 2W - 6 for every
     W = 26 .. 32. The two exclude each other from W = 26. My lean is the coin law (about 60 percent), because 8.69's
     last two values sit at 2W - 2 and the record's general finding is about a bit per condition plus a logarithm of
     luck. REFUTED-BY: for the edge law, any W in 21 .. 32 with H_L(W) >= W + 20; for the coin law, any W in 26 .. 32
     with H_L(W) <= 2W - 7. Both can fail (a slope between 1 and 2, or growth faster than linear).
  S3 descriptive, no prediction: the post-fresh decay, in bits lost per black-time condition after tick W - 1, while
     at least 16 seeds survive, pooled over phases, by width.
  C1 cap alarm: no seed reaches T (a maximum equal to the cap would make the census a lower bound only).

OUTCOME: (filled in after the run, below this line)
"""
import math, pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ompflags import OMP

HL20 = [1, 7, 6, 5, 6, 9, 10, 12, 17, 18, 17, 30, 29, 28, 32, 31, 30, 31, 33, 38, 37]

def black(phase, t):
    return "01"[(phase + t) % 2] == "1"

def main():
    wmax = int(sys.argv[1]) if len(sys.argv) > 1 else 32
    T = int(sys.argv[2]) if len(sys.argv) > 2 else 90
    exe = pathlib.Path(tempfile.mkdtemp()) / "leftside_survivors"
    arch = ["-mcpu=native"] if sys.platform == "darwin" else ["-march=native"]
    subprocess.run(["cc", "-O3", *arch, *OMP, "-o", str(exe), str(HERE / "leftside_survivors.c")], check=True)
    hist = {}                                  # (W, phase) -> {h: count}
    proc = subprocess.Popen([str(exe), "01", "0", str(wmax), str(T), "10"], stdout=subprocess.PIPE, text=True)
    for line in proc.stdout:
        head, _, body = line.partition(":")
        _, word, W, ph = head.split()
        d = {}
        for item in body.strip().strip(",").split(","):
            if item.strip():
                h, c = item.split(); d[int(h)] = int(c)
        hist[(int(W), int(ph))] = d
        if int(ph) == 1:
            W = int(W); best = max(max(hist[(W, 0)]), max(hist[(W, 1)]))
            print(f"  W={W:2d}: H_L = {best:3d}   W + 19 = {W + 19:3d}   2W - 6 = {2 * W - 6:3d}", flush=True)
    proc.wait()
    ok = {}
    H = {W: max(max(hist[(W, 0)]), max(hist[(W, 1)])) for W in range(wmax + 1)}
    ok["S0"] = [H[W] for W in range(21)] == HL20
    s1 = True
    for W in range(2, wmax + 1):
        for ph in (0, 1):
            d = hist[(W, ph)]
            N = lambda t: sum(c for h, c in d.items() if h >= t)
            for t in range(0, W - 1):
                a, b = N(t), N(t + 1)
                if black(ph, t): s1 &= (2 * b == a)
                else: s1 &= (b == a)
    ok["S1"] = s1
    edge = all(H[W] <= W + 19 for W in range(21, wmax + 1))
    coin = all(H[W] >= 2 * W - 6 for W in range(26, wmax + 1))
    print(f"\nS2: edge law (H_L <= W + 19, W = 21..{wmax}) {'HELD' if edge else 'REFUTED'}; "
          f"coin law (H_L >= 2W - 6, W = 26..{wmax}) {'HELD' if coin else 'REFUTED'}")
    print("S3: post-fresh decay, bits per black-time condition after tick W - 1 (N >= 16), pooled over phases:")
    for W in range(12, wmax + 1, 2):
        Ns = {}
        for ph in (0, 1):
            d = hist[(W, ph)]
            for t in range(W - 1, T + 1):
                Ns[(ph, t)] = sum(c for h, c in d.items() if h >= t)
        pts = []
        for ph in (0, 1):
            n0 = Ns[(ph, W - 1)]; k = 0
            for t in range(W - 1, T):
                if black(ph, t):
                    k += 1
                    n1 = Ns[(ph, t + 1)]
                    if n1 >= 16 and n0 > 0: pts.append(math.log2(n0 / n1) / k)
        mean = sum(pts) / len(pts) if pts else float('nan')
        surv = Ns[(0, W - 1)] + Ns[(1, W - 1)]
        print(f"  W={W:2d}: survivors after the fresh phase {surv}, mean bits per condition {mean:.2f} ({len(pts)} points)")
    ok["C1"] = all(H[W] < T for W in H)
    print("\n" + "  ".join(f"{k} {'HELD' if v else 'FAILED'}" for k, v in ok.items()))
    print("ALL CHECKS PASS" if all(ok.values()) else "SOME CHECKS FAILED")

if __name__ == "__main__":
    main()
