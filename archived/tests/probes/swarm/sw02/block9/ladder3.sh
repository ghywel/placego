#!/bin/sh
# Block 9 ladder, third run (period-4 control against rule30-open's channel-ladder.md): usage ladder3.sh LANG.
# Prediction, written 8 November 2026 18:58 UTC before this run:
#  (a) for 0001, 0011, 0111 the counts at every length are non-increasing in B (B = 16 from run 1, then 18, 20, 22);
#  (b) the six-step growth (c(26)/c(20))^(1/6) at B = 22 is at least 1.20 for 0011 and 0001, and at least 1.15
#      for 0111 (rule30-open's exact growth at W = 30: 1.2274, 1.2295, 1.1827; it cannot rise with width);
#  (c) for 0001 the count at length 26 falls strictly from B = 18 to B = 22, as rule30-open's 0001 channel keeps
#      falling at W = 30.
# Counterfactual: a count rising with B would be a bug (the language is monotone); (b) below the bounds would put my
# languages under rule30-open's exact W = 30 channel at a smaller width, a model mismatch to explain before use.
L="$1"
for b in 18 20 22; do "$L" 0011 $b 0 26; "$L" 0001 $b 1 26; "$L" 0111 $b 0 26; done
