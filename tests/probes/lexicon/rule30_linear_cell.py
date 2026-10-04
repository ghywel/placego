#!/usr/bin/env python3
"""rule30_linear_cell.py: Lemma 4 (the newest bit of column 1 enters the forced left half once, as an XOR), checked;
and where the two-sided zero runs end, for words not yet looked at.

RUN-ON:     cpu (pure Python 3, standard library; exact, with seeded random columns 1 for the check)
COMMAND:    python3 tests/probes/lexicon/rule30_linear_cell.py [W=16] [K=192] [JOBS=4]
COST:       a few minutes on 4 cores.

Lemma 4 (PRIZE-PROBLEMS.md section 8.2). Write L(k) for the cell at depth k of the forced left half (column -k at
time 0), tau for column 0 and sigma for column 1. Then L(k) depends on sigma(0), ..., sigma(k-1) only, and on the
newest of them like this:
    tau(k-1) = 0:  L(k) = sigma(k-1) XOR g_k(sigma(0), ..., sigma(k-2))      (call depth k a linear cell)
    tau(k-1) = 1:  L(k) does not depend on sigma(k-1)                        (a forced cell)
Proof. Rule 30 inverted to the left is x(i-1, t) = x(i, t+1) XOR (x(i, t) OR x(i+1, t)). By induction column -m at
time t depends on sigma(t), ..., sigma(t+m-1), and the newest, sigma(t+m-1), enters only through x(-m+1, t+1), as an
XOR. Unwinding to column -1 at time k-1: x(-1, k-1) = tau(k) XOR (tau(k-1) OR sigma(k-1)), which is
tau(k) XOR sigma(k-1) when tau(k-1) = 0 and does not involve sigma(k-1) when tau(k-1) = 1.

So with column 1 free, every linear cell can be set to 0 by its own bit, which is why the left side alone allows such
long runs (section 7). With column 1 made by a finite right half, a long run needs the right side's bits to equal the
left side's demands g_k, linear cell after linear cell.

PREDICTIONS, written 2026-10-04 before this script's first run:
  P2 (the lemma, checked): for 50 seeded random columns 1 and the words 01, 10, 001, 011, 0001, 0011, 0111, at every
     depth k up to K, flipping sigma(k-1) leaves L(1), ..., L(k-1) unchanged, flips L(k) when tau(k-1) = 0, and
     leaves the whole left half unchanged when tau(k-1) = 1.
  CF (counterfactual, must be caught): "flipping sigma(k-1) changes only L(k)". It is false (the flip also reaches
     deeper cells), and the check must say so, or it cannot see beyond L(k).
  C  (control, known answer): with the left half replaced by coin flips, the share of zero runs ending at a linear
     cell is the share of linear cells in the word, within 0.01.
  P3 (uncertain, blind for these words): for trace 0101... the ad-hoc look and section 8.2's parity table say 99% of
     the runs of 14 or more end at a linear cell. For the words 001, 011, 0001, 0011, 0111, with both sides exact
     (every right half up to W cells, depth up to K), at least 90% of the zero runs of 10 or more cells end at a
     linear cell (the 1 that ends the run sits at a linear depth). The shares of linear cells in these words are
     2/3, 1/3, 3/4, 1/2 and 1/4.
REFUTED-BY: P2 or C failing, or CF not caught (the instrument is wrong); P3 below 90% for any of the five words.
"""
import random, sys, pathlib
from multiprocessing import Pool

W = int(sys.argv[1]) if len(sys.argv) > 1 else 16
K = int(sys.argv[2]) if len(sys.argv) > 2 else 192
JOBS = int(sys.argv[3]) if len(sys.argv) > 3 else 4
WORDS = [(0, 1), (1, 0), (0, 0, 1), (0, 1, 1), (0, 0, 0, 1), (0, 0, 1, 1), (0, 1, 1, 1)]
BLIND = [(0, 0, 1), (0, 1, 1), (0, 0, 0, 1), (0, 0, 1, 1), (0, 1, 1, 1)]
LONG = 10

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
sys.argv = _argv
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def trace(word, n):
    return [word[t % len(word)] for t in range(n)]


def left_from_col1(tau, c1):
    """The forced left half L(1..K) from column 0 (tau, K+1 bits) and column 1 (an integer, bit t = sigma(t))."""
    c0 = sum(b << t for t, b in enumerate(tau))
    cols, out = [c1, c0], []
    for k in range(1, K + 1):
        m = (1 << (K - k + 1)) - 1
        cols.append(((cols[-1] >> 1) ^ (cols[-1] | cols[-2])) & m)
        out.append(cols[-1] & 1)
    return out


def ends(L, tau):
    """For each zero run that ends inside the window: (length, whether the 1 that ends it is at a linear cell)."""
    out, run = [], 0
    for k, b in enumerate(L, 1):
        if b == 0:
            run += 1
        else:
            if run:
                out.append((run, tau[k - 1] == 0))
            run = 0
    return out


def both_chunk(args):
    word, lo, hi = args
    tau = trace(word, K + 1)
    lin = tot = 0
    for R in range(lo, hi):
        for n, linear in ends(r30.forced_left(R, tau, K), tau):
            if n >= LONG:
                tot += 1
                lin += linear
    return lin, tot


def main():
    rng = random.Random(4)
    bad = cf_caught = 0
    for word in WORDS:
        tau = trace(word, K + 1)
        for _ in range(50):
            c1 = rng.getrandbits(K + 1)
            L = left_from_col1(tau, c1)
            for k in range(1, K + 1):
                L2 = left_from_col1(tau, c1 ^ (1 << (k - 1)))
                if L2[:k - 1] != L[:k - 1]:
                    bad += 1
                if tau[k - 1] == 0 and L2[k - 1] == L[k - 1]:
                    bad += 1
                if tau[k - 1] == 1 and L2 != L:
                    bad += 1
                if tau[k - 1] == 0 and L2[k:] != L[k:]:
                    cf_caught += 1
    report("P2 Lemma 4: the newest bit of column 1 enters once, as an XOR, at linear cells only",
           bad == 0, f"{len(WORDS)} words x 50 columns x {K} depths, {bad} violations")
    report("CF 'flipping sigma(k-1) changes only L(k)' is caught", cf_caught > 0, f"caught {cf_caught} times")
    worst = 0.0
    for word in BLIND:
        tau = trace(word, K + 1)
        lin = tot = 0
        for _ in range(20000):
            for n, linear in ends([rng.getrandbits(1) for _ in range(K)], tau):
                tot += 1
                lin += linear
        share = sum(1 for t in tau[:K] if t == 0) / K
        worst = max(worst, abs(lin / tot - share))
    report("C coin flips: the share of runs ending at a linear cell is the share of linear cells", worst <= 0.01,
           f"largest gap {worst:.4f}")
    with Pool(JOBS) as pool:
        for word in [(0, 1), (1, 0)] + BLIND:
            name = "".join(map(str, word))
            step = 2048
            res = pool.map(both_chunk, [(word, lo, min(lo + step, 1 << W)) for lo in range(0, 1 << W, step)])
            lin, tot = sum(r[0] for r in res), sum(r[1] for r in res)
            share = sum(1 for t in word if t == 0) / len(word)
            line = (f"word {name}: {lin} of {tot} zero runs of {LONG} or more end at a linear cell "
                    f"({lin / tot:.1%}; linear cells are {share:.0%} of depths)" if tot else
                    f"word {name}: no zero runs of {LONG} or more")
            if word in BLIND:
                verdict(f"P3 {line}", tot > 0 and lin / tot >= 0.90)
            else:
                print(f"   (recorded before, not blind) {line}", flush=True)
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
