#!/usr/bin/env python3
"""Summarise ground-truth PSNR logs written by bench.sh.

    ./analyze.py                 # every case found, default 'shader' column
    ./analyze.py --variants      # every label found, side by side
    ./analyze.py L2_trans_16px   # specific cases

Two details matter for reading the numbers honestly:

* At 24->60 every 5th output frame lands exactly on a source frame and is a
  trivial passthrough for every mode, so those are excluded -- they would
  otherwise inflate every column by the same meaningless amount.
* The first few output frames are dropped: the hook falls back to a
  zero-order hold until it has a full frame window, so they measure startup
  behaviour rather than interpolation quality.

Also note the ceiling: 'hold' can reach infinite PSNR on a static scene
because it copies frames byte-for-byte, while anything going through
libplacebo tops out around 79 dB from the GPU round-trip alone. Do not read
that gap as a shader defect.
"""
import os
import re
import sys

OUTROOT = os.environ.get("OUTROOT") or os.path.join(
    os.environ.get("TMPDIR", "/tmp"), "interp-bench")
SKIP_STARTUP = 5
BASELINES = ("hold", "linear")


def parse(path):
    if not os.path.exists(path):
        return {}
    out = {}
    for line in open(path):
        m = re.match(r"n:(\d+).*?psnr_y:([0-9.]+|inf)", line)
        if m:
            v = m.group(2)
            out[int(m.group(1))] = float("inf") if v == "inf" else float(v)
    return out


def mean_interp(d):
    """Mean PSNR over genuinely-interpolated frames."""
    vals = [v for n, v in d.items()
            if n > SKIP_STARTUP and (n - 1) % 5 != 0 and v != float("inf")]
    if not vals:
        return float("inf") if d else None
    return sum(vals) / len(vals)


def fmt(v):
    if v is None:
        return "    -  "
    if v == float("inf"):
        return "   inf "
    return f"{v:7.2f}"


args = [a for a in sys.argv[1:] if not a.startswith("--")]
show_variants = "--variants" in sys.argv

if not os.path.isdir(OUTROOT):
    sys.exit(f"no results at {OUTROOT} -- run bench.sh first")

cases = args or sorted(d for d in os.listdir(OUTROOT)
                       if os.path.isdir(os.path.join(OUTROOT, d)))

labels = set()
for c in cases:
    for f in os.listdir(os.path.join(OUTROOT, c)):
        if f.endswith(".log"):
            n = f[:-4]
            if n not in BASELINES:
                labels.add(n)
labels = sorted(labels) if show_variants else (["shader"] if "shader" in labels
                                               else sorted(labels)[:1])

w = 22
head = f"{'case':<{w}}{'hold':>8}{'linear':>8} |" + "".join(f"{l:>9}" for l in labels)
if not show_variants and labels:
    head += f"{'vs hold':>9}{'vs linear':>11}"
print()
print(head)
print("-" * len(head))

for c in cases:
    d = os.path.join(OUTROOT, c)
    vals = {m: mean_interp(parse(os.path.join(d, m + ".log")))
            for m in list(BASELINES) + labels}
    row = f"{c:<{w}}{fmt(vals['hold'])}{fmt(vals['linear'])} |"
    row += "".join(fmt(vals[l]) for l in labels)
    if not show_variants and labels:
        s, h, l = vals[labels[0]], vals["hold"], vals["linear"]
        if None in (s, h, l) or float("inf") in (s, h, l):
            row += f"{'  -':>9}{'  -':>11}"
        else:
            row += f"{s - h:>+9.2f}{s - l:>+11.2f}"
    print(row)

print()
print("PSNR of genuinely interpolated frames only, dB, higher is better.")
print("A motion-compensated shader that does not clearly beat 'linear' is not")
print("earning its complexity. Beating 'linear' by <0 means it is actively")
print("worse than stock libplacebo on that content.")
