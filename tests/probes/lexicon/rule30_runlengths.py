#!/usr/bin/env python3
"""rule30_runlengths.py: the lengths of zero runs in the forced left half, both sides exact, against the left side
alone; the cells around each long run (templates); and the Fibonacci and Pell counts of Lemma 3's envelope.

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_runlengths.py [W=18] [K=192] [JOBS=4]
PREDICTION: none for the histograms and templates (a measurement, after the owner asked on 2026-10-04 why runs of 13
            were missing). P1 is a theorem, checked: for the trace 0101..., the column-1 sequences that Lemma 3's two rules
            allow number S(m) for length 2m, with S(1) = 3, S(2) = 7, S(m+1) = 2 S(m) + S(m-1) (the half-companion Pell
            numbers); restricted to the zero times, they are the words with no "11", counted by Fibonacci F(m+2).
COST:       about a minute and a half on 4 cores.

Proof of P1. Lemma 3 (PRIZE-PROBLEMS.md section 8) forbids the pair (sigma(2s), sigma(2s+1)) = (1, 0), and forbids a pair
ending in 1 followed by a pair starting with 1. So the pairs are 00, 01, 11, and with a, b, c the numbers of words of m
pairs ending in 00, 01, 11: a' = b' = a + b + c, c' = a. Then S = a + b + c satisfies S(m+1) = 2 S(m) + S(m-1). At the
zero times alone, e(s) = 1 forces e(s-1) = 0, and any word with no "11" extends to a full column 1 (choose sigma(2s+1)
= 1 after e(s) = 1, 0 before e(s+1) = 1; both cannot be required), so they are exactly the Fibonacci-counted words.
"""
import random, sys, pathlib
from collections import Counter, defaultdict
from itertools import product
from multiprocessing import Pool

W = int(sys.argv[1]) if len(sys.argv) > 1 else 18
K = int(sys.argv[2]) if len(sys.argv) > 2 else 192
JOBS = int(sys.argv[3]) if len(sys.argv) > 3 else 4
F = 10

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
import rule30_twosided as ts                           # noqa: E402
sys.argv = _argv
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def runs_of(L):
    out, run = [], 0
    for k, b in enumerate(L, 1):
        if b == 0:
            run += 1
        else:
            if run:
                out.append((run, k - run))                 # (length, first zero's depth); an open run is dropped
            run = 0
    return out


def both_chunk(args):
    word, lo, hi = args
    tau = [word[t % len(word)] for t in range(K + 1)]
    hist, ctx = Counter(), defaultdict(Counter)
    for R in range(lo, hi):
        L = r30.forced_left(R, tau, K)
        for n, s in runs_of(L):
            hist[n] += 1
            if 11 <= n <= 20 and s - 1 - F >= 0 and s + n - 1 + F <= K:
                ctx[n][("".join(map(str, L[s - 1 - F:s - 1])), "".join(map(str, L[s + n - 1:s + n + F])))] += 1
    return hist, ctx


def left_chunk(args):
    word, seed, n = args
    rng = random.Random(seed)
    tau = [word[t % len(word)] for t in range(K + 1)]
    c0 = sum(b << t for t, b in enumerate(tau))
    hist = Counter()
    for _ in range(n):
        cols, L = [rng.getrandbits(K + 1), c0], []
        for k in range(1, K + 1):
            m = (1 << (K - k + 1)) - 1
            cols.append(((cols[-1] >> 1) ^ (cols[-1] | cols[-2])) & m)
            L.append(cols[-1] & 1)
        for n_, _ in runs_of(L):
            hist[n_] += 1
    return hist


def main():
    # P1: the Pell and Fibonacci counts, against brute force
    word = (0, 1)
    pell = [3, 7]
    while len(pell) < 12:
        pell.append(2 * pell[-1] + pell[-2])
    brute = {m: sum(ts.allowed(list(s), word) for s in product((0, 1), repeat=2 * m)) for m in range(1, 9)}
    report("P1 Lemma 3's envelope for 0101...: S(m) = 3, 7, 17, 41, ... (Pell), against brute force for m = 1..8",
           all(brute[m] == pell[m - 1] for m in brute), str([brute[m] for m in sorted(brute)]))
    fib = [1, 2]
    while len(fib) < 14:
        fib.append(fib[-1] + fib[-2])
    zero_words = {}
    for m in range(1, 9):
        zs = set()
        for s in product((0, 1), repeat=2 * m):
            if ts.allowed(list(s), word):
                zs.add(s[0::2])
        zero_words[m] = len(zs)
    report("P1 ... restricted to the zero times: the words with no 11, F(m+2) = 2, 3, 5, 8, 13, ...",
           all(zero_words[m] == fib[m] for m in zero_words), str([zero_words[m] for m in sorted(zero_words)]))
    with Pool(JOBS) as pool:
        for word in [(0, 1), (1, 0)]:
            name = "".join(map(str, word))
            H, C = Counter(), defaultdict(Counter)
            for h, c in pool.map(both_chunk, [(word, lo, min(lo + 4096, 1 << W)) for lo in range(0, 1 << W, 4096)]):
                H.update(h)
                for n, cc in c.items():
                    C[n].update(cc)
            Lh = Counter()
            for h in pool.map(left_chunk, [(word, s, (1 << W) // 32) for s in range(32)]):
                Lh.update(h)
            print(f"\ntrace {name}...: zero runs in the forced left half, depth <= {K}, by length")
            print(f"   both, every right half up to {W} cells: " + ", ".join(f"{n}: {H[n]}" for n in range(8, 22)))
            print(f"   left alone, {1 << W} random columns 1:  " + ", ".join(f"{n}: {Lh[n]}" for n in range(8, 22)))
            print(f"   templates (the {F} cells either side of each run, both sides exact):")
            for n in sorted(C):
                cc, total = C[n], sum(C[n].values())
                top = cc.most_common(2)
                share = sum(v for _, v in top) / total
                print(f"      run of {n:>2}: {total:>5} runs, {len(cc):>4} distinct surroundings; the two commonest "
                      f"cover {share:.0%}: " + "; ".join(f"{b}[0x{n}]{a} x{v}" for (b, a), v in top))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
