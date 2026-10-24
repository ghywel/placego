#!/bin/zsh
# Capped, process-group-scoped notebook build for the Rule 30 Prize pipeline (Local, 2026-10-24, for GC1760).
# usage: NB_PIPELINE_DIR=<pipeline folder> nb_build_capped.sh NAME CAP_S OUTLOG   (the folder holds NAME/essay.md and Rule30PrizeKit)
# What it does: starts `wolframscript -file build_sub.wl NAME` in its OWN process group (a setsid launcher), so the
# kernel, LeanLink's lake/lean children and any temp-file lean belong to that group; samples the group's processes and RSS
# every 10 s to OUTLOG.rss; at CAP_S seconds of wall it sends TERM to the whole group, then KILL after 10 s; after the job
# ends (any way) it lists every process still in the group and every lean/lake/WolframKernel on the machine, and records
# the exit code, wall time and that cleanup verdict. It kills nothing outside the group it started.
set -u
NAME=$1; CAP=$2; OUT=$3
[ -n "${NB_PIPELINE_DIR:-}" ] || { echo "set NB_PIPELINE_DIR to the pipeline folder (outside git)" >&2; exit 2; }
cd "$NB_PIPELINE_DIR" || { echo "no pipeline dir" >&2; exit 2; }
SETSID='import os,sys; os.setsid(); os.execvp(sys.argv[1], sys.argv[1:])'   # the job becomes its own process-group leader
START=$(date +%s); echo "start $(date '+%F %T') name=$NAME cap_s=$CAP" > "$OUT"; : > "$OUT.rss"
if [ -n "${NB_TEST_CMD:-}" ]; then python3 -c "$SETSID" zsh -c "$NB_TEST_CMD" & else python3 -c "$SETSID" wolframscript -file build_sub.wl "$NAME" > "$NAME/build.log" 2>&1 & fi
WS=$!; MYPG=$(ps -o pgid= -p $$ | tr -d ' '); PG=""
for i in {1..50}; do PG=$(ps -o pgid= -p $WS | tr -d ' '); [ "$PG" = "$WS" ] && break; sleep 0.1; done   # wait for setsid to take
if [ "$PG" != "$WS" ] || [ "$PG" = "$MYPG" ]; then echo "REFUSED: job pgid '$PG' is not its own pid $WS (wrapper pgid $MYPG); killing pid only" >> "$OUT"; kill -KILL $WS 2>/dev/null; wait $WS 2>/dev/null; echo "VERDICT not-clean (launcher)" >> "$OUT"; exit 3; fi
echo "job pid $WS pgid $PG (wrapper pgid $MYPG)" >> "$OUT"
CAPHIT=0
while kill -0 $WS 2>/dev/null; do
  NOW=$(date +%s)
  if (( NOW - START > CAP )); then CAPHIT=1; echo "WALL CAP HIT at $((NOW-START)) s: TERM to group $PG" >> "$OUT"; kill -TERM -- -$PG 2>/dev/null; sleep 10; kill -KILL -- -$PG 2>/dev/null; echo "KILL sent to group $PG" >> "$OUT"; break; fi
  echo "$(date +%H:%M:%S) $(ps -o pid=,rss=,comm= -g $PG 2>/dev/null | awk '{printf "%s:%s:%s ", $1, $2, $3}')" >> "$OUT.rss"
  sleep 10
done
wait $WS 2>/dev/null; RC=$?
sleep 2
LEFT=$(ps -o pid=,comm= -g $PG 2>/dev/null | wc -l | tr -d ' ')
GLOBAL=$(ps -axo pid=,comm= | grep -E '/(lean|lake|WolframKernel)$' | wc -l | tr -d ' ')
echo "exit $RC wall $(( $(date +%s) - START )) s cap_hit $CAPHIT group_left $LEFT lean_lake_kernel_anywhere $GLOBAL $(date '+%F %T')" >> "$OUT"
[ "$LEFT" = "0" ] && [ "$CAPHIT" = "0" ] && [ "$RC" = "0" ] && echo "VERDICT clean" >> "$OUT" || echo "VERDICT not-clean" >> "$OUT"
