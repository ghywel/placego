#!/usr/bin/env python3
"""THE CARRY AND THE APERTURE, OFFLINE (2026-09-28): B1 moving up holds 21.8 on the cage with the carry, moving down 25.3.
ownerdump.py read the carry's own inputs cell by cell: at a pattern's ends, and in the interior within reach of them,
the RIGHT alias's hypothesis carries a junk horizontal component -- inside horizontal stripes x is unmeasurable (the
aperture), and the background in the window pulls it -- while the wrong alias maps the background onto bars, which are
x-free, so it keeps x = 0. The carry's penalty compares whole vectors, so the right chain pays P2 at every junk step
and the clean wrong one pays nothing: the scans carry the wrong alias in from the ends.

The perception literature's answer to the aperture (Adelson & Movshon's intersection of constraints; the normal-flow
view of optical flow): a cell can only vouch for the component of motion ALONG its gradient. Here the penalty between
two hypotheses ignores the component of their difference along the cell's stripes -- the structure tensor's minor
axis over the 5 x 5 window, weighted by its coherence (smoothstep 0.5 -> 0.9), the more coherent of the two cells
deciding. On isotropic texture nothing changes. (Not the refuted structure-tensor FILL of gen_aperture.py, nor the
normal-flow projection of the output on C3: this changes only which of a tied cell's two aliases the carry picks.)

carry.py's quarter-level emulation (every shift within +-5 texels, the ridge test's rival, four scans), scored the same
way: the share of the rectangle's textured cells within 0.75 texel of the truth, winner-takes-all / the carry / the
carry with the aperture rule, as the whole vector | the vertical component alone. Both directions for V3 and B1; the
period family and the translations moving as the ladder moves them.

    apcarry.py                    V3 (three starts) and B1, both ways, and the rest of carry.py's cases
    apcarry.py --only B1 V3       a subset (prefixes)
    apcarry.py --clips street:streetpeople-1080p.mp4:8 ...     real footage: the share of cells each carry changes"""
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ambiguity as AM  # noqa: E402
import carry as CA  # noqa: E402
import limblevels as LL  # noqa: E402

P1, P2, TAU, SHA = CA.P1, CA.P2, CA.TAU, CA.SHA


def aperture(a):
    """per cell, (dy, dx): the stripe direction (the structure tensor's minor eigenvector) times sqrt(coherence')"""
    gy = np.zeros_like(a); gx = np.zeros_like(a)
    gy[1:-1] = 0.5 * (a[2:] - a[:-2]); gx[:, 1:-1] = 0.5 * (a[:, 2:] - a[:, :-2])
    jyy, jxx, jxy = AM.box5(gy * gy), AM.box5(gx * gx), AM.box5(gx * gy)
    coh = np.sqrt((jxx - jyy) ** 2 + 4 * jxy ** 2) / (jxx + jyy + 1e-9)
    th = 0.5 * np.arctan2(2 * jxy, jxx - jyy)            # the dominant gradient's angle (x, y)
    ex, ey = -np.sin(th), np.cos(th)                    # the stripes run perpendicular to it
    s = np.clip((coh - 0.5) / 0.4, 0.0, 1.0)
    s = s * s * (3 - 2 * s)
    return np.stack([ey, ex], axis=-1) * np.sqrt(s)[..., None]


def pen(v, u, w):
    m = v - u
    if w is not None:
        m = m - np.sum(m * w, axis=-1, keepdims=True) * w
    d = np.max(np.abs(m), axis=-1)
    return np.where(d < 0.5, 0.0, np.where(d < 1.5, P1, P2))


def carry(i1, i2, margin, flat, W):
    """carry.py's carry, the penalty optionally aperture-aware (W per cell, or None)"""
    has = (i2 >= 0) & ~flat
    cand = np.stack([SHA[i1], SHA[np.where(has, i2, i1)]], axis=2).astype(np.float32)
    D = np.stack([np.zeros(i1.shape), np.where(has, np.where(margin < TAU, 0.0, margin), np.inf)], axis=2)
    Wz = np.zeros(i1.shape + (2,)) if W is None else W
    total = np.zeros(D.shape)
    for axis, rev in ((1, False), (1, True), (0, False), (0, True)):
        cd, dd, fl, ww = cand, D, flat, Wz
        if axis == 0:
            cd, dd, fl, ww = cd.transpose(1, 0, 2, 3), dd.transpose(1, 0, 2), fl.T, ww.transpose(1, 0, 2)
        if rev:
            cd, dd, fl, ww = cd[:, ::-1], dd[:, ::-1], fl[:, ::-1], ww[:, ::-1]
        L = np.zeros(dd.shape)
        prevL, prevC, prevOK = None, None, np.zeros(dd.shape[0], bool)
        for x in range(dd.shape[1]):
            cur = dd[:, x].copy()
            if prevL is not None:
                wx = None
                if W is not None:          # the more coherent of the two cells decides what neither can see
                    wc, wp = ww[:, x], ww[:, x - 1]
                    wx = np.where((np.sum(wc * wc, -1) >= np.sum(wp * wp, -1))[:, None], wc, wp)
                pv = np.stack([np.stack([pen(cd[:, x, v], prevC[:, u], wx) for u in range(2)], 1) for v in range(2)], 1)
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
    a, b = CA.quarter(fr[k]), CA.quarter(fr[k + 1])
    C = CA.curves(a, b)
    i1, i2, margin = CA.flag(C)
    flat = AM.rng5(a) < 0.02
    return SHA[i1].astype(np.float32), carry(i1, i2, margin, flat, None), carry(i1, i2, margin, flat, aperture(a))


def okw(v, truth, sl, tex):
    """the whole vector within 0.75 texel of the truth (carry.py's score)"""
    return ((np.max(np.abs(v[sl] - truth), axis=-1) <= 0.75) & tex).sum()


def okv(v, truth, sl, tex):
    """the vertical component alone within 0.75 texel (which ALIAS; x inside stripes is the aperture's)"""
    return ((np.abs(v[sl][..., 0] - truth[0]) <= 0.75) & tex).sum()


def main():
    if "--clips" in sys.argv:
        print("\n== real footage: the share of textured quarter cells each carry changes (every other frame of 2-19)")
        print(f"{'clip':24}{'carry':>9}{'+aperture':>11}   textured cells")
        for spec in sys.argv[sys.argv.index("--clips") + 1:]:
            lab, f, sec = spec.split(":")
            fr = AM.clip_frames(LL.NP / f, float(sec))
            n1 = n2 = tot = 0
            for k in range(2, 19, 2):
                wta, c1, c2 = solve(fr, k)
                tex = AM.rng5(CA.quarter(fr[k])) >= 0.02
                tot += tex.sum()
                n1 += (np.any(wta != c1, axis=-1) & tex).sum(); n2 += (np.any(wta != c2, axis=-1) & tex).sum()
            print(f"{lab + ' ' + sec + ' s':24}{100 * n1 / tot:8.2f}%{100 * n2 / tot:10.2f}%   {tot}", flush=True)
        return
    only = sys.argv[sys.argv.index("--only") + 1:] if "--only" in sys.argv else None
    print("\n== quarter level, inside the rectangle: the share within 0.75 texel of the truth (whole vector | vertical "
          "alone), every other frame of 2-19")
    print(f"{'case':36}{'WTA':>13}{'carry':>13}{'+aperture':>13}")
    cases = []
    for case, xl, yl, w, h, offs in CA.CASES:
        if only and not case.startswith(tuple(only)):
            continue
        if case.startswith("V3"):
            offs = [100, 108, 112]
        for off in (offs or [None]):
            cases.append((case, xl, yl, w, h, off, False))
            if case.startswith(("V3", "B1")):
                cases.append((case, xl, yl, w, h, off, True))
    for case, xl, yl, w, h, off, up in cases:
        s = AM.scene(case, off) if off is not None else AM.scene(case)
        yl_ = yl.format(o=off) if off is not None else yl
        if up:                              # mirrored: the patch starts 288 px lower and moves up
            o0 = off if off is not None else 100
            n0 = s.count(f"{o0}+288*T") + s.count(f"{o0}+288*t")
            assert n0 in (1, 3), (case, n0)
            s = s.replace(f"{o0}+288*T", f"{o0 + 288}-288*T").replace(f"{o0}+288*t", f"{o0 + 288}-288*t")
            yl_ = f"{o0 + 288}-288*t"
        fr = AM.frames(s)
        pos = lambda law, k: eval(law, {"t": k / 24.0})
        n = 0
        acc = np.zeros(6)
        for k in range(2, 19, 2):
            xa, ya = pos(xl, k), pos(yl_, k)
            if xa + w > AM.W or ya + h > AM.H or ya < 0:
                continue
            truth = np.array([pos(yl_, k + 1) - ya, pos(xl, k + 1) - xa]) / CA.SCALE
            wta, c1, c2 = solve(fr, k)
            sl = (slice(int(ya + 8) // CA.SCALE, int(ya + h - 8) // CA.SCALE),
                  slice(int(xa + 8) // CA.SCALE, int(xa + w - 8) // CA.SCALE))
            tex = AM.rng5(CA.quarter(fr[k]))[sl] >= 0.02
            for j, v in enumerate((wta, c1, c2)):
                acc[2 * j] += okw(v, truth, sl, tex); acc[2 * j + 1] += okv(v, truth, sl, tex)
            n += tex.sum()
        lab = case + (f" start {off}" if off is not None else "") + (" UP" if up else "")
        print(f"{lab:36}" + "".join(f"{100 * acc[2 * j] / n:6.0f}% |{100 * acc[2 * j + 1] / n:4.0f}%" for j in range(3)),
              flush=True)


if __name__ == "__main__":
    main()
