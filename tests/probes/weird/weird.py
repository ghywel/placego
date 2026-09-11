#!/usr/bin/env python3
"""WEIRD GEOMETRY: five verb-object scenes whose velocity AND gradient-tensor fields are analytic and
NON-CONSTANT, read by the instruments that already exist (read_view 4: velocity; read_view 9: divergence,
curl, first shear). 2026-09-10, the owner's "really weird forms of synthetic geometry".

The tensor was proven this morning on constant fields, one component live at a time. Every scene here asks
something it has never been asked, and each has a closed-form inverse map in T so the ground-truth property
holds (the same expression at any frame rate is the same physical scene):

  spiral   z(t) = z0 e^{(a+ib)t}                       divergence AND curl live at once, both constant
  vortex   theta(t) = theta0 + w(r) t, w Gaussian in r  curl and shear varying smoothly in SPACE (the disc's flow)
  flag     y = y0 + A sin(kx - Wt)                      a curl field sinusoidal in x: a WAVELENGTH SWEEP gives the
                                                        instrument's spatial transfer function; and the crest moves
                                                        at W/k while the material moves at A W -- phase vs material
  jelly    x = x0 e^{K(1-cos Wt)/W}, y = y0 e^{-...}    the first shear oscillating in TIME: gain and phase lag
  bird     two wings hinged on a static body            a curl that flips sign across a hinge INSIDE one object:
                                                        the crease, and how wide the instrument smears it

Usage:  weird.py render      (all scenes, both views, N:N at 24 fps, 48 frames each)
        weird.py score       (tables)
        weird.py all
"""
import os
import pathlib
import re
import subprocess
import sys

import numpy as np

# run from a shell with the project's ffmpeg build and mingw64/bin on PATH, as every tool in tests/ does
NP = pathlib.Path(os.environ.get("NP_SCRATCH", "E:/nframe-project/np-scratch"))   # data, renders, logs live here
G = NP / "weird"
SC = pathlib.Path(__file__).resolve().parents[3]                                  # scripts/
W, H, FPS = 1280, 720, 24.0
CX, CY = 640.0, 360.0
FRAMES = 48
# the reading takes ~20 frames to settle on a field that changes everywhere (measured: the spiral's residual
# falls from 12 px/frame at frame 8 to 0.6 at frame 20 and stays); SKIP=8 polluted the first scores
SKIP = int(os.environ.get("SKIP", "20"))
FS_VEL, FS_DERIV = 32.0, 0.5
# TEX=M2: the ladder's 40 px periodic lattice. TEX=M1: the ladder's aperiodic five-sinusoid texture. The
# switch exists to separate "deformation defeats the matcher" from "a periodic lattice aliases under deformation".
TEXNAME = os.environ.get("TEX", "M2")
TEXTURES = {
    "M2": "128+110*sin(({x})/6.366)*sin(({y})/6.366)",
    # M2W: the same lattice at a 120 px period, 7.5 texels at the coarse level's 1/16 resolution -- above its
    # Nyquist even compressed by the jelly's 1.58 (4.7 texels). If the cliff is the coarse level's wagon-wheel
    # reversal of a near-Nyquist lattice, this texture moves the cliff; if not, it does not.
    "M2W": "128+110*sin(({x})/19.1)*sin(({y})/19.1)",
    "M1": ("128+22*(sin(0.15*({x})+0.09*({y}))+sin(0.28*({x})-0.21*({y}))+sin(0.51*({x})+0.44*({y}))"
           "+sin(0.83*({x})-0.97*({y}))+sin(1.21*({x})+0.64*({y})))"),
}
TEX = TEXTURES[TEXNAME]
SUFFIX = "" if TEXNAME == "M2" else f"_{TEXNAME}"
ONLY = [s for s in os.environ.get("ONLY", "").split(",") if s]


def tex(x, y):
    return TEX.format(x=x, y=y)


# ---- the scenes: geq expression and analytic truth ----------------------------------------------------------
# each truth(T, X, Y) returns dict(u, v, div, curl, shear, mask) in px/frame and 1/frame, on the image grid
def spiral():
    a, b = 0.24, 0.48
    expr = (f"st(0,X-{CX});st(1,Y-{CY});st(2,exp(-{a}*T));st(3,cos({b}*T));st(4,sin({b}*T));"
            f"st(5,ld(2)*(ld(0)*ld(3)+ld(1)*ld(4)));st(6,ld(2)*(-ld(0)*ld(4)+ld(1)*ld(3)));" + tex("ld(5)", "ld(6)"))

    def truth(T, X, Y):
        dx, dy = X - CX, Y - CY
        return dict(u=(a * dx - b * dy) / FPS, v=(b * dx + a * dy) / FPS,
                    div=np.full_like(dx, 2 * a / FPS), curl=np.full_like(dx, 2 * b / FPS), shear=np.zeros_like(dx),
                    mask=(np.abs(dx) < 500) & (np.abs(dy) < 280))
    return expr, truth


def vortex(w0=1.2):
    s2 = 200.0 ** 2
    expr = (f"st(0,X-{CX});st(1,Y-{CY});st(2,{w0}*exp(-(ld(0)*ld(0)+ld(1)*ld(1))/{2 * s2})*T);"
            f"st(3,ld(0)*cos(ld(2))+ld(1)*sin(ld(2)));st(4,-ld(0)*sin(ld(2))+ld(1)*cos(ld(2)));"
            f"if(lt(hypot(ld(0),ld(1)),380)," + tex("ld(3)", "ld(4)") + ",20)")

    def truth(T, X, Y):
        dx, dy = X - CX, Y - CY
        r2 = dx * dx + dy * dy
        w = w0 * np.exp(-r2 / (2 * s2))
        return dict(u=-w * dy / FPS, v=w * dx / FPS, div=np.zeros_like(dx),
                    curl=w * (2 - r2 / s2) / FPS, shear=2 * (w / s2) * dx * dy / FPS,
                    mask=np.sqrt(r2) < 330)
    return expr, truth


def flag(lam):
    A, Om = 16.0, 6.2832
    k = 2 * np.pi / lam
    expr = tex("X", f"Y-{A}*sin({k:.6f}*X-{Om}*T)")

    def truth(T, X, Y):
        ph = k * X - Om * T
        return dict(u=np.zeros_like(X), v=-A * Om * np.cos(ph) / FPS, div=np.zeros_like(X),
                    curl=A * Om * k * np.sin(ph) / FPS, shear=np.zeros_like(X),
                    mask=(X > 60) & (X < W - 60) & (Y > 60) & (Y < H - 60))
    return expr, truth


def jelly(K=0.72):
    Om = 3.1416
    expr = (f"st(0,exp(-{K}*(1-cos({Om}*T))/{Om}));st(1,(X-{CX})*ld(0));st(2,(Y-{CY})/ld(0));" + tex("ld(1)", "ld(2)"))

    def truth(T, X, Y):
        dx, dy = X - CX, Y - CY
        s = K * np.sin(Om * T)
        return dict(u=s * dx / FPS, v=-s * dy / FPS, div=np.zeros_like(dx), curl=np.zeros_like(dx),
                    shear=np.full_like(dx, 2 * s / FPS), mask=(np.abs(dx) < 420) & (np.abs(dy) < 260))
    return expr, truth


def bird():
    A, Om = 0.5, 3.1416
    HL, HR = 580.0, 700.0
    expr = (f"st(0,{A}*sin({Om}*T));st(1,cos(ld(0)));st(2,sin(ld(0)));"
            f"st(3,(X-{HL})*ld(1)+(Y-{CY})*ld(2));st(4,-(X-{HL})*ld(2)+(Y-{CY})*ld(1));"
            f"st(5,(X-{HR})*ld(1)-(Y-{CY})*ld(2));st(6,(X-{HR})*ld(2)+(Y-{CY})*ld(1));"
            f"if(gt(ld(3),-200)*lt(ld(3),0)*lt(abs(ld(4)),30)," + tex("ld(3)+1000", "ld(4)") + ","
            f"if(gt(ld(5),0)*lt(ld(5),200)*lt(abs(ld(6)),30)," + tex("ld(5)+2000", "ld(6)") + ","
            f"if(lt(abs(X-{CX}),60)*lt(abs(Y-{CY}),40)," + tex("X", "Y") + ",20)))")

    def truth(T, X, Y):
        th = A * np.sin(Om * T); thd = A * Om * np.cos(Om * T)
        c, s = np.cos(th), np.sin(th)
        px, py = X - HL, Y - CY
        xl, yl = px * c + py * s, -px * s + py * c
        left = (xl > -200) & (xl < 0) & (np.abs(yl) < 30)
        qx, qy = X - HR, Y - CY
        xr, yr = qx * c - qy * s, qx * s + qy * c
        right = (xr > 0) & (xr < 200) & (np.abs(yr) < 30)
        body = (np.abs(X - CX) < 60) & (np.abs(Y - CY) < 40) & ~left & ~right
        u = np.where(left, -thd * py, np.where(right, thd * qy, 0.0)) / FPS
        v = np.where(left, thd * px, np.where(right, -thd * qx, 0.0)) / FPS
        curl = np.where(left, 2 * thd, np.where(right, -2 * thd, 0.0)) / FPS
        return dict(u=u, v=v, div=np.zeros_like(u), curl=curl, shear=np.zeros_like(u),
                    mask=left | right | body, left=left, right=right, body=body, thd=thd)
    return expr, truth


SCENES = [("spiral", spiral()), ("vortex", vortex()), ("jelly", jelly()), ("bird", bird())] + \
         [(f"flag{lam}", flag(lam)) for lam in (1280, 640, 320, 160, 80)]
# THE STRAIN-RATE LADDER (the two cheap tests that are one design): the jelly's K and the vortex's w0 each
# halved four times from the failing values. K is the peak strain rate in 1/s; w0 the core's angular rate.
# The failing fraction against strain rate is the curve the mechanism has to explain.
LADDER = [(f"jellyK{K:g}", jelly(K)) for K in (0.72, 0.36, 0.18, 0.09, 0.045)] + \
         [(f"vortexW{w:g}", vortex(w)) for w in (1.2, 0.6, 0.3, 0.15, 0.075)]
if os.environ.get("LADDER") == "1":
    SCENES = LADDER
if ONLY:
    SCENES = [s for s in SCENES if s[0] in ONLY]


# ---- rendering ----------------------------------------------------------------------------------------------
def make_shaders():
    src = (SC / "shaders" / "quaddirectional-interpolation-propagated.glsl").read_text(encoding="utf-8")
    for view, name in ((4, "vel.glsl"), (9, "tensor.glsl")):
        t, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>" + str(view) + "\n", src)
        assert n == 1
        (G / name).write_text(t, encoding="utf-8", newline="\n")


def render(name, expr, view):
    out = G / f"{name}{SUFFIX}_{view}"
    if out.exists():
        for f in out.glob("*.png"):
            f.unlink()
    out.mkdir(parents=True, exist_ok=True)
    esc = expr.replace(",", "\\,").replace(";", "\\;")
    graph = f"nullsrc=s={W}x{H}:r=24:d=3,format=gray,geq=lum='{esc}',format=yuv420p"
    shader = "vel.glsl" if view == "vel" else "tensor.glsl"
    r = subprocess.run(["ffmpeg.exe", "-y", "-hide_banner", "-loglevel", "error", "-init_hw_device", "vulkan=vk",
                        "-filter_hw_device", "vk", "-f", "lavfi", "-i", graph,
                        "-vf", f"libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path={shader},format=rgb48le",
                        "-frames:v", str(FRAMES), str(out / "f%03d.png")], cwd=str(G), capture_output=True, text=True)
    n = len(list(out.glob("f*.png")))
    print(f"  {name:9s} {view:6s} {n} frames" + ("" if n == FRAMES else f"  SHORT: {r.stderr[:200]}"), flush=True)
    assert n == FRAMES, (name, view, r.stderr[:300])


def picture(name, expr):
    esc = expr.replace(",", "\\,").replace(";", "\\;")
    graph = f"nullsrc=s={W}x{H}:r=24:d=1,format=gray,geq=lum='{esc}',format=yuv420p"
    subprocess.run(["ffmpeg.exe", "-y", "-hide_banner", "-loglevel", "error", "-f", "lavfi", "-i", graph,
                    "-frames:v", "1", "-update", "1", str(G / f"{name}_frame0.png")], check=True)


# ---- scoring ------------------------------------------------------------------------------------------------
def load(p, fs):
    raw = subprocess.run(["ffmpeg.exe", "-v", "error", "-i", str(p), "-f", "rawvideo", "-pix_fmt", "rgb48le", "-"],
                         capture_output=True, check=True).stdout
    return (np.frombuffer(raw, np.uint16).reshape(H, W, 3).astype(np.float64) / 65535.0 - 0.5) * 2 * fs


def fit(read, truth):
    """gain and correlation of read against truth over the samples given, plus rms residual after the gain."""
    tr = truth - truth.mean(); rd = read - read.mean()
    if tr.std() < 1e-12:
        return dict(gain=np.nan, corr=np.nan, resid=read.std(), truth_rms=0.0, bias=read.mean() - truth.mean())
    gain = (rd * tr).sum() / (tr * tr).sum()
    corr = (rd * tr).sum() / np.sqrt((rd * rd).sum() * (tr * tr).sum())
    resid = np.sqrt(np.mean((read - (truth.mean() + gain * tr)) ** 2))
    return dict(gain=gain, corr=corr, resid=resid, truth_rms=np.sqrt(np.mean(truth ** 2)), bias=read.mean() - truth.mean())


def score(name, truth, step=4):
    Y, X = np.mgrid[0:H, 0:W]
    Xs, Ys = X[::step, ::step].astype(np.float64), Y[::step, ::step].astype(np.float64)
    acc = {k: ([], []) for k in ("u", "v", "div", "curl", "shear")}
    extras = []                      # per-frame SUMMARIES only: keeping whole fields for nine scenes ran out of memory
    for k in range(SKIP, FRAMES):
        T = k / FPS
        tr = truth(T, Xs, Ys)
        vel = load(G / f"{name}{SUFFIX}_vel" / f"f{k + 1:03d}.png", FS_VEL)[::step, ::step].copy()
        ten = load(G / f"{name}{SUFFIX}_tensor" / f"f{k + 1:03d}.png", FS_DERIV)[::step, ::step].copy()
        m = tr["mask"]
        reads = dict(u=vel[..., 0], v=vel[..., 1], div=ten[..., 0], curl=ten[..., 1], shear=ten[..., 2])
        for comp in acc:
            acc[comp][0].append(reads[comp][m].astype(np.float32)); acc[comp][1].append(tr[comp][m].astype(np.float32))
        ex = dict(T=T, shear_med=float(np.median(reads["shear"][m])))
        if "left" in tr:
            ex.update(thd=float(tr["thd"]),
                      left=float(np.median(reads["curl"][tr["left"]])), right=float(np.median(reads["curl"][tr["right"]])),
                      body=float(np.median(reads["curl"][tr["body"]])),
                      row_read=reads["curl"][int(CY) // step].copy(), row_truth=tr["curl"][int(CY) // step].copy())
        extras.append(ex)
        del vel, ten, reads, tr
    out = {comp: fit(np.concatenate(r), np.concatenate(t)) for comp, (r, t) in acc.items()}
    # the FAILING FRACTION: samples whose read direction is more than 45 degrees off the truth, among those
    # whose truth speed exceeds 1 px/frame -- the minority that locks to a wrong vector, as a single number
    ru, rv = np.concatenate(acc["u"][0]), np.concatenate(acc["v"][0])
    tu, tv = np.concatenate(acc["u"][1]), np.concatenate(acc["v"][1])
    moving = np.hypot(tu, tv) > 1.0
    ang = np.degrees(np.abs(np.arctan2(ru * tv - rv * tu, ru * tu + rv * tv)))
    out["failing"] = float(np.mean(ang[moving] > 45)) if moving.any() else float("nan")
    out["moving"] = int(moving.sum())
    return out, extras


def table(name, out):
    print(f"\n== {name}   failing fraction (direction off by >45 deg, truth speed >1): {out['failing']:.3f} of {out['moving']} samples")
    print(f"   {'component':9s} {'truth rms':>10} {'gain':>7} {'corr':>7} {'resid':>8} {'bias':>8}")
    for comp, f in out.items():
        if comp in ("failing", "moving"):
            continue
        g = f"{f['gain']:7.3f}" if np.isfinite(f['gain']) else "   (0) "
        c = f"{f['corr']:7.3f}" if np.isfinite(f['corr']) else "      -"
        print(f"   {comp:9s} {f['truth_rms']:10.4f} {g} {c} {f['resid']:8.4f} {f['bias']:+8.4f}")


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode in ("render", "all"):
        make_shaders()
        for name, (expr, _) in SCENES:
            picture(name, expr)
            for view in ("vel", "tensor"):
                render(name, expr, view)
    if mode in ("score", "all"):
        results = {}
        for name, (_, truth) in SCENES:
            out, pf = score(name, truth)
            results[name] = (out, pf)
            table(name, out)
        # the flag sweep: the tensor's spatial transfer function
        flags = [lam for lam in (1280, 640, 320, 160, 80) if f"flag{lam}" in results]
        if flags:
            print("\n== flag: gain against wavelength (the instrument's spatial transfer function)")
            print(f"   {'wavelength px':>14} {'v gain':>7} {'v corr':>7} {'curl gain':>10} {'curl corr':>10} {'curl truth rms':>15}")
        for lam in flags:
            o = results[f"flag{lam}"][0]
            print(f"   {lam:14d} {o['v']['gain']:7.3f} {o['v']['corr']:7.3f} {o['curl']['gain']:10.3f} {o['curl']['corr']:10.3f} {o['curl']['truth_rms']:15.4f}")
        if "bird" not in results or "jelly" not in results:
            print("\nWEIRD DONE (subset)")
            sys.exit(0)
        # the jelly: per-frame median shear against the sinusoid, with the phase lag fitted
        out, pf = results["jelly"]
        Ts = np.array([p["T"] for p in pf]); med = np.array([p["shear_med"] for p in pf])
        K, Om = 0.72, 3.1416
        best = None
        for lag in np.arange(-1.0, 1.001, 0.05):            # lag in FRAMES
            tr = 2 * K * np.sin(Om * (Ts + lag / FPS)) / FPS
            c = np.corrcoef(med, tr)[0, 1]
            if best is None or c > best[0]:
                best = (c, lag, (med * tr).sum() / (tr * tr).sum())
        print(f"\n== jelly: per-frame median shear vs 2K sin(Wt)/fps: best correlation {best[0]:.4f} at a lag of "
              f"{best[1]:+.2f} frames, gain there {best[2]:.3f}")
        # the bird: the crease
        out, pf = results["bird"]
        print("\n== bird: median curl per part, at the frames of largest wing speed")
        print(f"   {'T':>5} {'thetadot':>9} {'left truth':>11} {'left read':>10} {'right read':>11} {'body read':>10}")
        for p in pf:
            if abs(p["thd"]) > 1.4:
                print(f"   {p['T']:5.2f} {p['thd']:9.3f} {2 * p['thd'] / FPS:11.4f} {p['left']:10.4f} "
                      f"{p['right']:11.4f} {p['body']:10.4f}")
        # the crease width: curl along the wing's centre line through the left hinge, at one such frame
        p = max(pf, key=lambda q: abs(q["thd"]))
        T = p["T"]
        step = 4
        xs = np.arange(0, W, step)
        prof = p["row_read"]
        truthp = p["row_truth"]
        sel = (xs > 480) & (xs < 800)
        print(f"   crease profile at T={T:.2f} along y=360, x from 480 to 800 (hinges at 580 and 700):")
        print("   x:     " + " ".join(f"{x:6d}" for x in xs[sel][::2]))
        print("   truth: " + " ".join(f"{t:6.3f}" for t in truthp[sel][::2]))
        print("   read:  " + " ".join(f"{r:6.3f}" for r in prof[sel][::2]))
        print("\nWEIRD DONE")
