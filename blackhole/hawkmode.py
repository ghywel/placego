"""The Hawking mode itself, at the wavelength it is actually emitted at (2026-09-08).

    hawkmode.py <outdir> [frames] [panel width] [panel height] [pixels per M]

Ray optics cannot picture Hawking radiation at its peak: the photon spectrum peaks at w M = 0.243 (greybody.npz), a
wavelength of 25.8 M = 12.9 horizon radii, so the emitter is far smaller than its own light and only the l = 1 partial
wave gets out (98 % of the power). What CAN be drawn exactly is the mode function: the electromagnetic "up" mode of
the Regge-Wheeler equation at that frequency, born at the horizon with unit outgoing amplitude, partly transmitted
through the potential barrier that peaks at r = 3M (Gamma_1 = 0.415), partly reflected back in. Left panel l = m = 1,
right panel l = m = 2 (Gamma_2 = 0.0004: trapped), both in the equatorial plane, the field Re[psi(r*) exp(i (m phi -
w t))] as a signed colour (warm positive, cool negative), the flux-normalised amplitude psi rather than the 1/r field
so the outgoing wave keeps its brightness. Near the horizon the wave's crests pile up (r* -> -infinity: the same
outgoing wave, infinitely compressed in r, the trans-Planckian side of Hawking's derivation) and peel off it at the
coordinate speed 1 - 2M/r. The horizon is the black disc, the barrier's peak the dashed ring. Output rgb24 frames.
"""
import math
import pathlib
import sys
import time

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import hawkcolor as hc

out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
NF = int(sys.argv[2]) if len(sys.argv) > 2 else 240
PW = int(sys.argv[3]) if len(sys.argv) > 3 else 960
PH = int(sys.argv[4]) if len(sys.argv) > 4 else 1080
PPM = float(sys.argv[5]) if len(sys.argv) > 5 else 16.0
PERIODS = 3.0

t0 = time.time()
d = np.load(pathlib.Path(__file__).resolve().parent / "greybody.npz")
w = float(d["w_peak"])
modes = {1: (d["rs1"], d["psi1"], float(d["gamma1"])), 2: (d["rs2"], d["psi2"], float(d["gamma2"]))}
lam = 2 * math.pi / w
print(f"w = {w:.4f} / M, wavelength {lam:.1f} M = {lam / 2:.1f} r_s; Gamma_1 = {modes[1][2]:.4f}, Gamma_2 = {modes[2][2]:.5f}")

xs = (np.arange(PW) + 0.5 - PW / 2) / PPM
ys = -(np.arange(PH) + 0.5 - PH / 2) / PPM
X, Y = np.meshgrid(xs, ys)
R = np.hypot(X, Y)
PHI = np.arctan2(Y, X)
outside = R > 2.0
xh = np.maximum(R - 2.0, 1e-12)
RS = 2.0 + xh + 2.0 * np.log(xh / 2.0)
fields = {}
for l, (rs, psi, g) in modes.items():
    A = np.interp(RS, rs, psi.real)
    B = np.interp(RS, rs, psi.imag)
    A[~outside] = 0; B[~outside] = 0
    fields[l] = (A, B)
vmax = max(np.sqrt(A * A + B * B).max() for A, B in fields.values())
print(f"amplitude range: max |psi| = {vmax:.3f}; l = 1 outside the barrier |psi| = {np.sqrt(fields[1][0] ** 2 + fields[1][1] ** 2)[(R > 6) & (R < 8)].mean():.3f}, l = 2 there {np.sqrt(fields[2][0] ** 2 + fields[2][1] ** 2)[(R > 6) & (R < 8)].mean():.4f}")

WARM = np.array([1.0, 0.62, 0.22])
COOL = np.array([0.25, 0.55, 1.0])
horizon_ring = np.abs(R - 2.0) < 0.75 / PPM
barrier = (np.abs(R - 3.0) < 0.6 / PPM) & ((np.floor(PHI / (math.pi / 18)).astype(int) % 2) == 0)
period = 2 * math.pi / w
fh = open(out / "frames.rgb", "wb")
for n in range(NF):
    t = n / NF * PERIODS * period
    frame = np.zeros((PH, 2 * PW, 3), np.uint8)
    for k, l in enumerate((1, 2)):
        A, B = fields[l]
        ph = l * PHI - w * t
        v = (A * np.cos(ph) - B * np.sin(ph)) / vmax
        a = np.abs(v) ** 0.75
        rgb = np.where((v > 0)[..., None], WARM, COOL) * a[..., None]
        rgb[~outside] = 0
        rgb[horizon_ring] = 0.85
        rgb[barrier] = np.maximum(rgb[barrier], 0.45)
        img = (np.clip(rgb, 0, 1) ** (1 / 2.2) * 255 + 0.5).astype(np.uint8)
        frame[:, k * PW:(k + 1) * PW] = img
    frame[:, PW - 1:PW + 1] = 40
    # the wavelength bar and captions
    x0, y0 = 24, 110
    frame[y0 - 1:y0 + 2, x0:x0 + int(lam * PPM)] = 220
    frame[y0 - 8:y0 + 9, x0:x0 + 2] = 220; frame[y0 - 8:y0 + 9, x0 + int(lam * PPM) - 2:x0 + int(lam * PPM)] = 220
    hc.draw_text(frame, x0, y0 - 34, f"one wavelength: {lam:.1f} M = {lam / 2:.1f} horizon radii", 2, (220, 220, 220))
    hc.draw_text(frame, 24, 14, "the Hawking photon mode at its spectrum's peak, w = 0.243 / M", 2, (200, 200, 200))
    hc.draw_text(frame, 24, 40, "flux-normalised amplitude psi, equatorial plane, time e^(-i w t)", 2, (150, 150, 150))
    hc.draw_text(frame, PW + 24, 14, "the next multipole at the same frequency", 2, (200, 200, 200))
    hc.draw_text(frame, 24, PH - 60, f"l = 1, m = 1    Gamma = {modes[1][2]:.3f}: the dipole gets out (98% of the power)", 2, (230, 230, 230))
    hc.draw_text(frame, 24, PH - 32, "black disc: horizon r = 2 M    dashed: barrier peak r = 3 M", 2, (150, 150, 150))
    hc.draw_text(frame, PW + 24, PH - 60, f"l = 2, m = 2    Gamma = {modes[2][2]:.4f}: the quadrupole is trapped", 2, (230, 230, 230))
    hc.draw_text(frame, PW + 24, PH - 32, "a near-standing wave inside the barrier; a few percent leak out", 2, (150, 150, 150))
    fh.write(frame.tobytes())
    if n == NF // 2:
        hc.write_ppm(out / "still_mid.ppm", frame)
    if n % 60 == 0:
        print(f"  frame {n} ({time.time() - t0:.0f} s)", flush=True)
fh.close()
print(f"{NF} frames of {2 * PW}x{PH} -> {out / 'frames.rgb'} ({time.time() - t0:.0f} s)")
