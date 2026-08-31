#!/usr/bin/env python3
"""Export the acceleration/flow field as DATA, with units, not as a picture.

    ./fieldexport.py <raw16-file> <accel_diag_fs> <out-prefix> [--frames a,b,c]

WHY THIS EXISTS. Everything measured about this field so far has gone through
a picture: the shader encodes `a` into RGB, ffmpeg pushes it down a video
path, and a script decodes it back. That round trip is the weakest link in
calling the field an instrument, and it is load-bearing for every consumer
downstream of it -- the whole point of the N:N use case is that something
else reads these numbers.

This turns one render into two files:

    <prefix>.f32     raw float32, shape (frames, H, W, 2), ax then ay,
                     in px per source-interval^2 -- the shader's own units
    <prefix>.json    what those numbers mean: dimensions, units, the scale
                     they were decoded with, and the saturation audit below

WHAT IT GUARDS AGAINST. `ACCEL_DIAG_FS` is the encoding's full scale, and a
field value beyond it is CLIPPED, not wrapped -- it comes back as exactly
+/-FS and looks like a confident reading. That is not hypothetical: an early
low-band calibration in this project reported "+4.000" against a true +1.917
and the number was the encoding's ceiling rather than the shader's answer.
A 16-bit picture cannot tell you it overflowed, so this tool counts the
texels sitting at the rail and refuses to stay quiet about them.

Nothing here interprets the field. It decodes, audits, and writes; comparing
against truth is accelcheck.py's job.
"""
import json
import pathlib
import struct
import sys

if len(sys.argv) < 4:
    sys.exit(__doc__.strip().splitlines()[2].strip())

raw_path = pathlib.Path(sys.argv[1])
fs = float(sys.argv[2])
prefix = pathlib.Path(sys.argv[3])
W, H = 1280, 720

want = None
for arg in sys.argv[4:]:
    if arg.startswith("--frames"):
        want = [int(v) for v in arg.split("=", 1)[1].split(",")] \
            if "=" in arg else None
if want is None and "--frames" in sys.argv:
    want = [int(v) for v in sys.argv[sys.argv.index("--frames") + 1].split(",")]

data = raw_path.read_bytes()
fsz = W * H * 6                       # rgb48le: 3 channels x 2 bytes
nfr = len(data) // fsz
if nfr == 0:
    sys.exit(f"{raw_path}: {len(data)} bytes is not one {W}x{H} rgb48le frame")
frames = want if want is not None else list(range(nfr))
frames = [f for f in frames if 0 <= f < nfr]
if not frames:
    sys.exit(f"{raw_path}: holds {nfr} frames, none of the requested ones exist")

# TRI_DIAG=2 encodes a as 0.5 + (a / FS) * 0.5 in R (ax) and G (ay), so the
# decode is exact and the only lossy step is the 16-bit quantisation itself:
# one code is 2*FS/65535 px/interval^2.
code = 2.0 * fs / 65535.0
RAIL = 4                              # codes from an end that count as clipped

out = open(str(prefix) + ".f32", "wb")
sat = 0
live = 0
total = 0
amax = 0.0
for f in frames:
    fr = data[f * fsz:(f + 1) * fsz]
    vals = struct.unpack("<%dH" % (W * H * 3), fr)
    buf = bytearray()
    for i in range(0, len(vals), 3):
        r, g = vals[i], vals[i + 1]
        if r <= RAIL or r >= 65535 - RAIL or g <= RAIL or g >= 65535 - RAIL:
            sat += 1
        ax = (r / 65535.0 - 0.5) * 2.0 * fs
        ay = (g / 65535.0 - 0.5) * 2.0 * fs
        if abs(ax) > code * 8 or abs(ay) > code * 8:
            live += 1
        m = max(abs(ax), abs(ay))
        if m > amax:
            amax = m
        buf += struct.pack("<ff", ax, ay)
        total += 1
    out.write(buf)
out.close()

# Saturation has to be judged against the LIVE texels, not the whole frame.
# A sparse field can rail on most of what it actually reports while the
# whole-frame fraction still rounds to a fraction of a percent -- measured on
# a real A3 render: 0.141% of all texels at the rail, but coverage was 0.7%,
# so a fifth of every reading present was clipped. The whole-frame number
# would have called that negligible.
sat_pct = 100.0 * sat / total
sat_of_live = (100.0 * sat / live) if live else 0.0
# Independently of any fraction: a readback that touches the rail at all means
# the encoding ceiling was reached, and the max is then the ceiling rather
# than the measurement. That is the unambiguous tell.
railed = amax >= fs * (1.0 - 1e-6)
meta = {
    "shape": [len(frames), H, W, 2],
    "dtype": "float32",
    "layout": "frame, row, column, (ax, ay)",
    "units": "px per source-interval^2",
    "source": str(raw_path),
    "frames": frames,
    "accel_diag_fs": fs,
    "quantisation_step": code,
    "coverage_pct": round(100.0 * live / total, 2),
    "saturated_pct_of_frame": round(sat_pct, 4),
    "saturated_pct_of_live": round(sat_of_live, 2),
    "railed": railed,
    "max_abs": round(amax, 4),
}
pathlib.Path(str(prefix) + ".json").write_text(json.dumps(meta, indent=2))

print(f"wrote {prefix}.f32  ({len(frames)} frames, {W}x{H}, 2ch float32)")
print(f"      {prefix}.json (units, scale, audit)")
print(f"coverage      {meta['coverage_pct']:.1f}% of texels carry a reading")
print(f"quantisation  {code:.5f} px/interval^2 per code at FS={fs} in 16-bit")

# The audit is the point of the tool, so it is loud rather than a footnote.
if railed:
    print()
    print(f"*** CLIPPED: readings reach the encoding rail at |a| = {fs}.")
    print(f"*** {sat_of_live:.1f}% OF EVERY READING PRESENT is at the ceiling "
          f"({sat_pct:.3f}% of the frame).")
    print(f"*** Those texels were not measured, they were clamped, and any")
    print(f"*** median or mean over them is meaningless. Re-render with a")
    print(f"*** larger ACCEL_DIAG_FS.")
elif sat_of_live > 0.0:
    print(f"saturated     {sat_of_live:.2f}% of live readings near the rail; "
          f"max |a| {amax:.3f} against FS {fs}")
else:
    print(f"saturated     none; max |a| {amax:.3f} sits inside FS {fs}")
