#!/bin/zsh
cd "$(dirname "$0")"
nice -n 10 python3 sym_fast.py 46 7 3 1 150
nice -n 10 python3 sym_fast.py 46 7 2 0 150
