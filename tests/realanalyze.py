#!/usr/bin/env python3
"""Summarise real-footage decimate-and-reconstruct results from realbench.sh.

    ./realanalyze.py                    # all labels found
    ./realanalyze.py gen1 gen2 linear   # specific labels, in this order

Reports PSNR and SSIM side by side, deliberately. They can disagree, and when
they do, SSIM is the one to trust for this comparison: PSNR is mean-squared
error, which systematically rewards blur. A linear blend's smooth
double-image has lower squared error than a sharp but slightly-misplaced
motion-compensated frame, so PSNR can rank "do almost nothing" above real
motion compensation. Measured on real footage, PSNR ranked linear blending
above the shader while SSIM and direct visual inspection both ranked it
clearly below.

Also prints the passthrough check. Retained frames must be near-perfect; if
they are not, alignment is broken and no other number here means anything.
"""
import os
import re
import statistics
import sys

OUTROOT = os.environ.get("OUTROOT") or os.path.join(
    os.environ.get("TMPDIR", "/tmp"), "interp-real")


def read(path, pat):
    if not os.path.exists(path):
        return {}
    d = {}
    for line in open(path):
        m = re.match(pat, line)
        if m:
            v = m.group(2)
            d[int(m.group(1))] = float("inf") if v == "inf" else float(v)
    return d


P_PSNR = r"n:(\d+).*?psnr_y:([0-9.]+|inf)"
P_SSIM = r"n:(\d+).*?\sAll:([0-9.]+)"


def stats(d):
    """(synthesised mean, passthrough mean, passthrough exact count, n)"""
    syn = [v for n, v in d.items() if n % 2 == 0 and v != float("inf")]
    thru = [v for n, v in d.items() if n % 2 == 1]
    exact = sum(1 for v in thru if v == float("inf"))
    fin = [v for v in thru if v != float("inf")]
    return (statistics.mean(syn) if syn else None,
            statistics.mean(fin) if fin else float("inf"), exact, len(thru))


if not os.path.isdir(OUTROOT):
    sys.exit(f"no results at {OUTROOT} -- run realbench.sh first")

files = os.listdir(OUTROOT)
segs = sorted({m.group(1) for f in files
               if (m := re.match(r"ref_(\d+)\.mkv", f))}, key=int)
labels = sys.argv[1:] or sorted({m.group(1) for f in files
                                 if (m := re.match(r"psnr_(.+)_\d+\.log", f))})
if not labels or not segs:
    sys.exit("nothing to summarise")

print()
print("=== passthrough check (retained frames -- must be near-perfect) ===")
for lab in labels:
    row = f"  {lab:<10}"
    for s in segs:
        _, tm, ex, n = stats(read(os.path.join(OUTROOT, f"psnr_{lab}_{s}.log"), P_PSNR))
        row += f"  seg{s}: {'inf' if tm == float('inf') else f'{tm:.0f}dB'} ({ex}/{n} exact)"
    print(row)

print()
print("=== synthesised frames only (the measurement) ===")
w = 11
hdr = f"{'':<12}" + "".join(f"{l:>{w}}" for l in labels)
print(hdr)
print("-" * len(hdr))
for metric, pat, fmt in (("PSNR", P_PSNR, "{:>11.2f}"), ("SSIM", P_SSIM, "{:>11.4f}")):
    for s in segs:
        row = f"{metric} {s:<7}"
        for lab in labels:
            v, *_ = stats(read(os.path.join(OUTROOT, f"{metric.lower()}_{lab}_{s}.log"), pat))
            row += fmt.format(v) if v is not None else f"{'-':>{w}}"
        print(row)
    row = f"{metric} MEAN  "
    for lab in labels:
        vals = [stats(read(os.path.join(OUTROOT, f"{metric.lower()}_{lab}_{s}.log"), pat))[0]
                for s in segs]
        vals = [v for v in vals if v is not None]
        row += fmt.format(statistics.mean(vals)) if vals else f"{'-':>{w}}"
    print(row)
    print()
print("If PSNR and SSIM disagree, trust SSIM here -- see this file's docstring.")
