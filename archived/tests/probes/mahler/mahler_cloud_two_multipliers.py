#!/usr/bin/env python3
"""mahler_cloud_two_multipliers.py: TM, door (c). Do Mahler's two places supply Furstenberg's second multiplier?

RUN-ON:     cpu (Python 3 standard library; exact fractions)
COMMAND:    python3 tests/probes/mahler/mahler_cloud_two_multipliers.py [TMAX=24]
COST:       expected seconds.

Why. CONSTELLATION.md section H, door (c), and INSTINCT-CLOUD.md S2. Furstenberg's x2 x3 theorem pins down a single
orbit only when two independent multipliers act together, and Mahler's problem has one (x3/2). In the record's coding
(MAHLER.md section 1, G50, G51), each candidate lives in two places at once. The series S(b) gives the fractional part
u_0 in the reals and minus the integer part in the 2-adic integers. Could the pair of places supply the missing
second multiplier?

Setting. T(x) = (3x + (x mod 2))/2 on the 2-adic integers, with b_j the parity of T^j(x), and
u_j = sum_k b_(j+k) 2^k / 3^(k+1). A = S_strict is the set of x with every u_j < 1/2. Mahler's conjecture says A holds no
positive ordinary integer. At depth T, A_T is the set of residues mod 2^T whose length-T parity prefix is admissible:
some u_0 in [0, 1/2) yields it greedily (b = 1 exactly when u >= 1/3, then u -> (3u - b)/2). Admissible prefixes are
enumerated with exact interval arithmetic. A prefix becomes its residue by x = -C 3^(-T) mod 2^T, with
C = sum_j b_j 3^(T-1-j) 2^j (G51's nested residues).

Two lemmas by hand (RULE30-PRIZE.md 8.109), whose finite shadows are checked here.
  L1: for every y, 2y is in A if and only if 3y is. (T(2y) = 3y, and u_0(2y) = (2/3) u_0(3y).) So A is invariant
      under x -> 2x/3, which is T's inverse branch on the even numbers: the single Mahler direction.
  L2: A is invariant under neither x -> 3x nor x -> 2x. On Z_2, x3 is an isometry, and the closure of {3^n} is
      (1 + 8 Z_2) united with 3(1 + 8 Z_2), which is open. So a nonempty closed x3-invariant set contains an open piece
      of a sphere and has dimension 1, while A's closure has dimension log2(3/2) (GC1221). By L1, x2 fails too.
Reading if both hold: in the 6-adic solenoid the two places merge into the one diagonal map x3/2, a rank-one symmetry,
and Furstenberg, Rudolph and Einsiedler-Lindenstrauss rigidity needs rank two. Door (c) closes, and the record gets
the place where the second multiplier fails.

PREDICTIONS, written 2026-10-14 before any run and pushed before it.
  C0 (exact control): the prefix-to-residue formula agrees with direct iteration of T on 2,000 random residues per depth.
  C1 (exact control): |A_T| = 2, 3, 5, 8, 12, 18, 27, 40, 60, 90 for T = 1 .. 10, MAHLER.md section 1's A(T). An index
     shift of one would be reported as a convention difference, not a pass.
  C2 (exact, L1's shadow): {y mod 2^T : 2y mod 2^(T+1) in A_(T+1)} = {3^(-1) r mod 2^T : r in A_T} at every T <= TMAX.
  P1 (0.7, L2's shadow): the fraction f3(T) of A_T mapped into A_T by x3 falls, is below 0.25 by T = 24, and is never 1
     for T >= 10. The same holds for x2.
  P2 (0.6): f3 decays roughly geometrically, with a ratio per step between 0.7 and 0.95 over T = 12 .. 24.
  U, the unexpected check (0.5): 3 is not special. f5(T), for the unit 5, which has nothing to do with Mahler's map,
     is within a factor 2 of f3(T) at T = 24.
  Counterfactual. f3(T) staying near 1 at large T would make A nearly x3-invariant at every finite depth. That would
  contradict L2's dimension argument, or my reading of GC1221, and reopen door (c).

OUTCOME, 2026-10-14 20:00 BST (predictions pushed in 2306731; 2.5 s; the addendum 25 s).
  C0, C1 and C2 PASS. |A_T| equals the record's A(T) exactly, and L1's finite form holds to T = 24.
  P1 HELD: f3 falls to 0.0001 at T = 24 and is never 1 after T = 1; the same for f2.
  P2 REFUTED: f3 falls by exactly 2/3 a step (0.666 to 0.668). Exactly two residues survive at every depth, 0 and
    2^(T-1), the depth-T shadow of 0, while |A_T| grows like (3/2)^T.
  U REFUTED: 3 is special. f5 decays like a density (about 3/4 a step; 0.0053 at T = 24, fifty times f3).
  Post hoc (`addendum`): s(T) = {0, 2^(T-1)} for every T <= 28, and the four lifts behave as the induction says. That
  led to the theorem of RULE30-PRIZE.md 8.109: K meets 3K, K/3, 2K and K/2 only in 0. It is stronger than L2, which
  it replaces.
"""
import random
import sys
from fractions import Fraction as F

TMAX = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 24
REF = [2, 3, 5, 8, 12, 18, 27, 40, 60, 90]


def admissible(T):
    """Admissible length-T parity prefixes, by exact interval arithmetic on u_j."""
    level = [((), F(0), F(1, 2))]
    third = F(1, 3)
    for _ in range(T):
        nxt = []
        for bits, lo, hi in level:
            a, b = lo, min(hi, third)
            if a < b:
                nxt.append((bits + (0,), 3 * a / 2, 3 * b / 2))
            a, b = max(lo, third), hi
            if a < b:
                nxt.append((bits + (1,), (3 * a - 1) / 2, (3 * b - 1) / 2))
        level = nxt
    return [bits for bits, _, _ in level]


def residue(bits):
    T = len(bits)
    m = 1 << T
    C = sum(b * 3 ** (T - 1 - j) * 2 ** j for j, b in enumerate(bits))
    return (-C * pow(3, -T, m)) % m


def parities(r, T):
    out = []
    x = r
    for _ in range(T):
        b = x & 1
        out.append(b)
        x = (3 * x + b) // 2
    return tuple(out)


def main():
    rnd = random.Random(20261014)
    c0 = all(residue(parities(r, T)) == r % (1 << T)
             for T in range(1, 21) for r in (rnd.getrandbits(T + 8) for _ in range(2000)))
    print('C0 prefix -> residue formula agrees with direct iteration (T = 1..20, 2,000 each):', c0)
    A = {T: {residue(p) for p in admissible(T)} for T in range(1, TMAX + 2)}
    sizes = [len(A[T]) for T in range(1, 11)]
    print('C1 |A_T| for T = 1..10: %s; record %s; equal: %s' % (sizes, REF, sizes == REF))
    c2 = True
    for T in range(1, TMAX + 1):
        m = 1 << T
        s1 = {(r >> 1) % m for r in A[T + 1] if r % 2 == 0}
        s2 = {(pow(3, -1, m) * r) % m for r in A[T]}
        c2 &= s1 == s2
    print('C2 (L1) 2y in A_(T+1) <=> 3y in A_T, every T <= %d:' % TMAX, c2)
    print('\n  T   |A_T|   density    f2      f3      f5')
    rows = {}
    for T in range(1, TMAX + 1):
        m = 1 << T
        S = A[T]
        f = {k: sum(1 for r in S if (k * r) % m in S) / len(S) for k in (2, 3, 5)}
        rows[T] = f
        print('%3d  %6d  %.6f  %.4f  %.4f  %.4f' % (T, len(S), len(S) / m, f[2], f[3], f[5]))
    ratios = [rows[T + 1][3] / rows[T][3] for T in range(12, TMAX) if rows[T][3] > 0]
    print('\nf3 step ratios over T = 12..%d: min %.3f, max %.3f' % (TMAX, min(ratios), max(ratios)))


def addendum(TMAX2=28):
    """Post hoc (added after the run, 2026-10-14 20:01 BST): the exact survivor sets behind f3, and the parity facts that
    carry the induction in RULE30-PRIZE.md 8.109. s(T) = {r in A_T : 3r mod 2^T in A_T} is claimed to be {0, 2^(T-1)}."""
    ok_s, ok_par = True, True
    for T in range(1, TMAX2 + 1):
        m = 1 << T
        S = {residue(q) for q in admissible(T)}
        s = {r for r in S if (3 * r) % m in S}
        ok_s &= s == {0, 1 << (T - 1)}
        if T >= 2:
            m1 = 1 << (T + 1)
            S1 = {residue(q) for q in admissible(T + 1)}
            r = 1 << (T - 1)
            ok_par &= ((r in S1) == (T % 2 == 1)) and (((3 * r) % m1 in S1) == (T % 2 == 0))
            r2 = 3 << (T - 1)
            ok_par &= ((r2 in S1) == (T % 2 == 0)) and (((3 * r2) % m1 in S1) == (T % 2 == 1))
            ok_par &= (1 << T) in S1 and (3 << T) % m1 in S1
    print('addendum: s(T) = {0, 2^(T-1)} for every T <= %d: %s' % (TMAX2, ok_s))
    print('addendum: the four lifts behave as the induction says (T = 2..%d): %s' % (TMAX2, ok_par))


if __name__ == '__main__':
    if sys.argv[1:2] == ['addendum']:
        addendum()
    else:
        main()
