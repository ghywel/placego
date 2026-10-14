#!/usr/bin/env python3
"""mahler_cloud_converse_witness.py: INSTINCT-CLOUD.md S13. Does Mahler's set meet its image under a sign +1 multiplier?

RUN-ON:     cpu (Python 3 standard library; exact fractions)
COMMAND:    python3 tests/probes/mahler/mahler_cloud_converse_witness.py
COST:       expected under a minute.

Why. RULE30-PRIZE.md 8.110's sign rule proves K ∩ eK = {0} when e = 2^a u with 3^a u = 3 mod 4. For Erdős's power
form, GPT's G295 (second-read in CL384) proves the converse: for the other sign, infinitely many points survive. Its
two-choice step works digit by digit. Mahler's admissibility is an interval condition on the tail, so the joint tree
for x and ex may dead-end. Here e is 5, 9, 13 and -3, all of sign +1. Setting as in
tests/probes/mahler/mahler_cloud_two_multipliers.py (imported):
- T(x) = (3x + (x mod 2))/2 on Z_2;
- the code b(x) is the parity sequence;
- u_j = sum_k b_(j+k) 2^k / 3^(k+1);
- S_strict holds every u_j < 1/2, and K is its closure.
x -> b(x) is a bijection with inverse b -> -S_2(b), the series summed 2-adically. For a purely periodic code w of
length p, the 2-adic and real sums are the same rational, U = P / (1 - (2/3)^p), so x = -U.

Two tests.
- *Dead-end census.* s_e(T) is the set of residues r mod 2^T with r and e r both in A_T, leaving out 0's shadows 0 and
  2^(T-1). A dead end is an r in s_e(T) with neither lift (r or r + 2^T) in s_e(T+1). Run to T = 20.
- *Witness search.* For every periodic code w of length p <= 14 with all tails below 1/2, so that x = -U(w) is in
  S_strict and nonzero, iterate T exactly on y = e x. If y's orbit repeats within 3,000 steps, its code is eventually
  periodic. All its tails are then exact rationals, and y is in S_strict exactly when every tail is below 1/2. That
  is an exact certificate that x != 0 lies in S_strict ∩ e^(-1) S_strict, so K ∩ eK != {0}.

KILL TEST, written first (instinct rule item 9, the owner, 2026-10-14).
- *Confirms the pull's question, then closes it:* an exact witness for e = 5. The Mahler half then has its converse
  at 5. The table's two cells match, and S13 closes.
- *Tips the other way, and upgrades to a proposal for GPT:* no witness for any e, and every non-shadow survivor line
  dying out (s_e(T) empty for some T <= 20). Then K ∩ eK = {0} for a sign +1 multiplier, which breaks the symmetry with
  Erdős.
- *Inconclusive tips to HALT, fixed in advance:* survivors persist but there is no periodic witness. That would be a
  set statement in S10's family with strong finite evidence already. One block is spent, the evidence is recorded,
  and there is no further block unless a mechanism appears.

PREDICTIONS, written 2026-10-14 before any run and pushed before it.
  C0 (exact control): for 200 random periodic codes w, x = -U(w) iterated under T reproduces w.
  C1 (exact control): with e = 3, s_e(T) is empty at every T (8.109: only 0's shadows survive).
  H (hand, before the run, while writing U). If y has an eventually periodic code, its 2-adic and real sums are the
     same rational, so y = -u_0(y), which lies in (-1/2, 0] when y is in S_strict. So y = e x = -e U needs e > 0 and
     U < 1/(2e). Every witness for 5 has U < 1/10, for 9 U < 1/18, and for 13 U < 1/26. For -3 the search must find
     none: y = 3U > 0. A negative multiplier can have no witness in which both codes are eventually periodic.
     Moved here from U, where it first stood as a 0.5 guess.
  W1 (0.65): an exact witness exists for e = 5 with p <= 14.
  W2 (0.55): exact witnesses exist for 9 and 13 too. None for -3 (by H).
  D1 (0.8): the joint tree for 5 has dead ends. The two-choice step fails for Mahler even where the converse holds.
  D2 (0.75): s_5(T) is nonempty at every T <= 20 and grows. The same holds for -3: the finite survivors do not see H's
     restriction, which only binds pairs whose codes are both eventually periodic.
  U, the unexpected check (0.5): the first witness for 5 (smallest period, then smallest U) has a purely periodic
     y-code, with no preperiod.

OUTCOME, 2026-10-14 22:10 BST (predictions pushed in 52c75ec; 7.6 s).
  C0, C1 and H PASS.
  W1 REFUTED and W2 REFUTED: no exact witness for 5, 9 or 13 among the 834 admissible periodic codes with p <= 14.
    None for -3, as H requires.
  D1 HELD: every joint tree has dead ends, so G295's two-choice step does not transfer to Mahler.
  D2 HELD: non-shadow survivors persist at every T <= 20 for all four multipliers. At T = 20, e = 5 has 86 (10 dead
    ends), e = 9 has 125 (15), e = -3 has 35 (4). Surprise: e = 13 plateaus at exactly 9 survivors with 2 dead ends
    at every T from 6 to 20 (every depth checked after the run; the printed rows were every third).
  Cap check after the run: no orbit reached the 3,000-step cap (the longest walk was 11 steps), so the periodic
    search is exhaustive for p <= 14.
  U not testable: there was no witness.
  KILL TEST: inconclusive (survivors persist, no periodic witness), so it TIPS TO HALT, as fixed in advance.
"""

import importlib.util
import pathlib
import random
import sys
from fractions import Fraction as F
from itertools import product

path = pathlib.Path(__file__).resolve().parent / 'mahler_cloud_two_multipliers.py'
spec = importlib.util.spec_from_file_location('tm', path)
tm = importlib.util.module_from_spec(spec)
_saved, sys.argv = sys.argv, [sys.argv[0]]
spec.loader.exec_module(tm)
sys.argv = _saved

ES = (5, 9, 13, -3)
HALF = F(1, 2)


def periodic_value(w):
    p = len(w)
    P = sum(F(b * 2 ** k, 3 ** (k + 1)) for k, b in enumerate(w))
    return P / (1 - F(2, 3) ** p)


def tails_periodic(w):
    return [periodic_value(w[j:] + w[:j]) for j in range(len(w))]


def parity(y):
    return y.numerator % 2             # denominators are odd here


def T(y):
    b = parity(y)
    return (3 * y + b) / 2, b


def orbit_code(y, nmax=3000):
    """The code of y and its exact eventual period, if the orbit repeats within nmax steps."""
    seen, code = {}, []
    for n in range(nmax):
        if y in seen:
            return code, seen[y]
        seen[y] = n
        y, b = T(y)
        code.append(b)
    return code, None


def orbit_code_bounded(y, nmax=3000):
    """As orbit_code, but stops as soon as an iterate leaves (-1/2, 0]. By H applied to each iterate, such a y cannot be
    an S_strict point with an eventually periodic code, so the prune loses no certifiable witness."""
    seen, code = {}, []
    for n in range(nmax):
        if not (-HALF < y <= 0):
            return code, None
        if y in seen:
            return code, seen[y]
        seen[y] = n
        y, b = T(y)
        code.append(b)
    return code, None


def tails_eventually_periodic(code, start):
    pre, cyc = code[:start], code[start:]
    t = tails_periodic(cyc)
    out = list(t)
    u = t[0]
    for b in reversed(pre):
        u = F(b, 3) + F(2, 3) * u
        out.append(u)
    return out


def main():
    rnd = random.Random(20261014)
    c0 = True
    for _ in range(200):
        p = rnd.randint(1, 12)
        w = tuple(rnd.getrandbits(1) for _ in range(p))
        x = -periodic_value(w)
        y, got = x, []
        for _ in range(3 * p):
            y, b = T(y)
            got.append(b)
        c0 &= tuple(got) == (w * 3)[:3 * p]
    print('C0 x = -U(w) has code w (200 random periodic codes):', c0)

    A = {T_: {tm.residue(q) for q in tm.admissible(T_)} for T_ in range(1, 22)}

    def s(e, T_):
        m = 1 << T_
        return {r for r in A[T_] if (e * r) % m in A[T_]} - {0, 1 << (T_ - 1)}
    print('C1 e = 3: no survivor beyond 0\'s shadows at any T <= 20:', all(not s(3, T_) for T_ in range(1, 21)))
    print('\nDead-end census (non-shadow survivors |s_e(T)| and dead ends)')
    for e in ES:
        row = []
        for T_ in range(2, 21):
            cur, nxt = s(e, T_), s(e, T_ + 1)
            dead = sum(1 for r in cur if r not in nxt and r + (1 << T_) not in nxt)
            row.append((T_, len(cur), dead))
        print('  e = %3d: ' % e + ' '.join('%d:%d/%d' % t for t in row if t[0] % 3 == 2 or t[0] == 20))
        print('           dead ends at some depth: %s; survivors at every T <= 20: %s'
              % (any(d for _, _, d in row), all(n for _, n, _ in row)))

    print('\nWitness search over periodic codes, p <= 14')
    found = {e: [] for e in ES}
    adm = 0
    for p in range(1, 15):
        for w in product((0, 1), repeat=p):
            if not any(w):
                continue
            t = tails_periodic(w)
            if max(t) >= HALF:
                continue
            adm += 1
            x = -t[0]
            for e in ES:
                code, start = orbit_code_bounded(e * x)
                if start is None:
                    continue
                if max(tails_eventually_periodic(code, start)) < HALF:
                    found[e].append((p, w, t[0]))
    print('  admissible periodic codes tried: %d' % adm)
    for e in ES:
        f = sorted(found[e], key=lambda z: (z[0], z[2]))
        print('  e = %3d: %d witnesses; smallest period %s; first %s; max U %s'
              % (e, len(f), f[0][0] if f else '-', (''.join(map(str, f[0][1])), str(-f[0][2])) if f else '-',
                 (float(max(z[2] for z in f)) if f else '-')))
    print('H  bounds hold: %s; no witness for -3: %s' % (
        all(z[2] < F(1, 2 * e) for e in ES if e > 0 for z in found[e]), not found[-3]))
    if found[5]:
        p, w, u = sorted(found[5], key=lambda z: (z[0], z[2]))[0]
        code, start = orbit_code(-5 * u)
        print('U  first witness for 5: w = %s, x = %s; its y-code has preperiod %d, period %d'
              % (''.join(map(str, w)), -u, start, len(code) - start))


if __name__ == '__main__':
    main()
