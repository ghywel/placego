#!/bin/sh
# sequential sweep, one core; each fm run has a built-in 540 s limit
cd "$(dirname "$0")"
for n in 10000 20000 50000 100000 200000 500000 1000000 2000000 5000000 10000000; do
  nice -n 10 ./fm $n $n K$n.txt >> sweep.log 2>&1
done
echo DONE >> sweep.log
