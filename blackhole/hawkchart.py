"""The chart: photon greybody factors and the Hawking photon spectrum against the blackbody it is usually drawn as,
plus the mass ladder printed for the record (2026-09-08). numpy only, drawn by hand; writes <out.ppm>.

    hawkchart.py <out.ppm>
"""
import math
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import hawkcolor as hc

outp = pathlib.Path(sys.argv[1])
d = np.load(pathlib.Path(__file__).resolve().parent / "greybody.npz")
w, Gamma, dEdw, dEdw_geo = d["w"], d["Gamma"], d["dEdw"], d["dEdw_geo"]
P, Ndot, w_pk = float(d["P"]), float(d["Ndot"]), float(d["w_peak"])
T_H = 1 / (8 * math.pi)

W, H = 1600, 1100
img = np.zeros((H, W, 3), np.uint8)
img[:] = 12


class Axes:
    def __init__(self, box, xr, yr, logx=False, logy=False):
        self.x0, self.y0, self.x1, self.y1 = box
        self.xr, self.yr, self.logx, self.logy = xr, yr, logx, logy

    def _tx(self, x):
        a, b = self.xr
        if self.logx:
            x, a, b = np.log(x), math.log(a), math.log(b)
        return self.x0 + (x - a) / (b - a) * (self.x1 - self.x0)

    def _ty(self, y):
        a, b = self.yr
        if self.logy:
            y, a, b = np.log(np.maximum(y, 1e-300)), math.log(a), math.log(b)
        return self.y1 - (y - a) / (b - a) * (self.y1 - self.y0)

    def frame(self):
        img[self.y0:self.y1 + 1, self.x0:self.x0 + 2] = 120
        img[self.y0:self.y1 + 1, self.x1 - 1:self.x1 + 1] = 120
        img[self.y0:self.y0 + 2, self.x0:self.x1 + 1] = 120
        img[self.y1 - 1:self.y1 + 1, self.x0:self.x1 + 1] = 120

    def line(self, xs, ys, color, width=2):
        px, py = self._tx(np.asarray(xs, float)), self._ty(np.asarray(ys, float))
        ok = np.isfinite(px) & np.isfinite(py)
        px, py = px[ok], py[ok]
        for i in range(len(px) - 1):
            n = int(max(2, math.hypot(px[i + 1] - px[i], py[i + 1] - py[i]) * 1.5))
            xx = np.linspace(px[i], px[i + 1], n); yy = np.linspace(py[i], py[i + 1], n)
            for dx in range(width):
                for dy in range(width):
                    xi = (xx + dx - width // 2).astype(int); yi = (yy + dy - width // 2).astype(int)
                    m = (xi >= self.x0) & (xi <= self.x1) & (yi >= self.y0) & (yi <= self.y1)
                    img[yi[m], xi[m]] = color

    def vband(self, xa, xb, color):
        a, b = int(self._tx(xa)), int(self._tx(xb))
        img[self.y0 + 2:self.y1 - 1, a:b] = color

    def xtick(self, x, label):
        px = int(self._tx(x))
        img[self.y1 - 8:self.y1, px:px + 2] = 160
        hc.draw_text(img, px - hc.text_width(label, 2) // 2, self.y1 + 8, label, 2, (190, 190, 190))

    def ytick(self, y, label):
        py = int(self._ty(y))
        img[py:py + 2, self.x0:self.x0 + 8] = 160
        hc.draw_text(img, self.x0 - hc.text_width(label, 2) - 8, py - 7, label, 2, (190, 190, 190))

    def text(self, x, y, s, color=(220, 220, 220), scale=2):
        hc.draw_text(img, int(self._tx(x)), int(self._ty(y)), s, scale, color)


hc.draw_text(img, 40, 24, "Hawking radiation of a Schwarzschild black hole in photons  (computed this session; Page 1976 reproduced)", 2, (240, 240, 240))

# top: greybody factors
ax = Axes((160, 90, 1540, 470), (0.01, 1.5), (1e-8, 1.5), logx=True, logy=True)
ax.frame()
cols = [(255, 170, 60), (90, 200, 255), (150, 255, 150), (255, 120, 200), (200, 200, 120)]
for l in range(1, 6):
    ax.line(w, Gamma[l], cols[l - 1], 3)
    i = int(np.argmin(np.abs(np.log(Gamma[l]) - math.log(1e-3))))
    ax.text(w[i] * 1.12, 1e-3, f"l = {l}", cols[l - 1])
for v in (0.01, 0.03, 0.1, 0.3, 1.0):
    ax.xtick(v, f"{v:g}")
for v in (1e-8, 1e-6, 1e-4, 1e-2, 1.0):
    ax.ytick(v, f"{v:.0e}" if v < 0.5 else "1")
hc.draw_text(img, 170, 100, "greybody factor Gamma_l(w): the fraction of a horizon-born wave that reaches infinity", 2, (220, 220, 220))
hc.draw_text(img, 700, 480 + 30, "frequency w in units of 1/M   (T_H = 1/8 pi M = 0.040/M)", 2, (190, 190, 190))

# bottom: the spectrum
ymax = float(dEdw_geo.max()) * 1.08
ax2 = Axes((160, 600, 1540, 1000), (0.0, 1.2), (0.0, ymax))
ax2.frame()
M_film = hc.mass_for_TH(2000.0)
unit = hc.C ** 3 / (hc.G * M_film)
wa, wb = 2 * math.pi * hc.C / 780e-9 / unit, 2 * math.pi * hc.C / 380e-9 / unit
ax2.vband(wa, wb, (40, 40, 52))
ax2.line(w, dEdw_geo, (110, 110, 110), 3)
ax2.line(w, dEdw, (255, 170, 60), 4)
ipk = int(np.argmax(dEdw))
ax2.line([w_pk, w_pk], [0, dEdw[ipk]], (255, 170, 60), 1)
for v in (0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2):
    ax2.xtick(v, f"{v:g}")
ax2.ytick(0.0, "0"); ax2.ytick(ymax / 1.08, f"{ymax / 1.08:.1e}")
hc.draw_text(img, 170, 610, "power spectrum dE/dt dw, in units of hbar c^6 / G^2 M^2 per unit w M", 2, (220, 220, 220))
hc.draw_text(img, 700, 1010 + 30, "frequency w in units of 1/M", 2, (190, 190, 190))
ax2.text(0.42, ymax * 0.92, "grey: blackbody at T_H over the capture area 27 pi M^2  (P = 1.40e-4)", (170, 170, 170))
ax2.text(0.42, ymax * 0.82, f"orange: with the greybody factors  (P = {P:.3e}; Page 1976: 3.36e-5)", (255, 170, 60))
ax2.text(0.42, ymax * 0.72, f"peak w = {w_pk:.3f}/M = {w_pk / T_H:.1f} T_H (blackbody 2.8 T_H); wavelength {2 * math.pi / w_pk:.1f} M = {math.pi / w_pk:.1f} r_s", (255, 170, 60))
ax2.text(0.42, ymax * 0.62, "98% of the power in l = 1: at its peak the hole is a pure dipole", (255, 170, 60))
ax2.text(wa + 0.005, ymax * 0.30, "visible band (380-780 nm)", (140, 140, 170))
ax2.text(wa + 0.005, ymax * 0.24, "for the film's hole: T_H = 2000 K", (140, 140, 170))
ax2.text(wa + 0.005, ymax * 0.18, "M = 6.1e19 kg, horizon 91 nm", (140, 140, 170))
hc.write_ppm(outp, img)
print(f"wrote {outp}")

# the mass ladder, for the record
print()
print("mass ladder (Schwarzschild, photons only; P from this session's 3.364e-5 hbar c^6 / G^2 M^2; peak wavelength 25.8 GM/c^2):")
print(f"{'M (kg)':>10} {'T_H (K)':>10} {'horizon':>10} {'peak lambda':>12} {'P (W)':>10} {'at 1 m (W/m^2)':>15}  note")
M_sun, M_earth, M_moon = 1.989e30, 5.972e24, 7.35e22
rows = [(1e17, ""), (1e18, ""), (1e19, ""), (hc.mass_for_TH(6000.0), "T_H = 6000 K: the Sun's colour"),
        (hc.mass_for_TH(2000.0), "the film's hole"), (1e21, ""), (1e22, ""), (hc.mass_for_TH(2.725), "T_H = the CMB: heavier holes absorb more than they emit"),
        (M_moon, "the Moon"), (M_earth, "the Earth"), (M_sun, "the Sun"), (4e6 * M_sun, "Sgr A*")]
hk = hc.Hawking()
for M, note in rows:
    T = hc.MK_PER_TH / M
    rs = hc.rs_metres(M)
    lam = 25.8 * hc.G * M / hc.C ** 2
    Pw = hk.power_watts(M)
    def fm(x, u=("m", "mm", "um", "nm", "pm", "fm", "am", "zm")):
        if x >= 1e3:
            return f"{x / 1e3:.3g} km"
        for i, s in enumerate(u):
            if x >= 10 ** (-3 * i) or i == len(u) - 1:
                return f"{x / 10 ** (-3 * i):.3g} {s}"
    print(f"{M:10.2e} {T:10.3g} {fm(rs):>10} {fm(lam):>12} {Pw:10.2e} {Pw / (4 * math.pi):15.2e}  {note}")
