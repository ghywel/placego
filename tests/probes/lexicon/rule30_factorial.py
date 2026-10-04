#!/usr/bin/env python3
"""rule30_factorial.py: the four arms. Column 0 is periodic; column 1 is shared by both sides. The left side either
forces the left half (from columns 0 and 1) or leaves it free; the right side either produces column 1 (from a finite
right half) or leaves it free. One statistic for every arm: the longest run of zeros in the left half, depth 1..K.

RUN-ON:     cpu (pure Python 3, standard library; exact arithmetic, Monte Carlo sampling with fixed seeds)
COMMAND:    python3 tests/probes/lexicon/rule30_factorial.py [K=64] [SAMPLES=100000] [WORDS=01,0001]
COST:       about a minute.

The owner's design (2026-10-04): left alone (PRIZE-PROBLEMS.md section 7) and both (section 8) had been measured;
right alone had not.

  neither       left half free, column 1 free: the left half is K random bits.
  right alone   left half free, column 1 from a random right half. Column 1 does not reach a free left half, so
                this arm's left half is also K random bits. That is a proof, not a measurement, and the arm is shown
                to equal "neither" as a check (F1b). On its own the right side never forbids a finite configuration:
                for any finite right half, column 0's own update is met by choosing column -1, and that choice is
                exactly what the left side forces.
  left alone    left half forced, column 1 uniformly random.
  both          left half forced, column 1 from a uniformly random right half of width K.

PREDICTIONS, written 2026-10-04 before the first run:
  F1 (control, known answer): "neither" matches the exact distribution of the longest zero run in K fair bits
     (computed by recursion): every tail probability within 0.01.
  F1b (control): "right alone" equals "neither" within the same tolerance.
  F2 (uncertain): the right side matters only in the extreme tail. For runs of 4 to 12 cells, the probability of a
     run at least that long under "both" is within a factor of 2 of "left alone".
  F3 (recorded earlier, restated): the extremes differ. With column 1 free, exhaustive searches find runs of 32 cells
     ending by depth 64 (01, from depth 33). With column 1 from right halves up to 20 cells, no run exceeds 20 by
     depth 192 (rule30_rigidity.py, rule30_twosided_exact.py).
REFUTED-BY: F1 or F1b failing (the instrument is wrong); F2 failing at any run length from 4 to 12 (then the right side
  shortens typical runs too, not only the extreme ones).

OUTCOME of the first runs, 2026-10-04: F1 and F1b held. F2 was REFUTED for both words: the right side reshapes the
middle of the distribution too (see PRIZE-PROBLEMS.md section 8).

F4 (control, added after those runs at the owner's question "is pseudorandom enough?", written before its run): the
sampling generator is Python's seeded Mersenne Twister, which is linear over GF(2), the arithmetic Rule 30 lives in.
So `GEN=os` re-runs every arm with the operating system's entropy source (random.SystemRandom, os.urandom), which is
not linear and not seeded. Prediction: every tail probability agrees with the seeded run within 4 standard errors.
Refuted by any disagreement beyond that, which would mean the generator, not Rule 30, shapes a result.
"""
import random, sys, pathlib

K = int(sys.argv[1]) if len(sys.argv) > 1 else 64
SAMPLES = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
WORDS = [tuple(int(c) for c in w) for w in (sys.argv[3] if len(sys.argv) > 3 else "01,0001").split(",")]
GEN = __import__("os").environ.get("GEN", "mt")         # mt: seeded Mersenne Twister (default); os: system entropy

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


def longest(bits):
    run = m = 0
    for b in bits:
        run = run + 1 if b == 0 else 0
        m = max(m, run)
    return m


def exact_tail(n, B):
    """P(longest zero run in n fair bits >= B), by counting strings with every zero run < B."""
    # f[i] = number of strings of length i with no zero run of length >= B
    f = [0] * (n + 1)
    for i in range(n + 1):
        if i < B:
            f[i] = 2 ** i
        else:
            f[i] = sum(f[i - j - 1] for j in range(B))        # the last one at position i-j, then j zeros
    return 1 - f[n] / 2 ** n


def left_from_col1(word, c1bits):
    tau = [word[t % len(word)] for t in range(K + 1)]
    c0 = sum(b << t for t, b in enumerate(tau))
    c1 = sum(b << t for t, b in enumerate(c1bits))
    cols, out = [c1, c0], []
    for k in range(1, K + 1):
        m = (1 << (K - k + 1)) - 1
        cols.append(((cols[-1] >> 1) ^ (cols[-1] | cols[-2])) & m)
        out.append(cols[-1] & 1)
    return out


def tails(runs, Bs):
    n = len(runs)
    return [sum(r >= B for r in runs) / n for B in Bs]


def main():
    Bs = list(range(2, 21))
    exact = [exact_tail(K, B) for B in Bs]
    for word in WORDS:
        name = "".join(map(str, word))
        rng = (random.SystemRandom() if GEN == "os" else
               random.Random(1000 + int(name, 2) * 7 + len(name)))   # deterministic (str hash is randomised per run)
        tau = [word[t % len(word)] for t in range(K + 1)]
        neither = [longest([rng.getrandbits(1) for _ in range(K)]) for _ in range(SAMPLES)]
        right_alone = []
        for _ in range(SAMPLES):
            r30.forced_left(rng.getrandbits(K), tau, 4)        # a right half is made (and ignored by a free left half)
            right_alone.append(longest([rng.getrandbits(1) for _ in range(K)]))
        left_alone = [longest(left_from_col1(word, [rng.getrandbits(1) for _ in range(K + 1)])) for _ in range(SAMPLES)]
        both = [longest(r30.forced_left(rng.getrandbits(K), tau, K)) for _ in range(SAMPLES)]
        tn, tr, tl, tb = (tails(x, Bs) for x in (neither, right_alone, left_alone, both))
        dev = max(abs(a - b) for a, b in zip(tn, exact))
        report(f"F1 word {name}: 'neither' matches the exact longest-run law", dev <= 0.01, f"max deviation {dev:.4f}")
        dev2 = max(abs(a - b) for a, b in zip(tr, tn))
        report(f"F1b word {name}: 'right alone' equals 'neither'", dev2 <= 0.01, f"max deviation {dev2:.4f}")
        print(f"\n   word {name}: probability that the longest zero run in depth 1..{K} is at least B "
              f"({SAMPLES} samples per arm)")
        print("     B   exact  neither  right-alone  left-alone   both   left/both")
        for i, B in enumerate(Bs):
            ratio = (tl[i] / tb[i]) if tb[i] > 0 else float('inf')
            print(f"   {B:>3}  {exact[i]:.4f}  {tn[i]:.4f}   {tr[i]:.4f}     {tl[i]:.5f}   {tb[i]:.5f}   "
                  + (f"{ratio:6.2f}" if tb[i] > 0 else "   inf"))
        bad = [B for i, B in enumerate(Bs) if 4 <= B <= 12 and tb[i] > 0 and not (0.5 <= tl[i] / tb[i] <= 2.0)]
        bad += [B for i, B in enumerate(Bs) if 4 <= B <= 12 and tb[i] == 0 and tl[i] > 0]
        verdict(f"F2 word {name}: 'both' within a factor 2 of 'left alone' for B = 4..12", not bad,
                f"outside at B = {bad}" if bad else "")
        print(f"   longest seen: neither {max(neither)}, right alone {max(right_alone)}, left alone {max(left_alone)}, "
              f"both {max(both)}\n")
    print(f"{'ALL CONTROLS PASS' if FAILS == 0 else f'{FAILS} CONTROL FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
