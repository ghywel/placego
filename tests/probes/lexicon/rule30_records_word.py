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

# ADDENDUM, written 2026-10-06 before the second run (python3 rule30_records_word.py [THREADS] holes), after the owner's
# morning question (section 8.62): the walls nearest Condrey's constant wall are those with ONE white cell per period,
# 0 1^(p-1), which leave column 1 one free bit per p steps. They are the least free walls there are, and rigidity
# (section 7, R5) found them the most rigid. The coin model says R_w(d) grows like d / (p - 1).
#   H0 (control, must hold): for 0111 the largest R over the depths with at most 14 free bits is 19 (rule30_rigidity.py's
#       R5 line: "0111: 19 (from depth 31)").
#   H1 (LR, must hold on the conjecture): no run reaches the cap (509) for the words 011, 0111, ..., 01111111 at the
#       depths run (four depths each, the deepest with 32 free bits).
#   H2 (blind; the slope): for each word, the slope of R_w(d) between its two deepest points lies within
#       [0.7, 1.3] / (p - 1): the record keeps between 70% and 130% of the coin's share, unlike the free words, where
#       the share fell to 0.60.
#   H3 (blind; the law): R_w(d) <= 1.5 d / (p - 1) + 10 at every depth run.
#   CF (counterfactual, must fail): the word 1 (Condrey's wall, no free bit) has R = 1 from some depth: it must not
#       exceed 1 (and does not); the word 0 must cap. (Both known; kept as the harness's ends of the scale.)
# REFUTED-BY: H0 or CF failing (the engine); H1 failing is the result of the year; H2, H3 the other way.
# OUTCOME of the second run, 2026-10-06 (holes; 8 threads, 10 minutes; lines in rule30_records_word.txt): H0 PASSED (19),
# CF PASSED. H1 HELD: no cap at any of the 24 points (the deepest, 32 free bits, at depths 96 to 256). H3 HELD.
# H2 REFUTED: the two-point slopes are 1.00, 1.59, 0.60, 0.94, 0.64, 0.98 of the coin's, noise of small numbers;
# R/d at the deepest point is 0.81, 1.01, 0.75, 0.83, 0.83, 0.85 of the coin's 1/(p-1) for p = 3 to 8: the rigid
# side keeps about 0.8 of the coin, like 0101 (0.83), unlike the free side (0.70, 0.60). Section 8.62.
from ompflags import OMP

# SECOND ADDENDUM, written 2026-10-06 before the third run (python3 rule30_records_word.py [THREADS] slow), after the
# owner asked what the next step after Condrey's period 1 would have been without period 2 (section 8.63). Walls
# 0^a 1^b with a = b have the same freedom as 0101 (one half) and a switch density 2/(2a) instead of 1: the only thing
# that changes along a = 2, 4, 8, 16 is how long each stretch lasts. Next to a black stretch of r steps the forced
# left half is the checkerboard to depth r - 1 whatever column 1 is (Lemma 1); next to a white stretch column -1
# copies column 1. So the question is whether long stretches change the record's law, which for 0101 is 0.83 d.
#   SW0 (control, must hold): a = 1 is the 0101 wall: R(01, d) at d = 24, 32, 40, 48 equals the record file.
#   SW1 (LR, must hold on the conjecture): no run reaches the cap for a = 2, 4, 8, 16 at depths 8, 16, 24, 32, 40, 48
#       (free bits = d/2, so 24 at the deepest).
#   SW2 (blind): switch density matters: R/d at d = 48 falls with a, and at a = 16 it is below 0.60 (against 0.83
#       for 0101 and the coin's 1.0), because the checkerboard stretches admit no zeros.
#   SW3 (blind; the law's shape): at a = 16 the record from depth d is at most the longest white stretch's reach
#       plus a constant: R <= 2a + 12 at every depth run (the run cannot cross a black stretch's checkerboard).
# REFUTED-BY: SW0 failing (the engine); SW1 failing is the result of the year; SW2, SW3 the other way.
# OUTCOME of the third run, 2026-10-06 (slow; 8 threads, 7 minutes): SW0, SW1 PASSED. R at depths 8 .. 48: a = 2:
# see rule30_records_word.txt; R/d at 48 is 0.812, 0.812, 0.667, 0.792 for a = 2, 4, 8, 16. SW2 REFUTED (no fall
# with a; 0.79 at a = 16, not below 0.60). SW3 HELD (max 38 <= 44). Freedom, not switch density, sets LR's law.

# THIRD ADDENDUM, written 2026-10-06 before the fourth run (python3 rule30_records_word.py [THREADS] r210): Rule 210,
# x' = l xor (not c and r), the one other nonlinear left-permutive rule with a quiescent white background (section 8.64).
# records_word.c -DRULE210 replaces the inverse rule's OR by an AND-NOT; everything else is the same search.
# SEEN BEFORE these predictions (exploratory, 2026-10-06 09:35): the engine reported every prefix reaching the cap at
# depths 8, 16, 24 next to 0101, and an independent greedy computation in Python confirmed zero runs of 112 cells from
# depth 8 for all 16 prefixes, and found a column 1 (1011 0000 1111 1111 then zeros at the even times) whose forced left
# half is EMPTY at time 0. A search of two-sided configurations of width <= 16 found none with centre 0101 for 300 steps.
#   Z0 (control, must hold): the Rule 30 build is unchanged: R(01, d) at d = 8, 24, 46 equals the record file.
#   Z1 (must hold, given the exploratory finding): for Rule 210 next to 0101, every prefix reaches the cap at depths
#       8, 16, 24 and 32 (LR is false for Rule 210 at period 2).
#   Z2 (blind): at depth 1 as well, every prefix reaches the cap: there is no depth at which the forced cells bite.
#   Z3 (blind; B for Rule 210 to width 20): no two-sided configuration with the wall at its left end and a right half of
#       width at most 20 keeps the centre column 0101... for 300 steps.
#   CF (counterfactual, must fail): the Rule 210 build with the wall word 1 (Condrey's black wall) also reaches the cap.
#       It must not: its forced left half is the all-black fibre, R = 0.
# REFUTED-BY: Z0 or CF failing (the engine); Z1, Z2, Z3 the other way.
# OUTCOME of the fourth run, 2026-10-06 (r210; seconds): Z0, Z1, CF PASSED; Z2 HELD (the cap from depth 1); Z3 HELD (no right
# half of width <= 20 keeps the centre 0101 for 300 steps; most die within a few steps). LR is false for Rule 210 at
# period 2; B for Rule 210 is open to width 20.



HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "rule30_records_word.txt"
THREADS = next((a for a in sys.argv[1:] if a.isdigit()), "8")
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


def holes(exe):
    hist = {}
    rot_best = max(run(exe, "0111", d, record=False)[0] for d in range(2, 60) if nfree("0111", d) <= 14)
    report("H0 for 0111 the largest R over depths with at most 14 free bits is 19", rot_best == 19, f"{rot_best}")
    cf_ok = all(run(exe, "0", d, record=False)[1] for d in (1, 2, 3)) and \
        max(run(exe, "1", d, record=False)[0] for d in range(1, 9)) == 1
    report("CF  the word 0 caps and the word 1 never exceeds 1 (the ends of the scale)", cf_ok)
    capped, h2, h3, notes = False, True, True, []
    for p_ in range(3, 9):
        word = "0" + "1" * (p_ - 1)
        depths = [8 * p_, 16 * p_, 24 * p_, 32 * p_]
        pts = []
        for d in depths:
            r, c, line = run(exe, word, d)
            capped |= c
            pts.append((d, r))
            print(f"   {line}", flush=True)
        (d1, r1), (d2, r2) = pts[-2], pts[-1]
        slope = (r2 - r1) / (d2 - d1)
        h2 &= 0.7 / (p_ - 1) <= slope <= 1.3 / (p_ - 1)
        h3 &= all(r <= 1.5 * d / (p_ - 1) + 10 for d, r in pts)
        notes.append(f"{word}: slope {slope:.3f} = {slope * (p_ - 1):.2f} of the coin's; R/d at {d2}: {r2 / d2:.3f}")
    for n in notes:
        print("   " + n, flush=True)
    report("H1 no run reaches the cap", not capped)
    verdict("H2 each slope within [0.7, 1.3] of the coin's 1/(p-1)", h2)
    verdict("H3 R <= 1.5 d/(p-1) + 10 throughout", h3)
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def slow(exe):
    known = {}
    for ln in (HERE / "rule30_records_cloud.txt").read_text().splitlines():
        if ln.startswith("R "):
            f = ln.split(); known[int(f[1])] = int(f[2])
    ok0 = all(run(exe, "01", d, record=False)[0] == known[d] for d in (24, 32, 40, 48))
    report("SW0 a = 1 is the 0101 wall: R(01, d) at d = 24, 32, 40, 48 equals the record file", ok0)
    capped, rows = False, {}
    for a in (2, 4, 8, 16):
        word = "0" * a + "1" * a
        rows[a] = []
        for d in (8, 16, 24, 32, 40, 48):
            r, c, line = run(exe, word, d)
            capped |= c
            rows[a].append((d, r))
            print(f"   {line}", flush=True)
    report("SW1 no run reaches the cap", not capped)
    ratio = {a: rows[a][-1][1] / rows[a][-1][0] for a in rows}
    print("   R/d at 48: " + ", ".join(f"a = {a}: {ratio[a]:.3f}" for a in rows), flush=True)
    verdict("SW2 R/d at 48 falls with a and is below 0.60 at a = 16",
            all(ratio[x] >= ratio[y] for x, y in ((2, 4), (4, 8), (8, 16))) and ratio[16] < 0.60)
    verdict("SW3 at a = 16, R <= 2a + 12 = 44 at every depth run", all(r <= 44 for d, r in rows[16]),
            f"max {max(r for d, r in rows[16])}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def r210():
    exe = build()
    arch = ["-mcpu=apple-m1"] if sys.platform == "darwin" else []
    exe210 = pathlib.Path(tempfile.gettempdir()) / "rule30_records_word_210"
    subprocess.run(["cc", "-O3", *arch, *OMP, "-DRULE210", "-o", str(exe210), str(HERE / "records_word.c")], check=True)
    known = {}
    for ln in (HERE / "rule30_records_cloud.txt").read_text().splitlines():
        if ln.startswith("R "):
            f = ln.split(); known[int(f[1])] = int(f[2])
    report("Z0 the Rule 30 build is unchanged at d = 8, 24, 46", all(run(exe, "01", d, record=False)[0] == known[d] for d in (8, 24, 46)))
    caps = [run(exe210, "01", d, record=False)[1] for d in (8, 16, 24, 32)]
    report("Z1 Rule 210 next to 0101: every prefix reaches the cap at depths 8, 16, 24, 32 (LR is false for 210)", all(caps))
    verdict("Z2 from depth 1 as well", run(exe210, "01", 1, record=False)[1])
    report("CF  Rule 210 with the wall word 1 gives R = 0, not the cap", run(exe210, "1", 6, record=False)[0] == 0)
    # Z3: two-sided configurations, the wall at the left end, right halves of width <= 20, 300 steps
    def step210(x, mask):
        return ((x >> 1) ^ ((~x) & (x << 1))) & mask
    found = None
    mask = (1 << 1000) - 1
    for w in range(1, 21):
        for right in range(1 << (w - 1), 1 << w):      # the right half occupies cells 1 .. w, its last cell black
            x = right << 401                                # the centre is bit 400, white at time 0
            ok = True
            for t in range(1, 300):
                x = step210(x, mask)
                if (x >> 400) & 1 != t % 2:
                    ok = False; break
            if ok:
                found = (w, right); break
        if found:
            break
    verdict("Z3 no right half of width <= 20 keeps the centre 0101 for 300 steps (B for Rule 210 to width 20)",
            found is None, f"{found}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def main():
    if "r210" in sys.argv[1:]:
        r210()
        return
    exe = build()
    if "holes" in sys.argv[1:]:
        holes(exe)
        return
    if "slow" in sys.argv[1:]:
        slow(exe)
        return
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
