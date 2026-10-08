#!/usr/bin/env python3
"""rule30_cloud_relaxed_records.py: RRL, relaxed realizable records (row Q6), at GPT's request (CL040, GC549.18a).

RUN-ON:     cpu, python-sat (CaDiCaL 1.5.3)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_relaxed_records.py
COST:       minutes on one core.

GPT's GC549.16 reduces Q6 to the visible words of column 1. E(d, L) is feasible exactly when some visible word of
the actual right language has a zero band in its reconstructed initial left half, at depths d .. d + L - 1. GPT asked
whether the three reviewed forbidden words (11, 00000, 101001: GC499, GC502, GC504) already carry the obstruction.
This script asks it with SAT, in a model with no right half at all: the left half and centre, column 1 a free
sequence, the clock imposed at the centre through T = d + L - 1, and the initial white band. Then:
  free     column 1 unconstrained: the records over every column 1 (section 8.36's R(d));
  relax3   visible column 1 avoids 11, 00000 and 101001;
  relaxK   visible column 1 avoids every minimal forbidden word of the actual language up to length K = 10, computed
           here exactly (GC500: the words of length n come from initial right words of length 2n - 1);
  actual   the real right half, by RRX's encoding (rule30_cloud_rr_replay.py).
Visible symbols are column 1 at the clock's white times. Every value is reported per phase (phase p: the centre is
(t + p) mod 2), as GPT's guard asks. A record taken as a maximum over phases is never compared with one phase.
Each SAT model is checked by simulation. A relaxed constraint is necessary for the actual language at every white
start, so per phase actual <= relaxK <= relax3 <= free, and every UNSAT relaxed instance is a sufficient certificate
for the actual obstruction.

Depths: d = 3 .. 19 (ZR2's exact range), 21, 25, 29, 33, 37, 41 (L247's).
Controls:
  RRL-C1: the free records, maximized over the two phases, equal section 8.36's R(d) (RR's R_REC list) at every
          depth. Confidence 0.8 (the phase convention of those records is the risk).
  RRL-C2: per phase, actual <= relaxK <= relax3 <= free at every depth.
  RRL-C3 (GPT's case, GC549.18a): phase 0, d = 13, L = 5 is UNSAT under relax3; under no-11 alone the only visible
          words with the zero band are 010101001.
  RRL-C4: the actual per-phase records agree with CL038 at d = 21 .. 41 (14/15, 10/11, 6/7, 6/8, 7/8, 8/7).
PREDICTIONS (Cloud's, pushed before the first run):
  RRL-P1: at d = 13 the relax3 record is 4 in both phases, equal to the actual record. So the three words suffice
          there. Confidence 0.5.
  RRL-P2: the three words do not carry the obstruction in general. relax3 exceeds actual, same phase, at at least
          half of the 12 (depth, phase) cases with d in 21 .. 41, and its maximum over phases at d = 41 is at least 12.
          Confidence 0.55.
  RRL-P3: even relaxK with K = 10 exceeds actual, same phase, in at least one case with d in 21 .. 41. Confidence 0.5.
Counterfactual: if relax3 equals actual at every (depth, phase), a finite list of forbidden words already decides
  these records, and GC549's zero-band invariant has a finite target. If relaxK still lags far behind actual, the
  obstruction is not of finite type at these sizes.
"""
import os
import sys
import time

from pysat.solvers import Cadical153

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_cloud_rr_replay as rr                          # noqa: E402  (the actual records, per phase)
import rule30_cloud_visible_gaps as rv                       # noqa: E402  (the exact visible language)
sys.argv = _argv

R_REC = [1, 6, 5, 4, 3, 4, 3, 2, 9, 8, 7, 6, 17, 16, 15, 16, 15, 14, 15, 14, 17, 16, 19, 20, 19, 18, 17, 16, 19, 20,
         23, 24, 33, 32, 31, 30, 29, 32, 31, 38, 37, 36, 35, 34, 43, 42, 41, 40, 39, 44, 47, 46, 45, 44, 43, 42, 45, 46,
         51, 50, 49]                                         # section 8.36's R(d), d = 1 .., as in RR's source
DEPTHS = list(range(3, 20)) + [21, 25, 29, 33, 37, 41]
CL038 = {21: (14, 15), 25: (10, 11), 29: (6, 7), 33: (6, 8), 37: (7, 8), 41: (8, 7)}
THREE = ["11", "00000", "101001"]


def minimal_forbidden(K):
    """Minimal forbidden words of the actual visible language, lengths 2 .. K (GC500's exact finite count)."""
    lang = {}
    for n in range(1, K + 1):
        lang[n] = {rv.visible(w, n) for w in range(2 ** (2 * n - 1))}
    out = []
    for n in range(2, K + 1):
        for m in range(2 ** n):
            w = format(m, f"0{n}b")
            if w not in lang[n] and w[:-1] in lang[n - 1] and w[1:] in lang[n - 1]:
                out.append(w)
    return out, {n: len(lang[n]) for n in lang}


class Relaxed:
    """Left half and centre in the light cone of the centre up to T; column 1 a free sequence y(0 .. T - 1)."""

    def __init__(self, d, L, phase, forbidden):
        self.T = T = d + L - 1
        self.nv, self.var, cl = 0, {}, []
        for t in range(T):
            self.v(("y", t))
        for t in range(T):
            for i in range(-(T - t - 1), 1):                 # x(t + 1, i), i <= 0
                l, c = self.x(t, i - 1), self.x(t, i)
                r = self.v(("y", t)) if i == 0 else self.x(t, i + 1)
                y, o = self.x(t + 1, i), self.new()
                cl += [[-c, o], [-r, o], [c, r, -o]]
                cl += [[-y, l, o], [-y, -l, -o], [y, -l, o], [y, l, -o]]
        for t in range(T + 1):
            cl.append([self.x(t, 0)] if (t + phase) % 2 else [-self.x(t, 0)])
        for j in range(d, d + L):
            cl.append([-self.x(0, -j)])
        self.vis = [self.v(("y", t)) for t in range(T) if (t + phase) % 2 == 0]
        for w in forbidden:
            for s in range(len(self.vis) - len(w) + 1):
                cl.append([(-self.vis[s + k] if w[k] == "1" else self.vis[s + k]) for k in range(len(w))])
        self.s = Cadical153(bootstrap_with=cl)
        self.phase, self.d, self.L = phase, d, L

    def new(self):
        self.nv += 1
        return self.nv

    def v(self, key):
        if key not in self.var:
            self.var[key] = self.new()
        return self.var[key]

    def x(self, t, i):
        return self.v(("x", t, i))

    def solve_checked(self):
        if not self.s.solve():
            return False
        m = set(v for v in self.s.get_model() if v > 0)
        T = self.T
        y = [int(self.v(("y", t)) in m) for t in range(T)]
        row = {i: int(self.x(0, i) in m) for i in range(-T, 1)}
        for t in range(T + 1):                               # simulate the left half with column 1 = y
            if row[0] != (t + self.phase) % 2:
                raise RuntimeError(f"clock failed in simulation at t={t}")
            if t == T:
                break
            ext = dict(row)
            ext[1] = y[t]
            row = {i: ext.get(i - 1, 0) ^ (ext.get(i, 0) | ext.get(i + 1, 0)) for i in range(-(T - t - 1), 1)}
        if any(int(self.x(0, -j) in m) for j in range(self.d, self.d + self.L)):
            raise RuntimeError("white band failed")
        return True


def record(d, phase, forbidden, cap=80):
    L = 0
    while L < cap and Relaxed(d, L + 1, phase, forbidden).solve_checked():
        L += 1
    return L


def actual_record(d, phase, cap=80):
    L = 0
    while L < cap and rr.sat_checked(d, L + 1, phase):
        L += 1
    return L


def gpt_case():
    inst = Relaxed(13, 5, 0, THREE)
    unsat3 = not inst.s.solve()
    words = set()
    only11 = Relaxed(13, 5, 0, ["11"])
    while only11.s.solve():
        m = set(v for v in only11.s.get_model() if v > 0)
        w = "".join(str(int(v in m)) for v in only11.vis)
        words.add(w)
        only11.s.add_clause([(-v if v in m else v) for v in only11.vis])
    return unsat3, words


def main():
    t0 = time.time()
    forb, sizes = minimal_forbidden(10)
    print(f"actual visible language sizes C_n, n = 1 .. 10: {[sizes[n] for n in range(1, 11)]}")
    print(f"minimal forbidden words up to length 10: {len(forb)}; the shortest: {forb[:8]}  ({time.time()-t0:.0f} s)",
          flush=True)
    unsat3, words = gpt_case()
    print("RRL-C3", "PASS" if unsat3 and words == {"010101001"} else "FAIL", f"(relax3 UNSAT: {unsat3}; no-11 words "
          f"{sorted(words)})", flush=True)
    rows, c1, c2, c4 = {}, True, True, True
    for d in DEPTHS:
        rec = {}
        for ph in (0, 1):
            rec[ph] = (record(d, ph, []), record(d, ph, THREE), record(d, ph, forb), actual_record(d, ph))
            f, r3, rk, a = rec[ph]
            c2 &= a <= rk <= r3 <= f
        rows[d] = rec
        c1 &= max(rec[0][0], rec[1][0]) == R_REC[d - 1]
        if d in CL038:
            c4 &= (rec[0][3], rec[1][3]) == CL038[d]
        print(f"d = {d:2d}: phase 0 free/relax3/relax10/actual = {rec[0]}, phase 1 = {rec[1]}, "
              f"R(d) = {R_REC[d - 1]}  ({time.time() - t0:.0f} s)", flush=True)
    print("RRL-C1", "PASS" if c1 else "FAIL", "RRL-C2", "PASS" if c2 else "FAIL", "RRL-C4", "PASS" if c4 else "FAIL")
    p1 = rows[13][0][1] == 4 and rows[13][1][1] == 4
    deep = [(d, ph) for d in (21, 25, 29, 33, 37, 41) for ph in (0, 1)]
    over3 = sum(rows[d][ph][1] > rows[d][ph][3] for d, ph in deep)
    p2 = over3 >= 6 and max(rows[41][0][1], rows[41][1][1]) >= 12
    p3 = any(rows[d][ph][2] > rows[d][ph][3] for d, ph in deep)
    print("RRL-P1", "HELD" if p1 else "REFUTED", f"(relax3 at d = 13: {rows[13][0][1]} / {rows[13][1][1]})")
    print("RRL-P2", "HELD" if p2 else "REFUTED", f"(relax3 > actual in {over3} of 12 deep cases; at d = 41: "
          f"{rows[41][0][1]} / {rows[41][1][1]})")
    print("RRL-P3", "HELD" if p3 else "REFUTED", f"(relax10 > actual in "
          f"{sum(rows[d][ph][2] > rows[d][ph][3] for d, ph in deep)} of 12 deep cases)")


if __name__ == "__main__":
    main()
