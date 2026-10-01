#!/usr/bin/env bash
# The research build on Linux, inside the container the Dockerfile beside this makes (or on a plain Debian host).
# BUILDANDUSAGE.md's Linux recipe made a script, with the same optional pins as build-macos.sh, so a Linux host
# builds the SAME FFmpeg and libplacebo a Mac was gated on, carrying the same three patches:
#
#   docker build -t nframe-build - < Dockerfile
#   docker run --rm -v nframe-vol:/work nframe-build git clone <this repository> /work/nframe
#   docker run --rm --device /dev/dri -v nframe-vol:/work nframe-build \
#     bash /work/nframe/scripts/linux/build-linux.sh [stage]        placebo|ffmpeg|verify (default: all)
#   (add -e MESA_VK_DEVICE_SELECT=<vendor:device> on a host with several GPUs; the Arc A310 is 8086:56a6)
#
#   FFMPEG_REF / PLACEBO_REF   full shas to pin (default: master of the day)
#   ROOT                       where it builds (default /work)
#
# Everything is in ROOT, a docker volume, so the container is disposable. The patches come from the repo checkout
# the script lives in, never from a copy.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"           # scripts/
ROOT="${ROOT:-/work}"
PREFIX="$ROOT/libplacebo-install"
STAGE="${1:-all}"
JOBS="$(nproc)"
say()  { printf '\n== %s\n' "$*"; }
info() { printf '   %s\n' "$*"; }
die()  { printf '\nFAILED: %s\n' "$*" >&2; exit 1; }
want() { [ "$STAGE" = all ] || [ "$STAGE" = "$1" ]; }
pin() {   # pin <clone dir> <ref or empty> -- as build-macos.sh
  [ -n "$2" ] || return 0
  ( cd "$1" && git fetch --depth 1 origin "$2" && git checkout -q FETCH_HEAD ) || die "could not pin $1 to $2"
  info "pinned $(basename "$1") to $(cd "$1" && git rev-parse --short HEAD)"
}
# A pin asked for on a REUSED clone used to be ignored without a word (2026-10-01): the build carried on at whatever
# commit the clone held. Now a set REF must match the clone's commit, or the stage stops and says how to redo it.
check_pin() {   # check_pin <clone dir> <ref or empty>
  [ -n "$2" ] || return 0
  local head; head="$(cd "$1" && git rev-parse HEAD)" || die "cannot read $1's commit"
  case "$head" in
    "$2"*) info "$(basename "$1") is at the pin $2" ;;
    *) die "$1 is at $head, not the pin $2 (re-clone it: delete $1)" ;;
  esac
}

if want placebo; then
  say "libplacebo, patched"
  SRC="$ROOT/libplacebo"
  if [ ! -d "$SRC" ]; then
    git clone --depth 1 https://code.videolan.org/videolan/libplacebo.git "$SRC" || die "clone failed"
    pin "$SRC" "${PLACEBO_REF:-}"
    ( cd "$SRC" && git apply --verbose "$HERE/frame-mix-hook.patch" ) || die "frame-mix-hook.patch did not apply"
    # fast_float: src/convert.cc needs it where the C++ library lacks floating-point std::from_chars (libc++, on
    # macOS, 2026-08-30); GCC's libstdc++ has it, so here it is fetched only to keep the two builds alike
    ( cd "$SRC" && git submodule update --init --depth 1 3rdparty/fast_float ) || die "no fast_float"
  else
    info "reusing $SRC"
    check_pin "$SRC" "${PLACEBO_REF:-}"
  fi
  RECONF=""; [ -d "$SRC/build" ] && RECONF="--reconfigure"
  # the headers' own registry, not the distribution's older one: the generator must match the headers
  VKREG=/usr/local/share/vulkan/registry/vk.xml; [ -f "$VKREG" ] || VKREG=/usr/share/vulkan/registry/vk.xml
  info "vk.xml $VKREG"
  ( cd "$SRC" && meson setup build $RECONF --buildtype=release -Dvulkan=enabled -Dopengl=disabled -Ddemos=false \
      -Dvulkan-registry="$VKREG" -Dprefix="$PREFIX" ) || die "meson setup failed"
  # BUILDANDUSAGE.md: meson succeeds without shaderc and every shader then fails to load. Refuse that build.
  grep -q -E 'Run-time dependency shaderc found: YES' "$SRC/build/meson-logs/meson-log.txt" \
    || die "meson did not find shaderc: this libplacebo could not load a single custom shader"
  # One command a line, each with its own die: `a && b` is exempt from set -e, and the first run of this
  # script (2026-09-30) carried on to ffmpeg after libplacebo failed to compile -- a silent failure.
  ninja -C "$SRC/build" -j "$JOBS" || die "libplacebo did not compile"
  ninja -C "$SRC/build" install || die "libplacebo did not install"
fi

if want ffmpeg; then
  say "ffmpeg against it"
  FF="$ROOT/ffmpeg"
  if [ ! -d "$FF" ]; then
    git clone --depth 1 https://github.com/FFmpeg/FFmpeg.git "$FF" || die "clone failed"
    pin "$FF" "${FFMPEG_REF:-}"
    for p in frame-mix-nn-threshold.patch hw-base-encode-eof-nullcheck.patch; do
      ( cd "$FF" && git apply --verbose "$HERE/$p" ) || die "$p did not apply"
    done
  else
    info "reusing $FF"
    check_pin "$FF" "${FFMPEG_REF:-}"
  fi
  # A reused clone must carry the N:N patch (as build-macos.sh): an unpatched ffmpeg builds and runs without a word.
  grep -q 'ithresh = -1.0f' "$FF/libavfilter/vf_libplacebo.c" || die "$FF lacks frame-mix-nn-threshold.patch (delete $FF to re-clone)"
  PCF="$(find "$PREFIX" -name libplacebo.pc 2>/dev/null | head -1)"
  [ -n "$PCF" ] || die "no libplacebo.pc under $PREFIX: build the placebo stage first"
  PC="$(dirname "$PCF")"
  LIBDIR="$(dirname "$PC")"
  ( cd "$FF" && PKG_CONFIG_PATH="$PC" ./configure --enable-libplacebo --enable-vulkan --disable-doc \
      --extra-ldflags="-Wl,-rpath,$LIBDIR" ) || die "ffmpeg configure failed"
  make -C "$FF" -j "$JOBS" || die "ffmpeg did not compile"
  # Captured first: `ffmpeg | grep -q` under pipefail fails when grep stops at its match and ffmpeg dies on the
  # closed pipe -- the first run's 'built without the libplacebo filter' was that, on a build that had it.
  "$FF/ffmpeg" -hide_banner -filters > "$ROOT/ffmpeg-filters.txt" 2>&1 || die "the new ffmpeg does not run"
  grep -q ' libplacebo ' "$ROOT/ffmpeg-filters.txt" || die "ffmpeg built without the libplacebo filter"
fi

if want verify; then
  say "verify"
  vulkaninfo --summary 2>/dev/null | grep -E 'deviceName|driverName|apiVersion' | sed 's/^ */   /' || true
  cd "$HERE/tests"
  FFMPEG="$ROOT/ffmpeg/ffmpeg" FFPROBE="$ROOT/ffmpeg/ffprobe" ./smoke.sh
fi
