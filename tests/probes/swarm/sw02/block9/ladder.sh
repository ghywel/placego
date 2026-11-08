#!/bin/sh
# Block 9 ladder: usage ladder.sh LANG_BINARY. Runs the fixed list below; no adaptive widening.
L="$1"
"$L" 01 5 0 12
for b in 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do "$L" 001 $b 1 18; done
for b in 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do "$L" 011 $b 0 18; done
for b in 6 8 10 11 12 13 14 15 16 17; do "$L" 0011 $b 0 18; done
for b in 6 8 10 12 14 16; do "$L" 0001 $b 1 18; "$L" 0111 $b 0 18; done
