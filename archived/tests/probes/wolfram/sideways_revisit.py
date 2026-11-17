#!/usr/bin/env python3
"""sideways_revisit.py: what does a backward visit remember from the earlier read of the same trace index?
(Local, 2026-10-26, L961; revised L962 after GPT's GC1903; FROZEN SPEC FOR GPT'S AGREEMENT, not yet run.)

RUN-ON:   cpu, pure Python 3, one process.  python3 sideways_revisit.py > out.txt
LIMITS (L962): launched only by tests/probes/wolfram/run_capped.py --cpu 300 --wall 600 --rss-mib 512 --file-mib 1 --disk-mib 10
          --launch-free-mib 2048 --min-free-mib 1024 --swap-growth-mib 256, into a fresh directory; one CPU worker, no threads, network or
          GPU; nothing concurrent. Receipts (out.txt, time_receipt.txt, launcher.json) stored under cited/sideways-revisit-<date>/, read back.
CONTEXT:  L960 (sideways_fresh.py): backward visits (old index, not the one-level-drop repeat) in state 11 have P(s=1) = 0.7075; in 01, 0.4999.
          GC1901 (GPT): for two visits to the same leading index J separated by q columns, with the OLD visit at (r, t) = (d0 - 1, H_d0 + 1),
              s_new XOR s_old = XOR_(i=0..q-1) [ c_(r+i)(t-i-1) OR c_(r+i-1)(t-i-1) ],
          each term using trace indices <= J - 1 (the common leading bit cancels). Local's check of the identity is in L961.
If this holds, it changes DQ-009: whether a small remembered state explains the one measured deviation from fair input; no prize/proof status.

DEFINITIONS. For a decision at column d >= 2 in top state 11 or 01 whose input s = c_(d-1)(H_d + 1) has leading index J = H_d + d - 1 that is
OLD (J <= R_(d-1)) and is not the one-level-drop repeat (the L6 class R1 of sideways_fresh.py), find the most recent earlier column d0 < d at
which the top's input had the same leading index J (H_d0 + d0 - 1 = J). Earlier-read category E:
  E11 / E01: that earlier column was a decision in state 11 / 01 (its s is recorded);  E10: the top was in state 10 there (s read, no decision);
  ENONE: no earlier top input had index J (J was exposed only in the initial prefix a_0..a_tau or as a background index).
X = s_new XOR s_old (the GC1901 correction) where an earlier read exists; q = d - d0.
Proposed small memory M = (E, s_old, q capped at 4, current state). Record searched: GC1901's identity and sources; L960's searches; no new search.

PREDICTIONS, written 2026-10-26 before any run.
Controls (must hold):
  V0  the GC1901 identity: for every OB decision with an earlier read, X computed from the q OR terms equals s_new XOR s_old (exact).
  V0' (GC1903) V0 needs a positive number of identity comparisons; zero comparisons is UNTESTED, not PASS.
  V1  replicate (not replay: a fresh seed 20261026 + 961, same taus {101, 201} and run counts 300, 200) L960's OB cells within 0.02
      (P(s=1 | OB, 11) about 0.71, (OB, 01) about 0.50).
  V2  every OB decision has an old index (J <= R_(d-1)) and backlog R_(d-1) - J >= 0; the groups B = 0 (catch-up) and B >= 1 partition the
      OB decisions exactly (asserted, in the exit status).
Blind:
  P1  most OB decisions in state 11 have an earlier read in state 11 or 10 (E11 + E10 >= 0.7 of them), and P(s_new = 1 | OB, 11) is carried by
      X = 1 after s_old = 0: P(X = 1 | E11, s_old = 0, current 11) >= 0.8.
  P2  (kill test of M, approximate) some M cell with >= 50 decisions has 0.1 < P(s_new = 1 | M) < 0.9.
  EXACT (GC1903): M is exactly consistent on this sample iff EVERY nonempty cell has k = 0 or k = n; any 0 < k < n is an exact conflict and
      refutes deterministic closure on M; the first conflicting pair's descriptors (run, tau, columns, indices) are printed. No conflict is
      still not a theorem. Integer n and k are printed for every cell.
  P3  the plug-in conditional entropy H(s_new | M), weighted over OB decisions, is at most 0.6 bits; reported beside the same-table baseline
      H(s_new | current state) and their difference. Descriptive and in-sample (possibly biased low in sparse cells), not causal.
  CF  if H(s_new | M) >= 0.9 bits, the earlier read as coded in M carries little; this does not prove all earlier history irrelevant.
  PU  (unexpected) ENONE decisions: P(s = 1 | ENONE) within [0.4, 0.6]; if there are none, UNTESTED with the count.
OUTCOME, 2026-10-26 (the ONE stage agreed in GC1906, launched 12:12:38Z under run_capped.py sha256 a45685c2..., exit COMPLETED rc 0;
child 0.44 s real, 12,795,904 bytes max RSS by the time receipt; sampled RSS 0, too short for a sample; source sha256 9d28c3d2... frozen;
receipts out.txt 2a5d969d..., time_receipt.txt cfd1397e..., launcher.json f325fd7f..., cited/sideways-revisit-20261026/). Added after the run.
  Censored 0. V0 PASS (16,940 identity comparisons). V1 PASS (OB 11: 0.7110, n 9,162; OB 01: 0.5084, n 7,778). V2 PASS (B+ 11,393 + B0 5,547
  = 16,940). P1 FAILED (E11 + E10 share 0.5845; P(X=1 | E11, s_old=0, 11) = 497/650 = 0.7646). P2 approximate HELD. EXACT: 15 of 26 nonempty
  cells conflict, so deterministic closure on M is REFUTED (first pair in cell (E01, 0, 4, 11)). But every q = 2 cell, and every q = 3 cell in
  state 01, is exactly 0 or 1; the conflicts are q = 3 in state 11 (three cells) and q >= 4. P3 HELD: H(s_new | M) = 0.3453 bits against the
  state-only baseline 0.9282 (descriptive). PU UNTESTED: 0 ENONE decisions.
"""
import random, statistics, sys, math

def trace(rng, L):
    a = 0
    for t in range(0, L, 2): a |= 1 << t
    for t in range(1, L, 2):
        if rng.getrandbits(1): a |= 1 << t
    return a

def run(rng, tau, acc, runid):
    cap = 14 * tau + 400; L = tau + cap + 8
    a = trace(rng, L); b = a ^ (1 << tau); mask = (1 << (tau + 2)) - 1
    colsA = [0, a]                     # background columns c_0, c_1, ... kept for the OR-term identity
    pm1, p = 0, b
    dm1, dc = 0, (a ^ b) & mask
    R, Hprev, Jprev = tau, tau, tau
    lastread = {}                      # J -> (d0, category, s_old)
    H = tau
    for d in range(1, cap):
        c, cm1 = colsA[d], colsA[d - 1]
        un = dc | dm1
        if un == 0: return d
        Hn = un.bit_length() - 1
        if d >= 2:
            K = Hprev - Hn; J = Hn + d - 1; new = J > R
            H = Hn
            al, be = (dc >> H) & 1, (dm1 >> H) & 1
            s = (cm1 >> (H + 1)) & 1
            st = f"{al}{be}"
            if st != "10" and not new and not (K == 1 and J == Jprev):
                Bk = R - J
                if not (J <= R and Bk >= 0): acc["v2ok"] = False
                acc["v2"]["B0" if Bk == 0 else "B+"] = acc["v2"].get("B0" if Bk == 0 else "B+", 0) + 1
                if J in lastread:
                    d0, E, so = lastread[J]; q = d - d0
                    r, t = d0 - 1, J - d0 + 2                  # old visit at column d0 >= 2: r = d0 - 1 >= 1, t = H_d0 + 1
                    X = 0
                    for i in range(q):
                        X ^= ((colsA[r + i] >> (t - i - 1)) & 1) | ((colsA[r + i - 1] >> (t - i - 1)) & 1)
                    acc["v0n"] += 1
                    if X != (s ^ so): acc["v0"] = False
                    key = (E, so, min(q, 4), st)
                else:
                    E, so, X, key = "ENONE", None, None, ("ENONE", None, None, st)
                acc["cells"].setdefault(key, [0, 0]); acc["cells"][key][0] += 1; acc["cells"][key][1] += s
                desc = (runid, tau, d, J, s)
                fw = acc["firstwit"].setdefault(key, {})
                fw.setdefault(s, desc)
                if acc["conflict"] is None and 0 in fw and 1 in fw: acc["conflict"] = (key, fw[0], fw[1])
                acc["st"].setdefault(st, [0, 0]); acc["st"][st][0] += 1; acc["st"][st][1] += s
                acc["ob"].setdefault(st, [0, 0]); acc["ob"][st][0] += 1; acc["ob"][st][1] += s
                acc["E"].setdefault((st, E), 0); acc["E"][(st, E)] += 1
                if E == "E11" and so == 0 and st == "11":
                    acc["p1x"][0] += 1; acc["p1x"][1] += X
            cat = "E10" if st == "10" else ("E11" if st == "11" else "E01")
            lastread[J] = (d, cat, s)
            R = max(R, J); Jprev = J
        Hprev = Hn
        cn = (c >> 1) ^ (c | cm1); pn = (p >> 1) ^ (p | pm1); dn = (cn ^ pn) & mask
        colsA.append(cn)
        pm1, p, dm1, dc = p, pn, dc, dn
    return None

def main():
    rng = random.Random(20261026 + 961)
    fails = 0
    acc = {"cells": {}, "ob": {}, "E": {}, "v0": True, "v0n": 0, "v2": {}, "v2ok": True, "p1x": [0, 0], "firstwit": {}, "conflict": None, "st": {}}
    runid = 0; cens = 0
    for tau, N in ((101, 300), (201, 200)):
        for _ in range(N):
            runid += 1
            if run(rng, tau, acc, runid) is None: cens += 1
    print(f"CENSORED runs: {cens}"); fails += cens > 0
    v0 = acc["v0"] and acc["v0n"] > 0
    print(f"V0 GC1901 identity: {acc['v0n']} comparisons, {'PASS' if v0 else ('UNTESTED' if acc['v0n'] == 0 else 'FAIL')}"); fails += not v0
    p11 = acc["ob"]["11"][1] / acc["ob"]["11"][0]; p01 = acc["ob"]["01"][1] / acc["ob"]["01"][0]
    v1 = abs(p11 - 0.7075) <= 0.02 and abs(p01 - 0.4999) <= 0.02
    print(f"V1 OB P(s=1): 11 {p11:.4f} (n {acc['ob']['11'][0]}), 01 {p01:.4f} (n {acc['ob']['01'][0]}): {'PASS' if v1 else 'FAIL'}"); fails += not v1
    nob = sum(v[0] for v in acc["ob"].values())
    v2 = acc["v2ok"] and sum(acc["v2"].values()) == nob
    print(f"V2 OB partition {acc['v2']} sums to {sum(acc['v2'].values())} of {nob}; old index and B >= 0 everywhere: {'PASS' if v2 else 'FAIL'}"); fails += not v2
    n11 = acc["ob"]["11"][0]
    e = {E: acc["E"].get(("11", E), 0) / n11 for E in ("E11", "E10", "E01", "ENONE")}
    ecount = {k: acc["E"].get(("11", k), 0) for k in e}
    print("P1 OB-11 earlier-read counts:", ecount)
    if acc["p1x"][0] == 0:
        print("P1 UNTESTED: no (E11, s_old=0, 11) decisions")
    else:
        px = acc["p1x"][1] / acc["p1x"][0]
        print(f"P1 P(X=1 | E11, s_old=0, 11) {acc['p1x'][1]}/{acc['p1x'][0]} = {px:.4f}; E11+E10 share {e['E11'] + e['E10']:.4f}: "
              f"{'HELD' if e['E11'] + e['E10'] >= 0.7 and px >= 0.8 else 'FAILED'}")
    tot = sum(v[0] for v in acc["cells"].values()); Hc = 0; mixed = []
    for key, (n, k) in sorted(acc["cells"].items(), key=lambda kv: -kv[1][0]):
        pr = k / n
        if 0 < pr < 1: Hc += n / tot * (-(pr * math.log2(pr) + (1 - pr) * math.log2(1 - pr)))
        if n >= 50 and 0.1 < pr < 0.9: mixed.append(key)
        print(f"CELL {key}: n {n}, k {k}, P(s_new=1) {pr:.4f}{'  EXACT CONFLICT' if 0 < k < n else ''}")
    nconf = sum(1 for n, k in acc["cells"].values() if 0 < k < n)
    print(f"P2 approximate (a cell with n >= 50 and 0.1 < P < 0.9): {'HELD' if mixed else 'FAILED'}")
    print(f"EXACT: {nconf} of {len(acc['cells'])} nonempty cells conflict; deterministic closure on M "
          f"{'REFUTED' if nconf else 'not refuted on this sample (not a theorem)'}; first conflicting pair: {acc['conflict']}")
    Hb = 0
    for st, (n, k) in acc["st"].items():
        pr = k / n
        if 0 < pr < 1: Hb += n / tot * (-(pr * math.log2(pr) + (1 - pr) * math.log2(1 - pr)))
    print(f"P3 H(s_new | M) = {Hc:.4f} bits; baseline H(s_new | current state) = {Hb:.4f}; difference {Hb - Hc:.4f} (descriptive): "
          f"{'HELD' if Hc <= 0.6 else 'FAILED'}; CF (>= 0.9): {'MET' if Hc >= 0.9 else 'not met'}")
    en = [(n, k) for key, (n, k) in acc["cells"].items() if key[0] == "ENONE"]
    if en:
        nn = sum(n for n, _ in en); kk = sum(k for _, k in en); pe = kk / nn
        print(f"PU ENONE P(s=1) {kk}/{nn} = {pe:.4f}: {'HELD' if 0.4 <= pe <= 0.6 else 'FAILED'}")
    else:
        print("PU UNTESTED: 0 ENONE decisions")
    print(f"CONTROLS: {'ALL PASS' if fails == 0 else 'FAIL'} ({fails} failures)")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
