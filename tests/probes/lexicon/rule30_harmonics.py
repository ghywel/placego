#!/usr/bin/env python3
"""rule30_harmonics.py: the owner's "harmonics" lead (2026-10-04). Are the quantised two-sided run lengths of
RULE30-PRIZE.md section 8.2 harmonics of column 0's period p?

RUN-ON:     cpu (pure Python 3, standard library; exact for the two-sided arm, seeded for the left-alone arm)
COMMAND:    python3 tests/probes/lexicon/rule30_harmonics.py [W=16] [K=192] [JOBS=4]
COST:       a few minutes on 4 cores.

The owner: "The right side changes nothing alone, the left side alone is close to random, and together they produce
sharp, quantised behaviour ... this sounds very much like harmonics." For trace 0101... (p = 2) the long runs step by
2 (12, 14, 16). If that is a harmonic of the trace, then for a word of period p the interaction's structure should
sit at p and its multiples. Two statistics, each comparing "both sides exact" (every right half up to W cells) with
"left alone" (the same number of seeded random columns 1), so that only the interaction is measured:
  D(q)  the total-variation distance between the two arms' distributions of (run length mod q), over zero runs of 6
        or more cells that end inside the window; q = 2..5.
  X(j)  the excess correlation of the left half at lag j, with s = 2L - 1:  X(j) = A_both(j) - A_left(j), where
        A(j) is the mean of s(k) s(k+j) over k and over samples; j = 1..12.

PREDICTIONS, written 2026-10-04 before this script's first run (blind for the five words of period 3 and 4; 01 and
10 are shown but were looked at before):
  H1: for each of 001, 011, 0001, 0011, 0111, D(p) exceeds D(q) for every q in 2..5 that does not divide p. (D(4) is
      never below D(2), because mod 4 refines mod 2, so for p = 4 the comparison is with q = 3 and 5.)
  H2: for each of the same five words, the lag j in 2..12 with the largest |X(j)| is a multiple of p. (By chance:
      4 of 11 lags for p = 3, 3 of 11 for p = 4.)
  C (control, the noise floor): two independent left-alone samples of the same size differ by at most 0.01 in every
      D(q) and at most 0.005 in every X(j), so that the effects above are not sampling noise.
REFUTED-BY: C failing (the instrument cannot see the effect size); H1 or H2 failing for any of the five words.

OUTCOME of the first run, 2026-10-04 (W = 16, K = 192): C passed (largest gaps 0.0043 in D, 0.0008 in X). H1 and H2
were REFUTED for all five words. The interaction is real (up to 0.27 in D and 0.23 in X, against a floor of 0.004 and
0.001), but it does not sit at multiples of p. The strongest lag is 7 for all three words of period 4 (X(7) = +0.139,
+0.197, +0.227), 5 for 001, 11 for 011; for 01 and 10, 5 and 2, and weak. Lag 7 is the 7-cell ring, whose 4-cycles
have columns 0001, 0011 and 0111 (section 5): a resonance with Rule 30's own ring orbits, followed up in
rule30_resonance.py. A flaw found on reading: X(j) includes the squared mean of s, so a density difference between
the arms raises every lag (visible for 0011); the follow-up subtracts it.
"""
import random, sys, pathlib
from collections import Counter
from multiprocessing import Pool

W = int(sys.argv[1]) if len(sys.argv) > 1 else 16
K = int(sys.argv[2]) if len(sys.argv) > 2 else 192
JOBS = int(sys.argv[3]) if len(sys.argv) > 3 else 4
WORDS = [(0, 1), (1, 0), (0, 0, 1), (0, 1, 1), (0, 0, 0, 1), (0, 0, 1, 1), (0, 1, 1, 1)]
BLIND = WORDS[2:]
QS = [2, 3, 4, 5]
LAGS = list(range(1, 13))
MINRUN = 6

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


def stats(L):
    """Run-length residues and lag agreements of one left half L(1..K)."""
    res = Counter()
    run = 0
    for b in L:
        if b == 0:
            run += 1
        else:
            if run >= MINRUN:
                for q in QS:
                    res[(q, run % q)] += 1
            run = 0
    x = sum(b << k for k, b in enumerate(L))
    agree = [K - j - bin((x ^ (x >> j)) & ((1 << (K - j)) - 1)).count("1") for j in LAGS]
    return res, agree


def merge(parts):
    res, agree, n = Counter(), [0] * len(LAGS), 0
    for r, a, m in parts:
        res.update(r)
        agree = [u + v for u, v in zip(agree, a)]
        n += m
    return res, agree, n


def both_chunk(args):
    word, lo, hi = args
    tau = [word[t % len(word)] for t in range(K + 1)]
    res, agree = Counter(), [0] * len(LAGS)
    for R in range(lo, hi):
        r, a = stats(r30.forced_left(R, tau, K))
        res.update(r)
        agree = [u + v for u, v in zip(agree, a)]
    return res, agree, hi - lo


def left_chunk(args):
    word, seed, n = args
    rng = random.Random(seed)
    tau = [word[t % len(word)] for t in range(K + 1)]
    c0 = sum(b << t for t, b in enumerate(tau))
    res, agree = Counter(), [0] * len(LAGS)
    for _ in range(n):
        cols, L = [rng.getrandbits(K + 1), c0], []
        for k in range(1, K + 1):
            m = (1 << (K - k + 1)) - 1
            cols.append(((cols[-1] >> 1) ^ (cols[-1] | cols[-2])) & m)
            L.append(cols[-1] & 1)
        r, a = stats(L)
        res.update(r)
        agree = [u + v for u, v in zip(agree, a)]
    return res, agree, n


def dist(res, q):
    tot = sum(res[(q, r)] for r in range(q))
    return [res[(q, r)] / tot for r in range(q)] if tot else [0.0] * q


def tv(a, b, q):
    return 0.5 * sum(abs(u - v) for u, v in zip(dist(a, q), dist(b, q)))


def corr(agree, n):
    """A(j): the mean of s(k) s(k+j) = (agreements - disagreements) / pairs."""
    return [(2 * a - n * (K - j)) / (n * (K - j)) for a, j in zip(agree, LAGS)]


def main():
    N = 1 << W
    floor_d = floor_x = 0.0
    with Pool(JOBS) as pool:
        for word in WORDS:
            name, p = "".join(map(str, word)), len(word)
            both = merge(pool.map(both_chunk, [(word, lo, min(lo + 2048, N)) for lo in range(0, N, 2048)]))
            seeds = [(word, 7919 * p + s, N // 32) for s in range(32)]
            left = merge(pool.map(left_chunk, seeds))
            if word in ((0, 1), (0, 0, 1)):              # the noise floor, on one word of each kind
                left2 = merge(pool.map(left_chunk, [(word, 104729 + 7919 * p + s, N // 32) for s in range(32)]))
                floor_d = max(floor_d, max(tv(left[0], left2[0], q) for q in QS))
                floor_x = max(floor_x, max(abs(u - v) for u, v in zip(corr(left[1], left[2]), corr(left2[1], left2[2]))))
            D = {q: tv(both[0], left[0], q) for q in QS}
            X = [u - v for u, v in zip(corr(both[1], both[2]), corr(left[1], left[2]))]
            print(f"\nword {name} (p = {p}): runs of {MINRUN}+ counted, both {sum(both[0][(2, r)] for r in range(2))}, "
                  f"left alone {sum(left[0][(2, r)] for r in range(2))}")
            print("   D(q), q = 2..5:  " + "  ".join(f"{q}: {D[q]:.4f}" for q in QS))
            print("   X(j), j = 1..12: " + "  ".join(f"{j}: {x:+.4f}" for j, x in zip(LAGS, X)))
            jmax = max(range(1, len(LAGS)), key=lambda i: abs(X[i])) + 1      # lags 2..12
            others = [q for q in QS if p % q != 0 and q != p]
            h1 = all(D[p] > D[q] for q in others)
            h2 = jmax % p == 0
            if word in BLIND:
                verdict(f"H1 word {name}: D({p}) above D(q) for q = {others}", h1,
                        "; ".join(f"D({q}) = {D[q]:.4f}" for q in [p] + others))
                verdict(f"H2 word {name}: the strongest lag in 2..12 is a multiple of {p}", h2,
                        f"strongest lag {jmax}, X = {X[jmax - 1]:+.4f}")
            else:
                print(f"   (looked at before, not blind) H1 form: {h1}; H2 form: strongest lag {jmax}")
    report("C noise floor: two left-alone samples agree within 0.01 in D and 0.005 in X",
           floor_d <= 0.01 and floor_x <= 0.005, f"largest D gap {floor_d:.4f}, largest X gap {floor_x:.4f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
