#!/usr/bin/env python3
"""rule30_wheel.py: the wheel of PRIZE-PROBLEMS.md section 8.4 up close. Between its slips, is column 1 an exact copy
of itself every 56 steps? Is the repeating word the same for every right half? Is a slip only a shift in time? Do the
left half's long zero runs sit inside the coherent stretches? And (the random-chaos step) do Rule 30's siblings turn a
wheel too?

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_wheel.py [W=12] [T=2048] [K=192]
COST:       a few minutes on one core.

Definitions. Column 1 (trace 0101..., every right half up to W cells, T steps) is cut into windows of 56 steps at
t = 0, 56, 112, ...; window k is an exact copy when it equals window k - 1 bit for bit. A stretch is a maximal run of
exact copies; its word is its first window, and two words are the same domain when one is a rotation (a shift in time)
of the other. A slip is the gap between two consecutive stretches of one column. Right halves whose column 1 becomes
exactly periodic (period dividing 56) are set aside as locked, as in rule30_rotation.py.

PREDICTIONS, written 2026-10-04 before this script's first run:
  Q1 (blind): at least 30% of the windows of the unlocked columns are exact copies.
  Q2 (blind): at least 70% of slips are shifts in time: the stretch after is a rotation of the stretch before.
  Q3 (blind): one domain word, up to rotation, covers at least 90% of all stretches over all right halves (a
     universal wheel, as Condrey's checkerboard is universal for the all-ones trace).
  Q4 (blind): the left half's zero runs of 14 or more cells (both sides exact, depth up to K, starting at depth 60 or
     more) lie, in column-1 time [s - 1, s + n - 2], inside an exact stretch (sigma(t) = sigma(t - 56) throughout) at
     least 1.5 times as often as all spans of the same length do.
  S  (the chaos step, blind): none of the siblings 90, 120, 150, 210 has its highest column-1 line (trace 0101...,
     0 < f < 1/2) within 0.002 of 0.3036. The wheel is Rule 30's own.
  K1 (known answer): a synthetic wheel (one random 56-step word, with a random time shift and 10 random bits flipped at
     about every 300th step) gives Q2 and Q3 at 100%, and an exact-copy share of at least 0.3 (each slip spoils about
     two windows of the 36, at about 7 slips per sequence).
  K2 (known answer): the same line-finder on Rule 30 itself puts the highest column-1 line within 0.002 of 0.3036.
  CF (counterfactual): with windows of 55 steps instead of 56, at most 2% of windows are exact copies.
REFUTED-BY: K1, K2 or CF failing (the instrument); Q1 to Q4 or S failing.

OUTCOME of the first run, 2026-10-04 (W = 12, T = 2048, K = 192): K1 (exact share 0.667, 668/668 slips are shifts, one
word), K2 (0.3036) and CF (0.0000) passed. 166 of 4,096 right halves were locked; 3,930 were unlocked.
  Q1 REFUTED: only 8.4% of windows are exact copies. The wheel is coherent but rarely exact for a whole period.
  Q2 HELD: 5,430 of 5,714 slips (95.0%) are shifts in time. The commonest shifts (steps, mod 56) are 16, 36, 52, 0,
     30, 20, 40 and 26, all even, in step with the trace.
  Q3 HELD: one word covers 96.6% of stretches, and there are only 2 words:
     U  = 00010011010001001101000100110100010011010001001101001101 (23 ones; five blocks 0001001101 and one 001101)
     U2 = 00010011001101000100110011010001001100110100010011001101 (24 ones), 3.4%.
     (CORRECTION, 2026-10-05: U2 has least period 14, being 00010011001101 four times. It is the period-14 lock seen
     temporarily in unlocked columns, not a second wheel; rule30_walls.py.)
  Q4 REFUTED, the other way round: 0 of 40 long runs lie inside an exact stretch, against a base rate of 0.389. The
     long zero runs sit next to slips.
  S HELD: Rules 90, 120 and 210 have their highest column-1 line at 1/2 and Rule 150 at 1/3; only Rule 30 turns the
     wheel (0.3036).
"""
import math, random, sys, pathlib

W = int(sys.argv[1]) if len(sys.argv) > 1 else 12
T = int(sys.argv[2]) if len(sys.argv) > 2 else 2048
K = int(sys.argv[3]) if len(sys.argv) > 3 else 192
P = 56

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_periodic as r30                          # noqa: E402
import rule30_twosided as ts                           # noqa: E402
import rule30_siblings as sib                          # noqa: E402
sys.argv = _argv
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def canon(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def locked(c):
    last_bad = max([t for t in range(len(c) - P) if c[t] != c[t + P]], default=-1)
    return last_bad < len(c) - P - 400


def stretches(c, p=P):
    """[(first window index, last window index, word)] for maximal runs of exact copies."""
    wins = [tuple(c[a:a + p]) for a in range(0, len(c) - p + 1, p)]
    out, k = [], 1
    while k < len(wins):
        if wins[k] == wins[k - 1]:
            j = k
            while j + 1 < len(wins) and wins[j + 1] == wins[j]:
                j += 1
            out.append((k - 1, j, wins[k - 1]))
            k = j + 1
        else:
            k += 1
    return out, len(wins) - 1


def analyse(cols, p=P):
    exact = total = 0
    words, slips, shifts = {}, [0, 0], {}
    for c in cols:
        st, n = stretches(c, p)
        total += n
        exact += sum(j - i for i, j, _ in st)
        for _, _, w in st:
            cw = canon(w)
            words[cw] = words.get(cw, 0) + 1
        for (_, _, a), (_, _, b) in zip(st, st[1:]):
            slips[1] += 1
            rot = [d for d in range(p) if b == a[-d:] + a[:-d] or (d == 0 and a == b)]
            if rot:
                slips[0] += 1
                shifts[rot[0]] = shifts.get(rot[0], 0) + 1
    top = max(words.values()) if words else 0
    return exact / total if total else 0.0, slips, (top / sum(words.values()) if words else 0.0), words, shifts


def synthetic(rng, n):
    word = [rng.getrandbits(1) for _ in range(P)]
    cols, expected = [], []
    for _ in range(n):
        c, off, t, slips = [], rng.randrange(P), 0, []
        while t < T:
            if t and rng.random() < 1 / 300:
                off = rng.randrange(P)
                slips.append(t)
            c.append(word[(t + off) % P])
            t += 1
        for t in slips:                                  # damage near each slip, as a defect would
            for _ in range(10):
                u = min(T - 1, t + rng.randrange(20))
                c[u] ^= 1
        cols.append(c)
    return cols


def col1_rule(code, R, n):
    g = sib.gfun(code)
    mask = (1 << (R.bit_length() + n + 3)) - 1
    row, out = R << 1, []
    for t in range(n):
        out.append((row >> 1) & 1)
        row = ((((row << 1) ^ g(row, row >> 1, mask)) & mask) & ~1) | ((t + 1) % 2)
    return out


def top_line(cols, n):
    M = n // 4
    agree, ones = [0] * (M + 1), 0
    for b in cols:
        x = sum(v << k for k, v in enumerate(b))
        ones += bin(x).count("1")
        for j in range(M + 1):
            agree[j] += n - j - bin((x ^ (x >> j)) & ((1 << (n - j)) - 1)).count("1")
    N = len(cols)
    mean = (2 * ones - N * n) / (N * n)
    C = [(2 * a - N * (n - j)) / (N * (n - j)) - mean * mean for j, a in enumerate(agree)]
    win = [(1 + math.cos(math.pi * j / (M + 1))) / 2 * C[j] for j in range(M + 1)]
    best = (0.0, -1e9)
    for i in range(1, 2500):
        f = i * 0.0002
        s = C[0] + 2 * sum(win[j] * math.cos(2 * math.pi * f * j) for j in range(1, M + 1))
        if s > best[1]:
            best = (f, s)
    return best


def main():
    rng = random.Random(56)
    syn = synthetic(rng, 200)
    share, slips, uni, _, _ = analyse(syn)
    report("K1 synthetic wheel: slips are shifts, one word, exact share near expected",
           slips[1] > 0 and slips[0] == slips[1] and uni == 1.0 and share >= 0.3,
           f"exact share {share:.3f}, slips that are shifts {slips[0]}/{slips[1]}, top word share {uni:.3f}")

    cols, free, nlock = [], [], 0
    for R in range(1 << W):
        c = ts.column1(R, (0, 1), T)
        if locked(c):
            nlock += 1
        else:
            cols.append(c)
            free.append(R)
    print(f"\n   column 1, trace 0101..., every right half up to {W} cells, {T} steps: {nlock} locked, "
          f"{len(cols)} unlocked", flush=True)
    share55 = analyse(cols, 55)[0]
    report("CF windows of 55 steps are almost never exact copies", share55 <= 0.02, f"share {share55:.4f}")
    share, slips, uni, words, shifts = analyse(cols)
    verdict("Q1 at least 30% of 56-step windows are exact copies", share >= 0.30, f"{share:.3f}")
    verdict("Q2 at least 70% of slips are shifts in time", slips[1] > 0 and slips[0] / slips[1] >= 0.70,
            f"{slips[0]} of {slips[1]}")
    verdict("Q3 one domain word covers at least 90% of stretches", uni >= 0.90,
            f"top word {uni:.3f}; {len(words)} distinct words")
    common = sorted(words.items(), key=lambda kv: -kv[1])[:3]
    for w, n in common:
        print(f"      domain word {''.join(map(str, w))}  x{n}  (ones: {sum(w)} of {P})")
    print("      slip shifts (steps, mod 56), commonest: "
          + ", ".join(f"{d}: {n}" for d, n in sorted(shifts.items(), key=lambda kv: -kv[1])[:8]))

    tau = [t % 2 for t in range(K + 1)]
    inside = spans = base_in = base_n = 0
    for R, c in zip(free, cols):
        good = [t >= P and c[t] == c[t - P] for t in range(K + 1)]
        L = r30.forced_left(R, tau, K)
        run = 0
        for k, b in enumerate(L, 1):            # a run still open at depth K is dropped
            if b == 0:
                run += 1
                continue
            if run >= 14:
                s, n = k - run, run
                if s >= 60:
                    spans += 1
                    inside += all(good[s - 1:s + n - 1])
            run = 0
        for s in range(60, K - 14):                       # the base rate: every span of 14 in the same window
            base_n += 1
            base_in += all(good[s - 1:s + 13])
    ratio = (inside / spans) / (base_in / base_n) if spans and base_in else float("nan")
    verdict("Q4 long zero runs sit inside exact stretches at least 1.5 times as often as any span",
            spans > 0 and ratio >= 1.5,
            f"{inside} of {spans} long runs inside, base rate {base_in / base_n:.3f}, ratio {ratio:.2f}")

    print("\n   the chaos step: the highest column-1 line of each sibling, trace 0101... (1024 right halves, 1024 steps)")
    near = []
    for rule in (90, 120, 150, 210, 30):
        code = next(c for c in range(16) if sib.rule_number(c) == rule)
        f, s = top_line([col1_rule(code, R, 1024) for R in range(1024)], 1024)
        print(f"      Rule {rule:>3}: highest line at f = {f:.4f}, S = {s:.2f}", flush=True)
        if rule != 30:
            near.append(abs(f - 0.3036) <= 0.002)
        else:
            report("K2 the line-finder puts Rule 30's own line within 0.002 of 0.3036", abs(f - 0.3036) <= 0.002,
                   f"{f:.4f}")
    verdict("S none of the siblings 90, 120, 150, 210 turns the 0.3036 wheel", not any(near),
            f"{sum(near)} of 4 near 0.3036")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
