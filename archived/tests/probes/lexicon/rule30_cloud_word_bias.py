#!/usr/bin/env python3
"""rule30_cloud_word_bias.py: the owner's word-bias question. Do some words of Rule 30's centre column come up more
often than they should, and keep doing so?

RUN-ON:     cpu (tilt.c via cc for the Rule 30 columns, Python 3 standard library for the rest; seeded)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_word_bias.py [LOGN=22] [MT=24] [R30=3]
COST:       about seven minutes on four cores at LOGN = 22 (each Rule 30 column of 2^22 steps takes about five).

The owner (2026-10-09): "can we exploit this and find more ways in which the randomness breaks down. Perhaps look for
repetitions of encoded words, not in sequence but in batches over a sufficiently large sample size. Look for patterns
that re-occur in such a sample more than they should, suggesting bias towards those symbols."
What the record already has (PRIOR-ART.md, "The owner's PRNG question"; rule30_prng.py; rule30_tilt.py). The centre
column used alone passed every test tried here: a byte chi-square over 40,000 steps (P6), one stream's frequency and
4-step blocks, and no tilt or long memory over 2^21 steps (DFA exponent 0.5045). Rule 30's known failures as a
generator are of other uses: neighbouring columns are tied by the rule (x_(t+1)(i) XOR x_t(i-1) = x_t(i) OR x_t(i+1),
1 three times in four), rows of one run are not independent samples, and Meier and Staffelbach's key recovery is
cryptographic, not statistical. Nobody here has counted long words over a large sample, asked whether the
over-represented words stay over-represented, or looked for long repeated words.

The test. The single seed's centre column, N = 2^LOGN bits, cut into two halves. In each half, the aligned
non-overlapping k-bit words (the owner's "batches") are counted for k = 1 .. 16; m = 2^k words, E the expected count.
  - Batches: the whole sample's chi-square at each k, and the most frequent word's count, with p_top the chance that
    the largest of m fair counts is at least as high.
  - Persistence, the owner's "bias towards those symbols": e_w = (count - E) / sqrt(E) in each half, and
    S = sum_w e_w(half 1) e_w(half 2). If some words are favoured, they are high in both halves and S is large and
    positive; if a word is only high by chance in one half, the other half does not follow it. Under fair coins S has
    mean 0 and variance exactly m - 1 (the multinomial's standardised covariance is I - J/m, a projection), so
    Z_split = S / sqrt(m - 1). With equal halves, chi2(whole) = (chi2(half 1) + chi2(half 2)) / 2 + S exactly, so the
    persistence is precisely what the whole sample's chi-square gains over its halves' average.
  - The leaderboard: the 100 most frequent 12-bit words of half 1, and how many of them are above E in half 2.
  - Long repeats: every overlapping window of 36 bits; the colliding pairs, and the longest word that occurs twice.
    For fair coins about 2^(42 - L) maximal repeats of length L or more are expected at N = 2^22, so the longest
    repeat is about 42.
Controls. MT streams (Python's Mersenne Twister, seeds 9001 ..), and Rule 30 itself run from rows of fair coins
(tilt.c mode 1, seeds 1 ..). The second family is exactly fair, not just nearly: Rule 30 is left-permutive, so given
the cells x_0(1 .. T), the map from (x_0(0), x_0(-1), .., x_0(-T)) to the column (x_0(0), x_1(0), .., x_T(0)) is
triangular with x_0(-t) entering x_t(0) by XOR, a bijection. The column of a fair row is a run of fair coins
(standard; stated here because it makes the controls exact). One more MT stream carries a planted bias.

PREDICTIONS, written 2026-10-09 by 00:34 BST before this script's first run. Nothing has been run on the single seed
or on the controls below. The instrument was smoke-tested on MT seed 1 (not a control) and the planted stream, at
LOGN = 16 and 22: there the planted Z_split(12) was 9.24, and p_top was checked against 300 simulated maxima of
4,096 fair counts (1.3% below 0.01, 4.3% below 0.05, 47% below 0.5).
  WB-C1 (control, exact): the single seed's black counts after 10, 100, .., 10^6 steps are Wolfram's: 7, 52, 481,
      5,032, 50,098, 500,768.
  WB-C2 (control, exact): chi2(whole) = (chi2(half 1) + chi2(half 2)) / 2 + S on every stream at every k.
  WB-C3 (control, the planted bias): an MT stream in which 1.5% of the aligned 12-bit words of each half are replaced
      by a word drawn from a fixed set of 256. Each planted word is then only about 1.5 standard deviations high per
      half, so none stands out alone (some 270 of the 4,096 words are that high by chance), but Z_split at k = 12 is
      about 9 by the formula above. Passes if it is above 3.5.
  WB-C4 (control, calibration): over all the fair controls, the share of chi-square p-values below 0.01 and the share
      of p_top below 0.01, over k = 1 .. 16, are each at most 3%; Z_split over k = 4 .. 16 has mean within 0.25 of 0
      and standard deviation between 0.8 and 1.2.
  WB1 (blind; batches): the single seed's chi-square p-value is above 0.001 at every k = 1 .. 16. Confidence 0.85.
  WB2 (blind; no word re-occurs more than chance allows): p_top above 0.001 at every k = 1 .. 16. Confidence 0.85.
  WB3 (blind; the bias test): |Z_split| at most 3.3 at every k = 4 .. 16 (k = 1 .. 3 have few words and a heavy-tailed
      S, so WB1 covers them), and the leaderboard count lies between 35 and 62 (fair coins give about 48, standard
      deviation 5). Confidence 0.8.
UNEXPECTED CHECK (not computed by anyone yet), WB4: the single seed's longest repeated word is within one bit of the
  range of the fair controls' longest repeats. Confidence 0.75.
Counterfactual: if Rule 30's column favours some words, Z_split is large and positive at that k and at the longer
  k whose words contain them, and the leaderboard count is above 62. The planted control gives the scale. At this N
  the test sees, at k = 4, one word 2% more frequent than the rest; at k = 12, 256 words 14% more frequent; single
  rare words are better seen by p_top. A longest repeat well above the controls' would mean a stretch of the column
  that recurs, which a deterministic rule could produce and fair coins rarely do.
REFUTED-BY: WB-C1 to WB-C4 failing (the instrument); WB1 to WB4 failing.

OUTCOME of the first run, 2026-10-09 (00:33 to 00:43 BST, 9 min 52 s on four cores; a duplicate run started by
  mistake at 00:34 was stopped at 00:41 before it printed anything): ALL CHECKS PASS. WB-C1 PASS (7, 52, 481, 5,032,
  50,098, 500,768). WB-C2 PASS. WB-C3 PASS: the planted bias gives Z_split(12) = 9.24, as the formula said (chi-square
  z 14.0; 63 of the leaderboard's 100 were planted words, 76 above E in half 2). WB-C4 PASS: 27 fair streams, 1.2% of
  chi-square and p_top values below 0.01, Z_split mean +0.11 and standard deviation 0.975.
  WB1 HELD: smallest chi-square p = 0.010 (k = 11); 0.016 at k = 9, 0.024 at k = 14, all others above 0.4 or so.
  WB2 HELD: smallest p_top = 0.0044 (k = 12), from the word 111001000001, 133 times against 85.3 (z +5.16).
  WB3 HELD: largest |Z_split| at k = 4 .. 16 is 2.00 (k = 14; the controls' largest there +1.88); the leaderboard
  count is 53 (controls 44 .. 60, mean 50.9). The over-represented words of one half do not stay over-represented in
  the other, at any length from 4 to 16 bits.
  WB4 HELD (the unexpected check): the longest repeated word is 43 bits, at times 2,663,832 and 3,495,375 (controls
  40 .. 45, median 43); 124 pairs of equal 36-bit windows against 128.0 expected.
  So no word bias is seen at this scale. The one standout is 111001000001, high in both halves (65 and 68 against
  42.7). Post hoc, some 12-bit word reaching 65 in both halves has a chance of about 1 in 300 for fair coins, and the
  look across 16 values of k makes that unremarkable. It is a candidate to test in fresh bits (times 2^22 .. 2^23),
  not a finding.
Correction, 2026-10-09 05:47 BST (GPT GC698): the header of max_p said the independence formula "slightly overstates"
  the multinomial maximum's tail. It is the other way round: by negative association the true tail is at least the
  formula, so p_top can understate it. The smoke-test simulation above drew independent counts, so it checked the
  formula, not this dependence; WB-C4's fair multinomial controls (1.2% of p_top below 0.01) are the check that
  includes it. WB2 and RP4 test p_top > 0.001, and a larger true value only moves further above that line, so no
  verdict changes.
"""
import math, pathlib, random, subprocess, sys, tempfile
from concurrent.futures import ProcessPoolExecutor
from itertools import islice

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from rule30_prng import chi2_sf                                # noqa: E402

LOGN = int(sys.argv[1]) if len(sys.argv) > 1 else 22
MT = int(sys.argv[2]) if len(sys.argv) > 2 else 24
R30 = int(sys.argv[3]) if len(sys.argv) > 3 else 3
N = 1 << LOGN
KS = range(1, 17)
KL, TOP = 12, 100                                              # the leaderboard
K0 = 36                                                        # the repeat window
EPS, PLANT = 0.015, 256                                        # the planted bias
EXE = str(pathlib.Path(tempfile.gettempdir()) / "rule30_word_bias_tilt")
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def column(kind, seed):
    if kind == "mt":
        return format(random.Random(seed).getrandbits(N), f"0{N}b"), None
    if kind == "plant":
        rng = random.Random(seed)
        W = rng.sample(range(1 << KL), PLANT)
        s, out = format(rng.getrandbits(N), f"0{N}b"), []
        for half in (s[:N // 2], s[N // 2:]):                 # plant on each half's own grid of words
            n = len(half) // KL
            ch = [half[i * KL:(i + 1) * KL] for i in range(n)]
            for j in range(n):
                if rng.random() < EPS:
                    ch[j] = format(rng.choice(W), f"0{KL}b")
            out.append("".join(ch) + half[n * KL:])
        return "".join(out), set(W)
    mode = 0 if kind == "seed" else 1
    out = subprocess.run([EXE, str(N), str(mode), str(seed)], check=True, capture_output=True).stdout
    return out.decode(), None


def counts(s, k):
    c = [0] * (1 << k)
    for w in (s[i:i + k] for i in range(0, len(s) - k + 1, k)):
        c[int(w, 2)] += 1
    return c, len(s) // k


def max_p(c, n, m):
    """The chance that the largest of m fair counts (each binomial n, 1/m) is at least c, with the counts taken as
    independent: an approximation, and not a conservative one. Multinomial counts are negatively associated, so the
    true chance is at least this value; for n = 1, m = 2, c = 1 it is 1 against the formula's 3/4 (GPT GC698)."""
    p = 1 / m
    mu = n * p
    if mu > 2000:
        tail = 0.5 * math.erfc((c - 0.5 - mu) / math.sqrt(2 * mu * (1 - p)))
    else:
        lp, lq, lg = math.log(p), math.log1p(-p), math.lgamma(n + 1)
        tail, j = 0.0, c
        while j <= n:
            t = math.exp(lg - math.lgamma(j + 1) - math.lgamma(n - j + 1) + j * lp + (n - j) * lq)
            tail += t
            if j > mu and t < 1e-17 * tail:
                break
            j += 1
    if tail >= 1:
        return 1.0
    return -math.expm1(m * math.log1p(-tail))


def stats(h1, h2, k, planted=None):
    m = 1 << k
    c1, n1 = counts(h1, k)
    c2, n2 = counts(h2, k)
    n = n1 + n2
    E, E1, E2 = n / m, n1 / m, n2 / m
    c = [a + b for a, b in zip(c1, c2)]
    chi = sum((x - E) ** 2 for x in c) / E
    v1 = sum((a - E1) ** 2 for a in c1) / E1
    v2 = sum((b - E2) ** 2 for b in c2) / E2
    S = sum((a - E1) * (b - E2) for a, b in zip(c1, c2)) / math.sqrt(E1 * E2)
    top = max(range(m), key=lambda w: (c[w], -w))
    out = dict(chi=chi, p_chi=chi2_sf(chi, m - 1), z_chi=(chi - (m - 1)) / math.sqrt(2 * (m - 1)),
               ident=abs(chi - ((v1 + v2) / 2 + S)) <= 1e-9 * max(1.0, chi),
               top=format(top, f"0{k}b"), z_top=(c[top] - E) / math.sqrt(E * (1 - 1 / m)), p_top=max_p(c[top], n, m),
               z_split=S / math.sqrt(m - 1), r=S / math.sqrt(v1 * v2) if v1 * v2 > 0 else 0.0)
    if k == KL:
        lead = sorted(range(m), key=lambda w: (-c1[w], w))[:TOP]
        out["lead"] = sum(c2[w] > E2 for w in lead)
        if planted is not None:
            out["lead_planted"] = sum(w in planted for w in lead)
    if k in (8, 12):
        best = sorted(range(m), key=lambda w: (-c[w], w))[:5]
        out["top5"] = [(format(w, f"0{k}b"), c1[w], c2[w], (c[w] - E) / math.sqrt(E)) for w in best]
        out["E_half"] = E1
    return out


def longest_repeat(s):
    n = len(s) - K0 + 1
    ws = [int(s[i:i + K0], 2) for i in range(n)]
    ws.sort()
    dups = sorted({a for a, b in zip(ws, islice(ws, 1, None)) if a == b})
    del ws
    best, pairs = (0, 0, 0), 0
    for v in dups:
        pat = format(v, f"0{K0}b")
        pos, p = [], s.find(pat)
        while p >= 0:
            pos.append(p)
            p = s.find(pat, p + 1)
        pairs += len(pos) * (len(pos) - 1) // 2
        for a in range(len(pos)):
            for b in range(a + 1, len(pos)):
                p, q = pos[a], pos[b]
                lft = 0
                while p - lft - 1 >= 0 and s[p - lft - 1] == s[q - lft - 1]:
                    lft += 1
                rgt = 0
                while q + K0 + rgt < len(s) and s[p + K0 + rgt] == s[q + K0 + rgt]:
                    rgt += 1
                if K0 + lft + rgt > best[0]:
                    best = (K0 + lft + rgt, p - lft, q - lft)
    return dict(pairs=pairs, L=best[0], at=best[1:], word=s[best[1]:best[1] + best[0]] if best[0] else "")


def job(kind, seed):
    s, planted = column(kind, seed)
    h = len(s) // 2
    res = {k: stats(s[:h], s[h:], k, planted) for k in KS}
    res["rep"] = longest_repeat(s)
    if kind == "seed":
        res["black"] = {n: s[:n].count("1") for n in (10, 100, 1000, 10000, 100000, 1000000) if n <= N}
    return kind, seed, res


def main():
    subprocess.run(["cc", "-O2", "-o", EXE, str(HERE / "tilt.c")], check=True)
    jobs = [("seed", 0)] + [("r30", j + 1) for j in range(R30)] + [("plant", 4242)] + \
           [("mt", 9001 + j) for j in range(MT)]
    with ProcessPoolExecutor(max_workers=4) as ex:
        done = list(ex.map(job, *zip(*jobs)))
    seed = next(r for kind, _, r in done if kind == "seed")
    plant = next(r for kind, _, r in done if kind == "plant")
    ctrl = [(kind, sd, r) for kind, sd, r in done if kind in ("mt", "r30")]
    want = {10: 7, 100: 52, 1000: 481, 10000: 5032, 100000: 50098, 1000000: 500768}
    got = seed["black"]
    report("WB-C1 the single seed's black counts are Wolfram's", got == {n: want[n] for n in got},
           ", ".join(f"{n}: {c}" for n, c in got.items()))
    report("WB-C2 chi2(whole) = (chi2(half 1) + chi2(half 2)) / 2 + S on every stream and k",
           all(r[k]["ident"] for _, _, r in done for k in KS))
    report("WB-C3 the planted bias is caught: Z_split(12) > 3.5", plant[KL]["z_split"] > 3.5,
           f"Z_split {plant[KL]['z_split']:.2f}, chi-square z {plant[KL]['z_chi']:.2f}, leaderboard {plant[KL]['lead']}"
           f" of {TOP} ({plant[KL]['lead_planted']} of them planted words)")
    pc = [r[k]["p_chi"] for _, _, r in ctrl for k in KS]
    pt = [r[k]["p_top"] for _, _, r in ctrl for k in KS]
    zs = [r[k]["z_split"] for _, _, r in ctrl for k in KS if k >= 4]
    mz = sum(zs) / len(zs)
    sz = math.sqrt(sum((z - mz) ** 2 for z in zs) / (len(zs) - 1))
    fc, ft = sum(p < 0.01 for p in pc) / len(pc), sum(p < 0.01 for p in pt) / len(pt)
    report("WB-C4 the fair controls are calibrated", fc <= 0.03 and ft <= 0.03 and abs(mz) <= 0.25 and 0.8 <= sz <= 1.2,
           f"{len(ctrl)} streams; chi-square p < 0.01 in {fc:.3f}, p_top < 0.01 in {ft:.3f}; Z_split mean {mz:+.3f},"
           f" standard deviation {sz:.3f}")
    print("\n   the single seed, N = 2^%d; controls' range of Z_split in brackets" % LOGN)
    print("    k   chi-sq z   p_chi     top word            z_top   p_top    Z_split  [controls]       r")
    for k in KS:
        q = seed[k]
        cz = [r[k]["z_split"] for _, _, r in ctrl]
        print(f"   {k:2d}  {q['z_chi']:+8.2f}  {q['p_chi']:.4f}  {q['top']:>16s}  {q['z_top']:+6.2f}  {q['p_top']:.4f}"
              f"  {q['z_split']:+7.2f}  [{min(cz):+.2f}, {max(cz):+.2f}]  {q['r']:+.4f}")
    for k in (8, 12):
        print(f"   the five most frequent {k}-bit words (count in half 1, half 2; E = {seed[k]['E_half']:.1f} per half;"
              " z over the whole sample): " + "; ".join(f"{w} {a}, {b} ({z:+.2f})" for w, a, b, z in seed[k]["top5"]))
    lc = [r[KL]["lead"] for _, _, r in ctrl]
    print(f"   leaderboard: of half 1's {TOP} most frequent {KL}-bit words, {seed[KL]['lead']} are above E in half 2"
          f" (controls {min(lc)} .. {max(lc)}, mean {sum(lc) / len(lc):.1f})")
    rp, Lc = seed["rep"], [r["rep"]["L"] for _, _, r in ctrl]
    pr = [r["rep"]["pairs"] for _, _, r in ctrl]
    nw = N - K0 + 1
    ex = nw * (nw - 1) / 2 / 2 ** K0
    print(f"   long repeats: {rp['pairs']} pairs of equal {K0}-bit windows (fair coins expect {ex:.1f};"
          f" controls {min(pr)} .. {max(pr)}); longest repeated word {rp['L']} bits, at {rp['at'][0]} and {rp['at'][1]}"
          f" ({rp['word']}); controls' longest {min(Lc)} .. {max(Lc)}: {sorted(Lc)}")
    print(f"   the planted stream's longest repeat {plant['rep']['L']}; by kind, controls' Z_split at 12: "
          + ", ".join(f"{kind}{sd} {r[KL]['z_split']:+.2f}" for kind, sd, r in ctrl if kind == "r30"))
    print()
    verdict("WB1 batches: chi-square p > 0.001 at every k", all(seed[k]["p_chi"] > 0.001 for k in KS),
            f"smallest {min(seed[k]['p_chi'] for k in KS):.4f}")
    verdict("WB2 no word re-occurs more than chance allows: p_top > 0.001 at every k",
            all(seed[k]["p_top"] > 0.001 for k in KS), f"smallest {min(seed[k]['p_top'] for k in KS):.4f}")
    zmax = max(abs(seed[k]["z_split"]) for k in KS if k >= 4)
    verdict("WB3 no persistent bias: |Z_split| <= 3.3 at k = 4 .. 16, leaderboard in [35, 62]",
            zmax <= 3.3 and 35 <= seed[KL]["lead"] <= 62,
            f"largest |Z_split| {zmax:.2f}, leaderboard {seed[KL]['lead']}")
    verdict("WB4 (unexpected check) the longest repeat is within one bit of the controls' range",
            min(Lc) - 1 <= rp["L"] <= max(Lc) + 1, f"{rp['L']} against {min(Lc)} .. {max(Lc)}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
