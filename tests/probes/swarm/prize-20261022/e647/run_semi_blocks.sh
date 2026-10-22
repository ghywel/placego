#!/bin/sh
# SEMI-model prediction of the number of delta-solutions per dyadic block [2^j, 2^(j+1)),
# from a window of W = min(2^j, 2^21) n at the block start, scaled by 2^j / W in post-processing.
for j in 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36; do
  X=$((1<<j)); W=$X; if [ $W -gt 2097152 ]; then W=2097152; fi
  K=2600; if [ $X -lt 10000 ]; then K=$((X/2)); fi
  echo "BLOCK j=$j"
  nice -n 10 ./smodel4 $X $W $K 60
done
