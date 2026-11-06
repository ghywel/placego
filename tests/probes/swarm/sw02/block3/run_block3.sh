#!/bin/bash
# Block 3 run, frozen with reports/SW02-BLOCK3-JOB.md. From the repository root: run_block3.sh OUT_DIR
# SMOKE=1 runs every step at small sizes, to test the host. OUT_DIR must be durable and outside git.
# A step stopped by its cap is a result: the script records it and goes on.
set -u
OUT=$1
B=tests/probes/swarm/sw02/block3
REF=tests/probes/swarm/sw02
T=$B/targets.txt
mkdir -p "$OUT"/base "$OUT"/r02 "$OUT"/rows "$OUT"/xx "$OUT"/xxp "$OUT"/pq "$OUT"/caps
if [ "${SMOKE:-0}" = 1 ]; then
  ROWB=14; WXX=26; WP=28; WPF=22; WPQ=24; CXX=22; CPQ=20; WR=22; NR=20; CPU=120; WALL=300
else
  ROWB=22; WXX=44; WP=46; WPF=34; WPQ=40; CXX=36; CPQ=32; WR=31; NR=3000; CPU=10800; WALL=14400
fi
shasum -a 256 $B/lift.c $T $B/check_lift.py $B/tails.py $B/reentry.py $B/control_rows.txt $B/run_block3.sh > "$OUT/inputs.sha256"
cc -O2 -o "$OUT/lift" $B/lift.c || exit 1
L=$(cd "$OUT" && pwd)/lift
TT=$(pwd)/$T
step() { # name cpu dir command...
  name=$1; cpu=$2; dir=$3; shift 3
  echo "STEP $name $(date -u +%H:%M:%S)" | tee -a "$OUT/steps.log"
  ( cd "$dir" && python3 "$R/tests/probes/wolfram/run_capped.py" --out "$CAPS/$name" --cpu "$cpu" --wall "$WALL" \
      --rss-mib 8192 --file-mib 4096 --disk-mib 16384 --swap-growth-mib 4096 --track-tree -- "$@" > "$CAPS/$name.launch" 2>&1 )
  rc=$?
  cp "$CAPS/$name/out.txt" "$dir/$name.log" 2>/dev/null
  echo "STEP $name exit $rc $(head -1 "$CAPS/$name.launch") $(date -u +%H:%M:%S)" | tee -a "$OUT/steps.log"
}
R=$(pwd)
CAPS=$(cd "$OUT" && pwd)/caps
for w in 19 20 21 22; do step base$w 120 "$OUT/base" "$L" --targets "$TT" --mode pq --dense $w; done
step base 120 "$OUT/base" "$L" --targets "$TT" --mode pq --wmax 22 --wreport 16 --gapn 0 --out .
step r02 300 "$OUT/r02" "$L" --targets "$TT" --mode xx --r02 --wmax $WR --wreport 16 --gapn 0 --out .
step rows 1800 "$OUT/rows" "$L" --targets "$TT" --mode xx --rows $ROWB 4400 late.txt
step xx $CPU "$OUT/xx" "$L" --targets "$TT" --mode xx --wmax $WXX --wreport 16 --gapn 16 --gap-limit 60000000 --over-max 36 --dump --max-nodes 120000000 --out .
step xxp $CPU "$OUT/xxp" "$L" --targets "$TT" --mode xx --wmax $WP --wreport $WPF --prune-from $WPF --gapn 16 --gap-limit 60000000 --over-max 43 --max-nodes 200000000 --out .
step pq $CPU "$OUT/pq" "$L" --targets "$TT" --mode pq --wmax $WPQ --wreport 16 --gapn 16 --gap-limit 60000000 --over-max 34 --dump --max-nodes 120000000 --out .
step checkxx $CPU "$OUT/xx" python3 "$R/$B/check_lift.py" --targets "$TT" --mode xx --wmax $CXX --scc scc_xx.jsonl --dumps .
step checkpq $CPU "$OUT/pq" python3 "$R/$B/check_lift.py" --targets "$TT" --mode pq --wmax $CPQ --scc scc_pq.jsonl --dumps .
step tails 1800 "$OUT/xx" python3 "$R/$B/tails.py" "$R/$B/control_rows.txt" "$R/$REF" "$TT" . xx
step reentry 1800 "$OUT/rows" python3 "$R/$B/reentry.py" late.txt "$R/$REF" $NR
python3 "$B/summary.py" "$OUT" > "$OUT/SUMMARY.txt"
tail -40 "$OUT/SUMMARY.txt"
