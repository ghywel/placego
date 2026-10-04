#!/bin/bash
# timepair.sh <old.glsl> <new.glsl> [pairs] [clip.mkv]: render time of two shaders from a pre-rendered file,
# interleaved after a warm-up, as TESTING.md "Timing basis" asks; prints each pair and the medians. 2026-10-04.
set -u
OLD=$1; NEW=$2; N=${3:-5}; SRC=${4:-/tmp/nframe-identity/L7_textured_large.mkv}
HERE="$(cd "$(dirname "$0")/../.." && pwd)"; . "$HERE/mvk-env.sh"
FF=${FFMPEG:-ffmpeg}
t() { $FF -nostdin -hide_banner -benchmark -init_hw_device vulkan=vk -filter_hw_device vk -i "$SRC" \
        -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=$1" -f null - 2>&1 | grep -o "rtime=[0-9.]*" | cut -d= -f2; }
t "$OLD" >/dev/null; t "$NEW" >/dev/null
o=(); n=()
for i in $(seq 1 "$N"); do a=$(t "$OLD"); b=$(t "$NEW"); o+=("$a"); n+=("$b"); echo "  pair $i: old $a new $b"; done
med() { printf "%s\n" "$@" | sort -n | awk '{v[NR]=$1} END{print (NR%2)?v[(NR+1)/2]:(v[NR/2]+v[NR/2+1])/2}'; }
mo=$(med "${o[@]}"); mn=$(med "${n[@]}")
echo "TIMEPAIR: median old $mo s, new $mn s ($(awk -v a=$mo -v b=$mn 'BEGIN{printf "%+.1f%%", (b-a)/a*100}'))"
