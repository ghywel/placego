#!/usr/bin/env python3
"""THE AMBIGUITY FLAG, OFFLINE: does a cost-curve test mark V3's interior as a tie and its ends as anchors, and how often
does it fire on anything else? The first step PRIOR-ART.md's periodic-interior survey ranks (stereo's confidence
measures, PIV's peak ratio). No shader involved: the 1/8 level is emulated in numpy the way the shader builds it (luma at
each 1/8 texel's centre, a pixel corner, so the 2 x 2 average there; SAD over 5 x 5 texels) and every integer shift
within +-3 texels (+-24 px) is scored.

A RIVAL is a second BASIN, not merely a second low cost: a shift d2 at least 2 texels from the best d1 whose straight
path back to d1 crosses a RIDGE (a cost above both ends by a quarter of the curve's typical rise S = mean - c1). That
is what a periodic print gives; a stripe's aperture valley (equal costs ALONG the stripe) and a flat window do not --
the first form, "any low cost 2 texels away", flagged 60-70% of plain translations. The cell's margin is
(c_rival - c1) / S, infinite without a rival; AMBIGUOUS below a threshold.

    ambiguity.py                      V3 at the held (108) and flipped (112) starts, band by band, and the ladder
    ambiguity.py --cases L1_trans_8px V2_stairs_sq24_v6 ...     the share flagged on any cases (default: all 42)
    ambiguity.py --clips street:streetpeople-1080p.mp4:8 bttf:backtothefuture60sec24fps.mp4:30 ...
                                      real footage (np-scratch files; label:file:second, 1280x720 gray)

Per case: the share of textured cells (5 x 5 range >= 0.02) flagged at margins below 0.05 / 0.15 / 0.30, every
other frame of 2-19. For V3: per bar-band of the patch (top -> bottom), the flagged share and the unflagged cells'
vertical answer (+ right, - the alias)."""
import pathlib
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import limblevels as LL  # noqa: E402

W, H, R = 1280, 720, 3
TAUS = (0.05, 0.15, 0.30)


def frames(scene):
    r = subprocess.run([LL.FF, "-hide_banner", "-loglevel", "error", "-f", "lavfi", "-i", scene, "-pix_fmt", "gray",
                        "-f", "rawvideo", "-"], capture_output=True)
    a = np.frombuffer(r.stdout, np.uint8)
    n = a.size // (W * H)
    assert n >= 20, (n, r.stderr[:200])
    return a[: n * W * H].reshape(n, H, W).astype(np.float32) / 255.0


def eighth(f):
    # the shader samples each 1/8 texel's centre, a pixel corner: bilinear there is the 2 x 2 average
    return 0.25 * (f[3::8, 3::8] + f[3::8, 4::8] + f[4::8, 3::8] + f[4::8, 4::8])


def box5(x):
    p = np.pad(x, 2, mode="edge")
    c = np.cumsum(np.cumsum(p, 0), 1)
    c = np.pad(c, ((1, 0), (1, 0)))
    return c[5:, 5:] - c[:-5, 5:] - c[5:, :-5] + c[:-5, :-5]


def curves(a, b):
    """cost[dy, dx] per cell for every shift in +-R (B shifted; edge-clamped like a texture read)"""
    hh, ww = a.shape
    pb = np.pad(b, R, mode="edge")
    C = np.empty((2 * R + 1, 2 * R + 1, hh, ww), np.float32)
    for dy in range(-R, R + 1):
        for dx in range(-R, R + 1):
            C[dy + R, dx + R] = box5(np.abs(a - pb[R + dy:R + dy + hh, R + dx:R + dx + ww]))
    return C


def rng5(a):
    from numpy.lib.stride_tricks import sliding_window_view as sw
    p = np.pad(a, 2, mode="edge")
    v = sw(p, (5, 5))
    return v.max((-1, -2)) - v.min((-1, -2))


SH = [(dy, dx) for dy in range(-R, R + 1) for dx in range(-R, R + 1)]


def segment(a, b):
    """the integer shifts strictly between a and b on the straight path (a rounded line)"""
    n = max(abs(b[0] - a[0]), abs(b[1] - a[1]))
    return [(int(round(a[0] + (b[0] - a[0]) * t / n)), int(round(a[1] + (b[1] - a[1]) * t / n))) for t in range(1, n)]


def analyse(fr, k):
    a, b = eighth(fr[k]), eighth(fr[k + 1])
    C = curves(a, b)
    flat = C.reshape(len(SH), *a.shape)
    i1 = flat.argmin(0)
    c1 = flat.min(0)
    S = np.maximum(flat.mean(0) - c1, 1e-4)
    margin = np.full(a.shape, np.inf, np.float32)
    for j1, d1 in enumerate(SH):
        cell = i1 == j1
        if not cell.any():
            continue
        cc1, ss = c1[cell], S[cell]
        for j2, d2 in enumerate(SH):
            if max(abs(d2[0] - d1[0]), abs(d2[1] - d1[1])) < 2:
                continue
            c2 = flat[j2][cell]
            ridge = np.max([C[p[0] + R, p[1] + R][cell] for p in segment(d1, d2)], axis=0)
            rival = ridge - np.maximum(cc1, c2) >= 0.25 * ss
            m = np.where(rival, (c2 - cc1) / ss, np.inf)
            margin[cell] = np.minimum(margin[cell], m)
    d1y = np.array([d[0] for d in SH])[i1]
    d1x = np.array([d[1] for d in SH])[i1]
    return margin, rng5(a), d1y, d1x


def scene(case, off=None):
    s = LL.scene(case)
    if off is not None:
        assert s.count("100+288*T") == 3
        s = s.replace("100+288*T", f"{off}+288*T")
    return s


def clip_frames(path, sec):
    r = subprocess.run([LL.FF, "-hide_banner", "-loglevel", "error", "-ss", str(sec), "-i", str(path), "-frames:v", "21",
                        "-vf", f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"], capture_output=True)
    a = np.frombuffer(r.stdout, np.uint8)
    n = a.size // (W * H)
    assert n >= 20, (path, n, r.stderr[:200])
    return a[: n * W * H].reshape(n, H, W).astype(np.float32) / 255.0


def main():
    if "--clips" in sys.argv:
        print("\n== real footage: the share of textured 1/8 cells flagged (every other frame of 2-19, A->B)")
        print(f"{'clip':28}" + "".join(f"  <{t:.2f}" for t in TAUS) + "   textured cells")
        for spec in sys.argv[sys.argv.index("--clips") + 1:]:
            lab, f, sec = spec.split(":")
            fr = clip_frames(LL.NP / f, float(sec))
            n = np.zeros(len(TAUS)); tot = 0
            for k in range(2, 19, 2):
                m, rg, _, _ = analyse(fr, k)
                tex = rg >= 0.02
                tex[:3], tex[-3:], tex[:, :3], tex[:, -3:] = False, False, False, False
                tot += tex.sum()
                for j, t in enumerate(TAUS):
                    n[j] += (m[tex] < t).sum()
            print(f"{lab + ' ' + sec + ' s':28}" + "".join(f"{100 * n[j] / max(tot, 1):7.1f}%" for j in range(len(TAUS))) + f"   {tot:9d}")
        sys.exit(0)
    if "--cases" in sys.argv:
        cases = sys.argv[sys.argv.index("--cases") + 1:]
    else:
        cases = None
        for off in (108, 112):
            fr = frames(scene("V3_stairs_sq24_v12", off))
            flag = np.zeros((13, len(TAUS))); tot = np.zeros(13); right = np.zeros(13); wrong = np.zeros(13)
            for k in range(2, 20, 2):
                m, rg, d1y, d1x = analyse(fr, k)
                ya = off + 12 * k
                for band in range(13):
                    y0, y1 = (ya + 24 * band) // 8, (ya + 24 * band + 24) // 8
                    sl = (slice(y0, y1), slice((490 + 40) // 8, (490 + 260) // 8))
                    mm = m[sl].ravel()
                    tot[band] += mm.size
                    for j, t in enumerate(TAUS):
                        flag[band, j] += (mm < t).sum()
                    ok = mm >= TAUS[1]
                    right[band] += (d1y[sl].ravel()[ok] > 0).sum()
                    wrong[band] += (d1y[sl].ravel()[ok] < 0).sum()
            print(f"\n== V3 start {off}: per bar-band, top -> bottom (1/8 cells, every other frame of 2-19, A->B)")
            print("band   flagged <0.05 <0.15 <0.30    unflagged cells (margin >= 0.15): right / alias")
            for band in range(13):
                print(f"{band:4}   " + "".join(f"{100 * flag[band, j] / tot[band]:6.0f}%" for j in range(len(TAUS)))
                      + f"      {int(right[band]):5d} / {int(wrong[band]):5d}")
        cases = subprocess.run(["bash", "-c", f". '{LL.TESTS}/scenes.sh'; echo $ALL_CASES"], capture_output=True,
                                        text=True).stdout.split()
    print("\n== the share of textured 1/8 cells flagged, per case (every other frame of 2-19, A->B)")
    print(f"{'case':28}" + "".join(f"  <{t:.2f}" for t in TAUS) + "   textured cells")
    for case in cases:
        fr = frames(scene(case))
        n = np.zeros(len(TAUS)); tot = 0
        for k in range(2, min(20, fr.shape[0] - 1), 2):
            m, rg, _, _ = analyse(fr, k)
            tex = rg >= 0.02
            tex[:3], tex[-3:], tex[:, :3], tex[:, -3:] = False, False, False, False
            tot += tex.sum()
            for j, t in enumerate(TAUS):
                n[j] += (m[tex] < t).sum()
        print(f"{case:28}" + "".join(f"{100 * n[j] / max(tot, 1):7.1f}%" for j in range(len(TAUS))) + f"   {tot:9d}")


if __name__ == "__main__":
    main()
