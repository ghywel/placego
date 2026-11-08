#!/bin/sh
# Block 9 ladder, second run: usage ladder2.sh LANG_BINARY. Fixed list, no adaptive widening.
# Prediction, written 8 November 2026 18:56 UTC before this run (after run 1, whose 011 B = 20 count
# 183 > 180 missed my prediction 3 because PE-1's counts are at b = 22, not 20):
#  (a) 011, B = 22: one unlabelled SCC of 104931 states; counts at lengths 8, 10, 12, 14, 16 are
#      19, 35, 62, 109, 180; the minimal forbidden words up to length 16 are exactly the fourteen of
#      PE-1.2 and its skeptic: 00 010 01110 011110 111111111111111 11101111110 1110111110111
#      0111110111110 01111110111110 011111110111110 111011011111111 111011111111110
#      1110111110110110 0111111110111110 (some may be non-minimal if a shorter word appears).
#  (b) Longer words (to length 24) lower every growth estimate of run 1, and the ordering by width is kept:
#      growth at length 24 falls with B for 001 (B = 14..22) and for 011 (B = 16..22), and stays above 1.1.
# Counterfactual: a mismatch in (a) means my unlabelled-SCC language differs from PE-1's closure
# language at b = 22 and must be explained before comparison; a growth rising with B refutes (b).
L="$1"
"$L" 011 22 0 24
"$L" 001 22 1 24
for b in 14 16 18 20; do "$L" 001 $b 1 24; done
for b in 16 18 20; do "$L" 011 $b 0 24; done
