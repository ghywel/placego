#!/usr/bin/env python3
"""rule210_streams.py: on Rule 210, where conjecture LR fails at period 2 (section 8.65), is every zero-keeping column 1
eventually periodic? If it is, columns 0 and 1 of any finite configuration with centre 0101 would both be eventually
periodic, and Jen's theorem (two adjacent columns of a finite configuration are never both eventually periodic, for
left-permutive rules in Kopra's form) would give conjecture B for Rule 210 without a search. The question of
CHAT-LEDGER.md C053, made finite. (Local, 2026-10-06; section 8.65's addendum.)

RUN-ON:     cpu, one core (pure Python 3, big integers)
COMMAND:    python3 tests/probes/lexicon/rule210_streams.py [DEPTHS=1,8,16,24] [N=4000]   |   ... parity
COST:       a few minutes.

METHOD. The forced left half by the anti-diagonal recurrence (section 8.36) with Rule 210's inverse, l = x' xor
(not c and r): a_k = prefixXOR(b) xor (tau(k) ? ones : 0), b = (not (a_(k-1) << 1)) and ((a_(k-2) << 2) or
(sigma(k-1) << 1)). From depth d, with the free bits below d fixed (a prefix), the continuation that keeps the row zero
is unique: at a white time the linear cell fixes sigma, at a black time the forced cell must be 0 or the run ends. So
each prefix has one zero-keeping stream (or none). Its visible bits (sigma at even times) are followed for N depths
and tested for eventual periodicity: the smallest p <= 64 for which the last N/2 visible bits are p-periodic, and
the preperiod.

PREDICTIONS, written 2026-10-06 before this script's first run.
  ZS0 (control, must hold): the recurrence reproduces records_word.c -DRULE210: from depths 8 and 16 every prefix's
      stream survives N depths (section 8.65, Z1); and for Rule 30 (the OR in place of the AND-NOT) from depth 8 every
      prefix's forced walk ends within 60 depths (R(8) = 2).
  ZS1 (blind): every zero-keeping stream of Rule 210, from every depth in DEPTHS and every prefix, is eventually
      periodic with period at most 16 and preperiod at most 4 d + 32.
  ZS2 (blind): the eventual period is 1 (the stream ends in constant visible bits) for at least half the prefixes.
  CF  (counterfactual, must fail): a random visible stream of 4000 bits passes the same periodicity test. It must
      not (no period up to 64 over the last 2000 bits).
REFUTED-BY: ZS0 or CF failing (the instrument); ZS1 the other way, which would leave B for Rule 210 a real question;
  ZS2 the other way.

OUTCOME of the first run, 2026-10-06 (depths 1, 8, 16, 24; N = 4000; 26 seconds): ZS0 and CF PASSED. ZS1 REFUTED and ZS2
  REFUTED, completely: all 4,369 zero-keeping streams are aperiodic (no period up to 64 over the last 2,000 visible
  bits), none ends in constant bits. So the zero-keeping choice is not finite-state, Jen's theorem does not reach
  B for Rule 210, and B there is a real open question. Exploratory, after the run: the stream from depth 1 (the one
  that keeps the whole left half empty) is 1 0 11 0000 1^8 0^16 1^32 ... with run lengths 1, 1, 2, 4, 8, ..., 1024
  (checked to 6,000 depths), ones at share 0.34, and factor complexity p(n) = 10, 15, 20, 25, 31, 40, 63 at
  n = 4, 6, 8, 10, 12, 16, 24: linear, zero entropy, aperiodic.
"""
import random, sys

# ADDENDUM, written 2026-10-06 before the second run (python3 rule210_streams.py parity), after GPT's G26 proved that the
# empty-left-half stream is Rule 90 in disguise: on an empty left half the occupied cells have t + j odd, no two
# neighbours are both black, and the AND-NOT reduces to XOR. Which of the other zero-keeping streams share that
# parity-sparse regime, and which are genuinely nonlinear? For each prefix at depths 8, 16, 24 the stream's left half is
# built by the column recurrence for 300 times and 300 depths and searched for two horizontally adjacent black cells.
#   PS0 (control, must hold): the depth-1 stream (the empty left half) has no adjacent black pair anywhere in the window.
#   PS1 (blind): the parity-sparse streams are exactly those whose time-0 row is empty below d, one prefix per depth
#       (the all-zero row), so 1 of 16, 1 of 256, 1 of 4096.
#   PS2 (blind): every other stream shows an adjacent black pair within its first 2d times.
#   CF  (counterfactual, must fail): Rule 30's forced left half from the same visible stream (the OR in place of the
#       AND-NOT) has adjacent black pairs from the first times for every prefix; it must not be parity-sparse.
# REFUTED-BY: PS0 or CF failing (the instrument); PS1, PS2 the other way.
# OUTCOME of the second run, 2026-10-06 (parity; 35 s): PS0 and CF PASSED. PS1 REFUTED the other way: ALL 4,368 streams
# at depths 8, 16, 24 are parity-sparse (no two horizontally adjacent black cells in 300 x 300), not only the empty-row
# one; PS2 held vacuously. The explanation is a theorem (section 8.65, second addendum): next to 0101 the black cells of
# Rule 210's forced left half always have t + j odd, for every column 1, so the AND-NOT never fires and the left half
# is Rule 90's. The zero-keeping streams are the solutions of a linear system.

_a = [a for a in sys.argv[1:] if a != "parity"]
DEPTHS = [int(x) for x in _a[0].split(",")] if len(_a) > 0 else [1, 8, 16, 24]
N = int(_a[1]) if len(_a) > 1 else 4000
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def prefix_xor(x, bits):
    s = 1
    while s < bits:
        x ^= x << s
        s <<= 1
    return x & ((1 << bits) - 1)


def tau(k):
    return k & 1                                   # the wall 0101...: 0 at even times


def step(a1, a2, s, k, rule210):
    bits = k + 2
    mask = (1 << bits) - 1
    c = ((a2 << 2) | (s << 1)) & mask
    b = ((~(a1 << 1)) & c) if rule210 else (((a1 << 1) | c)) & mask
    a = prefix_xor(b & mask, bits)
    return a ^ mask if tau(k) else a


def stream(prefix_bits, d, n, rule210):
    """the zero-keeping stream from depth d: returns (visible bits list, ended_at or None)"""
    a1, a2 = tau(0), 0                             # a_0 = tau(0) = 0; a_(-1) = 0
    vis = []
    for k in range(1, n):
        free = tau(k - 1) == 0
        if k < d:
            s = prefix_bits.get(k - 1, 0) if free else 0
            a = step(a1, a2, s, k, rule210)
        else:
            a = step(a1, a2, 0, k, rule210)
            if (a >> k) & 1:
                if not free:
                    return vis, k
                a = step(a1, a2, 1, k, rule210)
                s = 1
                if (a >> k) & 1:
                    return vis, k
            else:
                s = 0
        if free:
            vis.append(s)
        a2, a1 = a1, a
    return vis, None


def periodicity(v):
    half = v[len(v) // 2:]
    for p in range(1, 65):
        if all(half[i] == half[i + p] for i in range(len(half) - p)):
            pre = next((i for i in range(len(v)) if all(v[j] == v[j + p] for j in range(i, len(v) - p))), len(v))
            return p, pre
    return None, None


def left_half(vis, T, depth, rule210):
    """columns of the forced left half from the visible bits (sigma at even times): rows[t][m-1] = x(-m, t)"""
    import numpy as np
    n = T + depth + 2
    tau = np.array([t & 1 for t in range(n)], dtype=np.uint8)
    sg = np.array([vis[t // 2] if (t & 1) == 0 and t // 2 < len(vis) else 0 for t in range(n)], dtype=np.uint8)
    g = (lambda c, r: (1 - c) & r) if rule210 else (lambda c, r: c | r)
    cols = []
    cur = tau[1:] ^ g(tau[:-1], sg[:-1]); right = tau[:-1]
    cols.append(cur)
    for _ in range(depth - 1):
        nxt = cur[1:] ^ g(cur[:-1], right[:len(cur) - 1]); right, cur = cur[:-1], nxt
        cols.append(cur)
    return [[int(cols[m][t]) for m in range(depth)] for t in range(T)]


def first_adjacent(rows):
    for t, row in enumerate(rows):
        for m in range(len(row) - 1):
            if row[m] and row[m + 1]:
                return t
    return None


def parity():
    T, depth = 300, 300
    v, _ = stream({}, 1, 2 * (T + depth) + 4, True)
    report("PS0 the empty-left-half stream has no adjacent black pair in 300 x 300", first_adjacent(left_half(v, T, depth, True)) is None)
    sparse = {}; late = []
    cf_dense = True
    for d in (8, 16, 24):
        nfree = len([t for t in range(d - 1) if tau(t) == 0])
        sparse[d] = []
        for pre in range(1 << nfree):
            bits = {2 * i: (pre >> i) & 1 for i in range(nfree)}
            v, end = stream(bits, d, 2 * (T + depth) + 4, True)
            rows = left_half(v, T, depth, True)
            fa = first_adjacent(rows)
            empty0 = not any(rows[0][:d - 1])
            if fa is None:
                sparse[d].append((pre, empty0))
            elif fa >= 2 * d:
                late.append((d, pre, fa))
            if pre < 4:
                cf_dense &= first_adjacent(left_half(v, 40, 40, False)) is not None and first_adjacent(left_half(v, 40, 40, False)) < 4
        print(f"   depth {d}: parity-sparse streams {len(sparse[d])} of {1 << nfree}; of them with an empty time-0 row: "
              f"{sum(1 for _, e in sparse[d] if e)}", flush=True)
    verdict("PS1 the parity-sparse streams are exactly the empty-row ones, one per depth",
            all(len(sparse[d]) == 1 and sparse[d][0][1] for d in sparse))
    verdict("PS2 every other stream shows an adjacent pair within 2d times", not late, f"late: {late[:5]}")
    report("CF  Rule 30's left half from the same streams is dense from the first times", cf_dense)
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


def main():
    if "parity" in sys.argv[1:]:
        parity()
        return
    # ZS0: Rule 30 from depth 8 ends quickly; Rule 210 from depths 8, 16 survives
    ok0 = True
    for pre in range(1 << 4):
        bits = {2 * i: (pre >> i) & 1 for i in range(4)}
        v, end = stream(bits, 8, 200, False)
        ok0 &= end is not None and end < 8 + 60
    for d in (8, 16):
        nfree = len([t for t in range(d - 1) if tau(t) == 0])
        for pre in range(1 << nfree):
            bits = {2 * i: (pre >> i) & 1 for i in range(nfree)}
            v, end = stream(bits, d, N, True)
            ok0 &= end is None
    report("ZS0 Rule 30's walks from depth 8 end within 60; Rule 210's streams from depths 8 and 16 survive N", ok0)
    rng = random.Random(210)
    p, _ = periodicity([rng.randint(0, 1) for _ in range(N)])
    report("CF  a random stream shows no period up to 64", p is None)
    worst_p, worst_pre, const, total, bad = 0, 0, 0, 0, []
    for d in DEPTHS:
        nfree = len([t for t in range(d - 1) if tau(t) == 0])
        for pre in range(1 << nfree):
            bits = {2 * i: (pre >> i) & 1 for i in range(nfree)}
            v, end = stream(bits, d, N, True)
            total += 1
            if end is not None:
                bad.append((d, pre, "ends", end)); continue
            p, preperiod = periodicity(v)
            if p is None:
                bad.append((d, pre, "aperiodic")); continue
            worst_p = max(worst_p, p); worst_pre = max(worst_pre, preperiod)
            const += p == 1
            if preperiod > 4 * d + 32:
                bad.append((d, pre, "late", preperiod))
        print(f"   depth {d}: {1 << nfree} prefixes done; worst period so far {worst_p}, worst preperiod {worst_pre}", flush=True)
    verdict("ZS1 every stream eventually periodic, period <= 16, preperiod <= 4d + 32", not bad and worst_p <= 16,
            f"{total} streams; worst period {worst_p}, worst preperiod {worst_pre}; exceptions {bad[:5]}")
    verdict("ZS2 at least half the streams end in constant visible bits", const * 2 >= total, f"{const} of {total}")
    print("\nALL CHECKS PASS" if FAILS == 0 else f"\n{FAILS} CHECK(S) FAILED")


if __name__ == "__main__":
    main()
