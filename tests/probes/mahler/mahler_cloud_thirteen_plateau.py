#!/usr/bin/env python3
"""mahler_cloud_thirteen_plateau.py: INSTINCT-CLOUD.md S14. Is K ∩ 13K a finite set?

RUN-ON:     cpu (Python 3 standard library; exact fractions)
COMMAND:    python3 tests/probes/mahler/mahler_cloud_thirteen_plateau.py [TMAX=60]
COST:       expected seconds.

Why. RULE30-PRIZE.md 8.111: for e = 13 (sign +1), the residues r mod 2^T with r and 13 r both admissible, leaving out
0's shadows 0 and 2^(T-1), number exactly 9, with 2 dead ends, at every depth from 6 to 20. A tree with at most N
nodes a level has at most N infinite branches. If the plateau holds for ever, K ∩ 13K has at most 9 nonzero points,
while 5 and 9 grow.

Method. Membership is tested directly. Iterate T on the integer r for T steps to get the length-T code (F1), then
follow the interval [0, 1/2) along that one code with exact fractions. s(T+1) is drawn from the lifts of s(T) together
with the lifts of 0's shadows, because reduction maps survivors to survivors or shadows. This reaches depth 60 with
no enumeration of A_T.

KILL TEST, written first (instinct rule item 9). Every outcome tips.
- *ACT:* the non-shadow survivors stay at most 9 at every T <= TMAX, or die out. K ∩ 13K is then measured as finite
  (or {0}). It is recorded, and the lines go to GPT as a proposal: why 13, and what are the points?
- *HALT:* survivors exceed 9 at some T <= TMAX. The plateau was transient and the surprise dissolves.

PREDICTIONS, written 2026-10-14 before any run and pushed before it.
  C1 (exact control): the direct method's counts for 5, 9, 13 and -3 at T <= 20 equal 8.111's enumeration.
  P1 (0.6): 13 stays at exactly 9 survivors with 2 dead ends at every T <= 60.
  P2 (0.5): the lines that never die are fewer than 9 and settle by T = 30. Their residues mod 2^60 do not reconstruct
     to a rational a/c with |a|, c < 2^29, matching 8.111's lack of a periodic witness.
  U, the unexpected check (0.4): 21 = 13 + 8 and 29 = 13 + 16 plateau too, so the plateau depends on e mod 8.
"""
import sys
from fractions import Fraction as F

TMAX = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 60
THIRD, HALF = F(1, 3), F(1, 2)


def admissible_residue(r, T):
    x, lo, hi = r, F(0), HALF
    for _ in range(T):
        b = x & 1
        x = (3 * x + b) >> 1
        if b == 0:
            hi = min(hi, THIRD)
            if lo >= hi:
                return False
            lo, hi = 3 * lo / 2, 3 * hi / 2
        else:
            lo = max(lo, THIRD)
            if lo >= hi:
                return False
            lo, hi = (3 * lo - 1) / 2, (3 * hi - 1) / 2
    return True


def survivors(e, TMAX):
    """s[T] = non-shadow r mod 2^T with r and e r mod 2^T admissible; dead[T] = members of s[T] with no lift in s[T+1]."""
    s = {}
    m = 2
    s[1] = {r for r in range(2) if admissible_residue(r, 1) and admissible_residue((e * r) % m, 1)} - {0, 1}
    for T in range(1, TMAX):
        m1 = 1 << (T + 1)
        base = s[T] | {0, 1 << (T - 1)}
        nxt = set()
        for r in base:
            for rr in (r, r + (1 << T)):
                if rr in (0, 1 << T):
                    continue
                if admissible_residue(rr, T + 1) and admissible_residue((e * rr) % m1, T + 1):
                    nxt.add(rr)
        s[T + 1] = nxt
    dead = {T: sum(1 for r in s[T] if r not in s[T + 1] and r + (1 << T) not in s[T + 1]) for T in range(1, TMAX)}
    return s, dead


def rational_reconstruct(r, k, bound):
    """Find a/c with c odd, |a|, c < bound, a = c r mod 2^k (lattice reduction in two dimensions)."""
    m = 1 << k
    u0, u1, v0, v1 = m, 0, r % m, 1
    while v0 * v0 >= bound * bound:
        q = u0 // v0
        u0, u1, v0, v1 = v0, v1, u0 - q * v0, u1 - q * v1
    if v1 != 0 and abs(v1) < bound and v1 % 2 != 0 and (v0 - v1 * r) % m == 0:
        return F(v0, v1)
    return None


def main():
    ref = {5: 86, 9: 125, 13: 9, -3: 35}                    # 8.111 at T = 20
    c1 = True
    for e, n in ref.items():
        s, _ = survivors(e, 20)
        c1 &= len(s[20]) == n
    print('C1 direct method matches 8.111 at T = 20 for 5, 9, 13, -3:', c1)
    s, dead = survivors(13, TMAX)
    counts = [(T, len(s[T]), dead.get(T)) for T in range(2, TMAX)]
    print('e = 13 (T, survivors, dead ends):', ' '.join('%d:%d/%s' % c for c in counts))
    print('P1 exactly 9 survivors and 2 dead ends at every T in 6..%d: %s'
          % (TMAX - 1, all(n == 9 and d == 2 for T, n, d in counts if T >= 6)))
    print('KILL TEST bounded by 9 at every T <= %d: %s' % (TMAX, all(len(s[T]) <= 9 for T in range(2, TMAX + 1))))
    roots = sorted({r % (1 << 30) for r in s[TMAX]})
    print('P2 survivors at depth %d: %d; distinct mod 2^30 (lines alive from 30 to %d): %d'
          % (TMAX, len(s[TMAX]), TMAX, len(roots)))
    for r in sorted(s[TMAX]):
        q = rational_reconstruct(r, TMAX, 1 << 29)
        print('  r mod 2^%d = %d   2-adic rational with small height: %s   13 r -> %s'
              % (TMAX, r, q, rational_reconstruct((13 * r) % (1 << TMAX), TMAX, 1 << 29)))
    for e in (21, 29):
        s2, d2 = survivors(e, 40)
        print('U  e = %d (T, survivors): %s' % (e, ' '.join('%d:%d' % (T, len(s2[T])) for T in range(4, 41, 4))))


if __name__ == '__main__':
    main()
