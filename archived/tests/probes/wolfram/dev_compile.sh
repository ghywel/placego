#!/bin/sh
# dev_compile.sh (Local, L1130): one DEVELOPMENT compile of a draft Lean file against the pipeline kit's environment.
# Not release evidence: prints the draft's sha256, compiles it with no output object, and reports diagnostics. A
# release check is always a separately frozen stage. Invoke from the kit root under run_capped.py, through
# `lake env sh dev_compile.sh FILE`, with small caps (CPU 120, wall 300, RSS 2048 MiB, file 4, disk 8, launch 4096).
set -eu
: "${CAPPED_OUT:?run under run_capped.py}"
python3 -c "import hashlib,sys; print('draft sha256', hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())" "$1"
status=0
lean -j1 "$1" || status=$?
echo "lean exit $status"
exit "$status"
