#!/usr/bin/env bash
# Build a patched libplacebo + ffmpeg on macOS, against MoltenVK.
#
#   ./build-macos.sh [stage]        deps|placebo|ffmpeg|verify
#   FORCE=1 ./build-macos.sh        rebuild even where outputs exist
#
# VERIFIED 2026-10-01 on an Apple M5 (macOS 27.0.1) and 2026-09-30 on an Intel MacBook Pro (macOS 15.8, RX 6600
# eGPU), MoltenVK 1.4.2, at ffmpeg ff2059a + libplacebo c42968d (BUILDANDUSAGE.md, "Status and pins"): smoke.sh 17
# of 17 on the M5, 15 of 15 on the Intel Mac (before two checks were added). First walked 2026-08-30 on the Intel
# Mac; it had been written blind on Windows and took five fixes, each commented at the point it matters.
#
# MEASURING HERE: the ground-truth ladder wandered from run to run until two MoltenVK switches were found that end
# it (tests/mvk-env.sh, which bench.sh sources; MOLTENVK-NONDETERMINISM-INVESTIGATED.md). With them a Mac is a
# measurement host too.
#
# HISTORY: the rest of this header was written on 2026-08-30, before the first run, and is kept as the record of
# what was expected. Both suspects below turned out not to be the problem; since 2026-09-02 the RX 6600 is also a
# Vulkan device on Windows.
#
# WHY MACOS IS A DIFFERENT PROPOSITION. There is no native Vulkan here.
# Everything runs through MoltenVK, which translates Vulkan to Metal. That is
# a third Vulkan implementation after Mesa and AMD's Windows driver, and a
# translation layer rather than a driver -- which makes it a harder portability
# test than Windows was, and a more interesting result if it passes.
#
# THE TWO THINGS MOST LIKELY TO BREAK, both worth checking before blaming
# anything else:
#
#   1. VK_KHR_push_descriptor. libplacebo asks for it, and it was absent from
#      MoltenVK for a long time. If shaders fail to load with a descriptor or
#      pipeline-layout error, this is the first suspect.
#   2. Storage images. The interpolation shaders declare ten of them for the
#      persistent flow cache and use imageStore/imageLoad throughout. MoltenVK
#      supports storage images, but the combination with the mpv-shader
#      //!STORAGE path is not something this project has ever exercised.
#
# GPU EXPECTATIONS. Apple added RDNA2 support for the Radeon RX 6000 series on
# Intel Macs in macOS 12 Monterey, so a card of that generation may well be
# driven natively here -- unlike on this project's Windows install, where the
# RX 6600 is enumerated by the OS and driven by D3D12 but never appears as a
# Vulkan device. If it does work, this becomes the only configuration in the
# project with both a modern GPU and a translation-layer Vulkan, which is the
# most interesting combination available.
#
# Worth thirty seconds in System Information -> Graphics/Displays first, since
# eGPU behaviour also depends on the macOS version. Falling back to an internal
# GPU costs nothing for a correctness and portability test.

set -uo pipefail

# Everything is found from this script's own directory (the patches, shaders/ and tests/ sit beside it), so the same
# script works in the repository, where it is scripts/build-*.sh, and in a copy whose root IS scripts/ (2026-10-01:
# it used to look for "$HERE/tests", which a copy without the scripts/ level does not have).
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${ROOT:-$HOME/np-build}"
# PINS (2026-09-30). By default each clone is upstream's master of the day. For numbers comparable across
# hosts, build the exact commits another host was gated on: FFMPEG_REF=<full sha> PLACEBO_REF=<full sha>. A
# shallow clone cannot check out an arbitrary commit, so the pin is fetched by its sha (both hosts allow it)
# and checked out detached; the patches then apply to it as to master.
pin() {   # pin <clone dir> <ref or empty>
  [ -n "$2" ] || return 0
  ( cd "$1" && git fetch --depth 1 origin "$2" && git checkout -q FETCH_HEAD ) \
    || die "could not pin $1 to $2"
  info "pinned $(basename "$1") to $(cd "$1" && git rev-parse --short HEAD)"
}
# A pin asked for on a REUSED clone used to be ignored without a word (2026-10-01): the build carried on at whatever
# commit the clone held. Now a set REF must match the clone's commit, or the stage stops and says how to redo it.
check_pin() {   # check_pin <clone dir> <ref or empty>
  [ -n "$2" ] || return 0
  local head; head="$(cd "$1" && git rev-parse HEAD)" || die "cannot read $1's commit"
  case "$head" in
    "$2"*) info "$(basename "$1") is at the pin $2" ;;
    *) die "$1 is at $head, not the pin $2 (re-clone it: FORCE=1, or delete $1)" ;;
  esac
}
PREFIX="$ROOT/libplacebo-install"
JOBS="${JOBS:-$(sysctl -n hw.ncpu 2>/dev/null || echo 4)}"
FORCE="${FORCE:-0}"
FROM="${1:-deps}"

say()  { printf '\n\033[1m== %s\033[0m\n' "$*"; }
info() { printf '   %s\n' "$*"; }
die()  { printf '\n\033[31mFAILED: %s\033[0m\n' "$*" >&2; exit 1; }

ensure_python() {
  MESONPY="$(sed -n '1s/^#!//p' "$(command -v meson)" 2>/dev/null)"
  [ -n "$MESONPY" ] && [ -x "$MESONPY" ] || MESONPY="$(command -v python3)"
  VENV="$ROOT/venv"
  # A venv from another interpreter is rebuilt, the old one kept aside (2026-09-30). The Intel Mac's was made
  # from Apple's python 3.9 before Homebrew existed there; reused, it put 3.9's site-packages on meson's 3.14
  # PYTHONPATH, and scale_shader.py (write_text(newline=), 3.10+) failed two smoke tests.
  if [ -x "$VENV/bin/python3" ]; then
    have="$("$VENV/bin/python3" -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
    want="$("$MESONPY" -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
    if [ "$have" != "$want" ]; then
      info "venv is python $have, meson's interpreter is $want: rebuilding it (the old one kept as venv.py$have)"
      mv "$VENV" "$VENV.py$have" || die "could not move the old venv aside"
    fi
  fi
  if [ ! -x "$VENV/bin/pip" ]; then
    info "creating $VENV using $MESONPY"
    "$MESONPY" -m venv "$VENV" || die "could not create the venv at $VENV"
  fi
  "$VENV/bin/pip" install --quiet --upgrade jinja2 || die "could not install jinja2"
  "$VENV/bin/pip" install --quiet --upgrade numpy ||
    info "numpy install failed -- harness metrics will not run"
  SITE="$(echo "$VENV"/lib/python*/site-packages)"
  [ -d "$SITE" ] || die "venv site-packages not found under $VENV"
  export PYTHONPATH="$SITE${PYTHONPATH:+:$PYTHONPATH}"
  # ...and the venv's own interpreter first on PATH (2026-09-30): the harness's tools start with `env python3`,
  # and a python3 that is not the one this site-packages was built for fails to import numpy's C core
  # ("No module named 'numpy._core._multiarray_umath'") -- four smoke tests failed so in a fresh ROOT.
  export PATH="$VENV/bin:$PATH"
  "$MESONPY" -c "import jinja2, sys; print('   jinja2   %s (via %s)' % (jinja2.__version__, sys.executable))" ||
    die "meson's interpreter still cannot import jinja2 (PYTHONPATH=$PYTHONPATH)"
}


[ "$(uname -s)" = "Darwin" ] || die "this is the macOS script; you are on $(uname -s)"
command -v brew >/dev/null || die \
  "Homebrew not found. Install it from https://brew.sh and re-run."
BREW="$(brew --prefix)"
mkdir -p "$ROOT" || die "cannot create $ROOT"

stage_wanted() {
  local order="deps placebo ffmpeg verify" s want=0
  for s in $order; do
    [ "$s" = "$FROM" ] && want=1
    [ "$s" = "$1" ] && { [ "$want" = 1 ] && return 0 || return 1; }
  done
  return 1
}

say "environment"
info "macOS    $(sw_vers -productVersion 2>/dev/null || echo unknown)"
info "arch     $(uname -m)"
info "brew     $BREW"
info "scripts  $HERE"
info "build    $ROOT"
info "jobs     $JOBS"

# ---------------------------------------------------------------------------
if stage_wanted deps; then
say "1/4  dependencies"
# molten-vk supplies the Vulkan implementation; vulkan-loader lets the standard
# loader find it; shaderc is the runtime GLSL->SPIR-V compiler libplacebo needs
# to compile custom .hook shaders at all.
PKGS=(meson ninja pkg-config molten-vk vulkan-headers vulkan-loader
      vulkan-tools shaderc glslang nasm python@3.12)
info "brew install ${#PKGS[@]} packages"
brew install "${PKGS[@]}" || die "brew install failed"

# libplacebo generates shader source with Jinja2; Debian supplies it
# transitively and MSYS2 does not, so assume nothing here either.
#
# macOS needs a different approach from both, for two reasons found on
# 2026-08-30 (this replaces a `pip install --user` that could never have
# worked):
#
#   1. Homebrew's Python is PEP 668 "externally managed". Any pip install into
#      it -- including --user -- is refused outright, not merely discouraged.
#   2. meson runs the template step under ITS OWN interpreter, the one in its
#      shebang, not whatever `python3` resolves to on PATH. So a venv earlier
#      on PATH would be ignored, and installing into the wrong interpreter
#      fails later and much less clearly.
#
# The fix that respects both: build a venv and expose it through PYTHONPATH,
# so meson's interpreter can import the modules while nothing is written into
# Homebrew's prefix. jinja2 and numpy are pure enough for this to be safe.
ensure_python
info ""
info "PYTHONPATH must stay set for the libplacebo build. If you run a later"
info "stage on its own the script re-exports it for you; for a manual meson"
info "invocation, set it yourself:"
info "  export PYTHONPATH=$SITE"

say "Vulkan through MoltenVK"
ICD="$BREW/share/vulkan/icd.d/MoltenVK_icd.json"
[ -f "$ICD" ] || ICD="$(find "$BREW" -name 'MoltenVK_icd.json' 2>/dev/null | head -1)"
[ -n "$ICD" ] && [ -f "$ICD" ] || die \
  "MoltenVK ICD manifest not found under $BREW. Vulkan cannot enumerate a
   device without it, so nothing further will work."
info "ICD      $ICD"
export VK_ICD_FILENAMES="$ICD"

if command -v vulkaninfo >/dev/null; then
  vulkaninfo --summary 2>/dev/null |
    grep -iE 'deviceName|driverName|apiVersion' | head -6 | sed 's/^/   /' ||
    info "vulkaninfo produced no device summary -- suspect the ICD"
else
  info "vulkaninfo not on PATH; skipping the device listing"
fi
info ""
info "Add this to your shell profile, or every later step will fail to find"
info "a Vulkan device:"
info "  export VK_ICD_FILENAMES=$ICD"
fi

# ---------------------------------------------------------------------------
if stage_wanted placebo; then
say "2/4  libplacebo, patched"
# re-export PYTHONPATH when this stage is entered directly (see ensure_python)
ensure_python   # idempotent; needed when entering at this stage directly
SRC="$ROOT/libplacebo"
if [ "$FORCE" = 1 ] || [ ! -d "$SRC" ]; then
  rm -rf "$SRC"
  git clone --depth 1 https://code.videolan.org/videolan/libplacebo.git "$SRC" \
    || die "clone failed"
  pin "$SRC" "${PLACEBO_REF:-}"
  ( cd "$SRC" && git apply --verbose "$HERE/frame-mix-hook.patch" ) \
    || die "patch did not apply -- upstream may have moved; rebase it"

  # `git clone --depth 1` fetches no submodules, and libplacebo has six.
  # Most are optional here, but fast_float is NOT: src/convert.cc hard-fails
  # on a static_assert without it, at object 64 of 64, long after everything
  # else has compiled (found 2026-08-30). Fetch it shallowly and by name --
  # a bare `git submodule update --init` would also drag in nuklear (demos
  # are disabled) and glad (the GL backend is disabled), for nothing.
  #
  # Note libplacebo also vendors jinja and markupsafe as submodules, which is
  # the "Alternatively, run git submodule update --init" its error message
  # suggests. We deliberately do NOT use those: the venv built in the deps
  # stage supplies jinja2 anyway, and it has to exist regardless because the
  # test harness needs numpy from it.
  ( cd "$SRC" && git submodule update --init --depth 1 3rdparty/fast_float ) \
    || die "could not fetch the fast_float submodule; src/convert.cc needs it"
  [ -f "$SRC/3rdparty/fast_float/include/fast_float/fast_float.h" ] \
    || die "fast_float fetched but its header is not where convert.cc expects it"
  info "fast_float submodule present"
else
  info "reusing existing clone (FORCE=1 to redo)"
  check_pin "$SRC" "${PLACEBO_REF:-}"
fi

if [ "$FORCE" = 1 ] || [ ! -f "$PREFIX/lib/pkgconfig/libplacebo.pc" ]; then
  # -Dopengl=disabled: the GL backend needs the glad submodule, which we
  # deliberately do not fetch (see above). Vulkan is the only backend this
  # project uses, so this is a saving rather than a workaround.
  #
  # -Dvulkan-registry must be given explicitly on macOS (found 2026-08-30).
  # libplacebo generates src/vulkan/utils_gen.c from the Vulkan registry
  # vk.xml, and searches for it under its own install prefix's datadir.
  # Debian's vulkan-headers puts it on a path that search finds; Homebrew
  # keeps it inside the formula's own keg, so the generator fails at ninja
  # step 2 with "Could not find the vulkan registry (vk.xml)" -- before any
  # compile, which makes it look like a build break rather than a missing
  # path. Point at it via `brew --prefix` so the version number stays out.
  VKREG="$(brew --prefix vulkan-headers 2>/dev/null)/share/vulkan/registry/vk.xml"
  [ -f "$VKREG" ] || VKREG="$BREW/share/vulkan/registry/vk.xml"
  [ -f "$VKREG" ] || die \
    "vk.xml not found. libplacebo cannot generate its Vulkan utils without it.
   Looked under the vulkan-headers keg and $BREW/share/vulkan/registry."
  info "vk.xml   $VKREG"
  ( cd "$SRC" && rm -rf build &&
    PKG_CONFIG_PATH="$BREW/lib/pkgconfig:${PKG_CONFIG_PATH:-}" \
    meson setup build --prefix="$PREFIX" --buildtype=release \
      -Dvulkan=enabled -Dopengl=disabled -Ddemos=false -Dtests=false \
      -Dvulkan-registry="$VKREG" ) \
    || die "meson setup failed"

  LOG="$SRC/build/meson-logs/meson-log.txt"
  grep -qiE "shaderc.*YES" "$LOG" || die \
    "meson did not find shaderc. It would build a libplacebo that silently
   cannot compile custom shaders. See $LOG"
  info "shaderc confirmed"
  grep -qiE "vulkan.*YES" "$LOG" || die "meson did not find Vulkan. See $LOG"
  info "vulkan confirmed"

  ( cd "$SRC" && ninja -C build -j "$JOBS" && ninja -C build install ) \
    || die "libplacebo build/install failed"
fi
[ -f "$PREFIX/lib/pkgconfig/libplacebo.pc" ] || die "libplacebo.pc missing"
info "libplacebo $(PKG_CONFIG_PATH="$PREFIX/lib/pkgconfig" pkg-config --modversion libplacebo)"
fi

# ---------------------------------------------------------------------------
if stage_wanted ffmpeg; then
say "3/4  ffmpeg against it"
FF="$ROOT/ffmpeg"
[ "$FORCE" = 1 ] && rm -rf "$FF"
if [ ! -d "$FF" ]; then
  git clone --depth 1 https://github.com/FFmpeg/FFmpeg.git "$FF" || die "clone failed"
  pin "$FF" "${FFMPEG_REF:-}"
  # Two ffmpeg-side patches this script used to leave to the reader (the M2
  # notes in BUILDANDUSAGE.md say "apply by hand"; folded in 2026-09-11):
  #   frame-mix-nn-threshold.patch -- without it the frame-mix hook silently
  #     never fires at N:N (the queue point-samples one frame), and a window
  #     of five or more is short a frame at the boundary, with no error.
  #   hw-base-encode-eof-nullcheck.patch -- an upstream NULL dereference on
  #     seek with an fps=-scaled output, the command shape used everywhere here.
  for p in frame-mix-nn-threshold.patch hw-base-encode-eof-nullcheck.patch; do
    info "applying $p"
    ( cd "$FF" && git apply --verbose "$HERE/$p" ) ||
      die "$p did not apply -- upstream may have moved; rebase it"
  done
else
  check_pin "$FF" "${FFMPEG_REF:-}"
fi
# A reused clone must already carry the N:N patch. An unpatched ffmpeg builds
# and runs without a word; only the marker test (a dark corner at fps=24 with
# TRI_DIAG=2) would ever show it, so check the source, not the build.
grep -q 'ithresh = -1.0f' "$FF/libavfilter/vf_libplacebo.c" ||
  die "$FF lacks frame-mix-nn-threshold.patch (FORCE=1 re-clones and re-applies)"

if [ "$FORCE" = 1 ] || [ ! -x "$FF/ffmpeg" ]; then
  ( cd "$FF" &&
    PKG_CONFIG_PATH="$PREFIX/lib/pkgconfig:$BREW/lib/pkgconfig" ./configure \
      --enable-libplacebo --enable-vulkan --enable-vulkan-static \
      --enable-videotoolbox \
      --disable-doc \
      --extra-cflags="-I$PREFIX/include -I$BREW/include" \
      --extra-ldflags="-L$PREFIX/lib -L$BREW/lib -Wl,-rpath,$PREFIX/lib -Wl,-rpath,$BREW/lib" ) \
    || die "ffmpeg configure failed -- see $FF/ffbuild/config.log"
  grep -q "^CONFIG_LIBPLACEBO=yes" "$FF/ffbuild/config.mak" \
    || die "configure did not enable libplacebo"
  ( cd "$FF" && make -j "$JOBS" ) || die "ffmpeg build failed"
fi
[ -x "$FF/ffmpeg" ] || die "ffmpeg not produced"
info "ffmpeg   $FF/ffmpeg"
fi

# ---------------------------------------------------------------------------
if stage_wanted verify; then
say "4/4  verify"
FF="$ROOT/ffmpeg"
export FFMPEG="$FF/ffmpeg" FFPROBE="$FF/ffprobe"
[ -x "$FFMPEG" ] || die "no ffmpeg -- run the ffmpeg stage first"
ensure_python   # the harness metrics import numpy from the venv via PYTHONPATH

if [ -z "${VK_ICD_FILENAMES:-}" ]; then
  ICD="$BREW/share/vulkan/icd.d/MoltenVK_icd.json"
  [ -f "$ICD" ] || ICD="$BREW/etc/vulkan/icd.d/MoltenVK_icd.json"
  export VK_ICD_FILENAMES="$ICD"
fi

# NOTE ON THE VULKAN LOADER, worked out the hard way on 2026-08-30.
#
# By default ffmpeg does not link the loader at all -- it dlopen()s it by bare
# leaf name at runtime ("libvulkan.dylib", then "libvulkan.1.dylib", then
# "libMoltenVK.dylib"; see load_libvulkan() in libavutil/hwcontext_vulkan.c).
# Homebrew puts all three in $BREW/lib, but a binary built with a current
# minos does not search /usr/local/lib on that path, so the call fails with
# "Unable to open the libvulkan library!" -- while vulkaninfo enumerates
# devices perfectly, because it links the loader normally. That split between
# two symptoms is the giveaway.
#
# The obvious fix is DYLD_FALLBACK_LIBRARY_PATH, and it does work -- but only
# until something re-execs. SIP strips every DYLD_* variable when a protected
# binary is exec'd, and /bin/bash and /usr/bin/nohup are both protected, so
# the variable silently vanishes the moment the harness shells out. It
# survived here only by accident, because an unprotected bash happened to be
# first on PATH. Anything depending on that is a trap for the next person.
#
# So the ffmpeg stage passes --enable-vulkan-static and an rpath to $BREW/lib
# instead: the loader becomes an ordinary recorded dependency that dyld
# resolves normally, with no environment variable involved anywhere.

info "--- libplacebo filter present?"
# Captured first, deliberately, rather than piped straight into grep -q.
# This script runs under `set -o pipefail`, and `grep -q` exits the moment it
# matches -- which SIGPIPEs ffmpeg, gives the pipeline a non-zero status, and
# fires the `|| die` even on success. That produced a "filter missing" failure
# on 2026-08-30 against an ffmpeg that had the filter (found by running the
# same command by hand). Any `cmd | grep -q` under pipefail has this bug.
FILTERS="$("$FFMPEG" -hide_banner -filters 2>/dev/null)" || true
case "$FILTERS" in
  *libplacebo*) info "present" ;;
  *) die "libplacebo filter missing from this ffmpeg" ;;
esac

info "--- which device does Vulkan give us?"
"$FFMPEG" -hide_banner -v verbose -init_hw_device vulkan=vk \
  -f lavfi -i color=c=black:s=64x64:d=0.1 -f null - 2>&1 |
  grep -iE "Device name|GPU listing|driver" | head -4 | sed 's/^/   /'

info "--- the harness, which is the real test"
# smoke.sh exercises every tool and, importantly, compiles the shaders and
# runs part of the ground-truth ladder. If MoltenVK is missing something the
# shaders need, it fails here with the actual error rather than vaguely.
if [ -f "$HERE/tests/smoke.sh" ]; then
  ( cd "$HERE/tests" && bash ./smoke.sh )
else
  die "harness not found at $HERE/tests"
fi

say "done"
# The real portability test, as build-windows.sh runs it. These scenes are pure
# functions of t, so the 60 fps render is the exact answer for a 24->60
# interpolation of the 24 fps render, and the numbers are platform-independent
# up to driver and compiler noise in the second decimal.
cat <<'REF'
   Reference, PSNR dB, bidirectional-interpolation.glsl (the base shader), 24->60. Compare with the row
   for YOUR pins: the pins move L1 by most of a decibel.
     Apple M5 through MoltenVK (tests/mvk-env.sh's switches), 2026-10-01,
     ffmpeg ff2059a + libplacebo c42968d (BUILDANDUSAGE.md, "Pins"):
       L1_trans_8px 61.92   L2_trans_16px 41.77   L9_occlusion 39.83
     Earlier pins, ffmpeg 5b614ef + libplacebo 3330a51, 2026-09-11:
       RX 6600 / Windows:              L1_trans_8px 61.24   L2_trans_16px 41.76   L9_occlusion 39.83
       Apple M5 through MoltenVK:      L1_trans_8px 61.26   L2_trans_16px 41.78   L9_occlusion 39.83
REF
if [ -f "$HERE/tests/bench.sh" ]; then
  # bench.sh does not change directory, so the shader path is relative to tests/.
  # OUTROOT stays on the internal disk: an exFAT root scatters ._ sidecars beside
  # every log (analyze.py skips them, other readers may not).
  ( cd "$HERE/tests" || exit 1
    SH=../shaders/bidirectional-interpolation.glsl
    export FFMPEG FFPROBE
    export OUTROOT="$ROOT/bench"
    for c in L1_trans_8px L2_trans_16px L9_occlusion; do
      bash ./bench.sh "$c" "$SH" mac_v0 || exit 1
    done
    python3 ./analyze.py --variants
  ) || info "ladder did not complete -- the build itself is still good; run it by hand"
else
  info "harness not found at $HERE/tests -- skipping the ladder"
fi
fi
