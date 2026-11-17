#!/bin/zsh
# build.sh MODULE [timeout] [lines]: lake build one module in the scratch copy of the verifier's kit, with time and memory
export PATH=$HOME/.elan/bin:$PATH
M=$1
cp $HOME/placego-data/wall/pkg/$M.lean $HOME/placego-data/wall/pkg/kit/lean/Ruliology/CellularAutomata/$M.lean
cd $HOME/placego-data/wall/pkg/kit/lean
LEAN_NUM_THREADS=2 /usr/bin/time -l nice -n 10 timeout ${2:-280} lake build Ruliology.CellularAutomata.$M 2>&1 | grep -vE 'page reclaims|page faults|swaps|block input|block output|messages|signals|voluntary|involuntary|instructions|cycles|peak memory|average' | head -${3:-70}
