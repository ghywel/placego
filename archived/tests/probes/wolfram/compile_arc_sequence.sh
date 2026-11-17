#!/bin/sh
# Compile only the frozen core-Lean dependency and break sequence into the supervisor's fresh output folder.
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
arc_sequence_lean=$1
cp reports/wolfram-agents/submissions/arc-codes/ArcBreakBounds.lean "$CAPPED_OUT/ArcBreakBounds.lean"
cp reports/wolfram-agents/submissions/arc-codes/ArcBreakSequence.lean "$CAPPED_OUT/ArcBreakSequence.lean"
cd "$CAPPED_OUT"
"$arc_sequence_lean" -o ArcBreakBounds.olean ArcBreakBounds.lean
LEAN_PATH="$CAPPED_OUT${LEAN_PATH:+:$LEAN_PATH}" "$arc_sequence_lean" ArcBreakSequence.lean
