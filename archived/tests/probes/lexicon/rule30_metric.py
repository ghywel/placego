#!/usr/bin/env python3
"""rule30_metric.py: how much information does column 1 actually carry next to 0101..., for typical right sides?

RUN-ON:     cpu (pure Python 3, standard library; seeded random right halves)
COMMAND:    python3 tests/probes/lexicon/rule30_metric.py [N=240] [T=4200]
COST:       about five minutes on one core.

rule30_entropy.py bounds the topological entropy of column 1's visible bits (every sequence any right side can make)
at 0.128 bits per visible bit, levelling off near 0.12 (RULE30-PRIZE.md section 8.20). The entropy rate of the
sequences that typical right sides make (random cells, each 0 or 1 with probability one half) is a different number,
at most the topological one. It is estimated here from long visible sequences of column 1 (even times only, Lemma 1),
with the first 600 steps dropped (the wheel's formation): the conditional block entropy
    h_k = H(next visible bit | the k visible bits before it),
which falls towards the entropy rate as k grows. The wheel U repeats every 56 steps, 28 visible bits, so k of 28 and
more lets the estimator see a whole turn of the wheel.

PREDICTIONS, written 2026-10-05 before this script's first run:
  ME0 (control, known answers): on the pure wheel (column 1 equal to U for ever) the estimator gives h_k < 0.005 for
      k >= 28; on a binary Markov source with known entropy rate 0.25 bits per bit (a symmetric chain that flips with
      probability 0.0417) it gives h_k within 0.02 of 0.25 for k = 1 .. 8.
  ME1 (consistency, a theorem's check): at k = 40 the estimate does not exceed the exact topological bound at m = 26,
      0.1277, by more than 0.01.
  ME2 (blind): column 1 carries real information at a positive rate: h_40 >= 0.04 bits per visible bit.
  ME3 (blind; the kicks carry it): the information per kick, h_40 times the mean number of visible bits between
      departures (rule30_wake.py: about 44, i.e. 88 steps), lies between 2 and 12 bits.
  CF  (counterfactual): with each sequence's visible bits shuffled (same ones, random order), h_4 rises to within
      0.03 of the binary entropy of the bits' frequency: the estimator sees order, not just the share of ones. (At k = 40
      shuffled, high-entropy data would leave almost every context unique and the plug-in estimate would collapse.)
  ST  (control, the estimator's sampling): h_40 from half of the sequences lies within 0.01 of h_40 from all of them.
REFUTED-BY: ME0, ME1, CF or ST failing (the instrument); ME2 or ME3 failing.

OUTCOME of the first run, 2026-10-05 (N = 240 right halves of 2,400 random cells, 1,800 visible bits each after the
first 600 steps): ME0 passed (pure wheel 0.0000 at k = 28, 32, 40; the Markov source 0.2479 against 0.2500). h_k for
k = 1, 2, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40: 0.673, 0.615, 0.147, 0.132, 0.114, 0.098, 0.098, 0.084, 0.082,
0.081, 0.080, 0.0795 bits per visible bit. ME1 passed (0.0795 against the bound 0.1277). ME2 HELD. ME3 HELD: 3.50 bits
per kick. CF passed (shuffled h_4 0.766 against a binary entropy of 0.767; unshuffled 0.147). ST passed (half 0.0802).
Typical right sides make column 1 carry about 0.08 bits per visible bit, two thirds of what the exact bound allows,
and the kicks, about 3.5 bits each, account for it.
"""
import math, pathlib, random, sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 240
T = int(sys.argv[2]) if len(sys.argv) > 2 else 4200
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_triangles as tr                         # noqa: E402
sys.argv = _argv
U = tr.U
KS = [1, 2, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
SKIP = 600
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def cond_entropy(seqs, k):
    """H(next | previous k) in bits, pooled over the sequences (plug-in estimate)."""
    joint, ctx = Counter(), Counter()
    for s in seqs:
        key = 0
        mask = (1 << k) - 1
        for i, b in enumerate(s):
            if i >= k:
                joint[(key, b)] += 1
                ctx[key] += 1
            key = ((key << 1) | b) & mask
    n = sum(ctx.values())
    return -sum(c / n * math.log2(c / ctx[key]) for (key, b), c in joint.items())


def column1_visible(R, steps):
    width = R.bit_length() + steps + 3
    mask = (1 << width) - 1
    row, vis = R << 1, []
    for t in range(steps):
        if t % 2 == 0 and t >= SKIP:
            vis.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
    return vis


def main():
    rng = random.Random(8080)
    # controls
    wheel = [[U[(t + d) % 56] for t in range(0, 4000, 2)] for d in range(0, 56, 2)]
    hw = {k: cond_entropy(wheel, k) for k in (28, 32, 40)}
    p = 0.0417
    hp = -(p * math.log2(p) + (1 - p) * math.log2(1 - p))
    markov = []
    for _ in range(40):
        b, s = rng.getrandbits(1), []
        for _ in range(10000):
            if rng.random() < p:
                b ^= 1
            s.append(b)
        markov.append(s)
    hm = {k: cond_entropy(markov, k) for k in range(1, 9)}
    report("ME0 known answers: the pure wheel gives < 0.005 at k >= 28; a Markov source gives its rate within 0.02",
           all(v < 0.005 for v in hw.values()) and all(abs(v - hp) <= 0.02 for v in hm.values()),
           "wheel " + ", ".join(f"k {k}: {v:.4f}" for k, v in hw.items()) + f"; Markov rate {hp:.4f}, estimates "
           + ", ".join(f"{v:.4f}" for v in hm.values()))

    seqs = []
    for _ in range(N):
        R = rng.getrandbits(2400) | (1 << 2399)        # wide enough never to run out of fresh cells
        seqs.append(column1_visible(R, T))
    h = {k: cond_entropy(seqs, k) for k in KS}
    print("   h_k (bits per visible bit): " + ", ".join(f"k {k}: {v:.4f}" for k, v in h.items()), flush=True)
    report("ME1 the estimate does not exceed the exact bound 0.1277 by more than 0.01", h[40] <= 0.1377,
           f"h_40 = {h[40]:.4f}")
    verdict("ME2 column 1 carries information at a positive rate: h_40 >= 0.04", h[40] >= 0.04, f"h_40 = {h[40]:.4f}")
    per_kick = h[40] * 44
    verdict("ME3 the information per kick (h_40 x 44 visible bits) lies between 2 and 12 bits", 2 <= per_kick <= 12,
            f"{per_kick:.2f} bits per kick")
    shuf = []
    for s in seqs[:60]:
        s2 = s[:]
        rng.shuffle(s2)
        shuf.append(s2)
    ones = sum(map(sum, shuf)) / sum(map(len, shuf))
    hb = -(ones * math.log2(ones) + (1 - ones) * math.log2(1 - ones))
    hs = cond_entropy(shuf, 4)
    report("CF shuffled bits give h_4 within 0.03 of the binary entropy of their frequency", abs(hs - hb) <= 0.03,
           f"h_4 shuffled {hs:.4f} (unshuffled {h[4]:.4f}); binary entropy {hb:.4f} (share of ones {ones:.3f})")
    hh = cond_entropy(seqs[: N // 2], 40)
    report("ST h_40 from half the sequences within 0.01 of all", abs(hh - h[40]) <= 0.01,
           f"half {hh:.4f}, all {h[40]:.4f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
