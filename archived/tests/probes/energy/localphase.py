"""ENERGY-TRANSFER.md 5.2c: a LOCAL phase estimator (motion magnification's idea) on 5.1's steps, by region size.

    localphase.py [steps=0.05,0.1,0.2,0.3,0.5,1.0] [sigmas=1,2,4] [sizes=268,128,64,32]

CPU only (numpy). The frames are phasestep.py's exactly (the same squares, texture, step at frame 24, seeded noise,
8-bit Y). For each consecutive pair: horizontal complex Gabor responses G = I * exp(i 2 pi x / lam) g_sigma(x, y),
lam in {12, 24, 48} px, sigma = lam / 2 (separable, by FFT convolution over the frame). The per-pixel phase difference
dphi = arg(G1 conj(G0)) gives a horizontal shift -dphi lam / (2 pi); the shifts are pooled over the region, weighted
by |G0||G1|, across all three scales. Scored as phasestep.py scores (noise = the spread over quiet pairs, signal =
the mover across the step), against the field's S/N from 5.2b.

Pre-registered in ENERGY-TRANSFER.md 5.2c (before it ran): L1 at 32 x 32 px a 0.3 px step at sigma 2 reads at S/N above
the field's 4.7.
"""
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[2]))
import masters                                                                   # noqa: E402

steps = [float(v) for v in (sys.argv[1] if len(sys.argv) > 1 else "0.05,0.1,0.2,0.3,0.5,1.0").split(",")]
sigmas = [float(v) for v in (sys.argv[2] if len(sys.argv) > 2 else "1,2,4").split(",")]
sizes = [int(v) for v in (sys.argv[3] if len(sys.argv) > 3 else "268,128,64,32").split(",")]
W, H, S, NF, STEP_AT = 1280, 720, 300, 48, 24
MOV = (200, 210); CTL = (780, 210)
LAMS = (12.0, 24.0, 48.0)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)


def frame(shift):
    """5.1's squares, but with ANTI-ALIASED side edges: each pixel column is weighted by the fraction of it the square
    covers, so the edge moves by exactly the step, as under a real lens. 5.1's hard edges move a whole column for any
    fractional step. The field (an eroded interior) and the phase slope (a Hann window) never saw that, but the Gabor
    filters reach 3 sigma = 72 px, past the 16 px margin, and a noiseless 0.05 px step read 0.197 until this."""
    img = np.zeros((H, W))
    for (x0, y0), dx in ((MOV, shift), (CTL, 0.0)):
        cov = np.clip(np.minimum(xx + 1, x0 + dx + S) - np.maximum(xx, x0 + dx), 0, 1) * ((yy >= y0) & (yy < y0 + S))
        img = img * (1 - cov) + cov * masters.clamp01(masters.tex(xx - x0 - dx, yy - y0))
    return img


def quant(v): return (np.round(16 + 219 * np.clip(v, 0, 1)) - 16) / 219


# the Gabor kernels' transfer functions, once (FFT convolution over the whole frame)
fyv = np.fft.fftfreq(H)[:, None]; fxv = np.fft.fftfreq(W)[None, :]
KER = []
for lam in LAMS:
    sg = lam / 2.0; f0 = 1.0 / lam
    # a Gaussian envelope times a complex carrier -> in frequency, a Gaussian centred at (f0, 0), one-sided
    KER.append((lam, np.exp(-2 * (np.pi * sg) ** 2 * ((fxv - f0) ** 2 + fyv ** 2))))


def responses(img):
    F = np.fft.fft2(img - img.mean())
    return [(lam, np.fft.ifft2(F * K)) for lam, K in KER]


def shift_region(r0, r1, sl):
    """Fleet and Jepson: the shift is the phase difference over the LOCAL phase gradient, not the filter's nominal
    frequency (a first version used 2 pi / lam and read a noiseless 0.3 px step at 68 percent: the texture's local
    frequency is not the filter's centre)"""
    num = den = 0.0
    for (lam, g0), (_, g1) in zip(r0, r1):
        a, b = g0[sl], g1[sl]
        c = b * np.conj(a)
        phx = np.angle(a[:, 1:] * np.conj(a[:, :-1]))          # the local phase gradient along x, rad/px
        c = c[:, :-1]; wgt = (np.abs(a) * np.abs(b))[:, :-1]
        ok = phx > 0.25 * (2 * np.pi / lam)                     # a sensible local frequency (no phase singularity)
        dx = -np.angle(c[ok]) / phx[ok]
        num += float((wgt[ok] * dx).sum()); den += float(wgt[ok].sum())
    return num / den if den > 0 else 0.0


print("# 5.2c local phase (Gabor, lam 12/24/48 px) on 5.1's squares; S/N as 5.2b")
print(f"{'side':>4s} {'sigma':>5s} {'step px':>7s} | {'read':>8s} {'% of s':>7s} | {'noise':>8s} | {'S/N':>7s} | detected")
for L in sizes:
    o = (S - L) // 2
    slm = (slice(MOV[1] + o, MOV[1] + o + L), slice(MOV[0] + o, MOV[0] + o + L))
    slc = (slice(CTL[1] + o, CTL[1] + o + L), slice(CTL[0] + o, CTL[0] + o + L))
    for sg in sigmas:
        for s in steps:
            rng = np.random.default_rng(20260930)
            a0, a1 = frame(0.0), frame(s)
            resp = []
            for k in range(NF):
                img = quant((a0 if k < STEP_AT else a1) + rng.normal(0, sg / 255.0, (H, W)))
                resp.append(responses(img))
            mov = [shift_region(resp[k], resp[k + 1], slm) for k in range(NF - 1)]
            ctl = [shift_region(resp[k], resp[k + 1], slc) for k in range(NF - 1)]
            quiet = [mov[k] for k in range(4, NF - 5) if abs(k - STEP_AT) > 3] + ctl[4:NF - 5]
            noise = float(np.std(quiet)); sig = mov[STEP_AT - 1]
            sn = abs(sig) / noise if noise > 0 else float("inf")
            print(f"{L:4d} {sg:5.0f} {s:7.3f} | {sig:+8.4f} {sig / s * 100:6.1f}% | {noise:8.5f} | {sn:7.1f} | {'YES' if sn > 3 else 'no'}",
                  flush=True)
