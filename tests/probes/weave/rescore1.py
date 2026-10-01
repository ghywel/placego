"""NFRAME-LIMITS, the weave, lead 4's step 1: the fine re-score, offline, on the default's own quarter flow (F1-F3).

    rescore1.py <workdir> <tap.glsl (flowtap.py, T2)> [cases=weave:11,weave:13,weave:19,weave:3,weave:5,noise:11,noise:19]

weavesweep.py's sources and scene (the translating box). The tap's field at N:N per 1/8 cell (frames 10-30, every
second one). For each moving cell:
  1. THE LATTICE, per cell, deterministic: the self-match of the cell's 32 x 32 neighbourhood of frame k against
     itself over shifts of 8-40 px (by FFT, as SSD: SSD(s) = sum a^2 + sum b^2 - 2 AC(s) over the overlap); the two
     lowest non-collinear shifts, kept if their mean squared difference is under 0.3 of the neighbourhood's variance.
     None -> no candidates but w.
  2. THE CANDIDATES: w, w +- p1, w +- p2; each scored at integer px by a 16 x 16 full-resolution SAD (S_k at the
     cell, S_k+1 shifted); the two best of the aliases and w itself refined +-1 px in half-pixel steps.
  3. THE PICK: the best replaces w only if it beats w's refined cost by at least 0.004 luma (1/255).
Reported: the core's and the box's gross (|error| > 2 px) before and after, cells changed, and the lattice-found rate.
Numbers only. (The pre-registration said SAD for the self-match; it is computed as SSD by FFT, for speed.)
"""
import os
import pathlib
import re
import subprocess
import sys

import numpy as np

W, H, N = 1280, 720, 48
BW, BH, X0, Y0 = 320, 202, 40.0, 259.0
work = pathlib.Path(sys.argv[1]); work.mkdir(parents=True, exist_ok=True)
TAP = pathlib.Path(sys.argv[2])
CASES = (sys.argv[3] if len(sys.argv) > 3 else "weave:11,weave:13,weave:19,weave:3,weave:5,noise:11,noise:19").split(",")
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
# weavesweep.py's sources: $NP_SCRATCH/weave/sweep, NP_SCRATCH defaulting to np-scratch beside the repository checkout
NP = pathlib.Path(os.environ.get("NP_SCRATCH", str(pathlib.Path(__file__).resolve().parents[5] / "np-scratch")))
SRC = str(NP / "weave/sweep")
assert re.search(r"//!PARAM read_view\n(?://!.*\n)+4\n", TAP.read_text()), "the tap's read_view default is not 4"
(work / "_tap.glsl").write_text(TAP.read_text())


def field(src):
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo", "-pix_fmt",
           "gray16le", "-s", f"{W}x{H}", "-r", "24", "-i", str(src), "-vf",
           "format=rgb48le,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_tap.glsl,format=rgb48le",
           "-fps_mode", "passthrough", "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"]
    r = subprocess.run(cmd, cwd=work, capture_output=True)
    if r.returncode or b"compile status" in r.stderr: sys.exit(f"ffmpeg failed: {r.stderr[:300]}")
    fr = np.frombuffer(r.stdout, np.uint16).reshape(-1, H, W, 3)
    out = [(f[4::8, 4::8, :2].astype(np.float32) / 65535.0 - 0.5) * 64.0 for f in fr]
    return [unbleed(f) for f in out] if UNBLEED else out


# THE READ'S BLEED (2026-10-01, found by G1): the reading samples its 1/8 field at pixel 8i + 4.5, so each cell's value
# carries 1/16 of the next cell's, right and below (bilinear). Every step from 1b to 1q took its input field that
# way, which handed each cell slightly perturbed neighbour flows. RESCORE_UNBLEED=1 deconvolves it (exact under the
# bilinear model; six Jacobi sweeps); the default stays the recorded steps' instrument.
UNBLEED = os.environ.get("RESCORE_UNBLEED", "0") == "1"


def unbleed(r):
    a, b = 15 / 16, 1 / 16
    v = r.copy()
    for _ in range(6):
        sx = np.concatenate([v[:, 1:], v[:, -1:]], 1); sy = np.concatenate([v[1:], v[-1:]], 0)
        sxy = np.concatenate([sy[:, 1:], sy[:, -1:]], 1)
        v = (r - a * b * sx - a * b * sy - b * b * sxy) / (a * a)
    return v


def sad(a, b, cx, cy, d):
    """16 x 16 mean |a - b(shifted by d)| around (cx, cy), bilinear in b"""
    x0, y0 = int(cx) - 8, int(cy) - 8
    fx, fy = x0 + d[0], y0 + d[1]
    ix, iy = int(np.floor(fx)), int(np.floor(fy)); ax, ay = fx - ix, fy - iy
    if x0 < 0 or y0 < 0 or ix < 0 or iy < 0 or ix + 17 > W or iy + 17 > H or x0 + 16 > W or y0 + 16 > H: return np.inf
    p = ((1 - ax) * (1 - ay) * b[iy:iy + 16, ix:ix + 16] + ax * (1 - ay) * b[iy:iy + 16, ix + 1:ix + 17]
         + (1 - ax) * ay * b[iy + 1:iy + 17, ix:ix + 16] + ax * ay * b[iy + 1:iy + 17, ix + 1:ix + 17])
    return float(np.mean(np.abs(a[y0:y0 + 16, x0:x0 + 16] - p)))


_sy, _sx = np.mgrid[-31:32, -31:32]
_keep = (np.hypot(_sx, _sy) >= 8) & (np.hypot(_sx, _sy) <= 40)
SX, SY = _sx[_keep], _sy[_keep]                               # the candidate lattice shifts, px


def sad_sparse(a, b, cx, cy, d):
    """COST CUT (1p): sad() on every other pixel of the same 16 x 16 block (8 x 8 samples), bilinear in b"""
    x0, y0 = int(cx) - 8, int(cy) - 8
    fx, fy = x0 + d[0], y0 + d[1]
    ix, iy = int(np.floor(fx)), int(np.floor(fy)); ax, ay = fx - ix, fy - iy
    if x0 < 0 or y0 < 0 or ix < 0 or iy < 0 or ix + 17 > W or iy + 17 > H or x0 + 16 > W or y0 + 16 > H: return np.inf
    p = ((1 - ax) * (1 - ay) * b[iy:iy + 16:2, ix:ix + 16:2] + ax * (1 - ay) * b[iy:iy + 16:2, ix + 1:ix + 17:2]
         + (1 - ax) * ay * b[iy + 1:iy + 17:2, ix:ix + 16:2] + ax * ay * b[iy + 1:iy + 17:2, ix + 1:ix + 17:2])
    return float(np.mean(np.abs(a[y0:y0 + 16:2, x0:x0 + 16:2] - p)))


def sad4(a, b, cx, cy, d):
    """COST C1: sad() on 4 x 4 samples at 4 px within the same 16 x 16 block, bilinear in b"""
    x0, y0 = int(cx) - 8, int(cy) - 8
    fx, fy = x0 + d[0], y0 + d[1]
    ix, iy = int(np.floor(fx)), int(np.floor(fy)); ax, ay = fx - ix, fy - iy
    if x0 < 0 or y0 < 0 or ix < 0 or iy < 0 or ix + 17 > W or iy + 17 > H or x0 + 16 > W or y0 + 16 > H: return np.inf
    p = ((1 - ax) * (1 - ay) * b[iy:iy + 16:4, ix:ix + 16:4] + ax * (1 - ay) * b[iy:iy + 16:4, ix + 1:ix + 17:4]
         + (1 - ax) * ay * b[iy + 1:iy + 17:4, ix:ix + 16:4] + ax * ay * b[iy + 1:iy + 17:4, ix + 1:ix + 17:4])
    return float(np.mean(np.abs(a[y0:y0 + 16:4, x0:x0 + 16:4] - p)))


def lattice(img, cx, cy):
    x0, y0 = int(cx) - 16, int(cy) - 16
    if x0 < 0 or y0 < 0 or x0 + 32 > W or y0 + 32 > H: return None
    P = img[y0:y0 + 32, x0:x0 + 32].astype(np.float64); P = P - P.mean(); var = P.var()
    if var < 1e-5: return None
    F = np.fft.fft2(P, s=(64, 64)); ac = np.fft.ifft2(F * np.conj(F)).real
    M = np.fft.fft2(np.ones((32, 32)), s=(64, 64)); ov = np.fft.ifft2(M * np.conj(M)).real
    sq = np.fft.ifft2(np.fft.fft2(P * P, s=(64, 64)) * np.conj(M)).real        # sum of a^2 over the overlap (a's side)
    sq2 = np.fft.ifft2(M * np.conj(np.fft.fft2(P * P, s=(64, 64)))).real      # and b's side
    msd = np.where(ov > 64, (sq + sq2 - 2 * ac) / np.maximum(ov, 1), np.inf)  # the mean squared difference at each shift
    vals = msd[SY % 64, SX % 64]                              # every shift of 8-40 px at once (vectorised)
    order = np.argsort(vals)
    ok = vals[order] < 0.3 * var
    if not ok.any(): return None
    cand = order[ok]
    p1 = np.array([SX[cand[0]], SY[cand[0]]], float)
    for c in cand[1:]:
        v = np.array([SX[c], SY[c]], float)
        if abs(p1[0] * v[1] - p1[1] * v[0]) > 1e-6: return p1, v
    return None


def refine(a, b, cx, cy, d):
    best, bc = d, sad(a, b, cx, cy, d)
    for dy in np.arange(-1, 1.01, 0.5):
        for dx in np.arange(-1, 1.01, 0.5):
            q = d + np.array([dx, dy]); c = sad(a, b, cx, cy, q)
            if c < bc: best, bc = q, c
    return best, bc


TAX = os.environ.get("RESCORE_TAX") == "1"
LATTICE = os.environ.get("RESCORE_LATTICE", "cell")                  # cell: the per-cell FFT; coarse 1e, two 1f, tile 1g, rival 1h, rival2 1i, rival3 1j
STEP = os.environ.get("RESCORE_STEP", "1c")                           # 1b, 1c (the default), 1d (+ the uniqueness test), 1k
STEP1C = STEP in ("1c", "1d", "1k", "1k2")                             # 1c, 1d, 1k and 1k2 refine before ranking
# THE COST CUTS for the GLSL form (each measured alone against step 1l): RESCORE_RANK=exact (1m), RESCORE_MENU=small
# (1n), RESCORE_SELF=sparse (1o), RESCORE_RANK=sparse (1p)
RANK = os.environ.get("RESCORE_RANK", "search")
MENU = os.environ.get("RESCORE_MENU", "full")
SELF = os.environ.get("RESCORE_SELF", "dense")
ISOLATE = os.environ.get("RESCORE_ISOLATE", "0") == "1"                # step 1r
GATE = os.environ.get("RESCORE_GATE", "any")                          # C3: own = the cell's own margin
RANK2 = os.environ.get("RESCORE_RANK2", "0") == "1"                   # C1: the two-stage ranking
from collections import Counter

_CACHE = {}
# THE CACHES' KEYS ARE MEMORY ADDRESSES (2026-10-01, a silent failure found by step 1j): a case's frames are freed when the
# next case loads, and a later case's frames can land at the SAME addresses -- then it read an earlier case's cached
# lattice or basins (weave 5 after four other cases: 83.8% wrong; alone: 29.7%). Every array whose address keys an entry
# is now held here, so no later array can reuse it while the entry lives, and reset_caches() empties all of them (rescore_disc
# calls it at every case). Steps 1e, 1g and 1h-1j were re-run with it; 1c, 1d, 1f and 1k on the FFT lattice use no cache.
_HOLD = []


def reset_caches():
    _CACHE.clear(); _BASINS.clear(); _HOLD.clear()


def lattice_coarse(img, cx, cy):
    """STEP 1e: the lattice as a shader could find it -- once per 32-px cell (cached), shifts on a 2-px grid within
    8-40 px, the SAD of an 8 x 8 subsample (4-px spacing) of the cell's 32 x 32 patch; the two lowest non-collinear
    shifts under 0.3 of the patch's mean absolute deviation, each refined to the pixel (+-1 px)"""
    gx, gy = int(cx) // 32, int(cy) // 32
    key = (img.__array_interface__["data"][0], gx, gy)          # the frame's own memory, not id(): a view's id is reused
    if key in _CACHE: return _CACHE[key]
    x0, y0 = gx * 32, gy * 32
    res = None
    if x0 + 32 + 42 <= W and y0 + 32 + 42 <= H and x0 - 42 >= 0 and y0 - 42 >= 0:
        ys, xs = np.mgrid[y0:y0 + 32:4, x0:x0 + 32:4]
        base = img[ys, xs].astype(np.float64); mad = np.mean(np.abs(base - base.mean()))
        if mad > 1e-3:
            def cost(sx, sy): return float(np.mean(np.abs(base - img[ys + sy, xs + sx])))
            cands = sorted(((cost(sx, sy), sx, sy) for sy in range(-40, 41, 2) for sx in range(-40, 41, 2)
                            if 8 <= np.hypot(sx, sy) <= 40), key=lambda z: z[0])
            good = [(c, sx, sy) for c, sx, sy in cands if c < 0.3 * mad]
            def fine(sx, sy):
                return min(((cost(sx + dx, sy + dy), sx + dx, sy + dy) for dy in (-1, 0, 1) for dx in (-1, 0, 1)), key=lambda z: z[0])[1:]
            if good:
                p1 = np.array(fine(good[0][1], good[0][2]), float)
                for c, sx, sy in good[1:]:
                    v = np.array(fine(sx, sy), float)
                    if abs(p1[0] * v[1] - p1[1] * v[0]) > 1e-6: res = (p1, v); break
    _CACHE[key] = res; _HOLD.append(img)
    return res


def lattice_two(img, cx, cy):
    """STEP 1f: the cell's OWN 32 x 32 neighbourhood, a two-stage search a shader can afford -- coarse shifts on a 4-px
    grid (8-40 px) by the SAD of an 8 x 8 subsample, the six best refined to the pixel (+-2 px) on a 16 x 16 subsample;
    the two lowest non-collinear under 0.3 of the patch's mean absolute deviation"""
    x0, y0 = int(cx) - 16, int(cy) - 16
    if x0 - 42 < 0 or y0 - 42 < 0 or x0 + 32 + 42 > W or y0 + 32 + 42 > H: return None
    ys8, xs8 = np.mgrid[y0:y0 + 32:4, x0:x0 + 32:4]
    ys16, xs16 = np.mgrid[y0:y0 + 32:2, x0:x0 + 32:2]
    b8 = img[ys8, xs8].astype(np.float64); b16 = img[ys16, xs16].astype(np.float64)
    mad = np.mean(np.abs(b16 - b16.mean()))
    if mad < 1e-3: return None
    c8 = lambda sx, sy: float(np.mean(np.abs(b8 - img[ys8 + sy, xs8 + sx])))
    c16 = lambda sx, sy: float(np.mean(np.abs(b16 - img[ys16 + sy, xs16 + sx])))
    coarse = sorted(((c8(sx, sy), sx, sy) for sy in range(-40, 41, 4) for sx in range(-40, 41, 4)
                     if 8 <= np.hypot(sx, sy) <= 40), key=lambda z: z[0])[:6]
    fine = []
    for _, sx, sy in coarse:
        fine.append(min(((c16(sx + dx, sy + dy), sx + dx, sy + dy) for dy in range(-2, 3) for dx in range(-2, 3)
                         if 8 <= np.hypot(sx + dx, sy + dy) <= 40), key=lambda z: z[0]))
    fine.sort(key=lambda z: z[0])
    good = [(c, sx, sy) for c, sx, sy in fine if c < 0.3 * mad]
    if not good: return None
    p1 = np.array(good[0][1:], float)
    for c, sx, sy in good[1:]:
        v = np.array([sx, sy], float)
        if abs(p1[0] * v[1] - p1[1] * v[0]) > 1e-6: return p1, v
    return None


def lattice_tile(img, cx, cy):
    """STEP 1g: once per 128-px TILE (cached): step 1f's two-stage search on a 64 x 64 patch at the tile's centre
    (8 x 8 at 8-px spacing for the coarse stage, 16 x 16 at 4-px spacing for the fine)"""
    tx, ty = int(cx) // 128, int(cy) // 128
    key = ("tile", img.__array_interface__["data"][0], tx, ty)
    if key in _CACHE: return _CACHE[key]
    x0, y0 = tx * 128 + 32, ty * 128 + 32
    res = None
    if x0 - 42 >= 0 and y0 - 42 >= 0 and x0 + 64 + 42 <= W and y0 + 64 + 42 <= H:
        ys8, xs8 = np.mgrid[y0:y0 + 64:8, x0:x0 + 64:8]
        ys16, xs16 = np.mgrid[y0:y0 + 64:4, x0:x0 + 64:4]
        b8 = img[ys8, xs8].astype(np.float64); b16 = img[ys16, xs16].astype(np.float64)
        mad = np.mean(np.abs(b16 - b16.mean()))
        if mad > 1e-3:
            c8 = lambda sx, sy: float(np.mean(np.abs(b8 - img[ys8 + sy, xs8 + sx])))
            c16 = lambda sx, sy: float(np.mean(np.abs(b16 - img[ys16 + sy, xs16 + sx])))
            coarse = sorted(((c8(sx, sy), sx, sy) for sy in range(-40, 41, 4) for sx in range(-40, 41, 4)
                             if 8 <= np.hypot(sx, sy) <= 40), key=lambda z: z[0])[:6]
            fine = sorted((min(((c16(sx + dx, sy + dy), sx + dx, sy + dy) for dy in range(-2, 3) for dx in range(-2, 3)
                                if 8 <= np.hypot(sx + dx, sy + dy) <= 40), key=lambda z: z[0]) for _, sx, sy in coarse),
                          key=lambda z: z[0])
            good = [(c, sx, sy) for c, sx, sy in fine if c < 0.3 * mad]
            if good:
                p1 = np.array(good[0][1:], float)
                for c, sx, sy in good[1:]:
                    v = np.array([sx, sy], float)
                    if abs(p1[0] * v[1] - p1[1] * v[0]) > 1e-6: res = (p1, v); break
    _CACHE[key] = res; _HOLD.append(img)
    return res


_BASINS = {}
LAST = {}                                                             # step 1h's last offsets and vectors (diagnostics)


def basins(Sk, Sk1):
    """STEP 1h: the 1/8 level's two basins per cell, as ALIAS_E computes them (tests/probes/limb/ambiguity.py's
    emulation): the best shift d1, the lowest rival d2 behind a ridge, the margin (rival - best) / S; texels (dy, dx)"""
    key = (Sk.__array_interface__["data"][0], Sk1.__array_interface__["data"][0])
    if key in _BASINS: return _BASINS[key]
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "limb"))
    import ambiguity as AM
    a, b = AM.eighth(Sk.astype(np.float64)), AM.eighth(Sk1.astype(np.float64))
    C = AM.curves(a, b); R = AM.R
    flat = C.reshape(len(AM.SH), *a.shape)
    i1 = flat.argmin(0); c1 = flat.min(0); S = np.maximum(flat.mean(0) - c1, 1e-4)
    margin = np.full(a.shape, np.inf); j2best = np.full(a.shape, -1)
    for j1, d1 in enumerate(AM.SH):
        cell = i1 == j1
        if not cell.any(): continue
        for j2, d2 in enumerate(AM.SH):
            if max(abs(d2[0] - d1[0]), abs(d2[1] - d1[1])) < 2: continue
            c2 = flat[j2][cell]
            ridge = np.max([C[q[0] + R, q[1] + R][cell] for q in AM.segment(d1, d2)], axis=0)
            m = np.where(ridge - np.maximum(c1[cell], c2) >= 0.25 * S[cell], (c2 - c1[cell]) / S[cell], np.inf)
            better = m < margin[cell]
            mc = margin[cell]; jc = j2best[cell]
            mc[better] = m[better]; jc[better] = j2
            margin[cell] = mc; j2best[cell] = jc
    SHa = np.array(AM.SH)
    d1 = SHa[i1]; d2 = np.where((j2best >= 0)[..., None], SHa[np.maximum(j2best, 0)], d1)
    _BASINS[key] = (d1, d2, margin); _HOLD.extend((Sk, Sk1))
    return _BASINS[key]


def lattice_rival(Sk, Sk1, i, j, cx, cy):
    """STEP 1h (route 1): the lattice from the 1/8 rival basins of the cell and its 3 x 3 neighbours (margin under 0.3),
    8 x (rival - best) px, each refined at full resolution by the self-match of frame k's own 32 x 32 neighbourhood
    (16 x 16 at 2-px spacing; +-4 px on a 2-px grid, then +-1 px), kept under 0.3 of the patch's MAD"""
    d1, d2, margin = basins(Sk, Sk1)
    if GATE == "own" and not margin[i, j] < 0.3: LAST.clear(); return None   # COST C3: the cell's OWN margin opens it
    if GATE == "ext5":                                              # COST C4: at least 5 of the 5 x 5 cells low
        win = margin[max(i - 2, 0):i + 3, max(j - 2, 0):j + 3]
        if int((win < 0.3).sum()) < 5: LAST.clear(); return None
    offs = []
    rad = 2 if LATTICE == "rival3" else 1                  # STEP 1j: the offsets from the 5 x 5 neighbourhood (40 px)
    for ii in range(max(i - rad, 0), min(i + rad + 1, margin.shape[0])):
        for jj in range(max(j - rad, 0), min(j + rad + 1, margin.shape[1])):
            if margin[ii, jj] < 0.3:
                o = 8.0 * np.array([d2[ii, jj][1] - d1[ii, jj][1], d2[ii, jj][0] - d1[ii, jj][0]], float)   # (x, y) px
                if o[0] < 0 or (o[0] == 0 and o[1] < 0): o = -o
                if not any(np.hypot(*(o - z)) < 4 for z in offs): offs.append(o)
    LAST.clear(); LAST["raw"] = list(offs); LAST["vec"] = []
    if not offs: return None
    x0, y0 = int(cx) - 16, int(cy) - 16
    if x0 - 50 < 0 or y0 - 50 < 0 or x0 + 32 + 50 > W or y0 + 32 + 50 > H: return None
    sp = 4 if SELF in ("sparse", "coarse") else 2         # COST CUT (1o): the self-match on 8 x 8 at 4 px, not 16 x 16 at 2
    ys16, xs16 = np.mgrid[y0:y0 + 32:sp, x0:x0 + 32:sp]
    b16 = Sk[ys16, xs16].astype(np.float64); mad = np.mean(np.abs(b16 - b16.mean()))
    if mad < 1e-3: return None
    LAST["taps"] = b16.size
    c16 = lambda sx, sy: float(np.mean(np.abs(b16 - Sk[ys16 + sy, xs16 + sx])))
    def isolated(c, sx, sy):
        # STEP 1r (after L1's stripes, labelled): a lattice vector is an ISOLATED minimum of the self-match -- its 8
        # neighbours at +-2 px all cost at least max(2 c, c + 0.15 MAD). Along a stripe the cost does not rise.
        if not ISOLATE: return True
        nb = min(c16(sx + dx, sy + dy) for dy in (-2, 0, 2) for dx in (-2, 0, 2) if (dx, dy) != (0, 0))
        return nb >= max(2 * c, c + 0.15 * mad)
    vecs = []
    ys4, xs4 = np.mgrid[y0:y0 + 32:8, x0:x0 + 32:8]                 # COST C5: 4 x 4 samples for the +-4 px stage
    b4 = Sk[ys4, xs4].astype(np.float64)
    c4 = lambda sx, sy: float(np.mean(np.abs(b4 - Sk[ys4 + sy, xs4 + sx])))
    cs = c4 if SELF == "coarse" else c16
    for o in offs:
        _, sx, sy = min((cs(int(o[0]) + dx, int(o[1]) + dy), int(o[0]) + dx, int(o[1]) + dy)
                        for dy in range(-4, 5, 2) for dx in range(-4, 5, 2) if (int(o[0]) + dx, int(o[1]) + dy) != (0, 0))
        c = c16(sx, sy)
        c, sx, sy = min((c16(sx + dx, sy + dy), sx + dx, sy + dy) for dy in (-1, 0, 1) for dx in (-1, 0, 1)
                        if (sx + dx, sy + dy) != (0, 0))
        if c < 0.3 * mad and isolated(c, sx, sy): vecs.append((c, np.array([sx, sy], float)))
    vecs.sort(key=lambda z: z[0])
    LAST["vec"] = [v for _, v in vecs]; LAST["evals"] = 34 * len(offs)
    if not vecs: return None
    if LATTICE in ("rival2", "rival3"):
        # STEP 1i (after 1h's anatomy, labelled): the rival offsets are true lattice vectors (96%) but LONG -- 1/8 basins
        # 5 texels apart, three lattice steps -- so the pair spans a SUBLATTICE (index 3 on the weave: (42, +-14)) or one
        # direction only. COMPLETE it: probe the short representatives of the cosets a/2, a/3 (each vector) and
        # (a + b)/2, (a - b)/2, (a + b)/3, (a - b)/3, a - b, a + b (each non-collinear pair), each refined +-1 px by the same
        # self-match and kept under 0.3 MAD; up to three rounds; the basis is then the SHORTEST valid vector and the
        # shortest valid one not collinear with it
        V = [v for _, v in vecs]; probed = []
        fold = lambda q: -q if (q[0] < 0 or (q[0] == 0 and q[1] < 0)) else q
        for _ in range(3):
            P = []
            for a in V: P += [a / 2, a / 3]
            for ia in range(len(V)):
                for ib in range(ia + 1, len(V)):
                    a, b = V[ia], V[ib]
                    if abs(a[0] * b[1] - a[1] * b[0]) < 1e-6: continue
                    for c in ((a + b) / 2, (a - b) / 2, (a + b) / 3, (a - b) / 3, a - b, a + b):
                        P.append(min((c + n * a + m * b for n in (-1, 0, 1) for m in (-1, 0, 1)), key=lambda z: np.hypot(*z)))
            new = []
            for q in P:
                q = fold(np.round(q))
                if not 8 <= np.hypot(*q) <= 40: continue
                if any(np.hypot(*(q - z)) < 2 for z in V + probed + new): continue
                probed.append(q)
                c, sx, sy = min((c16(int(q[0]) + dx, int(q[1]) + dy), int(q[0]) + dx, int(q[1]) + dy)
                                for dy in (-1, 0, 1) for dx in (-1, 0, 1))
                LAST["evals"] += 9
                if c < 0.3 * mad and isolated(c, sx, sy): new.append(fold(np.array([sx, sy], float)))
            if not new: break
            V += new
        V.sort(key=lambda z: np.hypot(*z))
        LAST["vec"] = V
        p1 = V[0]
        for v in V[1:]:
            if abs(p1[0] * v[1] - p1[1] * v[0]) > 1e-6: return p1, v
        return p1, np.zeros(2)
    p1 = vecs[0][1]
    for _, v in vecs[1:]:
        if abs(p1[0] * v[1] - p1[1] * v[0]) > 1e-6: return p1, v
    return p1, np.zeros(2)                                            # one direction only: its multiples


def rescore_cell(Sk, Sk1, u, mv, i, j, cx, cy):
    """step 1c for one moving cell: None (no lattice), else (the chosen vector, w's refined cost, the pick made)"""
    w = u[i, j].astype(np.float64)
    if LATTICE == "none": return None                              # G1: the tap's own field, measured as it stands
    L = (lattice_coarse(Sk, cx, cy) if LATTICE == "coarse" else lattice_two(Sk, cx, cy) if LATTICE == "two"
         else lattice_tile(Sk, cx, cy) if LATTICE == "tile"
         else lattice_rival(Sk, Sk1, i, j, cx, cy) if LATTICE in ("rival", "rival2", "rival3")
         else lattice(Sk, cx, cy))
    if L is None: return None
    p1, p2 = L
    nr = 1 if MENU == "small" else 3                       # COST CUT (1n): the nearest lattice steps only, distinct seeds
    pts = [n * p1 + m * p2 for n in range(-nr, nr + 1) for m in range(-nr, nr + 1)]
    pts = [q for q in pts if np.hypot(*q) <= 45]
    seeds = [u[ii, jj].astype(np.float64) for ii in range(max(i - 1, 0), min(i + 2, u.shape[0]))
             for jj in range(max(j - 1, 0), min(j + 2, u.shape[1])) if mv[ii, jj]]
    if MENU == "small":
        ds = []
        for s_ in seeds:
            if not any(np.hypot(*(s_ - z)) < 1.0 for z in ds): ds.append(s_)
        seeds = ds
    alts = []
    for s_ in seeds:
        for q in pts:
            c_ = s_ + q
            if np.hypot(*(c_ - w)) > 1.5 and not any(np.hypot(*(c_ - z)) < 1.0 for z in alts): alts.append(c_)
    def rough(q):
        if RANK == "exact": return sad(Sk, Sk1, cx, cy, q)  # COST CUT (1m): ranked at the candidate's own position
        f = sad_sparse if RANK == "sparse" else sad           # COST CUT (1p): ranked on 8 x 8 samples
        return min(f(Sk, Sk1, cx, cy, q + np.array([dx, dy])) for dy in (-0.5, 0, 0.5) for dx in (-0.5, 0, 0.5))
    LAST["menu"] = len(alts)                                         # the menu's size (the GLSL form's cost)
    if RANK2:
        # COST C1: a cheap first stage (4 x 4 samples at 4 px within the block, +-0.5 px) over the whole menu, then the
        # best four only by the full rough rank
        def rough4(q):
            return min(sad4(Sk, Sk1, cx, cy, q + np.array([dx, dy])) for dy in (-0.5, 0, 0.5) for dx in (-0.5, 0, 0.5))
        alts = sorted(alts, key=rough4)[:4]
    ints = sorted(alts, key=rough)[:2] if STEP1C else sorted(alts, key=lambda q: sad(Sk, Sk1, cx, cy, np.round(q)))[:2]
    if STEP == "1k2":
        # STEP 1k2 (after 1l's pendulum, labelled): the two candidates OFFERED are different basins -- the second is the
        # best-ranked one more than 2 px from the first -- so the uniqueness test always meets a real rival when one is
        # in the menu (1k alone let two refinements of one alias through on the rotating lattice)
        rk = sorted(alts, key=rough); ints = rk[:1]
        for q in rk[1:]:
            if np.hypot(*(q - rk[0])) > 2: ints.append(q); break
    wb, wc = refine(Sk, Sk1, cx, cy, w)
    scored = [(wc, wb)]
    for q in ints:
        qb, qc = refine(Sk, Sk1, cx, cy, q if STEP1C else np.round(q))
        scored.append((qc, qb))
    scored.sort(key=lambda z: z[0])
    bc, best = scored[0]
    ok = bc <= wc - 0.004
    if STEP == "1d" and len(scored) > 1:
        # STEP 1d, THE UNIQUENESS TEST (after the rotating EXACT print, labelled): the pick must also beat the runner-up
        # by the margin. On an exact print the aliases tie, and the cell keeps w (the lossless fallback)
        ok = ok and bc <= scored[1][0] - 0.004
    if STEP in ("1k", "1k2"):
        # STEP 1k (after 1i's anatomy, labelled): the runner-up is the best of a DIFFERENT basin, more than 2 px from the
        # pick. Two candidates that refine into the same basin (12.8 and 13.2 px) are one answer, not a tie
        rivals = [c for c, b in scored[1:] if np.hypot(*(b - best)) > 2]
        ok = ok and (not rivals or bc <= rivals[0] - 0.004)
    return (best if ok else w), wc, ok

def main():
    print(f"{'case':10s} | {'core gross: before -> after':>28s} | {'box gross: before -> after':>28s} | changed | lattice found")
    for case in CASES:
        kind, v = case.split(":"); v = float(v)
        src = pathlib.Path(f"{SRC}/src-{kind}-{v:g}.raw")
        S = np.fromfile(src, "<u2").reshape(N, H, W).astype(np.float32) / 65535.0
        F = field(src)
        cy_, cx_ = np.mgrid[4:H:8, 4:W:8].astype(np.float64) + 0.5
        tal = {"core": [0, 0, 0], "box": [0, 0, 0]}; changed = 0; cells = 0; latt = [0, 0]
        tax = Counter()
        for k in range(10, 31, 2):
            u = F[k]; out = u.copy()
            x0 = X0 + v * k
            inbox = (cx_ > x0) & (cx_ < x0 + BW) & (cy_ > Y0) & (cy_ < Y0 + BH)
            mv = inbox & (np.hypot(u[..., 0], u[..., 1]) > 0.5)
            for i, j in zip(*np.nonzero(mv)):
                cx, cy = cx_[i, j], cy_[i, j]; w = u[i, j].astype(np.float64)
                L = lattice(S[k], cx, cy); latt[1] += 1
                if L is None: continue
                latt[0] += 1
                p1, p2 = L
                # STEP 1b (after the anatomy of two cells, labelled): (i) EVERY lattice point within 45 px, since a valid basis
                # can need 2 p1 + p2 for (28, 0); (ii) a MENU: the 3 x 3 neighbours' own flows and their lattice points too
                # (the BBC's menu), since some locked cells read about zero, which is no lattice step from the truth
                pts = [n * p1 + m * p2 for n in range(-3, 4) for m in range(-3, 4)]
                pts = [q for q in pts if np.hypot(*q) <= 45]
                seeds = [u[ii, jj].astype(np.float64) for ii in range(max(i - 1, 0), min(i + 2, u.shape[0]))
                         for jj in range(max(j - 1, 0), min(j + 2, u.shape[1])) if mv[ii, jj]]
                alts = []
                for s_ in seeds:
                    for q in pts:
                        c_ = s_ + q
                        if np.hypot(*(c_ - w)) > 1.5 and not any(np.hypot(*(c_ - z)) < 1.0 for z in alts): alts.append(c_)
                # STEP 1c (after the taxonomy: 95% of what stayed wrong had the truth IN the menu, cut by an integer ranking):
                # rank every candidate by a small sub-pixel refine (+-0.5 px) first, the lesson of stage 1a again
                def rough(q):
                    return min(sad(S[k], S[k + 1], cx, cy, q + np.array([dx, dy])) for dy in (-0.5, 0, 0.5) for dx in (-0.5, 0, 0.5))
                ints = sorted(alts, key=rough)[:2] if STEP1C else sorted(alts, key=lambda q: sad(S[k], S[k + 1], cx, cy, np.round(q)))[:2]
                wb, wc = refine(S[k], S[k + 1], cx, cy, w)
                best, bc = wb, wc
                for q in ints:
                    qb, qc = refine(S[k], S[k + 1], cx, cy, q if STEP1C else np.round(q))
                    if qc < bc: best, bc = qb, qc
                if bc <= wc - 0.004:
                    out[i, j] = best
                if TAX and inbox[i, j]:                                   # what stays wrong, and why (the core only)
                    dcore = min(cx - x0, x0 + BW - cx, cy - Y0, Y0 + BH - cy)
                    if dcore > 32 and np.hypot(out[i, j][0] - v, out[i, j][1]) > 2:
                        tv = np.array([v, 0.0])
                        offered = np.hypot(*(w - tv)) <= 1.5 or any(np.hypot(*(np.round(q) - tv)) <= 1.5 for q in ints)
                        inmenu = any(np.hypot(*(q - tv)) <= 1.5 for q in alts)
                        tc = sad(S[k], S[k + 1], cx, cy, tv)
                        if not inmenu and np.hypot(*(w - tv)) > 1.5: tax["the truth not in the menu"] += 1
                        elif not offered: tax["in the menu, cut by the integer pre-selection (2 kept)"] += 1
                        elif tc <= wc - 0.004: tax["offered and better than w, yet not picked"] += 1
                        else: tax["offered, but short of the 0.004 margin over w"] += 1
                        tax["n"] += 1
            dd = np.minimum.reduce([cx_ - x0, x0 + BW - cx_, cy_ - Y0, Y0 + BH - cy_])
            for g, sel in (("core", inbox & (dd > 32)), ("box", inbox)):
                e0 = np.hypot(u[sel][:, 0] - v, u[sel][:, 1]); e1 = np.hypot(out[sel][:, 0] - v, out[sel][:, 1])
                tal[g][0] += sel.sum(); tal[g][1] += int((e0 > 2).sum()); tal[g][2] += int((e1 > 2).sum())
            changed += int(np.any(out[inbox] != u[inbox], axis=-1).sum()); cells += int(inbox.sum())
        c = lambda g: f"{100 * tal[g][1] / max(tal[g][0], 1):5.1f}% -> {100 * tal[g][2] / max(tal[g][0], 1):5.1f}%"
        print(f"{case:10s} | {c('core'):>28s} | {c('box'):>28s} | {100 * changed / max(cells, 1):5.1f}% | "
              f"{100 * latt[0] / max(latt[1], 1):5.1f}% of moving cells", flush=True)
        if TAX:
            for key in [x for x in tax if x != "n"]: print(f"      {key:55s} {100 * tax[key] / max(tax['n'], 1):5.1f}% of what stays wrong")


if __name__ == "__main__":
    main()
