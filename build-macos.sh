#!/usr/bin/env bash
# Build a patched libplacebo + ffmpeg on macOS, against MoltenVK.
#
#   ./build-macos.sh [stage]        deps|placebo|ffmpeg|verify
#   FORCE=1 ./build-macos.sh        rebuild even where outputs exist
#
# VERIFIED 2026-08-30 on macOS 15.7.9 (Intel), MoltenVK 1.4.2, against an
# AMD Radeon RX 6600 eGPU. It was written blind on Windows before that machine
# had been booted, and took five fixes to get there -- each is commented at
# the point it matters. The full harness passes: 10 of 10 in smoke.sh.
#
# Read the accuracy caveat in BUILDANDUSAGE.md before trusting a NUMBER from
# this platform. The shaders run correctly here, but the ground-truth ladder
# does not reproduce from run to run while the baselines through the same
# harness are bit-identical -- so this is a portability target, not a
# measurement one.
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

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/.." && pwd)"
ROOT="${ROOT:-$HOME/np-build}"
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
info "repo     $REPO"
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
[ -d "$FF" ] || git clone --depth 1 https://github.com/FFmpeg/FFmpeg.git "$FF" \
  || die "clone failed"

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
if [ -f "$REPO/scripts/tests/smoke.sh" ]; then
  ( cd "$REPO/scripts/tests" && bash ./smoke.sh )
else
  die "harness not found at $REPO/scripts/tests"
fi

say "done"
info "Linux reference for the ladder, base shader / variational:"
info "  L1_trans_8px 41.34 / 42.35   L2_trans_16px 38.45 / 39.89"
info "  L9_occlusion 38.31 / 40.18"
info "Windows reproduced these to 0.01 dB. If macOS does too, the patch is"
info "portable across three Vulkan implementations."
fi
