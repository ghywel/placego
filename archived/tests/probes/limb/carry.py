#!/usr/bin/env python3
"""THE CARRY, OFFLINE: does a min-sum over each flagged cell's two hypotheses, anchored at the unambiguous cells, put
V3's interior on the right answer at every start -- and leave everything else alone? The leap PRIOR-ART.md's survey
ranks (SGM's min-sum on costs, NG-fSGM's small candidate set, the Imry-Ma rule: ambiguous data kept exactly flat), tried
in numpy before any GLSL.

The level is the QUARTER level, emulated as the shader builds it (luma at each 1/4 texel's centre, a pixel corner: the
2 x 2 average there; SAD over 5 x 5 texels), because 12 px is exactly 3 of its texels -- the 1/8 level's whole 8-px
texels cannot say 12 (ambiguity.py found its end cells confidently wrong at one start). Every shift within +-5 texels
(+-20 px) is scored; ambiguity.py's ridge test finds each cell's rival basin.
  - Every textured cell with a rival basin has two candidates, its best (cost 0) and the rival (cost = its margin, in
    units of the curve's rise). A FLAGGED cell (margin < 0.05) has them at EXACTLY equal cost (the Imry-Ma rule: a
    faint preference inside is what lets a boundary lose its grip). A cell with no rival is a hard anchor.
  - (The first form made every unflagged cell a hard anchor: the cells beside a pattern's end that half-see it came out
    confidently WRONG at margins 0.1-0.2 and won every path through them -- V1 fell from 96% to 35%.)
  - A flat cell (5 x 5 range < 0.02) carries nothing: it breaks the paths.
  - Four scans (left, right, down, up), each L(p, v) = D(p, v) + min_u [L(p - r, u) + pen(v, u)] - min_u L(p - r, u),
    pen 0 / P1 for a one-texel step / P2 beyond; the four summed; each cell takes its cheaper candidate.
Scored inside the moving rectangle (8 px in from its edges, textured cells only) against the case's law: the share of
cells within 0.75 texel of the truth, winner-takes-all (today's answer at this level, seeds aside) against the carry, frames 2-19 every
other. Real footage: the share of cells whose answer the carry changes (no truth there; small is the point).

    carry.py                     V3 at six starts, the period family and the translations
    carry.py --clips street:streetpeople-1080p.mp4:8 ...     real footage, as ambiguity.py
    carry.py --only B1_alias_over_pan V3_stairs_sq24_v12     a subset of the cases
    carry.py --eighth ...        the same at the 1/8 level (+-3 texels): 16x cheaper, but 12 px is 1.5 of its texels"""
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ambiguity as AM  # noqa: E402
import limblevels as LL  # noqa: E402

EIGHTH = "--eighth" in sys.argv       # the 1/8 level instead: 16x cheaper to search, but 12 px is 1.5 of its texels
if EIGHTH:
    sys.argv.remove("--eighth")
SCALE = 8 if EIGHTH else 4
R, TAU, P1, P2 = (3 if EIGHTH else 5), 0.05, 0.1, 1.0
LAMBDA = 1e-3      # the shader's magnitude prior in miniature: a flat window or a stripe's aperture valley picks the
                   # smallest shift (as SEED_MAG_LAMBDA does), a true tie between two aliases of equal size stays a tie
SH = [(dy, dx) for dy in range(-R, R + 1) for dx in range(-R, R + 1)]
SHA = np.array(SH)


def quarter(f):
    if EIGHTH:
        return AM.eighth(f)
    return 0.25 * (f[1::4, 1::4] + f[1::4, 2::4] + f[2::4, 1::4] + f[2::4, 2::4])


def curves(a, b):
    hh, ww = a.shape
    pb = np.pad(b, R, mode="edge")
    C = np.empty((len(SH), hh, ww), np.float32)
    for j, (dy, dx) in enumerate(SH):
        C[j] = AM.box5(np.abs(a - pb[R + dy:R + dy + hh, R + dx:R + dx + ww])) + LAMBDA * (abs(dy) + abs(dx))
    return C


def flag(C):
    """per cell: best index, rival index (-1 if none), margin"""
    i1 = C.argmin(0)
    c1 = C.min(0)
    S = np.maximum(C.mean(0) - c1, 1e-4)
    margin = np.full(c1.shape, np.inf, np.float32)
    i2 = np.full(c1.shape, -1, np.int32)
    for j1, d1 in enumerate(SH):
        cell = i1 == j1
        if not cell.any():
            continue
        cc1, ss = c1[cell], S[cell]
        best_m = np.full(cc1.shape, np.inf, np.float32)
        best_j = np.full(cc1.shape, -1, np.int32)
        for j2, d2 in enumerate(SH):
            if max(abs(d2[0] - d1[0]), abs(d2[1] - d1[1])) < 2:
                continue
            c2 = C[j2][cell]
            seg = AM.segment(d1, d2)
            ridge = np.max([C[SH.index(p)][cell] for p in seg], axis=0)
            m = np.where(ridge - np.maximum(cc1, c2) >= 0.25 * ss, (c2 - cc1) / ss, np.inf)
            better = m < best_m
            best_m = np.where(better, m, best_m)
            best_j = np.where(better, j2, best_j)
        margin[cell] = best_m
        i2[cell] = best_j
    return i1, i2, margin


def pen(v, u):
    d = np.max(np.abs(v - u), axis=-1)
    return np.where(d == 0, 0.0, np.where(d <= 1, P1, P2))


def carry(i1, i2, margin, flat):
    """min-sum over <= 2 candidates per cell, four scans; returns the chosen shift per cell (dy, dx)"""
    has = (i2 >= 0) & ~flat
    cand = np.stack([SHA[i1], SHA[np.where(has, i2, i1)]], axis=2).astype(np.float32)     # (h, w, 2, 2)
    # data: the best costs 0; the rival its margin (in units of the curve's rise), EXACTLY 0 below TAU (Imry-Ma), and
    # no rival at all is a hard anchor. A cell next to a pattern's end can be confidently wrong at a small margin; a
    # hard anchor there wins every path through it, a soft one is outvoted by the run of right cells behind it (P2).
    D = np.stack([np.zeros(i1.shape), np.where(has, np.where(margin < TAU, 0.0, margin), np.inf)], axis=2)
    total = np.zeros(D.shape)
    for axis, rev in ((1, False), (1, True), (0, False), (0, True)):
        cd, dd, fl = cand, D, flat
        if axis == 0:
            cd, dd, fl = cd.transpose(1, 0, 2, 3), dd.transpose(1, 0, 2), fl.T
        if rev:
            cd, dd, fl = cd[:, ::-1], dd[:, ::-1], fl[:, ::-1]
        L = np.zeros(dd.shape)
        prevL, prevC, prevOK = None, None, np.zeros(dd.shape[0], bool)
        for x in range(dd.shape[1]):
            cur = dd[:, x].copy()
            if prevL is not None:
                # m[v] = min_u prevL[u] + pen(cand_v, prev_u) - min prevL
                pv = np.stack([np.stack([pen(cd[:, x, v], prevC[:, u]) for u in range(2)], 1) for v in range(2)], 1)
                m = np.min(prevL[:, None, :] + pv, axis=2) - np.min(prevL, axis=1, keepdims=True)
                cur = cur + np.where(prevOK[:, None], m, 0.0)
            cur = np.where(fl[:, x][:, None], np.array([0.0, np.inf]), cur)
            L[:, x] = cur
            prevL, prevC, prevOK = np.where(np.isinf(cur), 1e9, cur), cd[:, x], ~fl[:, x]
        if rev:
            L = L[:, ::-1]
        if axis == 0:
            L = L.transpose(1, 0, 2)
        total += np.where(np.isinf(L), 1e9, L)
    pick = total.argmin(2)
    return np.where(pick[..., None] == 0, cand[:, :, 0], cand[:, :, 1])


def solve(fr, k):
    a, b = quarter(fr[k]), quarter(fr[k + 1])
    C = curves(a, b)
    i1, i2, margin = flag(C)
    flat = AM.rng5(a) < 0.02
    return SHA[i1].astype(np.float32), carry(i1, i2, margin, flat), (margin < TAU) & ~flat


CASES = [  # case, x-law, y-law, w, h, start offset for V3 or None
    ("V3_stairs_sq24_v12", "490", "{o}+288*t", 300, 300, [100, 104, 108, 112, 116, 120]),
    ("B1_alias_over_pan", "490", "100+288*t", 200, 200, None),
    ("V2_stairs_sq24_v6", "490", "100+144*t", 300, 300, None), ("V1_bars_sine24_v6", "490", "100+144*t", 300, 300, None),
    ("H2_stairs_sq24_h6", "100+144*t", "210", 300, 300, None), ("H1_bars_sine24_h6", "100+144*t", "210", 300, 300, None),
    ("L7_textured_large", "384*t", "210", 300, 300, None), ("M2_period40", "384*t", "210", 300, 300, None),
    ("M3_period16_trap", "384*t", "210", 300, 300, None), ("M1_noise_large", "384*t", "210", 300, 300, None),
    ("P1_stairs_along_v4", "100+96*t", "210", 600, 300, None), ("P2_stairs_along_v8", "100+192*t", "210", 600, 300, None),
    ("P3_stairs_along_v12", "100+288*t", "210", 600, 300, None),
    ("P5_stairs_along_v8_alias", "100+192*t", "210", 600, 300, None),
    ("L1_trans_8px", "192*t", "310", 100, 100, None), ("L2_trans_16px", "384*t", "310", 100, 100, None),
    ("L3_trans_23px", "552*t", "310", 100, 100, None), ("L8_diagonal", "384*t", "216*t", 100, 100, None),
]


def main():
    only = sys.argv[sys.argv.index("--only") + 1:] if "--only" in sys.argv else None
    if "--clips" in sys.argv:
        print("\n== real footage: the carry's changes (quarter level, every other frame of 2-19)")
        print(f"{'clip':24}{'flagged':>9}{'changed':>9}   textured cells")
        for spec in sys.argv[sys.argv.index("--clips") + 1:]:
            lab, f, sec = spec.split(":")
            fr = AM.clip_frames(LL.NP / f, float(sec))
            nf = nc = tot = 0
            for k in range(2, 19, 2):
                wta, car, flg = solve(fr, k)
                tex = AM.rng5(quarter(fr[k])) >= 0.02
                tot += tex.sum(); nf += (flg & tex).sum()
                nc += (np.any(wta != car, axis=-1) & tex).sum()
            print(f"{lab + ' ' + sec + ' s':24}{100 * nf / tot:8.1f}%{100 * nc / tot:8.2f}%   {tot}")
        return
    print(f"\n== {'1/8' if EIGHTH else 'quarter'} level, inside the rectangle: the share within 0.75 texel of the truth (every other frame of 2-19)")
    print(f"{'case':34}{'WTA':>7}{'carry':>8}{'flagged':>9}")
    for case, xl, yl, w, h, offs in CASES:
        if only and case not in only:
            continue
        for off in (offs or [None]):
            s = AM.scene(case, off) if off is not None else AM.scene(case)
            fr = AM.frames(s)
            yl_ = yl.format(o=off) if off is not None else yl
            pos = lambda law, k: eval(law, {"t": k / 24.0})
            ok_w = ok_c = n = nf = 0
            for k in range(2, 19, 2):
                xa, ya = pos(xl, k), pos(yl_, k)
                if xa + w > AM.W or ya + h > AM.H:
                    continue
                truth = np.array([pos(yl_, k + 1) - ya, pos(xl, k + 1) - xa]) / SCALE
                wta, car, flg = solve(fr, k)
                sl = (slice(int(ya + 8) // SCALE, int(ya + h - 8) // SCALE), slice(int(xa + 8) // SCALE, int(xa + w - 8) // SCALE))
                tex = AM.rng5(quarter(fr[k]))[sl] >= 0.02
                ok_w += ((np.max(np.abs(wta[sl] - truth), axis=-1) <= 0.75) & tex).sum()
                ok_c += ((np.max(np.abs(car[sl] - truth), axis=-1) <= 0.75) & tex).sum()
                nf += (flg[sl] & tex).sum(); n += tex.sum()
            lab = case + (f" start {off}" if off is not None else "")
            print(f"{lab:34}{100 * ok_w / n:6.0f}%{100 * ok_c / n:7.0f}%{100 * nf / n:8.0f}%", flush=True)


if __name__ == "__main__":
    main()
