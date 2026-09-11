"""Shared pieces for the Hawking renders (2026-09-08): colour from a spectrum, the Hawking spectrum from greybody.npz,
a 5x7 bitmap font for captions, and a few constants. numpy only.

Radiance bookkeeping (geometric units, M = 1, per unit frequency w per steradian, both polarisations):
    blackbody          B_w(T) = w^3 / (4 pi^3 (exp(w / T) - 1))
    Hawking, at infinity, along a ray from the horizon (the shadow's uniform radiance in ray optics):
                       I_w = [S(w) / (27 w^2)] * B_w(T_H),   S = sum_l (2l + 1) Gamma_l(w),   T_H = 1 / (8 pi)
    seen by a static observer at r (blueshift beta = 1 / sqrt(1 - 2/r), the same in every direction):
                       I_loc(w) = beta^3 I_inf(w / beta)      (I_w / w^3 is invariant along a ray)
A temperature in kelvin converts to geometric units through the hole's mass: T_geo = (T_K / T_H,K) / (8 pi), and a
frequency w (geometric) is a wavelength lambda = 2 pi c / (w c^3 / (G M)). The CIE 1931 colour-matching functions are
the multi-lobe Gaussian fits of Wyman, Sloan & Shirley (2013), then XYZ -> linear sRGB (D65).
"""
import math
import pathlib

import numpy as np

HBAR, C, G, KB = 1.0546e-34, 2.99792458e8, 6.674e-11, 1.3807e-23
T_H_GEO = 1.0 / (8 * math.pi)
MK_PER_TH = HBAR * C ** 3 / (8 * math.pi * G * KB)        # M * T_H in kg K: 1.227e23


def mass_for_TH(T_K):
    return MK_PER_TH / T_K


def rs_metres(M_kg):
    return 2 * G * M_kg / C ** 2


LAM = np.linspace(380e-9, 780e-9, 401)                     # the colour integral's wavelength grid


def _lobe(lam_nm, mu, s1, s2):
    s = np.where(lam_nm < mu, s1, s2)
    return np.exp(-0.5 * ((lam_nm - mu) / s) ** 2)


_ln = LAM * 1e9
XBAR = 1.056 * _lobe(_ln, 599.8, 37.9, 31.0) + 0.362 * _lobe(_ln, 442.0, 16.0, 26.7) - 0.065 * _lobe(_ln, 501.1, 20.4, 26.2)
YBAR = 0.821 * _lobe(_ln, 568.8, 46.9, 40.5) + 0.286 * _lobe(_ln, 530.9, 16.3, 31.1)
ZBAR = 1.217 * _lobe(_ln, 437.0, 11.8, 36.0) + 0.681 * _lobe(_ln, 459.0, 26.0, 13.8)
CMF = np.stack([XBAR, YBAR, ZBAR], -1)                       # [lam, 3]
XYZ2RGB = np.array([[3.2406, -1.5372, -0.4986], [-0.9689, 1.8758, 0.0415], [0.0557, -0.2040, 1.0570]])


def omega_geo_of_lambda(M_kg):
    """the geometric frequency w M of each wavelength on LAM, for a hole of mass M_kg"""
    unit = C ** 3 / (G * M_kg)                              # rad/s per unit geometric frequency
    return 2 * math.pi * C / LAM / unit


def xyz_of_radiance(I_of_w, M_kg):
    """XYZ of a radiance given per unit geometric frequency, I_of_w(w) with w an array, for a hole of mass M_kg"""
    w = omega_geo_of_lambda(M_kg)
    I_w = I_of_w(w)
    I_lam = I_w * w / LAM                                    # I_lam dlam = I_w dw, |dw/dlam| = w / lam
    dl = LAM[1] - LAM[0]
    return (I_lam[:, None] * CMF).sum(0) * dl


def rgb_of_xyz(xyz):
    return np.clip(XYZ2RGB @ xyz, 0, None)


def planck_w(w, T_geo):
    x = np.clip(w / T_geo, 1e-9, 700)
    return w ** 3 / (4 * math.pi ** 3 * np.expm1(x))


def blackbody_rgb(T_K, M_kg):
    """linear sRGB (with its absolute luminance in the common radiance units) of a blackbody at T_K"""
    T_geo = T_K / (MK_PER_TH / M_kg) * T_H_GEO              # T_K / T_H,K * T_H,geo
    return rgb_of_xyz(xyz_of_radiance(lambda w: planck_w(w, T_geo), M_kg))


class Hawking:
    def __init__(self, npz=None):
        npz = pathlib.Path(npz) if npz else pathlib.Path(__file__).resolve().parent / "greybody.npz"
        d = np.load(npz)
        self.w, self.S = d["w"], d["S"]
        self.w_peak = float(d["w_peak"])
        self.P, self.Ndot = float(d["P"]), float(d["Ndot"])
        self.d = d

    def greybody_ratio(self, w):
        """S(w) / (27 w^2): 1 in geometric optics, -> 0 at low frequency"""
        lo, hi = self.w[0], self.w[-1]
        ratio = self.S / (27 * self.w ** 2)
        out = np.interp(np.log(np.clip(w, lo, hi)), np.log(self.w), ratio)
        out = np.where(w < lo, ratio[0] * (w / lo) ** 2, out)      # Gamma_1 ~ w^4 below the grid: ratio ~ w^2
        out = np.where(w > hi, 1.0, out)
        return out

    def radiance_inf(self, w):
        return self.greybody_ratio(w) * planck_w(w, T_H_GEO)

    def rgb(self, M_kg, beta=1.0):
        """linear sRGB of the glow seen by a static observer with blueshift beta"""
        return rgb_of_xyz(xyz_of_radiance(lambda w: beta ** 3 * self.radiance_inf(w / beta), M_kg))

    def power_watts(self, M_kg):
        return self.P * HBAR * C ** 6 / (G ** 2 * M_kg ** 2)


def tonemap(rgb_lin):
    """luminance-preserving Reinhard, then the display gamma; rgb_lin [..., 3] linear, exposure already applied"""
    L = 0.2126 * rgb_lin[..., 0] + 0.7152 * rgb_lin[..., 1] + 0.0722 * rgb_lin[..., 2]
    Lt = L / (1.0 + L)
    scale = np.where(L > 1e-12, Lt / np.maximum(L, 1e-12), 0.0)
    out = np.clip(rgb_lin * scale[..., None], 0, 1)
    over = np.clip(L - 4.0, 0, None) / 8.0                      # the very bright bleach toward white, as eyes do
    out = out + (1.0 - out) * np.clip(over, 0, 1)[..., None]
    return np.clip(out, 0, 1) ** (1 / 2.2)


# ---- a 5x7 font ---------------------------------------------------------------------------------------------------
_F = {}
_F["A"] = ".###. #...# #...# ##### #...# #...# #...#"
_F["B"] = "####. #...# #...# ####. #...# #...# ####."
_F["C"] = ".###. #...# #.... #.... #.... #...# .###."
_F["D"] = "####. #...# #...# #...# #...# #...# ####."
_F["E"] = "##### #.... #.... ####. #.... #.... #####"
_F["F"] = "##### #.... #.... ####. #.... #.... #...."
_F["G"] = ".###. #...# #.... #.### #...# #...# .###."
_F["H"] = "#...# #...# #...# ##### #...# #...# #...#"
_F["I"] = ".###. ..#.. ..#.. ..#.. ..#.. ..#.. .###."
_F["J"] = "..### ...#. ...#. ...#. ...#. #..#. .##.."
_F["K"] = "#...# #..#. #.#.. ##... #.#.. #..#. #...#"
_F["L"] = "#.... #.... #.... #.... #.... #.... #####"
_F["M"] = "#...# ##.## #.#.# #.#.# #...# #...# #...#"
_F["N"] = "#...# ##..# #.#.# #..## #...# #...# #...#"
_F["O"] = ".###. #...# #...# #...# #...# #...# .###."
_F["P"] = "####. #...# #...# ####. #.... #.... #...."
_F["Q"] = ".###. #...# #...# #...# #.#.# #..#. .##.#"
_F["R"] = "####. #...# #...# ####. #.#.. #..#. #...#"
_F["S"] = ".#### #.... #.... .###. ....# ....# ####."
_F["T"] = "##### ..#.. ..#.. ..#.. ..#.. ..#.. ..#.."
_F["U"] = "#...# #...# #...# #...# #...# #...# .###."
_F["V"] = "#...# #...# #...# #...# #...# .#.#. ..#.."
_F["W"] = "#...# #...# #...# #.#.# #.#.# ##.## #...#"
_F["X"] = "#...# #...# .#.#. ..#.. .#.#. #...# #...#"
_F["Y"] = "#...# #...# .#.#. ..#.. ..#.. ..#.. ..#.."
_F["Z"] = "##### ....# ...#. ..#.. .#... #.... #####"
_F["a"] = "..... ..... .###. ....# .#### #...# .####"
_F["b"] = "#.... #.... ####. #...# #...# #...# ####."
_F["c"] = "..... ..... .###. #.... #.... #...# .###."
_F["d"] = "....# ....# .#### #...# #...# #...# .####"
_F["e"] = "..... ..... .###. #...# ##### #.... .###."
_F["f"] = "..##. .#..# .#... ###.. .#... .#... .#..."
_F["g"] = "..... .#### #...# #...# .#### ....# .###."
_F["h"] = "#.... #.... ####. #...# #...# #...# #...#"
_F["i"] = "..#.. ..... .##.. ..#.. ..#.. ..#.. .###."
_F["j"] = "...#. ..... ..##. ...#. ...#. #..#. .##.."
_F["k"] = "#.... #.... #..#. #.#.. ##... #.#.. #..#."
_F["l"] = ".##.. ..#.. ..#.. ..#.. ..#.. ..#.. .###."
_F["m"] = "..... ..... ##.#. #.#.# #.#.# #.#.# #...#"
_F["n"] = "..... ..... ####. #...# #...# #...# #...#"
_F["o"] = "..... ..... .###. #...# #...# #...# .###."
_F["p"] = "..... ####. #...# #...# ####. #.... #...."
_F["q"] = "..... .#### #...# #...# .#### ....# ....#"
_F["r"] = "..... ..... #.##. ##..# #.... #.... #...."
_F["s"] = "..... ..... .#### #.... .###. ....# ####."
_F["t"] = ".#... .#... ###.. .#... .#... .#..# ..##."
_F["u"] = "..... ..... #...# #...# #...# #..## .##.#"
_F["v"] = "..... ..... #...# #...# #...# .#.#. ..#.."
_F["w"] = "..... ..... #...# #...# #.#.# #.#.# .#.#."
_F["x"] = "..... ..... #...# .#.#. ..#.. .#.#. #...#"
_F["y"] = "..... #...# #...# #...# .#### ....# .###."
_F["z"] = "..... ..... ##### ...#. ..#.. .#... #####"
_F["0"] = ".###. #...# #..## #.#.# ##..# #...# .###."
_F["1"] = "..#.. .##.. ..#.. ..#.. ..#.. ..#.. .###."
_F["2"] = ".###. #...# ....# ...#. ..#.. .#... #####"
_F["3"] = "##### ...#. ..#.. ...#. ....# #...# .###."
_F["4"] = "...#. ..##. .#.#. #..#. ##### ...#. ...#."
_F["5"] = "##### #.... ####. ....# ....# #...# .###."
_F["6"] = "..##. .#... #.... ####. #...# #...# .###."
_F["7"] = "##### ....# ...#. ..#.. .#... .#... .#..."
_F["8"] = ".###. #...# #...# .###. #...# #...# .###."
_F["9"] = ".###. #...# #...# .#### ....# ...#. .##.."
_F[" "] = "..... ..... ..... ..... ..... ..... ....."
_F["."] = "..... ..... ..... ..... ..... .##.. .##.."
_F[","] = "..... ..... ..... ..... .##.. ..#.. .#..."
_F["="] = "..... ..... ##### ..... ##### ..... ....."
_F["-"] = "..... ..... ..... ##### ..... ..... ....."
_F["+"] = "..... ..#.. ..#.. ##### ..#.. ..#.. ....."
_F["/"] = "....# ....# ...#. ..#.. .#... #.... #...."
_F["("] = "..#.. .#... #.... #.... #.... .#... ..#.."
_F[")"] = "..#.. ...#. ....# ....# ....# ...#. ..#.."
_F[":"] = "..... .##.. .##.. ..... .##.. .##.. ....."
_F["^"] = "..#.. .#.#. #...# ..... ..... ..... ....."
_F["_"] = "..... ..... ..... ..... ..... ..... #####"
_F["%"] = "##... ##..# ...#. ..#.. .#... #..## ...##"
_F["|"] = "..#.. ..#.. ..#.. ..#.. ..#.. ..#.. ..#.."
_F["~"] = "..... ..... .#... #.#.# ...#. ..... ....."
_F["'"] = "..#.. ..#.. ..... ..... ..... ..... ....."
_F["<"] = "...#. ..#.. .#... #.... .#... ..#.. ...#."
_F[">"] = ".#... ..#.. ...#. ....# ...#. ..#.. .#..."
_F["*"] = "..... #.#.# .###. ##### .###. #.#.# ....."
_F["["] = ".###. .#... .#... .#... .#... .#... .###."
_F["]"] = ".###. ...#. ...#. ...#. ...#. ...#. .###."
GLYPH = {}
for ch, rows in _F.items():
    r = rows.split(" ")
    assert len(r) == 7 and all(len(x) == 5 for x in r), ch
    GLYPH[ch] = np.array([[c == "#" for c in row] for row in r])


def text_width(text, scale=2):
    return len(text) * 6 * scale


def draw_text(img, x, y, text, scale=2, color=(220, 220, 220)):
    """draw text into img (H, W, 3) uint8 at top-left (x, y); returns the x after the text"""
    H, W = img.shape[:2]
    col = np.array(color, np.uint8)
    for ch in text:
        g = GLYPH.get(ch, GLYPH["?"] if "?" in GLYPH else GLYPH[" "])
        big = np.kron(g, np.ones((scale, scale), bool))
        h, w = big.shape
        y0, x0 = y, x
        y1, x1 = min(H, y0 + h), min(W, x0 + w)
        if y1 > y0 and x1 > x0 and y0 >= 0 and x0 >= 0:
            sub = img[y0:y1, x0:x1]
            m = big[: y1 - y0, : x1 - x0]
            sub[m] = col
        x += 6 * scale
    return x


def write_ppm(path, img):
    path = pathlib.Path(path)
    with open(path, "wb") as f:
        f.write(f"P6 {img.shape[1]} {img.shape[0]} 255".encode() + bytes([10]))
        f.write(np.ascontiguousarray(img, dtype=np.uint8).tobytes())
