"""clock_deadline_check.py: the refined left-only deadline H* explains GC1940's whole repair outcome (L1004, DQ-023).

Local, 2026-10-27. No search and no right-side edits: it evolves only the six cut left halves next to the clamped
clock, the diagnostic of GC1938/GC1939. GPT's stage (clock_cut_repair_intel.py) is not rerun.

Hand rules, for every right completion that has kept every earlier beat (the clock is black at even t):
  (i)  a black tick t with left neighbour l(t) = 0 fails at t+1 (the black centre masks the right side) [GC1938's H];
  (ii) white ticks t-2 and t with l = 0 at both fail at t+1. Passing t-2 needs r(t-2) = 1. Then r(t-1) = 0 XOR 1 = 1
       and r(t) = 1 XOR 1 = 0, but passing t needs r(t) = 1. This is L997's anti-latch, the coupled "no 00".
H* = the earlier of the two deadlines.

Predictions (written before the first replay): H* = 15, 16, 21, 23, 23, 28 for cuts 14, 15, 16, 21, 22, 23, equal to
GC1940's best observed failures. Counterfactual: a cut whose best observed failure exceeds H* would refute rule (ii).
H alone is 15, 17, 21, 23, 23, 33, so rule (ii) is what closes cuts 15 and 23.
Record searched: "no00", "free_bits_no00" (CL637, kit), "anti-latch" (L997), "H=d" (GC1938).

Run: python3 -I tests/probes/wolfram/clock_deadline_check.py   (exit status 1 on any mismatch)
Outcome (2026-10-27, M5, under 1 s): all six match, exit 0. The two inline replays that preceded this file gave the
same numbers.
"""
import sys

T, N = 60, 400
RIGHT = [int(c) for c in "0000110110001101000"]
BEST_GC1940 = {14: 15, 15: 16, 16: 21, 21: 23, 22: 23, 23: 28}


def row(cut):
    left = [1 if (d % 7) in (0, 1, 2) else 0 for d in range(N, 0, -1)]      # depths N..1, left to right
    left = [v if (N - i) <= cut else 0 for i, v in enumerate(left)]
    return left + [1] + RIGHT + [0] * (T + 5)


def left_trace(cut):
    x = row(cut)
    out = [x[N - 1]]
    for t in range(T):
        y = [0] * len(x)
        for i in range(1, len(x) - 1):
            y[i] = x[i - 1] ^ (x[i] | x[i + 1])
        y[N] = 1 if (t + 1) % 2 == 0 else 0                                    # clamp the centre to the clock
        x = y
        out.append(x[N - 1])
    return out


bad = 0
for cut, best in BEST_GC1940.items():
    l = left_trace(cut)
    h1 = next(t + 1 for t in range(0, T, 2) if l[t] == 0)
    h2 = next((t + 1 for t in range(3, T, 2) if l[t] == 0 and l[t - 2] == 0), T + 1)
    hstar = min(h1, h2)
    ok = hstar == best
    bad += not ok
    print("cut %2d: H = %2d, white-tick 00 deadline = %2d, H* = %2d, GC1940 best = %2d, %s" % (cut, h1, h2, hstar, best, "match" if ok else "MISMATCH"))
print("ALL MATCH" if not bad else "FAIL")

# ---- Second part (L1006, GC1942/GC1943 review; predictions written before it ran) ----
# GC1942's front parity: for d = 2 mod 4, l_(d+28)(d+28) = NOT l_d(d). Cut L21 (d = 22) has l(22) = 0 (GC1940), so
# P1: cut L49 (d = 50) has l(50) = 1, and cut L77 (d = 78) has l(78) = 0 again (GPT's unexpected check).
# P2: cut 49's black-tick deadline H is at least 53 (GC1942).
# Screens for every right completion (GC1943 adds the third): (i) black tick with l = 0; (ii) white ticks t-2, t with
# l = 0, 0; (iii) five white ticks u, u+2, ..., u+8 with l = 1, which forces failure by u+9 (kit col1_five_check).
# The result is reported, not asserted: it is the hand question GPT asked, H*** = the earliest of the three.
T2 = 140


def left_trace_long(cut, T):
    x = row_long(cut, T)
    out = [x[NL - 1]]
    for t in range(T):
        y = [0] * len(x)
        for i in range(1, len(x) - 1):
            y[i] = x[i - 1] ^ (x[i] | x[i + 1])
        y[NL] = 1 if (t + 1) % 2 == 0 else 0
        x = y
        out.append(x[NL - 1])
    return out


NL = 400


def row_long(cut, T):
    left = [1 if (d % 7) in (0, 1, 2) else 0 for d in range(NL, 0, -1)]
    left = [v if (NL - i) <= cut else 0 for i, v in enumerate(left)]
    return left + [1] + RIGHT + [0] * (T + 5)


p_ok = True
for cut, d, want in ((21, 22, 0), (49, 50, 1), (77, 78, 0)):
    l = left_trace_long(cut, T2)
    if l[d] != want:
        p_ok = False
    h1 = next((t + 1 for t in range(0, T2, 2) if l[t] == 0), None)
    h2 = next((t + 1 for t in range(3, T2, 2) if l[t] == 0 and l[t - 2] == 0), None)
    h3 = next((u + 9 for u in range(1, T2 - 8, 2) if all(l[u + 2 * j] == 1 for j in range(5))), None)
    hs = min(h for h in (h1, h2, h3) if h is not None)
    whites = "".join(str(l[t]) for t in range(d - 9, min(hs, d + 12), 2))
    print("cut %2d (d = %2d): l(d) = %d (predicted %d) | H(i) = %s, H(ii) = %s, H(iii) = %s, H*** = %d | white-tick l from %d: %s"
          % (cut, d, l[d], want, h1, h2, h3, hs, d - 9, whites))
print("P1 (front parity):", "HELD" if p_ok else "FAILED")
bad += not p_ok
print("ALL MATCH" if not bad else "FAIL")
sys.exit(1 if bad else 0)
