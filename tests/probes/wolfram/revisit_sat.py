#!/usr/bin/env python3
"""revisit_sat.py: certify the forced short revisits as every-trace local lemmas (SAT window encoding, LRAT-checked).
(Local, 2026-10-26, L969; FROZEN SPEC FOR GPT'S AGREEMENT, not yet run.)

RUN-ON:   cpu, one stage under tests/probes/wolfram/run_capped.py (proposed: --cpu 600 --wall 900 --rss-mib 1024 --file-mib 64 --disk-mib 256
          --launch-free-mib 2048 --min-free-mib 1024 --swap-growth-mib 256). It calls kissat (one solver process at a time, 60 s timeout
          each), drat-trim (DRAT -> LRAT) and the verified checker cake_lpr, sequentially; CNFs and proofs are written under the stage's
          fresh destination (the disk envelope covers them). No network, GPU or other concurrent compute.
CONTEXT:  L966 (the agreed revisit stage) found every observed q = 2 cell and every q = 3 / state-01 cell constant; GPT closed (E11, old 1, q 2)
          by hand (GC1908) with a two-copy argument, carried in L968; my (E01, old 0, q 2) branch is half closed (L968). The case trees grow
          one level per branch, so this spec certifies the forced cells mechanically, as GPT allowed after freezing "the actual constraints and
          exact coverage claim" (GC1908).
If this holds, it changes DQ-009: the short-revisit rules become every-trace lemmas with verified certificates; no prize/proof status.

ENCODING (exact). Window: relative columns d in [-5, 3] (the old read is at column 0) and relative levels t in [-4, 3] (the old top H0 is at 0).
Variables A[d][t], B[d][t]: the two copies' backgrounds (the twin traces); delta = A XOR B. For every (d, t) with d-1, d, d+1 and t, t+1 in
the window, both copies satisfy X[d+1][t] = X[d][t+1] XOR (X[d][t] OR X[d-1][t]) (the outward reconstruction). Case conditions:
  * Top(d) = h:  delta[d][t] = delta[d-1][t] = 0 for every window level t > h, and delta[d][h] OR delta[d-1][h] = 1.
  * the old read at column 0: Top(0) = 0, state (delta[0][0], delta[-1][0]) = the category (E11 = (1,1), E01 = (0,1), E10 = (1,0)),
    s_old = A[-1][1].
  * a drop pattern (k_1, ..., k_q), sum q, with no intermediate return to the index: Top(i) = -(k_1 + ... + k_i).
  * the current state at column q: (delta[q][-q], delta[q-1][-q]); s_new = A[q-1][-q+1] (leading index J again).
COVERAGE CLAIM. Every physical pair of reconstructions (two traces differing at one tock), at every column and height where these case
conditions hold, restricted to the window, is an accepted assignment: the recurrences hold everywhere, and the case conditions are facts
about it (only the within-window part of "zero above the top" is used, which is weaker). Hence an UNSAT result for (case AND s_new = NOT
expected) proves s_new = expected at every such instance, for EVERY trace. A SAT result proves nothing about physical realizability (the window
omits constraints); it is reported as "not certified", never as a counterexample.
Targets (the L966 constant cells): q = 2: (E01, 0) -> 0 and (E11, 1) -> 1, current state 11 or 01; q = 3 / state 01: (E01, 0) -> 1,
(E11, 0) -> 1, (E11, 1) -> 0, (E10, 0) -> 1, (E10, 1) -> 1; q = 3 / state 11: (E01, 0) -> 1, (E11, 0) -> 1. Valid drop patterns:
q = 2: (2, 0); q = 3: (3, 0, 0), (2, 1, 0), (0, 3, 0), (0, 1, 2), (0, 0, 3). A cell is certified when EVERY pattern's query is UNSAT (a pattern
whose case is itself UNSAT is vacuous and reported).
Record searched (2026-10-26): "SAT" and "drat" via PROBES.md (the 10-08..10-09 certificate line, cake_lpr pipeline); GC1908; no new search.

PREDICTIONS, written 2026-10-26 before any run.
Controls:
  K1  (positive) GPT's hand-proved (E11, old 1, q 2) cell is certified in both current states.
  K2  (consistency) every (cell, pattern) case WITHOUT the refuting assertion is SAT, or is reported as vacuous; at least one pattern per
      target cell is non-vacuous.
  K3  (negative) the L966 mixed cell (E11, old 1, q 3, current 11) is NOT certified (some pattern SAT with s_new = 0 and some with s_new = 1).
  K4  (mutant) with AND in place of OR in the recurrence, K1's queries change outcome (at least one becomes SAT).
  K5  every UNSAT is checked: kissat DRAT -> drat-trim LRAT -> cake_lpr prints "s VERIFIED UNSAT".
Blind:
  P1  every q = 2 target cell is certified (window as above).
  P2  every q = 3 / state 01 target cell is certified.
  P3  the two q = 3 / state 11 constant cells are certified.
  PU  (unexpected: how much history matters) shrinking the window to columns [-2, 3] loses the (E01, old 0, q 2) certificate (it needs
      columns d0 - 3 or earlier, as the hand case analysis in L968 did); K1 survives the shrink (GPT's proof used columns d - 2 .. d + 2).
"""
import itertools, os, subprocess, sys, time

KISSAT, DRAT_TRIM = "/opt/homebrew/bin/kissat", "/opt/homebrew/bin/drat-trim"
CAKE = os.path.expanduser("~/np-build/cake_lpr/cake_lpr")
OUT = os.environ.get("REVISIT_SAT_OUT", ".")

class CNF:
    def __init__(self): self.n = 0; self.cl = []
    def new(self): self.n += 1; return self.n
    def add(self, *lits): self.cl.append(list(lits))
    def xor(self, a, b):
        c = self.new(); self.add(-a, -b, -c); self.add(a, b, -c); self.add(a, -b, c); self.add(-a, b, c); return c
    def orr(self, a, b):
        c = self.new(); self.add(-a, c); self.add(-b, c); self.add(a, b, -c); return c
    def andd(self, a, b):
        c = self.new(); self.add(a, -c); self.add(b, -c); self.add(-a, -b, c); return c
    def eq(self, a, b): self.add(-a, b); self.add(a, -b)
    def dimacs(self): return f"p cnf {self.n} {len(self.cl)}\n" + "".join(" ".join(map(str, c)) + " 0\n" for c in self.cl)

def build(cat, s_old, pattern, cur, assert_new, D0=-5, D1=3, T0=-4, T1=3, mutant=False):
    f = CNF(); A, B = {}, {}
    for d in range(D0, D1 + 1):
        for t in range(T0, T1 + 1):
            A[d, t] = f.new(); B[d, t] = f.new()
    for X in (A, B):
        for d in range(D0 + 1, D1):
            for t in range(T0, T1):
                o = f.andd(X[d, t], X[d - 1, t]) if mutant else f.orr(X[d, t], X[d - 1, t])
                f.eq(X[d + 1, t], f.xor(X[d, t + 1], o))
    dl = {}
    def delta(d, t):
        if (d, t) not in dl: dl[d, t] = f.xor(A[d, t], B[d, t])
        return dl[d, t]
    def lit(v, val): return v if val else -v
    def top(d, h):
        for t in range(h + 1, T1 + 1):
            f.add(-delta(d, t)); f.add(-delta(d - 1, t))
        f.add(delta(d, h), delta(d - 1, h))
    st = {"E11": (1, 1), "E01": (0, 1), "E10": (1, 0)}[cat]
    top(0, 0); f.add(lit(delta(0, 0), st[0])); f.add(lit(delta(-1, 0), st[1]))
    f.add(lit(A[-1, 1], s_old))
    h = 0
    for i, k in enumerate(pattern, start=1):
        h -= k; top(i, h)
    q = len(pattern)
    cs = {"11": (1, 1), "01": (0, 1)}[cur]
    f.add(lit(delta(q, -q), cs[0])); f.add(lit(delta(q - 1, -q), cs[1]))
    if assert_new is not None: f.add(lit(A[q - 1, -q + 1], assert_new))
    return f

def solve(f, tag, certify):
    cnf = os.path.join(OUT, tag + ".cnf"); prf = os.path.join(OUT, tag + ".drat"); lrat = os.path.join(OUT, tag + ".lrat")
    open(cnf, "w").write(f.dimacs())
    r = subprocess.run([KISSAT, "-q", "--no-binary", cnf, prf], capture_output=True, text=True, timeout=60)
    res = "SAT" if r.returncode == 10 else "UNSAT" if r.returncode == 20 else f"UNKNOWN({r.returncode})"
    ver = None
    if res == "UNSAT" and certify:
        subprocess.run([DRAT_TRIM, cnf, prf, "-L", lrat], capture_output=True, text=True, timeout=120)
        c = subprocess.run([CAKE, cnf, lrat], capture_output=True, text=True, timeout=120)
        ver = "s VERIFIED UNSAT" in c.stdout
    for p in (prf, lrat):
        if os.path.exists(p): os.remove(p)
    return res, ver

PATTERNS = {2: [(2, 0)], 3: [(3, 0, 0), (2, 1, 0), (0, 3, 0), (0, 1, 2), (0, 0, 3)]}

def cell(cat, s_old, q, cur, expected, certify=True, **kw):
    out = []
    for pat in PATTERNS[q]:
        tag = f"{cat}_{s_old}_q{q}_{cur}_{''.join(map(str, pat))}" + ("_" + "_".join(f"{k}{v}" for k, v in kw.items()) if kw else "")
        cons, _ = solve(build(cat, s_old, pat, cur, None, **kw), tag + "_cons", False)
        if cons == "UNSAT": out.append((pat, "VACUOUS", None)); continue
        res, ver = solve(build(cat, s_old, pat, cur, 1 - expected, **kw), tag, certify)
        out.append((pat, res, ver))
    nonvac = [o for o in out if o[1] != "VACUOUS"]
    certified = bool(nonvac) and all(o[1] == "UNSAT" for o in nonvac)
    verified = all(o[2] for o in nonvac if o[1] == "UNSAT")
    return certified, verified, out

def main():
    t0 = time.time(); fails = 0
    targets = [("E01", 0, 2, "11", 0), ("E01", 0, 2, "01", 0), ("E11", 1, 2, "11", 1), ("E11", 1, 2, "01", 1),
               ("E01", 0, 3, "01", 1), ("E11", 0, 3, "01", 1), ("E11", 1, 3, "01", 0), ("E10", 0, 3, "01", 1), ("E10", 1, 3, "01", 1),
               ("E01", 0, 3, "11", 1), ("E11", 0, 3, "11", 1)]
    results = {}
    for tg in targets:
        c, v, out = cell(*tg); results[tg] = (c, v, out)
        print(f"CELL {tg}: certified {c}, all UNSATs verified {v}; " + "; ".join(f"{p}:{r}{'' if vv is None else ('/V' if vv else '/NOTV')}" for p, r, vv in out))
    k1 = results[("E11", 1, 2, "11", 1)][0] and results[("E11", 1, 2, "01", 1)][0]
    print("K1 GPT's E11/old1/q2 certified in both states:", "PASS" if k1 else "FAIL"); fails += not k1
    k2 = all(any(o[1] != "VACUOUS" for o in results[tg][2]) for tg in targets)
    print("K2 every target has a non-vacuous pattern:", "PASS" if k2 else "FAIL"); fails += not k2
    zs = [solve(build("E11", 1, pat, "11", val), f"neg_{''.join(map(str, pat))}_{val}", False)[0] for pat in PATTERNS[3] for val in (0, 1)]
    k3 = "SAT" in zs[0::2] and "SAT" in zs[1::2]
    print(f"K3 mixed cell (E11,1,3,11) not certified (s_new 0 and 1 both satisfiable in some pattern): {'PASS' if k3 else 'FAIL'} {zs}"); fails += not k3
    m = [solve(build("E11", 1, (2, 0), cur, 0, mutant=True), f"mut_{cur}", False)[0] for cur in ("11", "01")]
    k4 = "SAT" in m
    print(f"K4 AND-mutant changes K1: {'PASS' if k4 else 'FAIL'} {m}"); fails += not k4
    k5 = all(results[tg][1] for tg in targets if results[tg][0])
    print("K5 every certified cell's UNSATs verified by cake_lpr:", "PASS" if k5 else "FAIL"); fails += not k5
    p1 = all(results[tg][0] for tg in targets if tg[2] == 2)
    p2 = all(results[tg][0] for tg in targets if tg[2] == 3 and tg[3] == "01")
    p3 = all(results[tg][0] for tg in targets if tg[2] == 3 and tg[3] == "11")
    print(f"P1 q=2 cells certified: {'HELD' if p1 else 'FAILED'}; P2 q=3/01: {'HELD' if p2 else 'FAILED'}; P3 q=3/11 constants: {'HELD' if p3 else 'FAILED'}")
    sE = cell("E01", 0, 2, "11", 0, certify=False, D0=-2)[0] and cell("E01", 0, 2, "01", 0, certify=False, D0=-2)[0]
    sK = cell("E11", 1, 2, "11", 1, certify=False, D0=-2)[0] and cell("E11", 1, 2, "01", 1, certify=False, D0=-2)[0]
    print(f"PU shrink to columns [-2,3]: E01/0/q2 still certified {sE} (predicted False); K1 still certified {sK} (predicted True): "
          f"{'HELD' if (not sE and sK) else 'FAILED'}")
    print(f"ELAPSED {time.time() - t0:.1f} s; CONTROLS: {'ALL PASS' if fails == 0 else 'FAIL'} ({fails} failures)")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
