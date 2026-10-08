#!/usr/bin/env python3
"""rule30_cloud_review_gc505.py: Cloud's independent replay of the finite claims in GPT's GC505 to GC546 (CL035).

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_review_gc505.py
COST:       under a minute.

The hand arguments of GC505 to GC548 were read line by line in CL035. This script checks their finite claims in
Cloud's own coding (rows are sets of black sites; no code shared with GPT's probes). Every check below is GPT's own
stated value or exhaustive statement, so each is a control that should PASS.
  R505: on all 512 initial patches on [-4, 4] with site 0 flipped, first displacements -1, 0, +1 occur 256, 128,
        128 times and the second update moves left in 128, 64, 128 of them (320 of 512).
  R506: on all 8192 patches on [-6, 6], history L1 = -1, L2 = 0 occurs 1280 times with next law {-1: 1}; L1 = 0,
        L2 = 0 occurs 512 times with {-1: 1/2, 0: 1/2}; L1 = 1, L2 = 0 occurs 2048 times with {-1: 1/2, 0: 3/16,
        1: 7/32, 2: 3/64, 3: 3/64}.
  R511: on the same patches, E[L_N] = -1/4, -35/64, -105/128 and E[F_N] = 1, 7/4, 5/2 for N = 1, 2, 3, with F_N
        the fresh ticks of GC509's exposure scheme; and F_N <= E_N <= 2 F_N with E_N the largest span (GC532).
  R521: in every one of those histories, a unit right jump at tick 1 or 2 is followed by a left move (GC521).
  R507: the rows {-1, 0} and {-1} + {1 .. N} differ after one update exactly at {N + 1}, for N = 1 .. 30 (GC507),
        and after it the front moves left at least floor(N / 2) times in a row, for N = 2 .. 30 (GC508).
  R523: the finite pairs ({-1} or {-1, 0}, site 0 flipped) have damage {t} at even t and {t - 1, t} at odd t,
        through t = 200 (GC523); the seeds {0} and {0, 1} have the same centre trace through t = 3000 (GC525).
  R524: with singleton damage at 0, n cycles of displacements 0, 2 occur exactly when sites -2, -1 are 0, 1 and
        sites 1 .. 4n - 1 are 0, for n = 1, 2, 3, on 4096 random backgrounds each plus the extreme cases (GC524).
  R529: seed {-2, -1, 2} with site 0 flipped gives damage {0, 1} with background triple 011 at -1, 0, 1, and
        disagreement at 0 after the next update, while each single replica agrees there (GC529).
  R544: the solid seed [-m, m] has centre prefix 1, 0^m, 1 for m = 1 .. 40 (GC544).
  R545: on 20,000 random finite rows at a black-to-white centre transition, the new left distance p equals the
        preceding left solid depth ell, and the new right distance q equals r + 1 + z (GC545, GC546); the hand
        controls {-2, -1, 0} -> {-3, -2, 1} and {-2, -1, 0, 2} -> {-3, -2, 2, 3} hold.
  R520: on 20,000 random finite rows with a white centre, the white run's length equals the first mismatch depth
        against Condrey's zero fibre (zeros before q, 1 at q, then j mod 2), and on ties p = q = m it equals m + d
        with d GC513's checkerboard depth at site -1 at time m - 1 (GC513, GC520).
  R542: GC542's indexed Champernowne bit equals direct concatenation for n = 1 .. 20,000.
PREDICTION (Cloud's, pushed before the first run; the block's unexpected check): on the singleton orbit, among the
  white-run starts s in 1 .. 4000, the fraction with p = q (resonant) lies within 0.05 of 1/3, the iid-ensemble value
  of GC515, and the mean white-run length lies within 0.15 of 2 (G97's ensemble mean). Confidence 0.6 for the first,
  0.7 for the second. GC515 and GC516 warn that the ensemble law has no proved transfer to the selected orbit; this
  tests whether the selected orbit looks like the ensemble in these two numbers, which would be evidence, not proof.
Counterfactual: a resonance fraction far from 1/3 would say the singleton's run starts are spatially atypical, which
  would make the resonant-tail target of GC517 more (or less) prominent there than the ensemble suggests.

OUTCOME, 2026-10-08 (by 12:59 BST; 17 s): every control R505 to R542 PASS (R524: 3,210 corridor cases; R545: 7,037
  transitions; R520: 19,998 rows, 6,661 ties; no mismatch anywhere). PREDICTION: mean white length 2.068, HELD; the
  resonant fraction is 0.2561 over 976 white starts, REFUTED. The reference value was wrong, not the orbit: GC515's 1/3
  conditions on a white centre at a fixed time, not on a run start. Post-hoc, so not a test: at a white start the
  preceding row u has u_0 = u_-1 = 1, and GC545-GC546 give p = ell, q = r + 1 + z. Under the fair ensemble ell >= 1
  has P(ell = k) = 2^-k, r >= 0 has P(r = j) = 2^-(j+1), z is fair, so P(q = 1) = 1/4, P(q = k) = 3 * 2^-(k+1) for
  k >= 2, and P(p = q) = (1/2)(1/4) + sum over k >= 2 of 3 * 2^-(2k+1) = 1/8 + 1/8 = 1/4.
PREDICTION 2 (Cloud's, written after the first run and pushed before this second run; --late): on fresh singleton
  times, white starts s in 4001 .. 20000, the resonant fraction lies within 0.03 of 1/4 and the mean white length
  within 0.1 of 2. Confidence 0.75 and 0.8. A miss would say the singleton's run starts are spatially atypical.
"""
import random
from collections import Counter
from fractions import Fraction


def step(black):
    if not black:
        return set()
    lo, hi = min(black) - 1, max(black) + 1
    return {i for i in range(lo, hi + 1) if ((i - 1) in black) ^ ((i in black) or ((i + 1) in black))}


def report(name, ok, detail=""):
    print(name, "PASS" if ok else "FAIL", detail)


def front(a, b):
    d = a ^ b
    return min(d) if d else None


def patch_histories(lo, hi, ticks):
    """All patches on [lo, hi]: first-copy rows and fronts through `ticks` updates, site 0 flipped in the copy."""
    out = []
    n = hi - lo + 1
    for m in range(1 << n):
        u = {lo + i for i in range(n) if m >> i & 1}
        v = u ^ {0}
        us, fr = [u], [0]
        for _ in range(ticks):
            u, v = step(u), step(v)
            us.append(u)
            fr.append(front(u, v))
        out.append((m, us, fr))
    return out


def r505():
    h = patch_histories(-4, 4, 2)
    first = Counter(fr[1] for _, _, fr in h)
    left = Counter(fr[1] for _, _, fr in h if fr[2] == fr[1] - 1)
    report("R505", first == {-1: 256, 0: 128, 1: 128} and left == {-1: 128, 0: 64, 1: 128},
           f"{dict(first)}, left at tick 2: {dict(left)}")


def r506_511_521():
    h = patch_histories(-6, 6, 3)
    groups = {}
    for _, _, fr in h:
        if fr[2] == 0:
            groups.setdefault(fr[1], Counter())[fr[3]] += 1
    law = {k: {x: Fraction(c, sum(v.values())) for x, c in v.items()} for k, v in groups.items()}
    sizes = {k: sum(v.values()) for k, v in groups.items()}
    ok506 = (sizes == {-1: 1280, 0: 512, 1: 2048} and law[-1] == {-1: 1} and law[0] == {-1: Fraction(1, 2),
             0: Fraction(1, 2)} and law[1] == {-1: Fraction(1, 2), 0: Fraction(3, 16), 1: Fraction(7, 32),
             2: Fraction(3, 64), 3: Fraction(3, 64)})
    report("R506", ok506, f"sizes {sizes}")
    meanL, meanF, spans_ok, rev_ok = [], [], True, True
    for N in (1, 2, 3):
        sL = sF = 0
        for _, _, fr in h:
            sL += fr[N]
            B, F = 0, 0
            for t in range(N):
                J = fr[t] - 1 - t
                if J < B:
                    F += 1
                B = min(B, J)
            E = max(t - fr[t] + 1 for t in range(N))
            spans_ok &= F <= E <= 2 * F and E == -B
            sF += F
        meanL.append(Fraction(sL, len(h)))
        meanF.append(Fraction(sF, len(h)))
    for _, _, fr in h:
        for t in (0, 1):
            if fr[t + 1] - fr[t] == 1:
                rev_ok &= fr[t + 2] - fr[t + 1] == -1
    report("R511", meanL == [Fraction(-1, 4), Fraction(-35, 64), Fraction(-105, 128)] and
           meanF == [1, Fraction(7, 4), Fraction(5, 2)] and spans_ok, f"E[L] {[str(x) for x in meanL]}, "
           f"E[F] {[str(x) for x in meanF]}")
    report("R521", rev_ok)


def r507():
    ok = True
    for N in range(1, 31):
        x, y = {-1, 0}, {-1} | set(range(1, N + 1))
        x1, y1 = step(x), step(y)
        ok &= (x1 ^ y1) == {N + 1}
        if N >= 2:
            fr = [N + 1]
            for _ in range(N // 2):
                x1, y1 = step(x1), step(y1)
                fr.append(front(x1, y1))
            ok &= fr == [N + 1 - s for s in range(N // 2 + 1)]
    report("R507", ok)


def r523():
    ok = True
    for u0 in ({-1}, {-1, 0}):
        u, v = set(u0), u0 ^ {0}
        for t in range(201):
            ok &= (u ^ v) == ({t} if t % 2 == 0 else {t - 1, t})
            u, v = step(u), step(v)
    a, b, same = {0}, {0, 1}, True
    for t in range(3001):
        same &= (0 in a) == (0 in b)
        a, b = step(a), step(b)
    report("R523", ok and same, "(seeds {0} and {0, 1}: same centre through t = 3000)" if same else "")


def r524(rng):
    bad, pos = 0, 0
    for n in (1, 2, 3):
        sites = range(-8, 4 * n + 6)
        corridor = {-2: 0, -1: 1, **{k: 0 for k in range(1, 4 * n)}}
        for trial in range(4096 + 1024):
            bg = {k for k in sites if rng.random() < 0.5}
            if trial >= 4096:                              # force the corridor, other bits random
                bg = {k for k in bg if k not in corridor} | {-1}
            want = all((k in bg) == bool(b) for k, b in corridor.items())
            pos += want
            u, v, disp, L = set(bg), bg ^ {0}, [], 0
            for _ in range(2 * n):
                u, v = step(u), step(v)
                f = front(u, v)
                disp.append(f - L)
                L = f
            bad += (disp == [0, 2] * n) != want
    report("R524", not bad, f"({pos} corridor cases, {bad} mismatches)")


def r529():
    u, v = {-2, -1, 2}, {-2, -1, 0, 2}
    u1, v1 = step(u), step(v)
    trip = tuple(int(i in u1) for i in (-1, 0, 1))
    u2, v2 = step(u1), step(v1)
    rep0, rep1 = step(u1 ^ {0}), step(u1 ^ {1})
    ok = (u1 ^ v1) == {0, 1} and trip == (0, 1, 1) and ((0 in u2) != (0 in v2)) and \
        ((0 in rep0) == (0 in u2)) and ((0 in rep1) == (0 in u2))
    report("R529", ok)


def r544():
    ok = True
    for m in range(1, 41):
        row, c = set(range(-m, m + 1)), []
        for _ in range(m + 2):
            c.append(int(0 in row))
            row = step(row)
        ok &= c == [1] + [0] * m + [1]
    report("R544", ok)


def distances(row):
    lefts = [i for i in row if i < 0]
    rights = [i for i in row if i > 0]
    p = -max(lefts) if lefts else None
    q = min(rights) if rights else None
    return p, q


def r545(rng):
    bad, seen = 0, 0
    for _ in range(20000):
        u = {i for i in range(-12, 13) if rng.random() < 0.6}
        if 0 not in u:
            continue
        v = step(u)
        if 0 in v:
            continue
        seen += 1
        ell = next(k for k in range(1, 30) if -k - 1 not in u) if -1 in u else 0
        r = next(k for k in range(0, 30) if k + 1 not in u)
        z = int(r + 2 in u)
        p, q = distances(v)
        bad += (p != ell) or (q != r + 1 + z)
    ok = not bad and seen > 1000 and step({-2, -1, 0}) == {-3, -2, 1} and step({-2, -1, 0, 2}) == {-3, -2, 2, 3}
    report("R545", ok, f"({seen} transitions, {bad} mismatches)")


def white_run(row, cap=200):
    for t in range(cap):
        if 0 in row:
            return t
        row = step(row)
    return None


def r520(rng):
    bad, ties, seen = 0, 0, 0
    for _ in range(20000):
        row = {i for i in range(-14, 15) if i != 0 and rng.random() < 0.5}
        p, q = distances(row)
        if p is None or q is None:
            continue
        seen += 1
        R = white_run(row)
        fib = lambda j: 0 if j < q else (1 if j == q else j % 2)
        mis = next((j for j in range(1, 40) if (int(-j in row)) != fib(j)), None)
        if mis is None:
            continue
        bad += R != mis
        if p == q:
            ties += 1
            s_row = row
            for _ in range(p - 1):
                s_row = step(s_row)
            ref = lambda k: 1 - k % 2                       # black at even depth from site -1
            d = next((k for k in range(0, 40) if int(-1 - k in s_row) != ref(k)), None)
            bad += d is None or R != p + d
    report("R520", not bad, f"({seen} rows, {ties} ties, {bad} mismatches)")


def r542():
    direct = "".join(bin(k)[2:] for k in range(1, 6000))

    def bit(n):
        k, S = 1, 0
        while (k - 1) * 2 ** k + 1 < n:
            S = (k - 1) * 2 ** k + 1
            k += 1
        a = n - S - 1
        q, r = divmod(a, k)
        return (2 ** (k - 1) + q) >> (k - 1 - r) & 1
    report("R542", all(bit(n) == int(direct[n - 1]) for n in range(1, 20001)))


def prediction():
    row, rows = {0}, []
    for _ in range(4400):
        rows.append(row)
        row = step(row)
    c = [int(0 in r) for r in rows]
    starts = [s for s in range(1, 4001) if c[s] == 0 and c[s - 1] == 1]
    res = sum(1 for s in starts if distances(rows[s])[0] == distances(rows[s])[1])
    lengths = []
    for s in starts:
        k = s
        while c[k] == 0:
            k += 1
        lengths.append(k - s)
    frac, mean = res / len(starts), sum(lengths) / len(lengths)
    print(f"PREDICTION: {len(starts)} white starts; resonant fraction {frac:.4f}",
          "HELD" if abs(frac - 1 / 3) <= 0.05 else "REFUTED", f"; mean white length {mean:.4f}",
          "HELD" if abs(mean - 2) <= 0.15 else "REFUTED")


def late(lo=4001, hi=20000):
    """PREDICTION 2: integer rows (bit k is site k - t), white starts in [lo, hi]."""
    row, c, starts, res = 1, [], [], 0
    for t in range(hi + 60):
        cbit = row >> t & 1
        c.append(cbit)
        if lo <= t <= hi and cbit == 0 and c[t - 1] == 1:
            starts.append(t)
            left = row & ((1 << t) - 1)
            right = row >> (t + 1)
            p = t - (left.bit_length() - 1) if left else None
            q = (right & -right).bit_length() if right else None
            res += p == q
        row = ((row << 2) ^ ((row << 1) | row)) & ((1 << (2 * t + 3)) - 1)
    lengths = []
    for s in starts:
        k = s
        while c[k] == 0:
            k += 1
        lengths.append(k - s)
    frac, mean = res / len(starts), sum(lengths) / len(lengths)
    print(f"PREDICTION 2: {len(starts)} white starts in {lo} .. {hi}; resonant fraction {frac:.4f}",
          "HELD" if abs(frac - 0.25) <= 0.03 else "REFUTED", f"; mean white length {mean:.4f}",
          "HELD" if abs(mean - 2) <= 0.1 else "REFUTED")


if __name__ == "__main__" and "--late" in __import__("sys").argv:
    late()
elif __name__ == "__main__":
    rng = random.Random(505)
    r505(); r506_511_521(); r507(); r523(); r524(rng); r529(); r544(); r545(rng); r520(rng); r542(); prediction()
