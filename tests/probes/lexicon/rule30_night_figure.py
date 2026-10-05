#!/usr/bin/env python3
"""rule30_night_figure.py: one picture of the night of 2026-10-05 (RULE30-PRIZE.md sections 8.14 to 8.20).

RUN-ON:     cpu (pure Python 3, standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_night_figure.py
COST:       instant. Writes rule30_night.svg next to this script.

It draws numbers already recorded in the OUTCOME blocks of other probes, copied here with their sources:
  A. The adversary: R(m, s), the longest zero run a width-m layer fed any input can hold the left half to from depth
     s (rule30_ladder.py, rule30_ladder_deep.py), and the real right halves up to 12 cells (their DL5 / LD3 lines).
  B. The channel bound: bits per visible bit that column 1 can carry next to 0101..., for layer width m = 1 .. 26
     (rule30_entropy.py, its first run and both extensions).
  C. The bottleneck: the longest real zero run from depths 41 and 105 against the right half's width
     (rule30_realruns.py).
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
S = [17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97, 105]
A = {
    "m = 0 (column 1 free)": {17: 15, 25: 19, 33: 33, 41: 37},
    "m = 1": {17: 9, 25: 12, 33: 13, 41: 15, 49: 21, 57: 25},
    "m = 6": {17: 9, 25: 10, 33: 9, 41: 11, 49: 11, 57: 14, 65: 17, 73: 20, 81: 20, 89: 21, 97: 25, 105: 22},
    "m = 12": {41: 8, 49: 11, 57: 10, 65: 13, 73: 16, 81: 14, 89: 16, 97: 16, 105: 20},
    "real right halves": {17: 9, 25: 10, 33: 6, 41: 6, 49: 9, 57: 10, 65: 10, 73: 8, 81: 8, 89: 9, 97: 9, 105: 10},
}
B = [0.6942, 0.6942, 0.6942, 0.6174, 0.5090, 0.4415, 0.3773, 0.3562, 0.3223, 0.3161, 0.2852, 0.2578, 0.2546, 0.2442,
     0.2298, 0.2116, 0.1953, 0.1846, 0.1675, 0.1519, 0.1416, 0.1372, 0.1356, 0.1327, 0.1308, 0.1277]
C = {41: {16: 8, 18: 8, 20: 8, 22: 8, 24: 8, 26: 8, 28: 8}, 105: {16: 10, 18: 11, 20: 11, 22: 11, 24: 11, 26: 12, 28: 12}}
COL = ["#d1495b", "#edae49", "#00798c", "#30638e", "#222222"]


def panel(x0, y0, w, h, xs, ys, title, xlabel, ylabel, series, xticks, yticks):
    out = [f'<g transform="translate({x0},{y0})">',
           f'<text x="{w / 2}" y="-12" text-anchor="middle" font-size="14" font-weight="bold">{title}</text>',
           f'<line x1="0" y1="{h}" x2="{w}" y2="{h}" stroke="#555"/><line x1="0" y1="0" x2="0" y2="{h}" stroke="#555"/>',
           f'<text x="{w / 2}" y="{h + 34}" text-anchor="middle" font-size="12">{xlabel}</text>',
           f'<text x="-40" y="{h / 2}" text-anchor="middle" font-size="12" transform="rotate(-90 -40 {h / 2})">{ylabel}</text>']
    X = lambda v: (v - xs[0]) / (xs[1] - xs[0]) * w
    Y = lambda v: h - (v - ys[0]) / (ys[1] - ys[0]) * h
    for t in xticks:
        out.append(f'<line x1="{X(t):.1f}" y1="{h}" x2="{X(t):.1f}" y2="{h + 4}" stroke="#555"/>'
                   f'<text x="{X(t):.1f}" y="{h + 17}" text-anchor="middle" font-size="11">{t}</text>')
    for t in yticks:
        out.append(f'<line x1="-4" y1="{Y(t):.1f}" x2="0" y2="{Y(t):.1f}" stroke="#555"/>'
                   f'<text x="-8" y="{Y(t) + 4:.1f}" text-anchor="end" font-size="11">{t}</text>'
                   f'<line x1="0" y1="{Y(t):.1f}" x2="{w}" y2="{Y(t):.1f}" stroke="#eee"/>')
    ly = 8
    for k, (name, pts) in enumerate(series):
        c = COL[k % len(COL)]
        path = " ".join(f"{X(a):.1f},{Y(b):.1f}" for a, b in pts)
        out.append(f'<polyline points="{path}" fill="none" stroke="{c}" stroke-width="2"/>')
        out += [f'<circle cx="{X(a):.1f}" cy="{Y(b):.1f}" r="3" fill="{c}"/>' for a, b in pts]
        out.append(f'<text x="{w - 6}" y="{ly + 12 * k}" text-anchor="end" font-size="11" fill="{c}">{name}</text>')
    out.append("</g>")
    return out


def main():
    W, H = 1080, 380
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           'font-family="Helvetica, Arial, sans-serif">', f'<rect width="{W}" height="{H}" fill="white"/>']
    svg += panel(70, 50, 260, 260, (15, 107), (0, 40), "A. The adversary's runs grow",
                 "start depth s", "longest zero run R(m, s)",
                 [(n, sorted(d.items())) for n, d in A.items()], [17, 41, 73, 105], [0, 10, 20, 30, 40])
    svg += panel(430, 50, 260, 260, (1, 26), (0, 0.75), "B. Column 1's channel, exact bound",
                 "layer width m", "bits per visible bit (random = 1)",
                 [("next to 0101...", list(zip(range(1, 27), B)))], [1, 6, 11, 16, 21, 26], [0, 0.25, 0.5, 0.75])
    svg += panel(790, 50, 260, 260, (16, 28), (0, 16), "C. A wider seed buys almost nothing",
                 "right half's width (cells)", "longest real zero run",
                 [(f"from depth {s}", sorted(d.items())) for s, d in C.items()], [16, 20, 24, 28], [0, 4, 8, 12, 16])
    svg.append("</svg>")
    (HERE / "rule30_night.svg").write_text("\n".join(svg) + "\n")
    print("wrote rule30_night.svg")


if __name__ == "__main__":
    main()
