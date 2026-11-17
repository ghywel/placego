#!/usr/bin/env python3
"""rule30_cloud_wheel_balance.py: RB, why do the wheel's forward and backward kicks cancel? (row 6.1)

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_wheel_balance.py [TRIALS=600] [T=20000] [SEED=5601]
COST:       about a minute per 600 trials.

RD (rule30_cloud_wheel_drift.py, CL043) found that forward kicks (+130,434 notches) and backward kicks (-130,133)
cancel to 0.2%. The owner compared this with matter and antimatter (2026-10-08): the laws allow both, yet the
universe kept a small excess of one. Sakharov's conditions (1967) say what an excess needs. There must be a process
that changes the count, the two kinds must be treated differently, and the system must be out of equilibrium. The
wheel already has the first two: kicks change its phase, and forward and backward kicks differ in rate, size and
class. So the third is the live question: does the balance fail out of equilibrium, early in a run?

RD summed each kick's signed residue kick_of(dn) in [-14, 13], which is a convention for a number known mod 28.
This probe measures the same thing without that convention. A hand derivation from RV2's gap reading (transients
use only visible gaps 2 and 4) gives a charge. Give each visible cell (column 1 at a white time) the charge
14 x - 3, so a 2-gap block 100 carries +5 and a 4-gap block 10000 carries -1. One turn of the wheel (five 4-gaps,
one 2-gap) is neutral. If the 2-gap arrives after m 4-gaps instead of 5, the kick is 5 - m notches, and the
charge of that stretch is also 5 - m. So the true lifted kick between two locks is the change in the level
lambda = Q(t) - Phi(j(t)), where Q is the running charge and Phi(j) is the wheel's own running charge at its
position j. Zero net kick is the same as visible density exactly 3/14 on the chains, five 4-gaps per 2-gap.
Locks and chains are as in RD: stretches of at least 56 steps on U, and locks less than 56 steps apart are joined.
Controls:
  RB-C1: lambda is constant inside every lock (by construction), and Phi(28) = 0 (the wheel is neutral).
  RB-C2: every chained kick satisfies delta lambda = kick_of(dn) (mod 28). Prediction: it holds for every kick
         (confidence 0.8). The number with delta lambda != kick_of(dn) counts kicks that RD's convention lifted
         wrongly. On RD's own seed (4256, 300 trials) this is reported beside RD's sum of +301.
PREDICTIONS (Cloud's, pushed before the first run; fresh seed 5601, 600 trials, T = 20000):
  RB-P1: the true net chained charge is consistent with zero: |z| < 2, with z = sum / sqrt(sum of squared
         per-trial sums). Confidence 0.65.
  RB-P2 (Sakharov's third condition): split the chained kicks by the time they happen. In the early window
         t < 1000 the drift differs from zero (|z| > 3); in the windows 1000 .. 5000 and 5000 .. T it does not
         (|z| < 2). Confidence 0.35 for the conjunction.
  Counterfactual: if the early window balances too, the balance is not an equilibrium effect of this kind. It
         would hold from the first kicks on, which points to a structural reason rather than a statistical one.
UNEXPECTED CHECK (the owner's note that antimatter falls the same way as matter, ALPHA-g, 2023): a backward kick is
  not repelled by the lock. The mean length of the lock that follows a forward kick equals that after a backward
  kick to within 10%. Confidence 0.4.
Also reported, without predictions: the true kick sizes, and the whole-run charge including off-wheel stretches.

OUTCOME, 2026-10-08 (by 16:00 BST; 28 s and 58 s). RD's seed 4256 (300 trials): RB-C1 PASS, and RB-C2 PASS with no
  kick lifted differently from kick_of, so RD's +301 is exact and not an artefact of its sign convention. Fresh seed
  5601 (600 trials, 139,972 chained kicks over 11,318,622 steps): RB-C1 PASS. RB-C2 FAILED by one kick, so its
  prediction is REFUTED by one. At t = 71 in trial 133 a transient holds a visible 1-gap (gaps 4, 1, 4, 4), where the
  charge and the phase disagree by 14 notches (delta lambda +4, kick_of -10). It is the first 1-gap seen inside a
  transient; RV2 saw none in 19,177. Every other kick satisfies the identity exactly.
  RB-P1 HELD: forward kicks total +257,339 notches and backward -256,497, net +842, z = +0.50, an offset of
  +2.7e-6 per step. RB-P2 REFUTED: the windows 0 .. 1000, 1000 .. 5000 and 5000 .. T give z = -0.45, +1.08 and +0.15.
  The counterfactual is the outcome. The balance holds from the first thousand steps, so it is not an equilibrium
  effect of this kind, and a structural reason is more likely than a statistical one. The unexpected check HELD:
  the lock after a forward kick lasts 81.0 steps on average and after a backward kick 79.0 (seed 4256: 80.7, 79.0).
  True kick sizes (seed 5601): forward +4: 43,107, +2: 27,568, +3: 3,067, +1: 2,546, +8: 1,868, +6: 408, +7: 47,
  +10: 17, +12: 11, +5: 1; backward -6: 19,973, -2: 14,612, -4: 13,952, -5: 8,188, -3: 3,040, -1: 1,567.
  Post-hoc, a lead and not a result: 87% of kicks are even. From the start of one 2-gap block to the next is
  6 + 10m steps for m 4-gaps between them, which is 0 mod 4 exactly when m is odd, and the kick is 5 - m. So an even
  kick keeps the 2-gap on its time class mod 4, and only the 13% of odd kicks move it.
WHAT "CONSISTENT WITH ZERO" MEANS (added 2026-10-08 16:08 BST, after the owner asked; the script now prints the
  spread): it is not a claim that the net is zero. The 600 independent runs give a spread of 1,670 notches for the
  net, so +842 is half a standard deviation, and a true drift of zero would give a net at least that large about 60%
  of the time. The run bounds the drift; it does not remove it. At about two standard deviations the net lies
  between -2,500 and +4,200 notches, an offset between -8e-6 and +1.3e-5 per step (+2.7e-6 +/- 5.3e-6). Anything
  smaller cannot be seen at this size. The error shrinks only as the square root of the steps, so measuring would
  need about 3e14 steps to resolve 1e-9 per step. Only a proof can say the balance is exact.
"""
import math
import os
import random
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_cloud_wheel_drift as rd                        # noqa: E402
sys.argv = _argv

P = 56
TRIALS = int(sys.argv[1]) if len(sys.argv) > 1 else 600
T = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 5601
WINDOWS = ((0, 1000), (1000, 5000), (5000, T))
rd.T = T

VIS = [rd.U[2 * j] for j in range(28)]                      # the wheel at white times
PHI = [0]
for x in VIS:
    PHI.append(PHI[-1] + 14 * x - 3)


def charge_prefix(c1):
    """Q[t]: the charge of column 1 at the white times before t."""
    q, out = 0, [0]
    for t, x in enumerate(c1):
        if t % 2 == 0:
            q += 14 * x - 3
        out.append(q)
    return out


def level(Q, t, d):
    return Q[t] - PHI[((t - d) % P) // 2]


def z_of(sums):
    tot = sum(sums)
    sd = math.sqrt(sum(s * s for s in sums))
    return tot, (tot / sd if sd else 0.0)


def main():
    rng = random.Random(SEED)
    c1_ok = PHI[28] == 0
    n_kicks = lifts = c2_bad = rd_sum = 0
    chained, whole, steps = [], [], 0
    win_sums = [[] for _ in WINDOWS]
    win_steps = [0] * len(WINDOWS)
    sizes = Counter()
    after = {1: [], -1: []}
    for i in range(TRIALS):
        w = (16, 24, 32, 48, 64)[i % 5]
        c1 = rd.column1(rng.getrandbits(w) | 1)
        Q = charge_prefix(c1)
        lk = rd.locks(c1)
        lams = []
        for a, s, d in lk:
            t0 = a + a % 2
            lam = level(Q, t0, d)
            c1_ok &= all(level(Q, t, d) == lam for t in range(t0, s + 1, 2))
            lams.append(lam)
        tsum, wsum = 0, [0] * len(WINDOWS)
        chain_start = None
        for j in range(len(lk)):
            a, s, d = lk[j]
            if chain_start is None:
                chain_start = a
            if j + 1 < len(lk) and lk[j + 1][0] - s < P:
                dl = lams[j + 1] - lams[j]
                k = rd.kick_of((lk[j + 1][2] - d) % P)
                n_kicks += 1
                c2_bad += (dl - k) % 28 != 0
                lifts += dl != k
                rd_sum += k
                tsum += dl
                sizes[dl] += 1
                for wi, (lo, hi) in enumerate(WINDOWS):
                    if lo <= s < hi:
                        wsum[wi] += dl
                if dl:
                    after[1 if dl > 0 else -1].append(lk[j + 1][1] - lk[j + 1][0])
                continue
            if s > chain_start + P:
                steps += s - chain_start
                for wi, (lo, hi) in enumerate(WINDOWS):
                    win_steps[wi] += max(0, min(s, hi) - max(chain_start, lo))
            chain_start = None
        chained.append(tsum)
        for wi in range(len(WINDOWS)):
            win_sums[wi].append(wsum[wi])
        if lams:
            whole.append(lams[-1] - lams[0])
    print(f"SEED {SEED}: {TRIALS} trials, T = {T}; {n_kicks} chained kicks over {steps} chained steps")
    print("RB-C1", "PASS" if c1_ok else "FAIL")
    print("RB-C2", "PASS" if not c2_bad else "FAIL", f"({c2_bad} kicks off mod 28; {lifts} lifted differently "
          f"from kick_of; RD-convention sum {rd_sum})")
    tot, z = z_of(chained)
    sd = tot / z if z else 0.0
    print(f"true net chained charge {tot} notches, z = {z:+.2f} (sd {sd:.0f}); rotation offset "
          f"{tot / (28 * steps) if steps else 0:+.2e} +/- {sd / (28 * steps) if steps else 0:.2e} per step")
    print("RB-P1", "HELD" if abs(z) < 2 else "REFUTED")
    zs = []
    for (lo, hi), ws, st in zip(WINDOWS, win_sums, win_steps):
        wt, wz = z_of(ws)
        zs.append(wz)
        print(f"  window {lo} .. {hi}: {st} chained steps, net {wt} notches, z = {wz:+.2f}")
    print("RB-P2", "HELD" if abs(zs[0]) > 3 and all(abs(x) < 2 for x in zs[1:]) else "REFUTED")
    print("true kick sizes:", dict(sorted(sizes.items())))
    mf = sum(after[1]) / max(1, len(after[1]))
    mb = sum(after[-1]) / max(1, len(after[-1]))
    print(f"lock after a forward kick: mean {mf:.1f} steps ({len(after[1])}); after a backward kick: "
          f"mean {mb:.1f} ({len(after[-1])})")
    print("unexpected check", "HELD" if abs(mf - mb) <= 0.1 * max(mf, mb) else "REFUTED")
    wt, wz = z_of(whole)
    print(f"whole-run charge, first lock to last (off-wheel stretches included): {wt} notches, z = {wz:+.2f}")


if __name__ == "__main__":
    main()
