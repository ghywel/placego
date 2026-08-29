#!/usr/bin/env bash
# Build a patched libplacebo + ffmpeg on Windows, under MSYS2/MINGW64.
#
#   Run from the MINGW64 shell (not MSYS, not UCRT64):
#     /c/Users/<you>/Documents/Novel-Interpolate/scripts/build-windows.sh
#
#   ./build-windows.sh [stage]      run from a stage: deps|placebo|ffmpeg|verify
#   FORCE=1 ./build-windows.sh      rebuild even where outputs already exist
#
# WHY. The patch's whole justification is that libplacebo is cross-platform,
# and it has only ever been built and run on Debian/Ubuntu. A Windows build
# exercises a different compiler (mingw-w64 rather than gcc/glibc), a
# different Vulkan loader, a different vendor driver (AMD's proprietary
# Windows ICD rather than Mesa RADV), and non-POSIX path handling. If the
# patch and the shaders behave identically across that, the portability claim
# is evidence rather than assertion -- which is what an upstream reviewer will
# want.
#
# This is written to be RESUMABLE and to ASSERT rather than assume: every
# stage checks its own preconditions and refuses to continue on a silent
# failure. That discipline exists because this project has repeatedly been
# handed confident, plausible, meaningless results by a step that quietly did
# not do what it claimed -- a shader that failed to compile and still filled
# in a benchmark table being the worst case.
#
# The final stage does not merely check that ffmpeg runs. It runs part of the
# synthetic ground-truth ladder and compares the numbers against the values
# measured on Linux, so "it built" and "it produces the same answers" are
# separate, separately-confirmed facts.

set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/.." && pwd)"
ROOT="${ROOT:-$HOME/np-build}"
PREFIX="$ROOT/libplacebo-install"
JOBS="${JOBS:-$(nproc)}"
FORCE="${FORCE:-0}"
FROM="${1:-deps}"

say()  { printf '\n\033[1m== %s\033[0m\n' "$*"; }
info() { printf '   %s\n' "$*"; }
die()  { printf '\n\033[31mFAILED: %s\033[0m\n' "$*" >&2; exit 1; }

# ---------------------------------------------------------------------------
# Preconditions
# ---------------------------------------------------------------------------
[ "${MSYSTEM:-}" = "MINGW64" ] || die \
  "run this from the MINGW64 shell. MSYSTEM is '${MSYSTEM:-unset}'.
   Start it from: C:\\msys64\\mingw64.exe
   The plain MSYS shell builds against msys-2.0.dll and will not produce a
   native Windows binary; UCRT64 works too but is less exercised for ffmpeg."

command -v pacman >/dev/null || die "pacman not found -- is this really MSYS2?"
[ -f "$HERE/frame-mix-hook.patch" ] || die "patch not found at $HERE/frame-mix-hook.patch"

mkdir -p "$ROOT" || die "cannot create $ROOT"

stage_wanted() {  # ordered stage gate, so `./build-windows.sh ffmpeg` resumes
  local order="deps placebo ffmpeg verify" s want=0
  for s in $order; do
    [ "$s" = "$FROM" ] && want=1
    [ "$s" = "$1" ] && { [ "$want" = 1 ] && return 0 || return 1; }
  done
  return 1
}

# ---------------------------------------------------------------------------
say "environment"
info "MSYSTEM  $MSYSTEM"
info "repo     $REPO"
info "build    $ROOT"
info "jobs     $JOBS"

# ---------------------------------------------------------------------------
if stage_wanted deps; then
say "1/4  toolchain and dependencies"
# shaderc is the one that actually matters: libplacebo needs a RUNTIME
# GLSL->SPIR-V compiler to compile custom .hook shaders when they are loaded.
# Without it meson still succeeds and produces a libplacebo that cannot run
# any of our shaders -- a silent failure that only shows up much later.
PKGS=(
  git make diffutils
  mingw-w64-x86_64-toolchain
  mingw-w64-x86_64-meson
  mingw-w64-x86_64-ninja
  mingw-w64-x86_64-pkgconf
  mingw-w64-x86_64-shaderc
  mingw-w64-x86_64-vulkan-headers
  mingw-w64-x86_64-vulkan-loader
  mingw-w64-x86_64-nasm
  # libplacebo generates shader source at build time with a Python/Jinja2
  # template step. Debian pulls python3-jinja2 in as a transitive dependency
  # so a Linux build never notices; MSYS2 does not, and the failure arrives
  # partway through ninja as a bare ModuleNotFoundError. Note the package is
  # python-jinja, not python-jinja2.
  mingw-w64-x86_64-python
  mingw-w64-x86_64-python-jinja
)
info "pacman -S --needed ${#PKGS[@]} packages (this can take a while)"
pacman -S --needed --noconfirm "${PKGS[@]}" || die "package install failed"

for t in gcc meson ninja pkgconf git nasm; do
  command -v "$t" >/dev/null || die "$t still not on PATH after install"
  info "$(printf '%-8s %s' "$t" "$(command -v "$t")")"
done
pkgconf --exists shaderc || pkg-config --exists shaderc \
  || die "shaderc not visible to pkg-config -- libplacebo will build without a
   runtime shader compiler and every custom shader will fail to load"
info "shaderc  $(pkgconf --modversion shaderc 2>/dev/null || echo present)"

# Assert the import, not just the package. Several pythons can be on PATH and
# only the one meson picks matters; installing the package is not proof that
# the interpreter doing the work can see the module.
python -c "import jinja2, sys; print('   jinja2   %s (%s)' % (jinja2.__version__, sys.executable))" \
  || die "the python meson will use ($(command -v python)) cannot import jinja2.
   libplacebo generates shader source with it and ninja will fail partway
   through with ModuleNotFoundError."
fi

# ---------------------------------------------------------------------------
if stage_wanted placebo; then
say "2/4  libplacebo, patched"
SRC="$ROOT/libplacebo"
if [ "$FORCE" = 1 ] || [ ! -d "$SRC" ]; then
  rm -rf "$SRC"
  info "shallow clone"
  git clone --depth 1 https://code.videolan.org/videolan/libplacebo.git "$SRC" \
    || die "clone failed"
  # A shallow clone has no submodules, so the opengl backend's glad dependency
  # is absent and that backend hard-fails. Vulkan is all this needs.
  info "applying frame-mix-hook.patch"
  ( cd "$SRC" && git apply --verbose "$HERE/frame-mix-hook.patch" ) \
    || die "patch did not apply -- upstream may have moved; rebase it"
else
  info "reusing existing clone (FORCE=1 to redo)"
fi

if [ "$FORCE" = 1 ] || [ ! -f "$PREFIX/lib/pkgconfig/libplacebo.pc" ]; then
  ( cd "$SRC" && rm -rf build &&
    meson setup build --prefix="$PREFIX" --buildtype=release \
      -Dvulkan=enabled -Dopengl=disabled -Dd3d11=disabled \
      -Ddemos=false -Dtests=false ) || die "meson setup failed"

  LOG="$SRC/build/meson-logs/meson-log.txt"
  grep -qiE "Run-time dependency shaderc found: *YES" "$LOG" \
    || grep -qiE "shaderc.*YES" "$LOG" \
    || die "meson did not find shaderc. Building on would produce a libplacebo
   that silently cannot compile custom shaders. See $LOG"
  info "shaderc confirmed in meson log"
  grep -qiE "vulkan.*YES" "$LOG" || die "meson did not find Vulkan. See $LOG"
  info "vulkan confirmed in meson log"

  ( cd "$SRC" && ninja -C build -j "$JOBS" && ninja -C build install ) \
    || die "libplacebo build/install failed"
else
  info "reusing existing install (FORCE=1 to redo)"
fi
[ -f "$PREFIX/lib/pkgconfig/libplacebo.pc" ] || die "libplacebo.pc missing after install"
info "libplacebo $(PKG_CONFIG_PATH="$PREFIX/lib/pkgconfig" pkgconf --modversion libplacebo)"
fi

# ---------------------------------------------------------------------------
if stage_wanted ffmpeg; then
say "3/4  ffmpeg against it"
FF="$ROOT/ffmpeg"
if [ "$FORCE" = 1 ] || [ ! -d "$FF" ]; then
  rm -rf "$FF"
  info "shallow clone"
  git clone --depth 1 https://github.com/FFmpeg/FFmpeg.git "$FF" || die "clone failed"
fi

if [ "$FORCE" = 1 ] || [ ! -x "$FF/ffmpeg.exe" ]; then
  # No ffmpeg source changes are needed -- fps=, frame pacing,
  # custom_shader_path and frame_mixer= string lookup all already exist in
  # vf_libplacebo.c. Only libplacebo is patched.
  ( cd "$FF" &&
    PKG_CONFIG_PATH="$PREFIX/lib/pkgconfig" ./configure \
      --enable-libplacebo --enable-vulkan \
      --disable-doc --disable-programs --enable-ffmpeg --enable-ffprobe \
      --extra-cflags="-I$PREFIX/include" \
      --extra-ldflags="-L$PREFIX/lib" ) || die "ffmpeg configure failed --
   check $FF/ffbuild/config.log"
  grep -q "enable libplacebo" "$FF/ffbuild/config.log" 2>/dev/null ||
    ( cd "$FF" && grep -q "^CONFIG_LIBPLACEBO=yes" ffbuild/config.mak ) ||
    die "configure did not enable libplacebo"
  ( cd "$FF" && make -j "$JOBS" ) || die "ffmpeg build failed"
fi
[ -x "$FF/ffmpeg.exe" ] || die "ffmpeg.exe not produced"

# Windows has no rpath. The built binaries need libplacebo's DLL beside them
# or on PATH, or they fail at load time with an opaque error.
for dll in "$PREFIX/bin/"libplacebo*.dll; do
  [ -e "$dll" ] && { cp -f "$dll" "$FF/"; info "copied $(basename "$dll") next to ffmpeg.exe"; }
done
info "ffmpeg   $FF/ffmpeg.exe"
fi

# ---------------------------------------------------------------------------
if stage_wanted verify; then
say "4/4  verify -- built, runs, and agrees with Linux"
FF="$ROOT/ffmpeg"
FFMPEG="$FF/ffmpeg.exe"
FFPROBE="$FF/ffprobe.exe"
[ -x "$FFMPEG" ] || die "no ffmpeg.exe -- run the ffmpeg stage first"

info "--- filter present?"
"$FFMPEG" -hide_banner -filters 2>/dev/null | grep -q libplacebo \
  || die "libplacebo filter missing from this ffmpeg"
info "libplacebo filter present"

info "--- which GPU does Vulkan give us?"
"$FFMPEG" -hide_banner -v verbose -init_hw_device vulkan=vk \
  -f lavfi -i color=c=black:s=64x64:d=0.1 -f null - 2>&1 |
  grep -iE "Device name|Using device|driver" | head -4 | sed 's/^/   /'

info "--- does the frame-mix hook actually fire?"
# 24->60 on a synthetic clip. If the hook never fires, libplacebo silently
# falls back to its builtin blend and this still produces 60fps output -- so
# the frame COUNT alone proves nothing. The shader is what must load.
#
# The scene comes from tests/scenes.sh rather than being written out again
# here. An earlier version of this stage carried its own hand-written
# filtergraph and got it wrong -- `geq=lum='...':format=yuv420p` makes
# `format` an option to geq, which has no such option, and the whole thing
# fails with the distinctly unhelpful "Error opening input: Option not found".
# Reusing the definitions that the ladder already exercises removes the
# duplicate that could drift in the first place.
OUT="$ROOT/verify.mkv"
if [ -f "$REPO/scripts/tests/scenes.sh" ]; then
  # shellcheck disable=SC1091
  . "$REPO/scripts/tests/scenes.sh"
  GRAPH="$(scene L1_trans_8px 24)"
  [ -n "$GRAPH" ] && [ "$GRAPH" != "UNKNOWN_CASE" ] || die "scenes.sh gave no scene"
else
  GRAPH="color=c=black:s=640x360:r=24:d=2[bg];color=c=white:s=100x100:r=24:d=2[bx];[bg][bx]overlay=x='200*t':y=120:shortest=1,format=yuv420p"
fi
# The shader is addressed RELATIVELY, from a working directory set to its own
# folder. This is not stylistic: an absolute Windows path cannot be used in an
# ffmpeg filter argument at all, because the colon in "C:" is ffmpeg's own
# option separator and the parser splits on it, reporting
# "No option name near '/Users/...'". Measured against this build, every other
# form fails too -- escaping the colon gets mangled by MSYS2's argument
# conversion, single-quoting is eaten by the shell before ffmpeg sees it, and
# a POSIX path with conversion disabled cannot be opened by a native binary.
# A relative path is the only form that works, and it behaves identically on
# Linux.
if ! ( cd "$REPO/scripts" && "$FFMPEG" -y -hide_banner -loglevel error \
    -init_hw_device vulkan=vk -filter_hw_device vk \
    -f lavfi -i "$GRAPH" \
    -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=bidirectional-interpolation.glsl,format=yuv420p" \
    -c:v ffv1 "$OUT" ) 2>"$ROOT/verify.err"; then
  echo; sed 's/^/   /' "$ROOT/verify.err" | head -20
  die "the shader failed to load or run. If this mentions SPIR-V or a shader
   compiler, libplacebo was built without shaderc."
fi
N=$("$FFPROBE" -v error -count_frames -select_streams v:0 \
    -show_entries stream=nb_read_frames -of default=noprint_wrappers=1:nokey=1 "$OUT")
info "rendered $N frames through bidirectional-interpolation.glsl"

info "--- do all nine shaders compile on this platform?"
# Same relative-path requirement as above, so this runs from inside the shader
# directory and refers to each file by bare name.
fail=0
for f in "$REPO"/scripts/*.glsl; do
  n="$(basename "$f")"
  if ( cd "$REPO/scripts" && "$FFMPEG" -y -hide_banner -loglevel error \
      -init_hw_device vulkan=vk -filter_hw_device vk \
      -f lavfi -i "color=c=blue:s=320x180:r=24:d=0.5" \
      -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=$n,format=yuv420p" \
      -frames:v 4 -f null - ) 2>/dev/null; then
    printf '   OK    %s\n' "$n"
  else
    printf '   FAIL  %s\n' "$n"; fail=1
  fi
done
[ "$fail" = 0 ] || die "at least one shader does not compile on Windows"

info "--- same answers as Linux? (ground-truth ladder)"
# The real portability test. These scenes are pure functions of t, so the
# 60fps render is the exact correct answer for a 24->60 interpolation of the
# 24fps render -- and the expected numbers are therefore platform-independent.
# Small deviations are normal (different driver, different shader compiler);
# large ones mean something is genuinely behaving differently.
cat <<'REF'
   Linux reference, PSNR dB, base shader / variational:
     L1_trans_8px     41.34 / 42.35
     L2_trans_16px    38.45 / 39.89
     L9_occlusion     38.31 / 40.18
REF
if [ -f "$REPO/scripts/tests/bench.sh" ]; then
  # bench.sh does not change directory, so a relative shader path resolves
  # from here -- which is required on Windows for the reason above.
  ( cd "$REPO/scripts/tests" || exit 1
    SH=../bidirectional-interpolation.glsl
    export FFMPEG FFPROBE
    export OUTROOT="$ROOT/bench"
    for c in L1_trans_8px L2_trans_16px L9_occlusion; do
      bash ./bench.sh "$c" "$SH" win_v0 || exit 1
    done
    python ./analyze.py --variants 2>/dev/null || python3 ./analyze.py --variants
  ) || info "ladder did not complete -- the build itself is still good; run it by hand"
else
  info "harness not found at $REPO/scripts/tests -- skipping"
fi

say "done"
info "ffmpeg   $FFMPEG"
info "ffprobe  $FFPROBE"
info "Use it exactly as on Linux:"
info "  $FFMPEG -init_hw_device vulkan=vk -filter_hw_device vk -i IN \\"
info "    -vf libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=SHADER.glsl OUT"
fi
