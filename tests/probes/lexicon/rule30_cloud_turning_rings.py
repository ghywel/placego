#!/usr/bin/env python3
"""rule30_cloud_turning_rings.py: Rule 30 rows that turn rigidly (F^p x = shift^s x), their walls, and damage on them.

RUN-ON:     cpu (turning_rings.c via cc, driven from Python 3 with the standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_turning_rings.py [LMAX=28] [OUT=<tmp>/rule30_turning_rings]
            (a third argument "nodamage" skips the damage runs; used only for the smoke test)
COST:       a few minutes on four cores and about 2 GB of memory at LMAX = 28. Data goes to OUT, outside git.

Why (the owner, 2026-10-09, after CL071). One Rule 30 update turns GC686's 84-cell all-S ring by 14 sites. The owner
asked to explore rows that turn, and to come back to "a unit vector in a space-time picture is a velocity; the arrows
carry information only if the data, not the layout, chooses where they point". A turning row gives exactly such an
arrow: its space-time is constant along the vector (s, p), a pattern velocity s / p chosen by the row. Rule 30's own
signal speeds are already in the record and are not re-measured here as such: a difference's right edge moves at
exactly +1 (left-permutivity, PROOFS C4), its left edge at about 0.246 on random rows and -0.388 on the checkerboard
(CONSTELLATION row 3, Local's rule30_damage_speed.py; GPT GC505 to GC509; Baetens and Gravner).
Conventions: x(i) is site i, site i + 1 the right neighbour, F(x)(i) = x(i-1) XOR (x(i) OR x(i+1)),
shift^s x (i) = x(i - s), so s > 0 moves the pattern right.

Lemma TR (Cloud, by hand; elementary, and of the kind Boyle and Lee's Remark 2.1 describes for permutive maps, so
not claimed new). Let p >= 1 and |s| > p.
  (a) Every x on the whole line with F^p x = shift^s x is spatially periodic, and there are finitely many.
      Proof. F^p(x)(i) depends on x(i-p .. i+p) and equals x(i-s), which lies outside that window. If s > p, then
      x(m) = G(x(m+s-p) .. x(m+s+p)), so the window W_m = x(m+1 .. m+s+p) fixes W_{m-1}: W_{m-1} = T(W_m) for a map
      T on the 2^(s+p) windows. For every j >= 0, W_m = T^j(W_{m+j}) lies in T^j of the whole set, and on a finite
      set those images shrink to the periodic points of T. So every W_m is T-periodic, T is a bijection on its
      periodic points, and x is periodic with least period the length of W_0's cycle. If s < -p the same holds
      rightwards. Conversely every cycle of T gives such an x. QED.
  (b) If s < -p, T is a bijection, so there are exactly 2^(|s|+p) such x: every window of |s| + p cells extends to
      exactly one row that moves left |s| cells every p steps.
      Proof. F^p is left-permutive: F^p(x)(i) = x(i-p) XOR H(x(i-p+1 .. i+p)). Moving right, T drops the window's
      leftmost cell x(n-|s|-p) and appends x(n) = x(n-|s|-p) XOR H(..), where H reads only cells still in the new
      window (n - |s| + p <= n - 1). So the dropped cell is recovered from the new window. QED.
      For s > p, T drops the rightmost cell, which Rule 30 reads through the OR, and T is not injective.
So rows that outrun light leftwards are as many as there are windows, and rows that outrun it rightwards are rare.
GC686's ring is both. On its own ring it moves +14 per step, which is the same as -70.

Smoke test, disclosed, before these predictions: brute 12 and the census at |s| + p <= 12 (below GC686's ring, at
L = 15). Census and brute force agreed by eye. Every s < -p run had all 2^L windows periodic, which is how (b) was
noticed before it was proved. For s > p the periodic points were 3, 6, 3, 15, 31, 35, 85, 61, 60, 246 at p = 1,
L = 3 .. 12, in 2 to 7 cycles (p = 2 and 3 similar). No turning row there had an alternating column at all.
Instrument check, disclosed: "census 1 14" alone, read only for GC686's ring. It is found (N = 84) with six all-S
walls 14 sites apart, as the rotation implies; the driver's TC2 test was then corrected to compare up to rotation.
Nothing else in that output was read.

PREDICTIONS, written 2026-10-09 by 08:05 BST, before the full run (LMAX = 28; p = 1, 2, 3; p < |s|, |s| + p <= 28).
  TC1 (control, exact). Every census row satisfies F^p x = shift^s x on its ring, checked directly. For every (p, s)
      and every N <= 20, the census rows of least period N are exactly the brute-force rows with F^p x =
      shift^(s mod N) x.
  TC2 (control). GC686's ring 0x688eb74a45efb082671ee is found at p = 1, s = 14 with N = 84, and site 0 is an all-S
      wall in marker form.
  TC3 (Lemma TR(b), noticed in the smoke test, proved, now checked). For every s < -p, all 2^(|s|+p) windows are
      periodic.
  TC4 (blind). For s > p, T behaves like a random map. At every L = |s| + p from 16 to 28, log2(periodic points) is
      within 2.5 of log2 sqrt(pi 2^L / 2) (8.33 at L = 16, 14.33 at L = 28), and no run has more than 20 cycles.
      Confidence 0.6.
  TC5 (control by theory). Every all-S wall found is GC686's ring, up to rotation. Argument: an all-S turning row has
      every column 6-periodic, because columns 0 and 1 are (GC704 carries period 6 to every left column) and column
      i + s is column i shifted by p in time. So it lies in GC687's domain, with GC688's entrance. GC687 fixes its
      right half and L372's decoding its left half. This cross-checks GC687's exhaustive certificate on new data.
  TC6 (blind). No wall in the census has an L gap: no mixed S/L or all-L word appears. Confidence 0.7.
      Counterfactual: a mixed witness would be the first infinite physical trace with mixed S/L choice (portfolio
      question 4), to be replayed by direct simulation and sent for a second reading.
  TC7 (cross-check of GC625 and GC626). Every wall whose visible gaps are all 3 or 5 is in marker form: its full
      column-1 word is a cyclic concatenation of 110100 and 1101000100. Confidence 0.9; a failure means GC626 or this
      instrument is wrong.
  DV1 (control, PROOFS C4). On every background and flip, the rightmost difference is at the flip site + T at time T.
  DV2 (blind). On GC686's ring (T = 4096, all 84 flip sites), the left damage front moves left at a mean speed in
      [0.10, 0.40]. Confidence 0.6. Counterfactual: <= 0, healing from the left like the checkerboard.
  DV3 (blind). On GC686's ring the 84 flip sites' speeds lie within 0.04 of each other, so the speed belongs to the
      background, not to where the error is made. Confidence 0.5.
  DV4 (blind; the owner's velocity question). Pattern speed is not signal speed. Across up to 200 distinct turning
      rows with p = 1 and N <= 1024 (T = 2048, 8 flips each), the Spearman correlation between the left damage speed
      and the pattern speed |s*| has |rho| < 0.25. Here s* is the speed on the row's own ring, taken in (-N/2, N/2].
      Confidence 0.6. Counterfactual: |rho| > 0.4.
  DV5 (blind). That sample's median left speed lies in [0.15, 0.30], near the random row's 0.246. Confidence 0.5.
UNEXPECTED CHECK, TC8: for s > p, the largest cycle holds between 45% and 80% of the periodic points, averaged over
  the runs with L = 16 .. 28. (Random maps: the cyclic points form a random permutation, whose largest cycle holds
  about 62% on average.) Confidence 0.6.
REFUTED-BY: TC1, TC2, TC3, TC5 or DV1 failing (instrument or theory); TC4, TC6, TC7, TC8 or DV2 to DV5 failing as
  worded.
"""
import math, os, pathlib, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 28
OUT = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path(tempfile.gettempdir()) / "rule30_turning_rings"
NB = 20
NODAMAGE = len(sys.argv) > 3 and sys.argv[3] == "nodamage"
GC686 = 0x688eb74a45efb082671ee


def least_rotation(s):
    """Booth's algorithm: the lexicographically least rotation of s."""
    s2, f, k = s + s, [-1] * (2 * len(s)), 0
    for j in range(1, len(s2)):
        i = f[j - k - 1]
        while i != -1 and s2[j] != s2[k + i + 1]:
            if s2[j] < s2[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if i == -1 and s2[j] != s2[k + i + 1]:
            if s2[j] < s2[k]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return s2[k:k + len(s)]


def fields(line):
    return dict(kv.split("=", 1) for kv in line.split()[1:])


def spearman(a, b):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(v):
            j = i
            while j + 1 < len(v) and v[order[j + 1]] == v[order[i]]:
                j += 1
            for q in range(i, j + 1):
                r[order[q]] = (i + j) / 2
            i = j + 1
        return r
    ra, rb = ranks(a), ranks(b)
    ma, mb = sum(ra) / len(ra), sum(rb) / len(rb)
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = math.sqrt(sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb))
    return num / den if den else 0.0


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    exe = OUT / "turning_rings"
    subprocess.run(["cc", "-O2", "-o", str(exe), str(HERE / "turning_rings.c")], check=True)
    jobs = [(p, s) for p in (1, 2, 3) for s in range(-(LMAX - p), LMAX - p + 1) if abs(s) > p]
    jobs.sort(key=lambda j: -(abs(j[1]) + j[0]))

    def run(job):
        p, s = job
        f = OUT / f"census_p{p}_s{s}.txt"
        with open(f, "w") as fh:
            subprocess.run([str(exe), "census", str(p), str(s), str(NB)], stdout=fh, check=True)
        return job, f
    with open(OUT / "brute.txt", "w") as fh:
        subprocess.run([str(exe), "brute", str(NB)], stdout=fh, check=True)
    with ThreadPoolExecutor(3) as ex:
        files = dict(ex.map(run, jobs))

    bru = {}
    for line in open(OUT / "brute.txt"):
        d = fields(line)
        bru.setdefault((int(d["N"]), int(d["q"]), int(d["r"])), set()).add(int(d["canon"]))
    tc1 = tc3 = True
    sums, wits, bits = {}, [], {}
    for (p, s), f in files.items():
        can = {}
        for line in open(f):
            tag = line.split(" ", 1)[0]
            if tag == "FAIL":
                tc1 = False
                print(line.strip())
            elif tag == "SUM":
                sums[(p, s)] = {k: int(v) for k, v in fields(line).items()}
            elif tag == "CAN":
                d = fields(line)
                can.setdefault(int(d["N"]), set()).add(int(d["canon"]))
            elif tag == "WIT":
                d = fields(line)
                wits.append(d)
            elif tag == "BITS":
                d = fields(line)
                key = least_rotation(d["bits"])
                bits.setdefault(key, (int(d["N"]), int(d["su"])))
        for N in range(1, NB + 1):
            if can.get(N, set()) != bru.get((N, p, s % N), set()):
                tc1 = False
                print(f"TC1 mismatch p={p} s={s} N={N}: census {sorted(can.get(N, set()))[:5]} "
                      f"brute {sorted(bru.get((N, p, s % N), set()))[:5]}")
        if s < 0 and sums[(p, s)]["perpts"] != 1 << (abs(s) + p):
            tc3 = False
    print(f"TC1 {'PASS' if tc1 else 'FAIL'}: direct relation on every census row; census = brute force at N <= {NB}")
    print(f"TC3 {'PASS' if tc3 else 'FAIL'}: every s < -p run has all 2^L windows periodic")

    # TC4 and TC8: the right-moving runs against the random-map heuristic
    tc4, fr = True, []
    print("right-moving runs (s > p): L, p, s, cycles, log2 periodic points, minus log2 sqrt(pi 2^L / 2), max share")
    for (p, s), d in sorted(sums.items(), key=lambda kv: (kv[1]["L"], kv[0])):
        if s < 0 or d["L"] < 16:
            continue
        ref = math.log2(math.sqrt(math.pi * 2 ** d["L"] / 2))
        lp = math.log2(d["perpts"])
        share = d["maxN"] / d["perpts"]
        fr.append(share)
        if abs(lp - ref) > 2.5 or d["cycles"] > 20:
            tc4 = False
        print(f"  L={d['L']:2d} p={p} s={s:3d} cycles={d['cycles']:3d} log2P={lp:6.2f} diff={lp - ref:+5.2f} "
              f"share={share:.3f}")
    print(f"TC4 {'HELD' if tc4 else 'REFUTED'}")
    mshare = sum(fr) / len(fr) if fr else float("nan")
    print(f"TC8 {'HELD' if 0.45 <= mshare <= 0.80 else 'REFUTED'}: mean largest-cycle share {mshare:.3f}")

    # walls
    gc = "".join(str((GC686 >> i) & 1) for i in range(84))
    gck = least_rotation(gc)
    alls, mixed, vis_unmarked, tc2 = [], [], [], False
    for d in wits:
        nS, nL, mark = int(d["nS"]), int(d["nL"]), int(d["marker"])
        if not mark:
            vis_unmarked.append(d)
        if nL:
            mixed.append(d)
        elif mark:
            alls.append(d)
        j, b = int(d["j"]), d["bits"]
        if int(d["p"]) == 1 and int(d["s"]) == 14 and b[j:] + b[:j] == gc and mark and not nL:
            tc2 = True                                       # the wall at GC686's site 0
    print(f"walls with an S/L neighbour: {len(wits)} (all-S {len(alls)}, with an L gap {len(mixed)}, "
          f"not in marker form {len(vis_unmarked)})")
    print(f"TC2 {'PASS' if tc2 else 'FAIL'}: GC686's ring at p = 1, s = 14, site 0 an all-S wall in marker form")
    tc5 = all(least_rotation(d["bits"]) == gck for d in alls)
    print(f"TC5 {'PASS' if tc5 else 'FAIL'}: every all-S wall is GC686's ring up to rotation "
          f"({len({least_rotation(d['bits']) for d in alls})} distinct ring(s))")
    print(f"TC6 {'HELD' if not mixed else 'REFUTED'}")
    for d in mixed[:10]:
        print(f"  mixed: p={d['p']} s={d['s']} N={d['N']} j={d['j']} gaps={d['gaps']} bits={d['bits'][:200]}")
    print(f"TC7 {'HELD' if not vis_unmarked else 'REFUTED'}")
    for d in vis_unmarked[:10]:
        print(f"  unmarked: p={d['p']} s={d['s']} N={d['N']} j={d['j']} gaps={d['gaps']}")
    nwall = sum(d["nwall"] for d in sums.values())
    print(f"alternating columns (walls) in all runs, with repeats across runs: {nwall}")

    if NODAMAGE:
        return
    # damage: GC686's ring with every flip site, then a sample of distinct p = 1 rows
    def damage(lines, T, nf):
        r = subprocess.run([str(exe), "damage", str(T), str(nf)], input="".join(lines), capture_output=True,
                           text=True, check=True)
        return [fields(l) for l in r.stdout.splitlines() if l.startswith("DV")]
    g = damage([f"DMG 0 1 14 84 {gc}\n"], 4096, 84)[0]
    print(f"GC686 ring: left speed mean {g['mean']} min {g['min']} max {g['max']} (T = 4096, 84 flips), "
          f"right edge exact: {g['rightok'] == '1'}")
    dv2 = 0.10 <= float(g["mean"]) <= 0.40
    dv3 = float(g["max"]) - float(g["min"]) <= 0.04
    keys = sorted(bits)
    step = max(1, len(keys) // 200)
    sample = keys[::step][:200]
    lines = [f"DMG {i} 1 {bits[k][1]} {bits[k][0]} {k}\n" for i, k in enumerate(sample)]
    res = damage(lines, 2048, 8)
    sp = [float(d["mean"]) for d in res]
    ps = [abs(bits[sample[int(d["id"])]][1]) for d in res]
    rho = spearman(sp, ps)
    med = sorted(sp)[len(sp) // 2]
    dv1 = g["rightok"] == "1" and all(d["rightok"] == "1" for d in res)
    print(f"sample: {len(res)} distinct rows of {len(keys)} (N <= 1024), median left speed {med:.4f}, "
          f"min {min(sp):.4f}, max {max(sp):.4f}, Spearman rho with |s*| {rho:+.3f}")
    with open(OUT / "damage_sample.txt", "w") as fh:
        for d, v in zip(res, ps):
            fh.write(f"{d['id']} N={d['N']} |s*|={v} mean={d['mean']} min={d['min']} max={d['max']}\n")
    print(f"DV1 {'PASS' if dv1 else 'FAIL'}")
    print(f"DV2 {'HELD' if dv2 else 'REFUTED'}")
    print(f"DV3 {'HELD' if dv3 else 'REFUTED'}")
    print(f"DV4 {'HELD' if abs(rho) < 0.25 else 'REFUTED'}")
    print(f"DV5 {'HELD' if 0.15 <= med <= 0.30 else 'REFUTED'}")
    print(f"data in {OUT}")


if __name__ == "__main__":
    main()
