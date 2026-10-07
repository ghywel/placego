#!/usr/bin/env python3
"""rule30_kick_angles.py: KA, why class 12. The kick classes read in the wheel's own coordinate, its rotation angle.

RUN-ON:     cpu; part B needs python-sat (CaDiCaL)
COMMAND:    python3 tests/probes/lexicon/rule30_kick_angles.py            (part A: angles and landing windows)
            python3 tests/probes/lexicon/rule30_kick_angles.py --death C1 C2 ...   (part B: exact death times)
COST:       part A a minute or two; part B minutes to an hour per class.

The owner's question (2026-10-07): "The impossible class-12 - why 12. Why that number. ... Can we bisect and dissect
the number 12 specifically and why it sticks out and is impossibly stuck." A class is a position in the wheel's
56-step cycle, (t - d) mod 56, and the wheel U codes the rotation by 17/56 of a turn per step. So the class's
meaning is its angle, 17 a mod 56 (in 56ths of a turn; a notch, 1/28 of a turn, is two of these).

Found by looking, before any test (Cloud, 2026-10-07; not evidence):
  - U on the circle: a solid white arc at angles 16 .. 38, a solid black arc at 44 .. 55, and two combs that
    alternate with the wall, 39 .. 43 and 0 .. 15.
  - The four settled classes (entry 26) sit at angles 36 (class 12), 40 (32), 42 (42, exactly 3/4 of a turn) and
    44 (52). The three that survive (entry 27) are one unbroken run, notches 20, 21, 22; class 12 is notch 18,
    behind a gap at notch 19.
  - Every forward kick in entry 26's settled table lands in the same window, angles 44 .. 52, whatever class it
    departs from (from 42 by +1 .. +5 notches, from 40 by +2 .. +6, from 36 by +4 .. +8), and every backward kick
    (class 52, from 44) lands in 32 .. 42. So the landing zone is fixed and the size is the distance to it; class 12
    is the departure furthest from the zone.

Part A computes the angle table, and the landing angles of every kick in entry 26's tables at m = 16, settled and
after one turn. Part B finds, for each class, the least time on the wheel N at which no right side at all can make
that departure (full light cone, satisfiability; KS's encoding imported from rule30_kick_bite_sat.py). All-case
unsatisfiability is monotone in N (GPT's GC373), so a bisection over N is sound.

PREDICTIONS (Cloud's, pushed before either part first ran):
  KA-C1 (control): part B gives class 12's death time as 127 (one case alive at 126, none at 127), as Local's KLK
        found with kissat and an independent encoding (L227).
  KA-P1: in the one-turn table at m = 16, every forward kick lands in angles 44 .. 52 and every backward kick in
        32 .. 42, for every class, 2, 22, 39 and 49 included. Confidence 0.5. The settled table cannot count: that is
        where the pattern was seen.
  KA-P2: the other white-arc departures, classes 2 (angle 34) and 22 (angle 38), die before class 12, at N < 127.
        Confidence 0.7. That would make class 12 the last white-arc departure to die.
  KA-P3: the odd classes 39 and 49 (angles 47 and 49, inside the black arc) die before N = 127. Confidence 0.6.
Counterfactual: if KA-P1 fails broadly, the landing window is a coincidence of four classes. If a white-arc class
outlives class 12, "furthest from the landing zone" is not why class 12 is special.

OUTCOME, part A, 2026-10-07 22:44 BST (one run, 6 s):
  Settled at m = 16: the pattern as seen (forward landings 44 .. 52, backward 32 .. 42).
  KA-P1 REFUTED as written, on two counts. After one turn, forward kicks also land at 54. And the odd classes 39 and
  49 (angles 47 and 49) kick back to odd angles 27 .. 35, a window of their own that the prediction did not foresee.
  What held: the five even take-off points after one turn, classes 2, 12, 22, 32 and 42 at angles 34, 36, 38, 40 and
  42, offer 28 kicks between them, and all 28 land inside the one window 44 .. 54. Each class's sizes shift by one
  notch per two 56ths of take-off angle (+5 .. +10, +4 .. +9, +3 .. +8, +2 .. +7, +1 .. +6), which is what keeps the
  landings fixed. Settling trims the window's top from 54 to 52. Class 2 lacks the landing at 52.
  Reading: a forward kick is column 1 turning black early. The rotating point is moved into the start of the black
  arc, angles 44 .. 54, and the class records only where it took off from.

PART C (post-hoc, after the owner asked Cloud to reason through the mode-locking reading itself; written before
--sizes first ran, 2026-10-07 23:00 BST). The record already measured that the wheel's phase diffuses with no
restoring force (sections 8.10, 8.11, 8.43, 8.47): its frequency is locked, its phase is free. Inside that picture,
the thin locked strip (columns 2 to 4 or 5) is a filter on the interior's noise, and class 12 may be a large slip the
filter removes as the lock ages. Part C finds the death time of each class-12 kick size (+4 .. +9) on its own.
  KA-P4: the larger the kick, the sooner it dies (death time non-increasing from +4 to +9). Confidence 0.5. If a
         larger kick outlives a smaller one, "class 12 is a large slip the lock suppresses" is wrong.
OUTCOME, part C, 2026-10-07 (by 23:13 BST; three processes, CaDiCaL): kicks +4, +5, +6, +7 and +8 (landing at
  angles 44 to 52) are each possible after 126 steps on the wheel and impossible from 127; kick +9 (landing at 54)
  dies at 40. KA-P4 held only by its letter, since the times never increase but are tied. The reading it tested is
  refuted: there is no size cutoff tightening with time. All of class 12's kicks die together, so what dies at 127
  is the take-off at angle 36 itself, wherever it would land. The early death of +9 is the landing window's top
  edge, 54, the one that settling removes.

OUTCOME, part B, 2026-10-07 (finished by 22:48 BST; one run per class, CaDiCaL):
  KA-C1 PASS: class 12 is possible after 126 steps on the wheel and impossible from 127, Local's KLK value from an
        independent encoding and solver.
  Death times: class 22 (angle 38) at 53; class 2 (34) at 61; class 49 (49) at 61; class 39 (47) at 70; class 12
        (36) at 127. KA-P2 HELD and KA-P3 HELD.
  But the explanation behind KA-P2 fails. Class 2 takes off further from the landing window than class 12 does and
  dies at 61, so distance from the landing zone is not what keeps class 12 alive. What stands out is the death time
  itself: every other temporary launch point dies within about one turn (53 to 70 steps), while class 12 lasts
  about two (127), between two neighbours (34 and 38) that both die early.
  The last witness (exploratory, no prediction): at N = 126 the one live case is t0 = 0, phase 2, departure at 126,
  kick +5. Over the last turn before the kick, column 1 repeats exactly. Columns 2, 3 and 4 match the turn before
  except for 1, 2 and 3 cells just before the kick (at s - 1, s - 4 and s - 5). Columns 5 and 6 differ at 8 and 14 of
  56 times. Columns 7 to 44 differ at about half. So the lock is the thin strip GPT pinned (GC373, GC374), and the
  kick comes in as a front crossing it, column 4 then 3 then 2 then 1, in the zigzag of section 8.43. Nothing beyond
  column 6 repeats, so there is no second periodic object behind class 12 in this witness.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_kick_layers as kl                              # noqa: E402
sys.argv = _argv

U, P = kl.U, kl.P


def angle(a):
    return (17 * a) % P


def part_a():
    print("U by angle (56ths of a turn):")
    print("  ones :", sorted(angle(a) for a in range(P) if U[a]))
    print("  zeros:", sorted(angle(a) for a in range(P) if not U[a]))
    t0 = time.time()
    for name, sets in (("settled m = 16", kl.settled(16, kl.step_row)),
                       ("one turn m = 16", kl.one_turn_sets(16, kl.step_row))):
        table = kl.kicks_from(sets, 16, kl.step_row)
        print(f"{name}  ({time.time() - t0:.0f} s):")
        fwd, back = set(), set()
        for a, ks in sorted(table.items()):
            lands = [(angle(a) + 2 * k) % P for k in ks]
            print(f"  class {a:2d}, angle {angle(a):2d}, notch {angle(a) / 2:4.1f}: kicks {ks} land at angles {lands}")
            fwd |= {x for k, x in zip(ks, lands) if k > 0}
            back |= {x for k, x in zip(ks, lands) if k < 0}
        print(f"  forward landings {sorted(fwd)}; backward landings {sorted(back)}")
        if name.startswith("one"):
            ok = fwd <= set(range(44, 53)) and back <= set(range(32, 43))
            print("KA-P1", "HELD" if ok else "REFUTED")


def part_b(classes):
    import rule30_kick_bite_sat as ks

    def alive(cls, N):
        ks.N = N
        for t0 in (0, 1):
            cone = ks.Cone(t0, t0 + N + P + ks.F + 1)
            for d in range(0, P, 2):
                act, s, sels = ks.instance(cone, cls, d)
                if cone.s.solve(assumptions=[act]):
                    return True
        return False

    start = time.time()
    for cls in classes:
        lo, hi = 0, 168                                      # alive at lo (assumed, checked), dead at hi (checked)
        if alive(cls, hi):
            print(f"class {cls:2d} (angle {angle(cls):2d}): still possible after {hi} steps"
                  f"  ({time.time() - start:.0f} s)", flush=True)
            continue
        if not alive(cls, lo):
            print(f"class {cls:2d}: impossible even at N = 0", flush=True)
            continue
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if alive(cls, mid):
                lo = mid
            else:
                hi = mid
        print(f"class {cls:2d} (angle {angle(cls):2d}, notch {angle(cls) / 2:4.1f}): possible after {lo} steps on the"
              f" wheel, impossible from {hi}  ({time.time() - start:.0f} s)", flush=True)


def part_c(cls, sizes):
    """Death time of each kick size of one class (post-hoc; KA-P4 in the header, pushed first)."""
    import rule30_kick_bite_sat as ks

    def alive(N, kick):
        ks.N = N
        for t0 in (0, 1):
            cone = ks.Cone(t0, t0 + N + P + ks.F + 1)
            for d in range(0, P, 2):
                s = next(x for x in range(t0 + N, t0 + N + P) if (x - d) % P == cls)
                act = cone.new()
                for t in range(t0, s):
                    cone.s.add_clause([-act, cone.col1(t, U[(t - d) % P])])
                dns = [dn for dn in range(0, P, 2) if U[(s - dn) % P] != U[(s - d) % P]
                       and ks.kick_of((dn - d) % P) == kick]
                if not dns:
                    continue
                for t in range(s, s + ks.F + 1):           # one size has one phase, so no selector is needed
                    cone.s.add_clause([-act, cone.col1(t, U[(t - dns[0]) % P])])
                if cone.s.solve(assumptions=[act]):
                    return True
        return False

    start = time.time()
    for kick in sizes:
        lo, hi = 0, 140
        if not alive(lo, kick):
            print(f"class {cls} kick {kick:+d}: impossible even at N = 0", flush=True)
            continue
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if alive(mid, kick):
                lo = mid
            else:
                hi = mid
        print(f"class {cls} kick {kick:+d} (lands at angle {(angle(cls) + 2 * kick) % P}): possible after {lo}"
              f" steps on the wheel, impossible from {hi}  ({time.time() - start:.0f} s)", flush=True)


if __name__ == "__main__":
    if "--sizes" in sys.argv:
        i = sys.argv.index("--sizes")
        part_c(int(sys.argv[i + 1]), [int(x) for x in sys.argv[i + 2:]])
    elif "--death" in sys.argv:
        part_b([int(x) for x in sys.argv[sys.argv.index("--death") + 1:]])
    else:
        part_a()
