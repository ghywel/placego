#!/usr/bin/env python3
"""rule30_ladder_deep.py: the ladder's rungs at depth. Does R(m, s) stay bounded as the start depth s grows?

RUN-ON:     cpu (C99 via cc, driven from Python 3 with the standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_ladder_deep.py
COST:       about half an hour on one core.

R(m, s) is defined in ladder.c and rule30_ladder.py. The first table (s = 17, 25, 33) showed a thin layer taming the
adversary: from m = 7 on, R(m, 33) = 7, against 33 with column 1 free. If R(m, s) stays bounded as s grows for some
fixed m, then LR_m holds, and so does B for the period-two trace (section 8.11). ladder.c now keeps its start groups in
a hash table (only the groups the layer can produce), so s is limited by depth 126, not by 2^(s/2). Before this
script was written, the hash version reproduced all 30 values and group counts of the first table.

PREDICTIONS, written 2026-10-05 before this script's first run:
  DL0 (regression control): ladder.c reproduces the first table's 30 values.
  DL1 (blind): R(8, s) <= 16 for every s = 41, 49, ..., 105.
  DL2 (blind): R(10, s) <= 12 for every s = 41, 49, ..., 105.
  DL3 (blind, the contrast): with column 1 free the runs keep growing: R(0, 41) >= 35.
  DL4 (blind): at m = 12 there is no growth with depth: the mean of R(12, s) over s = 73..105 is at most the mean over
      s = 41..65, plus 1.
  DL5 (theorem checks): at every s, R never rises with m; and every R(m, s) is at least the longest zero run from depth
      s that a real right half (every one up to 12 cells) produces.
REFUTED-BY: DL0 or DL5 failing (the instrument); DL1 to DL4 failing.

OUTCOME of the first run, 2026-10-05 (14 minutes, the largest point 26 million start groups and 1.1 GB): DL0 passed
(all 30 values and group counts); DL5 passed (R never rises with m; the real runs from depths 41, 49, ..., 105 are
6, 9, 10, 10, 8, 8, 9, 9, 10, and every R is at least that). DL3 HELD: R(0, 41) = 37. DL1 REFUTED: R(8, s) reaches 25
(s = 97). DL2 REFUTED: R(10, s) reaches 21 (s = 105). DL4 REFUTED: at m = 12 the runs grow, early 8, 11, 10, 13 and
late 16, 14, 16, 16, 20. R(6, 105) hit the depth cap (at least 22; 240 start groups reach it). The table, s = 41 to
105 in steps of 8:
    m = 6:  11 11 14 17 20 20 21 25 22+ | m = 8:  8 11 11 13 16 17 16 25 21
    m = 10:  8 11 10 13 16 14 16 19 21  | m = 12: 8 11 10 13 16 14 16 16 20
    (m = 0: 37 at s = 41; m = 1: 15 21 25 and m = 4: 14 15 19 at s = 41, 49, 57)
The start groups grow exponentially with s at every m, by a ratio per 8 depths that settles to 3.40 (m = 6), 2.68
(m = 8), 2.40 (m = 10) and about 2.09 (m = 12). Disclosure: before this run a cost probe printed R(12, 57) = 10 and
R(12, 73) = 16, two of DL4's nine values. Without them DL4 is still refuted (early mean 10.7, late 16.5).
Read after the run (post hoc, so not a result): for m >= 4 and s >= 33, R is close to log2 G, the ratio lying
between 0.81 and 1.26; with column 1 free it is near 2. That reading is tested blind in rule30_ladder_budget.py.
"""
import pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
sys.argv = _argv
FIRST = {(0, 17): 15, (0, 25): 19, (0, 33): 33, (1, 17): 9, (1, 25): 12, (1, 33): 13, (2, 17): 9, (2, 25): 12,
         (2, 33): 13, (3, 17): 9, (3, 25): 12, (3, 33): 13, (4, 17): 9, (4, 25): 12, (4, 33): 11, (5, 17): 9,
         (5, 25): 10, (5, 33): 9, (6, 17): 9, (6, 25): 10, (6, 33): 9, (7, 17): 9, (7, 25): 10, (7, 33): 7,
         (8, 17): 9, (8, 25): 10, (8, 33): 7, (10, 17): 9, (10, 25): 10, (10, 33): 7}
DEEP_S = [41, 49, 57, 65, 73, 81, 89, 97, 105]
PLAN = [(0, [41]), (1, [41, 49, 57]), (4, [41, 49, 57])] + [(m, DEEP_S) for m in (6, 8, 10, 12)]
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def main():
    exe = pathlib.Path(tempfile.mkdtemp()) / "ladder"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "ladder.c")], check=True)

    def R(m, s):
        out = subprocess.run([str(exe), "run", str(m), str(s)], capture_output=True, text=True, timeout=3600).stdout
        print("   " + out.strip(), flush=True)
        return int(re.search(r"= (\d+)", out).group(1)), "CAPPED" in out

    regress = [k for k, v in FIRST.items() if R(*k)[0] != v]
    report("DL0 the hash-table ladder reproduces the first table", not regress, f"differing: {regress}")
    table, capped = {}, []
    for m, ss in PLAN:
        for s in ss:
            v, c = R(m, s)
            table[(m, s)] = v
            if c:
                capped.append((m, s))
    real = {}
    tau = [t % 2 for t in range(131)]
    for R0 in range(1, 1 << 12):
        L = r30.forced_left(R0, tau, 130)
        for s in DEEP_S:
            n = 0
            while s - 1 + n < len(L) and L[s - 1 + n] == 0:
                n += 1
            real[s] = max(real.get(s, 0), n)
    mono = all(table[(a, s)] >= table[(b, s)] for s in DEEP_S for a, b in ((6, 8), (8, 10), (10, 12))
               if (a, s) in table and (b, s) in table)
    above = all(table[(m, s)] >= real[s] for (m, s) in table if s in real)
    report("DL5 R never rises with m, and is never below the real runs", mono and above,
           "real from s: " + ", ".join(f"{s}: {real[s]}" for s in DEEP_S))
    verdict("DL1 R(8, s) <= 16 for s = 41..105", all(table[(8, s)] <= 16 for s in DEEP_S),
            f"max {max(table[(8, s)] for s in DEEP_S)}")
    verdict("DL2 R(10, s) <= 12 for s = 41..105", all(table[(10, s)] <= 12 for s in DEEP_S),
            f"max {max(table[(10, s)] for s in DEEP_S)}")
    verdict("DL3 with column 1 free the runs keep growing: R(0, 41) >= 35", table[(0, 41)] >= 35,
            f"R(0, 41) = {table[(0, 41)]}")
    early = [table[(12, s)] for s in (41, 49, 57, 65)]
    late = [table[(12, s)] for s in (73, 81, 89, 97, 105)]
    verdict("DL4 no growth at m = 12: mean over s = 73..105 <= mean over s = 41..65 + 1",
            sum(late) / len(late) <= sum(early) / len(early) + 1, f"early {early}, late {late}")
    print(f"   capped: {capped or 'none'}")
    print("\n   R(m, s): rows m, columns s")
    cols = sorted({s for (_, s) in table})
    print("        s: " + " ".join(f"{s:>4}" for s in cols))
    for m in sorted({m for (m, _) in table}):
        print(f"   m = {m:>2}: " + " ".join(f"{table[(m, s)]:>4}" if (m, s) in table else "   ." for s in cols))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
