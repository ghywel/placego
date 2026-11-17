#!/bin/sh
# SEMI (coarse buckets) at 3 windows per dyadic block, j=20..36, to reduce window variance of the delta=2 estimate.
for j in 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36; do
  for f in 1.1 1.4 1.7; do
    X=$(/usr/bin/python3 -c "print(int(2**$j*$f))")
    echo "BLOCK j=$j f=$f"
    nice -n 10 ./smodel5 $X 2097152 2600 60
  done
done
