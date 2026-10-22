#!/bin/bash
# CL504: four shards of kholek, merged summary.  Set SP to the directory holding the kholek binary.
# usage: kk.sh args...  (runs 4 shards of kholek, prints summary)
SP=${SP:-.}
tag=$(echo "$@" | tr ' ' _)
for s in 0 1 2 3; do $SP/kholek "$@" $s 4 > $SP/kk_${tag}_$s.txt & done; wait
cat $SP/kk_${tag}_?.txt | awk -v a="$*" '$1=="A"{ad+=$2; f+=$3} $1=="K"{K[$2]+=$3; if($2>top)top=$2} END{printf "== %s: admitted %d failures %d | failing keys:", a, ad, f; for(g=0;g<=top;g++) if(K[g]) printf " %d:%d", g, K[g]; printf "\n"}'
cat $SP/kk_${tag}_?.txt | grep "^X" | sort | uniq -c | head -20
