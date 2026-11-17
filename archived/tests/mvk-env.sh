# Sourced, not run: MoltenVK DETERMINISM for every macOS harness that runs ffmpeg + libplacebo (2026-09-30).
#
# On macOS the ladder wandered from run to run: 2-4 of 42 cases identical on the M5, 3 on the RX 6600, up to 6 dB
# apart. Two of MoltenVK's own switches end it:
#   - Metal argument buffers OFF: the Apple GPU's random gross dropouts (0 in 12 pendulum runs, against 5.6 per run);
#   - ONE active command buffer per queue: the race across buffers in flight on the AMD GPU and the Intel UHD 630.
# Together, the M5 repeats itself on 40 of 42 cases, all within 0.01 dB, and the RX 6600 on 41 of 42. The cost is
# 1-2 percent of a ladder run. The record is in TESTING.md.
#
# Set by default. MVK_DETERMINISTIC=0 keeps MoltenVK's own defaults, for example for a timing run or a sweep of the
# switches themselves (energy/mvksweep.sh). A value already in the environment wins. Linux and Windows are untouched.
# The python probes that call ffmpeg directly carry the same two lines.
if [ "$(uname -s)" = "Darwin" ] && [ "${MVK_DETERMINISTIC:-1}" != 0 ]; then
  export MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS="${MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS:-0}"
  export MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE="${MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE:-1}"
fi
