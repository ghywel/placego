#!/bin/sh
cd "$(dirname "$0")"
run() { Q=$1 nice -n 10 python3 kraft_slice.py $2 $3 auto $4 2>&1 | grep -E "^q=|kissat|verified" | tr '\n' ' '; echo; }
for m in 5^2,7 5,7^2 5,7,11 5,7,13 5,11,13 7,11,13 5^3,7 5^2,7^2 5,7,17 5,7,19 5,11,17 5,13,17; do run 3 $m 5 200; done
for m in 3^2,7 3^3,7 3,7,11 3,7,13 3^4,7 3^2,7,11; do run 5 $m 4 200; done
for m in 3^2,5 3^3,5 3,5,11 3^2,5^2; do run 7 $m 4 200; done
echo BATCH1-DONE
