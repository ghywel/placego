#!/usr/bin/env python3
"""The global motion of a clip, frame pair by frame pair (2026-09-19): phase correlation of consecutive luma frames
at quarter size, the peak's offset scaled back to full-size pixels. For a pan it is the pan's speed and direction;
for a shot with a moving subject on a static ground it is whichever dominates. The reading a defect report needs
first ("a fast pan across a textured wall"): how fast, in the shader's own units, and where the speed changes.

    panspeed.py <clip> [every]        prints frame, dx, dy, |v| px/frame; FFMPEG in the environment or ~/np-build
"""
import os, re, subprocess, sys
import numpy as np

FF = os.environ.get("FFMPEG", os.path.expanduser("~/np-build/ffmpeg/ffmpeg"))

def frames(src, scale=4):
    probe = subprocess.run([FF, "-hide_banner", "-i", src, "-frames:v", "1", "-f", "null", "-"], capture_output=True, text=True, stdin=subprocess.DEVNULL).stderr
    m = re.search(r"(\d{2,5})x(\d{2,5})", probe); w, h = int(m.group(1)), int(m.group(2))
    sw, sh = w // scale, h // scale
    p = subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-i", src, "-vf", f"scale={sw}:{sh}", "-f", "rawvideo", "-pix_fmt", "gray", "-"],
                       capture_output=True, stdin=subprocess.DEVNULL)
    a = np.frombuffer(p.stdout, dtype=np.uint8).reshape(-1, sh, sw).astype(np.float32) / 255.0
    return a, scale

def shift(a, b):
    """The offset that best maps a onto b: the phase correlation peak, with a parabolic sub-pixel refinement."""
    wy = np.hanning(a.shape[0])[:, None]; wx = np.hanning(a.shape[1])[None, :]
    A = np.fft.fft2((a - a.mean()) * wy * wx); B = np.fft.fft2((b - b.mean()) * wy * wx)
    R = A * np.conj(B); R /= np.abs(R) + 1e-9
    r = np.real(np.fft.ifft2(R))
    iy, ix = np.unravel_index(np.argmax(r), r.shape)
    h, w = r.shape
    def sub(i, n, axis):
        m = r[(iy - 1) % h, ix] if axis == 0 else r[iy, (ix - 1) % w]
        p = r[(iy + 1) % h, ix] if axis == 0 else r[iy, (ix + 1) % w]
        c = r[iy, ix]; d = (m - p) / (2 * (m - 2 * c + p)) if (m - 2 * c + p) != 0 else 0.0
        v = i + d
        return v - n if v > n / 2 else v
    return -sub(ix, w, 1), -sub(iy, h, 0), float(r[iy, ix])

def main():
    src = sys.argv[1]; every = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    a, s = frames(src)
    print(f"{os.path.basename(src)}: {len(a)} frames, measured at 1/{s}; dx dy in full-size px per source frame")
    for i in range(1, len(a), every):
        dx, dy, pk = shift(a[i - 1], a[i])
        dx *= s; dy *= s
        print(f"  {i:4d}  dx {dx:+7.2f}  dy {dy:+7.2f}  |v| {np.hypot(dx, dy):6.2f}  peak {pk:.3f}")

if __name__ == "__main__":
    main()
