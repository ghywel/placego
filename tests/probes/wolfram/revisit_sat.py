#!/usr/bin/env python3
"""revisit_sat.py: certify forced short revisits as every-trace local lemmas (SAT window encoding, LRAT-checked).
(Local, 2026-10-26, L969; revised L971 after GPT's GC1910 source review; FROZEN SPEC FOR GPT'S AGREEMENT, not yet run.)

STAGE (proposed): REVISIT_SAT_OUT=<dest> python3 tests/probes/wolfram/run_capped.py --out <dest> --cpu 900 --wall 900 --rss-mib 2048
          --file-mib 64 --disk-mib 256 --launch-free-mib 4096 --min-free-mib 1024 --swap-growth-mib 256 -- python3 tests/probes/wolfram/revisit_sat.py
  * (L974, after GC1911: one supervised group) REVISIT_SAT_OUT is REQUIRED and must resolve to the supervisor's exported CAPPED_OUT (the
    fresh destination; only the supervisor's out.txt / time_receipt.txt may be present); otherwise the driver refuses (exit 3).
  * Tools run as plain children of the driver, in the SAME process group as the driver and the supervisor's time process (no new sessions),
    so the supervisor's group RSS, pressure, disk and wall stops see them, and run_capped.py (L974) cleans that group on every terminal
    path, including a normal exit with leftovers (LEFTOVER_CLEANED). One tool at a time; each tool's files are capped at 1 MiB by
    RLIMIT_FSIZE set in the tool child (verified by getrlimit); streams go to retained files; parsing reads at most 64 KiB.
  * The driver polls every 0.5 s while a tool runs: a per-call wall timeout (kissat 60 s, drat-trim 120 s, cake_lpr 120 s) or a breach
    of the 600 s sampled aggregate CPU budget (all live members of the stage group by ps, plus reaped children by getrusage) kills the
    tool's process tree (TERM, 3 s, KILL) and ENDS the stage; after every tool, any other live member of the group ends the stage
    (LEFTOVER); a ps failure ends it (MONITOR_FAILURE); an unverified UNSAT ends it (UNVERIFIED). Every tool call is journalled at once
    in events.jsonl. Sampled, not exact: overshoot includes the polling interval, monitor latency and cleanup. CPU is checked before and after each tool; stop samples are recorded.
  * GC1912 amendment: unexpected solver exits (including file-limit failures) end the stage UNKNOWN; no later query is admitted.
  * DISK: before admitting each query the driver requires at most 256 MiB - 16 MiB under the destination; a query writes at most nine
    files (the CNF by the driver; DRAT, LRAT and six stdout/stderr files by tools, each at most 1 MiB), so the 16 MiB reservation is real.
    A proof larger than 1 MiB stops the stage unverified, with its artifacts retained.
  * Tool identity, recorded in the receipt: kissat 4.0.4 (binary sha256 ef5bf56e...), drat-trim (sha256 86a8209e...), the cake_lpr wrapper
    (sha256 70be2e42...: three lines, `exec /usr/bin/lockf -k ~/np-scratch-int/cake_lpr.lock <dir>/cake_lpr.bin "$@"`, one check at a time)
    and cake_lpr.bin (sha256 d23c413b...). Harmless instrument control (L971): a trivial UNSAT CNF gave kissat rc 20, drat-trim rc 0 and
    "s VERIFIED", cake_lpr rc 0 and "s VERIFIED UNSAT", maximum RSS 2,113,536 bytes by time -l: the "~8 GB" is a virtual reservation, not
    resident (measured on a tiny proof only; a larger proof could need more, and the 2048 MiB group stop would then end the stage, unverified).
CONTEXT:  L966 constant cells; GC1909 two-step theorem (carried L970) makes the q = 2 cells controls; the q = 3 cells are the targets.
If this holds, it changes DQ-009: the three-step rules become every-trace lemmas with verified certificates; no prize/proof status.

ENCODING. Coordinates relative to the old read: column d (old read at d = 0, absolute d0) and level t (old top at t = 0, absolute H0). Variables
A[d][t], B[d][t] (the two copies' backgrounds), delta = A XOR B. Recurrence X[d+1][t] = X[d][t+1] XOR (X[d][t] OR X[d-1][t]) for both copies
wherever all four cells are in the window. Case: Top(d) = h means delta[d][t] = delta[d-1][t] = 0 for window levels t > h and
delta[d][h] OR delta[d-1][h] = 1; old read: Top(0) = 0, state (delta[0][0], delta[-1][0]) = category, s_old = A[-1][1]; drop pattern
(k_1..k_q): Top(i) = -(k_1 + .. + k_i); current state (delta[q][-q], delta[q-1][-q]); s_new = A[q-1][-q+1].
PROFILES (GC1910's option 2: clamp to the physical boundary). Column profile p_d in {2, 3, 4, >=5}: d0 = p_d gives the lowest window column
D0 = -d0 (absolute column 0, the zero wall: A = B = 0 there, imposed), or D0 = -5 for d0 >= 5 (interior, no wall). Level profile p_h in
{q, .., 3, >=4}: H0 = p_h gives the lowest window level T0 = -H0 (absolute time 0; nothing below is needed by the recurrence), or T0 = -4 for
H0 >= 4. Top of window: columns D1 = q (the reread column is live), levels T1 = 3. Every window cell is then a real reconstruction cell for
every instance in its profile, and only true facts are imposed, so each physical instance restricts to an accepted assignment of its profile.
PATTERNS (GC1910): q = 2: (2, 0), (0, 2); q = 3: (3, 0, 0), (2, 1, 0), (0, 3, 0), (0, 1, 2), (0, 0, 3).
BRANCH = (cell, profile, pattern). Each branch runs two queries: CONS (the case without the reread assertion) and REF (the case with
s_new = NOT expected). Outcomes of a query: SAT, UNSAT_VERIFIED (kissat rc 20, drat-trim rc 0 with a line "s VERIFIED", cake_lpr rc 0 with a
line exactly "s VERIFIED UNSAT"), UNSAT_UNVERIFIED, UNKNOWN (timeout or other rc). A branch is COVERED iff CONS is UNSAT_VERIFIED (vacuous
with a checked proof) or REF is UNSAT_VERIFIED (implication with a checked proof). A cell is CERTIFIED iff every one of its branches is
covered; NON-VACUOUS iff some branch has CONS = SAT. Every UNSAT is sent to verification; any UNSAT_UNVERIFIED anywhere is a stage failure
(K5). UNKNOWN is never promoted. Retained per query: the CNF, DRAT, LRAT, each tool's stdout/stderr/rc, and sha256 of CNF and LRAT, in
results.jsonl inside the destination. COVERAGE CLAIM: a certified cell's reread equals the expected value at every instance meeting its case
conditions, for every trace (all profiles together cover d0 >= 2 and H0 >= q). An uncertified cell is "not certified", never refuted.
Record searched: as L969 (PROBES.md certificate line; GC1908, GC1909, GC1910); no new search.

PREDICTIONS (L969, kept; revised before any run where marked).
Controls:
  K1  (revised: patterns completed) both GC1909 q = 2 cells, (E01, 0) -> 0 and (E11, 1) -> 1, in both current states, are CERTIFIED.
  K2  (revised) every target cell is NON-VACUOUS (some branch with CONS = SAT).
  K3  the mixed cell (E11, 1, 3, 11): in the interior profile (d0 >= 5, H0 >= 4) both s_new values are SAT for some pattern (not certified).
  K4  the AND-mutant (AND in place of OR) breaks K1 in the interior profile (some REF query SAT).
  K5  no UNSAT_UNVERIFIED anywhere; every tool call ended with a recorded return code; no process group left behind.
Blind (from L969):
  P1  (now a control by GC1909; kept as written) every q = 2 cell certified.
  P2  every q = 3 / state 01 target cell certified.
  P3  the two q = 3 / state 11 constant cells certified.
  PU  (L969's shrink prediction is stale after GC1909 and is kept only as the original text; revised role, before execution:) report, for
      each certified q = 3 cell, whether it is already certified in the tightest column profile d0 = 2 (the wall-adjacent case), as a
      descriptive check of how much history the rule needs.
"""
import json, os, resource, signal, subprocess, sys, time, hashlib

KISSAT, DRAT_TRIM = "/opt/homebrew/bin/kissat", "/opt/homebrew/bin/drat-trim"
CAKE = os.path.expanduser("~/np-build/cake_lpr/cake_lpr")
TOOLS = [KISSAT, DRAT_TRIM, CAKE, CAKE + ".bin"]
CPU_BUDGET, DISK_CAP, ALLOW, FILE_CAP = 600.0, 256 << 20, 16 << 20, 1 << 20
OUT = os.environ.get("REVISIT_SAT_OUT")
STATE = {"fail": [], "n": 0}

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()

def dir_bytes(d):
    return sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(d) for f in fs)

def ps_rows():
    r = subprocess.run(["ps", "-A", "-o", "pid=,ppid=,pgid=,time=,stat=,command="], capture_output=True, text=True, timeout=5)
    if r.returncode != 0 or not r.stdout.strip(): raise SystemExit("MONITOR_FAILURE")
    rows = []
    for line in r.stdout.splitlines():
        f = line.split(None, 5)
        if len(f) < 5: raise SystemExit("MONITOR_FAILURE")
        rows.append((int(f[0]), int(f[1]), int(f[2]), f[3], f[4], f[5] if len(f) > 5 else ""))
    return rows

def cputime_s(t):
    parts = t.replace("-", ":").split(":")          # [[dd-]hh:]mm:ss.ss
    v = 0.0
    for x in parts: v = v * 60 + float(x)
    return v

def cpu_total():
    """sampled aggregate CPU: every live process of this stage group (driver, the time process, live tools) plus reaped children."""
    me = os.getpgrp(); live = sum(cputime_s(r[3]) for r in ps_rows() if r[2] == me and not r[4].startswith("Z"))
    b = resource.getrusage(resource.RUSAGE_CHILDREN)
    return live + b.ru_utime + b.ru_stime

def strangers():
    """live members of the stage group other than this driver, its parent (the time process) and ps itself."""
    me, mine, par = os.getpgrp(), os.getpid(), os.getppid()
    return [r for r in ps_rows() if r[2] == me and r[0] not in (mine, par) and not r[4].startswith("Z") and not r[5].startswith("ps ")]

def kill_tree(pid):
    rows = ps_rows(); kids = {pid}; grew = True
    while grew:
        grew = False
        for r in rows:
            if r[1] in kids and r[0] not in kids: kids.add(r[0]); grew = True
    for k in kids:
        try: os.kill(k, signal.SIGTERM)
        except ProcessLookupError: pass
    time.sleep(3)
    for k in kids:
        try: os.kill(k, signal.SIGKILL)
        except ProcessLookupError: pass

def journal(rec):
    with open(os.path.join(OUT, "events.jsonl"), "a") as fh: fh.write(json.dumps(rec) + "\n"); fh.flush()

def tool_preexec():
    resource.setrlimit(resource.RLIMIT_FSIZE, (FILE_CAP, FILE_CAP))
    if resource.getrlimit(resource.RLIMIT_FSIZE) != (FILE_CAP, FILE_CAP): os._exit(97)

def run_tool(argv, stem, timeout):
    """one tool, in THIS stage's process group (no new session), 1 MiB per written file, streams to files; polled every 0.5 s for
    wall timeout and the sampled aggregate CPU budget; a timeout, budget breach or leftover descendant ends the stage."""
    so, se = stem + ".stdout", stem + ".stderr"
    before = cpu_total()
    if before > CPU_BUDGET:
        journal({"tool": os.path.basename(stem), "stop": "CPU_BUDGET", "rc": None, "cpu_sample_s": before})
        raise SystemExit("CPU_BUDGET")
    t0 = time.time()
    with open(so, "w") as fo, open(se, "w") as fe:
        p = subprocess.Popen(argv, stdout=fo, stderr=fe, preexec_fn=tool_preexec)
        stop = None
        while p.poll() is None:
            time.sleep(0.5)
            sampled = cpu_total()
            if time.time() - t0 > timeout: stop = "TOOL_TIMEOUT"
            elif sampled > CPU_BUDGET: stop = "CPU_BUDGET"
            if stop:
                kill_tree(p.pid); p.wait(timeout=10)
                journal({"tool": os.path.basename(stem), "stop": stop, "rc": p.returncode, "cpu_sample_s": sampled}); raise SystemExit(stop)
    rc = p.returncode
    left = strangers()
    after = cpu_total()
    journal({"tool": os.path.basename(stem), "rc": rc, "wall_s": round(time.time() - t0, 3), "leftover": len(left), "cpu_sample_s": after})
    if left: raise SystemExit("LEFTOVER")
    if after > CPU_BUDGET: raise SystemExit("CPU_BUDGET")
    with open(so) as f: head = f.read(65536)
    return rc, head

class CNF:
    def __init__(self): self.n = 0; self.cl = []
    def new(self): self.n += 1; return self.n
    def add(self, *l): self.cl.append(list(l))
    def xor(self, a, b):
        c = self.new(); self.add(-a, -b, -c); self.add(a, b, -c); self.add(a, -b, c); self.add(-a, b, c); return c
    def orr(self, a, b):
        c = self.new(); self.add(-a, c); self.add(-b, c); self.add(a, b, -c); return c
    def andd(self, a, b):
        c = self.new(); self.add(a, -c); self.add(b, -c); self.add(-a, -b, c); return c
    def eq(self, a, b): self.add(-a, b); self.add(a, -b)
    def text(self): return f"p cnf {self.n} {len(self.cl)}\n" + "".join(" ".join(map(str, c)) + " 0\n" for c in self.cl)

def build(cat, s_old, pattern, cur, assert_new, pd, ph, mutant=False):
    q = len(pattern)
    D0 = -pd if pd != ">=5" else -5
    T0 = -ph if ph != ">=4" else -4
    D1, T1 = q, 3
    f = CNF(); A, B = {}, {}
    for d in range(D0, D1 + 1):
        for t in range(T0, T1 + 1): A[d, t] = f.new(); B[d, t] = f.new()
    if pd != ">=5":
        for t in range(T0, T1 + 1): f.add(-A[D0, t]); f.add(-B[D0, t])        # absolute column 0: the zero wall
    for X in (A, B):
        for d in range(D0 + 1, D1):
            for t in range(T0, T1):
                o = f.andd(X[d, t], X[d - 1, t]) if mutant else f.orr(X[d, t], X[d - 1, t])
                f.eq(X[d + 1, t], f.xor(X[d, t + 1], o))
    dl = {}
    def delta(d, t):
        if (d, t) not in dl: dl[d, t] = f.xor(A[d, t], B[d, t])
        return dl[d, t]
    lit = lambda v, val: v if val else -v
    def top(d, h):
        for t in range(h + 1, T1 + 1): f.add(-delta(d, t)); f.add(-delta(d - 1, t))
        f.add(delta(d, h), delta(d - 1, h))
    st = {"E11": (1, 1), "E01": (0, 1), "E10": (1, 0)}[cat]
    top(0, 0); f.add(lit(delta(0, 0), st[0])); f.add(lit(delta(-1, 0), st[1])); f.add(lit(A[-1, 1], s_old))
    h = 0
    for i, k in enumerate(pattern, start=1): h -= k; top(i, h)
    cs = {"11": (1, 1), "01": (0, 1)}[cur]
    f.add(lit(delta(q, -q), cs[0])); f.add(lit(delta(q - 1, -q), cs[1]))
    if assert_new is not None: f.add(lit(A[q - 1, -q + 1], assert_new))
    return f

def query(f, tag):
    if cpu_total() > CPU_BUDGET: raise SystemExit("CPU_BUDGET")
    if dir_bytes(OUT) > DISK_CAP - ALLOW: raise SystemExit("DISK_BUDGET")
    STATE["n"] += 1
    stem = os.path.join(OUT, tag); cnf = stem + ".cnf"; drat = stem + ".drat"; lrat = stem + ".lrat"
    with open(cnf, "w") as fh: fh.write(f.text())
    rec = {"tag": tag, "cnf_sha256": sha(cnf)}
    rc, _ = run_tool([KISSAT, "-q", "--no-binary", cnf, drat], stem + ".kissat", 60); rec["kissat_rc"] = rc
    if rc == 10: res = "SAT"
    elif rc == 20:
        drc, dout = run_tool([DRAT_TRIM, cnf, drat, "-L", lrat], stem + ".dratrim", 120); rec["drat_trim_rc"] = drc
        dok = drc == 0 and any(l.strip() == "s VERIFIED" for l in dout.splitlines())
        ok = False
        if dok and os.path.exists(lrat):
            rec["lrat_sha256"] = sha(lrat)
            crc, cout = run_tool([CAKE, cnf, lrat], stem + ".cake", 120); rec["cake_rc"] = crc
            ok = crc == 0 and any(l.strip() == "s VERIFIED UNSAT" for l in cout.splitlines())
        res = "UNSAT_VERIFIED" if ok else "UNSAT_UNVERIFIED"
        if not ok:
            STATE["fail"].append(f"unverified UNSAT {tag}")
            rec["result"] = res
            with open(os.path.join(OUT, "results.jsonl"), "a") as fh: fh.write(json.dumps(rec) + "\n")
            raise SystemExit("UNVERIFIED")
    else:
        rec["result"] = "UNKNOWN"
        with open(os.path.join(OUT, "results.jsonl"), "a") as fh: fh.write(json.dumps(rec) + "\n")
        raise SystemExit("SOLVER_FAILURE")
    rec["result"] = res
    with open(os.path.join(OUT, "results.jsonl"), "a") as fh: fh.write(json.dumps(rec) + "\n")
    return res

PATTERNS = {2: [(2, 0), (0, 2)], 3: [(3, 0, 0), (2, 1, 0), (0, 3, 0), (0, 1, 2), (0, 0, 3)]}
def profiles(q): return [(pd, ph) for pd in (2, 3, 4, ">=5") for ph in list(range(q, 4)) + [">=4"]]

def cell(cat, s_old, q, cur, expected):
    branches = []
    for pd, ph in profiles(q):
        for pat in PATTERNS[q]:
            tag = f"{cat}_{s_old}_q{q}_{cur}_d{pd}_h{ph}_{''.join(map(str, pat))}".replace(">=", "ge")
            cons = query(build(cat, s_old, pat, cur, None, pd, ph), tag + "_cons")
            ref = "SKIPPED_VACUOUS" if cons == "UNSAT_VERIFIED" else query(build(cat, s_old, pat, cur, 1 - expected, pd, ph), tag + "_ref")
            covered = cons == "UNSAT_VERIFIED" or ref == "UNSAT_VERIFIED"
            branches.append({"profile": (pd, ph), "pattern": pat, "cons": cons, "ref": ref, "covered": covered})
    return {"certified": all(b["covered"] for b in branches), "nonvacuous": any(b["cons"] == "SAT" for b in branches),
            "d2_certified": all(b["covered"] for b in branches if b["profile"][0] == 2), "branches": branches}

def main():
    if not OUT or not os.path.isdir(OUT): print("REFUSED: REVISIT_SAT_OUT must name the existing fresh destination"); return 3
    if os.path.realpath(OUT) != os.environ.get("CAPPED_OUT"): print("REFUSED: REVISIT_SAT_OUT is not the supervisor destination CAPPED_OUT"); return 3
    extra = set(os.listdir(OUT)) - {"out.txt", "time_receipt.txt"}
    if extra: print(f"REFUSED: destination not fresh: {sorted(extra)}"); return 3
    t0 = time.time()
    with open(os.path.join(OUT, "tools.json"), "w") as fh:
        json.dump({p.replace(os.path.expanduser("~"), "~"): sha(p) for p in TOOLS}, fh, indent=1)
    targets = [("E01", 0, 2, "11", 0), ("E01", 0, 2, "01", 0), ("E11", 1, 2, "11", 1), ("E11", 1, 2, "01", 1),
               ("E01", 0, 3, "01", 1), ("E11", 0, 3, "01", 1), ("E11", 1, 3, "01", 0), ("E10", 0, 3, "01", 1), ("E10", 1, 3, "01", 1),
               ("E01", 0, 3, "11", 1), ("E11", 0, 3, "11", 1)]
    R = {}
    try:
        for tg in targets:
            R[tg] = cell(*tg)
            b = R[tg]["branches"]
            print(f"CELL {tg}: certified {R[tg]['certified']}, non-vacuous {R[tg]['nonvacuous']}, d0=2 profile certified {R[tg]['d2_certified']}; "
                  f"branches {len(b)}: covered {sum(x['covered'] for x in b)}, vacuous {sum(x['cons'] == 'UNSAT_VERIFIED' for x in b)}, "
                  f"REF SAT {sum(x['ref'] == 'SAT' for x in b)}, UNKNOWN {sum('UNKNOWN' in (x['cons'], x['ref']) for x in b)}")
        k3 = [query(build("E11", 1, pat, "11", v, ">=5", ">=4"), f"K3_{''.join(map(str, pat))}_{v}") for pat in PATTERNS[3] for v in (0, 1)]
        k4 = [query(build("E11", 1, (0, 2), cur, 0, ">=5", ">=4", mutant=True), f"K4_{cur}") for cur in ("11", "01")]
    except SystemExit as e:
        print(f"STOPPED: {e}"); STATE["fail"].append(str(e)); k3 = k4 = []
        journal({"stage_stop": str(e)})
    q2 = [tg for tg in targets if tg[2] == 2]
    k1 = all(R.get(tg, {}).get("certified") for tg in q2)
    k2 = all(R.get(tg, {}).get("nonvacuous") for tg in targets)
    k3ok = bool(k3) and "SAT" in k3[0::2] and "SAT" in k3[1::2]
    k4ok = "SAT" in k4
    k5 = not STATE["fail"]
    print(f"K1 GC1909 q=2 cells certified: {'PASS' if k1 else 'FAIL'}")
    print(f"K2 every target non-vacuous: {'PASS' if k2 else 'FAIL'}")
    print(f"K3 mixed cell not certified in the interior profile: {'PASS' if k3ok else 'FAIL'} {k3}")
    print(f"K4 AND-mutant breaks K1 (interior): {'PASS' if k4ok else 'FAIL'} {k4}")
    print(f"K5 no unverified UNSAT, no leftover group, no budget stop: {'PASS' if k5 else 'FAIL'} {STATE['fail'][:5]}")
    for name, sel in (("P1 q=2", lambda tg: tg[2] == 2), ("P2 q=3/01", lambda tg: tg[2] == 3 and tg[3] == "01"),
                      ("P3 q=3/11 constants", lambda tg: tg[2] == 3 and tg[3] == "11")):
        cs = [tg for tg in targets if sel(tg)]
        print(f"{name}: {'HELD' if all(R.get(tg, {}).get('certified') for tg in cs) else 'FAILED'} "
              f"({sum(bool(R.get(tg, {}).get('certified')) for tg in cs)}/{len(cs)} certified)")
    print("PU d0=2 profile certified, q=3 cells:", {tg: R[tg]["d2_certified"] for tg in targets if tg[2] == 3 and tg in R})
    print(f"QUERIES {STATE['n']}; CPU (sampled aggregate) {cpu_total():.1f} s; ELAPSED {time.time() - t0:.1f} s; DEST BYTES {dir_bytes(OUT)}")
    fails = (not k1) + (not k2) + (not k3ok) + (not k4ok) + (not k5)
    print(f"CONTROLS: {'ALL PASS' if fails == 0 else 'FAIL'} ({fails} failures)")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
