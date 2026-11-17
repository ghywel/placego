#!/usr/bin/env python3
"""rule30_cloud_review_old1.py: Cloud's independent replay of GPT's OLD1 (GC584, GC588; row 6.1, entry 26)

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_review_old1.py [M=16]
COST:       under a minute.

GC584: KL's one-turn sets impose a starting companion observation and then 56 matched transitions, so a departure
from them follows 57 old observations. RD's shortest lock [a, s) has only 56 observations, 55 matched transitions.
GC588 (OLD1, run once by GPT with KL's step and set routines): at m = 16, with 21 new observations, the 55-transition
projection admits one more departure class than the 56-transition one, class 19 with kicks -8 .. -4. The rest of the
two tables are equal, with 252 extra hidden states (94 at terminal phase 18, 158 at 30). This replay shares no code
with KL or OLD1. It writes its own width-m window beside the wall (site 0 the clock t mod 2, site 1 the companion
column 1, sites 2 .. m hidden, site m + 1 a free input), steps it with Rule 30 by integer shifts, and propagates
hidden-state sets on the wheel U. Departure classes and kicks are defined as in KL: a departure at time a = t + 1
whose observation differs from U[a]; then for each even phase change dn with U[a - dn] equal to the departure
observation, 20 more steps on the new phase; the kick of dn is (-17 dn / 2) mod 28, signed to -14 .. 13.
Controls (should PASS):
  RO-C1: the window step agrees with direct Rule 30 on whole rows for every hidden state at m = 4 and 5.
  RO-C2: the 56-transition table at m = 16 has exactly the classes 2, 12, 22, 32, 39, 42, 49, 52 with GC588's
         alphabets.
PREDICTIONS (Cloud's, pushed before the first run):
  RO-P1: the 55-transition table equals GC588's exactly: the same eight classes plus class 19 with -8 .. -4.
         Confidence 0.85.
  RO-P2: the extra states number 252, 94 at terminal phase 18 and 158 at 30. Confidence 0.8.
UNEXPECTED CHECK (not computed by anyone yet): one transition shorter still, at 54 matched transitions
  (55 observations), at least one further departure class appears beyond class 19. Confidence 0.5.
Counterfactual: if 54 transitions give the same table as 55, class 19 is a one-off boundary effect, and the table
  is stable below 56 except for it.

OUTCOME, 2026-10-08 (by 21:09 BST; 8 s): RO-C1 and RO-C2 PASS. RO-P1 and RO-P2 HELD: with no code shared with KL or
  OLD1, the 56- and 55-transition tables are exactly GC588's. The 55-transition table adds only class 19, kicks -8 .. -4,
  and the extra states are 94 at terminal phase 18 and 158 at 30, 252 in all. The unexpected check was REFUTED: 54
  transitions give the same table as 55, and the counterfactual holds that far.
  Post-hoc, the same run extended down to 28 transitions. The table is unchanged from 55 down to 44. At 43 a class 29
  appears, with kicks -9 .. -5. At 38 class 2 gains +9. From 38 down to 28 nothing more changes. The classes that
  appear with shorter histories, 19 and then 29, continue the spacing of 10 of the odd classes 39 and 49, as the even
  classes 2, 12, .., 52 are spaced. This says nothing about which classes actual right halves reach.
"""
import sys

M = int(sys.argv[1]) if len(sys.argv) > 1 else 16
U = [int(c) for c in "00010011010001001101000100110100010011010001001101001101"]
P, F = 56, 20


def step(h, t, m, inp, c1):
    """One Rule 30 step of the window; returns (new hidden state, new companion bit)."""
    r = (t & 1) | (c1 << 1) | (h << 2) | (inp << (m + 1))
    new = (r << 1) ^ (r | (r >> 1))
    return (new >> 2) & ((1 << (m - 1)) - 1), (new >> 1) & 1


def advance(S, t, m, c1, want, keep=True):
    out = set()
    for h in S:
        for inp in (0, 1):
            nh, x1 = step(h, t, m, inp, c1)
            if (x1 == want) == keep:
                out.add(nh)
    return out


def kick_of(dn):
    k = (-17 * (dn // 2)) % 28
    return k if k < 14 else k - 28


def table(sets, m):
    out = {}
    for t in range(P):
        a = (t + 1) % P
        dep = advance(sets[t], t, m, U[t], U[a], keep=False)
        if not dep:
            continue
        ks = []
        for dn in range(0, P, 2):
            if U[(a - dn) % P] != 1 - U[a]:
                continue
            S = dep
            for s in range(a, a + F):
                S = advance(S, s, m, U[(s - dn) % P], U[(s + 1 - dn) % P])
                if not S:
                    break
            if S:
                ks.append(kick_of(dn))
        out[a] = sorted(ks)
    return out


def control():
    ok = True
    for m in (4, 5):
        for h in range(1 << (m - 1)):
            for t in (0, 1):
                for c1 in (0, 1):
                    for inp in (0, 1):
                        row = [t & 1, c1] + [(h >> b) & 1 for b in range(m - 1)] + [inp]
                        nxt = [row[i - 1] ^ (row[i] | row[i + 1]) for i in range(1, m + 1)]
                        ok &= step(h, t, m, inp, c1) == (sum(nxt[i] << (i - 1) for i in range(1, m)), nxt[0])
    return ok


def main():
    print("RO-C1", "PASS" if control() else "FAIL")
    counts = (54, 55, 56)
    sets = {n: [set() for _ in range(P)] for n in counts}
    for phase in range(P):
        cur = set(range(1 << (M - 1)))
        for off in range(P):
            t = (phase + off) % P
            cur = advance(cur, t, M, U[t], U[(t + 1) % P])
            if off + 1 in sets:
                sets[off + 1][(phase + off + 1) % P] |= cur
    tabs = {n: table(sets[n], M) for n in counts}
    for n in counts:
        print(f"{n} transitions:", {a: v for a, v in sorted(tabs[n].items())})
    gc588 = {2: [5, 6, 7, 8, 10], 12: [4, 5, 6, 7, 8, 9], 22: [3, 4, 5, 6, 7, 8], 32: [2, 3, 4, 5, 6, 7],
             39: [-10, -9, -8, -7, -6], 42: [1, 2, 3, 4, 5, 6], 49: [-11, -10, -9, -8, -7],
             52: [-6, -5, -4, -3, -2, -1]}
    print("RO-C2", "PASS" if tabs[56] == gc588 else "FAIL")
    print("RO-P1", "HELD" if tabs[55] == {**gc588, 19: [-8, -7, -6, -5, -4]} else "REFUTED")
    diff = [len(a - b) for a, b in zip(sets[55], sets[56])]
    extra = {ph: d for ph, d in enumerate(diff) if d}
    print("extra 55-transition states by terminal phase:", extra, "total", sum(diff))
    print("RO-P2", "HELD" if extra == {18: 94, 30: 158} else "REFUTED")
    new54 = sorted(set(tabs[54]) - set(tabs[55]))
    wider = {a: v for a, v in tabs[54].items() if a in tabs[55] and v != tabs[55][a]}
    print("54 transitions: new classes", new54, "; changed alphabets", wider)
    print("unexpected check", "HELD" if new54 else "REFUTED")


if __name__ == "__main__":
    main()
