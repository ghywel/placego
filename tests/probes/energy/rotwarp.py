"""ENERGY-TRANSFER.md 2.5: does moving a rigid rotation AS ONE pay, against the family's own interpolation?

    rotwarp.py <workdir> <scene> [texture=noise] [src_frames=96]

On a spinning or rolling disc (masters.py, 1280x720, textured ground, 24 -> 60), the disc region is GIVEN (as 3.2's
box was given by segmentation): the question is only whether a region already known to be rigid is better drawn by
one rotation than by the family's per-block field. Four ways, each output frame at t = k + a in (k, k+1):
  rec   -- the Cadence default (bidirectional ... global-cage-energy-carry) through libplacebo, as shipped;
  true  -- the disc drawn from source frames k and k+1, each moved by the TRUE rigid motion to t, blended (1-a, a):
           the upper bound of a rigid mode, resampling included;
  fit   -- the same warp, the rotation per interval fitted from the field: the four-frame shader's raw velocity
           (read_view 4) at N:N, a trimmed least-squares rigid fit u = v + w (-py, px) + s (px, py) over the disc
           eroded 12 px; the interval [k, k+1] takes the fit at field index k + 1 (the field tier's recorded
           off-by-one: field k matches the chord k - 1 -> k), dtheta = atan2(w, 1 + s);
  reg   -- fit's rotation refined by registration: dtheta minimising the squared difference between frame k + 1 and
           frame k rotated back, over the eroded disc; a coarse grid from 0 to 3x the fit (the field under-reads
           fast rims), then golden-section refinement.
fit and reg take the centre from the given region (its centroid in each source frame, linear in between).
EQUAL FOOTING (the second design, 2026-09-30 evening): every variant starts from the SAME 8-bit frames the shader
receives (swscale's yuv420p Y of the source, read back), and none pays an output dither: rec is read out of
libplacebo at 16 bits (format=gray16le, checked: no shift, identical levels). The first design built the warps from
the 16-bit source and pushed them through an 8-bit round trip, a double quantisation rec does not pay (rec blends
two 8-bit frames in float): it put rec ABOVE its own exact-frame level on spin-pendulum. Outside the disc every
variant IS rec's frame. Scored as PSNR-Y against the closed form at t, inside the disc (the true disc at t, 2 px
beyond the rim) and on the full frame. The CONTROL: rec on exact source frames must equal its 8-bit input. Numbers
only.
"""
import math
import os
import pathlib
import re
import subprocess
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
TESTS = HERE.parents[2]
SHADERS = TESTS.parent / "shaders"
sys.path.insert(0, str(TESTS))
import masters                                                                   # noqa: E402

work = pathlib.Path(sys.argv[1]); work.mkdir(parents=True, exist_ok=True)
SCENE = sys.argv[2]
TEX = sys.argv[3] if len(sys.argv) > 3 else "noise"
N = int(sys.argv[4]) if len(sys.argv) > 4 else 96
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
W, H = 1280, 720
table = {name: (kind, p) for name, kind, p, *_ in masters.masters(W, H)}
kind, P = table[SCENE]
assert kind in ("spin", "roll"), "a spinning or rolling disc"
sc = masters.Scene(kind, P, W, H, "textured", TEX, 0.0)
REC = "bidirectional-interpolation-variational-propagated-global-cage-energy-carry"


def geom(t):
    """the disc's centre, angle and radius at t, from the scene's own laws (masters.Scene.value)"""
    if kind == "spin":
        r, law = P[0], P[1]
        orbR, orbOm = (P[2], P[3]) if len(P) > 2 else (0.0, 0.0)
        c = (W / 2, H / 2) if orbR == 0 else (W / 2 + orbR * math.cos(orbOm * t), H / 2 + orbR * math.sin(orbOm * t))
        th = law[1] * t if law[0] == "constant" else law[1] * t * t / 2 if law[0] == "accelerating" \
            else law[1] * math.sin(2 * math.pi * t / law[2])
        return np.array(c), th, r
    rr, vv, _ = P
    p = 2 * (W - 2 * rr) / vv; tp = math.fmod(t, p)
    sl = vv * tp if tp < p / 2 else vv * (p - tp)
    return np.array((rr + sl, H - rr - 8)), sl / rr, rr


src = work / f"src24-{TEX}.raw"
if not src.exists():
    with open(src, "wb") as f:
        for k in range(N):
            f.write(np.floor(sc.value(float(k)) * 65535 + 0.5).clip(0, 65535).astype("<u2").tobytes())
srcf = np.memmap(src, dtype="<u2", mode="r", shape=(N, H, W))
y8 = subprocess.run([FF, "-v", "error", "-f", "rawvideo", "-pix_fmt", "gray16le", "-s", f"{W}x{H}", "-r", "24", "-i", str(src),
                     "-vf", "format=yuv420p,extractplanes=y", "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True, check=True).stdout
Y8 = np.frombuffer(y8, np.uint8).reshape(-1, H, W)
assert len(Y8) == N, f"8-bit read-back gave {len(Y8)} frames, not {N}"
S = lambda k: np.clip((Y8[k].astype(np.float32) - 16) / 219, 0, 1)      # what the shader samples
(work / "_rec.glsl").write_text((SHADERS / f"{REC}.glsl").read_text())
t_ = (SHADERS / "quaddirectional-interpolation-propagated.glsl").read_text()
s_, n_ = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t_); assert n_ == 1
(work / "_vel.glsl").write_text(s_)


def run(chain, rate, inp, keep=None, channels=1):
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo",
           "-pix_fmt", "gray16le", "-s", f"{W}x{H}", "-r", str(rate), "-i", str(inp), "-vf", chain + ",format=rgb48le",
           "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, cwd=work, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    fb = W * H * 6; out = {}; i = 0
    while True:
        buf = p.stdout.read(fb)
        if len(buf) < fb: break
        if keep is None or i in keep:
            im = np.frombuffer(buf, np.uint16).reshape(H, W, 3).astype(np.float32) / 65535.0
            out[i] = im[..., :channels] if channels > 1 else im[..., 0]
        i += 1
    err = p.stderr.read().decode(); p.wait()
    if p.returncode != 0 or "compile status" in err: sys.exit(f"ffmpeg failed: {err[:300]}")
    return out, i


def psnr(a, b, m=None):
    d = (a.astype(np.float64) - b) ** 2
    mse = float(d[m].mean()) if m is not None else float(d.mean())
    return 99.0 if mse == 0 else 10 * math.log10(1.0 / mse)


YY, XX = np.mgrid[0:H, 0:W].astype(np.float64) + 0.5          # pixel centres, masters' convention


def R(phi, px, py):
    c, s = math.cos(phi), math.sin(phi); return px * c - py * s, px * s + py * c


def sample(img, X, Y):                                         # bilinear at continuous (X, Y), pixel centres at +0.5
    x = X - 0.5; y = Y - 0.5
    x0 = np.floor(x).astype(np.int64); y0 = np.floor(y).astype(np.int64); fx = x - x0; fy = y - y0
    x0c, x1c = np.clip(x0, 0, W - 1), np.clip(x0 + 1, 0, W - 1); y0c, y1c = np.clip(y0, 0, H - 1), np.clip(y0 + 1, 0, H - 1)
    return ((1 - fx) * (1 - fy) * img[y0c, x0c] + fx * (1 - fy) * img[y0c, x1c]
            + (1 - fx) * fy * img[y1c, x0c] + fx * fy * img[y1c, x1c])


def sample3(img, X, Y):                                        # cubic spline (prefiltered, interpolating): a better resampler
    from scipy.ndimage import map_coordinates
    return map_coordinates(img, [Y - 0.5, X - 0.5], order=3, mode="nearest")


def disc(c, r, grow=0.0):
    return np.hypot(XX - c[0], YY - c[1]) < r + grow


# the given region: the true disc in each SOURCE frame (its centroid is what fit and reg use for the centre)
cent = np.array([geom(float(k))[0] for k in range(N)])
rad = geom(0.0)[2]

# the field at N:N and the rigid fit per source frame
fld, nf = run("format=yuv420p,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_vel.glsl", 24, src, channels=2)
cy_, cx_ = np.mgrid[4:H:8, 4:W:8].astype(np.float64) + 0.5
wfit = np.full(N, np.nan)
for k in range(min(N, nf)):
    u = (fld[k][4::8, 4::8, :2].astype(np.float64) - 0.5) * 64.0
    c = cent[k]; px, py = cx_ - c[0], cy_ - c[1]
    m = np.hypot(px, py) < rad - 12
    A = np.stack([np.ones(m.sum()), np.zeros(m.sum()), -py[m], px[m]], 1)
    A2 = np.stack([np.zeros(m.sum()), np.ones(m.sum()), px[m], py[m]], 1)
    M = np.concatenate([A, A2]); y = np.concatenate([u[..., 0][m], u[..., 1][m]])
    keep = np.ones(len(y), bool)
    for _ in range(3):                                        # trimmed: drop residuals over 3 MADs, refit
        sol, *_ = np.linalg.lstsq(M[keep], y[keep], rcond=None)
        res = np.abs(M @ sol - y); mad = np.median(res[keep]) + 1e-6
        keep = res < 3 * 1.4826 * mad
    w, s = sol[2], sol[3]
    wfit[k] = math.atan2(w, 1 + s)
true_d = np.array([geom(k + 1.0)[1] - geom(float(k))[1] for k in range(N - 1)])
dfit = np.array([wfit[k + 1] if k + 1 < N else np.nan for k in range(N - 1)])
ok = ~np.isnan(dfit)
print(f"# {SCENE}, texture {TEX}, {N} source frames; the disc r {rad} px")
print(f"  field's rotation per interval (the k+1 convention): median ratio to truth {np.median(dfit[ok][4:-4] / true_d[ok][4:-4]):.3f}"
      f"; the other convention (field k) {np.median(wfit[:-1][4:-4] / true_d[4:-4]):.3f}")

# registration per interval, seeded by the fit
sub = (slice(None, None, 4), slice(None, None, 4))


def ssd(k, phi):
    c0, c1 = cent[k], cent[k + 1]
    m = disc(c1, rad - 12)[sub]
    X, Y = XX[sub][m], YY[sub][m]
    qx, qy = R(-phi, X - c1[0], Y - c1[1])
    return float(np.mean((S(k + 1)[sub][m] - sample(S(k), c0[0] + qx, c0[1] + qy)) ** 2))


dreg = np.full(N - 1, np.nan)
for k in range(N - 1):
    f = dfit[k] if not np.isnan(dfit[k]) else 0.0
    sgn = 1.0 if f >= 0 else -1.0
    hi = 3 * abs(f) + 0.02
    grid = np.arange(0, hi, 0.002) * sgn
    e = [ssd(k, g) for g in grid]; j = int(np.argmin(e))
    a, b = grid[max(j - 1, 0)], grid[min(j + 1, len(grid) - 1)]
    g = (math.sqrt(5) - 1) / 2
    for _ in range(18):                                        # golden-section on [a, b]
        c1_, c2_ = b - g * (b - a), a + g * (b - a)
        if ssd(k, c1_) < ssd(k, c2_): b = c2_
        else: a = c1_
    dreg[k] = (a + b) / 2
print(f"  registration's rotation: median ratio to truth {np.median(dreg[4:-4] / true_d[4:-4]):.3f}; "
      f"median |error| {np.median(np.abs(dreg - true_d)[4:-4]) * rad:.3f} px at the rim (fit: {np.nanmedian(np.abs(dfit - true_d)[4:-4]) * rad:.3f})")

# THE FOUND REGION (2.5b, 2026-09-30 late evening): the rigid body found from the FIELD ALONE, nothing given. Per
# field index k: RANSAC for a similarity model u = v + w (-py, px) + s (px, py) over the moving cells (|u| > 0.5
# px/frame; two cells 40+ px apart fix the four parameters exactly), inliers within 1 px/frame, two refits, then the
# largest 8-connected inlier set, closed and hole-filled (a spin's still centre is a hole)
try:
    from scipy import ndimage as ndi
except ImportError:
    ndi = None
REF = np.array([W / 2, H / 2])


def mfit(px, py, ux, uy):
    n = len(px); A = np.zeros((2 * n, 4)); A[:n, 0] = 1; A[n:, 1] = 1
    A[:n, 2] = -py; A[n:, 2] = px; A[:n, 3] = px; A[n:, 3] = py
    return np.linalg.lstsq(A, np.concatenate([ux, uy]), rcond=None)[0]


def mres(sol, px, py, ux, uy):
    vx, vy, w, s = sol; return np.hypot(vx - w * py + s * px - ux, vy + w * px + s * py - uy)


found = {}
if ndi is not None:
    rng_ = np.random.default_rng(7)
    edge = np.zeros(cx_.shape, bool); edge[2:-2, 2:-2] = True             # the frame's border cells are out
    for k in range(min(N, nf)):
        u = (fld[k][4::8, 4::8, :2].astype(np.float64) - 0.5) * 64.0
        mv = (np.hypot(u[..., 0], u[..., 1]) > 0.5) & edge
        if mv.sum() < 20: continue
        px, py = cx_[mv] - REF[0], cy_[mv] - REF[1]; ux, uy = u[..., 0][mv], u[..., 1][mv]
        best = None
        for _ in range(300):
            i, j = rng_.choice(len(px), 2, replace=False)
            if math.hypot(px[i] - px[j], py[i] - py[j]) < 40: continue
            sol = mfit(px[[i, j]], py[[i, j]], ux[[i, j]], uy[[i, j]])
            inl = mres(sol, px, py, ux, uy) < 1.0
            if best is None or inl.sum() > best[1].sum(): best = (sol, inl)
        if best is None: continue
        sol, inl = best
        for _ in range(2):
            if inl.sum() < 4: break
            sol = mfit(px[inl], py[inl], ux[inl], uy[inl]); inl = mres(sol, px, py, ux, uy) < 1.0
        m = np.zeros(mv.shape, bool); m[mv] = inl
        lab, nl = ndi.label(m, structure=np.ones((3, 3)))
        if nl == 0: continue
        big = lab == (1 + int(np.argmax(ndi.sum(m, lab, range(1, nl + 1)))))
        big = ndi.binary_fill_holes(ndi.binary_closing(big, np.ones((3, 3))))
        found[k] = (big, sol)
    # the region against the true disc, cell by cell, anchored at k and at k - 1 (the field's timing convention)
    iou = {0: [], 1: []}
    for k, (big, _) in found.items():
        for lag in (0, 1):
            if k - lag < 0: continue
            c = geom(float(k - lag))[0]; tru = np.hypot(cx_ - c[0], cy_ - c[1]) < rad
            iou[lag].append((big & tru).sum() / max((big | tru).sum(), 1))
    print(f"  FOUND region: {len(found)} of {min(N, nf)} field frames hold one; IoU with the true disc, median "
          f"{np.median(iou[0]) if iou[0] else float('nan'):.3f} (anchored at k), {np.median(iou[1]) if iou[1] else float('nan'):.3f} (at k - 1)")

# the outputs
nout = int((N - 1) * 60 / 24); tt = lambda n: n * 24 / 60
interp = [n for n in range(10, nout - 10) if n % 5 != 0]
onsrc = [n for n in range(10, nout - 10) if n % 5 == 0]
want = set(interp) | set(onsrc)
def run16(chain, keep):
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo", "-pix_fmt", "gray16le",
           "-s", f"{W}x{H}", "-r", "24", "-i", str(src), "-vf", chain, "-f", "rawvideo", "-pix_fmt", "gray16le", "-"]
    p = subprocess.Popen(cmd, cwd=work, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = {}; i = 0
    while True:
        buf = p.stdout.read(W * H * 2)
        if len(buf) < W * H * 2: break
        if i in keep: out[i] = np.frombuffer(buf, "<u2").reshape(H, W).astype(np.float32) / 65535.0
        i += 1
    err = p.stderr.read().decode(); p.wait()
    if p.returncode != 0 or "compile status" in err: sys.exit(f"ffmpeg failed: {err[:300]}")
    return out
rec = run16("format=yuv420p,libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_rec.glsl:format=gray16le", want)
truth = {n: sc.value(tt(n)) for n in sorted(want)}


def warp(n, how):
    t = tt(n); k = int(math.floor(t)); a = t - k
    samp = sample3 if how.endswith("3") else sample
    how = how.rstrip("3")
    if how == "true":
        ct, tht, _ = geom(t); ck, thk, _ = geom(float(k)); ck1, thk1, _ = geom(k + 1.0)
        pk, pk1 = thk - tht, thk1 - tht
    else:
        d = dfit[k] if how == "fit" else dreg[k]
        ck, ck1 = cent[k], cent[k + 1]; ct = (1 - a) * ck + a * ck1
        pk, pk1 = -a * d, (1 - a) * d
    m = disc(ct, rad, 1.0)
    X, Y = XX[m] - ct[0], YY[m] - ct[1]
    qx, qy = R(pk, X, Y); v0 = samp(S(k), ck[0] + qx, ck[1] + qy)
    qx, qy = R(pk1, X, Y); v1 = samp(S(k + 1), ck1[0] + qx, ck1[1] + qy)
    cov = np.clip(rad - np.hypot(XX - ct[0], YY - ct[1]) + 0.5, 0, 1)
    img = rec[n].copy(); img[m] = cov[m] * ((1 - a) * v0 + a * v1) + (1 - cov[m]) * rec[n][m]
    return img, cov


try:                                                           # 3 = the cubic-spline resampler (scipy), the others bilinear as a shader samples
    import scipy.ndimage                                       # noqa: F401
    VARIANTS = ("true", "fit", "reg", "true3", "reg3")
except ImportError:
    VARIANTS = ("true", "fit", "reg"); print("  (no scipy here: the cubic variants are skipped)")
RING, TAU = 4, 0.03                                             # found2: the ring (cells) and the agreement threshold


def warp_found(n, ring=False, repair=False, thr=1.0, grow=True):
    """the region at source frame k is the found region of field index k; the motion over [k, k + 1] is field k + 1's
    model, applied about the region's own centroid p (so a spin in place stays in place at mid-interval).
    ring=True (found2, 2.5c, added after 2.5b's rim diagnosis): the region dilated by RING cells, and a pixel of the
    ring accepted only where the model's two samples of it (frame k and frame k + 1) agree within TAU: the same
    material point seen twice. The found region's own cells are accepted as before."""
    t = tt(n); k = int(math.floor(t)); a = t - k
    if k not in found or k + 1 not in found: return rec[n]
    core = found[k][0]; sol = found[k + 1][1]
    if repair:                                                    # found3 (2.5d): only where the field DISAGREES with the model
        u = (fld[k + 1][4::8, 4::8, :2].astype(np.float64) - 0.5) * 64.0
        pxr, pyr = cx_ - REF[0], cy_ - REF[1]
        vx_, vy_, w_, s_ = sol
        dis = np.hypot(vx_ - w_ * pyr + s_ * pxr - u[..., 0], vy_ + w_ * pxr + s_ * pyr - u[..., 1]) > thr
        if grow: dis = ndi.binary_dilation(dis, np.ones((3, 3)))
    big = ndi.binary_dilation(core, np.ones((3, 3)), iterations=RING) if ring else core
    vx, vy, w, s = sol; dth = math.atan2(w, 1 + s)
    p = np.array([cx_[core].mean(), cy_[core].mean()])
    vp = np.array([vx - w * (p[1] - REF[1]) + s * (p[0] - REF[0]), vy + w * (p[0] - REF[0]) + s * (p[1] - REF[1])])
    qx, qy = XX - p[0] - a * vp[0], YY - p[1] - a * vp[1]
    kx, ky = R(-a * dth, qx, qy); kx, ky = kx + p[0], ky + p[1]                     # where x was in frame k
    fx, fy = R((1 - a) * dth, qx, qy); fx, fy = fx + p[0] + vp[0], fy + p[1] + vp[1]  # and where it will be in k + 1
    ci, cj = np.floor(ky / 8).astype(int), np.floor(kx / 8).astype(int)
    ok = (ci >= 0) & (ci < big.shape[0]) & (cj >= 0) & (cj < big.shape[1])
    m = np.zeros((H, W), bool); m[ok] = big[ci[ok], cj[ok]]
    v0 = sample(S(k), kx[m], ky[m]); v1 = sample(S(k + 1), fx[m], fy[m])
    if ring:
        inc = np.zeros((H, W), bool); inc[ok] = core[ci[ok], cj[ok]]
        keep = inc[m] | (np.abs(v0 - v1) < TAU)                      # the core, or the ring where the two views agree
        if repair:
            dd = np.zeros((H, W), bool); dd[ok] = dis[ci[ok], cj[ok]]
            keep &= dd[m]
        mm = np.zeros(H * W, bool); mm[np.flatnonzero(m)[keep]] = True; mm = mm.reshape(H, W)
        img = rec[n].copy(); img[mm] = ((1 - a) * v0 + a * v1)[keep]
        return img
    img = rec[n].copy()
    img[m] = (1 - a) * v0 + a * v1
    return img


if found: VARIANTS = VARIANTS + ("found", "found2", "found3", "found4")
rows = {"rec": []} | {v: [] for v in VARIANTS}; full = {k: [] for k in rows}
for n in interp:
    m = disc(geom(tt(n))[0], rad, 2.0)
    for how in VARIANTS:
        img = (warp_found(n, how in ("found2", "found3", "found4"), how in ("found3", "found4"),
                          2.0 if how == "found4" else 1.0, how != "found4") if how.startswith("found") else warp(n, how)[0])   # outside the region, exactly rec's frame
        rows[how].append(psnr(img, truth[n], m)); full[how].append(psnr(img, truth[n]))
    rows["rec"].append(psnr(rec[n], truth[n], m)); full["rec"].append(psnr(rec[n], truth[n]))
# THE CONTROL: on an exact source frame rec shows its 8-bit input, so the two agree (the path adds nothing)
ctl = [psnr(rec[n], S(int(round(tt(n)))), disc(geom(tt(n))[0], rad, 2.0)) for n in onsrc]
floor_ = [psnr(S(int(round(tt(n)))), truth[n], disc(geom(tt(n))[0], rad, 2.0)) for n in onsrc]
print(f"  CONTROL: rec on exact source frames against its 8-bit input, inside the disc: median {np.median(ctl):.2f} dB "
      f"(must be high); the 8-bit input against the truth (the input's own floor): {np.median(floor_):.2f} dB")
med = {k: np.median(v) for k, v in rows.items()}
print(f"  interpolated frames ({len(interp)}), median PSNR-Y inside the disc: " + "  ".join(f"{k} {v:.2f}" for k, v in med.items())
      + ";  full frame: " + "  ".join(f"{k} {np.median(v):.2f}" for k, v in full.items()))
R_ = np.array(rows["rec"])
for how in VARIANTS:
    D = np.array(rows[how]) - R_
    print(f"  {how:4s} - rec inside the disc: median {np.median(D):+.2f} dB, beats rec on {int((D > 0).sum())} of {len(D)} frames")
print("SUMMARY " + " ".join(f"{k}={med[k]:.2f}" for k in rows) + f" control={np.median(ctl):.2f} floor={np.median(floor_):.2f}")
