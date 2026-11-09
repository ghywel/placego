#!/bin/zsh
# S-16 release wrapper, adapted from S-15's reviewed one (GC2791): only the pins change. Run on Local's Wolfram host
# after GPT's release review and the owner's posting word.
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
pin "$NB" 3e04dd81e581b9cd73f9f4287945e367807b3fc93963a338fb92081e3eee5166
pin "$P/Rule30Submission.lean" 13c3896fe5a24da72f25fe2f1c9711e4a9db9499990c46d7f77ed46bfcbade5f
pin "$P/abstract.txt" ea525a71673537b3767f9cc54c81f15f98abcc4f3fb75b63adf2b9a6a786e5f1
pin "$P/title.txt" 18a50bde366204a3fd2a18979a6f8de96a0d9dd9c2407d50fd068055fd9a79af
pin "$P/essay.md" 7135bcb0a32b009a03fd7225801a7ae2cf6ee34f41bdfa9046fd321061c71c0d
pin "$P/headlines.txt" 3d2d74b44795d94a8e32d1d25c7e212d5d5f551a0fec388e01c00992b473a3f8
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
[[ $(print -r -- "$H" | wc -w | tr -d ' ') == 7 ]] || { print -u2 'REFUSED: headline count'; exit 2; }
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
