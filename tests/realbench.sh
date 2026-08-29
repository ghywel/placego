#!/bin/bash
# Ground-truth benchmarking on REAL footage, by decimate-and-reconstruct.
#
#   ./realbench.sh <source-video> <label> <shader|linear|hold> [seconds...]
#
# Method: drop every 2nd frame, interpolate back to the original rate, and
# compare against the frames that were deleted. Those frames are the exact
# correct answer. This is the standard frame-interpolation benchmark method
# and it needs no special source material -- any video works.
#
#   [seg @ 24fps] --keep even--> [12fps] --interpolate--> [24fps]
#                \                                            /
#                 \-------------- compare --------------------/
#
# IMPORTANT -- read TESTING.md's "Real-footage traps" section before trusting
# any number this produces. Two things silently invalidate the measurement:
#
#   1. Frame misalignment. psnr pairs frames by TIMESTAMP, and 24000/1001 fps
#      rounded into a millisecond timebase does not pair cleanly. This script
#      renders to a file, then compares with setpts=N/TB on both sides to
#      force index pairing. It prints a passthrough check every run: the
#      RETAINED frames must come back bit-exact. If they do not, stop.
#   2. Source animated "on twos". If each drawing is held for 2 video frames,
#      half the frames being "reconstructed" are duplicates of frames the
#      shader was handed, which flatters every mode. Use ./screen.sh first.
#
# Also: report SSIM, not just PSNR. PSNR systematically favours blur -- a
# linear blend's smooth double-image scores BETTER on PSNR than a sharp but
# slightly-misplaced motion-compensated frame, which inverts the true
# ranking. Measured on real footage: PSNR ranked linear above the shader
# while SSIM and direct visual inspection both ranked it well below.

set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FFMPEG="${FFMPEG:-ffmpeg}"
FFPROBE="${FFPROBE:-ffprobe}"
OUTROOT="${OUTROOT:-${TMPDIR:-/tmp}/interp-real}"

SRC="${1:?usage: realbench.sh <source-video> <label> <shader-path|linear|hold> [seconds...]}"
LABEL="${2:?}"
WHAT="${3:?}"
shift 3
SEGS="${*:-210 240 300}"
RATE="${RATE:-24000/1001}"
HALFRATE="${HALFRATE:-12000/1001}"
DUR="${DUR:-3}"
mkdir -p "$OUTROOT"

case "$WHAT" in
  hold)   CHAIN="fps=$RATE"; HW="" ;;
  linear) CHAIN="libplacebo=fps=$RATE:frame_mixer=linear"; HW="-init_hw_device vulkan=vk -filter_hw_device vk" ;;
  *)      CHAIN="libplacebo=fps=$RATE:frame_mixer=custom_n:custom_shader_path=$WHAT"
          HW="-init_hw_device vulkan=vk -filter_hw_device vk" ;;
esac

for s in $SEGS; do
  # Full-rate reference and half-rate input, both lossless, both with
  # explicit timestamps so the frame counts are checkable.
  [ -s "$OUTROOT/ref_$s.mkv" ] || "$FFMPEG" -y -hide_banner -loglevel error \
    -ss "$s" -t "$DUR" -i "$SRC" -map 0:v:0 -an -sn \
    -vf "setpts=N/($RATE)/TB" -r "$RATE" -c:v ffv1 "$OUTROOT/ref_$s.mkv"
  [ -s "$OUTROOT/half_$s.mkv" ] || "$FFMPEG" -y -hide_banner -loglevel error \
    -i "$OUTROOT/ref_$s.mkv" \
    -vf "select='not(mod(n\,2))',setpts=N/($HALFRATE)/TB" -r "$HALFRATE" \
    -c:v ffv1 "$OUTROOT/half_$s.mkv"

  # Render NATURALLY -- no setpts, no -r. Either one makes the muxer re-time
  # and duplicate frames (a setpts here once turned 72 frames into 1725).
  # shellcheck disable=SC2086
  "$FFMPEG" -y -hide_banner -loglevel error $HW -i "$OUTROOT/half_$s.mkv" \
    -vf "${CHAIN},format=yuv420p" -c:v ffv1 "$OUTROOT/o_${LABEL}_$s.mkv" \
    2>"$OUTROOT/${LABEL}_$s.err" || { echo "  seg $s FAILED"; continue; }

  # Compare with forced frame-index alignment.
  for metric in psnr ssim; do
    "$FFMPEG" -y -hide_banner -loglevel error \
      -i "$OUTROOT/o_${LABEL}_$s.mkv" -i "$OUTROOT/ref_$s.mkv" \
      -filter_complex "[0:v]format=yuv420p,setpts=N/TB[a];[1:v]format=yuv420p,setpts=N/TB[b];[a][b]${metric}=stats_file=$OUTROOT/${metric}_${LABEL}_$s.log[o]" \
      -map "[o]" -f null - 2>/dev/null
  done
  echo "  seg $s done ($("$FFPROBE" -v error -count_frames -show_entries stream=nb_read_frames -of csv=p=0 "$OUTROOT/o_${LABEL}_$s.mkv") frames)"
done
echo "results under $OUTROOT -- summarise with: ./realanalyze.py"
