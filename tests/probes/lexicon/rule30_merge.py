#!/usr/bin/env python3
"""rule30_merge.py: do the forced walks of lead 1 merge, and do the merges set the record law R(d) ~ 0.8 d?

RUN-ON:     cpu (pure Python 3, standard library; records.c for the controls)
COMMAND:    python3 tests/probes/lexicon/rule30_merge.py [DMAX=45]
COST:       about a minute and under 1 GB at DMAX = 45 (the depth 65 witnesses: records.c, minutes, if not cached).

Background (PRIZE-PROBLEMS.md sections 8.36 to 8.38; rule30_influence.py). For column 0 = 0101..., a prefix of
column 1 (its free bits at times 0, 2, .., d - 3) fixes one forced walk from depth d. The record R(d) is the longest
zero run over every prefix. Under the coin model 2^(d/2) independent walks give R ~ d; the records give 0.8 d.
rule30_influence.py found single late bits re-randomise the run (influence 2/3, the coin value), and only a few early
bits are weak. Its reading: a cell at time t depends only on column 1 at times t and later, so the bit at time 2i can
change only rows 0 .. 2i. Its damage drifts down that strip as it moves left (it passes x_{t+1}(i) -> x_t(i-1) through
the XOR every time, and along a row only through an OR whose other input is 0), so it dies within a distance that
grows with the strip. Two prefixes whose difference has died reach the same walk state, and from then on they are
one walk: a merge.
The walk state at depth k is the pair (A_{k-1}, A_{k-2}). Its canonical form masks the bits of A_{k-2} that an OR
shields: A_k's input is (A_{k-1} << 1) | (A_{k-2} << 2), so A_{k-2}[j] is unseen wherever A_{k-1}[j + 1] = 1. Two
states with one canonical form have one future (exact). D(d) counts the canonical states at depth d over all
prefixes, delta(d) = nfree(d) - log2 D(d) the bits lost to merges before the run; among the prefixes still in a zero
run after l cells, S_l counts prefixes and D_l distinct canonical states (merges inside the run).

PREDICTIONS, written 2026-10-05 before this script's first run. Seen before: the records R(d) and their prefix
counts; RC3's tail slopes (0.513 and 0.481 bits per cell at depths 57 and 65); the histograms at depths 21 and 25
(rule30_influence.py); the influences of rule30_influence.py. Not seen: any count of states or merges, and any record
witness (W line) beyond RC5's comparison of the first witnesses at d and 2d for d = 21 .. 30.
  MG0 (controls, must hold): (a) an independent simulator (the left-parent rule, cell by cell) gives row 0 equal to
      the diagonals' cells, and flipping column 1 at time 2i changes no cell above row 2i but some cell at or below
      it; (b) flipping a shielded bit of A_{k-2} never changes the walk, and flipping an unshielded one does in at
      least 30% of trials (the counterfactual); (c) the merged frontier, its multiplicities as weights, gives
      records.c's record and every H line at each odd depth from 21 to DMAX.
  MG1 (blind; merges before the run): 1 <= delta(d) <= 5 at every odd d from 21 to DMAX, and delta grows by 1 to 3
      from depth 21 to 45 (linear in d, about 0.075 per unit depth, as the strip picture gives).
  MG2 (blind; merges inside the run): at depths 37, 41 and 45 the distinct states fall faster than the prefixes:
      log2 D_l loses 0.55 to 0.70 bits per cell, log2 S_l 0.45 to 0.55 (least squares over the cells with D_l >= 16).
  MG3 (blind; the explanation): the merges account for the record law: log2 D(d) / (b_D d), the record ratio the
      merged walks imply (b_D the slope of MG2), lies between 0.72 and 0.88 at depths 37, 41 and 45 (observed R/d
      from 49 to 81: 0.79 to 0.88).
  MG4 (blind): at depth 41, in at least 99% of the classes with two or more prefixes, the members differ only at
      times below 0.3 d.
  MG5 (blind; one record, few walks): at every odd depth from 41 to 61 and at 65, 69, 73, 77 and 81, the record
      witnesses (W lines, up to 64) form at most 6 distinct walks (distinct column 1 from time d - 1, the run's own
      forced bits), and at most 2 at the median depth.
  MG6 (blind): within each such walk the witnesses differ only at times below 0.35 d.
  MG7 (random-chaos, from hydrology; the owner's lightning channels): are merging walks a river network? In
      Scheidegger's model (1967) the streams are coalescing random walks: the distinct ones fall only as a power of
      the distance (t^(-1/2), so delta would grow like (1/2) log2 d, 0.55 from 21 to 45), and basins come in all
      sizes. Prediction: not here: at depth DMAX under 1% of prefixes lie in classes of 64 or more.
  CF (counterfactual): with XOR in place of the OR (no shielding) no two prefixes merge: D(d) = 2^nfree(d) at every
      odd d from 21 to 33.
REFUTED-BY: MG0 failing (the instruments); MG1 to MG7 and CF failing.

OUTCOME, 2026-10-05 (the first run, DMAX = 45, 14 seconds):
  MG0 PASSED: (a) on 200 random prefixes; (b) unshielded flips changed the run in 68% of trials (the coin's 2/3),
     shielded flips never; (c) at all 13 odd depths 21 .. 45 the merged frontier's weighted histogram is records.c's.
  MG1 HELD, and the growth is steady: D(d) = 303, 540, 953, 1694, 3006, 5324, 9464, 16779, 29753, 52640, 93236,
     164745, 291014 at d = 21, 23, .., 45; delta from 1.76 to 3.85 (growth 2.09), about 0.087 per unit depth. Each
     ratio D(d + 2) / D(d) lies between 1.765 and 1.782. Least squares: log2 D(d) = 0.4129 d - 0.42, so one free
     bit multiplies the distinct walks by 1.773, not 2.
  MG2 REFUTED: no merging inside the run. D_l loses 0.486, 0.489 and 0.495 bits per cell at depths 37, 41 and 45,
     and S_l loses 0.480, 0.491 and 0.490, the same coin rate. All the merging is in the prefix stage, where both
     choices branch; a forced walk does not merge with another.
  MG3 HELD (0.826, 0.823, 0.815).
  The explanation, then: the record is the coin maximum over D(d) independent walks, not over 2^(d/2) prefixes. The
  maximum of n runs 1 + 2M with P(M >= m) = 2^-m is about 2 log2 n + 1.67, so R(d) ~ 0.826 d + 0.8. Against
  Local's and Cloud's records at depths 49 .. 81 (12 depths) the residuals are -2.3, 4.1, 0.4, -3.2, -2.9, 1.5,
  -2.2, 2.5, -2.8, -2.1, -1.4, -2.7 (mean -0.9): the 0.8 law, from a count made at depths 45 and below.
  MG4 REFUTED: merging is not confined to early bits. At depth 41, 92945 classes have two or more prefixes, and the
     latest time at which a class's members differ is spread over 0 .. 30 (counts 5592, 20049, 21310, 15344, 10806,
     7188, 4867, 3219, 2011, 1212, 698, 366, 182, 67, 29, 5 at times 0, 2, .., 30: a geometric fall of about 0.68
     per two time units after the peak). 7789 classes (8.4%) differ at times above 0.3 d.
  MG5 HELD: the record witnesses form one walk at 11 of the 16 depths, two at 43, 49, 55 and 73, three at 61. A
     record is one walk reached by many prefixes (8 to 64 listed).
  MG6 REFUTED at 43 (members differ at time 32, against 15.05) and 65 (24 against 22.75); held at the other 14.
  MG7 REFUTED as worded: 6.8% of prefixes lie in classes of 64 or more at depth 45. The class sizes peak at 16 to 31
     (37% of prefixes), and the mean is 2^3.85 = 14. The tail falls fast: 6.2% at 64 to 127, 0.56% at 128 to 255,
     0.01% above that, largest 284. So the threshold, set for "a few dead bits", was wrong. The river reading fails
     too: Scheidegger's coalescing walks give delta growing like (1/2) log2 d, 0.55 from 21 to 45, against 2.09
     measured. The walks merge at a constant rate per step, an exponential loss, not a power law.
  CF HELD: with XOR for the OR, D = 2^nfree exactly at every odd depth 21 .. 33. Shielding is the whole mechanism.
  rule30_influence.py's strip reading survives in part. The merges are real and come from shielding (CF), and delta
  is linear in d (MG1). But merges are not confined to the early bits (MG4), and they stop inside a run (MG2).
"""
import math, pathlib, random, statistics, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 45
CACHE = pathlib.Path(tempfile.gettempdir()) / "rule30_records_cache"      # rule30_records.py's per-depth outputs
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def diag(P, Q, c, k, xor=False):
    """A_k from A_{k-1} = P and A_{k-2} = Q, c = column 1 at time k-1 (records.c's rule; xor: the counterfactual)."""
    X = ((P << 1) ^ (Q << 2) ^ (c << 1)) if xor else ((P << 1) | (Q << 2) | (c << 1))
    X = (X & ~1) | (k & 1)
    s = 1
    while s <= k:
        X ^= X << s
        s <<= 1
    return X & ((2 << k) - 1)


def canon(P, Q):
    return P, Q & ~(P >> 1)


def nfree(d):
    return (d - 2) // 2 + 1 if d >= 2 else 0


def walk(P, Q, k, cap=400):
    """The forced walk from depth k; returns the run and the cells (0 or 1) it met, the last one 1."""
    k0 = k
    while k - k0 < cap:
        A = diag(P, Q, 0, k)
        if (A >> k) & 1:
            if (k - 1) % 2 == 0:
                A = diag(P, Q, 1, k)
            else:
                return k - k0
        P, Q = A, P
        k += 1
    return cap


def state_at(prefix, d):
    P, Q = 0, 0
    for k in range(1, d):
        c = (prefix >> ((k - 1) // 2)) & 1 if (k - 1) % 2 == 0 else 0
        P, Q = diag(P, Q, c, k), P
    return P, Q


def left_half(bits, T, K):
    """Independent: x_t(-j) for t = 0 .. T - K - 1, j = 1 .. K, from column 0 = t mod 2 and column 1 (bits: time ->
    bit, odd times 0), by x_t(i-1) = x_{t+1}(i) XOR (x_t(i) OR x_t(i+1)). Returns {(t, j): cell}."""
    right = [t % 2 for t in range(T)]
    far = [bits.get(t, 0) if t % 2 == 0 else 0 for t in range(T)]
    cells = {}
    for j in range(1, K + 1):
        col = [right[t + 1] ^ (right[t] | far[t]) for t in range(len(right) - 1)]
        for t, v in enumerate(col):
            cells[(t, j)] = v
        far, right = right, col
    return cells


def records_output(d):
    f = CACHE / f"d{d}.txt"
    if f.exists():
        return f.read_text()
    exe = pathlib.Path(tempfile.gettempdir()) / "rule30_merge_records"
    if not exe.exists():
        subprocess.run(["cc", "-O2", "-fopenmp", "-o", str(exe), str(HERE / "records.c")], check=True)
    out = subprocess.run([str(exe), str(d), "0"], check=True, capture_output=True, text=True).stdout
    CACHE.mkdir(exist_ok=True)
    f.write_text(out)
    return out


def parse(out):
    R, H, W = None, {}, []
    for ln in out.splitlines():
        f = ln.split()
        if not f:
            continue
        if f[0] == "R":
            R = int(f[2])
        elif f[0] == "H":
            H[int(f[2])] = int(f[3])
        elif f[0] == "W":
            W.append(f[2])
    return R, H, W


def slope(xs, ys):
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def run_from(front, d):
    """The merged walk from the depth-d frontier {canonical state: multiplicity}: histogram, S_l and D_l."""
    H, S, Dl = {}, [], []
    cur, k = dict(front), d
    while cur:
        S.append(sum(cur.values()))
        Dl.append(len(cur))
        nxt = {}
        for (P, Q), m in cur.items():
            A = diag(P, Q, 0, k)
            if (A >> k) & 1:
                if (k - 1) % 2 == 0:
                    A = diag(P, Q, 1, k)
                else:
                    H[k - d] = H.get(k - d, 0) + m
                    continue
            key = canon(A, P)
            nxt[key] = nxt.get(key, 0) + m
        cur, k = nxt, k + 1
    return H, S, Dl


def controls(rng):
    ok = True
    for _ in range(200):                                        # MG0 (a)
        d = 33
        p = rng.getrandbits(nfree(d))
        bits = {2 * i: (p >> i) & 1 for i in range(nfree(d))}
        P, Q = 0, 0
        cells = left_half(bits, 2 * d + 4, d)
        for k in range(1, d):
            c = bits.get(k - 1, 0) if (k - 1) % 2 == 0 else 0
            P, Q = diag(P, Q, c, k), P
            ok &= ((P >> k) & 1) == cells[(0, k)]
        i = rng.randrange(nfree(d))
        flipped = dict(bits)
        flipped[2 * i] ^= 1
        cells2 = left_half(flipped, 2 * d + 4, d)
        diff = [t for (t, j), v in cells.items() if cells2[(t, j)] != v]
        ok &= bool(diff) and max(diff) <= 2 * i
    report("MG0a the simulator's row 0 is the diagonals' cells; the bit at time 2i changes only rows 0 .. 2i", ok)
    same, changed, trials = True, 0, 0                         # MG0 (b)
    while trials < 2000:
        d = 33
        P, Q = state_at(rng.getrandbits(nfree(d)), d)
        sh = [j for j in range(d - 1) if (P >> (j + 1)) & 1]
        un = [j for j in range(d - 1) if not (P >> (j + 1)) & 1]
        if not sh or not un:
            continue
        trials += 1
        L = walk(P, Q, d)
        same &= walk(P, Q ^ (1 << rng.choice(sh)), d) == L
        changed += walk(P, Q ^ (1 << rng.choice(un)), d) != L
    report("MG0b a shielded bit never changes the walk; an unshielded one does in at least 30% of trials",
           same and changed >= 0.3 * trials, f"unshielded flips changed the run {changed / trials:.2f}")


def main():
    rng = random.Random(1967)                                  # the year of Scheidegger's river-network model
    controls(rng)
    front, k = {(0, 0): [1, 0, 0]}, 1                           # canonical state -> [prefixes, OR, AND of them]
    res, ok0 = {}, True
    while k <= DMAX:
        if k % 2 == 1 and k >= 21:
            d = k
            mult = {s: v[0] for s, v in front.items()}
            H, S, Dl = run_from(mult, d)
            R, Hr, _ = parse(records_output(d))
            okd = H == Hr and max(H) == R
            ok0 &= okd
            sizes = [v[0] for v in front.values()]
            res[d] = dict(D=len(front), H=H, S=S, Dl=Dl, R=R, sizes=sizes,
                          diffs=[(v[1] ^ v[2]).bit_length() - 1 for v in front.values() if v[0] > 1])
            print(f"   depth {d}: D(d) = {len(front)} = 2^{math.log2(len(front)):.2f} of 2^{nfree(d)} prefixes "
                  f"(delta {nfree(d) - math.log2(len(front)):.2f}); record {max(H)} (records.c {R})"
                  f"{'' if okd else '  MISMATCH'}", flush=True)
        free = (k - 1) % 2 == 0
        i = (k - 1) // 2
        nxt = {}
        for (P, Q), (m, o, a) in front.items():
            for c in ((0, 1) if free else (0,)):
                A = diag(P, Q, c, k)
                key = canon(A, P)
                oo, aa = (o | (c << i), a | (c << i)) if free else (o, a)
                if key in nxt:
                    v = nxt[key]
                    v[0] += m; v[1] |= oo; v[2] &= aa
                else:
                    nxt[key] = [m, oo, aa]
        front, k = nxt, k + 1
    report(f"MG0c the merged frontier gives records.c's record and histogram at every odd depth 21 .. {DMAX}", ok0)

    delta = {d: nfree(d) - math.log2(r["D"]) for d, r in res.items()}
    print("   delta(d): " + ", ".join(f"{d}: {v:.2f}" for d, v in delta.items()))
    g = delta.get(45, delta[max(delta)]) - delta[21]
    verdict("MG1 1 <= delta(d) <= 5 at every odd depth, growing by 1 to 3 from 21 to 45",
            all(1 <= v <= 5 for v in delta.values()) and 1 <= g <= 3, f"growth {g:.2f}")

    bD, bS = {}, {}
    for d in (37, 41, 45):
        if d not in res:
            continue
        Dl, S = res[d]["Dl"], res[d]["S"]
        ls = [l for l in range(len(Dl)) if Dl[l] >= 16]
        bD[d] = -slope(ls, [math.log2(Dl[l]) for l in ls])
        bS[d] = -slope(ls, [math.log2(S[l]) for l in ls])
        print(f"   depth {d}: D_l = " + " ".join(str(x) for x in Dl[:24]) + (" .." if len(Dl) > 24 else ""))
        print(f"   depth {d}: S_l = " + " ".join(str(x) for x in S[:24]) + (" .." if len(S) > 24 else ""))
    verdict("MG2 distinct states fall 0.55 to 0.70 bits per cell, prefixes 0.45 to 0.55",
            all(0.55 <= bD[d] <= 0.70 and 0.45 <= bS[d] <= 0.55 for d in bD),
            ", ".join(f"{d}: D {bD[d]:.3f}, S {bS[d]:.3f}" for d in bD))
    rho = {d: math.log2(res[d]["D"]) / (bD[d] * d) for d in bD}
    verdict("MG3 the merged walks imply a record ratio log2 D(d) / (b_D d) of 0.72 to 0.88",
            all(0.72 <= r <= 0.88 for r in rho.values()), ", ".join(f"{d}: {r:.3f}" for d, r in rho.items()))

    if 41 in res:
        diffs = res[41]["diffs"]
        late = [i for i in diffs if 2 * i >= 0.3 * 41]
        print(f"   depth 41: {len(diffs)} classes with two or more prefixes; latest differing time by class: "
              + ", ".join(f"{2 * t}: {diffs.count(t)}" for t in sorted(set(diffs))))
        verdict("MG4 at depth 41, 99% of classes differ only at times below 0.3 d", len(late) <= 0.01 * len(diffs),
                f"{len(late)} of {len(diffs)} differ later")

    local = parse_local()
    walks, inner, ok5 = {}, {}, True
    for d in list(range(41, 62, 2)) + [65, 69, 73, 77, 81]:
        W = local[d] if d in local else parse(records_output(d))[2]
        start = (d - 1) // 2                                   # visible bit n is time 2n; the run's own from d - 1
        groups = {}
        for w in W:
            groups.setdefault(w[start:], []).append(w)
        walks[d] = len(groups)
        lat = -1
        for g in groups.values():
            for n in range(start):
                if len({w[n] for w in g}) > 1:
                    lat = max(lat, 2 * n)
        inner[d] = lat
        print(f"   depth {d}: {len(W)} witnesses, {len(groups)} distinct walks (sizes "
              f"{sorted((len(g) for g in groups.values()), reverse=True)}); latest time differing within a walk {lat}",
              flush=True)
    med = statistics.median(walks.values())
    verdict("MG5 at most 6 distinct record walks at every depth, at most 2 at the median",
            max(walks.values()) <= 6 and med <= 2, f"largest {max(walks.values())}, median {med}")
    verdict("MG6 within a record walk the witnesses differ only at times below 0.35 d",
            all(inner[d] < 0.35 * d for d in inner), ", ".join(f"{d}: {inner[d]}" for d in inner))

    sizes = res[max(res)]["sizes"]
    tot = sum(sizes)
    big = sum(s for s in sizes if s >= 64)
    bins = {}
    for s in sizes:
        b = 1 << (s.bit_length() - 1)
        bins[b] = bins.get(b, 0) + s
    print(f"   depth {max(res)}: prefixes by class size (lower power of 2): "
          + ", ".join(f"{b}: {bins[b] / tot:.4f}" for b in sorted(bins)) + f"; largest class {max(sizes)}")
    verdict("MG7 under 1% of prefixes in classes of 64 or more (not a river basin)", big < 0.01 * tot,
            f"{big / tot:.4f}")

    okc = True
    for d in range(21, 34, 2):
        fr = {(0, 0)}
        for k in range(1, d):
            free = (k - 1) % 2 == 0
            fr = {(diag(P, Q, c, k, xor=True), P) for (P, Q) in fr for c in ((0, 1) if free else (0,))}
        okc &= len(fr) == 1 << nfree(d)
        print(f"   XOR world, depth {d}: {len(fr)} states of 2^{nfree(d)} = {1 << nfree(d)}")
    verdict("CF without shielding no two prefixes merge (D = 2^nfree at 21 .. 33)", okc)
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def parse_local():
    out = {}
    f = HERE / "rule30_records_local.txt"
    if f.exists():
        for ln in f.read_text().splitlines():
            g = ln.split()
            if g and g[0] == "W":
                out.setdefault(int(g[1]), []).append(g[2])
    return out


if __name__ == "__main__":
    main()
