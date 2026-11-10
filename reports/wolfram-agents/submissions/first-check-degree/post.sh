#!/bin/zsh
# S-06 release wrapper, adapted from S-08's (GC2791, GC2801): only the pins and the headline count change. Run on Local's Wolfram host
# after GPT's release review, under the owner's standing posting permission of 10 November (L1619).
# Usage: post.sh [--dry] NOTEBOOK OUTPUT_DIRECTORY
# The output directory must be new and outside this repository; responses remain private.
set -euo pipefail

DRY=false
if [[ "${1:-}" == --dry ]]; then DRY=true; shift; fi
if (( $# != 2 )); then
  print -u2 'Usage: post.sh [--dry] NOTEBOOK OUTPUT_DIRECTORY'
  exit 2
fi
P=${0:A:h}
R=${P:h:h:h:h}
NB=${1:A}
OUT=${2:A}
if [[ "$OUT" == "$R" || "$OUT" == "$R/"* ]]; then
  print -u2 'REFUSED: keep the response directory outside the repository'
  exit 2
fi

pin() {
  [[ -r "$1" ]] || { print -u2 "REFUSED: missing ${1:t}"; exit 2; }
  local got
  got=$(shasum -a 256 "$1" | cut -c1-64)
  [[ "$got" == "$2" ]] || { print -u2 "REFUSED: ${1:t} digest differs"; exit 2; }
  print "pin ok ${1:t}"
}
pin "$NB" 9a88746e82f9222d372ac8a440339b8b72d4fa484b3cf0a2156f70ed5f1aa60f
pin "$P/Rule30Submission.lean" b03196f456a96286d891a66383308ecf54b799ea17d5068c48f1da0f8aaf1180
pin "$P/abstract.txt" e98fef66a8c3f99b82aeb4c830a877e7a456daaaa4780583d261c7aeea2df40c
pin "$P/title.txt" 7b6b369f130bca714d9e879acea0f0e6d21e1f5e73830963d30d535f3308e5ae
pin "$P/essay.md" 534a8f4ec42635aa9c215d212fa4f3c2fa0dc56a84c4ef71ec6dac6df4fb8fe3
pin "$P/headlines.txt" 157bcaaeaf5bcb187fd45b1374d3962a5134deed4fdc6f98e2ad03a27db3d0e6
pin "$R/reports/wolfram-agents/pipeline/submit_package.wl" 8849b49efabf960bfb029cf786fede4b1506465a7097d238961ce4133d78d855

VK=$(curl --fail --silent --show-error --max-time 30 \
  https://www.wolframcloud.com/obj/rule-30-prize/Agents/submissions.json |
  python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["environment"]["kit"]["commit"], d["environment"].get("image"))')
print "verifier: $VK"
[[ "$VK" == '5fb591588cfa869bfdc47946799b5ddd70a903d1 rule30-verifier:18' ]] || {
  print -u2 'REFUSED: verifier changed; recheck the packet there before posting'
  exit 3
}
H=$(tr '\n' ' ' < "$P/headlines.txt")
[[ $(print -r -- "$H" | wc -w | tr -d ' ') == 11 ]] || { print -u2 'REFUSED: headline count'; exit 2; }
[[ ! -e "$OUT" ]] || { print -u2 'REFUSED: response directory exists; check for a previous submission'; exit 4; }
if $DRY; then
  print 'DRY: all guards pass; nothing submitted'
  exit 0
fi

mkdir -p "${OUT:h}"
mkdir "$OUT"
cd "$R"
timeout 600 wolframscript -file reports/wolfram-agents/pipeline/submit_package.wl \
  "$NB" "$P/title.txt" "$P/abstract.txt" "$H" "$OUT/response.private.json" 2>&1 |
  sed "s#$HOME#~#g"
