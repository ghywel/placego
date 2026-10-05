#!/usr/bin/env python3
"""rule30_triangles.py: the white triangles of the right side, and how they relate to the wheel's kicks.

RUN-ON:     cpu (pure Python 3, standard library; seeded random right halves)
COMMAND:    python3 tests/probes/lexicon/rule30_triangles.py [N=1200] [T=3000]
COST:       about five minutes on one core. Writes rule30_triangles_kicks.png next to this script.

The owner's lead (2026-10-05): "there are valley defined similar structures such as white triangles that appear in
the pattern. Is it possible to track similar structures (same size triangle, different location), building a graph
of where those structures appear and how they relate to the kick?"

The object. In Rule 30 a maximal run of n >= 2 zeros [a, b], bounded by ones, becomes exactly [a + 1, b - 1] one step
later: x'(a) = 1 XOR (0 OR x(a+1)) = 1 when n >= 2, x'(b) = 0 XOR (0 OR 1) = 1, and the inside has three zero parents.
So every white triangle is an exact isosceles triangle, fixed by its birth: the row t where the run [a, b] appears
without the run [a - 1, b + 1] above it. The zero runs of the forced left half that the ladder measured (sections 8.12
to 8.16) are the bases of such triangles at time 0. Here they are followed in the right side's space-time, with
column 0 clamped to 0101..., where column 1 runs the wheel U and is kicked when a domain wall arrives (section 8.8).

An exploratory look (2026-10-05, 500 seeds, not recorded): inside the wheel's domain (the first few columns) births
have sizes 2 and 3 almost only; deeper in, sizes fall off by about a factor 4 per 2 cells; and the density of births
in columns 9 to 30 in the 48 steps before a kick is within about 10% of the density at random times, with a
footprint (fewer births, then more) only along the last 20 steps of the wall's path. TK1 below re-checks the second
point on fresh seeds; TR0, TK2 and TK3 are new.

Kicks. A departure is the first time t1 at which column 1 differs from U continued at the phase d of the last exact
window; its class is (t1 - d) mod 56 (32 and 52 are the two wall species of section 8.8). After a departure the phase
is found again at the next 56-step window equal to a rotation of U (phase d').

PREDICTIONS, written 2026-10-05 before this script's first run:
  TR0 (control, exact: the shrink theorem): in every simulated space-time, every maximal zero run of at least 2 cells
      clear of column 1 and of the edge is followed by ones at both its ends and zeros inside. The counterfactual
      must be caught: the same check fails for Rule 110, in which 100 maps to 0.
  TK1 (seen in the exploration, checked on fresh seeds): interior triangles do not foretell kicks. Pooled over columns
      12 to 30 and the 36 steps from t1 - 48 to t1 - 13, births of size >= 4 near kicks of each class have a density
      within 10% of the density at random times.
  TK2 (blind; the wall's strip): along the wall's path, cells a = 1 + (t1 - t) / 2 +- 1 for t from t1 - 20 to t1 - 4,
      births of size >= 4 are at most 0.6 times as dense as at random times, for each class.
  TK3 (blind; the owner's graph): same-size triangles in columns 2 to 4 form a lattice that repeats every 56 steps in
      an exact stretch, and a kick is a dislocation of it. Take kicks with an exact window just before the departure
      and an exact window after re-locking. (a) For at least 50% of them the set of births (phase (t - d) mod 56, a, n)
      in the window before equals the set (phase (t - d') mod 56, a, n) in the window after: the same lattice, shifted
      in time by the kick. (50%, not more: an exploratory look found columns beyond 3 or 4 often off the period even
      while column 1 is exact.) (b) The counterfactual: read the window after at the old phase d, as if there had been
      no kick, and the sets agree for at most 10% of the kicks with d' != d.
REFUTED-BY: TR0 failing, or its counterfactual not caught (the instrument); TK1, TK2 or TK3 failing.
"""
import pathlib, random, struct, sys, zlib
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
T = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
_argv, sys.argv = sys.argv, sys.argv[:1]
import rule30_wheel_left as wl                         # noqa: E402
sys.argv = _argv
U = [int(c) for c in wl.U]
P = 56
ROT = {tuple(U[(t - d) % P] for t in range(P)): d for d in range(P)}
C = 34
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def spacetime(R, steps, rule=30):
    width = R.bit_length() + steps + 3
    mask = (1 << width) - 1
    row, rows = R << 1, []
    for t in range(steps):
        rows.append(row)
        l, r = (row << 1) & mask, row >> 1
        if rule == 30:
            new = l ^ (row | r)
        else:                                            # Rule 110: 1 for (l, c, r) in 110, 101, 011, 010, 001
            new = ((row | r) & ~(l & row & r)) & mask
        row = (new & mask & ~1) | ((t + 1) % 2)
    return rows, width


def runs(row, lo, hi):
    """Maximal zero runs [a, b] with lo <= a, b < hi, bounded by ones at a - 1 and b + 1."""
    out, c = [], lo
    while c < hi:
        if (row >> c) & 1 == 0 and (row >> (c - 1)) & 1 == 1:
            b = c
            while b + 1 < hi and (row >> (b + 1)) & 1 == 0:
                b += 1
            if b + 1 < hi and (row >> (b + 1)) & 1 == 1:
                out.append((c, b))
            c = b + 1
        else:
            c += 1
    return out


def shrink_violations(rows, width):
    bad = total = 0
    for t in range(len(rows) - 1):
        hi = min(width - 2, 2 + (t + 40))
        for a, b in runs(rows[t], 2, hi):
            if b - a + 1 < 2:
                continue
            total += 1
            nxt = rows[t + 1]
            ok = (nxt >> a) & 1 == 1 and (nxt >> b) & 1 == 1 and all((nxt >> j) & 1 == 0 for j in range(a + 1, b))
            bad += not ok
    return bad, total


def births(rows):
    out = {}
    for t in range(1, len(rows)):
        q = rows[t - 1]
        for a, b in runs(rows[t], 2, C):
            n = b - a + 1
            if n >= 2 and not all((q >> j) & 1 == 0 for j in range(a - 1, b + 2)):
                out.setdefault(t, []).append((a, n))
    return out


def kicks(col1):
    """(t1, d, class, t2, d2): departure at t1 from phase d; re-locked at the window [t2, t2 + 56) with phase d2."""
    out, t, d, last = [], 0, None, None
    while t + P <= len(col1):
        if d is None:
            w = tuple(col1[t:t + P])
            if w in ROT:
                if last is not None:
                    out.append(last + (t, ROT[w]))
                    last = None
                d = ROT[w]
                t += P
            else:
                t += 1
            continue
        if col1[t] != U[(t - d) % P]:
            last = (t, d, (t - d) % P)
            d = None
        t += 1
    return out


def png(path, pixels, w, h):
    raw = b"".join(b"\x00" + bytes(pixels[y * w * 3:(y + 1) * w * 3]) for y in range(h))
    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff)
    pathlib.Path(path).write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
                                   + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def main():
    rng = random.Random(1990)
    bad = tot = 0
    bad110 = tot110 = 0
    near = {32: Counter(), 52: Counter()}
    ref = Counter()
    nk = {32: 0, 52: 0}
    nref = 0
    tk3_n = tk3_ok = tk3_cf_n = tk3_cf = 0
    example = None
    for i in range(N):
        R = rng.getrandbits(48) | (1 << 47)
        rows, width = spacetime(R, T)
        if i < 40:
            b_, t_ = shrink_violations(rows[:600], width)
            bad += b_
            tot += t_
            rows110, w110 = spacetime(R, 400, rule=110)
            b_, t_ = shrink_violations(rows110, w110)
            bad110 += b_
            tot110 += t_
        col1 = [(r >> 1) & 1 for r in rows]
        B = births(rows)
        for (t1, d, cl, t2, d2) in kicks(col1):
            if t1 < 300 or t1 > T - 70 or cl not in near:
                continue
            nk[cl] += 1
            for dt in range(-60, 9):
                for a, n in B.get(t1 + dt, []):
                    near[cl][(dt, a, min(n, 8))] += 1
            for _ in range(3):
                tr = rng.randrange(300, T - 70)
                nref += 1
                for dt in range(-60, 9):
                    for a, n in B.get(tr + dt, []):
                        ref[(dt, a, min(n, 8))] += 1
            if t1 >= P and tuple(col1[t1 - P:t1]) in ROT and ROT[tuple(col1[t1 - P:t1])] == d:
                before = {((t - d) % P, a, n) for t in range(t1 - P, t1) for a, n in B.get(t, []) if a + n - 1 <= 4}
                after = {((t - d2) % P, a, n) for t in range(t2, t2 + P) for a, n in B.get(t, []) if a + n - 1 <= 4}
                tk3_n += 1
                tk3_ok += before == after
                if d2 != d:
                    tk3_cf_n += 1
                    tk3_cf += before == {((t - d) % P, a, n) for t in range(t2, t2 + P) for a, n in B.get(t, [])
                                         if a + n - 1 <= 4}
                if example is None and before == after and t2 - t1 < 200:
                    example = (rows, t1, t2, B)
    report("TR0 the shrink theorem holds in Rule 30", bad == 0 and tot > 0, f"{bad} violations among {tot} runs")
    report("TR0 counterfactual caught: Rule 110 breaks it", bad110 > 0, f"{bad110} violations among {tot110} runs")

    def ratio(cl, cond):
        k = sum(v for key, v in near[cl].items() if cond(*key))
        r = sum(v for key, v in ref.items() if cond(*key)) * nk[cl] / max(nref, 1)
        return k / r if r else float("nan"), k, r
    print(f"   kicks: class 32 {nk[32]}, class 52 {nk[52]}; reference times {nref}")
    t1res = {cl: ratio(cl, lambda dt, a, n: 12 <= a <= 30 and -48 <= dt <= -13 and n >= 4) for cl in near}
    verdict("TK1 interior triangles do not foretell kicks (pooled density within 10%)",
            all(0.9 <= v[0] <= 1.1 for v in t1res.values()),
            "; ".join(f"class {cl}: {v[0]:.3f} ({v[1]} vs {v[2]:.0f})" for cl, v in t1res.items()))
    t2res = {cl: ratio(cl, lambda dt, a, n: -20 <= dt <= -4 and abs(a - (1 + (-dt) / 2)) <= 1 and n >= 4)
             for cl in near}
    verdict("TK2 the wall's strip holds few large triangles (at most 0.6 of random)",
            all(v[0] <= 0.6 for v in t2res.values()),
            "; ".join(f"class {cl}: {v[0]:.3f} ({v[1]} vs {v[2]:.0f})" for cl, v in t2res.items()))
    verdict("TK3 a kick is a dislocation of the triangle lattice: same set at the new phase >= 50%, at the old <= 10%",
            tk3_n > 0 and tk3_ok / tk3_n >= 0.5 and tk3_cf_n > 0 and tk3_cf / tk3_cf_n <= 0.1,
            f"new phase {tk3_ok} of {tk3_n} ({tk3_ok / max(tk3_n, 1):.1%}); old phase {tk3_cf} of {tk3_cf_n} "
            f"({tk3_cf / max(tk3_cf_n, 1):.1%})")

    # Figure: left, an example space-time (columns 0..60, a window around a kick), triangles by size;
    # right, the kick-aligned excess of births of size >= 3 for each class (columns 1..30, dt -60..8).
    W1, H1 = 61, 0
    img_rows = []
    if example:
        rows, t1, t2, B = example
        lo, hi = max(0, t1 - 150), min(len(rows), t2 + 120)
        tri = {}
        for t in range(lo, hi):
            for a, n in B.get(t, []):
                for h in range((n + 1) // 2):
                    for j in range(a + h, a + n - h):
                        if t + h < hi:
                            tri[(t + h, j)] = n
        for t in range(lo, hi):
            line = []
            for c in range(W1):
                if c == 1 and t in (t1, t2):
                    line.append((220, 30, 30))
                elif (rows[t] >> c) & 1:
                    line.append((25, 25, 25))
                elif (t, c) in tri:
                    n = tri[(t, c)]
                    line.append((255, 225, 120) if n <= 3 else ((120, 200, 255) if n <= 6 else (60, 110, 230)))
                else:
                    line.append((250, 250, 250))
            img_rows.append(line)
        H1 = hi - lo
    maps = []
    for cl in (32, 52):
        m = []
        for dt in range(-60, 9):
            line = []
            for a in range(1, 31):
                k = sum(near[cl][(dt, a, n)] for n in range(3, 9))
                r = sum(ref[(dt, a, n)] for n in range(3, 9)) * nk[cl] / max(nref, 1)
                x = (k + 1) / (r + 1)
                if x >= 1:
                    v = min(1.0, (x - 1) / 2)
                    line.append((255, int(255 * (1 - v)), int(255 * (1 - v))))
                else:
                    v = min(1.0, (1 - x) * 2)
                    line.append((int(255 * (1 - v)), int(255 * (1 - v)), 255))
            m.append(line)
        maps.append(m)
    S = 3
    width = (W1 + 4 + 30 + 4 + 30) * S
    height = max(H1, 69) * S
    pix = [255] * (width * height * 3)
    def put(x0, y0, block):
        for y, line in enumerate(block):
            for x, rgb in enumerate(line):
                for dy in range(S):
                    for dx in range(S):
                        o = (((y0 + y) * S + dy) * width + (x0 + x) * S + dx) * 3
                        pix[o:o + 3] = list(rgb)
    if img_rows:
        put(0, 0, img_rows)
    put(W1 + 4, 0, maps[0])
    put(W1 + 4 + 30 + 4, 0, maps[1])
    png(HERE / "rule30_triangles_kicks.png", pix, width, height)
    print("   wrote rule30_triangles_kicks.png: left, a space-time around a kick (column 0 at the left edge; black ones;"
          " triangles yellow for sizes 2-3, light blue 4-6, blue 7+; red marks on column 1 at the departure and at"
          " re-locking); middle and right, the excess of births of size >= 3 around kicks of class 32 and 52 (rows"
          " t1 - 60 .. t1 + 8 downwards, columns 1 .. 30; red above random, blue below)")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
