#!/usr/bin/env python3
"""rule30_records.py: lead 1. The longest zero run of the forced left half from each depth, over every column 1,
for column 0 = 0101..., deeper than before; and the record witnesses, for a renormalisation.

RUN-ON:     cpu (records.c, C99 with OpenMP, driven from Python 3)
COMMAND:    python3 tests/probes/lexicon/rule30_records.py [DMAX=61] [THREADS=all]   (Cloud: depths 1 .. DMAX, and 65)
            python3 tests/probes/lexicon/rule30_records.py local [THREADS=all]           (JOB M4, below)
COST:       Cloud: about an hour on 4 cores (depths 60, 61 and 65 dominate: 2^30, 2^30 and 2^32 prefixes, at 1.7 us
            each per core).

Lead 1 (PRIZE-PROBLEMS.md, open leads of 2026-10-05). Conjecture LR for the word 01 (section 7) says that for every
column 1 the forced left half has infinitely many ones; it alone implies period 2 for every finite configuration.
A proof needs a growth bound: a run of zeros starting at depth d ends by about 2d. The record runs known so far, with
column 1 free (rule30_witness.py, rule30_ladder_deep.py's R(0, s)): 9 cells from depth 9, 17 from 13, 33 from 33,
37 from 41. The coin-model reading (section 8.14): with column 1 free a zero cell costs half a bit, and the best of
2^(d/2) prefixes lasts about d cells, ending near 2d. The self-similar end points (16, 28 to 30, 64 to 68) suggested a
renormalisation, a rule turning a record at depth d into one at depth 2d; a first look found none.
records.c computes the exact record from any depth d (anti-diagonal recurrence, a running XOR by log-shifts; see its
header) about a thousand times faster than the Python search, with the histogram of each prefix's own longest run and
up to 64 record witnesses (column 1's visible bits to the end of the run).

PREDICTIONS, written 2026-10-05 before this script's first run. Seen before: records.c on depths 9, 13, 33 and 41
only (the known values: 9, 17, 33, 37; 1, 3 and 21 record prefixes at 9, 13, 33; 12 at 41), with its timing.
  RC0 (controls): records.c reproduces the known records at depths 9, 13, 33 and 41 and their record-prefix counts at
      9, 13 and 33; and it equals the Python search of rule30_witness.py (an independent implementation of the same
      definition) at every depth from 1 to 29, record and record-prefix count alike.
  RC1 (blind; the doubling law): for every depth d from 42 to DMAX (61), and 65, the record R(d) lies between 0.75 d
      and 1.35 d.
  RC2 (blind): the record runs end near twice their depth: d + R(d) between 1.75 d and 2.35 d for every such d.
  RC3 (blind; half a bit per cell): at depths 57 and 65, the number of prefixes whose own run is at least r falls,
      over the histogram's tail (from its median run up to R - 2), by 0.4 to 0.6 bits per cell (least squares).
  RC4 (blind): early bits do not matter: at depth 65 at least 64 prefixes reach the record.
  RC5 (blind; the renormalisation, expected null): no visible self-similarity. For each d from 21 to 30, the longest
      common factor of the first record witnesses at d and at 2d (lengths m and n, in visible bits) is at most
      log2(m n) + 6, which two random words exceed about one time in 64.
REFUTED-BY: RC0 failing (the instrument); RC1 to RC5 failing.

---------------------------------------------------------------------------------------------------------------
JOB M4 (Cloud wrote, 2026-10-05; for Local; CLOUD-LOCAL.md lead M4). The records at depths 69, 73 and 77 (and, if the
machine can be left for two days, 81), beyond what Cloud's four cores can do in a session.
RUN-ON:     cpu, the machine with the most cores (records.c is OpenMP; it scales linearly)
COMMAND:    python3 tests/probes/lexicon/rule30_records.py local [THREADS]
            (or by hand: cc -O2 -fopenmp -o /tmp/records tests/probes/lexicon/records.c && /tmp/records 73 10)
COST:       per core, about 2 hours at depth 65, then 16 times more every 8 depths: about 8 h at 69, 32 h at 73,
            128 h at 77 and 21 days at 81, divided by the number of cores. Depth 89 needs a GPU port (about 16
            times 81).
PREDICTIONS (written 2026-10-05 before any run of this job, and before Cloud's own run of depths 42 to 65):
  M4a (blind): RC1 and RC2 hold at every depth run: 0.75 d <= R(d) <= 1.35 d, and 1.75 d <= d + R(d) <= 2.35 d.
  M4b (blind): the record never falls by more than 6 cells from one depth run to the next one run.
HAND-BACK: commit the printed "R", "H" and "W" lines for each depth to tests/probes/lexicon/rule30_records_local.txt
(the script writes it), add a row to CLOUD-LOCAL.md's ledger with the machine, cores and wall time, and push to main as
CLOUD-LOCAL step 4 says. Cloud will record the verdicts in this header.
"""
import importlib.util, math, os, pathlib, subprocess, sys, tempfile
from multiprocessing import Pool

HERE = pathlib.Path(__file__).resolve().parent
LOCAL = len(sys.argv) > 1 and sys.argv[1] == "local"
_nums = [a for a in sys.argv[1:] if a != "local"]
DMAX = int(_nums[0]) if _nums and not LOCAL else 61
THREADS = int(_nums[-1]) if (LOCAL and _nums) or len(_nums) > 1 else (os.cpu_count() or 1)
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def build():
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_records"
    subprocess.run(["cc", "-O2", "-fopenmp", "-o", str(exe), str(HERE / "records.c")], check=True)
    return exe


def run(exe, d):
    out = subprocess.run([str(exe), str(d), str(THREADS)], check=True, capture_output=True, text=True).stdout
    R = count = None
    hist, wits = {}, []
    for line in out.split("\n"):
        f = line.split()
        if not f:
            continue
        if f[0] == "R":
            R, count = int(f[2]), int(f[3])
        elif f[0] == "H":
            hist[int(f[2])] = int(f[3])
        elif f[0] == "W":
            wits.append(f[2])
    return R, count, hist, wits, out


def python_search():
    spec = importlib.util.spec_from_file_location("wt", HERE / "rule30_witness.py")
    wt = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, [sys.argv[0], "01", "1", "1"]
    spec.loader.exec_module(wt)
    sys.argv = argv
    return wt


_WT = None


def py_record(d):
    global _WT
    if _WT is None:
        _WT = python_search()
    wt = _WT
    zeros_before = len([t for t in range(d - 1) if t % 2 == 0])
    res = [wt.best_with_witness((d, c)) for c in range(1 << zeros_before)]
    m = max(r[0] for r in res)
    return d, m, sum(1 for r in res if r[0] == m)


def tail_slope(hist):
    """Bits lost per cell over the tail: log2 of #prefixes with run >= r, from the median run to R - 2."""
    R = max(hist)
    total = sum(hist.values())
    cum, acc = {}, 0
    for r in sorted(hist, reverse=True):
        acc += hist[r]
        cum[r] = acc
    surv = lambda r: sum(v for k, v in hist.items() if k >= r)
    med = next(r for r in sorted(hist) if surv(r) <= total / 2)
    xs = [r for r in range(med, R - 1) if surv(r) > 0]
    ys = [math.log2(surv(r)) for r in xs]
    if len(xs) < 3:
        return float("nan")
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return -sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def lcf(a, b):
    """Length of the longest common factor (substring) of two strings."""
    best, prev = 0, [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    return best


def main():
    exe = build()
    if LOCAL:
        lines = []
        for d in (69, 73, 77, 81):
            R, count, hist, wits, out = run(exe, d)
            print(f"   depth {d}: record {R} (ends at {d + R}), {count} record prefixes", flush=True)
            lines.append(out)
            (HERE / "rule30_records_local.txt").write_text("".join(lines))
        return
    known = {9: (9, 1), 13: (17, 3), 33: (33, 21), 41: (37, None)}
    res = {}
    for d in list(range(1, DMAX + 1)) + [65]:
        R, count, hist, wits, _ = run(exe, d)
        res[d] = (R, count, hist, wits)
        if d % 8 == 1 or d > DMAX - 8:
            print(f"   depth {d}: record {R} (ends at {d + R}), {count} record prefixes", flush=True)
    with Pool(THREADS) as pool:
        py = {d: (m, c) for d, m, c in pool.map(py_record, range(1, 30))}
    ok_known = all(res[d][0] == R and (c is None or res[d][1] == c) for d, (R, c) in known.items())
    ok_py = all(res[d][:2] == py[d] for d in py)
    report("RC0 known records reproduced; equal to the Python search at depths 1 to 29", ok_known and ok_py,
           f"known {ok_known}; Python {ok_py}")
    print("   records R(d), d = 1 .. DMAX: " + ", ".join(f"{d}:{res[d][0]}" for d in res), flush=True)
    ds = [d for d in res if d >= 42]
    r1 = [d for d in ds if not 0.75 * d <= res[d][0] <= 1.35 * d]
    verdict("RC1 the doubling law: 0.75 d <= R(d) <= 1.35 d for d >= 42", not r1, f"exceptions {r1}")
    r2 = [d for d in ds if not 1.75 * d <= d + res[d][0] <= 2.35 * d]
    verdict("RC2 the records end between 1.75 d and 2.35 d", not r2, f"exceptions {r2}")
    sl = {d: tail_slope(res[d][2]) for d in (57, 65) if d in res}
    verdict("RC3 the tail falls by 0.4 to 0.6 bits per cell at depths 57 and 65",
            all(0.4 <= v <= 0.6 for v in sl.values()) and len(sl) == 2,
            ", ".join(f"{d}: {v:.3f}" for d, v in sl.items()))
    if 65 in res:
        verdict("RC4 at least 64 prefixes reach the record at depth 65", res[65][1] >= 64, f"{res[65][1]}")
    common, over = {}, []
    for d in range(21, 31):
        if d in res and 2 * d in res and res[d][3] and res[2 * d][3]:
            a, b = res[d][3][0], res[2 * d][3][0]
            common[d] = (lcf(a, b), math.log2(len(a) * len(b)) + 6)
            over += [d] if common[d][0] > common[d][1] else []
    verdict("RC5 no visible self-similarity: common factors of the witnesses at d and 2d within log2(m n) + 6",
            not over, ", ".join(f"{d}:{v}/{lim:.1f}" for d, (v, lim) in common.items()))
    out = [f"R {d} {res[d][0]} {res[d][1]} ; W " + " ".join(res[d][3][:4]) for d in res]
    (HERE / "rule30_records_cloud.txt").write_text("\n".join(out) + "\n")
    print("   wrote rule30_records_cloud.txt (records, record-prefix counts, up to 4 witnesses per depth)")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
