#!/usr/bin/env python3
"""rule30_cloud_word_replication.py: does the word-bias candidate 111001000001 come back in fresh bits?

RUN-ON:     cpu (tilt.c via cc, Python 3 standard library; seeded). Delegated to Local (the M5), 2026-10-09.
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_word_replication.py [LOGN=23] [MT=24]
COST:       one Rule 30 column of 2^23 steps (about 20 minutes on one core of the cloud container, four times the
            2^22 column of rule30_cloud_word_bias.py), then a few minutes of counting; about 3 GB at peak.

The owner asked (2026-10-09) for the post-hoc candidate of rule30_cloud_word_bias.py to be tested, and for the run to
go to whoever has the most compute. That probe (predictions f708ae4, outcome ff0ada7) found no word bias in the single
seed's first 2^22 centre-column bits. One word stood out after the fact: the aligned 12-bit word 111001000001 was the
most frequent of 4,096, 65 and 68 times in the two halves against 42.7 each (133 against 85.3, z = +5.16,
p_top = 0.0044). Some 12-bit word reaching 65 in both halves has a chance of about 1 in 300 for fair coins, and 16
values of k were looked at, so it is a candidate, not a finding. The honest test is fresh data chosen in advance: the
next 2^22 bits, times 2^22 .. 2^23 - 1, which no one has looked at.
The fresh block is cut exactly as the first sample was: two halves of 2^21 bits, aligned k-bit words on each half's
own grid (times 2^22 + 12 j and 2^22 + 2^21 + 12 j for k = 12). "First" below means the first sample, times
0 .. 2^22 - 1, recounted here; "fresh" means times 2^22 .. 2^23 - 1.
Statistics (definitions as in rule30_cloud_word_bias.py): z of one word's count, (count - E) / sqrt(E (1 - 1/m)).
Z_cross at each k: S = sum_w e_w(first) e_w(fresh) over the whole samples, Z_cross = S / sqrt(m - 1), exactly mean 0 and
variance 1 for independent fair samples. L_cross: the longest word occurring both in the first sample and in the
fresh one; fair coins give about 2^(43 - L) such maximal repeats of length L or more, so L_cross is about 43.
Controls: MT pairs of independent 2^22-bit streams (seeds 9101 ..), for Z_cross and L_cross.

PREDICTIONS, written 2026-10-09 by 05:35 BST before this script's first run. Nothing beyond time 2^22 - 1 of the
single seed has been counted by anyone in this project for words; the first sample's numbers are the published ones.
Smoke test only: at LOGN = 18, whose bits all lie inside the published first sample, with 4 MT pairs (4 s). The
pipeline ran end to end, and RP-C1 failed there, as it must below LOGN = 23.
  RP-C1 (control, exact): the first 10^6 bits have Wolfram's black counts; the first sample reproduces the published
      run: 111001000001 is its most frequent aligned 12-bit word, with counts 65 and 68 in its halves.
  RP-C2 (control, calibration): over the MT pairs, Z_cross over k = 4 .. 16 has mean within 0.25 of 0 and standard
      deviation between 0.8 and 1.2.
  RP1 (blind; the candidate): in the fresh block, 111001000001 has z below +2.0 (count below about 104, E = 85.3).
      Confidence 0.9. The counterfactual: z at least +3 would say the word does re-occur, and would call for a third
      block before anything is claimed.
  RP2 (blind; the leaderboard across samples): of the first sample's 100 most frequent 12-bit words, the number
      above E in the fresh block lies between 35 and 62 (fair coins give about 49). Confidence 0.85.
  RP3 (blind; persistence across samples): |Z_cross| at most 3.3 at every k = 4 .. 16. Confidence 0.85.
  RP4 (blind; the fresh block alone, as WB1 to WB3): chi-square and p_top above 0.001 at every k = 1 .. 16, and
      |Z_split| at most 3.3 at every k = 4 .. 16. Confidence 0.8.
UNEXPECTED CHECK (not computed by anyone yet), RP5: the owner's "repetitions in batches" read across batches.
  L_cross lies within one bit of the MT pairs' range. Confidence 0.75.
REFUTED-BY: RP-C1 or RP-C2 failing (the instrument); RP1 to RP5 failing.
Instrument note, 2026-10-09 05:41 BST, after GPT's audit GC697 and before any full run (no prediction changed):
  longest_cross returns 0 when the two strings share no 36-bit window, which only says L_cross < 36. It is now
  printed as censored, and RP5 reads UNTESTED if the seed's value or any MT pair's is censored.
OUTCOME, 2026-10-09 05:50 BST (Local, the M5, one core for the column; 05:45 to 05:50; run at commit 06c0df5f;
LOGN 23, MT 24): ALL CHECKS PASS, and every prediction HELD.
  RP-C1 PASS: black counts 7, 52, 481, 5032, 50098, 500768; the first sample's top 12-bit word is 111001000001, with
      65 and 68 in its halves. RP-C2 PASS: 24 MT pairs, Z_cross mean -0.042, standard deviation 0.990.
  RP1 HELD: the candidate does not come back. In the fresh block it occurs 82 times against E = 85.3 (z -0.36); in
      the first sample it was 133 (z +5.16).
  RP2 HELD: 51 of the first sample's 100 most frequent 12-bit words are above E in the fresh block.
  RP3 HELD: the largest |Z_cross| over k = 4 .. 16 is 1.55 (k = 16). Every value lies inside its MT pairs' range.
  RP4 HELD: the fresh block's smallest chi-square p is 0.1168 (k = 12), its smallest p_top 0.1740 (k = 7), and its
      largest |Z_split| 2.49 (k = 4). p_top is an independence approximation, not a conservative bound (GPT GC698);
      at 0.17 against a threshold of 0.001 the label changes nothing.
  RP5 HELD (unexpected check): the longest word in both samples is 43 bits, at times 927246 and 5242951, against MT
      pairs 41 .. 50. Nothing was censored.
  Reading: the candidate was a post-hoc fluctuation. Over 2^23 centre-column bits there is still no word bias, no
  persistence across samples, and no excess shared repeat.
"""
import math, pathlib, random, subprocess, sys, tempfile
from concurrent.futures import ProcessPoolExecutor
from itertools import islice

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_cloud_word_bias as wb                           # noqa: E402
sys.argv = _argv

LOGN = int(sys.argv[1]) if len(sys.argv) > 1 else 23
MT = int(sys.argv[2]) if len(sys.argv) > 2 else 24
N = 1 << LOGN
H = N // 2                                                    # one sample: 2^(LOGN - 1) bits
KS, KL, TOP, K0 = wb.KS, wb.KL, wb.TOP, wb.K0
CAND = "111001000001"
EXE = str(pathlib.Path(tempfile.gettempdir()) / "rule30_word_replication_tilt")
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def sample_counts(s, k):
    """Counts of aligned k-bit words over a sample, each half on its own grid (as rule30_cloud_word_bias.py)."""
    h = len(s) // 2
    a, na = wb.counts(s[:h], k)
    b, nb = wb.counts(s[h:], k)
    return [x + y for x, y in zip(a, b)], na + nb


def z_cross(c1, n1, c2, n2, m):
    E1, E2 = n1 / m, n2 / m
    return sum((a - E1) * (b - E2) for a, b in zip(c1, c2)) / math.sqrt(E1 * E2) / math.sqrt(m - 1)


def windows(s):
    return {int(s[i:i + K0], 2) for i in range(len(s) - K0 + 1)}


def longest_cross(a, b):
    """The longest word occurring in both a and b (found through shared K0-bit windows, then extended)."""
    shared = windows(a) & windows(b)
    best = (0, -1, -1)
    for v in shared:
        pat = format(v, f"0{K0}b")
        pa, pb = [], []
        p = a.find(pat)
        while p >= 0:
            pa.append(p)
            p = a.find(pat, p + 1)
        p = b.find(pat)
        while p >= 0:
            pb.append(p)
            p = b.find(pat, p + 1)
        for p in pa:
            for q in pb:
                lft = 0
                while p - lft - 1 >= 0 and q - lft - 1 >= 0 and a[p - lft - 1] == b[q - lft - 1]:
                    lft += 1
                rgt = 0
                while p + K0 + rgt < len(a) and q + K0 + rgt < len(b) and a[p + K0 + rgt] == b[q + K0 + rgt]:
                    rgt += 1
                if K0 + lft + rgt > best[0]:
                    best = (K0 + lft + rgt, p - lft, q - lft)
    return best


def mt_pair(seed):
    a = format(random.Random(seed).getrandbits(H), f"0{H}b")
    b = format(random.Random(seed + 50000).getrandbits(H), f"0{H}b")
    zs = {}
    for k in KS:
        if k >= 4:
            m = 1 << k
            c1, n1 = sample_counts(a, k)
            c2, n2 = sample_counts(b, k)
            zs[k] = z_cross(c1, n1, c2, n2, m)
    return zs, longest_cross(a, b)[0]


def main():
    subprocess.run(["cc", "-O2", "-o", EXE, str(HERE / "tilt.c")], check=True)
    with ProcessPoolExecutor(max_workers=4) as ex:
        col = ex.submit(subprocess.run, [EXE, str(N), "0", "0"], check=True, capture_output=True)
        ctrl = list(ex.map(mt_pair, [9101 + j for j in range(MT)]))
        s = col.result().stdout.decode()
    first, fresh = s[:H], s[H:]
    want = {10: 7, 100: 52, 1000: 481, 10000: 5032, 100000: 50098, 1000000: 500768}
    got = {n: s[:n].count("1") for n in want if n <= N}
    c12a, _ = wb.counts(first[:H // 2], KL)
    c12b, _ = wb.counts(first[H // 2:], KL)
    tot = [x + y for x, y in zip(c12a, c12b)]
    top = max(range(1 << KL), key=lambda w: (tot[w], -w))
    w0 = int(CAND, 2)
    report("RP-C1 Wolfram's black counts, and the first sample reproduces the published run",
           got == {n: want[n] for n in got} and format(top, f"0{KL}b") == CAND and (c12a[w0], c12b[w0]) == (65, 68),
           f"black counts {list(got.values())}; first sample's top 12-bit word {format(top, f'0{KL}b')},"
           f" candidate counts {c12a[w0]}, {c12b[w0]}")
    zc = [z for zs, _ in ctrl for z in zs.values()]
    mz = sum(zc) / len(zc)
    sz = math.sqrt(sum((z - mz) ** 2 for z in zc) / (len(zc) - 1))
    report("RP-C2 the MT pairs are calibrated", abs(mz) <= 0.25 and 0.8 <= sz <= 1.2,
           f"{len(ctrl)} pairs; Z_cross mean {mz:+.3f}, standard deviation {sz:.3f}")
    m = 1 << KL
    cf, nf = sample_counts(fresh, KL)
    E = nf / m
    zcand = (cf[w0] - E) / math.sqrt(E * (1 - 1 / m))
    lead = sorted(range(m), key=lambda w: (-tot[w], w))[:TOP]
    nlead = sum(cf[w] > E for w in lead)
    print(f"\n   the candidate {CAND} in the fresh block: {cf[w0]} against E = {E:.1f} (z {zcand:+.2f});"
          f" in the first sample it was {tot[w0]} (z {(tot[w0] - E) / math.sqrt(E * (1 - 1 / m)):+.2f})")
    print(f"   the first sample's {TOP} most frequent {KL}-bit words: {nlead} above E in the fresh block")
    zx, fstats = {}, {}
    for k in KS:
        mk = 1 << k
        c1, n1 = sample_counts(first, k)
        c2, n2 = sample_counts(fresh, k)
        zx[k] = z_cross(c1, n1, c2, n2, mk)
        fstats[k] = wb.stats(fresh[:H // 2], fresh[H // 2:], k)
    print("    k   Z_cross [MT pairs]        fresh: chi-sq p  p_top   Z_split  top word")
    for k in KS:
        q = fstats[k]
        cz = [zs[k] for zs, _ in ctrl if k in zs]
        rng = f"[{min(cz):+.2f}, {max(cz):+.2f}]" if cz else "[k < 4]"
        print(f"   {k:2d}  {zx[k]:+7.2f} {rng:>17s}   {q['p_chi']:.4f}  {q['p_top']:.4f}  {q['z_split']:+7.2f}"
              f"  {q['top']}")
    L, pa, pb = longest_cross(first, fresh)
    Lc = sorted(l for _, l in ctrl)
    lab = lambda v: f"<{K0} (censored)" if v == 0 else str(v)     # 0 means no shared K0-bit window (GPT GC697)
    print(f"   the longest word in both samples: {lab(L)} bits" + (f", at times {pa} and {H + pb}" if L else "")
          + f"; MT pairs {lab(Lc[0])} .. {lab(Lc[-1])}: {[lab(v) for v in Lc]}")
    print()
    verdict("RP1 the candidate does not come back: z < +2.0 in the fresh block", zcand < 2.0, f"z {zcand:+.2f}")
    verdict("RP2 leaderboard across samples in [35, 62]", 35 <= nlead <= 62, f"{nlead}")
    zmax = max(abs(zx[k]) for k in KS if k >= 4)
    verdict("RP3 no persistence across samples: |Z_cross| <= 3.3 at k = 4 .. 16", zmax <= 3.3, f"largest {zmax:.2f}")
    ok4 = all(fstats[k]["p_chi"] > 0.001 and fstats[k]["p_top"] > 0.001 for k in KS) and \
        all(abs(fstats[k]["z_split"]) <= 3.3 for k in KS if k >= 4)
    verdict("RP4 the fresh block passes WB1 to WB3", ok4,
            f"smallest p_chi {min(fstats[k]['p_chi'] for k in KS):.4f}, smallest p_top"
            f" {min(fstats[k]['p_top'] for k in KS):.4f}")
    if L == 0 or Lc[0] == 0:
        print(f"UNTESTED  prediction RP5 (unexpected check): censored, L_cross {lab(L)} and MT pairs from {lab(Lc[0])}")
    else:
        verdict("RP5 (unexpected check) L_cross within one bit of the MT pairs' range", Lc[0] - 1 <= L <= Lc[-1] + 1,
                f"{L} against {Lc[0]} .. {Lc[-1]}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
