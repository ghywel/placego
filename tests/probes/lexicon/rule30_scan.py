#!/usr/bin/env python3
"""rule30_scan.py: the counterexample search for period two, widened: every right half up to 32 cells.

RUN-ON:     cpu (C99 via cc, driven from Python 3 with the standard library; 3 processes)
COMMAND:    python3 tests/probes/lexicon/rule30_scan.py [WMAX=32] [NPROC=3]
COST:       about an hour on 3 cores for WMAX = 32 (4.3 billion right halves); minutes for WMAX = 28.

Rung 1 (RULE30-PRIZE.md sections 5 and 6) searched every right half up to 18 cells. A finite configuration with
column 0 = 0101... would be a right half whose forced left half is eventually zero. realruns.c's scan mode forces the
left half to depth 126 for every right half of at most W cells, records the longest zero run anywhere in L(1..126),
and lists as candidates the halves whose left half ends in at least 30 zeros at depth 126. Each candidate is then
followed to depth 2,000 with rule30_periodic.forced_left: a counterexample would have to stay zero.

PREDICTIONS, written 2026-10-05 before this script's first run:
  SC0 (control): for W = 12 the scan's histogram of longest runs equals one computed independently in Python
      (rule30_periodic.forced_left, depth 126).
  SC1 (blind; no counterexample, the coin model): no right half up to WMAX cells ends in 30 or more zeros at depth
      126, so no candidate exists to follow. (Under the coin model over the at most 2^18 or so distinct histories,
      the expected number is about 2^18 x 2^-30.) If candidates do appear, every one ends its run before depth 2,000.
  SC2 (blind; the plateau): the longest zero run anywhere in L(1..126) grows by at most 3 cells from W = 18 to
      W = WMAX, and is at most 22 at WMAX. (X3, section 8, found 20 at depth up to 192 for every width from 14 to
      24.)
REFUTED-BY: SC0 failing (the instrument); SC1 or SC2 failing. A candidate that stays zero to depth 2,000 would be
  reported at once, with its right half, and examined further, not counted.

OUTCOME of the first run, 2026-10-05 (WMAX = 32, 3 processes, 01:45 to 03:44 UTC): SC0 passed (the W = 12 histogram
equals the Python one). For W = 18, 20, ..., 32 (up to 4,294,967,295 right halves) the longest zero run in L(1..126)
is 17 at every width (reached by 13, 42, 161, 570, 2,354, 9,479, 37,644 and 150,578 halves), and there are 0
candidates. SC1 HELD and SC2 HELD. With no zero run longer than 17 to depth 126, no finite configuration whose right
half has at most 32 cells and whose left half has at most 108 cells has a column that is 0101... for ever.

---------------------------------------------------------------------------------------------------------------
JOB M3b (Cloud wrote, 2026-10-05; for Local, optional; CLOUD-LOCAL.md lead M3). The same search to 34 cells: 17
billion right halves, about 2 to 3 hours on 10 cores (Cloud's 32-cell run took 2 hours on 3 cores).
RUN-ON:     cpu, all cores
COMMAND:    python3 tests/probes/lexicon/rule30_scan.py 34 10
PREDICTION (written 2026-10-05 before any run of this job):
  SC3 (blind): no candidate ends in 30 or more zeros at depth 126, and the longest zero run in L(1..126) is still 17
      at W = 34.
REFUTED-BY: a candidate (then follow it deeper before anything else: it is either a near miss or the counterexample),
  or a longer run.
HAND BACK to Cloud when the run's output is recorded here, with a ledger line ("Local ran M3b"), pushed to main; AT
  ONCE, without finishing, if any candidate survives to depth 2,000.
OUTCOME of JOB M3b (Local, 2026-10-05, the M5: 10 cores; 15:36:58 to 16:27:30 BST, 50 min 32 s, run as written).
  SC0 PASSED (the scan agrees with the independent Python computation at W = 12). At W = 34, 17,179,869,183 right
  halves: longest zero run in L(1..126) 17, reached by 601,991 halves; candidates ending in >= 30 zeros: 0.
  SC3 HELD: no candidate, and the longest run still 17. SC1 and SC2 also HELD over the whole range (0 candidates,
  0 still zero at depth 2,000; 17 at every width from 18 to 34). The widths 18 to 32 reproduce the first run exactly
  (13, 42, 161, 570, 2,354, 9,479, 37,644 and 150,578 halves reaching 17), so a second machine agrees; the count
  reaching 17 keeps growing by 4.00 per two cells (601,991 / 150,578). So no finite configuration whose right half
  has at most 34 cells (and left half at most 108) has a column 0 that is 0101... for ever.
"""
import pathlib, re, subprocess, sys, tempfile
from collections import defaultdict

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
sys.argv = _argv
WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 32
WS = list(range(18, WMAX + 1, 2))
NPROC = int(sys.argv[2]) if len(sys.argv) > 2 else 3
TAILMIN = 30
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def longest_zero_run(L):
    best = run = 0
    for b in L:
        run = 0 if b else run + 1
        best = max(best, run)
    return best


def scan(exe, W):
    procs = [subprocess.Popen([str(exe), "scan", str(W), str(k), str(NPROC), str(TAILMIN)], stdout=subprocess.PIPE,
                              text=True) for k in range(NPROC)]
    M, cands = defaultdict(int), []
    for p in procs:
        out = p.communicate()[0]
        for n, c in re.findall(r"^M \d+ (\d+) (\d+)$", out, re.M):
            M[int(n)] += int(c)
        cands += [(int(R), int(t)) for R, t in re.findall(r"^C \d+ (\d+) (\d+)$", out, re.M)]
    return M, cands


def main():
    exe = pathlib.Path(tempfile.mkdtemp()) / "realruns"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "realruns.c")], check=True)
    M12, _ = scan(exe, 12)
    tau = [t % 2 for t in range(130)]
    ref = defaultdict(int)
    for R in range(1, 1 << 12):
        ref[longest_zero_run(r30.forced_left(R, tau, 126))] += 1
    report("SC0 the scan agrees with an independent Python computation at W = 12", dict(M12) == dict(ref),
           f"C {sorted(M12.items())[-4:]} vs Python {sorted(ref.items())[-4:]}")
    zmax, allc = {}, []
    for W in WS:
        M, cands = scan(exe, W)
        zmax[W] = max(n for n, c in M.items() if c)
        allc += [(W, R, t) for R, t in cands]
        print(f"   W {W}: {sum(M.values())} right halves; longest zero run in L(1..126) {zmax[W]} "
              f"(halves reaching it: {M[zmax[W]]}); candidates ending in >= {TAILMIN} zeros: {len(cands)}", flush=True)
    survivors = []
    for W, R, t in allc:
        L = r30.forced_left(R, [t % 2 for t in range(2002)], 2000)
        first = next((i + 1 for i in range(126, 2000) if L[i]), None)       # first one deeper than 126
        if first is None:
            survivors.append((W, R))
        print(f"   candidate W {W} R {R}: tail {t} at depth 126; next one at depth {first}", flush=True)
    if survivors:
        print(f"   *** CANDIDATES STILL ZERO AT DEPTH 2000: {survivors} -- examine further ***", flush=True)
    verdict("SC1 no right half up to WMAX cells ends in 30 or more zeros at depth 126", not allc,
            f"{len(allc)} candidates, {len(survivors)} still zero at depth 2,000")
    verdict("SC2 the plateau: at most 3 cells of growth from W = 18, and at most 22",
            zmax[WS[-1]] - zmax[WS[0]] <= 3 and zmax[WS[-1]] <= 22, ", ".join(f"W {W}: {zmax[W]}" for W in WS))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
