#!/bin/bash
# THE THREE TENSOR COMPONENTS ON MATCHED CONTENT (2026-09-10).
#
# The shear gate returned 96.4% of truth, against a recorded 30-80% for divergence and 85-99% for curl. Those
# three numbers are NOT comparable: they were measured on three different scenes. Divergence was scored on a
# FLAT disc expanding 0.6% a frame -- no texture to match and very small flows, which is the hardest case the
# small-flow floor can be given -- while the shear gate is a fully textured field with flows up to 7.6
# px/frame. Comparing them would be comparing the content, not the component.
#
# So put all three on ONE construction: the same textured field (the M2 texture, 40 px period), the same
# tensor magnitude of 0.04 per frame, and the same velocity at the edge of the scored region (7.6 px/frame).
# The three differ only in WHICH component of the velocity gradient is non-zero.
#
#   expansion   u = +K(x-cx), v = +K(y-cy)      divergence 2K/fps = 0.04, curl 0, shear 0
#   rotation    u = -W(y-cy), v = +W(x-cx)      curl 2W/fps = 0.04, divergence 0, shear 0
#   strain      u = +K(x-cx), v = -K(y-cy)      first shear 2K/fps = 0.04, divergence 0, curl 0
#
# Each forward map is a closed form in T (exponential or a rotation matrix), so geq samples its inverse and
# the ladder's ground-truth property holds. Each scene's OTHER two components are a built-in control: they
# are exactly zero by construction, so a non-zero reading there is leakage between the channels.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH" FFMPEG="$FFDIR/ffmpeg.exe"
NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/shear"; cd "$G"
echo "########## MATCHED TENSOR start $(date +%T)"
K=0.48   # 1/s; 2K/24 = 0.04 per frame
TEX='128+110*sin(ld(0)/6.366)*sin(ld(1)/6.366)'
EXPAND="nullsrc=s=1280x720:r=24:d=3,format=gray,geq=lum='st(0\,640+(X-640)*exp(-${K}*T))\;st(1\,360+(Y-360)*exp(-${K}*T))\;${TEX}',format=yuv420p"
ROTATE="nullsrc=s=1280x720:r=24:d=3,format=gray,geq=lum='st(2\,${K}*T)\;st(0\,640+(X-640)*cos(ld(2))+(Y-360)*sin(ld(2)))\;st(1\,360-(X-640)*sin(ld(2))+(Y-360)*cos(ld(2)))\;${TEX}',format=yuv420p"
STRAIN="nullsrc=s=1280x720:r=24:d=3,format=gray,geq=lum='st(0\,640+(X-640)*exp(-${K}*T))\;st(1\,360+(Y-360)*exp(${K}*T))\;${TEX}',format=yuv420p"
render() { rm -rf "$G/m_$1"; mkdir -p "$G/m_$1"
  ( cd "$G" && ffmpeg.exe -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -f lavfi -i "$2" \
      -vf "libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=tensor.glsl,format=rgb48le" -frames:v 24 "$G/m_$1/f%03d.png" ) 2>"$G/err_m_$1"
  echo "  $1: $(ls "$G/m_$1" 2>/dev/null | wc -l) frames"; grep -i error "$G/err_m_$1" | head -1; }
render expand "$EXPAND"; render rotate "$ROTATE"; render strain "$STRAIN"
python - "$G" <<'PY'
import pathlib, subprocess, sys
import numpy as np
g = pathlib.Path(sys.argv[1]); W, H, FS = 1280, 720, 0.5
Y, X = np.mgrid[0:H, 0:W]
mask = (np.abs(X-640) < 380) & (np.abs(Y-360) < 220)
def load(p):
    raw = subprocess.run(["ffmpeg.exe","-v","error","-i",str(p),"-f","rawvideo","-pix_fmt","rgb48le","-"],
                         capture_output=True, check=True).stdout
    return (np.frombuffer(raw, np.uint16).reshape(H,W,3).astype(np.float64)/65535.0 - 0.5)*2*FS
names = ("divergence","curl","first shear")
print(f"\n{'scene':12s} {'component':13s} {'truth':>8} {'read':>9} {'% of truth':>11} {'sd':>8}")
for scene, live in (("expand",0), ("rotate",1), ("strain",2)):
    fr = sorted((g/f"m_{scene}").glob("f*.png"))[6:]
    if not fr: print(f"{scene}: no frames"); continue
    d = np.array([[np.median(load(f)[...,c][mask]) for c in range(3)] for f in fr])
    for c in range(3):
        truth = 0.04 if c == live else 0.0
        med, sd = np.median(d[:,c]), d[:,c].std()
        pct = f"{100*med/truth:10.1f}%" if truth else f"{'(zero)':>11}"
        star = " <-" if c == live else ""
        print(f"{scene:12s} {names[c]:13s} {truth:8.4f} {med:+9.4f} {pct} {sd:8.4f}{star}")
PY
echo "MATCHED TENSOR DONE $(date +%T)"
