#!/bin/bash
# THE LAST THIRD OF THE TENSOR (2026-09-10). read_view 9 emits divergence (R), curl (G) and the FIRST SHEAR
# (B = du/dx - dv/dy). Lead E scored divergence against a zoom and curl against a rotating disc, but neither
# gate contains any shear -- a rigid rotation has none and a pure zoom has none -- so the one component that
# distinguishes a DEFORMING subject from a rigid one has never been measured.
#
# THE SCENE. A hyperbolic strain of a textured field: every point moves at u = K(x-cx), v = -K(y-cy), so the
# field stretches in x and compresses in y at matched rates. Divergence and curl are identically zero and the
# first shear is 2K/fps everywhere. The forward map is exponential, x(t) = cx + (x0-cx)e^{Kt}, so geq samples
# the inverse: a closed form in T alone, which is the ladder's ground-truth property.
#   K = 0.48 /s at 24 fps -> first shear 0.04 /frame, and 12.8 px/frame at the frame edge (inside the reach).
#
# THE CONTROL. R3_rot_tex is scored in the same run. Its curl is a known 0.2618 /frame and Lead E read it
# within one to five percent over the inner bands. If this scorer does not reproduce that, the shear number
# it prints is worthless, so the control is checked first.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH" FFMPEG="$FFDIR/ffmpeg.exe"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/shear"
mkdir -p "$G"; cd "$G"
. "$SC/tests/scenes.sh"
echo "########## SHEAR start $(date +%T)"

python - "$SC/shaders/quaddirectional-interpolation-propagated.glsl" "$G/tensor.glsl" <<'PY'
import pathlib, re, sys
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
t, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>9\n", t); assert n == 1, n
pathlib.Path(sys.argv[2]).write_text(t, encoding="utf-8", newline="\n")
print("  tensor.glsl: read_view 9 (divergence, curl, first shear at FS 0.5)")
PY

K=0.48
STRAIN="nullsrc=s=1280x720:r=24:d=3,format=gray,geq=lum='st(0\,640+(X-640)*exp(-${K}*T))\;st(1\,360+(Y-360)*exp(${K}*T))\;128+110*sin(ld(0)/6.366)*sin(ld(1)/6.366)',format=yuv420p"

render() {  # <name> <lavfi>
  rm -rf "$G/$1"; mkdir -p "$G/$1"
  ( cd "$G" && ffmpeg.exe -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -f lavfi -i "$2" \
      -vf "libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=tensor.glsl,format=rgb48le" -frames:v 24 "$G/$1/f%03d.png" ) 2>"$G/err_$1"
  echo "  $1: $(ls "$G/$1" 2>/dev/null | wc -l) frames"; head -2 "$G/err_$1" 2>/dev/null | grep -i error
}
render strain "$STRAIN"
render rot "$(scene R3_rot_tex 24)"

python - "$G" <<'PY'
import pathlib, subprocess, sys, math
import numpy as np
g = pathlib.Path(sys.argv[1]); FF = "ffmpeg.exe"; W, H, FS = 1280, 720, 0.5
def load(p):
    raw = subprocess.run([FF,"-v","error","-i",str(p),"-f","rawvideo","-pix_fmt","rgb48le","-"],
                         capture_output=True, check=True).stdout
    a = np.frombuffer(raw, np.uint16).reshape(H, W, 3).astype(np.float64)/65535.0
    return (a - 0.5) * 2 * FS          # divergence, curl, first shear, per frame

def stats(name, frames, mask, truth):
    d = []
    for f in sorted(frames):
        a = load(f)
        d.append([np.median(a[...,c][mask]) for c in range(3)])
    d = np.array(d)
    print(f"\n== {name}: {len(d)} frames, truth (div, curl, shear) = "
          f"({truth[0]:+.4f}, {truth[1]:+.4f}, {truth[2]:+.4f}) per frame")
    for c, nm in enumerate(("divergence","curl     ","shear    ")):
        med = np.median(d[:,c]); sd = d[:,c].std()
        t = truth[c]
        rel = f"{100*med/t:6.1f}% of truth" if abs(t) > 1e-9 else f"(truth zero; read {med:+.4f})"
        print(f"   {nm}  median {med:+.4f}  frame-to-frame sd {sd:.4f}   {rel}")

# the CONTROL first: R3_rot_tex, a 150 px disc at 640,360 rotating at pi rad/s -> curl 2w/fps = 0.2618
Y, X = np.mgrid[0:H, 0:W]
r = np.hypot(X-640, Y-360)
rotmask = (r > 0.1*150) & (r < 0.7*150)
frames = sorted((g/"rot").glob("f*.png"))[6:]
if frames: stats("R3_rot_tex, the control (inner bands 0.1-0.7 R)", frames, rotmask, (0.0, 0.2618, 0.0))
else: print("no rotation frames rendered")

# the shear scene: score away from the frame edge, where the exponential map runs off the source
K, fps = 0.48, 24.0
smask = (np.abs(X-640) < 380) & (np.abs(Y-360) < 220)
frames = sorted((g/"strain").glob("f*.png"))[6:]
if frames: stats("hyperbolic strain, the new gate (central region)", frames, smask, (0.0, 0.0, 2*K/fps))
else: print("no strain frames rendered")
PY
echo "SHEAR DONE $(date +%T)"
