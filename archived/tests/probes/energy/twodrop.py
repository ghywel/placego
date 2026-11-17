"""ENERGY-TRANSFER.md 1.5 and the survey's unit-free witness: a bouncing box's parabolas, and T^2 / h.

    twodrop.py <workdir> [bg=flat|textured] [texture=noise] [src_frames=240] [seg=auto|pixels|median|field|plate]

A textured box (320 x 202 at 1280 x 720) dropped from rest under gravity, drifting 1.5 px/frame sideways, bouncing
on the floor with restitution 0.8 (PHYSICAL restitution: vy -> -0.8 vy, vx unchanged; the masters' bounce keeps its
speed, which is not). g = 0.569 px/frame^2, so the first contact is at 19.2 px/frame. From ONLY what an interpolator
has -- the source frames and the field -- and the closed form ONLY to score:
  1. the box's centre per source frame: segmentation on the flat ground (> 0.02), or, on the textured ground,
     subtraction of the static background (the per-pixel temporal median of the clip, a static camera's standard),
     or (seg=field, added 2026-09-30 AFTER the median's miss: the median is the box wherever the box dwells, near the
     floor in the late low bounces) the field's own moving region, |u| > 0.75 px/frame on a 4-px grid, the ground
     being still. A constant time offset of the field (its recorded off-by-one) moves every contact alike: T and h,
     and so the witness, are immune to it. It FAILED (spurious regions up to 245 px away, a half-frame lag, the
     flights split into fragments), so: seg=plate, a CLEAN PLATE, the ground filmed empty before the throw (the
     camera step's recipe), subtracted;
  2. impacts where the vertical displacement reverses from falling to rising;
  3. a FREE parabola per flight (y = a t^2 + b t + c, least squares on that flight's frames; nothing assumes g);
  4. each impact time tau where the parabolas either side intersect (1.5: "where they meet is the impact's time");
  5. per complete flight: T = tau_(i+1) - tau_i and the rise h = y(contact) - y(apex), both from the fits;
  6. THE UNIT-FREE WITNESS: T^2 / h is 8 / g for every flight, so (T_i / T_j)^2 = h_i / h_j with no g, no scale,
     no frame rate. Its spread across flights, and the pairwise ratio errors, are the numbers;
  7. beside it, g the field's way (1.1's): the slope of the field's vertical velocity over each flight.
Numbers only.
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
BG = sys.argv[2] if len(sys.argv) > 2 else "flat"
TEX = sys.argv[3] if len(sys.argv) > 3 else "noise"
N = int(sys.argv[4]) if len(sys.argv) > 4 else 240
SEG = sys.argv[5] if len(sys.argv) > 5 else "auto"
SEG = ("pixels" if BG == "flat" else "median") if SEG == "auto" else SEG
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
W, H = 1280, 720
BW, BH = 320, 202
X0, Y0, VX, E = 474.0, 295.0, 1.5, 0.8
YB = H - BH / 2                                                 # the centre's height at contact
G = 19.2 ** 2 / (2 * (YB - Y0))

# the closed form: contact times, and the centre at any t
taus, vups = [math.sqrt(2 * (YB - Y0) / G)], []
v = G * taus[0]
while taus[-1] < N + 60:
    v *= E; vups.append(v); taus.append(taus[-1] + 2 * v / G)


def centre(t):
    if t < taus[0]: return X0 + VX * t, Y0 + G * t * t / 2
    i = max(j for j in range(len(taus)) if taus[j] <= t)
    s = t - taus[i]
    return X0 + VX * t, YB - vups[i] * s + G * s * s / 2


ys_, xs_ = np.mgrid[0:H, 0:W]
XX, YY = xs_ + 0.5, ys_ + 0.5
GROUND = np.zeros((H, W)) if BG == "flat" else masters.clamp01(masters.tex(XX, YY) * 0.35 + 0.1)


def frame(t):
    cx, cy = centre(t); x0, y0 = cx - BW / 2, cy - BH / 2
    covx = masters.clamp01(np.minimum(x0 + BW, XX + 0.5) - np.maximum(x0, XX - 0.5))
    covy = masters.clamp01(np.minimum(y0 + BH, YY + 0.5) - np.maximum(y0, YY - 0.5))
    cov = covx * covy
    inside = masters.clamp01(masters.tex_value(TEX, XX - x0, YY - y0) * 0.9 + 0.05)
    return np.where(cov > 0, GROUND + (inside - GROUND) * cov, GROUND)


src = work / f"src-{BG}-{TEX}.raw"
if not src.exists():
    with open(src, "wb") as f:
        for k in range(N): f.write(np.floor(frame(float(k)) * 65535 + 0.5).clip(0, 65535).astype("<u2").tobytes())
srcf = np.memmap(src, dtype="<u2", mode="r", shape=(N, H, W))
S = lambda k: srcf[k].astype(np.float32) / 65535.0

# 1. the centres
if SEG == "pixels":
    masks = [S(k) > 0.02 for k in range(N)]
elif SEG == "field":
    masks = None                                                 # filled from the field below
elif SEG == "plate":
    masks = []
    for k in range(N):
        m = np.abs(S(k) - GROUND) > 0.04                          # the plate: the ground alone, filmed before the throw
        rows_, cols_ = m.mean(1) > 0.15 * BW / W, m.mean(0) > 0.15 * BH / H
        masks.append(m & rows_[:, None] & cols_[None, :])
else:
    med = np.median(np.stack([S(k)[::2, ::2] for k in range(0, N, 2)]), axis=0)
    med = np.repeat(np.repeat(med, 2, 0), 2, 1)[:H, :W]
    masks = []
    for k in range(N):
        m = np.abs(S(k) - med) > 0.04
        # the box is one big blob: keep the rows and columns where it is dense (a stray pixel of residual cannot move it)
        rows_, cols_ = m.mean(1) > 0.15 * BW / W, m.mean(0) > 0.15 * BH / H
        masks.append(m & rows_[:, None] & cols_[None, :])
print(f"# twodrop: bg {BG}, texture {TEX}, seg {SEG}, {N} source frames; g {G:.4f} px/frame^2, first contact {taus[0]:.3f}")

# the field's vertical velocity (the four-frame shader's read_view 4 at N:N), median over each frame's box eroded 12 px
t_ = (SHADERS / "quaddirectional-interpolation-propagated.glsl").read_text()
s_, n_ = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t_); assert n_ == 1
(work / "_vel.glsl").write_text(s_)
cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo", "-pix_fmt", "gray16le",
       "-s", f"{W}x{H}", "-r", "24", "-i", str(src), "-vf",
       "format=yuv420p,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_vel.glsl,format=rgb48le", "-f", "rawvideo", "-"]
p = subprocess.Popen(cmd, cwd=work, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
fvy = np.full(N, np.nan); k = 0; fb = W * H * 6; fcent = np.full((N, 2), np.nan)
while k < N:
    buf = p.stdout.read(fb)
    if len(buf) < fb: break
    u = (np.frombuffer(buf, np.uint16).reshape(H, W, 3)[..., :2].astype(np.float32) / 65535.0 - 0.5) * 64.0
    if SEG == "field":
        g4 = u[2::4, 2::4]; mv = np.hypot(g4[..., 0], g4[..., 1]) > 0.75
        rows_, cols_ = mv.mean(1) > 0.15 * BW / W, mv.mean(0) > 0.15 * BH / H     # the one big blob, as the median's
        mv &= rows_[:, None] & cols_[None, :]
        if mv.any():
            fcent[k] = [XX[2::4, 2::4][mv].mean(), YY[2::4, 2::4][mv].mean()]
            e = mv.copy()
            for d in (-3, 3): e &= np.roll(mv, d, 0) & np.roll(mv, d, 1)
            if e.any(): fvy[k] = float(np.median(g4[..., 1][e]))
    else:
        m = masks[k]; e = m.copy()
        for d in (-12, 12): e &= np.roll(m, d, 0) & np.roll(m, d, 1)
        if e.any(): fvy[k] = float(np.median(u[..., 1][e]))
    k += 1
err = p.stderr.read().decode(); p.wait()
if p.returncode != 0 or "compile status" in err: sys.exit(f"ffmpeg failed: {err[:300]}")
if np.nanmax(np.abs(fvy)) < 0.5: sys.exit("the field read ZERO on a falling box: the read path is broken (see feedback_field_read_path)")
cent = fcent if SEG == "field" else np.array([[XX[m].mean(), YY[m].mean()] if m.any() else [np.nan, np.nan] for m in masks])
truth_c = np.array([centre(float(k)) for k in range(N)])
err_c = np.abs(cent - truth_c)
print(f"  the centres against the closed form: median |error| x {np.nanmedian(err_c[:, 0]):.3f}, y {np.nanmedian(err_c[:, 1]):.3f} px; "
      f"max y {np.nanmax(err_c[:, 1]):.3f}")

# 2. impacts: each LOWEST point, a strong local maximum of the centre's y. The contact lies in [m - 1, m + 1], and
# from positions alone frame m's side is ambiguous, so neither flight's fit uses it; the intersection places it
yv = cent[:, 1]
imp = [m for m in range(2, N - 2) if yv[m] >= yv[m - 1] and yv[m] >= yv[m + 1] and yv[m] - yv[m - 2] > 2 and yv[m] - yv[m + 2] > 2]
starts = [0] + [m + 1 for m in imp]; ends = [m - 1 for m in imp] + [N - 1]
flights = list(zip(starts, ends))
assert all(b - a >= 3 for a, b in flights), f"a flight too short to fit: {flights}"
# 3. a free parabola per flight
fits = []
for a, b in flights:
    tt = np.arange(a, b + 1, dtype=np.float64); y = yv[a:b + 1]; ok = ~np.isnan(y)
    fits.append(np.polyfit(tt[ok], y[ok], 2))
# 4. tau per impact: the parabolas either side intersect inside [m - 1, m + 1]
rows = []
for i, m in enumerate(imp):
    roots = [r.real for r in np.roots(fits[i] - fits[i + 1]) if abs(r.imag) < 1e-9 and m - 1 <= r.real <= m + 1]
    tau = min(roots, key=lambda r: abs(r - m)) if roots else float("nan")
    rows.append((m, tau, min(taus, key=lambda x: abs(x - m))))
print(f"  impacts found {len(rows)}; closed-form contacts in range {sum(1 for x in taus if 2 < x < N - 3)}")
for m, tau, tt_ in rows:
    print(f"    lowest frame {m:3d}  tau {tau:8.3f}  closed form {tt_:8.3f}  error {tau - tt_:+.3f} frames")

# 5-6. per complete flight: T and h from the fits, and the unit-free witness
wit = []
for i in range(1, len(fits) - 1):
    t0, t1 = rows[i - 1][1], rows[i][1]
    if math.isnan(t0) or math.isnan(t1): continue
    a2, b2, c2 = fits[i]
    T = t1 - t0
    ycont = (np.polyval(fits[i], t0) + np.polyval(fits[i], t1)) / 2
    h = ycont - (c2 - b2 * b2 / (4 * a2))
    j = min(range(len(taus) - 1), key=lambda j: abs(taus[j] - t0))
    Tt = taus[j + 1] - taus[j]; ht = vups[j] ** 2 / (2 * G)
    fa, fb_ = flights[i][0] + 1, flights[i][1] - 1           # the field's frames clear of both contacts
    tf = np.arange(fa, fb_ + 1); vv = fvy[fa:fb_ + 1]; okv = ~np.isnan(vv)
    gfield = np.polyfit(tf[okv], vv[okv], 1)[0] if okv.sum() >= 3 else float("nan")
    wit.append((T, h, Tt, ht, 2 * a2, gfield))
    print(f"    flight {i}: T {T:7.3f} (truth {Tt:7.3f})  h {h:7.2f} px (truth {ht:7.2f})  T^2/h {T * T / h:.4f} (truth {8 / G:.4f})"
          f"  g: the fit's curvature {2 * a2:.4f}, the field's slope {gfield:.4f} (truth {G:.4f})")
if len(wit) >= 2:
    q = np.array([T * T / h for T, h, *_ in wit])
    print(f"  THE UNIT-FREE WITNESS: T^2/h over {len(q)} flights: spread (SD / mean) {100 * q.std() / q.mean():.2f} %; "
          f"mean {q.mean():.4f} against 8/g {8 / G:.4f} ({100 * (q.mean() * G / 8 - 1):+.2f} %)")
    pr = [abs((wit[i][0] / wit[j][0]) ** 2 / (wit[i][1] / wit[j][1]) - 1) for i in range(len(wit)) for j in range(i + 1, len(wit))]
    print(f"  pairwise (T_i/T_j)^2 against h_i/h_j: median |error| {100 * np.median(pr):.2f} %, max {100 * max(pr):.2f} % over {len(pr)} pairs")
    gf = np.array([w[5] for w in wit]); gc = np.array([w[4] for w in wit])
    print(f"  g from the fits' curvature: {np.mean(gc):.4f} ({100 * (np.mean(gc) / G - 1):+.2f} %); from the field's slope: "
          f"{np.nanmean(gf):.4f} ({100 * (np.nanmean(gf) / G - 1):+.2f} %), per-flight spread {100 * np.nanstd(gf) / np.nanmean(gf):.1f} %")
tau_err = [abs(r[1] - r[2]) for r in rows if not math.isnan(r[1])]
if tau_err:
    te = np.array([r[1] - r[2] for r in rows if not math.isnan(r[1])])
    print(f"  tau's error: median {np.median(te):+.3f}, spread about it (median |dev|) {np.median(np.abs(te - np.median(te))):.3f} frames "
          f"(a constant offset is the field's timing, which T and h do not see)")
print(f"SUMMARY bg={BG} seg={SEG} tex={TEX} impacts={len(rows)} tau_err_median={np.median(tau_err) if tau_err else float('nan'):.3f} "
      f"tau_err_max={max(tau_err) if tau_err else float('nan'):.3f} flights={len(wit)}")
