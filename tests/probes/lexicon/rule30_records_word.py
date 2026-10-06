#!/usr/bin/env python3
"""rule30_records_word.py: conjecture LR for the words that leave column 1 almost free. The exact record zero run
R_w(d) of the forced left half, over every column 1, for the wall words 0001 and 00001, far deeper than
rule30_rigidity.py reached (14 free bits). The small item of RULE30-PRIZE.md section 7 ("whether LR holds for long
words that are mostly zeros"), listed on PERIOD-TWO.md's board. (Local, 2026-10-06; section 8.60; engine
records_word.c.)

RUN-ON:     cpu, every core (records_word.c is OpenMP; needs the libomp flags of ompflags.py on macOS)
COMMAND:    python3 tests/probes/lexicon/rule30_records_word.py [THREADS=8]
COST:       about 15 minutes at the defaults (the deepest point has 35 free bits).

WHY. With column 0 = w periodic, column 1 is free at the times where w is 0 and invisible where w is 1 (Lemma 1,
section 8.2). A word with z zeros per period p leaves z/p free bits per cell of the left half, and the forced
cells (where w(k-1) = 1) are its only conditions: (p - z)/p of the cells. The coin model of section 8.38 then
says R_w(d) grows like (z / (p - z)) d, less a merging loss: for 0101 the measured law is 0.826 d + 0.8 against
the coin's 1.0 d. For 0001, z/(p-z) = 3; for 00001, 4. These words are "where LR is most at risk" (section 7, R5).

SEEN BEFORE these predictions: the engine's build and controls (R(01, d) = 1, 6, 5, 2, 9, 17, 14, 20, 20, 38, 42 at
d = 1, 2, 3, 8, 9, 13, 20, 24, 30, 40, 46, all equal to rule30_records_cloud.txt; the word 0 caps; the word 1 gives
1). rule30_rigidity.py's recorded ranges from 2026-10-04 (14 free bits): the longest run over admissible depths is
54 to 58 for the rotations of 0001 and 45 to 66 for those of 00001. Nothing of 0001 or 00001 beyond that.

PREDICTIONS, written 2026-10-06 before this script's first run.
  W0 (control, must hold): R(01, d) equals the record file rule30_records_cloud.txt at every depth 1 to 61.
  W1 (control, must hold): the word 0 reaches the cap from every depth 1 to 6 (the search can see an infinite
      run); the word 1 gives 1 at every depth 1 to 12.
  W2 (cross-check against rule30_rigidity.py, must hold): for each rotation of 0001, the largest R over the depths
      with at most 14 free bits lies in [54, 58]; for each rotation of 00001, in [45, 66].
  W3 (LR, must hold on the conjecture): no run reaches the cap (253) at any depth run: 0001 at d = 8, 12, ..., 44
      and 00001 at d = 10, 15, ..., 45.
  W4 (blind): the growth is linear, not faster: R_w(d) / d at the deepest point is at most R_w(d) / d at d = 24
      (0001) or d = 25 (00001) plus 0.2.
  W5 (blind; the slope): a least-squares line through the points with d >= 24 (0001) or d >= 25 (00001) has slope
      in [2.3, 3.1] for 0001 and in [3.0, 4.2] for 00001 (the coin's 3 and 4, less a merging loss of up to a
      quarter).
  W6 (blind): R_w(d) < 4 d for 0001 and < 5 d for 00001 at every depth run.
  CF  (counterfactual, must fail): the word 0 is "excluded" in the sense of W3: its runs must reach the cap.
REFUTED-BY: W0, W1, W2 or CF failing (the engine or the harness); W3 failing is the result of the year (a column 1
  that keeps the left half zero: follow it deeper before anything else); W4 to W6 the other way.

OUTCOME of the first run, 2026-10-06 (8 threads, 32 minutes beside two other jobs; results in rule30_records_word.txt):
  W0 PASSED (62 depths). W1 FAILED on its wording: the word 1 gives the universal fibre, R = 1 from odd depths and
  0 from even ones (rigidity's R3 says "the longest run is 1", which is the maximum over depths; my control said "1 at
  every depth"). CF PASSED (the word 0 caps). W2 FAILED by 2 for one rotation: 0001: 54, 0010: 52, 0100: 58, 1000: 56
  (the prose said 54 to 58); 00001: 45, 66, 64, 48, 53 (the prose's 45 to 66). A rerun of rule30_rigidity.py (14 free
  bits, 4 jobs, 12 minutes) gave exactly 54, 52, 58, 56 for the rotations of 0001: the two implementations agree.
  R(0001, d) at d = 8, 12, ..., 44: 24, 28, 32, 52, 52, 80, 76, 84, 96, 100 (from 2^33 prefixes at 44).
  R(00001, d) at d = 10, 15, ..., 45: 35, 45, 50, 85, 85, 105, 115, 130 (from 2^36 prefixes at 45).
  W3 HELD: no cap. W4 HELD (R/d at 44 is 2.27 against 2.17 at 24; at 45 is 2.89 against 3.40 at 25). W5 REFUTED: the
  slopes are 2.11 (0001) and 2.40 (00001), below the bands [2.3, 3.1] and [3.0, 4.2]: the record's share of the coin's
  slope falls with freedom (0.83 for 0101, 0.70, 0.60). W6 HELD. The histograms show the forced cells very nearly
  halving the survivors, not exactly: from depth 45 with 00001, 34,359,738,788 of 2^36 end at run 0 (half is
  34,359,738,368), 17,175,829,450 at run 5 (a quarter is 17,179,869,184). I first wrote "exactly"; GPT corrected
  it from the file (CHAT-LEDGER.md C008).
"""
import pathlib, subprocess, sys, tempfile
from ompflags import OMP

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "rule30_records_word.txt"
THREADS = sys.argv[1] if len(sys.argv) > 1 else "8"
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def build():
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_records_word"
    arch = ["-mcpu=apple-m1"] if sys.platform == "darwin" else []
    subprocess.run(["cc", "-O3", *arch, *OMP, "-o", str(exe), str(HERE / "records_word.c")], check=True)
    return exe


def run(exe, word, d, split=12, record=True):
    out = subprocess.run([str(exe), word, str(d), THREADS, str(split)], capture_output=True, text=True,
                         check=True).stdout
    if record:
        with open(OUT, "a") as fh:
            fh.write(out)
    first = out.splitlines()[0]
    r = int(first.split("=")[1].split()[0])
    return r, "CAPPED" in first, first


def nfree(word, d):
    return sum(1 for t in range(d - 1) if word[t % len(word)] == "0")


def rotations(word):
    return sorted({word[i:] + word[:i] for i in range(len(word))})


def main():
    exe = build()
    known = {}
    for ln in (HERE / "rule30_records_cloud.txt").read_text().splitlines():
        if ln.startswith("R "):
            f = ln.split()
            known[int(f[1])] = int(f[2])
    bad = [d for d in range(1, 62) if d in known and run(exe, "01", d, record=False)[0] != known[d]]
    report("W0 R(01, d) equals the record file at depths 1 to 61", not bad, f"{len(known)} depths, bad {bad}")
    ok1 = all(run(exe, "0", d, record=False)[1] for d in range(1, 7))
    ok1 &= all(run(exe, "1", d, record=False)[0] == 1 for d in range(1, 13))
    report("W1 the word 0 caps from every depth 1 to 6; the word 1 gives 1", ok1)
    report("CF  the word 0 reaches the cap (it must: its left half can be all zero)",
           all(run(exe, "0", d, record=False)[1] for d in range(1, 7)))
    ok2, notes = True, []
    for word, lo, hi in (("0001", 54, 58), ("00001", 45, 66)):
        for rot in rotations(word):
            depths = [d for d in range(2, 40) if nfree(rot, d) <= 14]
            best = max(run(exe, rot, d, record=False)[0] for d in depths)
            ok2 &= lo <= best <= hi
            notes.append(f"{rot}: {best} (depths to {depths[-1]})")
    report("W2 the largest R over depths with at most 14 free bits, per rotation, lies in rigidity's range", ok2,
           "; ".join(notes))

    results = {}
    capped = False
    for word, depths in (("0001", list(range(8, 45, 4))), ("00001", list(range(10, 46, 5)))):
        results[word] = []
        for d in depths:
            r, c, line = run(exe, word, d)
            capped |= c
            results[word].append((d, r))
            print(f"   {line}", flush=True)
    report("W3 no run reaches the cap at any depth run (LR holds there)", not capped)
    held4 = held5 = held6 = True
    for word, d0, slo, shi, mult in (("0001", 24, 2.3, 3.1, 4), ("00001", 25, 3.0, 4.2, 5)):
        pts = results[word]
        r0 = dict(pts)[d0]
        dl, rl = pts[-1]
        held4 &= rl / dl <= r0 / d0 + 0.2
        late = [(d, r) for d, r in pts if d >= d0]
        n = len(late); sx = sum(d for d, _ in late); sy = sum(r for _, r in late)
        sxx = sum(d * d for d, _ in late); sxy = sum(d * r for d, r in late)
        slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
        held5 &= slo <= slope <= shi
        held6 &= all(r < mult * d for d, r in pts)
        print(f"   {word}: R/d at {d0}: {r0 / d0:.2f}, at {dl}: {rl / dl:.2f}; slope from {d0}: {slope:.3f}", flush=True)
    verdict("W4 linear, not faster: R/d at the deepest point <= R/d at 24 or 25, plus 0.2", held4)
    verdict("W5 slopes in [2.3, 3.1] (0001) and [3.0, 4.2] (00001)", held5)
    verdict("W6 R < 4d (0001) and R < 5d (00001) throughout", held6)
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
