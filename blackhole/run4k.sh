#!/bin/bash
export PATH="/c/msys64/mingw64/bin:${FFDIR:-$HOME/np-build/ffmpeg}:$PATH"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; NP="${NP_SCRATCH:-/e/nframe-project/np-scratch}"
cd "$NP/eyes/blackhole"
python "$HERE/geodesic_disc.py" jp full4k_jp 240 3840 2160 4 > kerr4k.log 2>&1
echo "KERR4K DONE $(date +%T)" >> kerr4k.log
bash ./kerr4krender.sh > kerr4krender.log 2>&1
