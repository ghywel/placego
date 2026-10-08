#!/usr/bin/env python3
"""rule30_cloud_rr_phases.py: RRP, per-phase realizable records at RR's deep depths, independently (row Q6)

RUN-ON:     cpu, python-sat (CaDiCaL 1.5.3)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_rr_phases.py [DEPTHS=49,57,65,73,81]
COST:       tens of minutes on one core.

Local's L291, accepting Cloud's CL036 offer: RR's deep records R_real(d) = 11, 11, 11, 10, 12 at d = 49, 57, 65, 73,
81 (L247) come from one encoding and one solver, and they are maxima over the two clock phases (RR's encoding has a
phase variable). Section 8.36's free record R(d) is the phase-0 record. This probe replays them in RRX's independent
encoding (rule30_cloud_rr_replay.py: CaDiCaL, an AND auxiliary, no phase variable, every SAT model checked by direct
simulation) and splits them by phase. R_ph(d) is the largest L for which some configuration's centre follows the
clock of phase ph for times 0 .. d + L - 1 while its time-0 cells at depths d .. d + L - 1 are white. SAT at L
implies SAT at L - 1, so each record is found by descending from RR's value.
The suffix threshold e. At L = R_ph(d) + 1, e is the latest start t0 for which the clock samples t0 .. T alone still
forbid the run. It equals the earliest sample of RRX's earliest-first deletion core (GPT, GC549 checkpoint 5), and
here it is found by bisection: dropping earlier samples only makes the instance easier.
Control:
  RRP-C1: at each depth the larger of the two phase records equals RR's value: SAT with a simulated model at it in at
          least one phase, and UNSAT one longer in both. Confidence 0.9; a disagreement is a bug to find first.
PREDICTIONS (Cloud's, pushed before the first run):
  RRP-P1: the two phase records differ by at most 2 at every depth. Confidence 0.75. (At d = 21 .. 41 they differ
          by 1 or 2: 14/15, 10/11, 6/7, 6/8, 7/8, 8/7, CL038.)
  RRP-P2: phase 1's record is at least phase 0's at three or more of the five depths. Confidence 0.55.
UNEXPECTED CHECK (extends RRX-P1): e is at most 10 at every depth and phase, so ending a realizable run still needs
  the clock from its first beats while d grows to 81. At d = 21 .. 41, e was 4 to 7. Confidence 0.6.
Counterfactual: if e grows with d, beyond d / 4 say, the samples near the run's own entry suffice to end it, which
  would point to a local synchronization mechanism (the RRX counterfactual, at depth).
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_cloud_rr_replay as rr                          # noqa: E402
sys.argv = _argv

RR = {49: 11, 57: 11, 65: 11, 73: 10, 81: 12}
T0 = time.time()


def say(msg):
    print(f"{msg}  ({time.time() - T0:.0f} s)", flush=True)


def record(d, ph, start):
    """Largest SAT L for phase ph, descending from start; returns (R_ph, UNSAT at R_ph + 1 confirmed)."""
    L = start
    if rr.sat_checked(d, L, ph):
        return L, not rr.sat_checked(d, L + 1, ph)
    while L > 0 and not rr.sat_checked(d, L - 1, ph):
        L -= 1
    return L - 1, True


def threshold(d, L, ph):
    """Latest t0 such that the clock samples t0 .. T alone keep (d, L, ph) UNSAT."""
    cone, s, sel = rr.instance(d, L, ph, selectors=True)
    T = cone.T
    lo, hi = 0, T                       # UNSAT with all samples (t0 = 0); t0 = T + 1 (no samples) is SAT
    if s.solve(assumptions=[sel[t] for t in range(0, T + 1)]):
        return None
    while lo < hi:                      # invariant: UNSAT at lo
        mid = (lo + hi + 1) // 2
        if s.solve(assumptions=[sel[t] for t in range(mid, T + 1)]):
            hi = mid - 1
        else:
            lo = mid
    return lo


def main():
    depths = [int(x) for x in sys.argv[1].split(",")] if len(sys.argv) > 1 else sorted(RR)
    c1 = p1 = True
    p2 = 0
    small_e = True
    for d in depths:
        rec = {}
        for ph in (0, 1):
            rec[ph], confirmed = record(d, ph, RR[d])
            say(f"d = {d}, phase {ph}: R_ph = {rec[ph]} (UNSAT at {rec[ph] + 1}: {confirmed})")
            c1 &= confirmed
        c1 &= max(rec.values()) == RR[d]
        p1 &= abs(rec[0] - rec[1]) <= 2
        p2 += rec[1] >= rec[0]
        for ph in (0, 1):
            e = threshold(d, rec[ph] + 1, ph)
            small_e &= e is not None and e <= 10
            say(f"  d = {d}, phase {ph}: suffix threshold e = {e} at L = {rec[ph] + 1}")
    print("RRP-C1", "PASS" if c1 else "FAIL")
    print("RRP-P1", "HELD" if p1 else "REFUTED")
    print("RRP-P2", "HELD" if p2 >= 3 else "REFUTED", f"({p2} of {len(depths)})")
    print("unexpected check", "HELD" if small_e else "REFUTED")


if __name__ == "__main__":
    main()
