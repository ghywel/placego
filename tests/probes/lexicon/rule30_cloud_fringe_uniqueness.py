#!/usr/bin/env python3
"""rule30_cloud_fringe_uniqueness.py: are 11, 101, 1011, 10101, .. the only seeds with the single cell's centre column?

RUN-ON:     cpu (fringe_uniqueness.c via cc, driven from Python 3 with the standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_fringe_uniqueness.py [WA=28] [WB=28] [WC=20] [NP=4]
COST:       a few minutes on four cores.

Proposition 20 (PROOFS.md entry 33, second-read by GPT GC641 and Local L351): the seeds S_r (black cells 0 and r,
cells 1 .. r-1 alternating white, black, ..) give the single cell's pattern at every cell x <= t - 1, hence its centre
column. The owner asked (2026-10-09) to push on the open converse: are these the only finite seeds with that column?
A seed is X = (L, 1, R): left half L, cell 0 black (it must be, as column bit 0 is 1), right half R = x_0(1 .. w).

Lemma U1 (Cloud, 2026-10-09, by hand). Let Y = (white, 1, R). If L is not white and its shallowest black is at depth
b, then the centre columns of X and Y agree before time b and differ at time b.
  Proof. X and Y differ only at cells <= -b, the rightmost at -b. Rule 30 is left-permutive: if two rows agree at
  every cell > i and differ at i, the next rows agree at every cell > i + 1 and differ at i + 1, since
  x'(i + 1) = x(i) XOR (x(i + 1) OR x(i + 2)) and the OR's inputs agree. So at time t the rightmost difference is at
  -b + t, exactly. Column 0 agrees for t < b and differs at t = b. QED.
Corollary. Let tau(R) be the first time Y's column leaves the single cell's (infinity if never). If X has the single
  cell's column, then either L is white and tau(R) is infinite, or L's shallowest black is at depth exactly tau(R).
  In particular a white or fringe right half forces a white left half. With a white right half this says the single
  cell is the only seed (L, 1, white) with its own column.
So the question splits into two scans.
  - Empty left (mode A): which R have tau(R) infinite? Run (white, 1, R) directly and stop at the first disagreement.
  - Any left (mode B): decrypt the single cell's column under each key R. The left half is the unique plaintext
    (left-permutivity); a finite seed with right half R exists only if that plaintext ends. Here "ends" is tested as
    "no black at depths D + 1 .. T - 1".
Exploratory baseline, computed by Cloud on 2026-10-09 before these predictions and disclosed: for right halves of
exact width w <= 18, mode A at T = 3000 found exactly one key lasting the whole run at each width, the fringe S_w. The
longest-lasting other key held out 3, 7, 11, 33, 33, 33, 77, 128, 140, 140, 140, 140, 153, 214, 280, 289 and 289 steps
at w = 2 .. 18. On 2026-10-08 (rule30_cloud_equivalent_seeds.c), mode B's question at w <= 16, depth <= 200,
T = 400 found only the family.

PREDICTIONS, written 2026-10-09 by 05:41 BST before this script's full run. Smoke test only, at widths <= 12
(python3 rule30_cloud_fringe_uniqueness.py 12 12 12). It reproduced the baseline's 13 keys and its longest-lasting
keys, and EQ-C1 and EQ-C2 passed. It also ran depth 1000 at width <= 12, which is slightly beyond the baseline: only
the family survived there.
  EQ-C1 (control, exact): mode B's survivors include the white key and every fringe S_r, each with a white plaintext.
  EQ-C2 (control, Lemma U1, a theorem): for every key of width 1 .. 16, mode B's shallowest plaintext black (T = 400)
      is at depth tau(R) from mode A, and the plaintext is white exactly for the fringe keys.
  EQ1 (blind; empty left): for every exact width w = 1 .. 28, the only right half with (white, 1, R) keeping the
      single cell's column for 3000 steps is S_w. Confidence 0.9.
  EQ2 (blind; any left, to depth 200): every key of width <= 28 except the white key and the fringes decrypts to a
      plaintext with a black at some depth 201 .. 239 (T = 240). So no finite seed with |R| <= 28 and a left half of
      depth <= 200 shares the column, apart from the family. Confidence 0.9.
  EQ3 (blind; deeper): the same for keys of width <= 20 with depth 1000 (T = 1040). Confidence 0.9.
UNEXPECTED CHECK, EQ4: the longest a non-fringe right half of width <= 28 keeps the single cell's column (the
  largest tau(R) < 3000) lies between 300 and 1000 steps. Confidence 0.6.
Counterfactual: a survivor outside the family in EQ1 to EQ3 would be a new equivalent seed, to be run to 10^4 steps
  and then proved like Proposition 20 or broken. EQ1 to EQ3 holding is evidence, not a proof: wider right halves and
  deeper left halves stay open.
REFUTED-BY: EQ-C1 or EQ-C2 failing (the instrument); EQ1 to EQ4 failing.
"""
import pathlib, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
WA = int(sys.argv[1]) if len(sys.argv) > 1 else 28
WB = int(sys.argv[2]) if len(sys.argv) > 2 else 28
WC = int(sys.argv[3]) if len(sys.argv) > 3 else 20
NP = int(sys.argv[4]) if len(sys.argv) > 4 else 4
TA, DB, TB, DC, TC = 3000, 200, 240, 1000, 1040
EXE = str(pathlib.Path(tempfile.gettempdir()) / "rule30_fringe_uniqueness")
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def fringe(r):
    """S_r's right half as a key: cells 1 .. r - 1 alternate white, black, ..; cell r black."""
    cells = [1 if j % 2 == 0 else 0 for j in range(1, r)] + [1]
    return sum(b << i for i, b in enumerate(cells))


def run(args):
    out = subprocess.run([EXE] + [str(a) for a in args], check=True, capture_output=True, text=True).stdout
    return [line.split() for line in out.splitlines()]


def parallel(argsets):
    with ThreadPoolExecutor(max_workers=NP) as ex:
        return [row for rows in ex.map(run, argsets) for row in rows]


def main():
    subprocess.run(["cc", "-O2", "-o", EXE, str(HERE / "fringe_uniqueness.c")], check=True)
    W = max(WA, WB, WC, 16)
    fr = {r: fringe(r) for r in range(1, W + 1)}
    # the lemma control: every key of width 1 .. 16 in both modes
    taus = {}
    for row in parallel([("A", w, p, NP, TA, "all") for w in range(1, 17) for p in range(NP)]):
        if row[0] == "T":
            taus[int(row[1])] = int(row[2])
    firsts = {int(r[1]): int(r[2]) for r in parallel([("B", 16, p, NP, DB, 400, "all") for p in range(NP)])
              if r[0] == "F"}
    bad = [k for k in range(1, 1 << 16)
           if not ((taus[k] == TA and firsts[k] == -1) or (taus[k] < TA and firsts[k] == taus[k]))]
    fset16 = {k for k in range(1, 1 << 16) if firsts[k] == -1}
    report("EQ-C2 Lemma U1: shallowest plaintext black = tau(R) on all 65,535 keys of width 1 .. 16",
           not bad and fset16 == {fr[r] for r in range(1, 17)}, f"{len(bad)} disagreements; white plaintexts"
           f" exactly the 16 fringes: {fset16 == {fr[r] for r in range(1, 17)}}")
    # EQ1: empty left, every exact width
    surv, worst = {}, {}
    rows = parallel([("A", w, p, NP, TA) for w in range(1, WA + 1) for p in range(NP)])
    w_of = lambda k: k.bit_length()
    for row in rows:
        if row[0] == "S":
            surv.setdefault(w_of(int(row[1])), []).append(int(row[1]))
    for row in rows:
        if row[0] == "M" and int(row[1]) >= 0:
            k = int(row[2])
            w = w_of(k)
            if int(row[1]) > worst.get(w, (-1, 0))[0]:
                worst[w] = (int(row[1]), k)
    eq1 = all(surv.get(w, []) == [fr[w]] for w in range(1, WA + 1))
    print("   empty left: keys lasting 3000 steps by width: "
          + ", ".join(f"{w}: {len(surv.get(w, []))}" for w in range(1, WA + 1)))
    print("   longest-lasting non-fringe key by width (tau, key cells 1 .. w): "
          + "; ".join(f"{w}: {t} {''.join(str((k >> j) & 1) for j in range(w))}"
                      for w, (t, k) in sorted(worst.items())))
    # EQ2, EQ3: decryption
    sb = {int(r[1]): int(r[2]) for r in parallel([("B", WB, p, NP, DB, TB) for p in range(NP)]) if r[0] == "S"}
    sc = {int(r[1]): int(r[2]) for r in parallel([("B", WC, p, NP, DC, TC) for p in range(NP)]) if r[0] == "S"}
    famB = {0} | {fr[r] for r in range(1, WB + 1)}
    famC = {0} | {fr[r] for r in range(1, WC + 1)}
    report("EQ-C1 the white key and every fringe survive decryption with a white plaintext",
           famB <= set(sb) and famC <= set(sc) and all(sb[k] == -1 for k in famB) and all(sc[k] == -1 for k in famC))
    print(f"   decryption survivors: width <= {WB}, depth <= {DB}: {len(sb)} keys ({len(set(sb) - famB)} outside"
          f" the family); width <= {WC}, depth <= {DC}: {len(sc)} keys ({len(set(sc) - famC)} outside)")
    for k in sorted((set(sb) - famB) | (set(sc) - famC))[:20]:
        print(f"   outside the family: key {k} (cells {''.join(str((k >> j) & 1) for j in range(w_of(k)))}),"
              f" shallowest plaintext black {sb.get(k, sc.get(k))}")
    print()
    verdict("EQ1 empty left: only S_w lasts 3000 steps at each width 1 .. %d" % WA, eq1)
    verdict("EQ2 any left to depth 200: only the family, width <= %d" % WB, set(sb) == famB)
    verdict("EQ3 any left to depth 1000: only the family, width <= %d" % WC, set(sc) == famC)
    tmax = max(worst.values())
    verdict("EQ4 (unexpected check) the longest-lasting non-fringe key holds 300 .. 1000 steps", 300 <= tmax[0] <= 1000,
            f"{tmax[0]} steps, width {w_of(tmax[1])}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
