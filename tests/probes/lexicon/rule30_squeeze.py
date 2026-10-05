#!/usr/bin/env python3
"""rule30_squeeze.py: the entropy squeeze. Next to a period-2 column, every column to its left is almost frozen.

RUN-ON:     cpu (C99 via cc for the automata, Python 3 standard library for the exact checks)
COMMAND:    python3 tests/probes/lexicon/rule30_squeeze.py [M list, default 8,12,16,20,24,26]
COST:       about ten minutes on one core, most of it building the m = 26 automaton (several GB of memory).

THE LEMMA (PRIZE-PROBLEMS.md section 8.33). For a sequence s, p_s(n) counts its distinct factors of length n and
h(s) = lim (1/n) log2 p_s(n) is its topological entropy. Let x be any configuration of Rule 30 with x_t(0) = t mod 2
for all t >= 0. Then for every layer width m, every column -k (k >= 1) has h <= (1/2) log2 lambda_m bits per step,
and at most 2^((h + o(1)) j) distinct patterns of width j ever appear just left of column 0. Here lambda_m is the
growth rate of the layer language L_m of entropy.c (column 1's visible bits from a layer of m cells with column 0
clamped and any input on the far side).
Proof, in four steps.
  1. Every factor of column 1's visible bits (even times) lies in L_m: restart at that even time; the layer reproduces
     cells 1 .. m. So p_v(n) <= N_m(n) = |L_m(n)|.
  2. The rule at cell 0 gives x_t(-1) = 1 at odd t and x_t(-1) = NOT x_t(1) at even t. So p_(col -1)(n) <=
     2 p_v(ceil(n/2)), and h(col -1) <= h(v) / 2.
  3. Rule 30 is left-permutive: x_t(j-2) = x_(t+1)(j-1) XOR (x_t(j-1) OR x_t(j)). The pair (col j-2, col j-1) is a
     sliding block code (window 2 in time) of (col j-1, col j), so entropy cannot grow leftwards, starting from
     (col -1, col 0) whose entropy is that of col -1 (col 0 has two factors of each length).
  4. A width-j pattern just left of column 0 at time t is a function of (col -1, col 0) over times t .. t+j-1.
COROLLARY. A period-2 counterexample (a finite configuration whose column 0 is eventually 0101..., shifted in time to
be periodic from 0) has every left column at no more than about 0.064 bits per step.
What this script checks is the computation the lemma rests on, not its logic: lambda_m was found by power iteration,
which is not a proof. Here each lambda_m gets an exact certificate. For a non-negative matrix A and a positive vector
w with A w <= lambda' w componentwise, the spectral radius is at most lambda' (Collatz-Wielandt), and the number of
paths of length n from the start state, which is N_m(n), is at most (w_start / min w) lambda'^n. entropy2.c's cert
mode computes w = sum of (A / lambda')^j 1 in floating point; this script rounds it up to integers and checks
A W <= lambda' W exactly, in integer arithmetic. Rounding up keeps a margin, because A w = lambda' (w - 1 + t_last)
with every entry of t_last below 1/4.

PREDICTIONS, written 2026-10-05 before this script's first run (the cert mode was tried on m = 4 to 20 for timing,
printing only the floating-point lambda' and round counts, no exact check):
  SQ0 (controls): (a) the leftward identity of step 3 holds at every cell of 50 random Rule 30 runs; (b) the forced
      left half built from 0101... and a random column 1, run forwards with column 1 imposed, reproduces column 0 =
      0101... exactly, and its column -1 is 1 at odd times and NOT column 1 at even times; (c) the counterfactual: the
      exact check rejects lambda'' = lambda_m (1 - 10^-3) with the same certificate vector, for every m.
  SQ1: for every m in the list, the exact check A W <= lambda' W passes, and log2 lambda' (bits per visible bit) is
      within 0.002 of the value recorded by rule30_entropy.py. At m = 26 the certified bound is at most 0.1292 bits
      per visible bit, so the corollary's figure is at most 0.0646 bits per step.
  SQ2 (step 1, tried on real data): every factor of 64 visible bits of column 1, from every even start, of 100
      random right halves (1 to 40 cells) driven by 0101... for 4,096 steps, is accepted by the automaton for
      m = 8, 12, 16 and 20.
  SQ3 (counterfactual for SQ2): fewer than 1% of 10,000 random words of 64 bits are accepted at m = 12, so SQ2's
      acceptance is not trivial.
REFUTED-BY: SQ0 failing (the instrument); SQ1, SQ2 or SQ3 failing (the bound, or the lemma's step 1).
"""
import math, pathlib, random, subprocess, sys, tempfile
from fractions import Fraction

HERE = pathlib.Path(__file__).resolve().parent
MS = [int(a) for a in sys.argv[1].split(",")] if len(sys.argv) > 1 else [8, 12, 16, 20, 24, 26]
RECORDED = {8: 0.356, 12: 0.258, 16: 0.212, 20: 0.1519, 24: 0.1327, 26: 0.1277}
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def build():
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_squeeze_entropy2"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "entropy2.c"), "-lm"], check=True)
    return exe


def certify(exe, m, tmp):
    path = pathlib.Path(tmp) / f"cert_{m}.txt"
    out = subprocess.run([str(exe), str(m), "4000", "cert", "1e-3", str(path)], check=True, capture_output=True,
                         text=True).stdout.split("\n")
    lam = float(next(l for l in out if l.startswith("E ")).split()[2])
    c = next(l for l in out if l.startswith("C ")).split()
    lp = float(c[2])
    succ, W = [], []
    for line in path.read_text().split("\n"):
        if line:
            i, a, b, w = line.split()
            succ.append((int(a), int(b)))
            W.append(math.ceil(float(w) * 2 ** 30))      # exact: a double times a power of 2, rounded up
    return lam, lp, succ, W, int(c[3])


def check(succ, W, lam):
    """Exact check of A W <= lam W, lam a float taken as the exact rational it is."""
    q = Fraction(lam)
    num, den = q.numerator, q.denominator
    for i, (a, b) in enumerate(succ):
        s = (W[a] if a >= 0 else 0) + (W[b] if b >= 0 else 0)
        if den * s > num * W[i]:
            return False
    return True


def accepted(succ, word):
    i = 0
    for b in word:
        i = succ[i][b]
        if i < 0:
            return False
    return True


def right_column1(R, T):
    """Column 1 of the right half-line with column 0 forced to t mod 2; bit i of row is cell i (cell 0 = column 0)."""
    mask = (1 << (R.bit_length() + T + 4)) - 1
    row, out = R << 1, []
    for t in range(T):
        out.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & mask & ~1) | ((t + 1) % 2)
    return out


def main():
    rng = random.Random(1986)                          # the year of Jen's "Global properties of cellular automata"
    # SQ0 (a): the leftward identity on random runs
    ok_a = True
    for _ in range(50):
        W0, steps = 200, 60
        row = rng.getrandbits(W0)
        rows = [row]
        for _ in range(steps):
            row = ((row << 1) ^ (row | (row >> 1))) & ((1 << W0) - 1)
            rows.append(row)
        bit = lambda t, i: (rows[t] >> i) & 1         # bit i = cell i; cell i's left neighbour is cell i - 1
        for t in range(steps - 1):
            for j in range(steps + 2, W0 - steps - 2):
                ok_a &= bit(t, j - 2) == bit(t + 1, j - 1) ^ (bit(t, j - 1) | bit(t, j))
    # SQ0 (b): the forced left half, run forwards
    ok_b = True
    for _ in range(20):
        n, K = 400, 150
        c1 = [rng.getrandbits(1) for _ in range(n)]
        cols = {1: c1, 0: [t % 2 for t in range(n)]}
        for j in range(1, -K, -1):                     # column j - 2 from columns j - 1 and j
            a, b = cols[j - 1], cols[j]
            cols[j - 2] = [a[t + 1] ^ (a[t] | b[t]) for t in range(len(a) - 1)]
        ok_b &= all(cols[-1][t] == (1 if t % 2 else 1 - c1[t]) for t in range(len(cols[-1])))
        cells = [cols[j][0] for j in range(-K, 1)]     # the forced row at t = 0; index i is cell i - K
        for t in range(K - 1):                          # forwards, with column 1 imposed; cells to the far left are
            cells = [(cells[i - 1] if i else 0) ^ (cells[i] | (cells[i + 1] if i < K else c1[t]))   # unknown (0),
                     for i in range(K + 1)]            # and that error moves right one cell per step, never
            ok_b &= cells[K] == (t + 1) % 2            # reaching column 0 before t = K
    exe = build()
    rejected_all, certs = True, {}
    with tempfile.TemporaryDirectory() as tmp:
        for m in MS:
            lam, lp, succ, W, rounds = certify(exe, m, tmp)
            ok = check(succ, W, lp)
            bad = check(succ, W, lam * (1 - 1e-3))
            rejected_all &= not bad
            bits = math.log2(lp)
            certs[m] = (ok, bits, succ, W)
            print(f"   m = {m}: {len(succ)} states; power iteration {math.log2(lam):.4f}, certified {bits:.4f} "
                  f"bits per visible bit ({rounds} rounds); exact check {'passes' if ok else 'FAILS'}; constant "
                  f"w_start / min w = {W[0] / min(W):.1f}; lambda (1 - 10^-3) "
                  f"{'wrongly accepted' if bad else 'rejected'}", flush=True)
    report("SQ0 controls: the leftward identity; the forced left half reproduces 0101 and step 2's column -1; the "
           "exact check rejects a bound below lambda", ok_a and ok_b and rejected_all,
           f"(a) {ok_a}; (b) {ok_b}; (c) {rejected_all}")
    ok1 = all(certs[m][0] and abs(certs[m][1] - RECORDED[m]) <= 0.002 for m in MS if m in RECORDED)
    top = max(MS)
    verdict("SQ1 every certificate passes exactly, within 0.002 of the recorded bound; at m = 26 at most 0.1292",
            ok1 and (top != 26 or certs[26][1] <= 0.1292),
            f"certified at m = {top}: {certs[top][1]:.4f} bits per visible bit, {certs[top][1] / 2:.4f} per step")
    # SQ2: real right halves' visible factors, accepted
    halves = [rng.getrandbits(rng.randrange(1, 41)) | 1 for _ in range(100)]
    vis = [right_column1(R, 4096)[0::2] for R in halves]
    acc = {}
    for m in (8, 12, 16, 20):
        if m not in certs:
            continue
        succ = certs[m][2]
        acc[m] = all(accepted(succ, v[i:i + 64]) for v in vis for i in range(len(v) - 64))
    verdict("SQ2 every 64-bit visible factor of real column 1 is in L_m (m = 8, 12, 16, 20)", all(acc.values()),
            ", ".join(f"m = {m}: {'all accepted' if a else 'SOME REJECTED'}" for m, a in acc.items()))
    if 12 in certs:
        succ = certs[12][2]
        frac = sum(accepted(succ, [rng.getrandbits(1) for _ in range(64)]) for _ in range(10000)) / 10000
        verdict("SQ3 fewer than 1% of random 64-bit words are in L_12", frac < 0.01, f"{frac:.4%}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
