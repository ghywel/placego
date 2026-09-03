# Methodology

How this project was actually built, and how to carry on building it.

The shaders and the patch are documented elsewhere
([README.md](README.md),
[SHADERS.md](SHADERS.md),
[tests/TESTING.md](tests/TESTING.md)). This document is about
the *process*, because the process turned out to be the more transferable
result. A working motion compensator is one artefact; a loop that can find
and fix a defect in a GPU shader in an afternoon is a capability.

It is written down because none of it is discoverable from the repository. A
reader can see the shaders and the tests; they cannot see the division of
labour that produced them, the traps that cost days, or the fact that most of
the tooling lives outside the repository entirely.

---

## 1. The three phases

### Phase 1 -- fix it at the library level, not in a script

The project started from a genuine gap. libplacebo's `frame_mixer` is a fixed
1D temporal blend kernel: it can cross-fade between frames, but it has no
concept of motion, and `custom_shader_path` hooks only ever receive a single
already-composited texture. There was no way to write a GPU shader that looks
at two frames and reasons about what changed.

The decision that shaped everything afterwards was to close that gap **in the
library**, as a new hook stage, rather than to work around it in a
multi-pass script. That is more work up front and it constrains what can be
done -- but it means every later capability is "just a shader", and the
result is something that could be submitted upstream rather than only used
locally. The patch was deliberately kept small and self-contained for that
reason.

The one substantial revision -- from a two-frame-only `tex2`/`rts_prev`
shape to the general `tex_mix[]`/`num_mix` array design -- was made *before*
anything was submitted, so from upstream's perspective there is one coherent
API, not a breaking change to justify.

### Phase 2 -- prove it with shaders that do something

A hook stage that nothing uses is a claim, not a result. So the next phase
built shaders that exercised it: first trivially, then a full
motion-compensated interpolator, then diagnostic builds that render what the
estimator is thinking rather than the final picture.

Two habits started here and paid off repeatedly:

- **Diagnostics are first-class.** Three diagnostic builds were maintained
  in deliberate lockstep with the production shader by hand for the
  project's first weeks. A diagnostic that has drifted from the thing it
  diagnoses is worse than none, so when the occlusion fallback was removed,
  all three were updated in the same commit -- and when variants arrived
  that lockstep could no longer be kept by hand, so they were retired
  (2026-09-03) for human-reading views generated from whichever shader
  they read (SHADERS.md).
- **Make invisible state visible.** The red/green `pair_changed` indicator
  meant GPU-side cache behaviour could be *seen* rather than trusted. The
  same instinct later produced the flow-field and residual visualisers that
  cracked the cartoon defect.

### Phase 3 -- hand over the render loop

This is the phase that changed the project's rate of progress, and it is the
part worth copying.

Until this point the cycle was: edit a shader, copy it to the NAS, run an
encode, copy the result back, scrub it in a player, form an opinion. That is
minutes to tens of minutes per iteration, every iteration needs a human, and
the human is the bottleneck for work that is mostly mechanical.

The fix was to build a **complete, local, GPU-free copy of the pipeline** and
hand it to the assistant:

- WSL2 Ubuntu, with Mesa's software Vulkan device (**lavapipe**, which
  reports itself as `llvmpipe`/`DRIVER_ID_MESA_LLVMPIPE`). No GPU
  passthrough, no host driver setup, no hardware at all.
- libplacebo built from a shallow clone with the patch applied, installed to
  a user-writable prefix.
- ffmpeg built against it, run directly from the build directory.
- Shaders read **live** from the real repository over the `/mnt/c` mount, so
  an edit is visible immediately with no copy step.
- Rendered frames read back over the `\\wsl.localhost\...` UNC path, so the
  assistant can look at its own output directly.

Full build details, exact flags and the reasoning behind each are recorded
separately; the important part is what it enables rather than the recipe.

Software rendering is slow, and that does not matter, because **this loop
measures correctness, not speed.** Speed is a real-hardware question and
stayed one throughout. What the loop bought was a closed cycle:

> form a hypothesis -> generate a shader variant -> render it -> *look at the
> output* -> measure it against ground truth -> keep or discard -> repeat

with no human in the middle. Iterations went from tens of minutes to a couple
of minutes, and -- more importantly -- from "a handful per session" to
"exhaustive". Several findings in TESTING.md are the result of testing six
mechanisms and refuting all six, which is simply not affordable at the old
cadence.

---

## 2. Who did what

Being precise about this matters, because the naive reading -- "the AI wrote
the shaders" -- is true and also misses why it worked.

### What the human supplied

**Direction, and the physical intuition behind it.** The single most
productive intervention in the project was the observation that this might be
a *square peg in a round hole* problem: pixel grids are square, the flow
field is square, but reality is not, and edges are almost always at odd
angles. That is not a conclusion available from the data; it is a physical
intuition about the world. It triggered a full architectural reassessment
that had not otherwise been on the table.

**Perceptual judgement.** The human eye remains meaningfully better than the
assistant's image inspection at this task. Repeatedly, a metric said one
thing and a viewer said another, and the viewer was right. The clearest case:
after three variants of an occlusion fallback were built and measured,
whole-frame SSIM marginally preferred keeping it. Direct viewing said all three
were worse than removing it entirely. Removing it was correct -- the metric
was rating the segment *containing* the artifact as the best of three,
because it could not see the defect at all. This produced a standing rule:
**a metric that cannot see the thing being judged does not get the casting
vote.**

**Problem localisation.** The highest-leverage format for a bug report here
turned out to be very specific:

> here is a clip, cut to the exact frames; the defect is at frames X to Y;
> here is what is wrong with it in words

Given that, the assistant could reliably reproduce, diagnose and fix. Given
"there is an artifact somewhere in this 60-second clip", it could not --
it would sample three moments out of thirty-five and confidently report the
wrong thing. Two rounds were lost to exactly that before the pattern was
recognised. **Cutting the clip yourself is worth more than describing where
to look.**

### What the assistant supplied

Exhaustive search, tool construction, and bookkeeping. Specifically: building
whatever measurement apparatus a question needed, generating and testing
variants in bulk, keeping the record of what had already been refuted, and
noticing when a result contradicted an earlier one.

### The division that worked

The human decided *what question to ask* and *whether the answer looked
right*. The assistant decided *how to measure it* and did the measuring. The
failures in this project came almost entirely from that boundary being
crossed in one direction: the assistant trusting a number over a viewer.

---

## 3. The method

The project leaned deliberately on the scientific method, and that is not
decoration -- several findings were only reachable that way.

### Ground truth before opinions

The founding trick of the test harness: **for a scene whose motion is a pure
function of `t`, a native 60fps render is the exact correct answer for a
24->60 interpolation of the 24fps render.** The same lavfi expression
rendered at two rates describes the identical physical scene sampled twice.

That converts "does this look smudgy" into a measurable error, needs no
source footage, and needs no GPU. For real footage the equivalent is
**decimate-and-reconstruct**: drop every second frame, interpolate them back,
and compare against the frames that were deleted.

### Always three modes, never one number

Every benchmark reports **hold** (frame duplication, no interpolation),
**linear** (stock libplacebo's blend -- what you get *without* this project),
and the shader under test. A PSNR figure alone says nothing about whether a
motion compensator is earning its complexity. Beating `hold` is trivial;
failing to beat `linear` means the whole thing is worse than doing almost
nothing.

### A ladder, not a benchmark

Test material was built as a **ladder of increasing complexity** rather than
one hard case, so a failure localises itself. Eighteen synthetic scenes:
static, translation at 8/16/23/40px per frame, low contrast, large flat
regions, large textured regions, diagonal motion, occlusion, noise, periodic
textures at two periods, a below-gate case, and four edge-specific scenes.

The point is that "it fails at 40px but not 23px" is a diagnosis, while "it
scores 34 dB" is not. The 23px case exists specifically because that is the
coarse search's reach -- the ladder is built around the implementation's own
constants so the numbers point somewhere.

### Build the metric that can see the defect

The recurring failure was frame-averaged metrics being blind to small, brief,
high-salience artifacts. Two purpose-built metrics fixed this:

- **Edge-weighted error.** A cartoon frame is mostly flat areas, where a
  wrong vector still samples the same colour and the error self-conceals,
  plus a few extremely high-contrast outline pixels where it does not.
  Measured: edges are ~15% of pixels and carry ~5x the error rate. Averaging
  over all pixels lets outline damage barely move the number while dominating
  perception.
- **Flow outlier fraction.** For every pixel, its flow's distance from the
  *median* of its neighbourhood. A genuine motion boundary is contiguous, so
  its neighbours share its value and it survives; an isolated false match is
  a local minority and does not. This metric sees false matches and ignores
  real motion -- exactly the discrimination needed -- and it is what made the
  cartoon fix measurable at all.

The general principle: when a metric and a viewer disagree, the first
question is not "which is right" but **"can this metric see the thing at
all?"**

### Refutation, and knowing when to stop

Substantial effort went into *excluding* explanations, and that was worth it.
Six candidate mechanisms for one edge-angle deficit were built and tested,
and all six were refuted -- sub-pixel resampling blur, anisotropic
regularisation, sub-pixel search quantisation, edge-aware flow upsampling,
isotropic search directions, isotropic matching aperture. The eventual cause
was something else entirely (a misfiring fallback), and the deficit was
smaller than first measured.

Two lessons came out of that:

- **Record refutations.** TESTING.md keeps them, including a section marked
  as substantially wrong with the correction beneath it rather than deleted.
  The wrong turn is part of the evidence.
- **Extreme tuning that changes nothing means the scope is wrong.** If
  pushing a parameter to an absurd value produces no effect, stop tuning and
  re-check what the parameter actually reaches. This recurred often enough to
  become a standing rule.

### Leaps, and stepping back

Not everything yields to incremental refinement. Twice the right move was to
stop and reassess the architecture:

- The realisation that the estimator was **compression-era** -- independent
  per-texel SAD searches with coherence bolted on afterwards -- while
  interpolation needs *true* motion, because content is placed at an
  intermediate position where any residual-minimising vector will not do.
  That reframing produced the variational cascade.
- The **reach principle**, arrived at independently four times before being
  named: one iteration propagates one texel, so coarse levels give many times
  the reach at a fraction of the cost. Once stated explicitly it stopped
  being rediscovered and started being applied deliberately -- the coarse
  vector medians that fixed the cartoon defect are a direct application.

The pattern for when to leap: when a series of incremental fixes each work
slightly and none work well, the model is wrong, not the parameters.

---

## 4. The toolchain

Most of the apparatus is **not** the shaders, and a good deal of it is not
even in the repository. This section is the inventory.

### In the repository: `scripts/tests/`

A complete ground-truth benchmark harness. Everything here runs on software
Vulkan and needs no GPU and, for the synthetic half, no source video at all.
**Start at [tests/TOOLS.md](tests/TOOLS.md)** -- a one-screen index of every tool,
the pipeline order they belong in, and the failure shape this directory keeps
producing. The table below is the longer form.


| file | what it does |
|---|---|
| `scenes.sh` | The synthetic ladder. Generates every test scene from lavfi expressions -- no source files. Motion is a pure function of `t`, which is what makes ground truth exist. |
| `bench.sh` | Runs a shader over the ladder against hold/linear baselines, writing per-case PSNR logs. `./bench.sh all <shader> <label>` |
| `analyze.py` | Summarises those logs. `--variants` puts every label side by side. Excludes the every-5th passthrough frames and the startup hold, both of which would otherwise inflate every column equally. |
| `visuals.sh` | Renders inspectable frames for one case: what the shader produced, what it should have produced, and an amplified difference. Point it at a debug shader to get the flow field instead. |
| `realbench.sh` | Decimate-and-reconstruct on real footage. Renders naturally to a file and forces index pairing, for reasons in the traps section below. |
| `realanalyze.py` | Summarises real-footage runs, reporting PSNR and SSIM side by side and asserting the passthrough check. |
| `screen.sh` | Screens footage for segments with genuine per-frame motion. Animation is often drawn "on twos", and frequently switches within one episode -- a segment on twos is useless for decimate-and-reconstruct, because half the "reconstructed" frames are duplicates of frames the shader was handed. |
| `edgeerror.sh` / `.py` | Reports error at edges separately from everywhere else. |
| `flowvis.py` | Turns any interpolator into a flow-field visualiser by rewriting only its final `hook()`, leaving all upstream passes untouched. |
| `flowoutliers.py` | Measures isolated false-match islands in a flow field. Probes frame dimensions rather than assuming them. |
| `prospect.py --load` | Re-ranks a saved scan without re-rendering. Scans are persisted by default: minutes of GPU time should not evaporate with the terminal, and comparing a scan before and after a shader change is how you tell whether a fix worked. |
| `jitter.sh` / `jitter.py` | Measures the OUTPUT in time rather than the flow field in space: a five-frame phase profile that exposes judder, and per-frame anomalies scored within their own phase. The complement to prospect.sh, which is blind to flow that is uniform but wrong. Also takes `--exclude`. |
| `smoke.sh` | Exercises every tool here and reports pass/fail per tool. Needs no source video. The check that the harness genuinely works on whatever platform it is run on -- it caught a WSL-only hardcoded path in the shader generator the first time it was run under MSYS2. |
| `prospect.sh` / `prospect.py` | Scans source material and ranks moments most likely to hide a defect, so a human reviews a shortlist instead of a whole film. Emits a ready-to-run `clip.sh` line for each candidate. |
| `clip.sh` | Cuts a frame-exact, lossless clip addressed by TIME rather than frame number, and verifies what it produced. |
| `gen_variational.py` | Generates the production shader from the base. Takes iteration counts, median counts and parameters as arguments, which is what makes exhaustive variant sweeps affordable. |
| `tieprobe.sh` / `tieprobe.py` | Perturbs every argmin cost by a few ULP and counts the output frames that then disagree -- how much of the result is decided by arithmetic noise rather than by the image. Exists because a bit-reproducible platform cannot otherwise measure this at all: re-running proves nothing when nothing perturbs the comparison. Reports both frame counts and worst-case dB, because a single flipped texel and a wrongly-warped frame are not the same finding. |
| `gen_tridirectional.py` | Generates the experimental 3-frame `tridirectional-interpolation.glsl` from the bidirectional base -- the base pipeline plus an anchor->outer flow chain and a quadratic (constant-acceleration) warp. Generated rather than forked so base fixes propagate. See `../TRIDIRECTIONAL.md`. |
| `accelcheck.py` | Calibrates the tridirectional shader's acceleration field against analytically known truth, in px/interval². Reads the `TRI_DIAG=2` render back at 16-bit, compares at the *fit's centre* rather than the output timestamp, and reports **coverage and conditional accuracy** rather than one average -- the field is legitimately sparse, and averaging over the texels that correctly read nothing calls a 6%-accurate field 100% wrong. |
| `trivis.py` | Renders the tridirectional shader's velocity and acceleration fields, the placement correction in px, and the confidence gate, as four separable panels. Refuses to run on a 2-frame shader. Its own docstring argues why four panels and not an extended colour wheel. |
| `scenecheck.sh` | Asserts the property the whole synthetic ladder rests on: that a scene's 60fps render really is exact ground truth for its 24fps one. Nothing else enforces it -- a scene that quietly depends on frame index still renders happily and still yields a full table of confident, meaningless numbers. Run it after adding or editing a scene. It found that `overlay` snaps its object to an even pixel, which puts an accuracy floor under every scene built that way. |

### Outside the repository: the WSL working set

Deliberately not committed -- it is scratch, and large -- but it is where
most of the actual work happened.

- **`~/build/libplacebo`, `~/build/ffmpeg`** -- the patched pipeline.
- **`~/build/shaders`** -- 56 generated shader variants at last count, the
  accumulated residue of hypothesis testing. The naming is by experiment:
  `dt_*` matching-cost variants (SAD, SSD, census, zero-mean SAD, each with
  and without regularisation), `fb_*` fallback variants, `iso_*` isotropy
  variants, `casc_*` cascade configurations, `bb_*` blend variants,
  `reach2x`, `rad1`, `nogate`. Most were refuted. **This directory is the
  record of what has already been tried**, and is worth consulting before
  proposing something.
- **`~/build/test`** -- source clips and rendered output. The clips matter:
  a 720p cartoon and a 1080p live-action feature, plus **short precisely-cut
  defect clips** (`blueydefect.mp4`, 21 frames; `headdefect.mkv`) which are
  the single most valuable test assets in the project.
- **`/tmp/interp-bench`, `/tmp/interp-real`** -- benchmark working
  directories, with baselines cached per case so a re-run only re-measures
  the shader under test.

### Proving portability, not asserting it

The patch's justification is that libplacebo is portable. That was an
argument, not evidence, for as long as it only ever ran on one distribution.
`scripts/build-windows.{ps1,sh}` build the same stack under MSYS2/mingw-w64
against AMD's proprietary Windows Vulkan driver -- a different compiler, a
different loader, a different driver, and non-POSIX paths.

The verification stage is the point of it. Checking that ffmpeg runs proves
almost nothing: with no shader loaded libplacebo silently falls back to its
builtin blend and still emits 60fps output, so a plausible frame count is not
evidence. Instead it compiles every shader, and re-runs part of the
ground-truth ladder against the values measured on Linux. Because those scenes
are pure functions of `t`, the correct answer is platform-independent, so the
numbers are directly comparable and a discrepancy means something real.

Worth noting for anyone repeating this: the patch was confirmed to still apply
cleanly to current libplacebo master before the build was attempted, which is
a five-minute check that avoids discovering a rebase is needed halfway through
a toolchain install.

**Result.** Same shaders, same patch, against a different compiler
(mingw-w64), a different Vulkan loader, and a different driver (AMD's
proprietary Windows ICD rather than Mesa lavapipe):

Re-measured 2026-08-31 after the ladder reset (see `tests/TESTING.md`), across
the whole 21-case ladder and both the base and production shaders rather than
the three cases spot-checked before:

| case | Linux (lavapipe) | Windows (Radeon, AMD ICD) |
|---|---|---|
| L1_trans_8px | 61.29 | 61.26 |
| L2_trans_16px | 41.78 | 41.78 |
| L6_flat_large | 55.53 | 55.52 |
| L9_occlusion | 39.83 | 39.83 |
| R1_rot_const | 37.30 | 37.30 |

**Maximum disagreement anywhere in the 42 measurements is 0.05 dB**, and the
one case reaching 0.08 is `L0_static`, which is the GPU round-trip ceiling
rather than an interpolation result. `hold` and `linear` baselines match
exactly. That is two entirely different Vulkan implementations -- AMD's
proprietary ICD against Mesa's software rasteriser -- two different compilers,
and two operating systems, agreeing to the second decimal. All shaders compile
and run on both.

(The pre-reset version of this table read 41.34/38.45/38.31 for the same three
cases it listed. Those numbers are not comparable with these: the ladder's
ground truth was pixel-quantised until the reset, which suppressed absolute
scores substantially. The *agreement* between platforms is the claim here, and
it held before and after.)

**What the exercise actually found** -- which is the argument for doing it at
all, since none of these were visible from Linux:

- An undocumented build dependency. libplacebo generates shader source with a
  Python/Jinja2 template step; Debian supplies it transitively, MSYS2 does
  not, and it fails partway through ninja as a bare `ModuleNotFoundError`
  naming no package.
- Absolute paths cannot appear in ffmpeg filter arguments on Windows, because
  the drive-letter colon is ffmpeg's option separator. Escaping, quoting and
  disabling path conversion were each measured and each fail.
- Paths embedded in a filter string are not path-converted by MSYS2 at all,
  so a POSIX path reaches a native binary that cannot open it. Between that
  and the previous point, only a relative path works.
- A relative path is not always enough either: MSYS2's POSIX root is
  `C:\msys64` while `/c` is a virtual mount of `C:\`, so a POSIX relative
  path spanning the two is meaningless to a native binary. `bench.sh` now
  copies the shader beside its output and refers to it by bare name, removing
  the path question entirely.
- Windows has no rpath, so the libplacebo DLL has to be placed beside the
  binary or loading fails with an unhelpful error.

The harness changes for the last two are behaviour-preserving on Linux, and
were re-verified there against the pre-change numbers before being kept.

### Generating your own inputs

Nothing in the synthetic half needs source footage. Scenes are lavfi
expressions -- `color=`, `nullsrc`, `geq`, `overlay=x='384*t'` -- which means
a new test case for a newly-suspected failure mode can be written in one
line and benchmarked immediately, with exact ground truth. When a hypothesis
needs a scene that does not exist, write the scene.

### The defect-hunting loop

The two-stage division from section 2 is now tooled, because the two halves
fail differently and the pairing is what makes it work:

> **Machine finds irregularities. Human confirms whether they are a problem
> or statistical noise.**

`prospect.sh` renders a scan through a flow-visualiser build of the
production shader and ranks moments by how badly the flow field disagrees
with itself. It is fast and literal: it detects data perturbation, which
*correlates* with visible defects without being the same thing. False
positives are expected and are the tool working correctly. What it removes is
the need to watch everything -- it turns a film into a shortlist.

A human then looks at the shortlist and decides. That judgement is not
automatable here: the eye catches visual incoherence immediately and is not
fooled by a number, which is precisely the failure mode the metrics in this
project keep exhibiting.

Its threshold is deliberately **relative** -- median plus k robust deviations
across the scan -- because what counts as a lot of outlier pixels depends
entirely on the material. Flat animation and grainy live action sit orders of
magnitude apart, so a fixed count either floods on one or goes silent on the
other. The consequence to understand: it finds the worst moments in what it
is given, not moments bad in absolute terms. Given a uniformly poor scan it
reports that and declines to rank, rather than inventing an order.

Each candidate comes with a `clip.sh` line, which closes the loop: prospect,
paste, get a verified clip, hand it over.

### Cutting the clip: three traps that look like user error

`clip.sh` exists because cutting a defect clip by hand fails for three
non-obvious reasons, each of which cost real time here:

1. **`-ss` with `-c copy` cannot be frame-accurate.** A stream copy must begin
   at a keyframe, so it snaps to one regardless of `accurate_seek`. Frame-exact
   cutting requires re-encoding, losslessly. This is the usual cause of "I
   asked for frame 1234 and got something else".
2. **Frame numbers reset after a seek.** In `select='between(n,...)'`, `n`
   counts from the first frame decoded *after* the seek, not from the start of
   the file, so a frame number read off a player does not survive being pasted
   into a filter. `clip.sh` seeks with `-copyts` and selects on absolute
   timestamps, which do survive.
3. **You read the position off the 60p output but need the 24p source.** Frame
   indices do not map between the two; time does. So the tool takes a time and
   does the conversion, printing it so it can be checked.

It verifies every cut -- exact frame count, non-black first frame, contact
sheet -- and fails loudly rather than returning a plausible-looking clip.
Proven frame-exact by cutting the same frames two ways, once with its fast
seek and once by decoding from the start of the file with no seek at all, and
requiring the results to be bit-identical.

### Building tools on demand

The pattern that made the last several fixes fast: **when a question needs an
instrument that does not exist, build the instrument.** `flowvis.py`,
`flowoutliers.py`, the edge-weighted metric and the temporal-jitter
measurement were all written mid-investigation, in minutes, because the
question demanded them. None were planned.

The enabling detail is that the instrument can reuse the production shader
wholesale -- `flowvis.py` replaces one function out of 115 passes -- so a
measurement is of the real system, not of a re-implementation that could
drift from it.

---

## 5. Traps

Every one of these produced confident, plausible, completely meaningless
numbers. They are listed because each cost real time and none announced
itself.

**Frame misalignment.** Three separate variants of this in real-footage
benchmarking, each producing a full results table. `psnr` pairs frames by
timestamp, not index, and 24000/1001 fps in a millisecond timebase does not
pair cleanly; an `fps` filter emitted an extra EOF frame that flipped
parity; a `setpts=N/TB` in a *render* step spaced frames a second apart and
`-r` filled the gaps, turning 72 frames into 1725. The fix is structural:
render naturally to a file, verify the frame count, compare with forced index
pairing, and **assert a passthrough check every run** -- the retained frames
must come back near-perfect, and if they do not, stop.

**A variant that failed to compile still produced a full table.** A global
text substitution intended for one function hit three, the shader failed to
compile, ffmpeg fell back, and the benchmark reported plausible numbers for
all of it. Compilation is now asserted per variant before benchmarking.

**Metrics blind to the defect.** Covered above; the reason it is repeated
here is that it happened more than once and is the most expensive trap in the
list.

**Reading results before the run finishes.** A log file existing does not
mean it is complete. One benchmark table was read mid-write and reported a
figure 0.3 dB off. Wait for the process to exit.

**Timing without a warm-up.** Shader compilation charged to a short render
made a change look 14% more expensive than the 6-9% it actually costs. Warm
up, and time something long enough that per-frame cost dominates.

**Stale copies.** Historically, an apparent shader logic bug that was a stale
file on the NAS. Suspect the copy before the code.

**Sampling too few frames.** Checking three moments out of thirty-five and
concluding the defect was not there. If a defect is reported in a range,
inspect the range.

---

## 6. If you are picking this up

The loop is the deliverable. To re-establish it:

1. Build the patched libplacebo and an ffmpeg against it, locally, with
   software Vulkan. No GPU needed.
2. Point it at the shaders in the repository over a live mount, so edits need
   no copy step.
3. Make sure rendered frames can be read back and *looked at* directly.
4. Run `./bench.sh all` to confirm the harness reproduces the numbers in
   TESTING.md before trusting it on anything new.

Then the working rules, in order of how much they cost to learn:

- A metric that cannot see the defect does not get the casting vote.
- Cut the clip to the exact frames before reporting a defect.
- Assert the alignment check on every real-footage run.
- Assert compilation before benchmarking a variant.
- If extreme tuning changes nothing, the scope is wrong, not the value.
- Do the work at the pyramid level where the kernel is large relative to the
  defect -- it is also where it is cheapest.
- Record refutations, including your own wrong turns, in place.
