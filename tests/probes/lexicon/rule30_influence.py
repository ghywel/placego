#!/usr/bin/env python3
"""rule30_influence.py: which bits of column 1 a zero run of the forced left half depends on (lead 1).

RUN-ON:     cpu (pure Python 3, standard library; records.c for the control)
COMMAND:    python3 tests/probes/lexicon/rule30_influence.py [SAMPLES=2000]
COST:       a few minutes on one core.

Background (RULE30-PRIZE.md sections 8.36, 8.37). For column 0 = 0101..., the record R(d) is the longest zero run
of the forced left half from depth d over every column 1. Inside a run each free bit of column 1 is forced (the two
choices give complementary cells), so a prefix p of column 1 (its free bits at times 0, 2, .., d-2) determines one
forced walk, and its run length L(p). R(d) = max over p of L(p). The records follow R(d) ~ 0.8 d from depth 49 to 81.
Under the coin model (half a bit per cell) the best of N independent walks lasts about 2 log2 N cells, so 0.8 d means
about 2^(0.4 d) effectively independent walks among the 2^(d/2) prefixes. One explanation: the run hardly depends on
column 1's earliest bits.
The measurement. For random prefixes p and each bit i, the influence f_i = P(L(p) != L(p XOR e_i)).

PREDICTIONS, written 2026-10-05 before this script's first run (no exploratory run):
  IN0 (control): this script's forced walk, run over every prefix at depths 21 and 25, gives exactly records.c's
      record and histogram (H lines).
  IN1 (blind): influence rises with the bit's time: the Spearman correlation of f_i with i exceeds 0.5 at each of
      depths 33, 41 and 49.
  IN2 (blind; the explanation): the earliest bits hardly matter: every bit at a time below 0.2 d has f_i below 0.1, at
      each depth.
  IN3 (blind): the latest bits matter most: every bit at a time above 0.6 d has f_i above 0.5.
REFUTED-BY: IN0 failing (the instrument); IN1 to IN3 failing.

OUTCOME, 2026-10-05 (the first run, 5 seconds, 2000 samples):
  IN0 PASSED: at depths 21 and 25 the forced walk over every prefix gives records.c's histogram exactly.
  IN1 HELD (Spearman 0.77, 0.83, 0.69 at depths 33, 41, 49).
  IN2 REFUTED: only the first two or three bits are weak. Influence by bit (time 0, 2, 4, 6, 8, 10):
     depth 33: 0.01 0.10 0.37 0.55 0.63 0.65;  depth 41: 0.00 0.04 0.20 0.44 0.56 0.65;
     depth 49: 0.00 0.01 0.11 0.31 0.49 0.60.  From time 12 on every bit sits at 0.63 to 0.69.
  IN3 HELD (the smallest late influence 0.65, 0.66, 0.65).
  The plateau is 2/3. Under the coin model a run is 1 + 2M with P(M >= m) = 2^-m, and two independent runs differ
  with probability 1 - 1/3 = 2/3. So flipping any bit from time 12 on gives a fresh, independent run: the prefixes are
  as independent as the coin model needs, except for a few early bits. The weak set grows slowly with depth (time 6
  falls from 0.55 to 0.31 between 33 and 49), not in proportion to d. As the whole explanation of R ~ 0.8 d it fails.
  A reading, not tested here: a cell at time t depends only on column 1 at times t and later (the left-parent rule
  builds row t from rows t and t + 1). So the bit at time 2i can change only rows 0 .. 2i. Its damage has to cross
  that strip to depth d, and an OR whose other input is 1 stops it. A thin strip loses the damage, and the two
  prefixes then reach the same walk state: an exact merge. rule30_merge.py counts the merges.
"""
import pathlib, random, subprocess, sys, tempfile
from ompflags import OMP          # Apple's clang needs libomp's flags (ompflags.py)

HERE = pathlib.Path(__file__).resolve().parent
SAMPLES = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def diag(P, Q, c, k):
    """A_k from A_{k-1} = P and A_{k-2} = Q (ints, bit j = entry j), c = column 1 at time k-1 (records.c's rule)."""
    X = (P << 1) | (Q << 2) | (c << 1)
    X = (X & ~1) | (k & 1)
    s = 1
    while s <= k:
        X ^= X << s
        s <<= 1
    return X & ((2 << k) - 1)


def run_length(prefix, d, cap=400):
    """The forced walk: prefix bit i is column 1 at time 2i (i < number of free bits before depth d)."""
    P, Q = 0, 0                                        # A_0 = tau(0) = 0; A_{-1} empty
    for k in range(1, d):
        c = (prefix >> ((k - 1) // 2)) & 1 if (k - 1) % 2 == 0 else 0
        P, Q = diag(P, Q, c, k), P
    k = d
    while k - d < cap:
        if (k - 1) % 2 == 0:                           # free step: the cell is forced to 0 by the choice of c
            A = diag(P, Q, 0, k)
            if (A >> k) & 1:
                A = diag(P, Q, 1, k)
        else:
            A = diag(P, Q, 0, k)
            if (A >> k) & 1:
                return k - d
        P, Q = A, P
        k += 1
    return cap


def nfree(d):
    return (d - 2) // 2 + 1 if d >= 2 else 0


def spearman(xs, ys):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(v):
            j = i
            while j + 1 < len(v) and v[order[j + 1]] == v[order[i]]:
                j += 1
            for k in range(i, j + 1):
                r[order[k]] = (i + j) / 2
            i = j + 1
        return r
    rx, ry = ranks(xs), ranks(ys)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return num / den if den else 0.0


def main():
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_influence_records"
    subprocess.run(["cc", "-O2", *OMP, "-o", str(exe), str(HERE / "records.c")], check=True)
    ok0 = True
    for d in (21, 25):
        out = subprocess.run([str(exe), str(d), "2"], check=True, capture_output=True, text=True).stdout
        H = {int(f.split()[2]): int(f.split()[3]) for f in out.split("\n") if f.startswith("H ")}
        mine = {}
        for p in range(1 << nfree(d)):
            L = run_length(p, d)
            mine[L] = mine.get(L, 0) + 1
        ok0 &= mine == H
        print(f"   depth {d}: records.c histogram {dict(sorted(H.items()))}; forced walk {dict(sorted(mine.items()))}",
              flush=True)
    report("IN0 the forced walk reproduces records.c's histogram at depths 21 and 25", ok0)
    rng = random.Random(1940)                          # the year the first Bombe ran
    res = {}
    for d in (33, 41, 49):
        n = nfree(d)
        f = [0] * n
        for _ in range(SAMPLES):
            p = rng.getrandbits(n)
            L = run_length(p, d)
            for i in range(n):
                f[i] += run_length(p ^ (1 << i), d) != L
        f = [x / SAMPLES for x in f]
        res[d] = f
        print(f"   depth {d}: influence of the bit at time 2i, i = 0 .. {n - 1}: "
              + " ".join(f"{x:.2f}" for x in f), flush=True)
    rho = {d: spearman(list(range(len(f))), f) for d, f in res.items()}
    verdict("IN1 influence rises with the bit's time (Spearman > 0.5 at each depth)",
            all(r > 0.5 for r in rho.values()), ", ".join(f"{d}: {r:.2f}" for d, r in rho.items()))
    early = {d: max(f[i] for i in range(len(f)) if 2 * i < 0.2 * d) for d, f in res.items()}
    verdict("IN2 the earliest bits (times below 0.2 d) have influence below 0.1", all(v < 0.1 for v in early.values()),
            ", ".join(f"{d}: largest {v:.2f}" for d, v in early.items()))
    late = {d: min(f[i] for i in range(len(f)) if 2 * i > 0.6 * d) for d, f in res.items()}
    verdict("IN3 the latest bits (times above 0.6 d) have influence above 0.5", all(v > 0.5 for v in late.values()),
            ", ".join(f"{d}: smallest {v:.2f}" for d, v in late.items()))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
