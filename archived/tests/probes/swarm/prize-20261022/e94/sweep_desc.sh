#!/bin/zsh
# usage: sweep_desc.sh LAT P NMIN NMAX K PER_RUN_TL TOTAL_TL LOG   (n descending)
LAT=$1; P=$2; NMIN=$3; NMAX=$4; K=$5; TL=$6; TOT=$7; LOG=$8
start=$(date +%s)
echo "# sweep(desc) $LAT $P n=$NMAX..$NMIN K=$K tl=$TL total=$TOT started $(date)" >> $LOG
for n in $(seq $NMAX -1 $NMIN); do
  now=$(date +%s); el=$((now-start))
  if [ $el -gt $TOT ]; then echo "# total time limit reached at n=$n" >> $LOG; break; fi
  nice -n 10 /usr/bin/python3 sat132.py $LAT $P $n $K $TL >> $LOG 2>&1
done
echo "# done $(date)" >> $LOG
