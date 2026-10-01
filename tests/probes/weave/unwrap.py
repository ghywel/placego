"""ENERGY-TRANSFER.md stage 1a: the survey's UNWRAPPING form, offline, on the default's own quarter-level flow.

    unwrap.py <workdir> <tap.glsl (flowtap.py, T1)> [cases=weave:3,weave:5,noise:5,patch:5]

The translating box of weavesweep.py (48 frames at 24, flat ground). `patch:v` is the weave box at +v with a noise patch
(96 x 64, centred) moving at -4 px/frame on its own: U3's control. The tap's field at N:N, per 1/8 cell (the reading's
own sampling), frames 6-41:
  1. the region: the largest 8-connected component of moving cells (|u| > 0.5), holes filled;
  2. the reference r: the median flow over its edge ring (cells within 2 of its boundary);
  3. the period lattice: the two strongest non-zero peaks (6-40 px) of the source frame's normalised autocorrelation
     over the region's box, if each is above 0.5; none -> no lift;
  4. the lift: w -> w + l, l the lattice vector (n a + m b, |n|,|m| <= 2) nearest r - w, only where l != 0 and the
     lifted motion matches the frames (12 x 12 mean |S_k - S_k+1(shifted)|) no worse than w does.
Reported: the core's and the ring's gross (|error| > 2 px) before and after; for the patch, the share of its cells
lifted and its error. Numbers only.
"""
import math
import os
import pathlib
import re
import subprocess
import sys

import numpy as np
from scipy import ndimage as ndi

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[2]))
import masters                                                                   # noqa: E402

work = pathlib.Path(sys.argv[1]); work.mkdir(parents=True, exist_ok=True)
TAP = pathlib.Path(sys.argv[2])
CASES = (sys.argv[3] if len(sys.argv) > 3 else "weave:3,weave:5,noise:5,patch:5").split(",")
REFINE = os.environ.get("UNWRAP_REFINE") == "1"                          # form 1r: refine the lifted motion before the guard
WIDE = int(os.environ.get("UNWRAP_WIDE", "15"))
CENTRE = os.environ.get("UNWRAP_CENTRE", "anchor")                        # stage 1c: 'cell' centres the wide median on the cell
LOCALMED = os.environ.get("UNWRAP_LOCALMED", "0") == "1"                   # v2 pooled the anchors' OWN flows (0); 1 pools their local medians                            # form 6: the reference's reach, in cells
FORM = int(os.environ.get("UNWRAP_FORM", "3"))                            # 2: the nearest lattice vector; 3: observed offsets
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
W, H, N = 1280, 720, 48
BW, BH, X0, Y0 = 320, 202, 40.0, 259.0
PW, PH, PV = 96, 64, -4.0                                                        # the independent patch (U3)
assert re.search(r"//!PARAM read_view\n(?://!.*\n)+4\n", TAP.read_text()), "the tap's read_view default is not 4"
(work / "_tap.glsl").write_text(TAP.read_text())
ys_, xs_ = np.mgrid[0:H, 0:W]
XX, YY = xs_ + 0.5, ys_ + 0.5


def rect(x0, y0, w, h):
    covx = masters.clamp01(np.minimum(x0 + w, XX + 0.5) - np.maximum(x0, XX - 0.5))
    covy = masters.clamp01(np.minimum(y0 + h, YY + 0.5) - np.maximum(y0, YY - 0.5))
    return covx * covy


def patch_x(v, t):
    """the patch starts at the box's right side at frame 6 and drifts left through it (PV - v px/frame relative)"""
    return X0 + v * t + (BW - PW - 4) + (PV - v) * (t - 6)


def frame(kind, v, t):
    tex = "noise" if kind == "noise" else "weave"
    x0 = X0 + v * t
    img = masters.clamp01(masters.tex_value(tex, XX - x0, YY - Y0) * 0.9 + 0.05) * rect(x0, Y0, BW, BH)
    if kind == "patch":                                                          # its own texture, its own motion
        px0 = patch_x(v, t); py0 = Y0 + BH / 2 - PH / 2
        c = rect(px0, py0, PW, PH)
        inner = masters.clamp01(masters.tex_value("noise", XX - px0 + 500, YY - py0 + 500) * 0.9 + 0.05)
        img = img * (1 - c) + inner * c
    return img


def field(src):
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo", "-pix_fmt",
           "gray16le", "-s", f"{W}x{H}", "-r", "24", "-i", str(src), "-vf",
           "format=rgb48le,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_tap.glsl,format=rgb48le",
           "-fps_mode", "passthrough", "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"]
    r = subprocess.run(cmd, cwd=work, capture_output=True)
    if r.returncode or b"compile status" in r.stderr: sys.exit(f"ffmpeg failed: {r.stderr[:300]}")
    fr = np.frombuffer(r.stdout, np.uint16).reshape(-1, H, W, 3)
    return [(f[4::8, 4::8, :2].astype(np.float32) / 65535.0 - 0.5) * 64.0 for f in fr]


def sample(img, X, Y):
    x = np.clip(X - 0.5, 0, W - 1.001); y = np.clip(Y - 0.5, 0, H - 1.001)
    x0 = np.floor(x).astype(int); y0 = np.floor(y).astype(int); fx = x - x0; fy = y - y0
    return ((1 - fx) * (1 - fy) * img[y0, x0] + fx * (1 - fy) * img[y0, x0 + 1]
            + (1 - fx) * fy * img[y0 + 1, x0] + fx * fy * img[y0 + 1, x0 + 1])


def lattice(img, region_px):
    ys, xs = np.nonzero(region_px)
    if len(ys) < 400: return None
    patch = img[ys.min():ys.max() + 1, xs.min():xs.max() + 1].astype(np.float64)
    msk = region_px[ys.min():ys.max() + 1, xs.min():xs.max() + 1].astype(np.float64)
    # MASKED, OVERLAP-NORMALISED autocorrelation (the second form, after stage 1a: the found region's bounding box
    # holds black ground at its margins, which diluted a plain autocorrelation until real peaks fell under the line)
    patch = (patch - patch[msk > 0].mean()) * msk
    if patch[msk > 0].std() < 1e-3: return None
    s2 = (patch.shape[0] * 2, patch.shape[1] * 2)
    F = np.fft.fft2(patch, s=s2); M = np.fft.fft2(msk, s=s2)
    num = np.fft.ifft2(F * np.conj(F)).real; ovl = np.fft.ifft2(M * np.conj(M)).real
    ac = np.where(ovl > 0.25 * ovl[0, 0], num / np.maximum(ovl, 1e-9), 0.0)
    ac /= ac[0, 0]
    ac = np.fft.fftshift(ac); cy, cx = ac.shape[0] // 2, ac.shape[1] // 2
    win = ac[cy - 40:cy + 41, cx - 40:cx + 41].copy()
    yy, xx = np.mgrid[-40:41, -40:41]
    win[np.hypot(yy, xx) < 6] = -1                                               # not the central peak
    peaks = []
    mx = ndi.maximum_filter(win, size=5)
    cand = np.argwhere((win == mx) & (win > 0.5))
    for y, x in sorted(cand, key=lambda p: -win[p[0], p[1]]):
        vec = np.array([xx[y, x], yy[y, x]], float)
        # A TRUE PERIOD (added after stage 1a: a smooth autocorrelation's highest values sit at the edge of the
        # excluded centre and read as peaks on noise): the autocorrelation must DIP between the centre and the peak,
        # to at least 0.25 below the peak, somewhere on the line joining them
        n = int(np.hypot(*vec)) * 2
        line = [ac[cy + int(round(s * vec[1])), cx + int(round(s * vec[0]))] for s in np.linspace(0.15, 0.85, max(n, 8))]
        if min(line) > win[y, x] - 0.25: continue
        if any(np.allclose(vec, -p) or np.allclose(vec, p) for p in peaks): continue
        if peaks and abs(peaks[0][0] * vec[1] - peaks[0][1] * vec[0]) < 1e-6: continue   # collinear with the first
        peaks.append(vec)
        if len(peaks) == 2: break
    if len(peaks) < 2: return None
    a, b = peaks
    def acv(vec):                                                   # the autocorrelation at an integer offset
        x, y = int(round(vec[0])), int(round(vec[1]))
        return float(ac[cy + y, cx + x]) if abs(x) < cx and abs(y) < cy else -1.0
    lattice.acv = acv
    return [n * a + m * b for n in range(-2, 3) for m in range(-2, 3)]


# FORM 1's detector, verbatim from a041d20 (the plain autocorrelation over the region's box, no dip test)
def lattice_plain(img, region_px):
    ys, xs = np.nonzero(region_px)
    if len(ys) < 400: return None
    patch = img[ys.min():ys.max() + 1, xs.min():xs.max() + 1].astype(np.float64)
    patch = patch - patch.mean()
    if patch.std() < 1e-3: return None
    F = np.fft.fft2(patch, s=(patch.shape[0] * 2, patch.shape[1] * 2))
    ac = np.fft.ifft2(F * np.conj(F)).real; ac /= ac[0, 0]
    ac = np.fft.fftshift(ac); cy, cx = ac.shape[0] // 2, ac.shape[1] // 2
    win = ac[cy - 40:cy + 41, cx - 40:cx + 41].copy()
    yy, xx = np.mgrid[-40:41, -40:41]
    win[np.hypot(yy, xx) < 6] = -1                                               # not the central peak
    peaks = []
    mx = ndi.maximum_filter(win, size=5)
    cand = np.argwhere((win == mx) & (win > 0.5))
    for y, x in sorted(cand, key=lambda p: -win[p[0], p[1]]):
        vec = np.array([xx[y, x], yy[y, x]], float)
        if any(np.allclose(vec, -p) or np.allclose(vec, p) for p in peaks): continue
        if peaks and abs(peaks[0][0] * vec[1] - peaks[0][1] * vec[0]) < 1e-6: continue   # collinear with the first
        peaks.append(vec)
        if len(peaks) == 2: break
    if len(peaks) < 2: return None
    a, b = peaks
    return [n * a + m * b for n in range(-2, 3) for m in range(-2, 3)]


def sad(k, S, cx, cy, d):
    X, Y = np.meshgrid(np.arange(cx - 6, cx + 6) + 0.5, np.arange(cy - 6, cy + 6) + 0.5)
    return float(np.mean(np.abs(sample(S[k], X, Y) - sample(S[k + 1], X + d[0], Y + d[1]))))


print(f"{'case':10s} | {'core gross: before -> after':>28s} | {'ring gross: before -> after':>28s} | {'lattice found':>13s} | patch: lifted, err before -> after")
for case in CASES:
    kind, v = case.split(":"); v = float(v)
    src = work / f"src-{kind}-{v:g}.raw"
    if not src.exists():
        with open(src, "wb") as f:
            for k in range(N): f.write(np.floor(frame(kind, v, float(k)) * 65535 + 0.5).clip(0, 65535).astype("<u2").tobytes())
    S = np.fromfile(src, "<u2").reshape(N, H, W).astype(np.float32) / 65535.0
    F = field(src)
    cy_, cx_ = np.mgrid[4:H:8, 4:W:8].astype(np.float64) + 0.5
    tally = {"core": [0, 0, 0], "ring": [0, 0, 0]}; latt = 0; patch = [0, 0, 0.0, 0.0]
    from collections import Counter; tax = Counter(); chg = [0, 0]
    for k in range(6, min(len(F), N) - 6):
        u = F[k]; mv = np.hypot(u[..., 0], u[..., 1]) > 0.5
        lab, nl = ndi.label(mv, structure=np.ones((3, 3)))
        if nl == 0: continue
        reg = ndi.binary_fill_holes(lab == 1 + int(np.argmax(ndi.sum(mv, lab, range(1, nl + 1)))))
        dist = ndi.distance_transform_edt(reg)
        ring = reg & (dist <= 2)
        r = np.median(u[ring], axis=0)
        regpx = np.repeat(np.repeat(reg, 8, 0), 8, 1)[:H, :W]
        if FORM in (5, 6):                                # stage 1b: no lattice; the reference by nearest anchor (jump flooding's result)
            L = None
        elif FORM == 4:                                     # form 4: the MASKED periodicity test gates, form 1's plain lattice lifts
            L = lattice_plain(S[k], regpx) if lattice(S[k], regpx) is not None else None
        else:
            L = lattice_plain(S[k], regpx) if FORM == 1 else lattice(S[k], regpx)
        if os.environ.get("UNWRAP_DEBUG") and k == 20:                           # one frame's anatomy
            x0d = X0 + v * k
            cored = (cx_ > x0d + 32) & (cx_ < x0d + BW - 32) & (cy_ > Y0 + 32) & (cy_ < Y0 + BH - 32) & reg
            vals, cnt = np.unique(np.round(u[cored]).astype(int), axis=0, return_counts=True)
            print(f"  [debug k 20] r = ({r[0]:+.2f},{r[1]:+.2f}); lattice basis: {None if L is None else (L[13] - L[12], L[17] - L[12])}")
            for vv, cc in sorted(zip(map(tuple, vals), cnt), key=lambda z: -z[1])[:6]:
                w = np.array(vv, float)
                l = min(L, key=lambda q: np.hypot(*(r - (w + q)))) if L is not None else np.zeros(2)
                print(f"    core w {vv}: {cc} cells; nearest lattice lift {tuple(np.round(l).astype(int))} -> {tuple(np.round(w + l).astype(int))}")
        out = u.copy()
        why = np.where(reg, 1 if L is None else 0, 0)             # 1 no lattice, 2 lift zero, 3 guard refused, 4 lifted
        changed = np.zeros(mv.shape, bool)
        if FORM in (5, 6):
            still = ~mv
            if FORM == 6:                                  # stage 1b': the 1/8 level's rival-basin test gates (ALIAS_E's offline twin)
                sys.path.insert(0, str(HERE.parents[1] / "limb")); import ambiguity as AM
                g8 = np.clip(S[k:k + 2], 0, 1)
                mg, rg8, _, _ = AM.analyse(g8, 0)
                gate = ndi.binary_dilation((mg < 0.3) & (rg8 >= 0.02), np.ones((3, 3)))[:mv.shape[0], :mv.shape[1]]
            anch = mv & ndi.binary_dilation(still, np.ones((5, 5)))              # a still cell within 2 cells
            if anch.any():
                av = np.zeros_like(u)
                for i, j in zip(*np.nonzero(anch)):                                # an anchor's value: its neighbouring anchors' median
                    sl = (slice(max(i - 2, 0), i + 3), slice(max(j - 2, 0), j + 3))
                    av[i, j] = np.median(u[sl][anch[sl]], axis=0)
                _, (ni, nj) = ndi.distance_transform_edt(~anch, return_indices=True)
                if FORM == 6:                                   # the WIDE reference: the anchors' median within +-15 cells
                    wide = {}
                for i, j in zip(*np.nonzero(mv)):
                    if FORM == 6 and not gate[i, j]: continue
                    w = u[i, j]
                    if FORM == 6:
                        a_ = (ni[i, j], nj[i, j]) if CENTRE == "anchor" else (i, j)   # 1c: centred on the cell, no jump flood
                        if a_ not in wide:
                            sl = (slice(max(a_[0] - WIDE, 0), a_[0] + WIDE + 1), slice(max(a_[1] - WIDE, 0), a_[1] + WIDE + 1))
                            src_ = av if LOCALMED else u                              # 1c: the anchor's own flow, no local median
                            wide[a_] = np.median(src_[sl][anch[sl]], axis=0) if anch[sl].any() else np.array([np.nan, np.nan])
                        if np.isnan(wide[a_][0]): continue                            # no anchor within reach: no adoption
                        rr = wide[a_]
                    else:
                        rr = av[ni[i, j], nj[i, j]]
                    grid = [rr + np.array([dx, dy]) for dy in np.arange(-1, 1.01, 0.5) for dx in np.arange(-1, 1.01, 0.5)]
                    d = min(grid, key=lambda q: sad(k, S, cx_[i, j], cy_[i, j], q))
                    if np.hypot(*(d - w)) > 2 and sad(k, S, cx_[i, j], cy_[i, j], d) <= sad(k, S, cx_[i, j], cy_[i, j], w):
                        out[i, j] = d; changed[i, j] = True; why[i, j] = 4
            latt += 1
        if L is not None and FORM == 3:
            # THE THIRD FORM (after the second's basis problem, post-hoc): the lattice test only GATES; the lifts are the
            # OBSERVED common offsets of w from r over the region, each kept only if the texture repeats there
            # (autocorrelation above 0.5): a cell displaced from its outline by a true period is lifted back by it
            latt += 1
            offs, cnt = np.unique(np.round(u[reg] - r).astype(int), axis=0, return_counts=True)
            per = [np.array(o, float) for o, c_ in zip(offs, cnt)
                   if c_ >= max(5, 0.03 * reg.sum()) and np.hypot(*o) >= 6 and lattice.acv(o) > 0.5]
            for i, j in zip(*np.nonzero(reg)):
                w = u[i, j]; o = w - r
                hit = [p_ for p_ in per if np.hypot(*(o - p_)) <= 2.0]
                if not hit: continue
                d = w - min(hit, key=lambda p_: np.hypot(*(o - p_)))
                if sad(k, S, cx_[i, j], cy_[i, j], d) <= sad(k, S, cx_[i, j], cy_[i, j], w):
                    out[i, j] = d
        elif L is not None:
            latt += 1
            for i, j in zip(*np.nonzero(reg)):
                w = u[i, j]
                l = min(L, key=lambda q: np.hypot(*(r - (w + q))))
                if np.hypot(*l) < 1e-6: why[i, j] = 2; continue
                d = w + l
                if REFINE:
                    # FORM 1r (after the taxonomy, post-hoc): the lift carries w's sub-pixel error into d, and on a steep
                    # print that costs about what the alias's own mismatch costs, so the guard became a coin toss. Lift to
                    # the basin, then REFINE to its bottom (+-1 px in half-pixel steps) before the guard compares.
                    grid = [d + np.array([dx, dy]) for dy in np.arange(-1, 1.01, 0.5) for dx in np.arange(-1, 1.01, 0.5)]
                    d = min(grid, key=lambda q: sad(k, S, cx_[i, j], cy_[i, j], q))
                if sad(k, S, cx_[i, j], cy_[i, j], d) <= sad(k, S, cx_[i, j], cy_[i, j], w):
                    out[i, j] = d; why[i, j] = 4
                else:
                    why[i, j] = 3
        x0 = X0 + v * k
        dd = np.minimum.reduce([cx_ - x0, x0 + BW - cx_, cy_ - Y0, Y0 + BH - cy_])
        inbox = (cx_ > x0) & (cx_ < x0 + BW) & (cy_ > Y0) & (cy_ < Y0 + BH)
        truth = np.zeros_like(u); truth[..., 0] = v
        inpatch = np.zeros_like(inbox)
        if kind == "patch":
            px0 = patch_x(v, k); py0 = Y0 + BH / 2 - PH / 2
            inpatch = (cx_ > px0 + 8) & (cx_ < px0 + PW - 8) & (cy_ > py0 + 8) & (cy_ < py0 + PH - 8)
            truth[inpatch, 0] = PV
            inside = (px0 >= X0 + v * k + 4) and (px0 + PW <= X0 + v * k + BW - 4)   # score it only while inside
            lifted = (changed[inpatch] if FORM == 5 else np.any(out[inpatch] != u[inpatch], axis=-1)) if inside else np.zeros(0, bool)
            if inside and inpatch.any():
                patch[0] += int(lifted.sum()); patch[1] += int(inpatch.sum()); patch.append(1)
                patch[2] += float(np.median(np.hypot(*(u[inpatch] - truth[inpatch]).T)))
                patch[3] += float(np.median(np.hypot(*(out[inpatch] - truth[inpatch]).T)))
        if os.environ.get("UNWRAP_TAXONOMY"):                                    # what stays wrong in the core, and why
            sel = inbox & (dd > 32) & ~inpatch
            e0 = np.hypot(*(u[sel] - truth[sel]).T); e1 = np.hypot(*(out[sel] - truth[sel]).T); wy = why[sel]
            bad = e1 > 2
            tax["over-read (w within 5 px of the truth, not a period)"] += int((bad & (e0 <= 5) & (out[sel] == u[sel]).all(-1)).sum())
            tax["alias unlifted: no lattice"] += int((bad & (e0 > 5) & (wy == 1)).sum())
            tax["alias unlifted: the nearest lattice lift is zero"] += int((bad & (e0 > 5) & (wy == 2)).sum())
            tax["alias unlifted: the matching guard refused"] += int((bad & (e0 > 5) & (wy == 3)).sum())
            tax["alias unlifted: outside the found region"] += int((bad & (e0 > 5) & ~reg[sel]).sum())
            tax["WRONG lift"] += int((bad & (wy == 4)).sum())
            tax["core cells"] += int(sel.sum()); tax["wrong after"] += int(bad.sum())
        chg[0] += int((changed & inbox).sum()); chg[1] += int(inbox.sum())
        for g, sel in (("core", inbox & (dd > 32) & ~inpatch), ("ring", inbox & (dd <= 16))):
            e0 = np.hypot(*(u[sel] - truth[sel]).T); e1 = np.hypot(*(out[sel] - truth[sel]).T)
            tally[g][0] += sel.sum(); tally[g][1] += int((e0 > 2).sum()); tally[g][2] += int((e1 > 2).sum())
    nfr = min(len(F), N) - 12
    c = lambda g: f"{100 * tally[g][1] / max(tally[g][0], 1):5.1f}% -> {100 * tally[g][2] / max(tally[g][0], 1):5.1f}%"
    npf = max(len(patch) - 4, 1)                                                 # frames with the patch inside
    pt = (f"{100 * patch[0] / max(patch[1], 1):5.1f}% lifted over {npf} frames, median err {patch[2] / npf:5.2f} -> {patch[3] / npf:5.2f} px"
          if kind == "patch" else "--")
    print(f"{case:10s} | {c('core'):>28s} | {c('ring'):>28s} | {latt:4d} of {nfr:3d} | {pt}", flush=True)
    if FORM in (5, 6): print(f"      the box's cells changed by more than 2 px: {100 * chg[0] / max(chg[1], 1):.1f}%")
    if os.environ.get("UNWRAP_TAXONOMY"):
        n = max(tax["core cells"], 1)
        for key in [x for x in tax if x not in ("core cells", "wrong after")]:
            print(f"      {key:55s} {100 * tax[key] / n:5.1f}% of the core ({100 * tax[key] / max(tax['wrong after'], 1):5.1f}% of what stays wrong)")
