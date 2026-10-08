#!/usr/bin/env python3
"""rule30_cloud_review_g248.py: Cloud's replay of G248 and its GC582 extension (row 6.1, the kicked wheel)

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_review_g248.py [TRIALS=600] [T=20000] [SEED=5601]
COST:       about two minutes.

G248 (GPT, GC581): for one pure splice of the visible wheel V (U's 28 even samples) from phase i to phase j, the
charge reading L = Phi(i) - Phi(j) and the phase reading K = -17 (i - j) satisfy L - K = 14 R (mod 28), where R is the
crossing zero gap. GC582 extends it to any two RB locks, adjacent or not: choose visible blacks A in the old lock and
B > A in the new one; then L - K = 14 (R_1 + .. + R_N) (mod 28), summed over the complete visible zero gaps from A to B,
whatever blacks are chosen. Cloud read both by hand first (CL056); this replays them on RB's own locks and seeds.
Controls (predicted to PASS, since both are theorems if the reading is right):
  RG248-C1: G248's hand controls. i = 0, j = 22 gives R = 2, L = K = 10; i = 0, j = 23 gives R = 1, L = 13, K = 27.
            Over all 28 x 28 formal splices, L - K = 14 R (mod 28).
  RG248-C2: GC582's identity at every pair of consecutive RB locks (chained or not), with the last visible black of
            the old lock and the first of the new as A and B, and again with a black drawn at random inside each
            lock, the same answer.
PREDICTION (Cloud's, pushed before the first run):
  RG248-P1: on seed 5601 exactly one chained kick has odd gap sum, RB's trial 133 at t = 71, with gaps 4, 1, 4, 4
            (GC582's reading of it). Confidence 0.85.
UNEXPECTED CHECK: among unchained consecutive lock pairs (56 or more steps apart, with an off-wheel stretch between
  them), fewer than 1% have an odd gap sum, so the charge and phase readings almost always agree mod 28 even across
  long transients. Confidence 0.5.
Counterfactual: if many unchained pairs have odd sums, odd visible gaps are common off the wheel, and RV2's "gaps 2
  and 4 only" is a property of short transients.
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_cloud_wheel_drift as rd                        # noqa: E402
sys.argv = _argv

P = 56
TRIALS = int(sys.argv[1]) if len(sys.argv) > 1 else 600
T = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 5601
rd.T = T
V = [rd.U[2 * a] for a in range(28)]
M = [0]
for x in V:
    M.append(M[-1] + x)                                       # M(a) for a = 0 .. 28; M(28) = 6


def Mx(a):
    return M[a % 28] + 6 * (a // 28)


def Phi(a):
    return 14 * Mx(a) - 3 * a                                 # 28-periodic


def splice(i, j):
    """L, K and the crossing gap R for the pure splice V(i + n), n < 0, then V(j + n), n >= 0."""
    l = next(l for l in range(1, 29) if V[(i - l) % 28])
    r = next(r for r in range(0, 28) if V[(j + r) % 28])
    return (Phi(i) - Phi(j)) % 28, (-17 * (i - j)) % 28, l + r - 1


def gap_sum(c1, A, B):
    """Sum of the complete visible zero gaps from the visible black at time A to the one at time B (both even)."""
    blacks = [t for t in range(A, B + 1, 2) if c1[t]]
    return sum((b - a) // 2 - 1 for a, b in zip(blacks, blacks[1:])), blacks


def main():
    L, K, R = splice(0, 22)
    c1_ok = (L, K, R) == (10, 10, 2) and splice(0, 23) == (13, 27, 1)
    c1_ok &= all((splice(i, j)[0] - splice(i, j)[1] - 14 * splice(i, j)[2]) % 28 == 0
                 for i in range(28) for j in range(28))
    print("RG248-C1", "PASS" if c1_ok else "FAIL", "(hand controls and all 784 formal splices)")
    rng = random.Random(SEED)
    pick = random.Random(SEED + 248)
    c2_ok = True
    odd_chained, n_chained, odd_free, n_free = [], 0, 0, 0
    for trial in range(TRIALS):
        w = (16, 24, 32, 48, 64)[trial % 5]
        c1 = rd.column1(rng.getrandbits(w) | 1)
        Q = [0]
        for t, x in enumerate(c1):
            Q.append(Q[-1] + (14 * x - 3 if t % 2 == 0 else 0))
        lk = rd.locks(c1)
        lam = []
        for a, s, d in lk:
            t0 = a + a % 2
            lam.append(Q[t0] - (Phi(((t0 - d) % P) // 2) + 0))
        for j in range(len(lk) - 1):
            (a, s, d), (a2, s2, d2) = lk[j], lk[j + 1]
            Lv = lam[j + 1] - lam[j]
            Kv = rd.kick_of((d2 - d) % P)
            old = [t for t in range(a + a % 2, s, 2) if c1[t]]
            new = [t for t in range(a2 + a2 % 2, s2, 2) if c1[t]]
            sums = set()
            for A, B in ((old[-1], new[0]), (pick.choice(old), pick.choice(new))):
                g, _ = gap_sum(c1, A, B)
                sums.add(g % 2)
                c2_ok &= (Lv - Kv - 14 * g) % 28 == 0
            c2_ok &= len(sums) == 1
            g, blacks = gap_sum(c1, old[-1], new[0])
            if a2 - s < P:
                n_chained += 1
                if g % 2:
                    gaps = [(b - x) // 2 - 1 for x, b in zip(blacks, blacks[1:])]
                    odd_chained.append((trial, s, gaps, Lv, Kv))
            else:
                n_free += 1
                odd_free += g % 2
    print("RG248-C2", "PASS" if c2_ok else "FAIL", f"({n_chained} chained and {n_free} unchained consecutive pairs)")
    print("chained pairs with odd gap sum:", odd_chained)
    p1 = len(odd_chained) == 1 and odd_chained[0][0] == 133 and 4 in odd_chained[0][2] and 1 in odd_chained[0][2]
    print("RG248-P1", "HELD" if p1 else "REFUTED")
    frac = odd_free / n_free if n_free else 0.0
    print(f"unchained pairs with odd gap sum: {odd_free} of {n_free} ({frac:.4f})")
    print("unexpected check", "HELD" if frac < 0.01 else "REFUTED")


if __name__ == "__main__":
    main()
