#!/usr/bin/env python3
"""rule30_complement.py: the owner's complementary pair. How long can a finite seed keep two irrational numbers
complementary?

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_complement.py [WMAX=18]
COST:       about five minutes on one core.

The owner (2026-10-05): "I wonder if a rational number can have a complementary pair, such that two related irrational
numbers combine to form a rational one."

The pair (PRIZE-PROBLEMS.md section 8.22). Rule 30 at column 0 reads tau(t+1) = x_t(-1) XOR (tau(t) OR x_t(1)). With
tau = 0101... it forces x_t(-1) = 1 at odd t and x_t(1) = NOT x_t(-1) at even t. Read the even-time bits of column -1
as a binary number A and those of column 1 as B: complementary bits add without carries, so A + B = 0.111... = 1, and
the odd-time bits of column -1 make the number 1 as well. By Jen's theorem B cannot be eventually periodic in a
finite configuration, so A and B would be two irrational numbers, made independently by the left and right sides,
summing to exactly 1.

The measurement. Take a right half R (cells 1..W) and its forced left half L (section 5). Cut L at depth d (cells
deeper than d set to 0): a finite seed of w = d + 1 + W cells. Its column 0 follows 0101... exactly until time P =
the depth of the first 1 of L beyond d (the cut's first change reaches column 0 at that time, at one cell per step,
ahead of every other change). So the pair stays complementary for about P / 2 digits. The excess E = P - w says how
far a seed can beat its own width.

PREDICTIONS, written 2026-10-05 before this script's first run:
  CP0 (control, exact): for 200 random cuts (R up to 14 cells, d up to 60), the finite seed run forwards has column 0
      equal to 0101... for exactly P steps, and at every earlier time the two conditions (x(-1) = 1 at odd t,
      x(1) = NOT x(-1) at even t) hold, with the first violation at t = P - 1.
  CP1 (blind): the excess, maximised over every right half of exact width W and every cut depth d (left half to depth
      126), is at most 12 for every W from 0 to WMAX: a finite seed keeps the pair complementary for at most about
      (w + 12) / 2 digits.
  CP2 (blind): the largest excess over all widths occurs at a width of at most 8 cells. Wider right halves carry
      more bits but deliver them too late (the bottleneck, section 8.17).
REFUTED-BY: CP0 failing (the instrument); CP1 or CP2 failing.

OUTCOME of the first run, 2026-10-05 (WMAX = 18): CP0 passed (0 of 200 differ). The largest excess by exact width
W = 0 .. 18: +5, +8, +7, +6, +5, +9, +8, +7, +6, +5, +4, +3, +2, +1, +3, +2, +1, +0, -1. CP1 HELD (largest +9) and
CP2 HELD (at W = 5). The champion: right half 10001 (R = 17), its forced left half cut at depth 20, 26 cells in all,
keeps column 0 at 0101... for 35 steps. The same run of 14 zeros from depth 21 serves every width from 5 to 13, and
a run of 17 from depth 94 every width from 14 to 18: extra cells further out do not change them. With rule30_scan.py
(no zero run longer than 17 for right halves up to 32 cells) the excess is negative for every width from 18 to 32.
"""
import pathlib, random, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 18
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
sys.argv = _argv
K = 126
TAU = [t % 2 for t in range(K + 2)]
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def first_one_beyond(L, d):
    """Depth of the first 1 of L deeper than d (L[k - 1] is depth k), or None within the computed depth."""
    return next((k for k in range(d + 1, len(L) + 1) if L[k - 1]), None)


def simulate(R, L, d, T):
    """Run the finite seed (left half cut at depth d, column 0 = tau(0) = 0, right half R) forward T steps.
    Returns columns -1, 0, 1 as lists."""
    off = d + T + 2                                    # bit off + i holds cell i
    row = sum(L[k - 1] << (off - k) for k in range(1, d + 1)) | (R << (off + 1))
    mask = (1 << (off + R.bit_length() + T + 3)) - 1
    cm1, c0, c1 = [], [], []
    for _ in range(T):
        cm1.append((row >> (off - 1)) & 1)
        c0.append((row >> off) & 1)
        c1.append((row >> (off + 1)) & 1)
        row = ((row << 1) ^ (row | (row >> 1))) & mask
    return cm1, c0, c1


def main():
    rng = random.Random(1830)
    bad = 0
    for _ in range(200):
        R = rng.getrandbits(rng.randrange(1, 15)) | 1
        L = r30.forced_left(R, TAU, K)
        d = rng.randrange(0, 61)
        P = first_one_beyond(L, d)
        if P is None:
            continue
        cm1, c0, c1 = simulate(R, L, d, P + 3)
        ok = all(c0[t] == t % 2 for t in range(P)) and c0[P] != P % 2
        conds = [(cm1[t] == 1) if t % 2 else (c1[t] == 1 - cm1[t]) for t in range(P + 1)]
        ok &= all(conds[:P - 1] if P >= 1 else []) and not conds[P - 1]
        bad += not ok
    report("CP0 the cut seed follows 0101... for exactly P steps, and the pair conditions break at t = P - 1", bad == 0,
           f"{bad} of 200 differ")

    best = {}
    for W in range(0, WMAX + 1):
        lo, hi = (0, 1) if W == 0 else (1 << (W - 1), 1 << W)
        e_best, arg = None, None
        for R in range(lo, hi):
            L = r30.forced_left(R, TAU, K)
            run, longest, start = 0, 0, 1
            for k in range(1, K + 1):                  # the longest zero run anywhere, and where it starts
                if L[k - 1]:
                    run = 0
                else:
                    run += 1
                    if run > longest:
                        longest, start = run, k - run + 1
            e = longest - W                            # P - w = (d + 1 + run) - (d + 1 + W), with d = start - 1
            if e_best is None or e > e_best:
                e_best, arg = e, (R, start, longest)
        best[W] = (e_best, arg)
        print(f"   right halves of exact width {W:2d}: largest excess {e_best:+d} (R = {arg[0]}, run of {arg[2]} from "
              f"depth {arg[1]})", flush=True)
    emax = max(v[0] for v in best.values())
    wbest = [W for W, v in best.items() if v[0] == emax]
    verdict("CP1 the excess is at most 12 at every width", emax <= 12, f"largest {emax:+d} at widths {wbest}")
    verdict("CP2 the largest excess occurs at a width of at most 8", min(wbest) <= 8, f"widths {wbest}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
