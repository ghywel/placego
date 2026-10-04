#!/usr/bin/env python3
"""rule30_twosided.py: the right side as a constraint on column 1. With column 0 periodic, the left side needs a column 1
whose forced left half ends in zeros (rule30_rigidity.py). The right side limits which columns 1 can occur at all. Does
the combination close the gap that the left side alone leaves open?

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_twosided.py [DMAX=60] [JOBS=4] [WORDS=01,10,001,010,100,0001,0010,0100,1000]
COST:       minutes on 4 cores at the defaults.

The constraint (proved here, checked as T1). At column 1, Rule 30 reads sigma(t+1) = tau(t) + (sigma(t) OR x_t(2))
mod 2, where tau is column 0 and sigma is column 1. Whatever column 2 does:
  C0: where tau(t) = 0, sigma(t+1) = sigma(t) OR x_t(2), so sigma(t) = 1 forces sigma(t+1) = 1;
  C1: where tau(t) = 1, sigma(t+1) = NOT (sigma(t) OR x_t(2)), so sigma(t+1) = 1 forces sigma(t) = 0.
For the alternating trace these give: e(s) = sigma at the zero times never has two ones in a row (T2).

PREDICTIONS, written 2026-10-04 before the first run (the owner's suggestion, the same day, to use the right side as
a complementary constraint):
  T1 (a proof, checked as a control): C0 and C1 hold for column 1 of every right half tried. Counterfactual: random
     sequences violate them (the constraint is not vacuous).
  T2 (a consequence, control): for the traces 0101... and 1010..., column 1 at the zero times has no "11".
  T3 (a measurement, no prediction of its size): the exact set of column-1 prefixes that some right half produces,
     against the set allowed by C0 and C1. If it is smaller, the right side constrains column 1 beyond C0 and C1.
  T4 (the experiment, uncertain): searching only columns 1 that satisfy C0 and C1, the longest zero run of the forced
     left half from depth d no longer grows with d for the alternating trace. It stays at or below 16 for every d
     tested, where the left side alone allows runs of about d.
REFUTED-BY: T1 or T2 failing (the derivation is wrong); for T4, a run longer than 16 for the alternating trace at any
  depth tested, or a clear growth with d.
"""
import random, sys
from multiprocessing import Pool

DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 60
JOBS = int(sys.argv[2]) if len(sys.argv) > 2 else 4
WORDS = [tuple(int(c) for c in w) for w in (sys.argv[3] if len(sys.argv) > 3 else
                                             "01,10,001,010,100,0001,0010,0100,1000").split(",")]
CAP = 400
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def step(row):
    return (row << 1) ^ (row | (row >> 1))


def column1(R, word, n):
    """Column 1 at times 0..n-1 for the right half R (bit i-1 = cell i) with column 0 clamped to the periodic word."""
    tau = [word[t % len(word)] for t in range(n + 1)]
    mask = (1 << (R.bit_length() + n + 3)) - 1
    row, out = tau[0] | (R << 1), []
    for t in range(n):
        out.append((row >> 1) & 1)
        row = (step(row) & mask & ~1) | tau[t + 1]
    return out


def allowed(sigma, word):
    """C0 and C1 between consecutive times."""
    for t in range(len(sigma) - 1):
        if word[t % len(word)] == 0 and sigma[t] == 1 and sigma[t + 1] == 0:
            return False
        if word[t % len(word)] == 1 and sigma[t + 1] == 1 and sigma[t] == 1:
            return False
    return True


def cell(tau_int, col1_int, k):
    cols = [col1_int, tau_int]
    for j in range(1, k + 1):
        m = (1 << (k - j + 1)) - 1
        cols.append(((cols[-1] >> 1) ^ (cols[-1] | cols[-2])) & m)
    return cols[-1] & 1


def tau_int(word, n):
    return sum(word[t % len(word)] << t for t in range(n + 1))


def states_before(word, d):
    """Every (zero-time bits of column 1 over times 0..d-2, sigma(d-2)) that C0 and C1 allow. The left half depends only
    on the zero-time bits (rule30_rigidity.py, Lemma 1); the future constraint only on the last value."""
    states = {(0, 0), (1 if word[0] == 0 else 0, 1)}
    for t in range(1, d - 1):
        new = set()
        for bits, last in states:
            for b in (0, 1):
                if word[(t - 1) % len(word)] == 0 and last == 1 and b == 0:
                    continue
                if word[(t - 1) % len(word)] == 1 and b == 1 and last == 1:
                    continue
                nb = bits | (b << t) if word[t % len(word)] == 0 else bits
                new.add((nb, b))
        states = new
    return sorted(states)


def run_from(args):
    """Longest zero run from depth d, over columns 1 allowed by C0 and C1 that start in this state."""
    word, d, (bits, last) = args
    T = tau_int(word, d + CAP + 2)
    best, stack = 0, [(d, bits, last)]
    while stack:
        k, c1, prev = stack.pop()
        if k - d > best:
            best = k - d
        if k - d >= CAP:
            return CAP
        t = k - 1                                        # cell k is the first to see column 1 at time k-1
        for b in (0, 1):
            if t >= 1 and word[(t - 1) % len(word)] == 0 and prev == 1 and b == 0:
                continue
            if t >= 1 and word[(t - 1) % len(word)] == 1 and b == 1 and prev == 1:
                continue
            c = c1 | (b << t) if word[t % len(word)] == 0 else c1
            if cell(T, c, k) == 0:
                stack.append((k + 1, c, b))
    return best


def run_from_free(args):
    """The same search with no right-side constraint (rule30_rigidity.py's), for the side-by-side comparison."""
    word, d, code = args
    T = tau_int(word, d + CAP + 2)
    zeros = [t for t in range(d - 1) if word[t % len(word)] == 0]
    c1 = sum(((code >> i) & 1) << t for i, t in enumerate(zeros))
    best, stack = 0, [(d, c1)]
    while stack:
        k, c = stack.pop()
        best = max(best, k - d)
        if k - d >= CAP:
            return CAP
        t = k - 1
        for cc in ([c, c | (1 << t)] if word[t % len(word)] == 0 else [c]):
            if cell(T, cc, k) == 0:
                stack.append((k + 1, cc))
    return best


def main():
    rng = random.Random(30)
    # T1 and T2
    ok = total = 0
    for word in WORDS:
        for _ in range(300):
            R = rng.getrandbits(rng.randint(1, 20))
            s = column1(R, word, 40)
            ok += allowed(s, word)
            total += 1
    report("T1 C0 and C1 hold for column 1 of every right half tried", ok == total, f"{ok} of {total}")
    viol = sum(not allowed([rng.getrandbits(1) for _ in range(40)], w) for w in WORDS for _ in range(100))
    report("T1 counterfactual caught: random sequences violate C0/C1", viol > 0, f"{viol} of {100 * len(WORDS)} random")
    ok2 = tot2 = 0
    for word in [(0, 1), (1, 0)]:
        z = [t for t in range(40) if word[t % 2] == 0]
        for _ in range(500):
            s = column1(rng.getrandbits(rng.randint(1, 20)), word, 40)
            e = [s[t] for t in z]
            ok2 += all(not (e[i] and e[i + 1]) for i in range(len(e) - 1))
            tot2 += 1
    report("T2 for 0101... and 1010..., column 1 at the zero times has no 11", ok2 == tot2, f"{ok2} of {tot2}")
    # T3: the exact language of column-1 prefixes against C0/C1
    print("\nT3 column-1 prefixes of length n: produced by some right half of width n / allowed by C0,C1 / all 2^n")
    from itertools import product
    for word in WORDS[:3]:
        cells = []
        for n in ((6, 10, 14, 20) if word in [(0, 1), (1, 0)] else (6, 10, 14)):
            exact = {tuple(column1(R, word, n)) for R in range(1 << n)}
            allow = sum(allowed(list(s), word) for s in product((0, 1), repeat=n))
            cells.append(f"n={n}: {len(exact)} / {allow} / {1 << n}")
        print(f"   word {''.join(map(str, word))}: " + "; ".join(cells))
    # T5 (a measurement, no prediction): long columns 1 from random right halves. Are they eventually periodic, how
    # many distinct factors do they have, and do different right halves give the same sequence up to a time shift?
    print("\nT5 long columns 1 (3000 steps) from 40 random right halves of width 1..40:")
    for word in [(0, 1), (1, 0)]:
        seqs = []
        for _ in range(40):
            w = rng.randint(1, 40)
            seqs.append(column1(rng.getrandbits(w) | (1 << (w - 1)), word, 3000))
        s = seqs[0][1000:]
        comp = [len({tuple(s[i:i + n]) for i in range(len(s) - n)}) for n in (4, 8, 16, 32, 64)]
        per = next((q for q in range(1, 600) if all(s[i] == s[i + q] for i in range(len(s) - q))), None)
        ref = "".join(map(str, seqs[0][1000:3000]))
        same = sum("".join(map(str, q[2000:2200])) in ref for q in seqs[1:])
        print(f"   word {''.join(map(str, word))}: tail eventually periodic: {per is not None}; distinct factors of "
              f"length 4, 8, 16, 32, 64 in 2000 cells: {comp}; tails found inside the first one's: {same} of 39")
    # T6 (a measurement, no prediction): is column 1 generated by a finite automaton in base 2 (a finite 2-kernel),
    # and how does its pattern count grow on long runs? Controls: a random sequence (kernel doubles) and Thue-Morse
    # (2-automatic: kernel 2).
    print("\nT6 columns 1 over 65536 steps: 2-kernel size (prefix 48), k = 0..9, and distinct patterns of length")
    print("   8, 16, 32, 64, 128, 256 after the first 4096 steps:")
    rng6 = random.Random(3)
    N = 1 << 16
    def kernel(s, L=48, kmax=9):
        return [len({tuple(s[r + (1 << k) * n] for n in range(L)) for r in range(1 << k) if r + (1 << k) * (L - 1) < len(s)})
                for k in range(kmax + 1)]
    for word in [(0, 1), (1, 0)]:
        for _ in range(3):
            w = rng6.randint(1, 30)
            s = column1(rng6.getrandbits(w) | (1 << (w - 1)), word, N)
            st = "".join(map(str, s[4096:]))
            pc = [len({st[i:i + n] for i in range(len(st) - n)}) for n in (8, 16, 32, 64, 128, 256)]
            per = next((q for q in range(1, 4097) if st[-8192:] == st[-8192 - q:-q]), None)
            print(f"   word {''.join(map(str, word))}, right half width {w:>2}: kernel {kernel(s)}; patterns {pc}; "
                  f"tail period {per}")
    rs = [rng6.getrandbits(1) for _ in range(N)]
    print(f"   control, random: kernel {kernel(rs)}")
    print(f"   control, Thue-Morse: kernel {kernel([bin(n).count('1') % 2 for n in range(N)])}")
    # T4: two-sided against left-only
    print()
    with Pool(JOBS) as pool:
        for word in WORDS:
            rows = []
            for d in range(2, DMAX + 1):
                st = states_before(word, d)
                if len(st) > 300000:
                    break
                two = max(pool.map(run_from, [(word, d, s) for s in st], chunksize=max(1, len(st) // (8 * JOBS))))
                nfree = len([t for t in range(d - 1) if word[t % len(word)] == 0])
                free = max(pool.map(run_from_free, [(word, d, c) for c in range(1 << nfree)],
                                    chunksize=max(1, (1 << nfree) // (8 * JOBS)))) if nfree <= 16 else None
                rows.append((d, two, free))
            worst = max(r[1] for r in rows)
            text = " ".join(f"{d}:{t}" + (f"/{f}" if f is not None else "") for d, t, f in rows[::4])
            print(f"   word {''.join(map(str, word))}: depth:two-sided/left-only (every 4th depth)  {text}", flush=True)
            if word in [(0, 1), (1, 0)]:
                verdict(f"T4 word {''.join(map(str, word))}: two-sided longest zero run <= 16 at every depth 2..{rows[-1][0]}",
                        worst <= 16, f"worst {worst}")
            else:
                print(f"      longest two-sided run over depths 2..{rows[-1][0]}: {worst}" + (" (CAP)" if worst >= CAP else ""))
    print(f"\n{'ALL CONTROLS PASS' if FAILS == 0 else f'{FAILS} CONTROL FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
