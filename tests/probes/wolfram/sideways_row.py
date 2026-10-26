#!/usr/bin/env python3
"""sideways_row.py: the sinking top is driven by ONE background row; is its bias in the row or in the top's choice of row?
(Local, 2026-10-26, L958; frozen before its first run.)

RUN-ON:   cpu, pure Python 3, one process.  python3 sideways_row.py > out.txt.   CAPS: ulimit -t 900; tau <= 201; columns <= 14 tau + 400.
CONTEXT:  L957 (reports/rule30-sideways-front.md): four bits close the sideways top (L2); state 10 always survives (L3); state 01 survives
          iff the shared cell above the top, one column back, is black (L4). GPT's GC1897 mask identity is L4's (0,1) case.
If this holds, it changes DQ-009: the forgetting front's speed would be carried by a single background row; no prize/proof status.

HAND LEMMA L5 (L958, single-party). Let H be the top of supp delta_d U supp delta_(d-1) and s = c_(d-1)(H+1), the shared background cell
just above the top in the previous column. State 11 at the top comes only from 10 or 11 (01 survives into 10, never 11).
  From 10 at d-1 (where c_(d-2)(H) = 0 by L3): u = c_d(H) = c_(d-1)(H+1) XOR (c_(d-1)(H) OR 0), w = c_(d-1)(H); so u = w iff s = 0.
  From 11 at d-1 that survived (c_(d-1)(H) = c_(d-2)(H) = v): u = s XOR (v OR v) = s XOR v, w = v; so u = w iff s = 0.
So: state 10 survives always (to 11); 11 survives iff s = 0 (else to 01); 01 survives iff s = 1 (to 10), else the level vacates.
The top's fate at its level is a deterministic function of ONE row of the shared background, the row just above it, read along the
columns. (In the forward picture that row is the spacetime row at time H+1, read across depths.) With fair independent s the residence
from 10 is 8 columns (L957's hand chain). L957 measured P(s = 1 | 01) = 0.6154 and P(s = 1 | 11) = 1 - 0.4824 = 0.5176.

QUESTION: is the bias in the ROW (rows of this reconstructed spacetime are correlated along depth) or in the TOP (it selects where it
sits)? And how far does a drop go?
Record searched (2026-10-26): as sideways_front.py (same day; "sideways" 271/75, "0.246" 72/30); no new search.

PREDICTIONS, written 2026-10-26 before the first run.
Controls:
  R0  L5 at every column of every real run: survival and next top state are exactly the rule above, with s read from the background.
  R1  the run reproduces L957's top statistics within 0.02: P(s = 1 | 01) about 0.615, P(s = 0 | 11) about 0.482 (tau = 101, 201).
Blind:
  P1  (the row) unconditionally, consecutive cells of a background row are nearly uncorrelated: P(c_d(t) = 1 | c_(d-1)(t) = 1) over levels
      10 <= t <= 100 and columns 200 <= d <= 600 lies in [0.45, 0.55], and so does the plain density.
  P2  (the top's choice) the bias sits at arrival: P(s = 1) at the first decision after the top arrives at a new level is >= 0.60, and for
      decisions at age >= 6 columns in the level it is within [0.45, 0.56].
  P3  drops: P(drop = 1) >= 0.75 and P(drop >= 4) <= 0.03 (L957: mean 1.27).
  CF  if P1 fails (rows correlated, say >= 0.58), the bias is the row's, and a derivation needs the reconstructed rows' statistics,
      not a selection argument.
  PU  (unexpected: the wall) the plain density of background rows near the floor (levels 0 <= t <= 3, d in 200..600) differs from the
      mid-level density by less than 0.05.
"""
import random, statistics, sys

def trace(rng, L):
    a = 0
    for t in range(0, L, 2): a |= 1 << t
    for t in range(1, L, 2):
        if rng.getrandbits(1): a |= 1 << t
    return a

def run(rng, tau, acc):
    cap = 14 * tau + 400; L = tau + cap + 8
    a = trace(rng, L); b = a ^ (1 << tau); mask = (1 << (tau + 2)) - 1
    cm1, c, pm1, p = 0, a, 0, b
    dm1, dc = 0, (c ^ p) & mask
    prevH, age, ok = None, 0, True
    for d in range(1, cap):
        un = dc | dm1
        if un == 0: return d, ok
        H = un.bit_length() - 1
        if H != prevH: age = 0; prevH = H
        al, be = (dc >> H) & 1, (dm1 >> H) & 1
        s = (cm1 >> (H + 1)) & 1
        cn = (c >> 1) ^ (c | cm1); pn = (p >> 1) ^ (p | pm1); dn = (cn ^ pn) & mask
        surv = (dn >> H) & 1
        nxt = (surv, al)            # next pair at level H: (delta_(d+1)(H), delta_d(H))
        st = (al, be)
        if d >= 2:                  # L5 is stated for d >= 2 (at d = 1 the cell s is column 0, white, and state 10 survives by L3)
            if st == (1, 0): want = (1, (1, 1))
            elif st == (1, 1): want = (1, (1, 1)) if s == 0 else (0, (0, 1))
            else: want = (1, (1, 0)) if s == 1 else (0, (0, 0))
            if (surv, nxt) != want: ok = False
            key = "11" if st == (1, 1) else "01" if st == (0, 1) else None
            if key:
                acc[key][0] += 1; acc[key][1] += s
            # first decision after arrival at a new level (state 10 decides nothing; the first s that matters)
            if key and acc["_lastlevel"] != H:
                acc["arr"][0] += 1; acc["arr"][1] += s; acc["_lastlevel"] = H
            if key and age >= 6:
                acc["old"][0] += 1; acc["old"][1] += s
        un2 = dn | dc
        H2 = un2.bit_length() - 1 if un2 else -1
        if H2 < H: acc["drops"].append(H - H2)
        cm1, c, pm1, p, dm1, dc = c, cn, p, pn, dc, dn
        age += 1
    return None, ok

def row_stats(rng, n):
    """Plain density and P(1|1) along background rows: columns 200..600, levels 0..100, from fresh traces."""
    one = tot = pair11 = prev1 = 0; floor_one = floor_tot = 0
    for _ in range(n):
        L = 800; a = trace(rng, L)
        cm1, c = 0, a
        cols = []
        for d in range(1, 601):
            cm1, c = c, (c >> 1) ^ (c | cm1)
            if d >= 199: cols.append(c)
        for t in range(0, 101):
            bits = [(col >> t) & 1 for col in cols]
            if t <= 3:
                floor_one += sum(bits); floor_tot += len(bits)
            if t >= 10:
                one += sum(bits); tot += len(bits)
                for x, y in zip(bits, bits[1:]):
                    if x: prev1 += 1; pair11 += y
    return one / tot, pair11 / prev1, floor_one / floor_tot

def main():
    rng = random.Random(20261026 + 958)
    fails = 0
    acc = {"11": [0, 0], "01": [0, 0], "arr": [0, 0], "old": [0, 0], "drops": [], "_lastlevel": None}
    allok = True
    for tau, N in ((101, 300), (201, 200)):
        for _ in range(N):
            acc["_lastlevel"] = None
            D, ok = run(rng, tau, acc)
            if D is None: print("CENSORED"); fails += 1
            allok &= ok
    print("R0 L5 holds at every column (d >= 2):", "PASS" if allok else "FAIL"); fails += not allok
    p01 = acc["01"][1] / acc["01"][0]; p11 = 1 - acc["11"][1] / acc["11"][0]
    r1 = abs(p01 - 0.6154) <= 0.02 and abs(p11 - 0.4824) <= 0.02
    print(f"R1 P(s=1|01) = {p01:.4f}, P(s=0|11) = {p11:.4f} (counts {acc['01'][0]}, {acc['11'][0]}): {'PASS' if r1 else 'FAIL'}"); fails += not r1
    dens, c11, floor = row_stats(rng, 60)
    p1 = 0.45 <= c11 <= 0.55 and 0.45 <= dens <= 0.55
    print(f"P1 background rows: density {dens:.4f}, P(1|1) along the row {c11:.4f}: {'HELD' if p1 else 'FAILED'}; CF (P(1|1) >= 0.58): {'MET' if c11 >= 0.58 else 'not met'}")
    pa = acc["arr"][1] / acc["arr"][0]; po = acc["old"][1] / acc["old"][0]
    p2 = pa >= 0.60 and 0.45 <= po <= 0.56
    print(f"P2 P(s=1) at the first decision in a level {pa:.4f} (n {acc['arr'][0]}); at age >= 6 {po:.4f} (n {acc['old'][0]}): {'HELD' if p2 else 'FAILED'}")
    dr = acc["drops"]; f1 = sum(1 for x in dr if x == 1) / len(dr); f4 = sum(1 for x in dr if x >= 4) / len(dr)
    hist = {k: sum(1 for x in dr if x == k) for k in range(1, 8)}
    print(f"P3 drops: n {len(dr)}, mean {statistics.mean(dr):.4f}, P(1) {f1:.4f}, P(>=4) {f4:.4f}, histogram {hist}: {'HELD' if f1 >= 0.75 and f4 <= 0.03 else 'FAILED'}")
    print(f"PU floor density {floor:.4f} vs mid {dens:.4f}: {'HELD' if abs(floor - dens) < 0.05 else 'FAILED'}")
    print(f"CONTROLS: {'ALL PASS' if fails == 0 else 'FAIL'} ({fails} failures)")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
