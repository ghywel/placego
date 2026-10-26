#!/usr/bin/env python3
"""sideways_fresh.py: do the sinking top's decisions on fresh, prescribed and reused inputs follow one conditional law?
(Local, 2026-10-26, L960; frozen before its first run.)

RUN-ON:   cpu, pure Python 3, one process.  python3 sideways_fresh.py > out.txt.   CAPS: ulimit -t 900; tau in {101, 201}; columns <= 14 tau + 400;
          measurability check on at most 400 sampled columns.
CONTEXT:  GPT GC1899 (reports/rule30-sideways-fresh-input.md, exposure induction; Local's carrying read in L960: it carries) and GC1900
          (review of L959). With J_d = H_d + d - 1 and R the furthest exposed trace index, the next height is computable before any new bit
          is exposed; a NEW ODD index gives an exactly fair input s (conditional on the declared exposure history); a new even index is the
          prescribed tick; an old index is determined by that history. Backlog B_(d+1) = max(0, B_d + K_d - 1), K the drop.
          L957-L959 found the top's survival decided by s (L3-L6) and a fair-input window model matching the real speed; GC1900 notes that
          after larger drops the residences differ sharply from the fair chain (01u 7.643 vs 5, 11u 2.931 vs 7).
If this holds, it changes DQ-009: which of the front's inputs are coins, and whether the reused ones carry the deviation; no prize/proof status.

Input classes for a decision at column d >= 2 in top state 11 or 01 (s = c_(d-1)(H_d + 1), leading index J_d):
  NO  new odd index (J_d > R_(d-1), J_d odd)   -- exactly fair by GC1899
  NE  new even index (J_d > R_(d-1), J_d even) -- prescribed tick plus history
  R1  old index immediately after a one-level drop (J_d = J_(d-1), the L6 repeat)
  OB  any other old index (a backward visit, B >= 1)
Record searched (2026-10-26): "fresh sideways" via GC1899's search (13 hits / 8 files); sideways_front.py's searches the same day; no new search.

PREDICTIONS, written 2026-10-26 before the first run.
Controls:
  F0  measurability (GC1899's induction, operationally): at sampled columns, replacing every trace bit beyond R_d by its complement leaves
      both backgrounds at levels <= H_d and the next difference pair unchanged.
  F1  NO inputs are fair: P(s = 1 | NO) within 3 standard errors of 1/2, overall and separately in states 11 and 01.
  F2  the L6 repeat: P(s = 1 | R1, state 11 or 01) = 1 exactly.
  F3  backlog bookkeeping: B_(d+1) = max(0, B_d + K_d - 1) at every column, and a new index occurs iff B_d = 0 and K_d = 0.
Blind:
  P1  (closure-compatible) prescribed inputs behave like fresh ones given state: |P(s=1 | NE, st) - P(s=1 | NO, st)| <= 0.03 for st = 11, 01.
  P2  (where the deviation lives) backward visits are biased toward black: P(s = 1 | OB, st) >= 0.60 in both states (GC1900's residences:
      01u long means 01 survives, 11u short means 11 leaves; both need s = 1).
  P3  the share of decisions by class: NO in [0.30, 0.45], NE in [0.30, 0.45], R1 in [0.08, 0.20], OB in [0.03, 0.15].
  CF  if P1 fails (a gap >= 0.08 in either state), a fair-input model needs a parity bit; if P2 fails (OB near 1/2), the large-drop
      residence deviation is not carried by the inputs and must come from the lower discrepancy.
  PU  (unexpected) mean backlog over all decisions is at most 0.5, and B >= 3 occurs in at most 2% of decisions.

OUTCOME, 2026-10-26 (single run 11:11 GMT, 0.6 s, 16 MB max RSS; frozen sha256 fb4b5d93..., commit f2640c05; raw out.txt sha256 bd192e5c...,
cited/sideways-fresh-20261026/). Added after the run. F0 PASS (400 columns), F1 PASS (NO 0.4986 in 11, 0.5009 in 01, 0.4994 pooled), F2 PASS
(R1 all black, 2,768 + 33,031), F3 PASS. P1 HELD: NE - NO gaps 0.0042 (11) and 0.0043 (01). P2 FAILED in part: OB P(s=1) = 0.7075 in state 11
(n 9,355) but 0.4999 in 01 (n 7,829). P3 HELD (NO 0.4252, NE 0.4242, R1 0.1018, OB 0.0488). PU HELD (mean B 0.0644, P(B>=3) 0.0065).
"""
import random, statistics, sys

def trace(rng, L):
    a = 0
    for t in range(0, L, 2): a |= 1 << t
    for t in range(1, L, 2):
        if rng.getrandbits(1): a |= 1 << t
    return a

def cols(a, d):
    """columns d-1 and d of the reconstruction from trace a (as ints over t)."""
    cm1, c = 0, a
    for _ in range(1, d): cm1, c = c, (c >> 1) ^ (c | cm1)
    return cm1, c

def obits(al, be, u, w, mask):
    return ((al & ~be & ~w) | (~al & be & ~u) | (al & be & ~(u ^ w))) & mask

def run(rng, tau, acc, check):
    cap = 14 * tau + 400; L = tau + cap + 8
    a = trace(rng, L); b = a ^ (1 << tau); mask = (1 << (tau + 2)) - 1
    cm1, c, pm1, p = 0, a, 0, b
    dm1, dc = 0, (c ^ p) & mask
    R, Jprev, Hprev, Bprev, Kprev = tau, tau, tau, 0, 0
    H, age = tau, 0
    for d in range(1, cap):
        un = dc | dm1
        if un == 0: return d
        Hn = un.bit_length() - 1
        if d >= 2:
            K = Hprev - Hn
            J = Hn + d - 1
            new = J > R
            Bwant = max(0, Bprev + K - 1)
            if (new != (Bprev == 0 and K == 0)): acc["f3"] = False
            R = max(R, J); B = R - J
            if B != Bwant: acc["f3"] = False
            if Hn != H: age = 0; H = Hn
            al, be = (dc >> H) & 1, (dm1 >> H) & 1
            s = (cm1 >> (H + 1)) & 1
            if (al, be) != (1, 0):
                st = f"{al}{be}"
                if new: cl = "NO" if J % 2 else "NE"
                elif K == 1 and J == Jprev: cl = "R1"
                else: cl = "OB"
                k = (cl, st); acc["n"][k] = acc["n"].get(k, 0) + 1; acc["s"][k] = acc["s"].get(k, 0) + s
                acc["B"].append(B)
            Jprev, Bprev = J, B
        else:
            al, be = (dc >> H) & 1, (dm1 >> H) & 1
        cn = (c >> 1) ^ (c | cm1); pn = (p >> 1) ^ (p | pm1); dn = (cn ^ pn) & mask
        if check and d >= 2 and d % 50 == 0 and acc["chk"] < 400:
            acc["chk"] += 1
            junk = ((~a) >> (R + 1)) << (R + 1)
            a2 = (a & ((1 << (R + 1)) - 1)) | (junk & ((1 << L) - 1)); b2 = a2 ^ (1 << tau)
            x1, x0 = cols(a2, d); y1, y0 = cols(b2, d)
            lm = (1 << (H + 1)) - 1
            same_bg = (x0 & lm) == (c & lm) and (x1 & lm) == (cm1 & lm)
            xn = (x0 >> 1) ^ (x0 | x1); yn = (y0 >> 1) ^ (y0 | y1)
            same_next = ((xn ^ yn) & mask & lm) == (dn & lm)
            if not (same_bg and same_next): acc["f0"] = False
        Hprev = H
        cm1, c, pm1, p, dm1, dc = c, cn, p, pn, dc, dn
        age += 1
    return None

def main():
    rng = random.Random(20261026 + 960)
    fails = 0
    acc = {"n": {}, "s": {}, "B": [], "f0": True, "f3": True, "chk": 0}
    for tau, N in ((101, 300), (201, 200)):
        for i in range(N):
            if run(rng, tau, acc, check=(tau == 101 and i < 40)) is None: print("CENSORED"); fails += 1
    print(f"F0 measurability on {acc['chk']} sampled columns:", "PASS" if acc["f0"] and acc["chk"] > 0 else "FAIL"); fails += not (acc["f0"] and acc["chk"] > 0)
    print("F3 backlog bookkeeping:", "PASS" if acc["f3"] else "FAIL"); fails += not acc["f3"]
    tot = sum(acc["n"].values())
    P = lambda cl, st: (acc["s"].get((cl, st), 0) / acc["n"][(cl, st)]) if acc["n"].get((cl, st)) else float("nan")
    for cl in ("NO", "NE", "R1", "OB"):
        for st in ("11", "01"):
            print(f"CELL {cl} {st}: n {acc['n'].get((cl, st), 0)}, P(s=1) {P(cl, st):.4f}")
    f1 = True
    for sts in (("11",), ("01",), ("11", "01")):
        n = sum(acc["n"].get(("NO", st), 0) for st in sts); k = sum(acc["s"].get(("NO", st), 0) for st in sts)
        q = k / n; se = (0.25 / n) ** 0.5
        ok = abs(q - 0.5) <= 3 * se; f1 &= ok
        print(f"F1 NO {'+'.join(sts)}: {q:.4f} (3 SE {3*se:.4f}) {'PASS' if ok else 'FAIL'}")
    fails += not f1
    f2 = all(acc["s"].get(("R1", st), 0) == acc["n"].get(("R1", st), 0) for st in ("11", "01"))
    print("F2 L6 repeat inputs all black:", "PASS" if f2 else "FAIL"); fails += not f2
    g11, g01 = abs(P("NE", "11") - P("NO", "11")), abs(P("NE", "01") - P("NO", "01"))
    print(f"P1 NE-NO gaps 11 {g11:.4f}, 01 {g01:.4f} (<= 0.03): {'HELD' if max(g11, g01) <= 0.03 else 'FAILED'}; CF parity (>= 0.08): {'MET' if max(g11, g01) >= 0.08 else 'not met'}")
    p2 = P("OB", "11") >= 0.60 and P("OB", "01") >= 0.60
    print(f"P2 OB P(s=1) 11 {P('OB','11'):.4f}, 01 {P('OB','01'):.4f} (>= 0.60): {'HELD' if p2 else 'FAILED'}")
    share = {cl: sum(acc["n"].get((cl, st), 0) for st in ("11", "01")) / tot for cl in ("NO", "NE", "R1", "OB")}
    p3 = 0.30 <= share["NO"] <= 0.45 and 0.30 <= share["NE"] <= 0.45 and 0.08 <= share["R1"] <= 0.20 and 0.03 <= share["OB"] <= 0.15
    print(f"P3 shares {', '.join(f'{k} {v:.4f}' for k, v in share.items())}: {'HELD' if p3 else 'FAILED'}")
    mb = statistics.mean(acc["B"]); b3 = sum(1 for x in acc["B"] if x >= 3) / len(acc["B"])
    print(f"PU mean backlog {mb:.4f}, P(B>=3) {b3:.4f}: {'HELD' if mb <= 0.5 and b3 <= 0.02 else 'FAILED'}")
    print(f"CONTROLS: {'ALL PASS' if fails == 0 else 'FAIL'} ({fails} failures)")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
