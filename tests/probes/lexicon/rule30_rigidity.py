#!/usr/bin/env python3
"""rule30_rigidity.py: left-side rigidity. With column 0 periodic, can ANY column 1 at all (not only one made by a
finite right half) force a left half that ends in zeros? Exhaustive over every column 1, from each starting depth.

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_rigidity.py [FREE_BITS=16] [JOBS=4] [PMAX=6]
COST:       minutes on 4 cores at the defaults.

The reduction (proved by hand and machine-checked here, check R1). Rule 30 gives x_t(-1) = x_{t+1}(0) + (x_t(0) OR
x_t(1)) mod 2. Where the trace tau(t) = x_t(0) is 1, the OR is 1 whatever x_t(1) is. So the forced left half depends
on column 1 only at the times where tau is 0: a primitive word with z zeros in its period p leaves z/p free bits per
left cell. The left half x_0(-k) is determined by tau and by column 1 at times 0..k-1. A finite configuration needs
the left half to be eventually zero: an infinite run of zeros. The search below is a depth-first search over column 1's
free bits, one cell at a time. From a starting depth d it requires every cell from d onward to be zero, and records
the longest run reached. It enumerates every free bit before d (so the maximum over all column 1 is exact), up to
FREE_BITS free bits before d.

PREDICTIONS, written 2026-10-04 before the first run (after rule30_periodic.py and a one-word exploration of the
alternating trace, in which the longest zero run from depth d, over every column 1, ended before depth 2.5d for
d <= 38):
  R1 (control): the left half never depends on column 1 at a time where tau = 1, and always changes when a bit at a
     time where tau = 0 is flipped (the second is not guaranteed in general: recorded, not required).
  R2 (control, the search can see an infinite run): for the word "0" (tau = 000...), column 1 = 000... gives the zero
     configuration, so the search must reach its cap (an "unbounded" run) from every starting depth.
  R3 (control): for the word "1" (tau = 111...) there are no free bits; the left half is the universal one,
     0,1,0,1,... (Condrey's universal fibre), so the longest zero run from any depth is 1.
  R4 (the conjecture, uncertain): for every primitive word of period p = 2..PMAX, from every starting depth tested,
     the longest zero run is finite and ends before depth 3d + 12. No run reaches the cap.
REFUTED-BY: R1-R3 failing (the instrument is wrong); for R4, any word whose search reaches the cap (a candidate
  column 1 forcing an eventually-zero left half: then for that word the obstruction must come from the right half),
  or a run ending at or beyond 3d + 12 (the doubling pattern does not hold).

OUTCOME of the first run (FREE_BITS 10, PMAX 4), recorded 2026-10-04: R1-R3 held. R4's main claim held: no word's
search reached the cap. R4's bound was REFUTED for two words, 0010 and 0100 (a run from depth 14 ends at 62). The exit
code reflects only the controls; a prediction prints HELD or REFUTED.

R5 is post hoc, added after that run, and is not a prediction. A finite configuration whose trace is exactly
periodic from t = 0 stays finite and keeps a periodic trace one step later, with the word rotated by one. So such a
configuration exists for one rotation of a cyclic word exactly when it exists for all of them. It is enough to rule
out one rotation per class, the most rigid one. R5 prints, for each cyclic class, the longest zero run of each
rotation over every depth tested.
"""
import sys
from itertools import product
from multiprocessing import Pool

FREE_BITS = int(sys.argv[1]) if len(sys.argv) > 1 else 16
JOBS = int(sys.argv[2]) if len(sys.argv) > 2 else 4
PMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 6
CAP = 400            # a run this long counts as unbounded
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def cell(tau_int, col1_int, k):
    """x_0(-k), forced by column 0 (tau) and column 1, both held as ints with bit t = time t, t = 0..k."""
    cols = [col1_int, tau_int]
    for j in range(1, k + 1):
        m = (1 << (k - j + 1)) - 1
        cols.append(((cols[-1] >> 1) ^ (cols[-1] | cols[-2])) & m)
    return cols[-1] & 1


def tau_int(word, n):
    return sum(word[t % len(word)] << t for t in range(n + 1))


def search(args):
    """Longest zero run from depth d, over every column 1 (free bits only at the zeros of tau)."""
    word, d, code = args
    T = tau_int(word, d + CAP + 2)
    zeros = [t for t in range(d + CAP + 2) if word[t % len(word)] == 0]
    before = [t for t in zeros if t < d - 1]           # free bits that cells 1..d-1 depend on, fixed by `code`
    col1 = 0
    for i, t in enumerate(before):
        col1 |= ((code >> i) & 1) << t
    best = 0
    stack = [(d, col1)]                               # next cell to force to zero, column 1 so far
    while stack:
        k, c1 = stack.pop()
        run = k - d
        if run > best:
            best = run
        if run >= CAP:
            return word, d, CAP
        t = k - 1                                     # cell k is the first to depend on column 1 at time k-1
        options = [c1, c1 | (1 << t)] if word[t % len(word)] == 0 else [c1]
        for c in options:
            if cell(T, c, k) == 0:
                stack.append((k + 1, c))
    return word, d, best


def primitive_words(p):
    return [w for w in product((0, 1), repeat=p)
            if all(any(w[i] != w[(i + q) % p] for i in range(p)) for q in range(1, p) if p % q == 0)]


def depths_for(word):
    """Every starting depth whose free bits before it number at most FREE_BITS."""
    out, d = [], 1
    while True:
        n = sum(1 for t in range(d - 1) if word[t % len(word)] == 0)
        if n > FREE_BITS or d > 200:
            return out
        out.append((d, n))
        d += 1


def main():
    import random
    rng = random.Random(4)
    # R0: the explicit columns for tau = 0101... (PRIZE-PROBLEMS.md section 7, Lemma 1), from the column recurrence
    K, okc, okp = 41, 0, 0
    T = tau_int((0, 1), K)
    for _ in range(2000):
        s = [rng.getrandbits(1) for _ in range(K + 1)]
        c1 = sum(b << t for t, b in enumerate(s))
        cols = [c1, T]
        for j in range(1, 3):
            m = (1 << (K - j + 1)) - 1
            cols.append(((cols[-1] >> 1) ^ (cols[-1] | cols[-2])) & m)
        cm1, cm2 = cols[2], cols[3]
        okc += all(((cm1 >> t) & 1) == (1 if t % 2 else 1 - s[t]) for t in range(K - 1)) and \
               all(((cm2 >> t) & 1) == (s[t] if t % 2 == 0 else s[t + 1]) for t in range(K - 2))
        okp += (cm1 & 1) + (cm2 & 1) == 1
    report("R0 tau = 0101...: column -1 = (not s(2u), 1), column -2 = (s(2u), s(2u+2)), x(-1) + x(-2) = 1",
           okc == 2000 and okp == 2000, f"{okc} and {okp} of 2000")
    # R1: the left half ignores column 1 where tau = 1
    ok = flips = total = 0
    for word in [w for p in range(1, 5) for w in primitive_words(p)]:
        K = 40
        T = tau_int(word, K)
        for _ in range(40):
            c1 = rng.getrandbits(K + 1)
            noise = sum(rng.getrandbits(1) << t for t in range(K + 1) if word[t % len(word)] == 1)
            ok += all(cell(T, c1, k) == cell(T, c1 ^ noise, k) for k in range(1, K))
            zt = [t for t in range(K // 2) if word[t % len(word)] == 0]
            if zt:
                t0 = rng.choice(zt)
                flips += any(cell(T, c1, k) != cell(T, c1 ^ (1 << t0), k) for k in range(1, K))
            total += 1
    report("R1 the left half never depends on column 1 where tau = 1", ok == total, f"{ok} of {total}")
    print(f"      (a flip where tau = 0 changed the left half in {flips} cases)")
    pool = Pool(JOBS)
    results = {}
    for p in range(1, PMAX + 1):
        for word in primitive_words(p):
            rows = []
            for d, n in depths_for(word):
                res = pool.map(search, [(word, d, c) for c in range(1 << n)], chunksize=max(1, (1 << n) // (8 * JOBS)))
                rows.append((d, max(r[2] for r in res)))
            results[word] = rows
    w0, w1 = (0,), (1,)
    report("R2 control: for tau = 000... the search reaches its cap from every depth (it can see an infinite run)",
           all(m >= CAP for _, m in results[w0]), f"depths 1..{len(results[w0])}")
    report("R3 control: for tau = 111... the longest zero run is 1 from every depth (the universal left half)",
           all(m <= 1 for _, m in results[w1]), f"max {max(m for _, m in results[w1])}")
    print()
    for p in range(2, PMAX + 1):
        for word in primitive_words(p):
            rows = results[word]
            capped = [d for d, m in rows if m >= CAP]
            worst = max(rows, key=lambda r: (r[0] + r[1]) / r[0])
            bad = [(d, m) for d, m in rows if d + m >= 3 * d + 12]
            verdict(f"R4 word {''.join(map(str, word))}: every zero run ends, and before depth 3d+12",
                   not capped and not bad,
                   f"depths 1..{rows[-1][0]}; latest end {worst[0] + worst[1] - 1} from depth {worst[0]}"
                   + (f"; CAPPED at depths {capped[:5]}" if capped else "") + (f"; late ends {bad[:5]}" if bad else ""))
    print("\nR5 (post hoc) the longest zero run of each rotation, over every depth tested, by cyclic class:")
    seen = set()
    for p in range(2, PMAX + 1):
        for word in primitive_words(p):
            rots = sorted({word[i:] + word[:i] for i in range(p)})
            if rots[0] in seen:
                continue
            seen.add(rots[0])
            cells = []
            for r in rots:
                d, m = max(results[r], key=lambda x: x[1])
                cells.append(f"{''.join(map(str, r))}: {m}" + (" (CAP)" if m >= CAP else f" (from depth {d})"))
            best = min(rots, key=lambda r: max(m for _, m in results[r]))
            print(f"   class of {''.join(map(str, rots[0]))}: " + "; ".join(cells)
                  + f"  -> most rigid rotation {''.join(map(str, best))}")
    pool.close()
    print(f"\n{'ALL CONTROLS PASS' if FAILS == 0 else f'{FAILS} CONTROL FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
