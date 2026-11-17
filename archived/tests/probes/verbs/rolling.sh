#!/bin/bash
# A VERB-OBJECT CASE: A ROLLING WHEEL (2026-09-10, the owner's suggestion that pairs like "wobbling jelly"
# or "spinning dinnerplate" might generate cases an analytic taxonomy misses).
#
# Rolling without slipping is a LOCK between rotation and translation: omega = v/R. It puts, inside ONE rigid
# body at ONE instant, every speed from zero to 2v -- the contact point is instantaneously at rest while the
# top moves at twice the centre. No axis-wise taxonomy generates that, because it is not a point in the space
# of motions but a constraint curve through it. Physics supplies constraints; taxonomy supplies dimensions.
#
# What it puts the estimator in: a single object spanning from BELOW ITS GATE (the contact, ~0 px/frame) to
# the top of its comfortable range, with the flow direction sweeping the full 360 degrees around the rim, and
# all of it one rigid body with no boundary between the regimes.
#
#   R = 150 px, v = 8 px/frame (192 px/s), so omega = v/R and the top moves at 16 px/frame.
#   Truth, in px/frame, at body offset (dx, dy) from the centre:  u = v - (v/R) dy ,  w = (v/R) dx
#   Contact (0, +R): (0, 0).  Centre: (8, 0).  Top (0, -R): (16, 0).
# The forward map is a rotation matrix in t composed with a linear translation -- a closed form, so the
# ground-truth property holds.
set -u
FFDIR="${FFDIR:-$HOME/np-build/ffmpeg}"   # the project ffmpeg build (BUILDANDUSAGE.md); mingw64/bin for its DLLs
export PATH="/c/msys64/mingw64/bin:$FFDIR:$PATH" FFMPEG="$FFDIR/ffmpeg.exe"
SC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"; G="$NP/verbs"
mkdir -p "$G"; cd "$G"
echo "########## ROLLING start $(date +%T)"

python - "$SC/shaders/quaddirectional-interpolation-propagated.glsl" "$G/vel.glsl" <<'PY'
import pathlib, re, sys
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
t, n = re.subn(r"(//!PARAM read_view\n(?://!.*\n)+)0\n", r"\g<1>4\n", t); assert n == 1
pathlib.Path(sys.argv[2]).write_text(t, encoding="utf-8", newline="\n")
print("  vel.glsl: read_view 4 (machine velocity, FS 32 px/frame)")
PY

R=150; V=192            # px/s ; 8 px/frame at 24 fps
CX=300; CY=360
# body offset by inverting the rotation, texture in the body frame so it rides with the wheel
SCENE="nullsrc=s=1280x720:r=24:d=3,format=gray,geq=lum='st(0\,X-(${CX}+${V}*T))\;st(1\,Y-${CY})\;st(2\,(${V}/${R})*T)\;st(3\,ld(0)*cos(ld(2))+ld(1)*sin(ld(2)))\;st(4\,-ld(0)*sin(ld(2))+ld(1)*cos(ld(2)))\;if(lt(hypot(ld(0)\,ld(1))\,${R})\,128+110*sin(ld(3)/6.366)*sin(ld(4)/6.366)\,20)',format=yuv420p"

rm -rf "$G/roll"; mkdir -p "$G/roll"
( cd "$G" && ffmpeg.exe -y -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -f lavfi -i "$SCENE" \
    -vf "libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=vel.glsl,format=rgb48le" -frames:v 24 "$G/roll/f%03d.png" ) 2>"$G/err_roll"
echo "  rendered $(ls "$G/roll" | wc -l) frames"; grep -i error "$G/err_roll" | head -1
# a picture frame too, so the scene can be looked at
( cd "$G" && ffmpeg.exe -y -hide_banner -loglevel error -f lavfi -i "$SCENE" -frames:v 1 -update 1 "$G/roll_frame0.png" ) 2>/dev/null

python - "$G" <<'PY'
import pathlib, subprocess, sys
import numpy as np
g = pathlib.Path(sys.argv[1]); W, H, FS = 1280, 720, 32.0
R, VPF, CX, CY, FPS = 150.0, 8.0, 300.0, 360.0, 24.0
def load(p):
    raw = subprocess.run(["ffmpeg.exe","-v","error","-i",str(p),"-f","rawvideo","-pix_fmt","rgb48le","-"],
                         capture_output=True, check=True).stdout
    return (np.frombuffer(raw, np.uint16).reshape(H,W,3).astype(np.float64)/65535.0 - 0.5)*2*FS
print("\nthe vertical diameter, where truth is horizontal and spans 0 to 2v:")
print(f"{'dy (px from centre)':>20} {'truth u':>9} {'read u':>9} {'read w':>9} {'% of truth':>11}")
rows=[]
for f in sorted((g/"roll").glob("f*.png"))[8:20]:
    n = int(f.stem[1:]) - 1
    cx = CX + VPF*n                      # centre at output frame n (N:N, so one source frame each)
    a = load(f)
    for dy in (-120, -80, -40, 0, 40, 80, 120):
        x0, y0 = int(cx), int(CY+dy)
        if not (20 <= x0 < W-20): continue
        u = np.median(a[y0-6:y0+7, x0-6:x0+7, 0]); w = np.median(a[y0-6:y0+7, x0-6:x0+7, 1])
        rows.append((dy, VPF - (VPF/R)*dy, u, w))
if rows:
    import collections
    agg = collections.defaultdict(list)
    for dy,t,u,w in rows: agg[dy].append((t,u,w))
    for dy in sorted(agg):
        t = agg[dy][0][0]; u = np.median([x[1] for x in agg[dy]]); w = np.median([x[2] for x in agg[dy]])
        pct = f"{100*u/t:10.1f}%" if abs(t) > 0.2 else f"{'(near zero)':>11}"
        print(f"{dy:20d} {t:9.2f} {u:9.2f} {w:9.2f} {pct}")
    print(f"\n({len(rows)//7} frames aggregated; truth w is 0 on this diameter, so the read w column is leakage)")
else:
    print("no samples")
PY
echo "ROLLING DONE $(date +%T)"
