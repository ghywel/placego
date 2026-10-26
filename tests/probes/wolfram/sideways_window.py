#!/usr/bin/env python3
"""sideways_window.py: is the sideways front speed a finite-window number? (Local, 2026-10-26, L959; frozen before its first run.)

RUN-ON:   cpu, pure Python 3, one process.  python3 sideways_window.py > out.txt.   CAPS: ulimit -t 900; tau <= 201; window runs 200,000 columns
          per k, k <= 6.
CONTEXT:  L957/L958 (reports/rule30-sideways-front.md). Exact: four bits close the top (L2); 10 always survives (L3); 11 survives iff the
          cell s above is white (L5); 01 survives iff s is black (L4); a vacated level leaves its cell black (L6). Measured: background rows
          fair and uncorrelated; arrival bias 0.868; drops mean 1.27; real speed about 0.155 levels per column.
If this holds, it changes DQ-009: the forgetting front's speed becomes a finite-chain quantity; no prize/proof status.

HAND (L959). With fair independent s after the first decision, residence at a level (columns from arrival to the drop):
  arrive in 10: 8 columns; arrive in 11 with the first s forced black (L6): 1 + E01 = 6; arrive in 01 with the first s forced: 1 + E10 = 9
  (E10 = 8, E11 = 7, E01 = 5). With P(forced) = 0.736 (from 0.868 = P(forced) + P(unforced)/2) and mean drop 1.27, the speed lies between
  1.27 / 6.53 = 0.194 (all forced arrivals in 11) and 1.27 / 8.74 = 0.145 (all in 01); the measured 0.155 sits inside.

THE WINDOW MODEL. By L1 the levels at and below any level form a closed system given the backgrounds there, and the backgrounds obey the
same recurrence c_(d+1)(t) = c_d(t+1) XOR (c_d(t) OR c_(d-1)(t)) row by row from the row above. Keep the top level, the k levels below it
and the row above; feed the row above's next value with a fair coin (the measured rows are fair). At a drop the window slides down; new
bottom levels start with no difference and fair background. If the window empties (a drop past its bottom), restart a top in state 10 one
level below the window (counted as a drop of k+1). Speed v(k) = total drop / columns over 200,000 columns.
Record searched (2026-10-26): as sideways_front.py (same day); no new search.

PREDICTIONS, written 2026-10-26 before the first run.
Controls:
  W0  L6 exactly in the real process: after every drop of one level that arrives in state 11 or 01, the first s is black.
  W1  the real runs reproduce L957's speed within 0.004 (pooled tau = 101, 201: v = total drop / total columns).
Blind:
  P1  real residence by arrival: arrive 10 in [7.5, 8.5]; 11 after a forced first s in [5.5, 6.5]; 01 after a forced first s in [8.5, 9.5].
  P2  v(k) is nonincreasing in k (dips <= 0.003 allowed).
  P3  (the door) v(3) is within 5% of the real speed; v(6) within 2%.
  CF  v(6) more than 10% from the real speed: the deep profile or the fair-row feed matters, and no small chain carries the speed.
  PU  (unexpected) window empties per drop at k = 4 are at most 2%.
"""
import random, statistics, sys

def trace(rng, L):
    a = 0
    for t in range(0, L, 2): a |= 1 << t
    for t in range(1, L, 2):
        if rng.getrandbits(1): a |= 1 << t
    return a

def obits(al, be, u, w, mask):
    return ((al & ~be & ~w) | (~al & be & ~u) | (al & be & ~(u ^ w))) & mask

def real(rng, tau, acc):
    cap = 14 * tau + 400; L = tau + cap + 8
    a = trace(rng, L); b = a ^ (1 << tau); mask = (1 << (tau + 2)) - 1
    cm1, c, pm1, p = 0, a, 0, b
    dm1, dc = 0, (c ^ p) & mask
    H, label, res = None, None, 0
    for d in range(1, cap):
        un = dc | dm1
        if un == 0:
            if label: acc["res"].setdefault(label, []).append(res)
            return d
        Hn = un.bit_length() - 1
        al, be = (dc >> Hn) & 1, (dm1 >> Hn) & 1
        if Hn != H:                                   # arrival at a new level (or the start)
            if label: acc["res"].setdefault(label, []).append(res)
            drop = None if H is None else H - Hn
            if drop is None: label = None
            elif (al, be) == (1, 0): label = "10"
            else: label = f"{al}{be}" + ("f" if drop == 1 else "u")
            H, res = Hn, 0
            s = (cm1 >> (H + 1)) & 1
            if label in ("11f", "01f") and s != 1: acc["w0"] = False
        cn = (c >> 1) ^ (c | cm1); pn = (p >> 1) ^ (p | pm1); dn = (cn ^ pn) & mask
        un2 = dn | dc
        H2 = un2.bit_length() - 1 if un2 else -1
        acc["cols"] += 1
        if H2 < H: acc["drop"] += H - H2
        res += 1
        cm1, c, pm1, p, dm1, dc = c, cn, p, pn, dc, dn
    return None

def window(rng, k, ncols):
    # band levels 0..k+1 (relative): level k is the top, k+1 the row above; bit i is relative level i
    n = k + 2; mask = (1 << n) - 1; topbit = k
    c = rng.getrandbits(n); cm1 = rng.getrandbits(n)
    dc, dm1 = 1 << topbit, 0
    drop = 0; empties = 0; drops = 0
    for _ in range(ncols):
        fair = rng.getrandbits(1)
        cn = (((c >> 1) | (fair << (n - 1))) ^ (c | cm1)) & mask      # row above the band gets a fair coin
        on = obits(dc, dm1, c, cm1, mask)
        dn = ((dc >> 1) ^ on) & mask & ((1 << (k + 1)) - 1)           # no difference above the top
        un2 = dn | dc
        if un2 == 0:
            empties += 1; drops += 1; drop += k + 1
            c, cm1 = rng.getrandbits(n), rng.getrandbits(n); dc, dm1 = 1 << topbit, 0
            continue
        H2 = un2.bit_length() - 1
        sh = topbit - H2
        if sh > 0:
            drops += 1; drop += sh
            fill = lambda x: ((x << sh) | rng.getrandbits(sh)) & mask
            c, cm1 = fill(cn), fill(c)
            dc, dm1 = (dn << sh) & mask, (dc << sh) & mask
        else:
            cm1, c, dm1, dc = c, cn, dc, dn
    return drop / ncols, empties / max(drops, 1)

def main():
    rng = random.Random(20261026 + 959)
    fails = 0
    acc = {"res": {}, "cols": 0, "drop": 0, "w0": True}
    for tau, N in ((101, 300), (201, 200)):
        for _ in range(N):
            if real(rng, tau, acc) is None: print("CENSORED"); fails += 1
    print("W0 L6: first s black after every one-level drop into 11 or 01:", "PASS" if acc["w0"] else "FAIL"); fails += not acc["w0"]
    vr = acc["drop"] / acc["cols"]
    ok1 = abs(vr - 0.1555) <= 0.004
    print(f"W1 real speed {vr:.4f} (L957 about 0.155): {'PASS' if ok1 else 'FAIL'}"); fails += not ok1
    for key in sorted(acc["res"]):
        r = acc["res"][key]; print(f"RES arrive {key}: n {len(r)}, mean {statistics.mean(r):.3f}")
    tot = sum(len(v) for v in acc["res"].values())
    print("ARRIVAL fractions:", {k: round(len(v) / tot, 4) for k, v in sorted(acc["res"].items())})
    m = lambda key: statistics.mean(acc["res"][key]) if key in acc["res"] else float("nan")
    p1 = 7.5 <= m("10") <= 8.5 and 5.5 <= m("11f") <= 6.5 and 8.5 <= m("01f") <= 9.5
    print(f"P1 residences 10 / 11f / 01f = {m('10'):.3f} / {m('11f'):.3f} / {m('01f'):.3f}: {'HELD' if p1 else 'FAILED'}")
    vk = {}
    for k in range(1, 7):
        v, e = window(rng, k, 200000); vk[k] = (v, e)
        print(f"WINDOW k={k}: v {v:.4f}, empties per drop {e:.4f}")
    p2 = all(vk[k + 1][0] <= vk[k][0] + 0.003 for k in range(1, 6))
    r3, r6 = abs(vk[3][0] - vr) / vr, abs(vk[6][0] - vr) / vr
    print(f"P2 nonincreasing: {'HELD' if p2 else 'FAILED'}")
    print(f"P3 v(3) gap {r3:.3f} (<= 0.05): {'HELD' if r3 <= 0.05 else 'FAILED'}; v(6) gap {r6:.3f} (<= 0.02): {'HELD' if r6 <= 0.02 else 'FAILED'}; CF (> 0.10): {'MET' if r6 > 0.10 else 'not met'}")
    print(f"PU empties per drop at k=4 {vk[4][1]:.4f} (<= 0.02): {'HELD' if vk[4][1] <= 0.02 else 'FAILED'}")
    print(f"CONTROLS: {'ALL PASS' if fails == 0 else 'FAIL'} ({fails} failures)")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
