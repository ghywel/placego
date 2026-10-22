#!/bin/sh
cd "$(dirname "$0")"
n=1
while [ $n -le 10000 ]; do ./fm $n | awk '{print $1, $3}' | sed 's/n=//; s/f=//'; n=$((n+1)); done > allf.txt
echo DONE >> allf.txt
