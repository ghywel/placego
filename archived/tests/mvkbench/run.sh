#!/usr/bin/env bash
# MoltenVK-vs-native-Metal microbenchmark. macOS only (needs the Metal
# framework and swiftc; Vulkan side needs Homebrew vulkan-loader + glslc).
#
#   ./run.sh [rounds]        # default 3
#
# WHY THIS EXISTS. "The translation layer is the bottleneck" is the obvious
# suspicion on any Mac result, and it is untestable at the pipeline level --
# there is no native-Metal build of libplacebo to race. What IS testable is
# the kernel level: the same kernel logic written twice, GLSL dispatched
# through Vulkan/MoltenVK vs MSL dispatched through Metal directly, same
# grids, same barrier policy, same timing, batches interleaved A/B so
# thermal drift cannot favour a side. Three kernels isolate three suspects:
#
#   alu   pure FMA chains        -- delivered FLOPS, translation of arithmetic
#   sad   5x5 block-match search -- the flow search in miniature, texture path
#   tiny  near-empty dispatches  -- per-dispatch fixed cost (48-68 passes/frame
#                                   make this the pipeline-shaped suspect)
#
# THE TRAP IT ENCODES: comparing SYSTEMS tells you nothing about WHY. The
# macro fps deficit conflates kernel speed, dispatch overhead, clocks and
# thermals; only twin kernels separate them. Measured 2026-09-01 on the M2
# (BUILDANDUSAGE.md "Is MoltenVK the bottleneck"): kernels at parity to
# <0.5%, per-dispatch overhead ~28x, delivered FLOPS ~36% of nominal on a
# fanless chassis -- i.e. the layer was exonerated for execution and the
# deficit reassigned. Not wired into smoke.sh: it needs Metal + swiftc and
# answers a platform question, not a correctness one.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROUNDS="${1:-3}"
BREW="$(brew --prefix 2>/dev/null || echo /opt/homebrew)"
export VK_ICD_FILENAMES="${VK_ICD_FILENAMES:-$BREW/etc/vulkan/icd.d/MoltenVK_icd.json}"

cd "$HERE"
for k in init alu sad tiny; do
  "$BREW/bin/glslc" -fshader-stage=compute -O "$k.comp" -o "$k.spv" || exit 1
done
clang -O2 -o vkbench vkbench.c -I"$BREW/include" -L"$BREW/lib" -lvulkan || exit 1
swiftc -O metalbench.swift -o metalbench -framework Metal || exit 1

for r in $(seq 1 "$ROUNDS"); do
  for m in alu sad tiny; do
    ./metalbench "$m" 2 2>/dev/null
    ./vkbench   "$m" 2 2>/dev/null
  done
done | tee results.csv | sort -t, -k1,1 -k2,2 |
awk -F, '{key=$1","$2; sum[key]+=$4; n[key]++}
     END {for (k in sum) printf "%-12s %.4f ms/dispatch (n=%d)\n", k, sum[k]/n[k], n[k]}' | sort
