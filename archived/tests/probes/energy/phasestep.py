"""ENERGY-TRANSFER.md 5.2: a phase-based estimator on 5.1's one-frame step sweep -- how far is the field from the bound?

    phasestep.py [steps=0.05,0.1,0.2,0.3,0.5,1.0] [sigmas=0,1,2,4] [sizes=268]

sizes (5.2b): the side of a CENTRED square region inside each 300 px square (268 = the whole eroded square).

CPU only (numpy), no GPU and no ffmpeg: it rebuilds substep.py's frames exactly (the same squares, texture,
step at frame 24, and the same seeded noise), and estimates the horizontal shift between consecutive frames of each
square's region (eroded 16 px, as substep.py scores) by the Fourier shift theorem: the cross-power spectrum
F1 conj(F0) has phase -2 pi (u dx + v dy) for a rigid shift, so a weighted least-squares fit of that phase against
frequency, over the bins where the texture has energy (and away from the wrap), is the shift. A Hann window keeps
the region's edges out of the spectrum.

Scored like substep.py: the NOISE is the frame-to-frame spread of the estimate over quiet frames (the control and
the mover away from the step), the SIGNAL the mover's estimate across the step (frame 23 -> 24). Detected when
S/N > 3. The quantisation matches the shaders' input: 8-bit (limited range Y), as their pipeline sees it.

Pre-registered in ENERGY-TRANSFER.md 5.2 (before it ran): Q1 the step read at 95-105 percent at every size; Q2 at
sigma 4 a 0.05 px step detected at S/N > 10.
"""
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[2]))
import masters                                                                   # noqa: E402

steps = [float(v) for v in (sys.argv[1] if len(sys.argv) > 1 else "0.05,0.1,0.2,0.3,0.5,1.0").split(",")]
sigmas = [float(v) for v in (sys.argv[2] if len(sys.argv) > 2 else "0,1,2,4").split(",")]
sizes = [int(v) for v in (sys.argv[3] if len(sys.argv) > 3 else "268").split(",")]
W, H, S, NF, STEP_AT = 1280, 720, 300, 48, 24
MOV = (200, 210); CTL = (780, 210); ER = 16
yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)

def frame(shift):                                            # substep.py's frame(), verbatim in effect
    img = np.zeros((H, W))
    for (x0, y0), dx in ((MOV, shift), (CTL, 0.0)):
        inside = (xx >= x0 + dx) & (xx < x0 + dx + S) & (yy >= y0) & (yy < y0 + S)
        img = np.where(inside, masters.clamp01(masters.tex(xx - x0 - dx, yy - y0)), img)
    return img

def quant(v):                                                # what the shaders see: 8-bit limited-range Y
    return (np.round(16 + 219 * np.clip(v, 0, 1)) - 16) / 219

def setup(n):
    global win, fy, fx
    win = np.outer(np.hanning(n), np.hanning(n))
    fy = np.fft.fftfreq(n)[:, None] * np.ones((1, n)); fx = np.ones((n, 1)) * np.fft.fftfreq(n)[None, :]

def shift_est(a, b):
    """dx, dy of b relative to a, by the phase slope of the cross-power spectrum"""
    A = np.fft.fft2((a - a.mean()) * win); B = np.fft.fft2((b - b.mean()) * win)
    C = B * np.conj(A)
    mag = np.abs(C)
    keep = (mag > np.percentile(mag, 90)) & (np.abs(fx) < 0.2) & (np.abs(fy) < 0.2) & ((fx != 0) | (fy != 0))
    ph = np.angle(C[keep]); u = fx[keep]; v = fy[keep]; w = mag[keep]
    # phase = -2 pi (u dx + v dy): weighted least squares, iterated once to unwrap against the first estimate
    M = np.stack([-2 * np.pi * u, -2 * np.pi * v], 1)
    sol = np.linalg.lstsq(M * w[:, None], ph * w, rcond=None)[0]
    pred = M @ sol
    ph2 = pred + np.angle(np.exp(1j * (ph - pred)))
    sol = np.linalg.lstsq(M * w[:, None], ph2 * w, rcond=None)[0]
    return sol

def crop(img, x0, y0):
    o = (S - L) // 2
    return img[y0 + o:y0 + o + L, x0 + o:x0 + o + L]

print("# 5.2 phase slope on 5.1's squares; signal = the mover's dx across the step (23 -> 24); noise = the spread of dx on quiet pairs")
print(f"{'side':>4s} {'sigma':>5s} {'step px':>7s} | {'read':>8s} {'% of s':>7s} | {'noise':>8s} | {'S/N':>7s} | detected")
for L in sizes:
  setup(L)
  for sg in sigmas:
      rng = np.random.default_rng(20260930)                   # substep.py's seed: the same noise, frame for frame
      for s in steps:
          rng = np.random.default_rng(20260930)
          a0, a1 = frame(0.0), frame(s)
          frames = []
          for k in range(NF):
              img = (a0 if k < STEP_AT else a1) + (rng.normal(0, sg / 255.0, (H, W)) if sg > 0 else 0)
              frames.append(quant(img))
          mov = [shift_est(crop(frames[k], *MOV), crop(frames[k + 1], *MOV))[0] for k in range(NF - 1)]
          ctl = [shift_est(crop(frames[k], *CTL), crop(frames[k + 1], *CTL))[0] for k in range(NF - 1)]
          quiet = [mov[k] for k in range(4, NF - 5) if abs(k - STEP_AT) > 3] + ctl[4:NF - 5]
          noise = float(np.std(quiet)); sig = mov[STEP_AT - 1]
          sn = abs(sig) / noise if noise > 0 else float("inf")
          print(f"{L:4d} {sg:5.0f} {s:7.3f} | {sig:+8.4f} {sig / s * 100:6.1f}% | {noise:8.5f} | {sn:7.1f} | {'YES' if sn > 3 else 'no'}", flush=True)
