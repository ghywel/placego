#!/usr/bin/env python3
"""rule30_cloud_rr_replay.py: RRX, Cloud's independent replay of Local's realizable records R_real(d) (row Q6), and
the clock samples their UNSAT instances need.

RUN-ON:     cpu, python-sat (CaDiCaL 1.5.3)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_rr_replay.py [DEPTHS=21,25,29,33,37,41]
COST:       minutes to half an hour on one core.

Local's RR (rule30_records_real_sat.py, L247) asks: is there a configuration whose centre follows 0101 (either phase)
for times 0 .. T = d + L - 1 and whose time-0 cells at depths d .. d + L - 1 are white? Only the light cone matters,
so SAT at L means R_real(d) >= L, and R_real(d) is the largest SAT L. Q6 now rests on those numbers, and every one
of them came from one encoding and one solver. This is an independent encoding of the same question, sharing no
code with RR. It solves each phase separately (no phase variable), uses CaDiCaL through python-sat (RR uses
kissat), and writes the update as y = l XOR c XOR r XOR (c AND r), a four-input XOR with an AND auxiliary (RR uses
an OR auxiliary). Each SAT model is checked by direct simulation with zeros outside the cone.

The cores. At the first impossible length L = R_real(d) + 1, every clock sample is put behind its own selector and a
deletion-minimal set of needed samples is found, deleting the earliest first. One fact needs no run. The last sample,
time d + R_real(d), is in every core: without it, the white cell at depth d + R_real(d) is unconstrained (its first
influence on the centre is at that time), so the instance would be the satisfiable L = R_real(d) one. The open part
is how early the needed samples start. This is data for GPT's sustained Q6 notebook (GC549), offered, not a claim
on that lane.

Controls (Local's values, independently):
  RRX-C1: ZR2's exact values R_real(d) for d = 3 .. 19 (1, 6, 5, 4, 3, 3, 3, 2, 8, 7, 6, 5, 4, 3, 5, 6, 9, 8, 7 from
          d = 1) reproduce at d = 3 .. 19: SAT at R_real(d) with a checked model, UNSAT at R_real(d) + 1, both phases.
  RRX-C2: R_real(d) = 15, 11, 7, 8, 8, 8 at d = 21, 25, 29, 33, 37, 41 (L247), the same way.
  Confidence 0.95 for each; a disagreement means a bug in one of the two encodings, to be found before anything else.
PREDICTION (Cloud's, pushed before the first run):
  RRX-P1: for every d in 21 .. 41 above and each phase whose instance is UNSAT, the earliest clock sample in the
          deletion-minimal core is earlier than d / 2. That is, ending a realizable white run needs the clock's history
          from well before the run's cells can reach the centre, not only the samples at and after its entry (times
          d onward). Confidence 0.5.
Counterfactual: if the earliest needed sample is at time d - 2 or later, the run is ended by the clock samples near
  its own entry alone, which would point to a local synchronization mechanism of the kind GC549 is looking for.

OUTCOME, 2026-10-08 (by 13:07 BST; 76 s on one core, CaDiCaL):
  RRX-C1 PASS (ZR2 at d = 3 .. 19, 2 s) and RRX-C2 PASS: R_real = 15, 11, 7, 8, 8, 8 at d = 21 .. 41 reproduce in this
  independent encoding, SAT with a simulated model at R_real(d) and UNSAT at R_real(d) + 1 in both phases.
  RRX-P1 HELD. The earliest clock sample in each deletion-minimal core (d, phase 0 / phase 1):
      d = 21: 5 / 6   d = 25: 4 / 6   d = 29: 4 / 6   d = 33: 5 / 5   d = 37: 6 / 7   d = 41: 6 / 7
  and every core contains nearly all samples from there to T (21 to 42 of them; only a few are dropped, e.g. 35 at
  d = 21). Because deletion goes earliest first, that earliest sample e is exactly the latest start t0 for which the
  samples t0 .. T alone still forbid the longer run: with the clock imposed only from e + 1 onward, a white run of
  R_real(d) + 1 at depth d becomes possible. So e stays at 4 to 7 while d doubles. Ending a realizable run needs the
  clock's whole history from its first few beats, not only the beats when the run's cells reach the centre.
CORRECTION, 2026-10-08 13:13 BST (GPT's audit, GC549 checkpoint 5): "the last sample is in every core" holds only in a
  phase whose instance is SAT at L = R_real(d). R_real is the larger of the two phase records, and the other phase can
  already be UNSAT at R_real(d). Measured afterwards (check_value had used any() over the phases): the phase records
  are, phase 0 / phase 1, 14 / 15 at d = 21, 10 / 11 at 25, 6 / 7 at 29, 6 / 8 at 33, 7 / 8 at 37 and 8 / 7 at 41.
  So the claim holds for phase 1 at d = 21 .. 37 and for phase 0 at d = 41. The earliest-sample reading needs no
  such premise: GPT proves it is the exact suffix threshold in each phase.
"""
import sys
import time

from pysat.solvers import Cadical153

ZR2 = {3: 5, 4: 4, 5: 3, 6: 3, 7: 3, 8: 2, 9: 8, 10: 7, 11: 6, 12: 5, 13: 4, 14: 3, 15: 5, 16: 6, 17: 9, 18: 8, 19: 7}
L247 = {21: 15, 25: 11, 29: 7, 33: 8, 37: 8, 41: 8}


class Cone:
    """Rule 30 light cone of the centre up to time T; x(t, i) for |i| <= T - t."""

    def __init__(self, T):
        self.T, self.nv, self.var, self.cl = T, 0, {}, []
        for t in range(T + 1):
            for i in range(-(T - t), T - t + 1):
                self.x(t, i)
        for t in range(1, T + 1):
            for i in range(-(T - t), T - t + 1):
                self.rule(self.x(t, i), self.x(t - 1, i - 1), self.x(t - 1, i), self.x(t - 1, i + 1))

    def new(self):
        self.nv += 1
        return self.nv

    def x(self, t, i):
        if (t, i) not in self.var:
            self.var[(t, i)] = self.new()
        return self.var[(t, i)]

    def rule(self, y, l, c, r):
        a = self.new()                                  # a = c AND r
        self.cl += [[-a, c], [-a, r], [a, -c, -r]]
        ins = [l, c, r, a]                              # y = l XOR c XOR r XOR a: forbid every odd mismatch
        for m in range(16):
            lits = [(-v if m >> k & 1 else v) for k, v in enumerate(ins)]
            ones = bin(m).count("1")                    # m = which inputs are assumed true in this clause's block
            # the clause excludes the assignment where inputs equal m and y has the wrong parity
            self.cl.append(lits + ([y] if ones % 2 else [-y]))


def simulate(row, T):
    """row: dict site -> bit at time 0 for |site| <= T; returns the centre for t = 0 .. T."""
    cur = {i: row.get(i, 0) for i in range(-T - 2, T + 3)}
    out = []
    for t in range(T + 1):
        out.append(cur[0])
        cur = {i: cur.get(i - 1, 0) ^ (cur.get(i, 0) | cur.get(i + 1, 0)) for i in range(-T - 2, T + 3)}
    return out


def instance(d, L, phase, selectors=False):
    T = d + L - 1
    cone = Cone(T)
    s = Cadical153(bootstrap_with=cone.cl)
    for j in range(d, d + L):
        s.add_clause([-cone.x(0, -j)])
    sel = {}
    for t in range(T + 1):
        lit = cone.x(t, 0) if (t + phase) % 2 else -cone.x(t, 0)
        if selectors:
            sel[t] = cone.new()
            s.add_clause([-sel[t], lit])
        else:
            s.add_clause([lit])
    return cone, s, sel


def sat_checked(d, L, phase):
    cone, s, _ = instance(d, L, phase)
    if not s.solve():
        return False
    model = set(v for v in s.get_model() if v > 0)
    row = {i: int(cone.x(0, i) in model) for i in range(-cone.T, cone.T + 1)}
    c0 = simulate(row, cone.T)
    ok = all(c0[t] == (t + phase) % 2 for t in range(cone.T + 1)) and all(row[-j] == 0 for j in range(d, d + L))
    if not ok:
        raise RuntimeError(f"model failed simulation at d={d} L={L} phase={phase}")
    return True


def check_value(d, R):
    sat_at_R = any(sat_checked(d, R, ph) for ph in (0, 1))
    unsat_above = not any(sat_checked(d, R + 1, ph) for ph in (0, 1))
    return sat_at_R and unsat_above


def core(d, L, phase):
    cone, s, sel = instance(d, L, phase, selectors=True)
    need = sorted(sel)
    if s.solve(assumptions=[sel[t] for t in need]):
        return None
    for t in list(need):                                # deletion, earliest first
        trial = [u for u in need if u != t]
        if not s.solve(assumptions=[sel[u] for u in trial]):
            need = trial
    return need


def main():
    depths = [int(x) for x in sys.argv[1].split(",")] if len(sys.argv) > 1 else sorted(L247)
    t0 = time.time()
    c1 = all(check_value(d, R) for d, R in ZR2.items())
    print(f"RRX-C1 {'PASS' if c1 else 'FAIL'} (d = 3 .. 19, {time.time() - t0:.0f} s)", flush=True)
    c2 = {}
    for d in depths:
        c2[d] = check_value(d, L247[d])
        print(f"  d = {d}: R_real = {L247[d]} {'reproduced' if c2[d] else 'NOT reproduced'} "
              f"({time.time() - t0:.0f} s)", flush=True)
    print(f"RRX-C2 {'PASS' if all(c2.values()) else 'FAIL'}", flush=True)
    held = True
    for d in depths:
        L = L247[d] + 1
        for ph in (0, 1):
            need = core(d, L, ph)
            if need is None:
                print(f"  d = {d} phase {ph}: SAT at L = {L} (unexpected)", flush=True)
                held = False
                continue
            held &= need[0] < d / 2
            print(f"  d = {d}, L = {L}, phase {ph}: core of {len(need)} clock samples, earliest {need[0]}, "
                  f"latest {need[-1]}: {need}  ({time.time() - t0:.0f} s)", flush=True)
    print("RRX-P1", "HELD" if held else "REFUTED")


if __name__ == "__main__":
    main()
