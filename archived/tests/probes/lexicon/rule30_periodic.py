#!/usr/bin/env python3
"""rule30_periodic.py: can a finite Rule 30 configuration have a periodic column? Periods 1 to 6, exhaustively over
small right halves, by the inverse (left-permutive) construction, with the published period-1 result as the control.

RUN-ON:     cpu (pure Python 3, standard library; exact bit arithmetic, no floating point anywhere)
COMMAND:    python3 tests/probes/lexicon/rule30_periodic.py [W_brute=7] [W_inverse=14] [K=192] [JOBS=1] [PERIODS=1-6]
COST:       4m38s on one core at the defaults (Cloud, 2026-10-04). The inverse search doubles with each step of
            W_inverse and grows linearly in K; JOBS splits it across processes (the standard library's
            multiprocessing). Local's job (CLOUD-LOCAL.md): 7 20 256 10 1-6 on the M5, an estimated 1-2 hours.

Background. Rule 30 is x'(i) = x(i-1) + x(i) + x(i+1) + x(i)x(i+1) mod 2 (LEXICON.md 3.5), linear in x(i-1). So
the column-0 trace t -> x_t(0) and the right half x_0(1..) determine the whole left half uniquely: x_t(-1) =
x_{t+1}(0) + (x_t(0) OR x_t(1)), and so on leftwards. A finite configuration whose column 0 is eventually periodic
with period p, shifted in time, is a finite configuration whose column 0 is exactly p-periodic from t = 0. So for a
given p the question is whether some finite right half R and some primitive word of length p force a left half that
is eventually zero. Condrey (arXiv:2609.09431, 2026-09-08) settled p = 1: no nonzero finite configuration has an
eventually constant column. Jen (Physica D 45, 1990) showed that two ADJACENT columns are never both eventually
periodic. Rule 30 Prize Problem 1 asks about ONE column (the centre, from a single black cell), for every p.

PREDICTIONS, written 2026-10-04 before the first run:
  A (control, a published theorem): brute force over every nonzero configuration with support in [-w, w], w = 1..7,
    reproduces Condrey's sharp constant-prefix maxima, 2*ceil(w/2)+1 (centre 0) and 2*floor(w/2)+2 (centre 1), the
    overall maximum w+2, and the number of maximisers, 2^w (w even) and 2^w - 1 (w odd). If it does not, the first
    suspect is our reading of "support radius" and "prefix length", not the theorem.
  B (control): for the constant traces the forced left half is eventually alternating (period 2) and never eventually
    zero, for every nonzero right half; for the all-ones trace it is the same for every right half.
  C (control of the construction): every forced configuration, cut at depth K, reproduces its requested trace for
    the first K/2 steps when simulated forwards; flipping one cell of its left half at depth k breaks the trace at
    exactly t = k (caught).
  D (the new case, uncertain): for p = 2 (traces 0101... and 1010...), no right half with support in [1, W_inverse]
    forces a left half that is eventually zero (no finite configuration with a period-2 column of that right
    extent). The same for p = 3..6. The tail structure of the forced left halves is recorded, not predicted.
  E (uncertain): the brute-force maximum length for which a nonzero configuration's trace follows its first p values
    grows linearly in w for each p <= 6, like p = 1's w + 2.
REFUTED-BY: A or B or C failing (the instrument is wrong; nothing after it counts); for D, any right half whose forced
  left half is eventually zero over its last 64 cells. That would be a CANDIDATE finite configuration with a periodic
  column, and it would have to be confirmed by simulating it forwards.
"""
import sys
from itertools import product
from multiprocessing import Pool

W_BRUTE = int(sys.argv[1]) if len(sys.argv) > 1 else 7
W_INV = int(sys.argv[2]) if len(sys.argv) > 2 else 14
K = int(sys.argv[3]) if len(sys.argv) > 3 else 192
JOBS = int(sys.argv[4]) if len(sys.argv) > 4 else 1
PERIODS = (lambda s: range(int(s.split("-")[0]), int(s.split("-")[-1]) + 1))(sys.argv[5] if len(sys.argv) > 5 else "1-6")
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def step(row):
    """One Rule 30 step on a row held as an int, bit b = cell b (cells must stay away from bit 0)."""
    return (row << 1) ^ (row | (row >> 1))


def trace(cfg_bits, centre_bit, T):
    row, out = cfg_bits, []
    for _ in range(T):
        out.append((row >> centre_bit) & 1)
        row = step(row)
    return out


def follow_len(tr, p):
    """How long the trace follows its own first p values: the largest l with tr[t] == tr[t - p] for p <= t < l."""
    for t in range(p, len(tr)):
        if tr[t] != tr[t - p]:
            return t
    return len(tr)


# ---- A and E: brute force over every configuration of support radius w ------------------------------------------
def brute(wmax, pmax=6):
    rows = []
    for w in range(1, wmax + 1):
        T = 8 * w + 40
        off = T + w + 2                                   # keeps the light cone off bit 0
        best = {p: 0 for p in range(1, pmax + 1)}
        best_c = {0: 0, 1: 0}
        count_at = {}
        for bits in range(1, 1 << (2 * w + 1)):
            cfg = bits << (off - w)                       # support in [-w, w], centre at bit off
            tr = trace(cfg, off, T)
            c = tr[0]
            l1 = follow_len(tr, 1)
            if l1 >= T:
                return None, f"w={w}: a configuration's trace stayed constant for all {T} steps"
            best_c[c] = max(best_c[c], l1)
            count_at[l1] = count_at.get(l1, 0) + 1
            for p in range(1, pmax + 1):
                lp = follow_len(tr, p)
                if lp >= T:
                    return None, f"w={w}, p={p}: a trace stayed {p}-periodic for all {T} steps: CANDIDATE {bits:b}"
                best[p] = max(best[p], lp)
        rows.append((w, best_c, best, count_at.get(w + 2, 0)))
    return rows, ""


# ---- B, C, D: the inverse construction ---------------------------------------------------------------------------
def forced_left(R, tau, K):
    """Left half x_0(-1..-K) forced by the right half R (bit i-1 = cell i, i >= 1) and the trace tau[0..K].
    Exact: the right side is evolved with column 0 clamped to tau; the left columns follow from left-permutivity."""
    width = R.bit_length() + K + 3
    mask = (1 << width) - 1
    row = tau[0] | (R << 1)
    col1 = 0
    for t in range(K + 1):
        col1 |= ((row >> 1) & 1) << t
        if t < K:
            row = (step(row) & mask & ~1) | tau[t + 1]
    col0 = sum(b << t for t, b in enumerate(tau[:K + 1]))
    cols = [col1, col0]                                 # cols[-1] = column -k+1, cols[-2] = column -k+2
    left = []
    for k in range(1, K + 1):
        m = (1 << (K - k + 1)) - 1                      # column -k is known for t = 0 .. K-k
        c = ((cols[-1] >> 1) ^ (cols[-1] | cols[-2])) & m
        left.append(c & 1)
        cols.append(c)
    return left


def tail_kind(left, n=64):
    tail = left[-n:]
    if not any(tail):
        return "ZERO"
    for q in range(1, 33):
        if all(tail[i] == tail[i + q] for i in range(n - q)):
            return f"period {q}"
    return "aperiodic over the last 64"


def primitive_words(p):
    out = []
    for w in product((0, 1), repeat=p):
        if all(any(w[i] != w[(i + d) % p] for i in range(p)) for d in range(1, p) if p % d == 0):
            out.append(w)
    return out


def check_construction(rng_words, K):
    """C: a forced configuration cut at depth K reproduces its trace for K/2 steps; a flipped cell at depth k breaks
    the trace at exactly t = k."""
    ok = flips = flips_ok = total = 0
    for word in rng_words:
        for R in (1, 0b1011, 0b110010111):
            tau = [word[t % len(word)] for t in range(K + 1)]
            L = forced_left(R, tau, K)
            off = 2 * K + 8
            cfg = (tau[0] << off) | (R << (off + 1))
            for k, b in enumerate(L, 1):
                cfg |= b << (off - k)
            tr = trace(cfg, off, K // 2)
            ok += tr == tau[:K // 2]
            total += 1
            k = K // 4
            bad = trace(cfg ^ (1 << (off - k)), off, K // 2)
            flips += 1
            first = next((t for t in range(K // 2) if bad[t] != tau[t]), None)
            flips_ok += first == k
    report("C forced configuration cut at depth K reproduces its trace for K/2 steps", ok == total, f"{ok} of {total}")
    report("C counterfactual caught: one flipped cell at depth k breaks the trace at exactly t = k",
           flips_ok == flips, f"{flips_ok} of {flips}")


def search_chunk(args):
    """One slice of the inverse search: right halves lo..hi-1 against one trace word."""
    word, lo, hi, K, want_prefixes = args
    p = len(word)
    tau = [word[t % p] for t in range(K + 1)]
    kinds, zero, prefixes = {}, [], set()
    for R in range(lo, hi):
        if R == 0 and not any(word):
            continue                                  # the zero configuration itself
        L = forced_left(R, tau, K)
        kind = tail_kind(L)
        kinds[kind] = kinds.get(kind, 0) + 1
        if kind == "ZERO" and len(zero) < 20:
            zero.append((word, R))
        if want_prefixes:
            prefixes.add(tuple(L[:32]))
    return word, kinds, zero, prefixes


def main():
    print(f"Rule 30 periodic columns: brute force to w={W_BRUTE}, inverse construction to right support {W_INV}, "
          f"depth K={K}\n", flush=True)
    rows, err = brute(W_BRUTE)
    if rows is None:
        report("A/E brute force", False, err)
    else:
        okA = True
        for w, bc, best, nmax in rows:
            e0, e1 = 2 * ((w + 1) // 2) + 1, 2 * (w // 2) + 2
            ecount = 2 ** w if w % 2 == 0 else 2 ** w - 1
            okA &= bc[0] == e0 and bc[1] == e1 and max(bc.values()) == w + 2 and nmax == ecount
        report("A Condrey's constant-prefix maxima and maximiser counts reproduced (published control)", okA,
               "; ".join(f"w={w}: c0 {bc[0]}, c1 {bc[1]}, #(w+2) {n}" for w, bc, _, n in rows))
        print("E  longest prefix following its first p values, by w (p = 1..6):")
        for w, _, best, _ in rows:
            print(f"     w={w}:  " + "  ".join(f"p{p}={best[p]:>3}" for p in sorted(best)))
    check_construction([w for p in range(1, 5) for w in primitive_words(p)], K)
    print(flush=True)
    chunk = max(1, (1 << W_INV) // max(1, 8 * JOBS))
    pool = Pool(JOBS) if JOBS > 1 else None
    for p in PERIODS:
        words = primitive_words(p)
        kinds, zero_hits, n = {}, [], 0
        seen = {}
        tasks = [(word, lo, min(lo + chunk, 1 << W_INV), K, p == 1)
                 for word in words for lo in range(0, 1 << W_INV, chunk)]
        results = pool.imap_unordered(search_chunk, tasks) if pool else map(search_chunk, tasks)
        for word, k, z, pre in results:
            for kk, v in k.items():
                kinds[kk] = kinds.get(kk, 0) + v
                n += v
            zero_hits += z
            seen.setdefault(word, set()).update(pre)
        universal = {w: len(s) == 1 for w, s in seen.items()}
        summary = ", ".join(f"{k}: {v}" for k, v in sorted(kinds.items(), key=lambda kv: -kv[1]))
        if p == 1:
            okB = not zero_hits and set(kinds) == {"period 2"} and universal[(1,)]
            report("B period 1 (control): forced left halves eventually alternating, never zero; universal for 1111...",
                   okB, f"{n} cases; {summary}")
        else:
            report(f"D period {p}: no right half in [1, {W_INV}] forces an eventually-zero left half "
                   f"({len(words)} primitive words)", not zero_hits,
                   f"{n} cases; {summary}" + (f"; CANDIDATES {zero_hits[:5]}" if zero_hits else ""))
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
