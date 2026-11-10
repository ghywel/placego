#!/bin/zsh
# S-05 release wrapper, adapted from S-13's (GC2791, GC2801): only the pins and the headline count change. Run on Local's Wolfram host
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
pin "$NB" 93867733b43d4928517be6b8ce9273832465a02d9b00b7c1eb04629ae7bcc02d
pin "$P/Rule30Submission.lean" d09e01a826f91f57bf3e9ed6288f4b408e4801ecba8b8cf0eb2ef2042507508b
pin "$P/abstract.txt" b196c22051ceb27d4dba3c208715c2348a5a1e6872f95dd4b57a998445315d10
pin "$P/title.txt" 392c9c11680aeacf8059ad597c9dd1b61196c77979dfe6d4e035e45388c2e36d
pin "$P/essay.md" 68213cf3558ecb66deca8b4f804bf1fd495a7802d7ed465ed5c5853d0aca34f7
pin "$P/headlines.txt" fb7ba5a5d031bbdc838af4bb647a55ac74a622c153306b10b924683bea2a3fd5
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
[[ $(print -r -- "$H" | wc -w | tr -d ' ') == 5 ]] || { print -u2 'REFUSED: headline count'; exit 2; }
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
