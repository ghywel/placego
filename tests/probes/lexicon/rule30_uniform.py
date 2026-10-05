#!/usr/bin/env python3
"""rule30_uniform.py: is "total width plus a constant" one law for every centre word? (lead 1, uniform over periods)

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_uniform.py [WMAX=16]
COST:       about fifteen minutes on one core.

Background (PRIZE-PROBLEMS.md sections 8.24, 8.40, 8.41). rule30_complement.py measured, for the centre word 0101...,
how long a finite seed keeps its centre column on the word. Take a right half R of exact width W and its forced left
half (rule30_periodic.forced_left), and cut the left half at depth d. That makes a seed of w = d + 1 + W cells whose
centre column follows the word until time P, the depth of the first 1 beyond the cut. The excess E = P - w,
maximised over cuts, is (the longest zero run of the forced left half) - W. For 0101 it never exceeded +9, at any
width up to 32 cells.
If every condition at the wall costs one bit, a seed's w bits buy about w steps whatever the word, so the largest
excess should stay a small constant for every word. That is a uniform law, the shape the prize table says would win
(a uniform argument over all periods). Any finite bound proves Problem 1 for that word, since an eventually
periodic centre column would need a seed that keeps the word for ever.

PREDICTIONS, written 2026-10-05 before this script's first run (widths W = 0 .. 16, cuts to depth 126):
  UW0 (control, must hold): for 01 the largest excess by exact width reproduces rule30_complement.py's outcome:
      +5, +8, +7, +6, +5, +9, +8, +7, +6, +5, +4, +3, +2, +1, +3, +2, +1 at W = 0 .. 16.
  UW1 (blind; one law for every word): for each two-colour word of period up to 4 (001, 011, 0001, 0011, 0111), the
      largest excess at every width is at most +12.
  UW2 (blind; wider is worse): for each two-colour word, the largest excess over widths 12 .. 16 is below the
      largest over widths 0 .. 8. The bits of a wide right half arrive too late (section 8.17).
  UW3 (blind; the one-colour walls, from Condrey's explicit fibres): for w = 1 the largest excess is at most +2 at
      every width; for w = 0, over nonzero right halves, at most +2 at every width from 1 to 16.
  UW4 (random-chaos: does the law need a period?): a random wall (4096 random bits) obeys UW1's +12 at every width.
REFUTED-BY: UW0 failing (the instrument); UW1 to UW4 failing.
"""
import pathlib, random, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
WMAX = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 16
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
sys.argv = _argv
K = 126
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def excess_by_width(tau, skip_zero=False):
    out = {}
    for W in range(0, WMAX + 1):
        lo, hi = (0, 1) if W == 0 else (1 << (W - 1), 1 << W)
        best, arg, capped = None, None, False
        for R in range(lo, hi):
            if skip_zero and R == 0:
                continue
            L = r30.forced_left(R, tau, K)
            run, longest, start = 0, 0, 1
            for k in range(1, K + 1):
                if L[k - 1]:
                    run = 0
                else:
                    run += 1
                    if run > longest:
                        longest, start = run, k - run + 1
            capped |= start + longest - 1 == K
            e = longest - W
            if best is None or e > best:
                best, arg = e, (R, start, longest)
        if best is not None:
            out[W] = (best, arg, capped)
    return out


def main():
    rng = random.Random(4096)
    words = {"01": [0, 1], "001": [0, 0, 1], "011": [0, 1, 1], "0001": [0, 0, 0, 1], "0011": [0, 0, 1, 1],
             "0111": [0, 1, 1, 1], "1": [1], "0": [0], "random": [rng.getrandbits(1) for _ in range(4096)]}
    res = {}
    for n, w in words.items():
        tau = [w[t % len(w)] for t in range(K + 2)]
        res[n] = excess_by_width(tau, skip_zero=(n == "0"))
        print(f"   {n:6s}: largest excess by width: "
              + " ".join(f"{W}:{v[0]:+d}{'*' if v[2] else ''}" for W, v in res[n].items()), flush=True)
        top = max(res[n].values(), key=lambda v: v[0])
        print(f"           champion: R = {top[1][0]}, a run of {top[1][2]} zeros from depth {top[1][1]}", flush=True)
    want = [5, 8, 7, 6, 5, 9, 8, 7, 6, 5, 4, 3, 2, 1, 3, 2, 1]
    report("UW0 01 reproduces rule30_complement.py", [res["01"][W][0] for W in range(min(17, WMAX + 1))]
           == want[:min(17, WMAX + 1)])
    two = ["001", "011", "0001", "0011", "0111"]
    capped = [n for n in res if any(v[2] for v in res[n].values())]
    print(f"   (* = the run reached depth 126, so the excess is a lower bound; words affected: {capped or 'none'})")
    verdict("UW1 the largest excess is at most +12 for every two-colour word",
            all(v[0] <= 12 for n in two for v in res[n].values()),
            ", ".join(f"{n}: {max(v[0] for v in res[n].values()):+d}" for n in two))
    late = {n: max(res[n][W][0] for W in range(12, WMAX + 1)) for n in two}
    early = {n: max(res[n][W][0] for W in range(0, 9)) for n in two}
    verdict("UW2 wider is worse: the best over widths 12 .. 16 is below the best over 0 .. 8",
            all(late[n] < early[n] for n in two), ", ".join(f"{n}: {late[n]:+d} vs {early[n]:+d}" for n in two))
    verdict("UW3 the one-colour walls stay within +2",
            all(v[0] <= 2 for v in res["1"].values()) and all(v[0] <= 2 for W, v in res["0"].items() if W >= 1),
            f"1: {max(v[0] for v in res['1'].values()):+d}, 0: "
            f"{max(v[0] for W, v in res['0'].items() if W >= 1):+d}")
    verdict("UW4 the random wall stays within +12", all(v[0] <= 12 for v in res["random"].values()),
            f"largest {max(v[0] for v in res['random'].values()):+d}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def longest_run(L, K):
    run, longest, start = 0, 0, 1
    for k in range(1, K + 1):
        if L[k - 1]:
            run = 0
        else:
            run += 1
            if run > longest:
                longest, start = run, k - run + 1
    return longest, start


def deep(K2=320):
    """The addendum: every right half whose zero run reaches depth 126 is recomputed to depth K2."""
    rng = random.Random(4096)
    words = {"01": [0, 1], "001": [0, 0, 1], "011": [0, 1, 1], "0001": [0, 0, 0, 1], "0011": [0, 0, 1, 1],
             "0111": [0, 1, 1, 1], "random": [rng.getrandbits(1) for _ in range(4096)]}
    for n, w in words.items():
        tau = [w[t % len(w)] for t in range(K2 + 2)]
        best, still = {}, 0
        for W in range(0, WMAX + 1):
            lo, hi = (0, 1) if W == 0 else (1 << (W - 1), 1 << W)
            e_best = None
            for R in range(lo, hi):
                lg, st = longest_run(r30.forced_left(R, tau[:K + 2], K), K)
                if st + lg - 1 == K:
                    lg, st = longest_run(r30.forced_left(R, tau, K2), K2)
                    still += st + lg - 1 == K2
                e = lg - W
                e_best = e if e_best is None or e > e_best else e_best
            best[W] = e_best
        print(f"   {n:6s} to depth {K2}: largest excess by width: " + " ".join(f"{W}:{e:+d}" for W, e in best.items())
              + f"; runs still reaching {K2}: {still}", flush=True)


if __name__ == "__main__":
    deep() if sys.argv[1:2] == ["deep"] else main()
