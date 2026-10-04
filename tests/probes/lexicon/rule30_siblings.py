#!/usr/bin/env python3
"""rule30_siblings.py: the same instrument on all 16 elementary rules that share Rule 30's left inverse,
x' = l XOR g(c, r). For each rule and each period-two trace, every right half up to W cells: is there a finite
configuration whose column 0 repeats the trace (a witness)? And, where there is none, how long can a zero run in the
forced left half be?

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_siblings.py [W=14] [K=128] [JOBS=4]
COST:       a few minutes on 4 cores.

Why (the random-chaos rule of WORKFLOW-SAVED-MEMORY.md: one step the plan did not call for). Rung 1 searched
27 million Rule 30 cases and found no finite configuration with a periodic column. A search that finds nothing must
be shown able to find something. Rule 30 offers no known positive case, but its siblings do: under Rule 60 (g = c)
a single 1 at position -1 gives column 0 = 0101... forever. So the instrument is run unchanged, with g as a
parameter, on all 16 siblings. Rule 30 is g(c, r) = c OR r.

A witness here is exact for K steps. The forced left half is zero beyond some depth D <= K/2; the finite configuration
(left half to depth D, column 0 = tau(0), the right half) is then run FORWARD with the rule for K steps, independently
of the inverse construction, and column 0 must equal the trace at every step.

PREDICTIONS, written 2026-10-04 before this script's first run:
  S1 (control, known answer): Rule 30 has no witness for 01 or 10 (rung 1, PRIZE-PROBLEMS.md section 5).
  S2 (counterfactual, known answer): Rule 60 has a witness for trace 01 with an empty right half (a single 1 at
     depth 1), and the forward run confirms it. If S2 fails, rung 1 could not have seen a counterexample.
  S3 (instrument): for every rule, 200 seeded random right halves (100 per trace), the forced left half cut at
     depth K and run
     forward reproduces the trace for the first K/2 steps (the inverse construction is right for every
     sibling).
  S4 (uncertain, blind): of the 8 rules that keep the all-zero row fixed (g(0, 0) = 0), exactly two have no witness
     for either period-two trace: the shift (Rule 240, g = 0) and Rule 30.
REFUTED-BY: S1, S2 or S3 failing (the instrument is wrong); for S4, any other set of witness-free rules.

OUTCOME of the first run, 2026-10-04 (W = 14, K = 128): S1, S2 and S3 held (Rule 30: no witness; Rule 60: the
single-cell witness, and in fact every right half is a witness, because g = c makes the left half ignore column 1;
S3: 0 mismatches). S4 was REFUTED: the witness-free rules that fix the zero row are 30, 90, 120, 150, 180, 210 and 240,
that is all of them except Rule 60. Among the rules that do not fix the zero row, 105 and 15 have witnesses everywhere
(their zero row is already alternating), and 75 and 45 have one each (the empty right half, trace 01). Longest zero
run without a witness, traces 01 / 10: Rule 30 17 / 16, Rule 90 16 / 15, Rule 210 16 / 15, Rule 150 14 / 14,
Rule 120 9 / 10, Rule 180 1 / 1, Rule 240 1 / 1.
"""
import random, sys
from multiprocessing import Pool

W = int(sys.argv[1]) if len(sys.argv) > 1 else 14
K = int(sys.argv[2]) if len(sys.argv) > 2 else 128
JOBS = int(sys.argv[3]) if len(sys.argv) > 3 else 4
WORDS = [(0, 1), (1, 0)]
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def gfun(code):
    """g as a bitwise function of two integers; code bit (2c + r) is g(c, r)."""
    def g(c, r, mask):
        out = 0
        for cv in (0, 1):
            for rv in (0, 1):
                if code >> (2 * cv + rv) & 1:
                    out |= (c if cv else ~c) & (r if rv else ~r)
        return out & mask
    return g


def rule_number(code):
    n = 0
    for l in (0, 1):
        for c in (0, 1):
            for r in (0, 1):
                n |= (l ^ (code >> (2 * c + r) & 1)) << (4 * l + 2 * c + r)
    return n


def forced_left(code, R, tau):
    """Column 1 from the right half R (bit j = position j+1) with column 0 clamped to tau, then the left half L(1..K)
    forced from columns 0 and 1. Rows are integers with bit j = position j."""
    g = gfun(code)
    width = R.bit_length() + K + 3
    mask = (1 << width) - 1
    row = tau[0] | (R << 1)
    col1 = 0
    for t in range(K + 1):
        col1 |= ((row >> 1) & 1) << t
        if t < K:
            row = (((row << 1) ^ g(row, row >> 1, mask)) & mask & ~1) | tau[t + 1]
    col0 = sum(b << t for t, b in enumerate(tau[:K + 1]))
    cols, left = [col1, col0], []
    for k in range(1, K + 1):
        m = (1 << (K - k + 1)) - 1
        c = ((cols[-1] >> 1) ^ g(cols[-1], cols[-2], m)) & m
        left.append(c & 1)
        cols.append(c)
    return left


def forward_column0(code, left, R, steps):
    """Run the finite row (left half, column 0 = tau(0) supplied by the caller in R's bit 0, right half) forward and
    return column 0 for times 0..steps-1. The row is stored with an offset so that every index stays non-negative."""
    g = gfun(code)
    D = len(left)
    off = D + steps + 2
    row = R << off                                    # R here already holds column 0 at bit 0
    for k, b in enumerate(left, 1):
        row |= b << (off - k)
    width = off + R.bit_length() + steps + 2
    mask = (1 << width) - 1
    out = []
    for _ in range(steps):
        out.append((row >> off) & 1)
        row = ((row << 1) ^ g(row, row >> 1, mask)) & mask
    return out


def chunk(args):
    code, word, lo, hi = args
    tau = [word[t % len(word)] for t in range(K + 1)]
    wit, longest = [], 0
    for R in range(lo, hi):
        L = forced_left(code, R, tau)
        ones = [k for k, b in enumerate(L, 1) if b]
        D = ones[-1] if ones else 0
        if D <= K // 2:
            col0 = forward_column0(code, L[:D], tau[0] | (R << 1), K)
            if col0 == tau[:K]:
                wit.append((R, D))
            continue
        run = m = 0
        for b in L:
            run = run + 1 if b == 0 else 0
            m = max(m, run)
        longest = max(longest, m)
    return wit, longest


def main():
    rng = random.Random(30)
    bad = 0
    for code in range(16):
        for word in WORDS:
            tau = [word[t % len(word)] for t in range(K + 1)]
            for _ in range(100):
                R = rng.getrandbits(W)
                L = forced_left(code, R, tau)
                if forward_column0(code, L, tau[0] | (R << 1), K // 2) != tau[:K // 2]:
                    bad += 1
    report("S3 the forced left half, cut at depth K and run forward, reproduces the trace for K/2 steps, all 16 rules",
           bad == 0, f"{bad} mismatches")
    table = {}
    with Pool(JOBS) as pool:
        for code in range(16):
            for word in WORDS:
                step = 1024
                res = pool.map(chunk, [(code, word, lo, min(lo + step, 1 << W)) for lo in range(0, 1 << W, step)])
                wit = [w for r in res for w in r[0]]
                table[(code, word)] = (wit, max(r[1] for r in res))
    print(f"\n   rule  g(c,r) table (00,01,10,11)  fixes 0  | witnesses of {1 << W} right halves, trace 01 ; 10 "
          f"| longest zero run without a witness, depth <= {K}")
    free = []
    for code in range(16):
        g = "".join(str(code >> i & 1) for i in range(4))
        w01, l01 = table[(code, (0, 1))]
        w10, l10 = table[(code, (1, 0))]
        fixes = (code & 1) == 0
        if fixes and not w01 and not w10:
            free.append(rule_number(code))
        ex = (w01 or w10)[:1]
        print(f"   {rule_number(code):>4}  {g}                       {'yes' if fixes else 'no ':>3}      | "
              f"{len(w01):>6} ; {len(w10):>6}   first {ex[0] if ex else '-'} | {l01:>3} ; {l10:>3}")
    w30 = table[(14, (0, 1))][0] + table[(14, (1, 0))][0]
    report("S1 Rule 30 has no witness for 01 or 10", not w30, f"{len(w30)} witnesses")
    report("S2 Rule 60 has the single-cell witness for trace 01 (empty right half, a 1 at depth 1)",
           (0, 1) in table[(12, (0, 1))][0], f"witnesses for 01: {len(table[(12, (0, 1))][0])}")
    verdict("S4 the witness-free rules that fix the zero row are exactly 240 and 30", sorted(free) == [30, 240],
            f"witness-free: {sorted(free)}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
