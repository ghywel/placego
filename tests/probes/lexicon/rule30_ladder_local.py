#!/usr/bin/env python3
"""rule30_ladder_local.py: the layer ladder R(M, S) of sections 8.12 and 8.14, far deeper, for an outright exclusion:
no finite configuration, with any right half at all, has column 0 = 0101... from time 0 and its leftmost black cell
less than S cells to the left. (Local, 2026-10-05; RULE30-PRIZE.md section 8.56; engine ladder_deep.c.)

RUN-ON:     cpu, every core (ladder_deep.c is OpenMP; about 0.7 GB at M = 24)
COMMAND:    python3 tests/probes/lexicon/rule30_ladder_local.py check
            python3 tests/probes/lexicon/rule30_ladder_local.py deep [M=24] [DEPTHS=153,185,217,249,265] [THREADS=6]
COST:       check: a minute. deep: each 16 depths cost about 2.3 times more at M = 24 (70 core-seconds at 121, so
            about 27 core-hours at 265; the whole list about 42 core-hours).

WHY IT IS AN EXCLUSION. A width-M layer next to column 0, fed any input sequence in column M + 1, can show every
column 1 that a real right half can show, and more. If a configuration had column 0 = 0101... from time 0 and its
leftmost black cell at depth L, the forced left half would be zero at every depth beyond L. So R(M, S) would be
infinite for every M and every S > L. A finite R(M, S) for one M therefore excludes every L < S.
From Cloud's own runs (section 8.14: R(12, 105) = 20) this already gives L >= 105, which had not been stated.

PREDICTIONS, written 2026-10-05 before the first deep run. Seen before: ladder_deep.c at depths up to 137 for
M = 10 to 24, to measure its cost (R(24, 105) = 13, R(24, 121) = 12, with 58,281 and 141,210 start groups).
  LL0 (control, must hold): ladder_deep.c prints exactly ladder.c's histogram and R at 15 points, M from 0 to 12 and
      S from 9 to 89 (mode check).
  LL1 (the exclusion; blind): R(24, S) is finite at every depth run (no run reaches the cap of 318).
  LL2 (blind; the coin law of section 8.14): R(24, S) / log2 G(24, S) lies between 0.75 and 1.35 at every depth run,
      where G is the number of start groups.
  LL3 (blind): G(24, S) grows by a factor between 1.40 and 1.60 for every 8 depths, from 153 to the deepest.
  LL4 (blind): R(24, S) <= 40 at every depth up to 265.
REFUTED-BY: LL0 failing (the engine). LL1 failing would be a run that never ends within the cap: a candidate for a
  column 1 that keeps the left half zero, to be followed deeper before anything else. LL2 to LL4 the other way.

OUTCOME: (recorded below as the depths finish)
"""
import math, pathlib, subprocess, sys, tempfile
from ompflags import OMP

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "rule30_ladder_local.txt"
POINTS = [(0, 9), (0, 17), (0, 25), (0, 33), (1, 17), (1, 33), (1, 41), (4, 33), (4, 49), (6, 57), (8, 41), (8, 73),
          (10, 57), (12, 65), (12, 89)]


def build():
    old = pathlib.Path(tempfile.gettempdir()) / "rule30_ladder_ref"
    new = pathlib.Path(tempfile.gettempdir()) / "rule30_ladder_deep"
    subprocess.run(["cc", "-O2", "-o", str(old), str(HERE / "ladder.c")], check=True)
    arch = ["-mcpu=apple-m1"] if sys.platform == "darwin" else []
    subprocess.run(["cc", "-O3", "-DNW=5", *arch, *OMP, "-o", str(new), str(HERE / "ladder_deep.c")], check=True)
    return old, new


def strip(text):
    return "\n".join(ln.split(";")[0].replace("R M", "R") for ln in text.strip().splitlines())


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    old, new = build()
    if mode == "check":
        bad = 0
        for m, s in POINTS:
            a = subprocess.run([str(old), "hist", str(m), str(s)], capture_output=True, text=True, check=True).stdout
            b = subprocess.run([str(new), str(m), str(s), "4"], capture_output=True, text=True, check=True).stdout
            same = strip(a) == strip(b)
            bad += not same
            print(f"   M {m:2d} S {s:3d}: {'same' if same else 'DIFFERENT'}  {strip(b).splitlines()[-1]}", flush=True)
        print(f"{'PASS' if bad == 0 else 'FAIL'}  LL0 ladder_deep.c equals ladder.c at {len(POINTS)} points")
        return
    m = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    depths = [int(x) for x in (sys.argv[3] if len(sys.argv) > 3 else "153,185,217,249,265").split(",")]
    threads = sys.argv[4] if len(sys.argv) > 4 else "6"
    rows = []
    for s in depths:
        out = subprocess.run([str(new), str(m), str(s), threads], capture_output=True, text=True, check=True).stdout
        with open(OUT, "a") as fh:
            fh.write(out)
        last = out.strip().splitlines()[-1]
        f = last.replace("(", " ").replace(";", " ").split()
        r, capped = int(f[f.index("=") + 1]), "CAPPED" in last
        groups = int(f[f.index("start") - 1])
        rows.append((s, r, groups, capped))
        print(f"   {last}", flush=True)
    print(f"{'HELD' if not any(c for *_, c in rows) else 'REFUTED'}  prediction LL1 every run is finite")
    ratios = [r / math.log2(g) for s, r, g, c in rows]
    print(f"{'HELD' if all(0.75 <= x <= 1.35 for x in ratios) else 'REFUTED'}  prediction LL2 R / log2 G in "
          f"[0.75, 1.35]  ({', '.join(f'{x:.2f}' for x in ratios)})")
    growth = [(rows[i + 1][2] / rows[i][2]) ** (8 / (rows[i + 1][0] - rows[i][0])) for i in range(len(rows) - 1)]
    if growth:
        print(f"{'HELD' if all(1.40 <= x <= 1.60 for x in growth) else 'REFUTED'}  prediction LL3 G grows 1.40 to "
              f"1.60 per 8 depths  ({', '.join(f'{x:.3f}' for x in growth)})")
    print(f"{'HELD' if all(r <= 40 for s, r, g, c in rows if s <= 265) else 'REFUTED'}  prediction LL4 R <= 40 to "
          f"depth 265  ({', '.join(f'{s}: {r}' for s, r, g, c in rows)})")


if __name__ == "__main__":
    main()
