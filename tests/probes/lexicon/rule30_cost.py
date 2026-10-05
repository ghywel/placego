#!/usr/bin/env python3
"""rule30_cost.py: what the seed's right part pays per condition, position by position (RULE30-PRIZE.md section
8.52; the cost side of PERIOD-TWO.md section 7, question 1).

RUN-ON:     cpu (Python 3 and a C compiler; count_j.c counts; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_cost.py [WMAX=22] [windows | deep | phases]
COST:       under a minute on one core.

Background (section 8.51). N_{w,j}(T) counts the configurations of exact hull width w whose column 0, at distance j
from the hull's left end, reads 0101... (either phase) at times 0 .. T-1. The lemma of section 8.51: for T <= j the
count halves exactly at every step (the seed's left part pays one bit per condition, by left-permutivity). From
T = j on, every condition must be paid by the right part. The step ratio rho(w, j, T) = N_{w,j}(T+1) / N_{w,j}(T)
for T >= j is what the right part pays. If it is bounded below 1 at every single step, the cost side is a per-step
statement, the kind an induction proves; if not, it holds only on average.

PREDICTIONS, written 2026-10-05 before this script's first run (word 0101..., both phases):
  CJ0 (control, must hold): summed over j, N_{w,j}(T) equals count.c's N_w(T) for w = 12 .. 18; and the lemma holds
      exactly: N_{w,j}(T) = N_{w,j}(1) / 2^(T-1) for every T <= j, every j, every w up to WMAX.
  CJ1 (blind; per step): for w = 16 .. WMAX, every j and every T >= j with N_{w,j}(T) >= 256, rho <= 0.75.
  CJ2 (blind; on average): the mean of log2 rho over those steps lies between -1.2 and -0.9.
  CJ3 (blind; not exact): at least one of those steps has rho above 0.55, so the right part's cost is not exactly
      one bit at every step.
  CJ4 (counterfactual, the word 0, which Condrey's theorem closes): over the same steps, the word 0's largest rho
      is at most 0101's largest rho.
REFUTED-BY: CJ0 failing (the instrument); CJ1 to CJ4 failing.

OUTCOME, 2026-10-05 (the first run, 3 seconds):
  CJ0 PASSED: the positions sum to count.c's totals, and the lemma of section 8.51 is exact at every w up to 22.
  CJ1 REFUTED: the right part does not pay at every step. Of 276 right-paid steps (w = 16 .. 22, N >= 256), 42 have
     rho of 0.95 or more, most exactly 1: free steps, where the condition is already implied by the earlier ones.
     46 have rho below 0.05: collapses. The rest spread between. Example, w = 22, j = 2: 1048576, 524288, 196608,
     65536, 65536, 65536, 12288.
  CJ2 HELD: the mean of log2 rho is -1.041. On average each right-paid condition costs a bit.
  CJ3 HELD (rho reaches 1).
  CJ4 HELD (both reach 1); the word 0's mean log2 rho is -1.632: its right part pays more per condition.
  So the cost side is not a per-step statement. A proof needs amortisation: a potential that free steps run up and
  collapses pay off. Mode windows asks whether that debt stays bounded.

MODE windows. For k = 1 .. 10, the worst k-step ratio N_{w,j}(T+k) / N_{w,j}(T) over right-paid windows (T >= j,
N_{w,j}(T) >= 256, w = 16 .. WMAX), and the longest run of consecutive free steps (rho >= 0.95).
PREDICTIONS for windows, written 2026-10-05 after the outcome above and before windows' first run:
  CW1 (blind): the longest run of consecutive free steps is at most 4, at every w from 16 to WMAX.
  CW2 (blind; bounded debt): log2 of the worst k-step ratio is at most 3 - 0.5 k for every k from 1 to 10.

OUTCOME of windows, 2026-10-05 (2 seconds):
  CW1 HELD: the longest run of consecutive free steps is 3 at every w from 16 to 22. It does not grow with w.
  CW2 HELD: log2 of the worst k-step ratio, k = 1 .. 10: 0, 0, 0, -1.30, -2.35, -2.85, -3.79, -8.35, -9.00, -inf.
     Any 4 consecutive right-paid conditions cost at least 1.3 bits, and any 8 at least 8.3, at every position
     and width measured (counts of 256 or more). The debt is bounded, as far as it can be counted.

MODE deep. The same at widths 16 .. 26, and the constant of the bounded-debt form: for alpha = 0.5,
c(w) = max over right-paid windows (T >= j, every count N_{w,j}(T) >= 1, k >= 1) of log2(N(T+k) / N(T)) + 0.5 k,
where windows that reach a zero count are left out (they satisfy any bound).
PREDICTIONS for deep, written 2026-10-05 after the windows outcome and before deep's first run:
  CD1 (blind): the longest run of free steps (counts >= 256) stays at most 3 at every w from 23 to 26.
  CD2 (blind; the constant): c(w) is at most 6 at every w from 16 to 26, and c(26) - c(16) is at most 1.

OUTCOME of deep, 2026-10-05 (15 seconds):
  CD1 HELD: the longest run of free steps is 3 at every w from 16 to 26.
  CD2 REFUTED: c(w) = 1.50 at most widths, but 3.00 at w = 17, 2.00 at 24 and 5.00 at 26 (c <= 6 held; the growth
     limit did not). The jumps come from small counts: a few survivors passing many conditions intact, the luck the
     coin model puts in a logarithm. At large counts the debt is bounded (CD1); at small counts it grows slowly with w.

MODE phases. Each phase of 0101 counted alone (words 0101... and 1010...), w = 16 .. 24, counts >= 256. A right-paid
step from T to T + 1 imposes the condition at time T, whose kind is set by the word's cell at T - 1: after a black
cell the condition involves the left half alone (section 8.40), and the newest right cell cannot pay (section 8.52).
PREDICTIONS for phases, written 2026-10-05 before phases' first run:
  CP1 (blind): at least 80% of the free steps (rho >= 0.95) are after a black cell.
  CP2 (blind): at least 60% of the collapses (rho < 0.05) are after a white cell.

OUTCOME of phases, 2026-10-05 (seconds): free steps 113 after black, 28 after white; collapses 108 after black, 26
  after white.
  CP1 HELD, just (80%).
  CP2 REFUTED (19%): collapses come after black cells too. After a black cell the condition is all or nothing: the
     left half, which is the same for the survivors of one position, decides it for all of them at once. The
     conditions after a white cell, which couple column 1 to the left half, are the ones that split the survivors.
"""
import math, pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 22
TMAX = 50
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def run(exe, wmin, wmax, word, per):
    out = subprocess.run([str(exe), str(wmin), str(wmax), str(TMAX), word, str(per)], check=True,
                         capture_output=True, text=True).stdout
    J, C = {}, {}
    for line in out.split("\n"):
        f = line.split()
        if f and f[0] == "J":
            J[(int(f[1]), int(f[2]), int(f[3]))] = int(f[4])
        elif f and f[0] == "C":
            C[(int(f[1]), int(f[2]))] = int(f[3])
    return J, C


def steps(J, wlo, whi):
    """(w, j, T, rho) for every right-paid step with N_{w,j}(T) >= 256."""
    out = []
    for (w, j, T), n in J.items():
        if wlo <= w <= whi and T >= max(j, 1) and n >= 256:
            out.append((w, j, T, J.get((w, j, T + 1), 0) / n))
    return out


def windows(exe):
    J, _ = run(exe, 16, WMAX, "01" * 200, 2)
    longest = {}
    for (w, j, T), n in J.items():
        if T >= max(j, 1) and n >= 256:
            k = 0
            while J.get((w, j, T + k), 0) >= 256 and J.get((w, j, T + k + 1), 0) / J[(w, j, T + k)] >= 0.95:
                k += 1
            longest[w] = max(longest.get(w, 0), k)
    print("   longest run of free steps by w: " + ", ".join(f"{w}: {k}" for w, k in sorted(longest.items())))
    verdict("CW1 at most 4 consecutive free steps", all(k <= 4 for k in longest.values()),
            f"largest {max(longest.values())}")
    worst = {}
    for (w, j, T), n in J.items():
        if T >= max(j, 1) and n >= 256:
            for k in range(1, 11):
                worst[k] = max(worst.get(k, 0.0), J.get((w, j, T + k), 0) / n)
    print("   worst k-step ratio, log2, k = 1 .. 10: "
          + " ".join(f"{math.log2(worst[k]):.2f}" if worst[k] > 0 else "-inf" for k in range(1, 11)))
    verdict("CW2 log2 worst k-step ratio <= 3 - 0.5 k", all(worst[k] == 0 or math.log2(worst[k]) <= 3 - 0.5 * k
                                                         for k in range(1, 11)),
            ", ".join(f"k = {k}: {math.log2(worst[k]):.2f}" for k in range(1, 11)
                      if worst[k] > 0 and math.log2(worst[k]) > 3 - 0.5 * k) or "all within")


def phases(exe):
    tally = {("free", "black"): 0, ("free", "white"): 0, ("collapse", "black"): 0, ("collapse", "white"): 0}
    for word in ("01" * 200, "10" * 200):
        J, _ = run(exe, 16, 24, word, 1)
        for (w, j, T), n in J.items():
            if T >= max(j, 1) and n >= 256:
                rho = J.get((w, j, T + 1), 0) / n
                kind = "black" if word[T - 1] == "1" else "white"
                if rho >= 0.95:
                    tally[("free", kind)] += 1
                elif rho < 0.05:
                    tally[("collapse", kind)] += 1
    print("   " + ", ".join(f"{a} after {b}: {c}" for (a, b), c in tally.items()))
    fb = tally[("free", "black")] / max(1, tally[("free", "black")] + tally[("free", "white")])
    cw = tally[("collapse", "white")] / max(1, tally[("collapse", "black")] + tally[("collapse", "white")])
    verdict("CP1 at least 80% of free steps after a black cell", fb >= 0.8, f"{100 * fb:.0f}%")
    verdict("CP2 at least 60% of collapses after a white cell", cw >= 0.6, f"{100 * cw:.0f}%")


def deep(exe):
    J, _ = run(exe, 16, 26, "01" * 200, 2)
    longest, cw = {}, {}
    for (w, j, T), n in J.items():
        if T < max(j, 1):
            continue
        if n >= 256:
            k = 0
            while J.get((w, j, T + k), 0) >= 256 and J.get((w, j, T + k + 1), 0) / J[(w, j, T + k)] >= 0.95:
                k += 1
            longest[w] = max(longest.get(w, 0), k)
        k = 1
        while J.get((w, j, T + k), 0) >= 1:
            cw[w] = max(cw.get(w, -99.0), math.log2(J[(w, j, T + k)] / n) + 0.5 * k)
            k += 1
    print("   longest run of free steps by w: " + ", ".join(f"{w}: {k}" for w, k in sorted(longest.items())))
    print("   c(w) for alpha = 0.5: " + ", ".join(f"{w}: {c:.2f}" for w, c in sorted(cw.items())))
    verdict("CD1 at most 3 free steps in a row at w = 23 .. 26", all(longest.get(w, 0) <= 3 for w in range(23, 27)),
            ", ".join(f"{w}: {longest.get(w, 0)}" for w in range(23, 27)))
    verdict("CD2 c(w) <= 6 at every w, and c(26) - c(16) <= 1",
            all(c <= 6 for c in cw.values()) and cw[26] - cw[16] <= 1, f"c(16) {cw[16]:.2f}, c(26) {cw[26]:.2f}, "
            f"largest {max(cw.values()):.2f}")


def main():
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_cost_c"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "count_j.c")], check=True)
    if len(sys.argv) > 2 and sys.argv[2] == "phases":
        phases(exe)
        return
    if len(sys.argv) > 2 and sys.argv[2] == "deep":
        deep(exe)
        return
    if len(sys.argv) > 2 and sys.argv[2] == "windows":
        windows(exe)
        return
    w01 = "01" * 200
    J, C = run(exe, 1, WMAX, w01, 2)
    ok_sum = all(sum(J.get((w, j, T), 0) for j in range(w)) == C[(w, T)] for w in range(12, 19) for T in range(1, TMAX))
    ok_lem = all(J.get((w, j, T), 0) * 2 ** (T - 1) == J.get((w, j, 1), 0)
                 for w in range(1, WMAX + 1) for j in range(w) for T in range(1, j + 1))
    report("CJ0 the positions sum to count.c's totals, and the lemma holds exactly for T <= j", ok_sum and ok_lem,
           f"sums {'agree' if ok_sum else 'DIFFER'}; lemma {'exact' if ok_lem else 'BROKEN'}")
    st = steps(J, 16, WMAX)
    worst = max(st, key=lambda s: s[3])
    mean = sum(math.log2(s[3]) for s in st if s[3] > 0) / len([s for s in st if s[3] > 0])
    print(f"   0101: {len(st)} right-paid steps with N >= 256; largest rho {worst[3]:.3f} at w, j, T = {worst[:3]};"
          f" mean log2 rho {mean:.3f}")
    hist = {}
    for s in st:
        b = min(int(s[3] * 20), 19) / 20
        hist[b] = hist.get(b, 0) + 1
    print("   0101: rho histogram (lower edge: count): " + ", ".join(f"{b:.2f}: {c}" for b, c in sorted(hist.items())))
    for w in (WMAX,):
        for j in (2, w // 2, w - 3):
            row = [J.get((w, j, T), 0) for T in range(1, TMAX)]
            print(f"   0101, w = {w}, j = {j}: N for T = 1 ..: " + " ".join(str(n) for n in row if n))
    verdict("CJ1 rho <= 0.75 at every right-paid step", worst[3] <= 0.75, f"largest {worst[3]:.3f} at {worst[:3]}")
    verdict("CJ2 mean log2 rho between -1.2 and -0.9", -1.2 <= mean <= -0.9, f"{mean:.3f}")
    verdict("CJ3 some step has rho above 0.55", worst[3] > 0.55, f"largest {worst[3]:.3f}")
    J0, _ = run(exe, 1, WMAX, "0" * 400, 1)
    st0 = steps(J0, 16, WMAX)
    w0 = max(st0, key=lambda s: s[3]) if st0 else (0, 0, 0, 0.0)
    m0 = sum(math.log2(s[3]) for s in st0 if s[3] > 0) / max(1, len([s for s in st0 if s[3] > 0]))
    print(f"   word 0: {len(st0)} right-paid steps; largest rho {w0[3]:.3f} at {w0[:3]}; mean log2 rho {m0:.3f}")
    verdict("CJ4 the word 0's largest rho is at most 0101's", w0[3] <= worst[3], f"{w0[3]:.3f} against {worst[3]:.3f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
