#!/usr/bin/env python3
"""The volume of the unit ball in n dimensions, drawn in numpy with the Hawking caption font (2026-09-10).

    V_n = pi^(n/2) / Gamma(n/2 + 1)          S_(n-1) = n V_n  (the surface measure of the unit (n-1)-sphere)

Every value is exact and knowable; none is visualisable past n = 3. The curve rises to a peak at n = 5 and
then falls to zero: a unit ball in a thousand dimensions has a volume of about 10^-886, and almost all of
what volume it has lies within a hair of its surface. These are facts about the very objects the owner says
cannot be seen, and they were known before anyone could draw a 4-cube.
"""
import math
import os
import pathlib
import subprocess
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))   # hawkcolor.py is beside this file
from hawkcolor import draw_text, text_width

FF = os.environ.get("FFMPEG", "ffmpeg")
W, H = 1280, 720


def V(n):
    return math.pi ** (n / 2) / math.gamma(n / 2 + 1)


ns = list(range(0, 26))
vols = [V(n) for n in ns]
surf = [n * V(n) for n in ns]

img = np.full((H, W, 3), 18, np.uint8)
L, R, T, B = 90, W - 40, 60, H - 90                  # plot box
ymax = 36.0


def px(n, y):
    return int(L + (R - L) * n / 25), int(B - (B - T) * y / ymax)


# axes and grid
for y in range(0, 37, 5):
    x0, yy = px(0, y); x1, _ = px(25, y)
    img[yy, x0:x1] = (45, 45, 45)
    draw_text(img, 20, yy - 7, f"{y:2d}", scale=2, color=(130, 130, 130))
for n in ns:
    x, y0 = px(n, 0)
    img[y0:y0 + 6, x] = (90, 90, 90)
    if n % 5 == 0:
        draw_text(img, x - 6, B + 12, f"{n}", scale=2, color=(130, 130, 130))
draw_text(img, (L + R) // 2 - text_width("dimension n", 2) // 2, B + 30, "dimension n", scale=2,
          color=(170, 170, 170))


def curve(vals, color, radius=4):
    pts = [px(n, min(v, ymax)) for n, v in zip(ns, vals)]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        steps = max(abs(x1 - x0), abs(y1 - y0), 1)
        for k in range(steps + 1):
            x = int(x0 + (x1 - x0) * k / steps); y = int(y0 + (y1 - y0) * k / steps)
            img[y - 1:y + 2, x - 1:x + 2] = color
    for (x, y) in pts:
        yy, xx = np.ogrid[-radius:radius + 1, -radius:radius + 1]
        m = yy ** 2 + xx ** 2 <= radius ** 2
        img[y - radius:y + radius + 1, x - radius:x + radius + 1][m] = color


curve(surf, (120, 150, 235))
curve(vols, (245, 180, 60))

# labels at the peaks
nv = max(ns, key=V); x, y = px(nv, V(nv))
draw_text(img, x + 12, y - 54, f"unit ball volume peaks at n = {nv}: {V(nv):.3f}", scale=2, color=(245, 180, 60))
draw_text(img, x + 12, y - 32, "then falls to zero for ever", scale=2, color=(245, 180, 60))
nsf = max(ns, key=lambda n: n * V(n)); x, y = px(nsf, nsf * V(nsf))
draw_text(img, x + 12, y - 8, f"unit sphere surface peaks at n = {nsf}: {nsf * V(nsf):.2f}", scale=2, color=(120, 150, 235))

# the familiar rungs, named, in the empty right half
for i, ln in enumerate(("the rungs you can picture:",
                        "  n=1  segment  2         circle   2 pi",
                        "  n=2  disc     pi        sphere   4 pi",
                        "  n=3  ball     4 pi/3    3-sphere 2 pi^2",
                        "  n=4  4-ball   pi^2/2",
                        "  the 3-sphere is the one you would live on")):
    draw_text(img, 640, 240 + 24 * i, ln, scale=2, color=(200, 200, 200))

draw_text(img, L, 18, "V_n = pi^(n/2)/Gamma(n/2+1)    orange: unit n-ball volume    blue: unit (n-1)-sphere surface",
          scale=2, color=(215, 215, 215))
draw_text(img, L, H - 40, "every number here is exact, and none past n = 3 can be pictured", scale=2, color=(150, 150, 150))
draw_text(img, L, H - 20, "a unit ball in 1000 dimensions has volume about 10^-886", scale=2, color=(150, 150, 150))

subprocess.run([FF, "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-i", "-",
                "-frames:v", "1", "-update", "1", sys.argv[1]], input=img.tobytes(), check=True)
print("peak volume n =", nv, f"{V(nv):.4f}", "| peak surface n =", nsf, f"{nsf*V(nsf):.3f}",
      "| V_1000 = 10^%.0f" % (1000 / 2 * math.log10(math.pi) - math.lgamma(501) / math.log(10)))
