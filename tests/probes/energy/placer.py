"""ENERGY-TRANSFER.md 3.2: the impact placer prototype -- split at the impact, fit each side, intersect.

    placer.py <workdir> [src_frames=96]

On bounce-constant (flat black ground, 1280x720, 24 -> 60), using ONLY what an interpolator has -- the source frames
and the field's own velocity (read_view 4 of the four-frame propagated shader, rendered at N:N) -- and the closed
form ONLY to score:
  1. the box's centre in each source frame, by segmentation (> 0.03 on the black ground);
  2. an impact lies in [k, k+1] where the frame-to-frame displacement's component reverses;
  3. the velocity before = the field's median over the box at k - 1, after = at k + 2 (both clear of the impact);
  4. the two lines p_k + v_b (t - k) and p_{k+1} + v_a (t - k - 1) intersect, in the reversing component, at tau;
  5. an output frame at t in (k, k+1) is source frame k shifted by v_b (t - k) when t <= tau, else source frame k+1
     shifted by v_a (t - k - 1); zero fill; then quantised as the shaders' pipeline is (8-bit, limited range Y).
Each is scored as PSNR (luma, full frame) against the truth at t, beside the recommendation's and the four-frame
shader's own output at the same frames, and hold's on exact source frames as the CONTROL of the scoring path.

Pre-registered in ENERGY-TRANSFER.md (commit d2e92f6): Q1 tau within 0.1 source frames of the closed form; Q2 the
placed impact frames within 3 dB of the shaders' smooth-frame level; Q3 the placed frames beat both shaders at every
impact frame.
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
N = int(sys.argv[2]) if len(sys.argv) > 2 else 96
FF = os.environ.get("FFMPEG", "ffmpeg")
if sys.platform == "darwin" and os.environ.get("MVK_DETERMINISTIC", "1") != "0":   # MoltenVK determinism (tests/mvk-env.sh)
    os.environ.setdefault("MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS", "0")
    os.environ.setdefault("MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE", "1")
W, H = 1280, 720
SCENE = "bounce-constant"
table = {name: (kind, p) for name, kind, p, *_ in masters.masters(W, H)}
kind, b = table[SCENE]
sc = masters.Scene(kind, b, W, H, "flat", "sines", 0.0)
segs = masters.trajectory(b, float(W), float(H))
true_hits = [sg[0] for sg in segs[1:] if sg[0] < N - 2]

src = work / "src24.raw"
if not src.exists():
    with open(src, "wb") as f:
        for k in range(N):
            v = np.floor(sc.value(float(k)) * 65535 + 0.5).clip(0, 65535).astype("<u2")
            f.write(v.tobytes())
srcf = np.memmap(src, dtype="<u2", mode="r", shape=(N, H, W))

stems = {"rec": "bidirectional-interpolation-variational-propagated", "quad": "quaddirectional-interpolation-propagated"}
for k, stem in stems.items():
    (work / f"_{k}.glsl").write_text((SHADERS / f"{stem}.glsl").read_text())
t = (SHADERS / f"{stems['quad']}.glsl").read_text()
s, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t); assert n == 1
(work / "_vel.glsl").write_text(s)

def run(chain, fps, keep=None, channels=1):
    """frames out of ffmpeg as float arrays (channel 0, or u/v for the field); keep = set of frame indices"""
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo",
           "-pix_fmt", "gray16le", "-s", f"{W}x{H}", "-r", "24", "-i", str(src), "-vf", chain + ",format=rgb48le",
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
    if p.returncode != 0: sys.exit(f"ffmpeg failed: {err[:300]}")
    return out, i

def psnr(a, b):
    mse = float(np.mean((a.astype(np.float64) - b) ** 2)); return 99.0 if mse == 0 else 10 * math.log10(1.0 / mse)

def quant8(v):                                             # gray -> 8-bit limited-range Y -> back, as yuv420p does
    return (np.round(16 + 219 * np.clip(v, 0, 1)) - 16) / 219

def shift(img, d):                                         # sub-pixel translate by d = (dx, dy), zero fill, bilinear
    dx, dy = d; ix, iy = math.floor(dx), math.floor(dy); fx, fy = dx - ix, dy - iy
    def sh(a, sx, sy):
        o = np.zeros_like(a)
        ys, yd = (slice(0, H - sy), slice(sy, H)) if sy >= 0 else (slice(-sy, H), slice(0, H + sy))
        xs, xd = (slice(0, W - sx), slice(sx, W)) if sx >= 0 else (slice(-sx, W), slice(0, W + sx))
        o[yd, xd] = a[ys, xs]; return o
    return ((1 - fx) * (1 - fy) * sh(img, ix, iy) + fx * (1 - fy) * sh(img, ix + 1, iy)
            + (1 - fx) * fy * sh(img, ix, iy + 1) + fx * fy * sh(img, ix + 1, iy + 1))

# 1. the source frames' box centres, by segmentation
src01 = lambda k: srcf[k].astype(np.float32) / 65535.0
# THE SCORING PATH (the fourth run, 2026-09-30 late evening, after 2.5 found the flaw): PLACER_PATH=equal (the
# default) gives every method the SAME 8-bit frames the shader receives (swscale's yuv420p Y, read back), reads the
# shaders out of libplacebo at 16 bits (format=gray16le: no output dither), and scores the placed frames directly.
# The third run's path (PLACER_PATH=legacy) placed from the 16-bit source and pushed the result through an 8-bit
# round trip, a double quantisation the shaders do not pay (they blend two 8-bit frames in float).
EQUAL = os.environ.get("PLACER_PATH", "equal") == "equal"
if EQUAL:
    y8 = subprocess.run([FF, "-v", "error", "-f", "rawvideo", "-pix_fmt", "gray16le", "-s", f"{W}x{H}", "-r", "24", "-i", str(src),
                         "-vf", "format=yuv420p,extractplanes=y", "-f", "rawvideo", "-pix_fmt", "gray", "-"],
                        capture_output=True, check=True).stdout
    Y8 = np.frombuffer(y8, np.uint8).reshape(-1, H, W); assert len(Y8) == N
S8 = lambda k: np.clip((Y8[k].astype(np.float32) - 16) / 219, 0, 1)
cent, masks = [], []
for k in range(N):
    m = src01(k) > 0.03
    ys, xs = np.nonzero(m); cent.append(np.array([xs.mean(), ys.mean()])); masks.append(m)
cent = np.array(cent)
# the field at N:N: the box's median velocity per source frame (mask eroded 12 px)
fld, nf = run("format=yuv420p,libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=_vel.glsl", 24, channels=2)
vel = np.zeros((N, 2))
for k in range(min(N, nf)):
    m = masks[k]; e = m.copy()
    for d in (-12, 12):
        e &= np.roll(m, d, 0) & np.roll(m, d, 1)
    u = (fld[k][..., :2] - 0.5) * 2 * 32.0
    vel[k] = np.median(u[e], axis=0)

# 2-4. impacts from the displacements; tau by intersecting the two sides
disp = np.diff(cent, axis=0)                                # disp[k] = centre(k+1) - centre(k)
impacts = []
for k in range(1, N - 3):
    for c in (0, 1):
        if np.sign(disp[k - 1, c]) != np.sign(disp[k + 1, c]) and abs(disp[k - 1, c]) > 2 and abs(disp[k + 1, c]) > 2:
            vb, va = vel[k - 1], vel[k + 2]
            if abs(vb[c] - va[c]) < 1e-6: continue
            tau = (cent[k + 1, c] - cent[k, c] + vb[c] * k - va[c] * (k + 1)) / (vb[c] - va[c])
            # the reversal rule fires on the impact interval AND the one after it (both straddle a reversed displacement);
            # the second's tau lands outside its interval and was clamped to the boundary in the first run -- drop it
            if k < tau < k + 1: impacts.append((k, c, float(tau), vb, va))
print(f"# {SCENE}, {N} source frames: {len(impacts)} impacts found, {len(true_hits)} in the closed form")
for k, c, tau, vb, va in impacts:
    near = min(true_hits, key=lambda h: abs(h - tau)) if true_hits else math.nan
    print(f"  interval [{k},{k+1}] axis {'xy'[c]}: tau {tau:.3f}, closed form {near:.3f}, error {tau - near:+.3f}; "
          f"v before ({vb[0]:+.2f},{vb[1]:+.2f}) after ({va[0]:+.2f},{va[1]:+.2f}) px/frame")

# 5. the output frames within 0.5 source frames of a hit, and a sample of smooth frames
nout = int((N - 1) * 60 / 24)
tt = lambda n: n * 24 / 60
imp_frames = {n for n in range(nout) if true_hits and min(abs(tt(n) - h) for h in true_hits) < 0.5}
smooth = {n for n in range(10, nout - 10) if not true_hits or min(abs(tt(n) - h) for h in true_hits) > 2}
onsrc = {n for n in range(10, nout - 10) if n % 5 == 0}
want = imp_frames | smooth | onsrc
outs = {}
for name, chain in (("hold", "format=yuv420p,fps=60"),
                    ("rec", "format=yuv420p,libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_rec.glsl"),
                    ("quad", "format=yuv420p,libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=_quad.glsl")):
    if EQUAL and name != "hold":
        cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo", "-pix_fmt",
               "gray16le", "-s", f"{W}x{H}", "-r", "24", "-i", str(src), "-vf", chain + ":format=gray16le", "-f", "rawvideo",
               "-pix_fmt", "gray16le", "-"]
        r16 = subprocess.run(cmd, cwd=work, capture_output=True, check=True).stdout
        fr = np.frombuffer(r16, "<u2").reshape(-1, H, W)
        outs[name] = {n: fr[n].astype(np.float32) / 65535.0 for n in want if n < len(fr)}
    else:
        outs[name], _ = run(chain, 60, keep=want)
truth = {n: sc.value(tt(n)) for n in sorted(want)}
ctrl = [psnr(outs["hold"][n], truth[n]) for n in sorted(onsrc) if n in outs["hold"]]
print(f"  CONTROL: hold on exact source frames, PSNR-Y median {np.median(ctrl):.2f} dB ({len(ctrl)} frames); path "
      + ("EQUAL (8-bit input for all, shaders at 16 bits)" if EQUAL else "LEGACY (the third run's)"))
if EQUAL:
    c2 = [psnr(outs["rec"][n], S8(int(round(tt(n))))) for n in sorted(onsrc) if n in outs["rec"]]
    print(f"  CONTROL (equal path): rec on exact source frames against its 8-bit input {np.median(c2):.2f} dB (must be high)")
sm = {k: np.median([psnr(outs[k][n], truth[n]) for n in smooth if n in outs[k]]) for k in ("rec", "quad")}
print(f"  smooth frames (> 2 from a hit): rec {sm['rec']:.2f} dB, quad {sm['quad']:.2f} dB ({len(smooth)} frames)")
rows, placed_raw, meta = [], {}, {}
for n in sorted(imp_frames):
    t = tt(n)
    imp = min(impacts, key=lambda i: abs(i[2] - t)) if impacts else None
    if imp is None: continue
    k, c, tau, vb, va = imp
    # the NEARER source frame on t's own side of tau, shifted by that side's velocity
    cands = [f for f in (math.floor(t), math.ceil(t)) if (f <= tau) == (t <= tau) and 0 <= f < N]
    base = min(cands, key=lambda f: abs(f - t)) if cands else (k if t <= tau else k + 1)
    placed_raw[n] = shift(S8(base) if EQUAL else src01(base), (vb if t <= tau else va) * (t - base))
    meta[n] = (t, tau)
# THE SAME PATH AS THE SHADERS: the placed frames through ffmpeg's yuv420p round trip (the first run quantised Y
# only, and read 69 dB on exact frames where hold through the real path reads 56.7 -- an unfair ~12 dB)
if placed_raw and EQUAL:
    for n in sorted(placed_raw):
        t, tau = meta[n]
        r = (n, t, psnr(placed_raw[n], truth[n]), psnr(outs["rec"][n], truth[n]), psnr(outs["quad"][n], truth[n]))
        rows.append(r)
        print(f"  out {n:3d} t {t:6.2f} (tau {tau:.2f}): placed {r[2]:6.2f}  rec {r[3]:6.2f}  quad {r[4]:6.2f} dB")
elif placed_raw:
    order = sorted(placed_raw)
    praw = work / "placed.raw"
    with open(praw, "wb") as f:
        for n in order: f.write((np.clip(placed_raw[n], 0, 1) * 65535 + 0.5).astype("<u2").tobytes())
    # through libplacebo like the shaders' frames (swscale's plain round trip reads 56.7 dB on an exact frame where
    # libplacebo's reads 63.2: the second run put the placer 6.5 dB behind on the path alone)
    cmd = [FF, "-v", "error", "-init_hw_device", "vulkan=vk", "-filter_hw_device", "vk", "-f", "rawvideo", "-pix_fmt",
           "gray16le", "-s", f"{W}x{H}", "-r", "60", "-i", str(praw),
           "-vf", "format=yuv420p,libplacebo,format=rgb48le", "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    fb = W * H * 6
    for i, n in enumerate(order):
        im = np.frombuffer(raw[i * fb:(i + 1) * fb], np.uint16).reshape(H, W, 3)[..., 0].astype(np.float32) / 65535.0
        t, tau = meta[n]
        r = (n, t, psnr(im, truth[n]), psnr(outs["rec"][n], truth[n]), psnr(outs["quad"][n], truth[n]))
        rows.append(r)
        print(f"  out {n:3d} t {t:6.2f} (tau {tau:.2f}): placed {r[2]:6.2f}  rec {r[3]:6.2f}  quad {r[4]:6.2f} dB")
if rows:
    P = np.array([r[2:] for r in rows])
    print(f"  impact frames: median placed {np.median(P[:, 0]):.2f}, rec {np.median(P[:, 1]):.2f}, quad {np.median(P[:, 2]):.2f} dB; "
          f"placed beats both on {int(np.sum((P[:, 0] > P[:, 1]) & (P[:, 0] > P[:, 2])))} of {len(P)}")
