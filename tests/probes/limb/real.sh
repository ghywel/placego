#!/bin/bash
# The coarse texture-energy channel on real footage (decimate-and-reconstruct, realbench.sh): the committed
# recommendation (vp) against the prototype at two weights, on the three standard clips and the street clip (people
# walking past a still street: bodies against a still background, the case the party found). Three 3-second
# segments each; realanalyze.py summarises PSNR and SSIM per clip.
#   ./real.sh            -> $NP_SCRATCH/limb/real/<clip>/..., real-table.txt
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
NP="${NP_SCRATCH:-$(cd "$TESTS/../../.." && pwd)/np-scratch}"
V="$NP/limb/variants"; G="$NP/limb/real"; mkdir -p "$G"
export FFMPEG="${FFMPEG:-$HOME/np-build/ffmpeg/ffmpeg}" FFPROBE="${FFPROBE:-$HOME/np-build/ffmpeg/ffprobe}"
PY="${PY:-$HOME/np-build/venv/bin/python3}"
cd "$TESTS"
# VARIANTS="label:path label:path ..." overrides the default set (the control vp is always first)
DEFAULT="energy4:$V/bidirectional-interpolation-variational-propagated-energy4.glsl energy8:$V/bidirectional-interpolation-variational-propagated-energy8.glsl"
read -r -a SHADERS <<< "vp:$TESTS/../shaders/bidirectional-interpolation-variational-propagated.glsl ${VARIANTS:-$DEFAULT}"
LABELS="$(for s in "${SHADERS[@]}"; do printf "%s " "${s%%:*}"; done)"
G="$NP/limb/real${TAG:+-$TAG}"; mkdir -p "$G"
clip() {
  local src="$1" tag="$2"; shift 2
  export OUTROOT="$G/$tag"; rm -rf "$OUTROOT"; mkdir -p "$OUTROOT"
  local s
  for s in "${SHADERS[@]}"; do
    bash ./realbench.sh "$NP/$src" "${s%%:*}" "${s#*:}" "$@" </dev/null 2>&1 | grep -iE "FAIL|ALARM|passthrough" | head -3 | sed "s/^/  [$tag ${s%%:*}] /"
  done
  echo "== $tag"; "$PY" ./realanalyze.py $LABELS 2>&1 | grep -E "PSNR|SSIM|dB" | head -12
}
{
clip streetpeople-1080p.mp4        street   2 8 14
clip avengersclip.mp4              avengers 10 30 50
clip backtothefuture60sec24fps.mp4 bttf     10 30 50
clip bluey.mkv                     bluey    60 180 300
echo "REAL DONE $(date +%T)"
} 2>&1 | tee "$G/real-table.txt"
