#!/bin/zsh
# run_capped.sh: launch one probe under stage-wide limits and keep receipts (Local, 2026-10-26, L961).
# Usage: run_capped.sh OUTDIR CPU_S WALL_S RSS_MIB OUT_MIB -- command args...
# Enforces: CPU seconds (ulimit -t), output file size (ulimit -f), wall time and process-group RSS (sampled every second; kill on exceed),
# a pre-launch free-memory gate (>= 4 GiB free+inactive, no swap in use growth check), one process group. Writes OUTDIR/{out.txt,err.txt,
# time.txt,launcher.log}. Exit status: the child's, or 124 wall stop, 125 RSS stop, 126 memory gate refused.
set -u
OUT=$1 CPU=$2 WALL=$3 RSS=$4 OMB=$5; shift 5; [[ $1 == -- ]] && shift
mkdir -p $OUT; LOG=$OUT/launcher.log
pg=$(sysctl -n hw.pagesize); vs=$(vm_stat)
free_pages=$(( $(echo "$vs" | awk '/Pages free/ {gsub("\\.","",$3); print $3}') + $(echo "$vs" | awk '/Pages inactive/ {gsub("\\.","",$3); print $3}') ))
free_mib=$(( free_pages * pg / 1048576 ))
echo "start $(date -u +%Y-%m-%dT%H:%M:%SZ) cpu=$CPU wall=$WALL rss_mib=$RSS out_mib=$OMB free_mib=$free_mib cmd=$*" > $LOG
if (( free_mib < 4096 )); then echo "REFUSED memory gate" >> $LOG; exit 126; fi
(
  ulimit -t $CPU; ulimit -f $(( OMB * 2048 ))
  exec /usr/bin/time -l "$@" > $OUT/out.txt 2> $OUT/err.txt
) &
child=$!
t0=$SECONDS; stopc=""
while kill -0 $child 2>/dev/null; do
  sleep 1
  pids=$child; for k in $(pgrep -P $child 2>/dev/null); do pids="$pids,$k"; for g in $(pgrep -P $k 2>/dev/null); do pids="$pids,$g"; done; done
  rss_kib=$(ps -o rss= -p $pids 2>/dev/null | awk '{s+=$1} END {print s+0}')
  if (( rss_kib > RSS * 1024 )); then echo "RSS STOP at ${rss_kib} KiB" >> $LOG; pkill -TERM -P $child; kill -TERM $child; stopc=125; break; fi
  if (( SECONDS - t0 > WALL )); then echo "WALL STOP" >> $LOG; pkill -TERM -P $child; kill -TERM $child; stopc=124; break; fi
done
wait $child; rc=$?
[[ -n $stopc ]] && rc=$stopc
echo "end $(date -u +%Y-%m-%dT%H:%M:%SZ) rc=$rc elapsed_s=$(( SECONDS - t0 ))" >> $LOG
grep -E 'real|maximum resident' $OUT/err.txt > $OUT/time.txt 2>/dev/null
exit $rc
