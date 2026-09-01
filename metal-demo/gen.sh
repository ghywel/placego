#!/usr/bin/env bash
# Regenerate generated/ from the GLSL source of truth. Run after ANY edit
# to the quad shader (or its base + generator chain). The .metal files and
# graph.json here are generated material -- never hand-edited (METALPORT.md).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PATH="/opt/homebrew/bin:$PATH"
python3 "$HERE/../tests/gen_metal.py" \
    "$HERE/../quaddirectional-interpolation.glsl" \
    "$HERE/generated" --compile
