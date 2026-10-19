#!/usr/bin/env python3
"""mahler_contrib_checks.py: independent checks of the numerical claims in Joshua Coon's Lean 4 formalization of
Mahler's 3/2 problem (github.com/jjc16/mahler-3-2-lean4, received by e-mail on 2026-10-19; CL463). Our own code,
written from the statements only; none of their code is run here.

C1  horizon H(n): the first step j at which no alpha in [n, n+1) keeps every {alpha (3/2)^i}, i <= j, in [0, 1/2).
    Exact integers: n_(i+1) = ceil(3 n_i / 2) is forced (MAHLER.md, G50), and the window through step N is
    max_i n_i (2/3)^i <= alpha < min_i (n_i + 1/2)(2/3)^i.
    Claims: seed 149 survives 28 and fails 29; their record holder 29871555608238677 survives 113 and fails 114.
    Ours to compare: the census record below 2^56, 9850069454682037, horizon 137.
C2  B(29) >= 4096: no positive seed below 4096 survives step 29.
C3  the first-defect valuation lock: an odd seed whose first j0 blocks have length 3 and whose next block has length
    >= 4 has v_2(19 a0 + 9) = 3 j0 + 3 exactly. A block is one odd step and s - 1 even steps: 3 b + 1 = 2^s u.
C4  the window and union escape bounds: for every xi in [1, 2^W) some n <= W + c has {xi r^n} outside the set,
    tested by exact propagation of the set of survivors for small W. Control: the same code on Mahler's [0, 1/2)
    must give first-empty step 29 at W = 12 (C2's census control, n = 149).

Record searched (record_find, 2026-10-19): '13/24', '25/36', '7/12' -> 0 hits; '19a0|v_2(19' -> 0 hits;
'29871555608238677' -> 0 hits; MAHLER.md read: census records, 149 at horizon 29 (C0), Stephan's 3/7 window.

PREDICTIONS (written before any run of this file):
  C1 must hold: H(149) = 29 (our census C0). Their record seed: H = 114 if the definitions agree (0.85); if not,
     the conventions differ by one. Ours: H(9850069454682037) = 137 (census). So their seed is not a record (0.9).
  C2 must hold: max H over 1 <= n < 4096 is 29 at n = 149, so nothing below 4096 survives step 29.
  C3 (0.9): the lock holds on every tested seed. Unknown: what happens when the defect block has length 1 or 2.
  C4 (0.8): every claimed bound holds at every W tested, with first-empty steps well below W + c (the bounds are
     proved with slack). Counterfactual: a survivor past W + c at some small W would refute a Lean-checked theorem,
     which would mean a statement mismatch between their formal and informal wording, not a kernel error.
  Unexpected check: C4's control at W = 12 must reproduce the census exactly; a mismatch means the propagator is wrong.

OUTCOME (2026-10-19, this container; their repository at commit 04ed5389):
  C1 HELD: H(149) = 29; H(29871555608238677) = 114, so the conventions agree (survives 113, fails 114). Our census
     seed 9850069454682037 (54 bits) has H = 137, so a smaller seed survives longer: theirs is not a record.
  C2 HELD: the maximum horizon below 4096 is 29, at 149; no seed below 4096 survives step 29.
  C3 HELD on all 40,249 seeds with defect >= 4. Unexpected: the lock extends. With a first defect of length 1 the
     valuation is exactly 3 j0 + 1 (61,807 seeds), with length 2 exactly 3 j0 + 2 (47,523 seeds). Reason: the
     T-code map is a 2-adic isometry (G51), so v_2(19 a0 + 9) = v_2(a0 + 9/19) is the length of the common prefix of
     a0's code and (100)^infinity; the defect block 1, 10 or 10..0 (four or more) differs from 100 at its 2nd, 3rd or
     4th symbol.
  C4 HELD at every W = 1..10 for all five sets, first-empty steps well inside the bounds: window 3/8 at most 15
     (W = 10, claim 25); union 7/12 at most 14 (claim 22); union 2/3 at most 17 (claim 24); union 25/36 at most 17
     (claim 26); base 4/3 window at most 9 (claim 18). Control HELD: the propagator gives 29 for Mahler at W = 12.
  Extra (scratch, same day): the window (2/7, 5/7) keeps 1, 2, 4, 6, 10, ..., 166 carry branches at depths 0..15,
     Mahler's binary partition numbers, and 200 against 202 at depth 16, exactly as their theorem states.
  Lean build (clean environment, no secrets): 142 of 142 files, 1,944 jobs, 0 errors, 0 warnings, 0 sorry; 637 axiom
     reports, all within propext, Quot.sound, Classical.choice; an independent #print axioms on 19 headline theorems
     agrees. Two names in their paper's table differ from the code (shifted_three_eighths_... is
     window_three_eighths_...; dubickas2008_closed_union_explicit_and_infinite_escape is two theorems).
"""
import sys, random
from fractions import Fraction as F

def horizon(n, cap=10**6):
    """First step j at which the window for seeds in [n, n+1) is empty (exact integer comparison)."""
    # compare lo = n_i 2^i / 3^i and hi = (2 n_i + 1) 2^(i-1) / 3^i over a common denominator 3^j as the walk goes
    lo_num, lo_den = n, 1              # max lower bound as a fraction num/den
    hi_num, hi_den = 2 * n + 1, 2      # min upper bound
    x, p2, p3 = n, 1, 1
    for j in range(1, cap):
        x = (3 * x + 1) // 2           # ceil(3x/2)
        p2 *= 2; p3 *= 3
        a_num, a_den = x * p2, p3              # n_j (2/3)^j
        b_num, b_den = (2 * x + 1) * p2, 2 * p3   # (n_j + 1/2)(2/3)^j
        if a_num * lo_den > lo_num * a_den: lo_num, lo_den = a_num, a_den
        if b_num * hi_den < hi_num * b_den: hi_num, hi_den = b_num, b_den
        if lo_num * hi_den >= hi_num * lo_den: return j
    return None

def v2(x):
    c = 0
    while x % 2 == 0: x //= 2; c += 1
    return c

def blocks(a0, k):
    b, out = a0, []
    for _ in range(k):
        t = 3 * b + 1; s = v2(t); u = t >> s; out.append(s); b = 3 ** (s - 1) * u
    return out

def lock_case(a0):
    """(j0, defect length, v2(19 a0 + 9)) for an odd seed, or None if the first 40 blocks are all 3."""
    bl = blocks(a0, 40); j0 = 0
    while j0 < len(bl) and bl[j0] == 3: j0 += 1
    if j0 == len(bl): return None
    return j0, bl[j0], v2(19 * a0 + 9)

def propagate(U, r, W, maxn):
    """First n with no xi in [1, 2^W) keeping {xi r^n'} in U for all n' <= n. U: list of half-open [l, r)."""
    S = [(F(1), F(2 ** W))]
    rn = F(1)
    for n in range(maxn + 1):
        T = []
        for a, b in S:
            xa, xb = a * rn, b * rn
            for k in range(xa.numerator // xa.denominator, -(-xb.numerator // xb.denominator) + 1):
                for l, rr in U:
                    lo, hi = max(xa, k + l), min(xb, k + rr)
                    if lo < hi: T.append((lo / rn, hi / rn))
        S = T
        if not S: return n
        rn *= r
    return None

UNIONS = {
    'window 3/8 [1/6,13/24) base 3/2, claim W+15': ([(F(1, 6), F(13, 24))], F(3, 2), 15),
    'union 7/12, claim W+12': ([(F(0), F(1, 6)), (F(1, 4), F(1, 3)), (F(5, 12), F(2, 3)), (F(3, 4), F(5, 6))], F(3, 2), 12),
    'union 2/3, claim W+14': ([(F(0), F(1, 9)), (F(1, 6), F(4, 9)), (F(1, 2), F(5, 9)), (F(11, 18), F(7, 9)), (F(5, 6), F(8, 9))], F(3, 2), 14),
    'union 25/36, claim W+16': ([(F(0), F(1, 12)), (F(1, 9), F(11, 36)), (F(4, 9), F(2, 3)), (F(25, 36), F(3, 4)), (F(5, 6), F(8, 9)), (F(11, 12), F(1))], F(3, 2), 16),
    'window 7/24 [1/3,5/8) base 4/3, claim W+8': ([(F(1, 3), F(5, 8))], F(4, 3), 8),
}

if __name__ == '__main__':
    print('C1:', 'H(149) =', horizon(149), '| H(29871555608238677) =', horizon(29871555608238677),
          '| H(9850069454682037) =', horizon(9850069454682037),
          '| bits:', (29871555608238677).bit_length(), (9850069454682037).bit_length())
    hs = [(horizon(n), n) for n in range(1, 4096)]
    print('C2: max horizon below 4096 =', max(hs), '| seeds below 4096 surviving step 29:', sum(1 for h, n in hs if h > 29))
    random.seed(20261019); stats = {}; bad = []
    inv19 = pow(19, -1, 2 ** 200)
    for trial in range(200000):
        K = random.randrange(3, 120)
        base = (-9 * inv19) % 2 ** K            # agrees with -9/19 on K bits: many leading 3-blocks
        a0 = base + (2 ** K) * random.randrange(1, 2 ** 40)
        if trial % 2: a0 = random.randrange(1, 2 ** 64)
        if a0 % 2 == 0: continue
        c = lock_case(a0)
        if c is None: continue
        j0, s, v = c
        key = 's>=4' if s >= 4 else f's={s}'
        st = stats.setdefault(key, [0, 0, {}]); st[0] += 1
        if v == 3 * j0 + 3: st[1] += 1
        else:
            d = v - (3 * j0 + 3); st[2][d] = st[2].get(d, 0) + 1
            if s >= 4 and len(bad) < 5: bad.append((a0, j0, s, v))
    for key in sorted(stats):
        n, ok, diffs = stats[key]
        print(f'C3: defect {key}: {n} seeds, v2 = 3 j0 + 3 on {ok}; other offsets {dict(sorted(diffs.items()))}')
    print('C3: counterexamples with defect >= 4:', bad)
    print('C4 control (Mahler [0,1/2), base 3/2, W = 12): first empty step', propagate([(F(0), F(1, 2))], F(3, 2), 12, 60))
    Wmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    for name, (U, r, c) in UNIONS.items():
        firsts = [propagate(U, r, W, W + c + 5) for W in range(1, Wmax + 1)]
        held = all(f is not None and f <= W + c for W, f in zip(range(1, Wmax + 1), firsts))
        print(f'C4: {name}: first empty step for W = 1..{Wmax}: {firsts}; claim holds at every W: {held}')
