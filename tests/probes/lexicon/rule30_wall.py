#!/usr/bin/env python3
"""rule30_wall.py: lead 1 restated as a boundary-value problem: Rule 30 on a half-line against a 0101 wall.

RUN-ON:     cpu (pure Python 3, standard library; records.c for the control)
COMMAND:    python3 tests/probes/lexicon/rule30_wall.py
COST:       about a minute.

The claim, derived by hand (2026-10-05, RULE30-PRIZE.md section 8.39). Column 0 = t mod 2. The left-parent rule at
column 0, x_{t+1}(0) = x_t(-1) XOR (x_t(0) OR x_t(1)), says two things. At even t it fixes column 1: x_t(1) = 1 XOR
x_t(-1). At odd t, x_t(0) = 1, and it says x_t(-1) = 1. Meanwhile the left half evolves forward by Rule 30 using only
column 0: x_{t+1}(-1) = x_t(-2) XOR (x_t(-1) OR x_t(0)). So the forced left halves for 0101 are exactly the
forward evolutions of Rule 30 on the half-line x <= -1 against a wall x_t(0) = t mod 2, from any row 0, subject to one
condition: the cell beside the wall is black at every odd time. The condition at odd time t sees row 0 to depth t + 1,
and through the left edge of its light cone, which is pure XOR. So it fixes the cell at depth t + 1 from the cells
before it: row 0's even depths are forced and its odd depths are free, as the forced walk's free and non-free steps.
LR for 0101 then reads: no row 0 that is white beyond some depth keeps the wall's neighbour black at every odd time.
The doubling conjecture reads: a row 0 white from depth d on fails by odd time 2d + 3. Its run from depth d is
(first failing odd time) + 1 - d.

PREDICTIONS, written 2026-10-05 before this script's first run:
  WA0 (control, must hold): for 300 random columns 1, the forced left half built by the left-parent rule (an
      independent code path, cell by cell) equals the wall evolution of its own row 0 in every cell of the light cone
      to time 40, and the wall's neighbour is black at every odd time to 40.
  WA1 (blind; the free bits): column 1's even-time bits c_0, c_2, .., c_2m and row 0's odd-depth cells at depths 1, 3,
      .., 2m + 1 determine each other, triangularly: x_0(-(2m+1)) = NOT c_2m XOR (a function of c_0 .. c_2m-2). It is
      checked over every prefix for m up to 10.
  WA2 (blind; the equivalence): for every depth d from 3 to 27, the longest wall run over every row 0 that is white
      from depth d on, (first failing odd time) + 1 - d, equals records.c's R(d).
  WA3 (counterfactual): with the wall in the other phase (x_t(0) = (t + 1) mod 2) and the same condition, the
      equivalence breaks: at some depth from 3 to 27 the longest wall run differs from records.c's R(d).
REFUTED-BY: WA0 failing (the derivation); WA1 to WA3 failing.

OUTCOME, 2026-10-05 (the first run, 4 seconds):
  WA0 PASSED (300 random columns 1, every cell of the light cone to time 40).
  WA1 HELD (every prefix, m = 0 .. 10).
  WA2 HELD: the wall's longest run equals records.c's R(d) at all 25 depths from 3 to 27.
  WA3 HELD, but weakly: the other phase gives exactly R(d - 2) at every depth from 5 to 27 (and R(1), R(2) at 3, 4).
     It is the same problem shifted by one time step, not a different one, so the counterfactual shows that the
     phase is bookkeeping, not that the equivalence could have failed. A stronger counterfactual would change the
     wall's word.
  So the forced left half for 0101 is a boundary-value problem for Rule 30 itself: evolve the half-line x <= -1
  forward against a wall that alternates white and black, and require the wall's neighbour to be black at every odd
  time. The free data are row 0's odd-depth cells; each odd time's condition fixes the next even-depth cell.
"""
import pathlib, random, subprocess, sys, tempfile
from ompflags import OMP          # Apple's clang needs libomp's flags (ompflags.py)

HERE = pathlib.Path(__file__).resolve().parent
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def wall_step(r, t, W, phase=0):
    """Row t -> row t + 1 of Rule 30 on x <= -1; bit j - 1 of r is x(-j); the wall x_t(0) = (t + phase) mod 2."""
    return ((r >> 1) ^ (r | ((r << 1) | ((t + phase) & 1)))) & ((1 << W) - 1)


def forced_half(c, T, K):
    """Independent: x_t(-j), t = 0 .. T, j = 1 .. K, from column 0 = t mod 2 and column 1 (c: time -> bit, odd 0)."""
    right = [t % 2 for t in range(T + K + 2)]
    far = [c.get(t, 0) if t % 2 == 0 else 0 for t in range(T + K + 2)]
    cells = {}
    for j in range(1, K + 1):
        col = [right[t + 1] ^ (right[t] | far[t]) for t in range(len(right) - 1)]
        for t in range(min(T + 1, len(col))):
            cells[(t, j)] = col[t]
        far, right = right, col
    return cells


def first_failure(r0, W, tmax, phase=0):
    """The first odd time t <= tmax at which the wall's neighbour (bit 0) is white; tmax + 2 if none."""
    r = r0
    for t in range(tmax + 1):
        if t % 2 == 1 and not (r & 1):
            return t
        r = wall_step(r, t, W, phase)
    return tmax + 2


def wall_record(d, phase=0):
    """Longest wall run from depth d: over row 0's free odd depths 1 .. d - 1, even depths forced, white from d on."""
    best = -1
    nodd = len(range(1, d, 2))
    tmax = 4 * d + 20
    W = d + tmax + 4
    for bits in range(1 << nodd):
        r0, b = 0, 0
        for k in range(1, d):
            if k % 2 == 1:
                if (bits >> b) & 1:
                    r0 |= 1 << (k - 1)
                b += 1
            elif first_failure(r0, k + 1, k - 1, phase) == k - 1:  # depth k is fixed by the condition at time k - 1
                r0 |= 1 << (k - 1)
        best = max(best, first_failure(r0, W, tmax, phase) + 1 - d)
    return best


def main():
    rng = random.Random(30)
    ok = True
    T = K = 40
    for _ in range(300):
        c = {t: rng.getrandbits(1) for t in range(0, 2 * (T + K) + 4, 2)}
        cells = forced_half(c, T, T + K)
        r = 0
        for j in range(1, T + K + 1):
            r |= cells[(0, j)] << (j - 1)
        W = T + K
        for t in range(T + 1):
            for j in range(1, K + 1):                          # x_t(-j) needs row 0 to depth j + t
                ok &= ((r >> (j - 1)) & 1) == cells[(t, j)]
            if t % 2 == 1:
                ok &= (r & 1) == 1
            r = wall_step(r, t, W)
    report("WA0 the forced half is the wall evolution of its row 0; the wall's neighbour is black at odd times", ok)
    ok1 = True
    for m in range(11):
        n = m + 1
        seen = set()
        for p in range(1 << n):
            c = {2 * i: (p >> i) & 1 for i in range(n)}
            cells = forced_half(c, 0, 2 * m + 1)
            word = tuple(cells[(0, 2 * i + 1)] for i in range(n))
            seen.add(word)
            q = p ^ (1 << m)                                   # flip c_2m: depth 2m + 1 flips, earlier ones stay
            c2 = {2 * i: (q >> i) & 1 for i in range(n)}
            cells2 = forced_half(c2, 0, 2 * m + 1)
            ok1 &= cells2[(0, 2 * m + 1)] != cells[(0, 2 * m + 1)]
            ok1 &= all(cells2[(0, 2 * i + 1)] == cells[(0, 2 * i + 1)] for i in range(m))
        ok1 &= len(seen) == 1 << n
    verdict("WA1 column 1's even bits and row 0's odd depths determine each other, triangularly (m <= 10)", ok1)
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_wall_records"
    subprocess.run(["cc", "-O2", *OMP, "-o", str(exe), str(HERE / "records.c")], check=True)
    ok2, diff3 = True, []
    for d in range(3, 28):
        out = subprocess.run([str(exe), str(d), "0"], check=True, capture_output=True, text=True).stdout
        R = int(out.split()[2])
        w, w3 = wall_record(d), wall_record(d, phase=1)
        ok2 &= w == R
        if w3 != R:
            diff3.append(d)
        print(f"   depth {d:2d}: records.c {R:2d}  wall {w:2d}  other phase {w3:2d}", flush=True)
    verdict("WA2 the wall's longest run equals records.c's R(d) at every depth 3 .. 27", ok2)
    verdict("WA3 the other phase breaks the equivalence", bool(diff3), f"differs at {diff3}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
