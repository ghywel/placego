#!/bin/zsh
# S-12 release wrapper, adapted from the S-08 hybrid's (GC2791, GC2801): only the pins change. Run on Local's Wolfram host
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
pin "$NB" 921e668a8c44ed736286018eec1c7b29c26f564ab8133f87c65398463a5bed74
pin "$P/Rule30Submission.lean" 3d36e9068d67b634da019b1a465daa9140ec60ce2e9365d2772610211aaed6df
pin "$P/abstract.txt" 10c549f2185ae48c12a233339e2d8f38f2949eeceb2cdef4b672819f90558d15
pin "$P/title.txt" ec7b0c59406cc6bd8b955cc3f7f00f12ca4cc16bbe0ba2465e9cc4b9e29f62d5
pin "$P/essay.md" fe17e5d4710e298491572db65271e3ce7fb4a9ece536a33fa8af92a1a1941c36
pin "$P/headlines.txt" a348f7cd871ee68a72f29ba20e4f75cd093a368a72e6df04a8e4dc35057d8307
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
[[ $(print -r -- "$H" | wc -w | tr -d ' ') == 20 ]] || { print -u2 'REFUSED: headline count'; exit 2; }
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
