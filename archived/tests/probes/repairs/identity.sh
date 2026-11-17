#!/bin/bash
# identity.sh <a.glsl> <b.glsl> [case ...]: render ladder scenes through two shaders and say whether every output
# frame is byte-identical (framemd5). Scenes are pre-rendered once to ffv1 (a file source: TESTING.md "Timing
# basis"), 24 -> 60 fps, with MoltenVK's determinism switches on macOS. Run a against a first: the control must be
# identical, or nothing this says means anything. REPAIRS.md lead L1, 2026-10-04.
set -u
A=$1; B=$2; shift 2
CASES=${*:-L7_textured_large L2_trans_16px O5_osc_textured L9_occlusion}
HERE="$(cd "$(dirname "$0")/../.." && pwd)"          # tests/
. "$HERE/mvk-env.sh"
FF=${FFMPEG:-ffmpeg}
W=${IDENTITY_DIR:-/tmp/nframe-identity}; mkdir -p "$W"
render() {   # shader case -> framemd5 lines (hash column only)
  $FF -nostdin -hide_banner -loglevel error -init_hw_device vulkan=vk -filter_hw_device vk -i "$W/$2.mkv" \
      -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=$1" -f framemd5 - 2>"$W/err.log" | grep -v '^#' | awk -F, '{print $NF}'
}
same=0; diff=0
for c in $CASES; do
  [ -s "$W/$c.mkv" ] || $FF -nostdin -hide_banner -loglevel error -f lavfi -i "$(. "$HERE/scenes.sh"; scene "$c" 24)" \
      -frames:v 61 -c:v ffv1 -level 3 -y "$W/$c.mkv"
  ha=$(render "$A" "$c"); hb=$(render "$B" "$c")
  n=$(echo "$ha" | grep -c .); d=$(diff <(echo "$ha") <(echo "$hb") | grep -c '^<')
  [ "$n" -gt 0 ] || { echo "  $c: NO FRAMES ($(head -2 "$W/err.log"))"; diff=$((diff+1)); continue; }
  if [ "$d" = 0 ]; then echo "  $c: identical ($n frames)"; same=$((same+1)); else echo "  $c: $d of $n frames differ"; diff=$((diff+1)); fi
done
echo "IDENTITY DONE: $same identical, $diff not"
