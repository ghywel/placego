# Handover: how to get up to speed and take a piece of this work

*For a person, or for an AI assistant given this file. If you are an
assistant: read this file and the documents it names in the order given,
confirm the toolchain with the checklist at the end, then stop and wait for
the human's command. Do not start an experiment you were not asked for.*

This project is CPU- and GPU-bound, not idea-bound. The open leads at the end
of this file are real, measurable, and independent of one another; anyone
with a GPU that runs Vulkan, an afternoon, and the discipline described here
can take one and bring back a number. That is the point of this document.
Written 2026-09-04; run `git log --since=2026-09-04` to see what moved after.

*What you do not receive, on purpose: the owner's memory files and scratch
directories. They are one person's working notes and one assistant
instance's accumulated context, and they are not part of this handover.
Whether you are a person or an assistant, you build your own from the
documents named below and from the runs you make: your own notes, your own
scratch, your own record of what you confirmed. Do not ask for the owner's,
do not copy them if you find them on a shared machine (a directory of
handoff notes and memory mirrors exists outside this repository for the
owner's own sessions), and do not import another assistant's memory as
your own. The repository is the shared record; everything that matters is
in it, and if something you need is not, that is a gap to report, not a
reason to reach for someone else's notes.*

## 1. What this is, in one paragraph

A patch to libplacebo (the GPU rendering library ffmpeg's `libplacebo`
filter is built on) that lets a user-supplied GLSL shader see a whole window
of source frames at once, and a family of shaders built on it that estimate,
for every point on the screen and in real time, not only where things are
moving but how their motion is changing: velocity, acceleration, and jerk.
The interpolated picture (24 -> 60 frames per second) is the harness that
made the estimate testable against exact ground truth; the field of
measurements is the product. Everything is measured before it is claimed,
and the failures stay on the record next to the successes.

## 2. Read these, in this order

1. `WHAT-WE-BUILT.md` -- the plain-language register: what exists, what it
   cannot do, what is new. Twenty minutes. Read it even if you are an expert.
2. `README.md` -- the patch (`PL_HOOK_FRAME_MIX`), documented for upstream
   review, and the map of this directory.
3. `SHADERS.md` -- every shader, what it is for, its numbers, its lineage.
4. `tests/TESTING.md` and `tests/TOOLS.md` -- the ground-truth ladder, the
   real-footage method and its traps, and every instrument.
5. `NFRAME-LIMITS.md` -- the front line. Section 9 is the current one.
6. `PLAN.md` and `../ROADMAP.md` (repository root) -- the working plan and the
   current focus.
7. `TRIDIRECTIONAL.md`, `QUADDIRECTIONAL.md`, `QUINTDIRECTIONAL.md`, `SEXTDIRECTIONAL.md` -- the
   three-, four- and five-frame experiments, hypotheses stated before the
   results. `THREEDIMENSIONAL.md` is the design record for depth from
   motion. `METALPORT.md` is the native port.
8. `METHODOLOGY.md` -- how the work was actually done, including the division
   of labour between the human and the assistant. `PRIOR-ART.md` -- where
   this sits in the scientific record.
9. `BUILDANDUSAGE.md` -- building the patched ffmpeg on Linux, Windows and
   macOS. Do this before anything below.

## 3. The method, which is not optional

These rules are why the numbers in this repository can be trusted. Results
produced without them are not comparable to the record and will be redone.

- **Ground truth first.** Synthetic scenes whose motion is a formula
  (`tests/scenes.sh`) give the exact answer at every point and instant. Real
  footage is measured by decimate-and-reconstruct (`tests/realbench.sh`),
  where the deleted frames are the exact answer. Nothing is judged by eye
  alone; the eye is used to find what to measure.
- **Predict before you run.** Write down what should happen and what would
  count as failure. The experiment documents (`TRIDIRECTIONAL.md` onward)
  show the form: a numbered pre-registration, then the results against it.
- **Instrument before science.** If a number surprises you, suspect the
  measurement before the thing measured. Half the corrections in the record
  were the instrument (a wrong truth instant, a misaligned frame pairing, a
  hook silently skipped). The bench scripts now fail loudly when the hook is
  skipped; `PL_FRAME_MIX_STRICT=1` in the environment paints such frames
  magenta.
- **Per-texel and pooled, always both.** Every calibration in the record
  pooled over the object for a week and hid a quarter-pixel per-texel bias
  (`NFRAME-LIMITS.md` section 9). Report the spread next to the median.
- **Failures stay on the record.** A refuted idea is written up with its
  numbers and its mechanism, dated, in the document it belongs to. Do not
  delete; append and mark.
- **A shipped shader is never edited for an experiment.** Copy it to scratch,
  or better, edit a copy of the two-frame base and regenerate the family
  (section 4). Compare against the shipped file *in the same run*.
- **Generated files are regenerated, never hand-edited.** Every three-, four-
  and five-frame shader and the demonstration file are produced by the
  generators in `tests/` from a two-frame base; the header of each file says
  the exact command.
- **Time everything you propose to ship, interleaved.** Run the old and the
  new alternately after a warm-up; a first measurement of "+15%" this week
  was ordering and thermal, and vanished interleaved. A change that costs
  render time ships as its own variant file or behind a switch (see
  `SUBPEL_REFINE` / `SUBPEL_SELFREF` / `ZERO_SEED` in the bases), never as an
  overwrite of the fast tier.
- **The gate for a base change** is all three: the 32-case ladder (mean up,
  no loss beyond about a decibel), the real-footage segments (PSNR and SSIM
  not down), and interleaved time. Then every regenerated file is smoked.
- **No personal data, no absolute paths, no binaries in the repository.**
  Filter strings must not contain drive-letter paths (`tests/smoke.sh`
  explains why). Scratch work lives outside the tree or is not staged.

## 4. The machinery

**The patch.** `frame-mix-hook.patch` adds the `PL_HOOK_FRAME_MIX` stage: a
`.hook`-format shader declares how many frames it wants (1-8) and receives
them with their timestamps. `frame-mix-nn-threshold.patch` lets the hook fire
at equal input and output rates (the field is measured at N:N, e.g.
`fps=24` from a 24 fps source) and sizes the frame queue for five-frame
windows. When the queue cannot fill a window the hook is skipped and the
patch says so at error level.

**The shaders** (`shaders/`). Five two-frame bases: stock, `-seeded`,
`-propagated`, `-animation`, `-variational`. The generators build the rest:

    cd tests
    ./gen_tridirectional.py  tridirectional-interpolation-propagated.glsl  bidirectional-interpolation-propagated.glsl
    ./gen_quaddirectional.py quaddirectional-interpolation-propagated.glsl bidirectional-interpolation-propagated.glsl
    ./gen_quintdirectional.py quintdirectional-interpolation-propagated.glsl bidirectional-interpolation-propagated.glsl
    ./add_human_reading.py --default 1 ../shaders/human-reading-quad.glsl   # the painted demonstration

Bare names resolve in `shaders/`; paths work too. Each generated file flips
the field-only switches on (`SUBPEL_REFINE`, `SUBPEL_SELFREF`, `ZERO_SEED`) and appends
the human-reading tail: a `read_view` shader parameter, 0 = the picture,
1/2/3 = velocity/acceleration/jerk painted for a person, 4/5/6 = the same
fields raw for a machine.

**The ladder.** `tests/scenes.sh` defines every case as an ffmpeg `lavfi`
expression; `tests/scenecheck.sh` proves each case's rendered frames match
its formula. `tests/bench.sh <case> <shader> <label>` renders 24 -> 60 and
scores the synthesised frames against the 60 fps truth; `tests/analyze.py
--variants` tabulates everything under `$OUTROOT`:

    export FFMPEG=/path/to/patched/ffmpeg FFPROBE=/path/to/ffprobe OUTROOT=/some/scratch/dir
    cd tests
    ./bench.sh L1_trans_8px ../shaders/quaddirectional-interpolation-propagated.glsl quadprop
    ./analyze.py --variants

Real footage: `./realbench.sh <video> <label> <shader> <seconds...>` then
`./realanalyze.py`. Read `TESTING.md`'s "Real-footage traps" first; the
passthrough check must pass or nothing else means anything.

**A field render** (the measurement itself), at N:N: set a diagnostic mode
and its full scale in a copy of the shader, render raw 16-bit, decode. Modes:
2 acceleration, 5 jerk, 7 velocity, 8/9 the four-frame cubic's acceleration/
jerk from the same anchor. The field is encoded as `0.5 + x * 0.5 / FS` in R
and G, px per source interval (squared, cubed):

    sed -E -e 's/const int TRI_DIAG = 0;/const int TRI_DIAG = 2;/' \
           -e 's/const float ACCEL_DIAG_FS +?= 2\.0;/const float ACCEL_DIAG_FS = 2.0;/' shader.glsl > c.glsl
    grep -q 'TRI_DIAG = 2;' c.glsl || echo "PATCH FAILED"      # always assert a sed on a shader constant
    ffmpeg -init_hw_device vulkan=vk -filter_hw_device vk -f lavfi -i "$(source tests/scenes.sh; scene A5_accel_tex_a067 24)" \
           -vf "libplacebo=fps=24:frame_mixer=custom_n:custom_shader_path=c.glsl" -pix_fmt rgb48le -f rawvideo seq.raw
    OUT_FPS=24 SRC_FPS=24 tests/accelcheck.py A5_accel_tex_a067 seq.raw 10 2.0

`tests/rotcheck.py` scores rotation against a vector truth, `fieldexport.py`
writes a field with its units and an audit for handover to other software
(the jerk-null floor in the record was read with a scratch script over
`accelcheck.py`'s decode; a per-texel standard deviation over the object's
interior, median over frames). The painted view is the same render
with the `read_view` default changed in the parameter block at the end of
the file (the bare number after `//!MAXIMUM 6`), output to images.

**New scenes** need no new code: `_rect` and `_blobt` in `scenes.sh` take
their position and angle as expressions in `T`, so a textured box moving on
the diagonal or a disc at a fixed angle is one line, and `scenecheck.sh`
proves it.

## 5. The front line, as of 2026-09-04

Section 9 of `NFRAME-LIMITS.md` carries the measurements behind each of
these. Pick one; state your prediction; measure the shipped shader the same
way in the same run.

1. **Textured diagonal cases for the ladder.** Every textured case moves
   along x, which hid a blind spot for a week: on the diagonal the coarse
   level's point-sampled Moire locks periodic texture to a lattice copy.
   Add an X-series (a periodic and an aperiodic box on the diagonal at a
   fractional and an integer coarse-texel speed, and one at 30 degrees),
   check them with `scenecheck.sh`, run the family through them, and put
   the table in `TESTING.md`. Cheap, and it makes the harness see what the
   disc showed.
2. **The zero seed shipped, as `ZERO_SEED`, with its aperture gate.** A
   fourth seed at zero in the 1/8 passes, gated by Moire evidence, a cost
   margin, a boundary discount and a structure-tensor aperture test (the
   register's oldest open lead, now built): +0.23 dB ladder mean, footage
   unchanged, +3.9% time, off in the two-frame bases and on in every
   generated field shader. Six passes and their gates are in section 9.
   What remains is items 3 and 4, and the disc's rim beyond the 1/8
   level's 16 px reach.
3. **The fractional-shift period lock.** A matching window smaller than the
   texture period cannot tell copies apart at a fractional shift of that
   level, and no scoring after the integer search can undo its choice. The
   condition is stated; the remedy (a larger or multi-scale window, or a
   period estimate) is not built.
4. **The oblique-texture residual.** After the self-referenced fit the
   per-texel velocity noise is 0.13 px on axis-aligned texture and 0.20 at
   0.36 rad. A sweep over texture angle at fixed translation would map it;
   the per-axis fit on a diagonal valley is the first suspect.
5. **The quint's estimator choice per texel.** The quartic's acceleration
   carries 34% more noise than the cubic's by construction and pays for it
   where the truncation correction is not needed; modes 8/9 give the cubic
   from the same anchor. A per-texel choice rule is unbuilt.
6. **A trust channel for machine readers.** Modes 4-6 hand a machine the
   raw field; the check verdicts that the shader already computes are not
   yet exported alongside it.
7. **More hardware, more footage.** Five consumer GPUs, 720p and 1080p, a
   handful of clips. Any new platform's ladder and field calibrations are
   worth having; `tests/smoke.sh` first, then the ladder, then a table in
   `README.md`'s hardware section.
8. **Ports.** The Metal port exists (`METALPORT.md`, `tests/gen_metal.py`)
   and is the only native port the owner intends to make; the ladder and
   the field calibrations are the acceptance numbers for any other.
9. **The engine's cost, and what is left of it.** The obvious move --
   converting the hot passes to `//!COMPUTE` with shared-memory tiles --
   was measured and refuted: correct within 0.05 dB and slower (+13% on
   the two-frame base, +9% on the quad), and a 4.5x cut in texture taps
   was bit-identical and no faster. The engine's time is dispatch count,
   not taps. Pass fusion followed from that and shipped on 2026-09-04:
   each A->B pass carries its B->A twin, one dispatch instead of two,
   -4 to -8.5% across the family (`SHADERS.md`, "What fusion buys").
   What is left is the search arithmetic -- about 21 ms per frame on the
   quad, six pairs of it -- and that is an algorithm question. Two traps
   are asserted in the tooling because both cost an evening: a bound name
   that nothing saves or declares disables the whole hook at run time
   with no compile error, and a storage image cannot stand in for a
   texture the pipeline re-saves across a Jacobi iteration.
10. **A scale-aware generator: the resolution half exists.** Every rule
   in the tracker is in pixels and frames; a 4K, 72 fps render of the
   rotating disc showed the consequences (`NFRAME-LIMITS.md` section 9,
   `WHAT-WE-BUILT.md`). `tests/scale_shader.py` scales a two-frame picture
   shader's pyramid to a larger frame, and
   `bidirectional-interpolation-variational-4k.glsl` is its product,
   measured (SHADERS.md, "the 4K shader"). The tool takes the field
   shaders too, and the 4K disc through the scaled quad gets its velocity
   map back (NFRAME-LIMITS.md section 9). Not done: a ladder at 4K for a
   field shader before one ships, and the frame-RATE half -- a stride
   through the frames for the field at high rates, so the motion of
   interest is sampled six to ten times per cycle; the disc's acceleration
   at 72 fps is what that half is for.
11. **The second witness.** The GPU is the test base; a software Vulkan
   implementation (Mesa lavapipe) is the cross-check that every ladder
   number is arithmetic and not a driver: the 2026-08-31 ladders agreed to
   0.05 dB. Today's shipped changes have not yet had that check; re-apply
   the current hook patch there, rebuild, run the propagated line's ladder,
   and record the agreement.

## 6. Bringing a result back

One experiment per commit. The message states the prediction, the numbers
against the shipped shader from the same run, the three gates if a base
changed, and the mechanism if one was found; a refuted idea is a valid
result and gets the same treatment in the document it belongs to. Regenerate
every generated file after a base change and smoke each one (`bench.sh` on
one translation case and one acceleration case is enough to catch a broken
bind). Tables in the documents are dated; when your change moves published
numbers, add a dated note next to the table rather than editing it silently.

## 7. Traps that cost hours

- ffmpeg's `-frames:v`, `lavfi` durations (`d=`) and the first output frame:
  at N:N the first frame's window is short and the hook is skipped there by
  design; drop frame 0 from any field measurement.
- The human-reading demonstration file paints the field, so it cannot be
  PSNR-scored; that is expected, not a failure.
- On Windows/MSYS2 the patched ffmpeg exits silently when its DLL directory
  is not on `PATH`; a shell whose `PATH` starts with the MSYS (not mingw64)
  binaries loses exported variables such as `OUTROOT`. `tests/smoke.sh` has
  the rest.
- A `sed` on a shader constant must be asserted with a `grep` afterwards;
  column-aligned constants defeat exact-match patterns and the render then
  silently runs at the default.
- Never compare a per-texel number with a pooled one; never compare a
  spin-up scene's number with a constant-rate scene's; never time A-then-B.

## 8. First hour

1. Build per `BUILDANDUSAGE.md`; run `tests/smoke.sh` with `FFMPEG` and
   `FFPROBE` set. Every tool must report pass.
2. Run one ladder case with the shipped propagated quad and confirm the
   number in `SHADERS.md` (L1 and A5 are quick).
3. Render one field at N:N and decode it with `accelcheck.py`; confirm the
   calibration figure in `QUADDIRECTIONAL.md`.
4. Switch `read_view` to 1 on a copy and look at the painted velocity on
   `R3_rot_tex`; a clean hue wheel means the pipeline is yours.
5. Stop. Report what you confirmed, and wait for the command.
