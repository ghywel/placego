#!/usr/bin/env python3
"""rule30_wheel_left.py: the left half forced by the pure wheel. Column 0 = 0101..., column 1 = the universal 56-step
domain word of rule30_wheel.py, both exactly periodic in time. What left half do they force, and how long are its
zero runs?

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_wheel_left.py [KMAX=200000]
COST:       seconds to a minute.

Why it is finite. If columns 0 and 1 are periodic in time with period P (for t >= 0), the left-permutive recursion
    c_{-k}(t) = c_{-k+1}(t+1) XOR ( c_{-k+1}(t) OR c_{-k+2}(t) )
keeps every column P-periodic, so the pair (c_{-k+1}, c_{-k}) runs through a finite set of 2^(2P) states and the
forced left half L(k) = c_{-k}(0) is eventually periodic in k. Either it becomes zero for good (the pair (0, 0) is
fixed), or its zero runs are bounded. The script follows the pairs until one repeats.

The words (printed by rule30_wheel.py's first run, 2026-10-04; window starts at multiples of 56, so t = 0 is even):
  U  = 00010011010001001101000100110100010011010001001101001101   the universal word, 96.6% of stretches
  U2 = 00010011001101000100110011010001001100110100010011001101   the second word, 3.4%
Each is tried at every even rotation (an odd one would put the word out of step with the trace). A rotation is kept
only if it obeys Lemma 3 (C0 and C1) everywhere on the cycle, as a real column 1 must.

PREDICTIONS, written 2026-10-04 before this script's first run:
  W1 (blind): for no kept rotation of U or U2 is the forced left half eventually zero.
  W2 (blind): for every kept rotation of U, the forced left half's longest zero run is at most 12 (shorter than the
     two-sided runs of 14 to 24 that rule30_wheel.py found next to slips, so the long runs need the slips).
  C1 (known answer): the 7-cell ring's 4-cycle, read as column 0 = its 0101... column and column 1 = the column to
     its right, forces a left half of period 7 (the ring itself, continued).
  C2 (known answer): column 0 = column 1 = all zeros forces the zero left half (the detection of "eventually zero").
REFUTED-BY: C1 or C2 failing (the instrument); W1 or W2 failing.

FIRST RUN, 2026-10-04: W1 HELD, W2 REFUTED (longest run 23 under the pure universal wheel). C1 FAILED, and the fault was
the control's: forced() stops at the first repeated state, so for the 7-ring it returns 8 cells (10000001, which match
the ring), and the check compared them with 21. Fixed by comparing over the cells returned. The second run adds, as a
measurement, the longest run by depth (192, 1000, 10000, all) and the depth of the first run of 14.

SECOND RUN, 2026-10-04: C1 and C2 passed. W1 HELD (no rotation of U or U2 gives a left half that is eventually zero).
W2 REFUTED. Under the pure universal wheel the longest zero run, over the 28 phases, is 5 to 10 by depth 192, 5 to 14 by
1,000, 10 to 17 by 10,000 and 14 to 23 by 200,000, close to log2 of the depth, the law of coin flips. The first run
of 14 ends at depth 599 at the earliest, usually thousands. No pair of columns repeats within 200,000 depths. U2 forces
a left half of exact period 728 = 56 x 13, with runs of at most 9. So within the two-sided search's depth (192) the
pure wheel gives runs of at most 10, and the two-sided runs of 14 to 20 there need the slips (rule30_wheel.py, Q4).
C3 was added after this run, as an exhaustive fact: U is the two-arc coding of the rotation t -> 17t mod 56.
"""
import sys

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
U = "00010011010001001101000100110100010011010001001101001101"
U2 = "00010011001101000100110011010001001100110100010011001101"
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def as_int(bits):
    return sum(int(b) << t for t, b in enumerate(bits))


def lemma3_ok(tau, sigma):
    P = len(sigma)
    for t in range(P):
        u = (t + 1) % P
        if tau[t] == 0 and sigma[t] == 1 and sigma[u] == 0:
            return False
        if tau[t] == 1 and sigma[u] == 1 and sigma[t] == 1:
            return False
    return True


def forced(tau, sigma, kmax=KMAX):
    """Follow the column pairs. Returns (L up to the first repeat, preperiod, period, eventually zero)."""
    P = len(sigma)
    mask = (1 << P) - 1

    def rot1(x):                                       # x(t+1), cyclically
        return ((x >> 1) | ((x & 1) << (P - 1))) & mask
    a, b = as_int(sigma), as_int(tau)                 # a = column 1, b = column 0: the pair (c_{-k+2}, c_{-k+1}) at k = 1
    seen, L = {}, []
    for k in range(1, kmax + 1):
        c = rot1(b) ^ (b | a)
        L.append(c & 1)
        state = (b, c)
        if state in seen:
            k0 = seen[state]
            return L, k0, k - k0, (b == 0 and c == 0)
        seen[state] = k
        a, b = b, c
    return L, None, None, False


def longest_zero_run(L):
    run = m = 0
    for x in L:
        run = run + 1 if x == 0 else 0
        m = max(m, run)
    return m


def ring_columns(n=7):
    m = (1 << n) - 1

    def step(x):
        return (((x << 1) | (x >> (n - 1))) & m) ^ (x | (((x >> 1) | (x << (n - 1))) & m))
    for x0 in range(1 << n):
        cyc, x = [x0], step(x0)
        while x != x0 and len(cyc) <= 4:
            cyc.append(x)
            x = step(x)
        if x == x0 and len(cyc) == 4:
            for i in range(n):
                col = [(s >> i) & 1 for s in cyc]
                if col == [0, 1, 0, 1]:
                    right = [(s >> ((i + 1) % n)) & 1 for s in cyc]
                    left = [[(s >> ((i - k) % n)) & 1 for s in cyc] for k in range(1, 3 * n + 1)]
                    return col, right, left
    return None


def rotation_coding(word, a=17, P=56):
    """Lay the word on the circle of P points by t -> a t mod P (a bijection when gcd(a, P) = 1; it keeps parity, as
    a is odd and P even). Return, for each parity of t, the number of arcs of 1s among that parity's points."""
    circle = {}
    for t in range(P):
        circle[(a * t) % P] = int(word[t])
    out = []
    for par in (0, 1):
        pts = [j for j in range(P) if j % 2 == par]
        out.append(sum(1 for i, j in enumerate(pts) if circle[j] == 1 and circle[pts[i - 1]] == 0))
    return out, "".join(str(circle[j]) for j in range(P))


def main():
    arcs, laid = rotation_coding(U)
    report("C3 (a fact, exhaustive over the 56 points) U is a two-arc coding of the rotation by 17/56: one arc of 1s"
           " for each parity of t", arcs == [1, 1], f"arcs (even t, odd t) = {arcs}; on the circle {laid}")
    arcs2, _ = rotation_coding(U2)
    print(f"   U2 on the same circle: arcs (even t, odd t) = {arcs2}", flush=True)
    col, right, left = ring_columns()
    L, k0, per, zero = forced(col, right, 1000)
    report("C1 the 7-ring's 4-cycle forces a left half of period 7, the ring continued",
           per is not None and 7 % per == 0 and not zero and L == [x[0] for x in left][:len(L)],
           f"preperiod {k0}, period {per}")
    L, k0, per, zero = forced([0] * 56, [0] * 56, 10)
    report("C2 two zero columns force the zero left half", zero and not any(L), f"period {per}, zero {zero}")

    tau = [t % 2 for t in range(56)]
    any_zero, worst = False, 0
    for name, word in (("U", U), ("U2", U2)):
        kept = 0
        for r in range(0, 56, 2):
            sigma = [int(word[(t - r) % 56]) for t in range(56)]
            if not lemma3_ok(tau, sigma):
                continue
            kept += 1
            L, k0, per, zero = forced(tau, sigma)
            run = longest_zero_run(L)
            any_zero |= zero
            if name == "U":
                worst = max(worst, run)
            first14 = next((k for k in range(len(L)) if k >= 13 and not any(L[k - 13:k + 1])), None)
            grow = ", ".join(f"{d}: {longest_zero_run(L[:d])}" for d in (192, 1000, 10000, len(L)) if d <= len(L))
            print(f"   {name} delayed by {r:>2}: left half {'EVENTUALLY ZERO' if zero else 'not eventually zero'}, "
                  f"preperiod {k0}, period {per}, longest zero run {run}; by depth {grow}; "
                  f"first run of 14 ends at depth {None if first14 is None else first14 + 1}", flush=True)
        print(f"   {name}: {kept} of 28 even rotations obey Lemma 3", flush=True)
    verdict("W1 no kept rotation's left half is eventually zero", not any_zero)
    verdict("W2 under the pure universal wheel the longest zero run is at most 12", worst <= 12, f"longest {worst}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
