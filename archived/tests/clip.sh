#!/bin/bash
# Cut a frame-exact, lossless clip from source material, addressed by TIME.
#
#   ./clip.sh <source> <at> [pad-frames] [output.mkv]
#
#   <at>   where the defect is. Either a time -- 12.5, 1:23.4, 00:01:23.400 --
#          or an explicit source frame as #1234.
#   [pad]  frames of context either side (default 10, so 21 frames).
#
# WHY THIS EXISTS. Cutting a defect clip by hand is unreliable for three
# reasons that all look like user error and are not:
#
#   1. `-ss` with `-c copy` CANNOT be frame-accurate. A stream copy has to
#      start at a keyframe, so it snaps to one no matter what `accurate_seek`
#      says. Frame-exact cutting requires re-encoding -- losslessly here, so
#      nothing is lost. This is the single biggest cause of "I asked for frame
#      1234 and got something else".
#
#   2. Frame numbers RESET after a seek. In `select='between(n,...)'`, `n`
#      counts from the first frame decoded after the seek, not from the start
#      of the file. So a frame number read off a player does not survive being
#      pasted into a filter. This script seeks with `-copyts` and selects on
#      ABSOLUTE timestamps instead, which do survive.
#
#   3. You are usually reading a position off the 60p INTERPOLATED output but
#      need frames from the 24p SOURCE. Frame indices do not map between them;
#      time does. So this takes a time and does the conversion itself.
#
# The mapping, for 23.976 -> 60: output frame N sits at N/60 seconds, which
# falls inside source pair floor(N/60 * 23.976). Read the time off the player,
# give it here, and the arithmetic is done for you -- and printed, so it can
# be checked rather than trusted.
#
# Always verifies what it produced: exact frame count, no black first frame,
# and a contact sheet. If a check fails it says so loudly rather than handing
# back a plausible-looking clip.
#
# Set FFMPEG/FFPROBE to point at the patched build.

set -u
FFMPEG="${FFMPEG:-ffmpeg}"
FFPROBE="${FFPROBE:-ffprobe}"

SRC="${1:?usage: clip.sh <source> <at> [pad-frames] [output.mkv]}"
AT="${2:?where: a time (12.5 | 1:23.4 | 00:01:23.400) or a frame as #1234}"
PAD="${3:-10}"
OUT="${4:-}"

[ -f "$SRC" ] || { echo "no such file: $SRC" >&2; exit 1; }

# --- source properties -----------------------------------------------------
# Parsed by KEY, not by position: ffprobe emits fields in the stream's own
# order rather than the order requested, so positional parsing silently
# transposes them. The csv writer's separator option is also rejected by some
# builds, and fails by producing empty values rather than an error -- which
# then propagates as a plausible-looking wrong answer.
PROBE=$("$FFPROBE" -v error -select_streams v:0 \
    -show_entries stream=r_frame_rate,width,height,codec_name \
    -of default=noprint_wrappers=1 "$SRC")
field() { printf '%s\n' "$PROBE" | sed -n "s/^$1=//p" | head -1; }
FPS_R=$(field r_frame_rate)
WIDTH=$(field width)
HEIGHT=$(field height)
CODEC=$(field codec_name)
[ -n "$FPS_R" ] || { echo "could not probe $SRC -- is it a video file?" >&2; exit 1; }

FPS_N="${FPS_R%%/*}"
FPS_D="${FPS_R##*/}"
[ "$FPS_N" = "$FPS_D" ] && FPS_D=1
FPS=$(awk -v n="$FPS_N" -v d="$FPS_D" 'BEGIN{printf "%.6f", n/d}')

# --- resolve <at> to a source frame index ----------------------------------
case "$AT" in
  \#*)
    FRAME="${AT#\#}"
    ;;
  *)
    # accept H:M:S(.ms), M:S(.ms), or plain seconds
    SECS=$(awk -F: -v s="$AT" 'BEGIN{
        n = split(s, p, ":")
        if (n == 3)      v = p[1]*3600 + p[2]*60 + p[3]
        else if (n == 2) v = p[1]*60 + p[2]
        else             v = p[1]
        printf "%.6f", v
    }')
    FRAME=$(awk -v s="$SECS" -v n="$FPS_N" -v d="$FPS_D" \
            'BEGIN{printf "%d", int(s * n / d + 0.5)}')
    ;;
esac

START=$((FRAME - PAD)); [ "$START" -lt 0 ] && START=0
END=$((FRAME + PAD))
COUNT=$((END - START + 1))

# Exact frame times, with a sub-frame tolerance either side so float rounding
# cannot drop the boundary frames.
T0=$(awk -v f="$START" -v n="$FPS_N" -v d="$FPS_D" 'BEGIN{v=(f-0.4)*d/n; printf "%.6f", (v<0)?0:v}')
T1=$(awk -v f="$END"   -v n="$FPS_N" -v d="$FPS_D" 'BEGIN{printf "%.6f", (f+0.4)*d/n}')

# The seek only has to land EARLIER than T0 -- the timestamp select does the
# exact work -- so it can be sloppy and fast.
SEEK=$(awk -v t="$T0" 'BEGIN{v=t-2.0; printf "%.6f", (v<0)?0:v}')

[ -n "$OUT" ] || OUT="$(basename "${SRC%.*}")_f${START}-${END}.mkv"

printf 'source   %s  (%sx%s %s, %s fps)\n' "$(basename "$SRC")" \
       "$WIDTH" "$HEIGHT" "$CODEC" "$FPS"
printf 'asked    %s\n' "$AT"
printf '  -> source frame %s, cutting %s..%s (%s frames)\n' \
       "$FRAME" "$START" "$END" "$COUNT"
printf '  -> source time  %ss .. %ss\n' "$T0" "$T1"
printf 'output   %s\n' "$OUT"

# -copyts keeps the ORIGINAL timestamps after the seek, which is what makes
# selecting by absolute time work at all. ffv1 because lossless re-encoding is
# the only way to be frame-exact (see note 1 above).
if ! "$FFMPEG" -y -hide_banner -loglevel error \
      -ss "$SEEK" -copyts -i "$SRC" \
      -vf "select='between(t,$T0,$T1)',setpts=PTS-STARTPTS" \
      -fps_mode passthrough -map 0:v:0 -an -sn -dn \
      -c:v ffv1 "$OUT"; then
  echo "  FAILED: ffmpeg returned an error" >&2
  exit 1
fi

# --- verify, rather than assume -------------------------------------------
GOT=$("$FFPROBE" -v error -count_frames -select_streams v:0 \
      -show_entries stream=nb_read_frames -of default=noprint_wrappers=1:nokey=1 "$OUT")
echo "verify"
ok=0
if [ "$GOT" = "$COUNT" ]; then
  echo "  frames        $GOT (expected $COUNT)  OK"
else
  echo "  frames        $GOT (expected $COUNT)  MISMATCH"
  ok=1
fi

# A black first frame means the seek landed somewhere wrong. That has happened
# before and silently invalidated an entire investigation.
BLACK=$("$FFMPEG" -v error -i "$OUT" -vf "select='eq(n\,0)',format=gray,scale=32:18" \
        -frames:v 1 -f rawvideo - 2>/dev/null | od -An -tu1 | tr -s ' ' '\n' |
        grep -v '^$' | sort -rn | head -1)
if [ -n "$BLACK" ] && [ "$BLACK" -gt 8 ]; then
  echo "  first frame   not black (peak $BLACK)  OK"
else
  echo "  first frame   BLACK OR EMPTY (peak ${BLACK:-none})  -- seek landed wrong"
  ok=1
fi

# A contact sheet, so the right moment can be confirmed at a glance instead of
# by opening the clip in a player.
SHEET="${OUT%.*}_sheet.jpg"
COLS=$(awk -v c="$COUNT" 'BEGIN{print (c<7)?c:7}')
ROWS=$(awk -v c="$COUNT" -v k="$COLS" 'BEGIN{print int((c+k-1)/k)}')
if "$FFMPEG" -y -v error -i "$OUT" \
     -vf "scale=iw/3:ih/3,tile=${COLS}x${ROWS}:margin=4:padding=3:color=0x303030" \
     -frames:v 1 -q:v 3 "$SHEET" 2>/dev/null; then
  echo "  contact sheet $SHEET"
fi

if [ "$ok" = 0 ]; then
  echo "  clip covers source frames $START..$END inclusive"
else
  echo "  CHECKS FAILED -- do not trust this clip" >&2
  exit 1
fi
