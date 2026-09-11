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

AND DO NOT AVERAGE THE RAW COLUMN. A decibel is not the same quantity at both
ends of this table. Found 2026-09-10 while ablating the shipped components:
removing the whole variational cascade IMPROVED the plain ladder mean by 1.29
dB, which read as the cascade being a liability -- but the gain was
L2_trans_16px moving 50.01 -> 71.08 and L6_flat_large 48.72 -> 65.55, two
cases that are already far past any visible error, while its losses were on
the aperture series where error is visible. Restricted to the regime that can
matter the cascade is a positive, not a liability. The same averaging had the
zero seed, which rescues H1 from 19.28 to 55.86 dB, contributing no more per
case than a change nobody could see. So the summary below CAPS each case
before averaging: improvements above the cap contribute nothing, differences
below it count in full. The cap is a convention (see CAP_DB), not a
perceptual measurement -- it is there to stop the arithmetic being nonsense,
not to claim a threshold of visibility.
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


# Above this, a difference is not a difference anyone can see, and averaging it
# against a case sitting at 19 dB is arithmetic on two different quantities.
# 40 dB is the usual convention for visually lossless 8-bit; it is a
# convention and the honest way to place it is the owner's eyes on a render.
CAP_DB = float(os.environ.get("CAP_DB", "40"))


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
        if f.endswith(".log") and not f.startswith("._"):
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

table = {}
for c in cases:
    d = os.path.join(OUTROOT, c)
    vals = {m: mean_interp(parse(os.path.join(d, m + ".log")))
            for m in list(BASELINES) + labels}
    table[c] = vals
    row = f"{c:<{w}}{fmt(vals['hold'])}{fmt(vals['linear'])} |"
    row += "".join(fmt(vals[l]) for l in labels)
    if not show_variants and labels:
        s, h, l = vals[labels[0]], vals["hold"], vals["linear"]
        if None in (s, h, l) or float("inf") in (s, h, l):
            row += f"{'  -':>9}{'  -':>11}"
        else:
            row += f"{s - h:>+9.2f}{s - l:>+11.2f}"
    print(row)


if labels:
    usable = [c for c in cases
              if all(table[c].get(l) not in (None, float("inf")) for l in labels)]
    if usable:
        capped = {l: sum(min(table[c][l], CAP_DB) for c in usable) / len(usable)
                  for l in labels}
        raw = {l: sum(table[c][l] for c in usable) / len(usable) for l in labels}
        binding = [c for c in usable if min(table[c][l] for l in labels) < CAP_DB]
        ref = labels[0]
        print()
        print(f"{'summary over ' + str(len(usable)) + ' scoreable cases':<{w}}"
              f"{'raw mean':>12}{'capped at ' + str(int(CAP_DB)):>14}"
              f"{'vs ' + ref:>12}")
        print("-" * (w + 38))
        for l in labels:
            print(f"{l:<{w}}{raw[l]:12.2f}{capped[l]:14.2f}{capped[l] - capped[ref]:+12.2f}")
        print()
        print(f"{len(binding)} of {len(usable)} cases have any variant below {CAP_DB:g} dB; only those can")
        print("move the capped mean. The raw mean is kept because the record quotes it,")
        print("but prefer the capped column: it does not average a decibel at 19 dB")
        print("against a decibel at 71 dB as though they were the same quantity.")

print()
print("PSNR of genuinely interpolated frames only, dB, higher is better.")
print("A motion-compensated shader that does not clearly beat 'linear' is not")
print("earning its complexity. Beating 'linear' by <0 means it is actively")
print("worse than stock libplacebo on that content.")
