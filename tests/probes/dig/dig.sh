#!/bin/bash
# The defect funnel on real material, end to end (2026-09-19): prospect a window of a source for moments where
# the flow field disagrees with itself, cut each candidate frame-exactly, decimate-and-reconstruct it with
# hold, linear and the shader, and rank the candidates by how the SHADER FARES AGAINST LINEAR -- because the
# prospector finds estimator disagreement, which is not the same thing as a visible fault. The first candidate
# it ever ranked (an anime opening's credits over a dense cityscape pan: 16% of every frame an outlier) came
# out 3.7 dB AHEAD of linear on reconstruction, with the lowest edge error: a hard field, not a defect. The
# owner's brief: "use the prospector tool to find sequences with detectable error that aren't abrupt scene
# cuts". A detectable error is one the reconstruction can measure, so that is the ranking.
#
#   ./dig.sh <source> <start-seconds> <duration-seconds> [label] [shader]
#
#   The shader defaults to the recommendation; the label to the source's basename. Output: a table under
#   $NP_SCRATCH/dig/<label>/ (RESULTS.txt) with one row per candidate -- the prospector's rank and time, the
#   three modes' PSNR (Y, synthesised frames only) and SSIM, the edge error of linear and the shader, and the
#   shader's margin over linear in dB -- sorted by that margin ascending: the top of the table is where the
#   shader is worst relative to the bar, the material to look at with eyes and to crystallise.
#
#   Caveats carried from the tools it drives (read TOOLS.md): decimation doubles every motion, so a clip that
#   fails here at 12 fps may be fine at 24 (the margin is still the right ranking); a clip on twos flatters
#   every mode (screen.sh first on animation); PSNR rewards blur (SSIM and the edge error are the columns to
#   trust); and the prospector masks scene cuts but a candidate that straddles one is still possible -- the
#   contact sheet clip.sh writes beside each clip shows it.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS="$(cd "$HERE/../.." && pwd)"
export FFMPEG="${FFMPEG:-${FFDIR:-$HOME/np-build/ffmpeg}/ffmpeg}"
export FFPROBE="${FFPROBE:-$(dirname "$FFMPEG")/ffprobe}"
export PY="${PY:-$HOME/np-build/venv/bin/python3}"; export PYTHON="$PY"
SRC="${1:?usage: dig.sh <source> <start-seconds> <duration-seconds> [label] [shader]}"
START="${2:?start seconds}"; DUR="${3:?duration seconds}"
LABEL="${4:-$(basename "${SRC%.*}" | tr -c 'A-Za-z0-9._-' '_' | cut -c1-40)}"
SHADER="${5:-$TESTS/../shaders/bidirectional-interpolation-variational-propagated.glsl}"
NP_SCRATCH="${NP_SCRATCH:-$(cd "$TESTS/../../.." && pwd)/np-scratch}"
OUT="$NP_SCRATCH/dig/$LABEL"; mkdir -p "$OUT"
TOP="${TOP:-6}"                                          # candidates taken from the prospector's shortlist
PAD="${PAD:-40}"                                          # frames of context either side of a candidate (the bench needs 72)
export OUTROOT="$OUT/bench"; mkdir -p "$OUTROOT"
export WORK="$OUT/prospect"

echo "== dig: $(basename "$SRC") from ${START}s for ${DUR}s -> $OUT"
# REUSE=1 keeps an existing prospect.txt (the scan is the slow half; the bench can be run again alone).
if [ "${REUSE:-0}" = 1 ] && [ -s "$OUT/prospect.txt" ]; then echo "   reusing $OUT/prospect.txt"; else
"$TESTS/prospect.sh" "$SRC" "$START" "$DUR" "$SHADER" > "$OUT/prospect.txt" 2>&1 </dev/null
fi
grep -E "candidate|nothing stands out|scan took" "$OUT/prospect.txt" | sed 's/^/   /'
# The shortlist's clip.sh lines carry the time and the pad the prospector suggests; the time is what is kept.
grep -E "^\s+\./clip\.sh " "$OUT/prospect.txt" | head -n "$TOP" | awk '{print $(NF-1)}' > "$OUT/candidates.txt"
n=$(wc -l < "$OUT/candidates.txt" | tr -d ' ')
[ "$n" -gt 0 ] || { echo "   no candidates; nothing to bench"; exit 0; }

score() {   # label -> "psnr ssim" over the synthesised frames (even n after the first four), from the bench's logs
  "$PY" - "$OUTROOT" "$1" <<'PY'
import re, sys, statistics, os
root, lab = sys.argv[1], sys.argv[2]
def load(path, key):
    v = []
    for line in open(path):
        m = re.search(key + r":([0-9.]+|inf)", line); n = re.match(r"n:(\d+)", line)
        if m and n: v.append((int(n.group(1)), 99.0 if m.group(1) == "inf" else float(m.group(1))))
    return [x for n, x in v if n % 2 == 0 and n > 4]
try:
    p = load(os.path.join(root, f"psnr_{lab}_0.log"), "psnr_y")
    s = load(os.path.join(root, f"ssim_{lab}_0.log"), "All")
    print(f"{statistics.mean(p):.2f} {statistics.mean(s):.4f}")
except Exception as e:
    print("nan nan")
PY
}
edge() {   # variants... -> the edge tool's rows
  "$TESTS/edgeerror.sh" 0 "$@" 2>/dev/null | awk 'NF==4 && $2 ~ /^[0-9.]+$/ {print $1, $2, $3}'
}

printf "%-4s %-12s %8s %8s %8s %7s %7s %7s %8s %8s %9s\n" rank time hold linear shader ssimH ssimL ssimS edgeL edgeS margin > "$OUT/RESULTS.txt"
# The candidates are read into an array first: a loop fed from the file lost every candidate but the first,
# because the bench's ffmpeg read the rest of the list as its standard input (2026-09-19).
CANDS=(); while IFS= read -r line; do CANDS+=("$line"); done < "$OUT/candidates.txt"
i=0
for at in "${CANDS[@]}"; do
  i=$((i + 1)); clip="$OUT/clip-$i.mkv"
  echo "-- candidate $i at $at"
  "$TESTS/clip.sh" "$SRC" "$at" "$PAD" "$clip" > "$OUT/clip-$i.txt" 2>&1 </dev/null || { echo "   clip failed (see clip-$i.txt)"; continue; }
  rm -f "$OUTROOT"/*_0.* "$OUTROOT"/ref_0.mkv "$OUTROOT"/half_0.mkv
  for m in hold linear; do "$TESTS/realbench.sh" "$clip" "$m" "$m" 0 > "$OUT/bench-$i-$m.txt" 2>&1 </dev/null; done
  "$TESTS/realbench.sh" "$clip" shader "$SHADER" 0 > "$OUT/bench-$i-shader.txt" 2>&1 </dev/null
  grep -h "FAILED" "$OUT"/bench-$i-*.txt | sed 's/^/   /'
  read -r ph sh <<<"$(score hold)"; read -r pl sl <<<"$(score linear)"; read -r ps ss <<<"$(score shader)"
  read -r _ el _ <<<"$(edge linear | head -1)"; read -r _ es _ <<<"$(edge shader | head -1)"
  margin=$("$PY" -c "print(f'{float(\"$ps\")-float(\"$pl\"):+.2f}')" 2>/dev/null || echo nan)
  printf "%-4s %-12s %8s %8s %8s %7s %7s %7s %8s %8s %9s\n" "$i" "$at" "$ph" "$pl" "$ps" "$sh" "$sl" "$ss" "${el:-nan}" "${es:-nan}" "$margin" | tee -a "$OUT/RESULTS.txt"
  mkdir -p "$OUT/bench-$i"; mv "$OUTROOT"/o_*_0.mkv "$OUTROOT"/*_0.log "$OUT/bench-$i/" 2>/dev/null
done

echo; echo "== ranked by the shader's margin over linear (ascending: worst first)"
{ head -1 "$OUT/RESULTS.txt"; tail -n +2 "$OUT/RESULTS.txt" | sort -k11,11n; } | tee "$OUT/RANKED.txt"
echo "clips and contact sheets: $OUT/clip-N.mkv, clip-N_sheet.jpg"
