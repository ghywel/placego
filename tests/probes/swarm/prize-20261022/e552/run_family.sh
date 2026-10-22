#!/bin/zsh
cd "$(dirname "$0")"
for spec in "24 5 12 0" "8 3 4 0" "80 9 40 0" "80 9 20 0" "120 11 60 0" "80 9 16 0" "120 11 40 0"; do
  nice -n 10 python3 sym_fast.py ${=spec} 90
done
