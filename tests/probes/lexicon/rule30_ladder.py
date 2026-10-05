#!/usr/bin/env python3
"""rule30_ladder.py: the first rungs of the LR_m ladder (PRIZE-PROBLEMS.md section 8.11), the "kick game" done
properly. How long can a layer of width m next to column 0 = 0101..., fed the most adversarial input, hold the
forced left half at zero, starting at depth s?

RUN-ON:     cpu (C99 via cc, driven from Python 3 with the standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_ladder.py
COST:       a few minutes on one core.

R(m, s) is the longest run of zeros starting at depth s, over every start of the layer's cells 1..m and every input
sequence in column m + 1 (ladder.c, which explains why the search is a breadth-first search over at most 2^m
states). m = 0 is the left side alone (conjecture LR, section 7): column 1 is free.

PREDICTIONS, written 2026-10-05 before this script's first run:
  LS  (control): ladder.c's left-half recursion agrees with rule30_linear_cell.py's column recursion on 200 seeded
      random columns 1 of 120 steps.
  LD1 (control, known answer): R(0, 33) = 33, the exhaustive left-alone value of rule30_rigidity.py at depth 33
      (rule30_twosided_exact.py's X2).
  LD2 (theorem check, the ladder): R(m, s) >= R(m + 1, s) for every m and s computed.
  LD3 (theorem check): R(m, s) is at least the longest zero run starting at depth s that a real finite right half
      (every one up to 12 cells) produces, for every m.
  LD4 (blind): a finite layer tames the left side: R(m, 33) <= 24 for some m <= 10.
  LD5 (blind): at m = 8 the run grows with the start depth at most half as fast as at m = 0:
      R(8, 33) - R(8, 17) <= (R(0, 33) - R(0, 17)) / 2.
  LD6 (blind): no layer of width 1 or more lets the input hold the left half at zero to the deepest depth computed
      (126); no R(m >= 1, s) is capped.
REFUTED-BY: LS, LD1, LD2 or LD3 failing (the instrument); LD4, LD5 or LD6 failing.
"""
import pathlib, random, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_argv, sys.argv = sys.argv, [sys.argv[0], "1", "120", "1"]      # rule30_linear_cell reads W, K, JOBS at import
import rule30_linear_cell as lc                                  # noqa: E402
sys.argv = [sys.argv[0]]
import rule30_periodic as r30                                    # noqa: E402
sys.argv = _argv
MS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
SS = [17, 25, 33]
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def main():
    tmp = pathlib.Path(tempfile.mkdtemp())
    exe = tmp / "ladder"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "ladder.c")], check=True)

    rng = random.Random(30)
    bad = 0
    tau = [t % 2 for t in range(121)]
    for _ in range(200):
        sigma = [rng.getrandbits(1) for _ in range(121)]
        want = lc.left_from_col1(tau, sum(b << t for t, b in enumerate(sigma)))[:120]
        got = subprocess.run([str(exe), "left", "".join(map(str, sigma[:120]))], capture_output=True, text=True).stdout
        bad += [int(c) for c in got.strip()] != want
    report("LS ladder.c's left recursion agrees with the column recursion", bad == 0, f"{bad} of 200 differ")

    R, capped = {}, {}
    for m in MS:
        for s in SS:
            out = subprocess.run([str(exe), "run", str(m), str(s)], capture_output=True, text=True).stdout
            v = int(re.search(r"= (\d+)", out).group(1))
            R[(m, s)] = v
            capped[(m, s)] = "CAPPED" in out
            print("   " + out.strip(), flush=True)

    report("LD1 R(0, 33) = 33, the exhaustive left-alone value", R[(0, 33)] == 33, f"R(0, 33) = {R[(0, 33)]}")
    mono = all(R[(MS[i], s)] >= R[(MS[i + 1], s)] for s in SS for i in range(len(MS) - 1))
    report("LD2 R(m, s) never increases with m (the ladder)", mono)
    real = {}
    tauK = [t % 2 for t in range(141)]
    for R0 in range(1, 1 << 12):
        L = r30.forced_left(R0, tauK, 140)
        for s in SS:
            n = 0
            while s - 1 + n < len(L) and L[s - 1 + n] == 0:
                n += 1
            real[s] = max(real.get(s, 0), n)
    ok3 = all(R[(m, s)] >= real[s] for m in MS for s in SS)
    report("LD3 every R(m, s) is at least the real two-sided run from depth s (right halves up to 12 cells)", ok3,
           ", ".join(f"real from {s}: {real[s]}" for s in SS))
    tame = [m for m in MS if R[(m, 33)] <= 24]
    verdict("LD4 a finite layer tames the left side: R(m, 33) <= 24 for some m <= 10", bool(tame), f"m with R <= 24: {tame}")
    g0 = R[(0, 33)] - R[(0, 17)]
    g8 = R[(8, 33)] - R[(8, 17)]
    verdict("LD5 at m = 8 the run grows with depth at most half as fast as at m = 0", g8 <= g0 / 2,
            f"growth from s = 17 to 33: m = 0 {g0}, m = 8 {g8}")
    cap = [(m, s) for (m, s), c in capped.items() if c and m >= 1]
    verdict("LD6 no layer of width 1 or more holds the left half at zero to depth 126", not cap, f"capped: {cap}")
    print("\n   R(m, s), rows m, columns s = " + ", ".join(map(str, SS)))
    for m in MS:
        print(f"      m = {m:>2}: " + "  ".join(f"{R[(m, s)]:>3}" for s in SS))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
