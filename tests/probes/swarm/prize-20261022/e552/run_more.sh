#!/bin/zsh
cd "$(dirname "$0")"
nice -n 10 python3 sym_fast.py 49 7 7 0 90 cadical
nice -n 10 python3 sym_fast.py 49 7 24 1 60
nice -n 10 python3 sym_fast.py 49 7 8 1 60
nice -n 10 python3 sym_fast.py 51 7 17 0 100
nice -n 10 python3 sym_fast.py 49 7 6 1 60
nice -n 10 python3 sym_fast.py 53 7 4 1 60
