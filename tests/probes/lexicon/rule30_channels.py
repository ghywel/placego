#!/usr/bin/env python3
"""rule30_channels.py: the owner's question about the lightning. Do the walks gravitate to certain paths?

RUN-ON:     cpu (pure Python 3, standard library; exact propagation, no sampling)
COMMAND:    python3 tests/probes/lexicon/rule30_channels.py [T=2048] | rule30_channels.py cause [T=2048]
COST:       about two minutes on one core. Writes rule30_channels.png next to this script.

The owner (2026-10-05): "Given current follows the path(s) of least resistance distributed throughout the material
substrate, do the lightning walks tend to gravitate towards certain paths or patterns?"

Two kinds of lightning, on pyramids of depth T (black weight 1, white weight EPS = 0.1, moves to the three cells below):
  The flicker (rule30_lightning.py): each step picks one of the three cells below in proportion to their weights,
    seeing only the next row. Its landing law is computed here exactly, row by row, instead of by sampling.
  The polymer: the current spread through the whole substrate. Every path from the apex is weighted by the product of
    its cells' weights, and a bolt is a path drawn with that weight (a directed polymer at a fixed temperature, the
    statistical-physics model of a path of least resistance with fluctuations). Its landing law and the share of
    paths through each cell come from exact forward and backward sums (transfer matrices).
What is known, for an environment of independent random cells (PRIOR-ART.md): the directed polymer in 1 + 1 dimensions
is in strong disorder at every temperature (Comets, Shiga and Yoshida, Bernoulli 9, 2003; Comets and Vargas, ALEA 2,
2006), and strong disorder is equivalent to path localisation: the chance that two polymers in the same environment
end at the same point does not die out (Comets, Shiga and Yoshida; Bates and Chatterjee, CMP 2020). A walk that sees
only its next step, in a random space-time environment, instead obeys an ordinary central limit theorem (Balazs,
Rassoul-Agha and Seppalainen, CMP 266, 2006). So for random substrates theory says the polymer channels and the
flicker spreads. Whether Rule 30's substrate does the same, or has paths of its own, is the question here.

The measures, at depths 128, 256, ..., T:
  L(t): the same-landing chance. Two bolts, drawn independently on the same pyramid, end on the same cell of row t.
    A free random walk has L(t) ~ 1 / sqrt(4 pi t / 3), so L falls by half when the depth goes up four times.
  Ibar(t): L averaged over rows 1 to t (the time-averaged form in the theorems).
  R: the share of rows on which two independent polymer bolts to depth T pass through the same cell.
Pyramids: Rule 30 from a single 1; NRAND random pyramids with Rule 30's interior density and black edges; the
all-black pyramid (the control: both kinds of lightning become the free trinomial walk); and, as the chaos step, Rule 30
with 1% of its interior cells flipped at random.

PREDICTIONS, written 2026-10-05 before this script's first run (no exploratory run):
  CH0 (controls, exact): on the all-black pyramid the flicker's and the polymer's landing laws equal the free trinomial
      walk, computed independently, to within 1e-12 at every depth; every law sums to 1 within 1e-9; and the polymer's
      total weight, recomputed from the forward and backward sums at every row, agrees with itself within 1e-9
      (relative).
  CH1 (blind; the flicker spreads): the flicker's same-landing chance falls like a free walk's: L(T) / L(128) lies
      between 0.15 and 0.4 (free: sqrt(128 / T) = 0.25 at T = 2048) on Rule 30 and on every random pyramid. Its bolts
      share cells more than free walks do, but not by much: L(T) is 1 to 4 times the free walk's.
  CH2 (blind; the polymer channels): the polymer's time-averaged same-landing chance does not fall like a free walk's:
      Ibar(T) / Ibar(128) above 0.6 (free: about 0.25), and Ibar(T) above 0.1, on Rule 30 and on at least
      NRAND - 1 of the random pyramids. Two polymer bolts to depth T share the same cell on more than a fifth of the
      rows (R > 0.2).
  CH3 (blind; no special paths): Rule 30 channels like a random substrate. Its flicker L(T), its polymer Ibar(T) and its
      polymer R each lie between 0.67 times the smallest and 1.5 times the largest of the random pyramids' values.
  CH4 (blind, uncertain): the polymer's channels lean left on Rule 30, as the flicker does: its mean landing point at
      depth T is left of -0.035 T, half the flicker's drift of -0.07 per row (rule30_lightning.py, LG4 and LG5).
  CH5 (the chaos step, blind): flipping 1% of Rule 30's interior cells moves the polymer's channels but hardly moves
      the flicker. Comparing the landing laws at depth T before and after (cosine similarity), the polymer's is below
      0.5 and the flicker's above 0.9.
REFUTED-BY: CH0 failing (the instrument); CH1 to CH5 failing.

OUTCOME of the first run, 2026-10-05 (T = 2048, one minute): CH0 PASSED (gaps 3e-17 and 4e-17; the free walk's
L(2048) = 0.0076 and Ibar(2048) = 0.0150). Rule 30's interior density 0.5017; the random pyramids' 0.5003.
  The flicker: L(2048) / L(128) = 0.245 on Rule 30 and 0.20 to 0.32 on the random pyramids (free 0.249); L(2048) is
      1.52 times the free walk's on Rule 30, 1.63 to 1.75 on random. CH1 HELD: the flicker spreads like a free walk on
      every substrate, with a little sharing. Its mean landing point on Rule 30 is -140.5 (random -1.0 to +1.5).
  The polymer on the random pyramids: Ibar(2048) = 0.104 to 0.128, Ibar(2048) / Ibar(128) = 0.74 to 1.01 (free 0.26),
      R = 0.160 to 0.221, largest landing cell 0.07 to 0.28. As theory says, it channels: two bolts end on the same
      cell about one time in eight at every depth, and share a fifth of their route.
  The polymer on Rule 30: Ibar(2048) = 0.037, ratio 0.467, R = 0.069, largest landing cell 0.037. CH2 REFUTED (on
      Rule 30, and on R for two random pyramids, 0.160 and 0.190). CH3 REFUTED: the flicker's L(2048), 0.0116, is in
      the random band (0.0124 to 0.0134), but the polymer's Ibar is three times lower than the random pyramids' and R
      2.3 to 3.2 times lower. Rule 30 spreads the current out: its lightning forms fewer and weaker channels than a
      random substrate's. This is the first measure in this family that tells Rule 30 from coin flips beyond its
      handedness.
  CH4 HELD: the polymer lands at -179.3 on Rule 30 (-0.088 T), left of the flicker's -140.5; random polymers -37 to
      +34. CH5 REFUTED: 1% flips leave the polymer's landing law at cosine 0.671 (the flicker's 0.992); the flipped
      Rule 30 keeps Rule 30's weak channels (Ibar 0.044, R 0.072). The weak channelling survives 1% noise.
  The figure: the flicker is one smooth beam; the polymer is a braid of thin filaments inside a beam leaning left.

ADDENDUM, written 2026-10-05 after the first run and before the second (python3 rule30_channels.py cause): why does Rule
30 channel less? Rule 30 is surjective, so from an initial row of fair coins every row is again fair coins: what differs
from a random pyramid is only how the cells are tied across rows. Two substrates separate the seed from the rule: Rule
30 run from a random initial row (the pyramid is the cone below one cell of row 0), and Rule 90 from a random row
(rows of fair coins as well, tied by a linear rule). And one candidate mechanism: a polymer channels when its paths'
resistances differ a lot, so the spread of the white count W along uniform random paths (no preference for black),
Var(W) / T over 2,000 paths, measures how much the substrate offers to choose from.
  CH6 (blind): Rule 30 from a random row channels like Rule 30 from a single 1: polymer Ibar(T) within a factor 1.5
      of the single seed's, and below 0.67 times the smallest of three new random pyramids'. The weak channels belong
      to the rule, not to the seed.
  CH7 (blind): the mechanism is a smaller spread of path resistances: Var(W) / T on Rule 30 (single seed and both
      random-row runs) is below 0.8 times every random pyramid's.
  CH8 (blind, uncertain): Rule 90 from a random row channels like the random pyramids (Ibar(T) within [0.67 min,
      1.5 max] of theirs).
OUTCOME of the second run, 2026-10-05 (python3 rule30_channels.py cause, T = 2048, one minute). Polymer Ibar(2048), R,
and the path spread Var(W)/T: Rule 30 from a single 1 0.0368, 0.069, 0.179; Rule 30 from two random rows 0.0332 and
0.0361, 0.061 and 0.051, 0.182 and 0.170; Rule 90 from two random rows 0.0711 and 0.0701, 0.113 and 0.161, 0.240 and
0.237; three random pyramids 0.104 to 0.119, 0.159 to 0.192, 0.248 to 0.251. CH6 HELD: the weak channels belong to the
rule, not the seed. CH7 HELD: Rule 30's routes differ less in resistance, by 0.72 of the random pyramids' spread. The
cause is the handedness again (rule30_lightning.py, LG4): below a black cell the lower-right child is black a quarter
of the time and below a white one three quarters, while the other two children are uncorrelated with it. That gives
a covariance of -1/8 on a third of a uniform path's steps, so Var(W)/T = 1/4 - 2 (1/3)(1/8) = 0.167 to first order,
close to the measured 0.17 to 0.18. CH8 HELD, at the edge of its band (0.0701 against a lower limit of 0.0697): Rule 90
channels about 0.6 times as much as random although its path spread is nearly random (0.24), so the spread is not the
whole story; Rule 90's longer-range structure (its nested triangles) is the candidate, not tested here.
"""
import array, math, pathlib, random, struct, sys, zlib

HERE = pathlib.Path(__file__).resolve().parent
_nums = [a for a in sys.argv[1:] if a != "cause"]
T = int(_nums[0]) if _nums else 2048
EPS = 0.1
NRAND = 4
N = 2 * T + 3                                          # index i = x + T + 1, one padding cell at each end
DEPTHS = sorted({d for d in (128, 256, 512, 1024, 2048, 4096, 8192) if d < T} | {T})   # T itself always last
TO01 = bytes.maketrans(b"01", b"\x00\x01")
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def rule30_rows():
    rows, row, mask = [], 1 << T, (1 << (2 * T + 1)) - 1          # bit x + T holds cell x
    for _ in range(T):
        cells = format(row, f"0{2 * T + 1}b")[::-1].encode().translate(TO01)
        rows.append(bytearray(b"\x00" + cells + b"\x00"))
        row = ((row << 1) ^ (row | (row >> 1))) & mask
    return rows


def random_rows(density, rng):
    rows = []
    for t in range(T):
        r = bytearray(N)
        for x in range(-t, t + 1):
            r[x + T + 1] = 1 if abs(x) == t or rng.random() < density else 0
        rows.append(r)
    return rows


def black_rows():
    rows = []
    for t in range(T):
        r = bytearray(N)
        r[T + 1 - t:T + 2 + t] = b"\x01" * (2 * t + 1)
        rows.append(r)
    return rows


def flipped(rows, share, rng):
    out = [bytearray(r) for r in rows]
    for t in range(2, T):
        r = out[t]
        for i in range(T + 2 - t, T + 1 + t):                     # interior cells, |x| < t
            if rng.random() < share:
                r[i] ^= 1
    return out


def weights(r):
    return [1.0 if b else EPS for b in r]


def stats(P, r):
    """Same-landing chance, mean landing point, largest cell, share on white cells inside the pyramid."""
    L = sum(p * p for p in P)
    mean = sum(p * (i - T - 1) for i, p in enumerate(P) if p)
    white = sum(p for p, b in zip(P, r) if p and not b)
    return L, mean, max(P), white


class Panel:
    """A downsampled picture of path density: the largest share in each f x f block of cells."""

    def __init__(self):
        self.f = max(1, T // 512)
        self.rows = [[0.0] * (N // self.f) for _ in range(T // self.f)]

    def add(self, t, law):
        f, row = self.f, self.rows[t // self.f] if t // self.f < len(self.rows) else None
        if row is not None:
            for k in range(len(row)):
                m = max(law[k * f:(k + 1) * f])
                if m > row[k]:
                    row[k] = m


def flicker(rows, panel=None):
    """The flicker's exact landing law, row by row. Returns per-row stats and the laws at DEPTHS."""
    P = [0.0] * N
    P[T + 1] = 1.0
    st, laws = [stats(P, rows[0])], {}
    for t in range(1, T):
        w = weights(rows[t])
        S = [0.0] + [a + b + c for a, b, c in zip(w, w[1:], w[2:])] + [0.0]      # S[i] = w[i-1] + w[i] + w[i+1]
        q = [p / s if p else 0.0 for p, s in zip(P, S)]
        P = [0.0] + [wi * (a + b + c) for wi, a, b, c in zip(w[1:], q, q[1:], q[2:])] + [0.0]
        st.append(stats(P, rows[t]))
        if t + 1 in DEPTHS:
            laws[t + 1] = P
        if panel:
            panel.add(t, P)
    return st, laws


def polymer(rows, panel=None):
    """The polymer's forward sums (each row normalised to sum 1: the landing law at that depth), then the backward sums
    for depth T and the path marginals. Returns per-row stats of the landing laws, the laws at DEPTHS, R, the share of
    path weight on white cells, and the relative spread of the total weight recomputed at every row."""
    Z = [0.0] * N
    Z[T + 1] = 1.0
    fw, logf, st, laws = [array.array("d", Z)], [0.0], [stats(Z, rows[0])], {}
    for t in range(1, T):
        w = weights(rows[t])
        Z = [0.0] + [wi * (a + b + c) for wi, a, b, c in zip(w[1:], Z, Z[1:], Z[2:])] + [0.0]
        s = sum(Z)
        Z = [z / s for z in Z]
        fw.append(array.array("d", Z))
        logf.append(logf[-1] + math.log(s))
        st.append(stats(Z, rows[t]))
        if t + 1 in DEPTHS:
            laws[t + 1] = Z
    B, logb = [1.0] * N, 0.0
    logZ, R, white = [0.0] * T, 0.0, 0.0
    for t in range(T - 1, -1, -1):
        prod = [f * b for f, b in zip(fw[t], B)]
        s = sum(prod)
        m = [x / s for x in prod]
        R += sum(x * x for x in m)
        white += sum(x for x, c in zip(m, rows[t]) if x and not c)
        if panel:
            panel.add(t, m)
        logZ[t] = logf[t] + logb + math.log(s)
        if t:
            u = [wi * b for wi, b in zip(weights(rows[t]), B)]
            B = [0.0] + [a + b + c for a, b, c in zip(u, u[1:], u[2:])] + [0.0]
            mx = max(B)
            B = [b / mx for b in B]
            logb += math.log(mx)
    spread = (max(logZ) - min(logZ)) / max(1.0, abs(logZ[0]))
    return st, laws, R / T, white / T, spread


def trinomial():
    """The free walk, computed on its own: L at every row and the laws at DEPTHS."""
    p = [0.0] * N
    p[T + 1] = 1.0
    Ls, laws = [1.0], {}
    for t in range(1, T):
        p = [0.0] + [(a + b + c) / 3 for a, b, c in zip(p, p[1:], p[2:])] + [0.0]
        Ls.append(sum(x * x for x in p))
        if t + 1 in DEPTHS:
            laws[t + 1] = p
    return Ls, laws


def ibar(st, d):
    return sum(s[0] for s in st[1:d]) / (d - 1)


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b)) / math.sqrt(sum(x * x for x in a) * sum(y * y for y in b))


def png(path, pix, w, h):
    raw = b"".join(b"\x00" + bytes(pix[y * w * 3:(y + 1) * w * 3]) for y in range(h))

    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff)
    pathlib.Path(path).write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
                                   + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def figure(rows, panels):
    """Side-by-side panels of path density (log scale from 1e-6 to 1, yellow to red) over the pyramid (black cells
    grey, by their share in each block)."""
    f = panels[0].f
    h, wp = T // f, N // f
    w = wp * len(panels) + 8 * (len(panels) - 1)
    pix = [255] * (w * h * 3)
    grey = [[None] * wp for _ in range(h)]
    for y in range(h):
        for xb in range(wp):
            n = b = 0
            for t in range(y * f, y * f + f):
                for i in range(xb * f, xb * f + f):
                    if abs(i - T - 1) <= t:
                        n += 1
                        b += rows[t][i]
            if n:
                grey[y][xb] = int(235 - 85 * b / n)
    for k, panel in enumerate(panels):
        x0 = k * (wp + 8)
        for y in range(h):
            for xb in range(wp):
                o = (y * w + x0 + xb) * 3
                d = panel.rows[y][xb]
                if d > 1e-6:
                    g = min(1.0, (math.log10(d) + 6) / 6)
                    pix[o:o + 3] = [255, int(230 * (1 - g)), int(60 * (1 - g))]
                elif grey[y][xb] is not None:
                    v = grey[y][xb]
                    pix[o:o + 3] = [v, v, v]
    png(HERE / "rule30_channels.png", pix, w, h)


def main():
    rng = random.Random(1882)                          # the year of the first photograph of lightning
    trL, tri = trinomial()
    blk = black_rows()
    _, flaws = flicker(blk)
    pst, plaws, _, _, cons = polymer(blk)
    gap_f = max(max(abs(a - b) for a, b in zip(flaws[d], tri[d])) for d in DEPTHS)
    gap_p = max(max(abs(a - b) for a, b in zip(plaws[d], tri[d])) for d in DEPTHS)
    sums = max(abs(sum(l) - 1) for l in list(flaws.values()) + list(plaws.values()))
    free = {d: trL[d - 1] for d in DEPTHS}
    free_ibar = {d: sum(trL[1:d]) / (d - 1) for d in DEPTHS}
    report("CH0 all-black: flicker and polymer equal the trinomial walk; laws sum to 1; the polymer's weight agrees "
           "across rows", gap_f < 1e-12 and gap_p < 1e-12 and sums < 1e-9 and cons < 1e-9,
           f"flicker gap {gap_f:.1e}, polymer gap {gap_p:.1e}, sum error {sums:.1e}, weight spread {cons:.1e}")
    print("   free walk: L(d) " + ", ".join(f"{d}: {free[d]:.4f}" for d in DEPTHS) + "; Ibar(d) "
          + ", ".join(f"{d}: {free_ibar[d]:.4f}" for d in DEPTHS), flush=True)
    del blk, flaws, plaws, tri

    r30rows = rule30_rows()
    inside = sum(sum(r30rows[t][T + 2 - t:T + 1 + t]) for t in range(2, T))
    density = inside / sum(2 * t - 1 for t in range(2, T))

    def run(name, rows, panels=(None, None)):
        fs, fl = flicker(rows, panels[0])
        ps, pl, R, pwhite, cons = polymer(rows, panels[1])
        res = dict(fL={d: fs[d - 1][0] for d in DEPTHS}, fmean=fs[T - 1][1], fwhite=sum(s[3] for s in fs) / T,
                   pL={d: ps[d - 1][0] for d in DEPTHS}, pI={d: ibar(ps, d) for d in DEPTHS}, pmax=ps[T - 1][2],
                   pmean=ps[T - 1][1], R=R, pwhite=pwhite, cons=cons, fland=fl[T], pland=pl[T])
        print(f"   {name}:\n      flicker L(d) " + ", ".join(f"{d}: {res['fL'][d]:.4f}" for d in DEPTHS)
              + f"; mean landing {res['fmean']:+.1f}; white share {res['fwhite']:.3f}", flush=True)
        print("      polymer L(d) " + ", ".join(f"{d}: {res['pL'][d]:.4f}" for d in DEPTHS)
              + "; Ibar(d) " + ", ".join(f"{d}: {res['pI'][d]:.4f}" for d in DEPTHS)
              + f"; R {R:.3f}; largest landing cell {res['pmax']:.3f}; mean landing {res['pmean']:+.1f}; white share "
              f"{pwhite:.3f}; weight spread {cons:.1e}", flush=True)
        return res

    panels = (Panel(), Panel())
    r30 = run("Rule 30", r30rows, panels)
    figure(r30rows, panels)
    print("   wrote rule30_channels.png: Rule 30's pyramid (black cells grey), the flicker's path density (left) and "
          "the polymer's (right), yellow to red on a log scale from 1e-6 to 1", flush=True)
    del panels
    rnd = [run(f"random pyramid {k + 1} (density {density:.4f})", random_rows(density, rng)) for k in range(NRAND)]
    pert = run("Rule 30 with 1% of its interior flipped (the chaos step)", flipped(r30rows, 0.01, rng))

    D = DEPTHS[-1]
    allp = [r30] + rnd
    names = ["Rule 30"] + [f"random {k + 1}" for k in range(NRAND)]
    ok1 = all(0.15 <= r["fL"][D] / r["fL"][128] <= 0.4 and 1 <= r["fL"][D] / free[D] <= 4 for r in allp)
    verdict("CH1 the flicker spreads like a free walk (L(T) / L(128) in [0.15, 0.4]) and shares 1 to 4 times as much",
            ok1, "; ".join(f"{n}: ratio {r['fL'][D] / r['fL'][128]:.3f}, {r['fL'][D] / free[D]:.2f} x free"
                           for n, r in zip(names, allp)) + f"; free ratio {free[D] / free[128]:.3f}")
    chan = [r["pI"][D] / r["pI"][128] > 0.6 and r["pI"][D] > 0.1 for r in rnd]
    ok2 = (r30["pI"][D] / r30["pI"][128] > 0.6 and r30["pI"][D] > 0.1 and sum(chan) >= NRAND - 1
           and all(r["R"] > 0.2 for r in allp))
    verdict("CH2 the polymer channels: Ibar(T) / Ibar(128) > 0.6 and Ibar(T) > 0.1, and R > 0.2", ok2,
            "; ".join(f"{n}: Ibar ratio {r['pI'][D] / r['pI'][128]:.3f}, Ibar {r['pI'][D]:.3f}, R {r['R']:.3f}"
                      for n, r in zip(names, allp)) + f"; free walk Ibar ratio {free_ibar[D] / free_ibar[128]:.3f}")

    def band(label, v):
        lo, hi = min(v(r) for r in rnd), max(v(r) for r in rnd)
        return 0.67 * lo <= v(r30) <= 1.5 * hi, f"{label}: Rule 30 {v(r30):.4f}, random {lo:.4f} to {hi:.4f}"
    b = [band("flicker L(T)", lambda r: r["fL"][D]), band("polymer Ibar(T)", lambda r: r["pI"][D]),
         band("polymer R", lambda r: r["R"])]
    verdict("CH3 Rule 30 channels like a random substrate (each measure within [0.67 min, 1.5 max] of random)",
            all(x[0] for x in b), "; ".join(x[1] for x in b))
    verdict("CH4 the polymer leans left on Rule 30: mean landing left of -0.035 T", r30["pmean"] < -0.035 * T,
            f"polymer {r30['pmean']:+.1f}, flicker {r30['fmean']:+.1f}, threshold {-0.035 * T:+.1f}; random polymers "
            + ", ".join(f"{r['pmean']:+.1f}" for r in rnd))
    cp, cf = cosine(r30["pland"], pert["pland"]), cosine(r30["fland"], pert["fland"])
    verdict("CH5 the chaos step: 1% flips move the polymer's landing law (cosine < 0.5), not the flicker's (> 0.9)",
            cp < 0.5 and cf > 0.9, f"polymer cosine {cp:.3f}, flicker cosine {cf:.3f}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


def ca_rows(rule, rng):
    """Rows 0 .. T-1 of an elementary rule (30 or 90) run from a row of fair coins; the pyramid is the cone below cell
    0 of row 0 (row t's cells -t .. t depend only on row 0's cells -2t .. 2t)."""
    W = 4 * T + 1
    row, mask = rng.getrandbits(W), (1 << W) - 1        # bit x + 2T holds cell x
    rows = []
    for t in range(T):
        r = bytearray(N)
        cells = format(row >> (2 * T - t), f"0{2 * t + 1}b")[-(2 * t + 1):][::-1].encode().translate(TO01)
        r[T + 1 - t:T + 2 + t] = cells
        rows.append(r)
        l, rr = row << 1, row >> 1
        row = ((l ^ (row | rr)) if rule == 30 else (l ^ rr)) & mask
    return rows


def path_spread(rows, rng, n=2000):
    """Var(W) / T for the white count W along n uniform random paths from the apex."""
    ws = []
    for _ in range(n):
        x, w = T + 1, 0
        for t in range(1, T):
            x += rng.randrange(-1, 2)
            w += not rows[t][x]
        ws.append(w)
    m = sum(ws) / n
    return sum((v - m) ** 2 for v in ws) / (n - 1) / T


def cause():
    rng = random.Random(1883)
    D = DEPTHS[-1]
    subs = [("Rule 30 from a single 1", rule30_rows())]
    subs += [(f"Rule 30 from a random row {k + 1}", ca_rows(30, rng)) for k in range(2)]
    subs += [(f"Rule 90 from a random row {k + 1}", ca_rows(90, rng)) for k in range(2)]
    density = 0.5017
    subs += [(f"random pyramid {k + 1}", random_rows(density, rng)) for k in range(3)]
    res = {}
    for name, rows in subs:
        cone = sum(sum(rows[t][T + 1 - t:T + 2 + t]) for t in range(T)) / (T * T)
        ps, _, R, pwhite, _ = polymer(rows)
        v = path_spread(rows, rng)
        res[name] = dict(I=ibar(ps, D), R=R, V=v)
        print(f"   {name}: density {cone:.4f}; polymer Ibar({D}) {res[name]['I']:.4f}, R {R:.3f}, white share "
              f"{pwhite:.3f}; path spread Var(W)/T {v:.4f}", flush=True)
    rnd = [res[f"random pyramid {k + 1}"] for k in range(3)]
    seed = res["Rule 30 from a single 1"]
    r30r = [res[f"Rule 30 from a random row {k + 1}"] for k in range(2)]
    r90r = [res[f"Rule 90 from a random row {k + 1}"] for k in range(2)]
    lo, hi = min(r["I"] for r in rnd), max(r["I"] for r in rnd)
    show = lambda rs, k: ", ".join(f"{r[k]:.4f}" for r in rs)
    verdict("CH6 Rule 30 from a random row channels like from a single 1 (within 1.5x) and below 0.67 x random",
            all(seed["I"] / 1.5 <= r["I"] <= 1.5 * seed["I"] and r["I"] < 0.67 * lo for r in r30r),
            f"single seed {seed['I']:.4f}; random rows {show(r30r, 'I')}; random {lo:.4f} to {hi:.4f}")
    vmin = min(r["V"] for r in rnd)
    verdict("CH7 the path spread Var(W)/T on Rule 30 is below 0.8 x every random pyramid's",
            all(r["V"] < 0.8 * vmin for r in [seed] + r30r),
            f"Rule 30 {show([seed] + r30r, 'V')}; random from {vmin:.4f}")
    verdict("CH8 Rule 90 from a random row channels like the random pyramids",
            all(0.67 * lo <= r["I"] <= 1.5 * hi for r in r90r), f"Rule 90 {show(r90r, 'I')}")


if __name__ == "__main__":
    cause() if "cause" in sys.argv[1:] else main()
