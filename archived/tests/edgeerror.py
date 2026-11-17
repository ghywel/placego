#!/usr/bin/env python3
"""Report interpolation error AT EDGES separately from everywhere else.

    ./edgeerror.sh <segment>     # wrapper that extracts frames, then runs this

WHY THIS EXISTS. Whole-frame PSNR/SSIM systematically understate the defect
that viewers actually complain about, and for flat-shaded animation they can
be actively misleading. A cartoon frame is mostly large flat areas -- where a
wrong motion vector still samples the same colour, so the error self-conceals
-- plus a small number of extremely high-contrast outline pixels, where it
does not. Averaging over all pixels lets outline damage barely move the
number while dominating perception.

Measured on real cartoon footage: edges are ~15% of pixels but carry ~5x the
per-pixel error rate, i.e. roughly half of all error. A change that improves
whole-frame PSNR by a healthy margin can improve edge error by almost
nothing, which is exactly the case that looks good in a table and unchanged
on screen.

Reads raw 8-bit grey planes (no numpy in the target environment).
"""
import os
import sys

W = int(os.environ.get("W", 1280))
H = int(os.environ.get("H", 720))
THRESH = int(os.environ.get("EDGE_THRESH", 60))
N = W * H


def frames(path):
    with open(path, "rb") as f:
        while True:
            b = f.read(N)
            if len(b) < N:
                return
            yield b


def main(tmp, variants):
    ref_p = os.path.join(tmp, "ref.raw")
    edge_p = os.path.join(tmp, "edge.raw")
    if not (os.path.exists(ref_p) and os.path.exists(edge_p)):
        sys.exit(f"missing ref.raw/edge.raw in {tmp}")
    ref = list(frames(ref_p))
    edge = list(frames(edge_p))
    nf = min(len(ref), len(edge))
    if nf == 0:
        sys.exit("no frames")

    masks, cov = [], 0
    for k in range(nf):
        e = edge[k]
        m = bytearray(N)
        c = 0
        for i in range(N):
            if e[i] > THRESH:
                m[i] = 1
                c += 1
        masks.append(m)
        cov += c
    print(f"frames: {nf}   edge-mask coverage: {cov/(nf*N)*100:.1f}% of pixels "
          f"(sobel > {THRESH} on the reference)")
    print()
    print(f"{'variant':<12}{'err AT edges':>14}{'err ELSEWHERE':>15}{'ratio':>9}")
    print("-" * 50)
    for name in variants:
        p = os.path.join(tmp, f"{name}.raw")
        if not os.path.exists(p):
            continue
        out = list(frames(p))
        if len(out) < nf:
            continue
        se = so = ce = co = 0
        for k in range(nf):
            a, b, m = out[k], ref[k], masks[k]
            for i in range(N):
                d = a[i] - b[i]
                if d < 0:
                    d = -d
                if m[i]:
                    se += d
                    ce += 1
                else:
                    so += d
                    co += 1
        ae = se / ce if ce else 0.0
        ao = so / co if co else 0.0
        print(f"{name:<12}{ae:>14.2f}{ao:>15.2f}{ae/max(ao,1e-9):>8.1f}x")
    print()
    print("Mean |luma error| per pixel, 0-255, over synthesised frames only.")
    print("Both columns are per-pixel rates, so directly comparable.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("usage: edgeerror.py <tmpdir> <variant> [variant...]")
    main(sys.argv[1], sys.argv[2:])
