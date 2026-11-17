#!/usr/bin/env python3
"""rule30_cloud_bricks.py: next to the 0101 wall, a periodic column 1 freezes the left half into one repeated brick.

RUN-ON:     cpu (rule30_bricks.c via cc, driven from Python 3 with the standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_bricks.py [PMAX=20] [OUT=<tmp>/rule30_bricks]
COST:       measured in the outcome. Data goes to OUT, outside git.

Why (the owner, 2026-10-09): "interlocking shapes are some of the most interesting objects ... especially the unusual
single form shapes that interlock to infinity. I would like an exploration on the applicability on rule 30."
RULE30-PRIZE.md §8.72 holds the whole exploration; this probe is its computation.

Rule 30's histories are tilings. Take one Wang tile per neighbourhood (l, c, r): west edge (l, c), east edge (c, r),
south edge c, north edge f(l, c, r). The tilings of the plane by these 8 tiles are exactly the bi-infinite Rule 30
histories. The set is not aperiodic: the white row, the checkerboard and every turning row (§8.71) tile periodically,
each as a wallpaper of one brick (a fundamental domain of its period lattice). GC686's ring, whose lattice is spanned
by (14, 1) and (0, 6) in (space, time), is a wall of 14 x 6 bricks, each column of bricks one step lower than the
last.

Jen's case freezes into bricks (elementary; noted here, not claimed new). Let column 0 be the wall 0101.. and column
1 any word of even length P, both P-periodic. Rule 30 run sideways, x_t(i-1) = x_{t+1}(i) XOR (x_t(i) OR x_t(i+1)),
maps the pair (c_i, c_{i+1}) to (c_{i-1}, c_i), a map Phi on 2^(2P) states. So from some depth mu on, the left half is
periodic in space as well as in time: a wallpaper of one P x Q brick, Q the cycle length. Proposition 7 (Jen) says that
brick is never blank. Theorem B (§8.54) says its rows have no white run longer than 2P - 2. The prize's period-2 case
is the other side of this: column 1 not periodic, no brick forced, and a finite seed would need the blank one.

Smoke test, disclosed, before these predictions (P = 2, 4, 6, 8, every word):
  P = 2: 4 words, one brick, the checkerboard (black and white columns alternating, constant in time; Q = 2).
  P = 4: 8 words to the checkerboard, 8 to a Q = 7 brick of density 13/28 (the 7-ring's 4-cycle, §5 and G4.2).
  P = 6: 16 to the checkerboard, 48 to a Q = 84 brick staggered 14 by one step, density 43/84: GC686's all-S ring.
         GPT's own word 110100 enters it at once (mu = 0).
  P = 8: 32 to the checkerboard, 224 to the 7-ring brick; transients up to 29 columns.
  By hand, after the smoke test: a word white at every even time sends column -1 black for ever and then the
  checkerboard, which accounts for 2^(P/2) of the checkerboard's 2^(P/2 + 1) words.

PREDICTIONS, written 2026-10-09 by 08:27 BST, before the run at P = 10 .. 20 (every word of length P).
  BK1 (control). Word 110100 at P = 6 gives mu = 0, Q = 84, staggered Q' = 14 by one step, density 43/84.
  BK2 (control, Proposition 7). No word at any P reaches the blank brick.
  BK3 (control, Theorem B). No row of any forced left half has a white run longer than 2P - 2.
  BK4 (blind). At every P from 10 to 20 there are at most 8 distinct bricks, counted up to a turn in time.
      Confidence 0.5.
  BK5 (blind). At every P from 10 to 20 the checkerboard holds exactly 2^(P/2 + 1) words. Confidence 0.6.
  BK6 (blind). At every P from 10 to 20 one brick other than the checkerboard holds more than half the words.
      Confidence 0.6.
UNEXPECTED CHECK, BK7: the longest transient at each P stays below 2^(P/2 + 2) columns (64 at P = 8, where the smoke
  test saw 29). Confidence 0.5.
Counterfactual: many bricks, or no dominant one, would say the sideways map behaves like a random map on its
  2^(2P) states. A few universal bricks would say the left half next to the wall has a small set of crystals,
  periodic cousins of the band, and the prize asks whether a non-periodic column 1 can make it crystallise blank.
REFUTED-BY: BK1 to BK3 failing (the instrument or a theorem); BK4 to BK7 failing as worded.

OUTCOME, 2026-10-09 (full run 08:31 to 08:33 BST, 86 s; every word of every even length 2 .. 20; data outside git).
  The instrument changed once, before the P = 20 run and after the predictions. The first run, started at 08:27,
  walked every word around its whole brick and was projected at about an hour for P = 20. A fast path now stops
  each walk at the first state of a brick already found, or a rotation of one. Its output was byte-identical to the
  original program's at every P from 2 to 18. The original's P = 20 run was stopped, and the recorded run is the
  fast one throughout.
  BK1, BK2 and BK3 PASS. Word 110100 enters GC686's brick at once (Q 84, Q' 14 by one step, density 43/84). No word
  at any P freezes blank, and no row has a white run longer than 2P - 2.
  BK4 HELD: at most 7 bricks at any P (1, 2, 2, 2, 3, 6, 4, 4, 7, 6 at P = 2 .. 20).
  BK5 HELD: the checkerboard holds exactly 2^(P/2 + 1) words at every P.
    POST HOC: they are exactly the words whose visible bits (column 1 at the wall's white times) are constant, at
    every P from 2 to 20. One direction is a hand check. All white visible bits make column -1 all black; all black
    ones make column -1 a copy of the wall and column -2 all black. An all-black column is followed by an all-white
    one, and that pair is the checkerboard. The converse is measured, not proved.
  BK6 REFUTED as worded: at P = 18 the largest brick other than the checkerboard holds 105,984 of 262,144 words
    (40.4%). It held at every other P: 78% at P = 10, 56% at 12, 66% at 14, 81% at 16, 53% at 20.
  BK7 HELD (the unexpected check): the longest transient is 33, 92, 127, 426, 1006 and 1554 columns at P = 10 .. 20.
    It is under 2^(P/2 + 2) everywhere, and the median at P = 20 is 496.
  The bricks, by the columns' own period (each recurs at every multiple of it):
    2: the checkerboard, black and white columns alternating, constant in time.
    4: the 7-ring's 4-cycle, 7 columns wide, 13 black of 28.
    6: GC686's all-S ring, 84 wide, staggered every 14 by one step; it takes 48 of the 64 words at P = 6.
    10: 155 wide staggered every 31 by 2 steps, and 90 wide staggered every 18 by 6. At P = 20 the 155 brick is
        again the largest, with 53% of all words.
    12: 138 (staggered every 46), 60 (every 15) and 100 (every 25).
    14: 728 (every 104), 1316 (every 94) and 644 (every 92).
    16: 325 (no stagger) and 2032 (every 127).
    18: 1962 (every 218), 8370 (every 930), 4050 (every 225), 342 (every 19) and 477 (every 53).
    20: 25000 (every 1250) and 400 (every 40).
  So all 1,398,100 words of every even length up to 20 freeze into one of 20 bricks. Every brick has density
  between 0.464 and 0.514, and every brick but three (the checkerboard, the 7-ring's and the 325) is staggered.
"""
import math, pathlib, subprocess, sys, tempfile, time
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20
OUT = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path(tempfile.gettempdir()) / "rule30_bricks"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    exe = OUT / "rule30_bricks"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "rule30_bricks.c")], check=True)
    r = subprocess.run([str(exe), "6", "110100"], capture_output=True, text=True, check=True).stdout.split("\n")[0]
    f = r.split()
    bk1 = f[1:5] == ["0", "84", "14", "1"] and abs(float(f[5]) - 43 / 84) < 1e-4
    print(f"BK1 {'PASS' if bk1 else 'FAIL'}: word 110100 -> mu {f[1]}, Q {f[2]}, Q' {f[3]} by {f[4]}, dens {f[5]}")
    bk2 = bk3 = bk4 = bk5 = bk6 = bk7 = True
    for P in range(2, PMAX + 1, 2):
        t0 = time.time()
        with open(OUT / f"bricks_P{P}.txt", "w") as fh:
            subprocess.run([str(exe), str(P)], stdout=fh, check=True)
        dt = time.time() - t0
        words, bricks, summ = [], [], None
        for line in open(OUT / f"bricks_P{P}.txt"):
            if line.startswith("BRICK"):
                bricks.append(dict(kv.split("=", 1) for kv in line.split()[1:]))
            elif line.startswith("SUM"):
                summ = dict(kv.split("=", 1) for kv in line.split()[1:])
            else:
                words.append(line.split())
        n = len(words)
        mu = [int(w[1]) for w in words]
        if int(summ["blank"]):
            bk2 = False
        if int(summ["zero_run_over_2P-2"]):
            bk3 = False
        cb = [b for b in bricks if b["a"] == format(2 ** P - 1, "x") and b["b"] == "0"]   # the checkerboard
        cbw = int(cb[0]["words"]) if cb else 0
        others = sorted((int(b["words"]) for b in bricks if b not in cb), reverse=True)
        top = others[0] if others else 0
        if P >= 10:
            if len(bricks) > 8:
                bk4 = False
            if cbw != 2 ** (P // 2 + 1):
                bk5 = False
            if top <= n / 2:
                bk6 = False
            if max(mu) >= 2 ** (P // 2 + 2):
                bk7 = False
        print(f"P={P:2d} words={n} bricks={len(bricks)} checkerboard={cbw} (2^(P/2+1)={2 ** (P // 2 + 1)}) "
              f"largest other={top} ({top / n:.3f}) max mu={max(mu)} median mu={sorted(mu)[n // 2]} ({dt:.1f} s)")
        for b in sorted(bricks, key=lambda b: -int(b["words"]))[:6]:
            print(f"    brick Q={b['Q']} Q'={b['Qs']} r={b['r']} dens={b['dens']} words={b['words']} "
                  f"columns a={b['a']} b={b['b']}")
    print(f"BK2 {'PASS' if bk2 else 'FAIL'}")
    print(f"BK3 {'PASS' if bk3 else 'FAIL'}")
    for name, ok in (("BK4", bk4), ("BK5", bk5), ("BK6", bk6), ("BK7", bk7)):
        print(f"{name} {'HELD' if ok else 'REFUTED'}")
    print(f"data in {OUT}")


if __name__ == "__main__":
    main()
