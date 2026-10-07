#!/usr/bin/env python3
"""rule30_kick_bite_sat.py: KS, the exact form of KB. Can ANY right half make the wheel kick at class 12?

RUN-ON:     cpu; needs python-sat (pip install python-sat), CaDiCaL through it
COMMAND:    python3 tests/probes/lexicon/rule30_kick_bite_sat.py [N=168]  |  ... --reach
COST:       minutes (to be recorded below).

Why this is exact (Cloud, 2026-10-07, while KB's hunt ran). A kick is an event in a finite window: column 1 on the
wheel U at an even phase d for N steps from a time t0, a departure at s = t0 + N or later with class (s - d) mod 56,
then 21 observations on a new even phase d'. Column 1 at time t depends only on the row at t0 within its light cone,
cells 1 .. 1 + (t - t0). So the question "does some right half, finite or infinite, with any history, make this
event?" is a finite satisfiability problem. Leaving the row at t0 unconstrained covers every history, because any
history's row at t0 is some row. Only the wall's phase at t0 matters, so t0 = 0 and t0 = 1 cover all cases. A
solution is a finite right half: cut it beyond the light cone. (This also shows that KB's split into finite and
infinite right halves could not have mattered for any single kick: finiteness can matter only for statements about
all time, such as "the kicks never stop".)

Encoding: one variable per cell of column 1's light cone over the window; Rule 30 as x' = l XOR (c OR r), with
column 0 = t mod 2 as constants; column 1 fixed to U at phase d on [t0, s); for the new phase, one selector per
eligible d' (U at phase d' must differ from U at phase d at time s), at least one selector true, and each selector
fixing column 1 to U at phase d' on [s, s + 20]. One incremental solver per t0, one activation literal per (class,
d) instance. s is the least time >= t0 + N with (s - d) mod 56 = class.

Controls:
  KS-C1 (positive): class 42 and class 32 are satisfiable for some d and t0. Real right halves make both (KB run 1:
        seeds 47231 and 63761 for class 42).
  KS-C2 (negative, the counterfactual that the encoding can say no): class 22, which KL allows after one turn but
        excludes once settled, is unsatisfiable for every d and t0 at N = 168. If it is satisfiable, either this
        encoding or entry 26 is wrong, and nothing else here is read until that is settled.
  KS-C3: every satisfying assignment found is replayed by direct simulation of its row, and column 1 reproduces
        the event.
PREDICTIONS (Cloud's, pushed before the first run):
  KS-P1: class 12 is satisfiable at N = 168: some right half makes a class-12 kick, and it is merely rare (KB found
         none in about 650 settled events). Confidence 0.6. If it is unsatisfiable for every d and t0, class 12 is
         forbidden by structure more than 20 columns out, which KL's m = 20 automaton cannot see. That would be a
         genuine bite, and the next step is the least N at which it closes.
  KS-P2: if class 12 is satisfiable, its kicks lie in KL's +4 .. +8. Confidence 0.9.

REACH (post-hoc, written after run 1's t0 = 0 half showed class 12 unsatisfiable at all 28 phases, and before
--reach first ran, 2026-10-07 21:40 BST):
  KR-C1 (control, agreement with entry 26): at width m = 20, with column 21 free, class 12 is satisfiable for some
        phase at N = 168, as KL's m = 20 automaton allows it.
  KR-P1: class 12 dies at some width between 21 and 64. Confidence 0.6; otherwise it needs more than 64 columns.
  KR-P2: in the full cone, class 12 is still satisfiable at N = 56 (KL's one-turn set allows it) and dies by
        N = 140. Confidence 0.5.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_walls as wl                                    # noqa: E402
sys.argv = _argv
from pysat.solvers import Solver                             # noqa: E402

U = [int(c) for c in wl.U]
P, F = 56, 20
N = int(sys.argv[1]) if len(sys.argv) > 1 else 168


def kick_of(dn):
    k = (-17 * (dn // 2)) % 28
    return k if k < 14 else k - 28


class Cone:
    def __init__(self, t0, E, m=None):
        """Column 1's light cone over [t0, E]. With m, only columns 1 .. m follow the rule and column m + 1 is a
        free input at every step, as in KL's m-layer automaton."""
        self.t0, self.E, self.nv, self.var = t0, E, 0, {}
        self.s = Solver(name='cadical153')
        cap = lambda t: 1 + E - t if m is None else min(1 + E - t, m + 1)
        for t in range(t0, E + 1):
            for i in range(1, cap(t) + 1):
                self.var[(t, i)] = self.new()
        for t in range(t0, E):
            for i in range(1, min(E - t, cap(t + 1)) + 1):
                if m is not None and i > m:
                    continue
                self.rule(t, i)

    def new(self):
        self.nv += 1
        return self.nv

    def rule(self, t, i):
        y, c, r = self.var[(t + 1, i)], self.var[(t, i)], self.var[(t, i + 1)]
        o = self.new()
        self.s.add_clause([-c, o])
        self.s.add_clause([-r, o])
        self.s.add_clause([c, r, -o])
        if i == 1:                                           # left neighbour is the wall, a constant
            if t % 2 == 0:
                self.s.add_clause([-y, o])
                self.s.add_clause([y, -o])
            else:
                self.s.add_clause([-y, -o])
                self.s.add_clause([y, o])
            return
        l = self.var[(t, i - 1)]
        self.s.add_clause([-y, l, o])
        self.s.add_clause([-y, -l, -o])
        self.s.add_clause([y, -l, o])
        self.s.add_clause([y, l, -o])

    def col1(self, t, bit):
        v = self.var[(t, 1)]
        return v if bit else -v


def instance(cone, cls, d):
    """Activation literal for: wheel at phase d on [t0, s), departure of class cls at s, 21 steps on a new phase."""
    t0 = cone.t0
    s = next(s for s in range(t0 + N, t0 + N + P) if (s - d) % P == cls)
    act = cone.new()
    for t in range(t0, s):
        cone.s.add_clause([-act, cone.col1(t, U[(t - d) % P])])
    sels = {}
    for dn in range(0, P, 2):
        if U[(s - dn) % P] == U[(s - d) % P]:
            continue
        z = cone.new()
        sels[z] = dn
        for t in range(s, s + F + 1):
            cone.s.add_clause([-z, cone.col1(t, U[(t - dn) % P])])
    cone.s.add_clause([-act] + list(sels))
    return act, s, sels


def replay(cone, model, d, s, dn):
    """Rebuild the row at t0 from the model and simulate column 1 directly."""
    pos = set(v for v in model if v > 0)
    t0, E = cone.t0, cone.E
    row = 0
    for i in range(1, 2 + E - t0):
        if cone.var[(t0, i)] in pos:
            row |= 1 << i
    row |= t0 % 2
    c1 = []
    for t in range(t0, s + F + 1):
        c1.append((row >> 1) & 1)
        row = (((row << 1) ^ (row | (row >> 1))) & ~1) | ((t + 1) % 2)
    ok = all(c1[t - t0] == U[(t - d) % P] for t in range(t0, s))
    return ok and all(c1[t - t0] == U[(t - dn) % P] for t in range(s, s + F + 1))


def main():
    start = time.time()
    E_of = lambda t0: t0 + N + P + F + 1
    results = {}
    replay_ok = True
    for t0 in (0, 1):
        cone = Cone(t0, E_of(t0))
        for cls in (42, 32, 22, 12):
            for d in range(0, P, 2):
                act, s, sels = instance(cone, cls, d)
                sat = cone.s.solve(assumptions=[act])
                kicks = []
                if sat:
                    model = cone.s.get_model()
                    on = [z for z in sels if model[z - 1] > 0]
                    for z in on:
                        kicks.append(kick_of((sels[z] - d) % P))
                        replay_ok &= replay(cone, model, d, s, sels[z])
                results[(t0, cls, d)] = (sat, sorted(kicks))
            ok = [(d, results[(t0, cls, d)][1]) for d in range(0, P, 2) if results[(t0, cls, d)][0]]
            print('t0 %d class %2d: satisfiable at %d of 28 phases %s  (%.0f s)'
                  % (t0, cls, len(ok), ok[:6], time.time() - start), flush=True)
    sat_cls = lambda c: [k for k, v in results.items() if k[1] == c and v[0]]
    print('KS-C1', 'PASS' if sat_cls(42) and sat_cls(32) else 'FAIL')
    print('KS-C2', 'PASS' if not sat_cls(22) else 'FAIL (class 22 satisfiable: %s)' % sat_cls(22)[:3])
    print('KS-C3', 'PASS' if replay_ok else 'FAIL')
    k12 = sorted(set(k for key, v in results.items() if key[1] == 12 and v[0] for k in v[1]))
    print('KS-P1', 'HELD' if sat_cls(12) else 'REFUTED', '(%d satisfiable instances)' % len(sat_cls(12)))
    if sat_cls(12):
        print('KS-P2', 'HELD' if all(4 <= k <= 8 for k in k12) else 'REFUTED', '(kicks seen %s)' % k12)
    print('total %.0f s' % (time.time() - start))


def reach():
    """Post-hoc (predictions in the header's REACH block, pushed first): the least width m, and the least time N on
    the wheel, at which class 12 dies."""
    global N
    start = time.time()
    N = 168
    for m in (20, 24, 28, 32, 40, 48, 64, 96):
        alive = []
        for t0 in (0, 1):
            cone = Cone(t0, t0 + N + P + F + 1, m)
            for d in range(0, P, 2):
                act, s_, sels = instance(cone, 12, d)
                if cone.s.solve(assumptions=[act]):
                    alive.append((t0, d))
        print('width m = %3d, N = 168: class 12 satisfiable at %2d of 56 (t0, phase) pairs  (%.0f s)'
              % (m, len(alive), time.time() - start), flush=True)
    for N in (56, 84, 112, 140):
        alive, dead22 = [], True
        for t0 in (0, 1):
            cone = Cone(t0, t0 + N + P + F + 1)
            for d in range(0, P, 2):
                act, s_, sels = instance(cone, 12, d)
                if cone.s.solve(assumptions=[act]):
                    alive.append((t0, d))
        print('full cone, N = %3d: class 12 satisfiable at %2d of 56 pairs  (%.0f s)'
              % (N, len(alive), time.time() - start), flush=True)


if __name__ == '__main__':
    if '--reach' in sys.argv:
        reach()
    else:
        main()
