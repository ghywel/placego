# The tools in this directory — read this before building another one

Fifty-eight scripts live at this level (2026-10-01; twenty-five when this file
was written), plus `mvkbench/` and the one-off measurements in `probes/`. Each
exists because a specific measurement went wrong once, and each one's docstring
records the trap it was built to avoid.
**This file is the index; the docstrings are the authority.** Read the header
of anything you are about to invoke, not just its usage line.

Written 2026-08-31 after an investigation drifted: a new prospector was built
without checking whether an existing one covered it, `screen.sh` was skipped
even though `realbench.sh`'s docstring says to run it first, and whole-frame
metrics were used where `edgeerror.sh` exists precisely because whole-frame
metrics understate the defect. Every one of those was already solved here.

---

## Pipelines — the order matters

**Synthetic ladder** (ground truth exists, no source video needed):

```
scenes.sh ──> bench.sh ──> analyze.py
     │             └─────> visuals.sh        (look at one case)
     └──> scenecheck.sh                      (after ANY scene edit)
```

**Real footage** (ground truth manufactured by decimation):

```
screen.sh ──> realbench.sh ──> realanalyze.py
                    └────────> edgeerror.sh   (the one that sees the defect)
```

Skipping `screen.sh` invalidates the rest on content shot "on twos".
Stopping at `realanalyze.py` will mislead you — see below.

**Finding where to look in a film:**

```
prospect.sh  ──> ranks by FLOW OUTLIERS      (estimator failures)
jitter.sh    ──> ranks by TEMPORAL defects   (judder the flow field cannot see)
accelprospect.sh ──> ranks by ACCELERATION   (where a 2-frame model is wrong)
        └──> clip.sh   (cut the candidate, frame-exactly)
```

---

## Ground truth and benchmarking

| tool | what it does | the trap it encodes |
|---|---|---|
| `scenes.sh` | Defines every synthetic scene. Sourced, not run. | Motion must be a pure function of `t`, or ground truth does not exist. Scenes are analytic (`geq`), not `overlay` — overlay snaps to whole even pixels. |
| `scenecheck.sh` | Asserts the 60fps render really is ground truth for the 24fps one. | **Run after any scene edit.** A misaligned benchmark does not fail, it lies. Distinguishes POSITIONAL (broken) from exact-to-rounding (fine). |
| `bench.sh` | Runs a shader over the ladder against hold/linear. | Paths inside ffmpeg filter arguments must be RELATIVE on Windows — copies the shader beside its output. |
| `analyze.py` | Summarises `bench.sh` logs. `--variants` for side-by-side. | Excludes the every-5th passthrough frames and the startup hold, which would inflate every column equally. Since 2026-09-10 it also prints a CAPPED mean (each case capped at CAP_DB, default 40) beside the raw one: a decibel at 19 dB and a decibel at 71 dB are not the same quantity, and averaging them had a component ablation come out with the wrong sign (NFRAME-LIMITS.md). Prefer the capped column. |
| `visuals.sh` | Renders shader / truth / amplified difference for one case. | — |
| `realbench.sh` | Decimate-and-reconstruct on real footage. | Renders naturally (no `setpts`/`-r`) or the muxer re-times and duplicates. Asserts a passthrough check every run. |
| `realanalyze.py` | Summarises real-footage runs. | **PSNR rewards blur.** A linear blend can outrank a sharp but slightly-misplaced motion-compensated frame. Trust SSIM — and see `edgeerror.sh`. |
| `edgeerror.sh` / `.py` | Error AT EDGES separately from everywhere else. | **Whole-frame metrics systematically understate the defect.** Measured: whole-frame PSNR said both shaders beat linear by 2.5 dB on a segment where they were *worse than linear at edges*. If the effect you are chasing lives at edges, this is the instrument, not `realanalyze.py`. |
| `screen.sh` | Screens segments for genuine per-frame motion. | Animation on twos makes half the "reconstructed" frames duplicates, flattering every mode equally. Also a fast read on how hard a segment is: low median dB = lots of motion. |
| `mvk-env.sh` | Sourced, not run: MoltenVK determinism on macOS -- Metal argument buffers off and one active command buffer per queue. `MVK_DETERMINISTIC=0` opts out (timing runs, switch sweeps); a value already in the environment wins; Linux and Windows are untouched. Sourced by `bench.sh`, `probes/masters/check.sh` and `fieldtier.sh`, and `probes/mvk/*`. | Without it a Mac ladder wandered by up to 6 dB from run to run (2-4 of 42 cases repeating); with it 40 of 42 are identical and all 42 within 0.01 dB (TESTING.md, the end). `realbench.sh`, `visuals.sh`, `scenecheck.sh`, `loop.sh`, `watch.sh`, `prospect.sh`, `jitter.sh`, `tieprobe.sh` and the older probes do NOT source it: on a Mac, `. ./mvk-env.sh` first. |
| `masters.py` | The master scenes as analytic ground truth on any host: the demo's full-frame scenes (a box bouncing under five speed laws, breathe, spin, the rolling wheel; snow, fish, planets, the roundabout) as laws of (x, y, t), exported as rgb48le source and truth at any two rates, and the per-interval field chords (`--export-field`); `--list`. Driven by `probes/masters/`. | The engine is not the truth, this file is: `probes/masters/identity.sh` holds it to the engine's exports to the last 16-bit level. |
| `bandmetric.py` | `bandmetric.py <outroot> <segment-seconds> <label>...`: `realbench.sh` outputs scored inside the MOVING BAND (texels where the two source frames differ by more than 12/255, dilated 4 px) and outside it, with the band's share of the frame. | Ghosting lives in the band; a whole-frame figure dilutes it. |
| `chamfer.py` | `chamfer.py <outroot> <segment-seconds> <label>...`: the chamfer line distance (Chen and Zwicker, ECCV 2022) between the truth's and the reconstruction's line art on `realbench.sh` outputs, and the line-pixel count ratio. | PSNR sees only luma error; a doubled or torn line shows here as distance. |
| `cel_scenes.py` | `cel_scenes.py <rigid\|walk\|walk_flat> <out.mkv> [frames=97] [fps=24]`: synthetic cel animation (flat fills, 2-px outlines, 640x360) rendered at every instant, so the odd frames of a decimated pair are the exact in-between. | On real cel footage the true in-between of a walk is a third drawing no warp can reach; here the metrics mean what they say. |

## Finding defects in material

| tool | signal | blind to |
|---|---|---|
| `prospect.sh` / `prospect.py` | Per-pixel distance from the neighbourhood MEDIAN of the flow field. Finds isolated false matches — the estimator locking onto the wrong shape. | Real motion, deliberately. A coherent field scores zero however fast it moves. |
| `jitter.sh` / `jitter.py` | The OUTPUT in time: a five-frame phase profile exposing judder. | Flow that is uniform but wrong. Complement to `prospect`. |
| `accelprospect.sh` | Acceleration magnitude from the tridirectional field — where a 2-frame model is structurally wrong. | **Caveat, measured:** ranks partly by overall motion magnitude, so it correlates with "hard segment" as well as "accelerating segment". Cross-check with `screen.sh`'s median dB before concluding. Also has no scene-cut masking, which `prospect.py` does have. |
| `clip.sh` | Cuts a frame-exact lossless clip addressed by TIME. | Seeking is not frame-exact by default; frame numbers reset after a seek. Verified by cutting two ways and requiring bit-identity. |
| `flowoutliers.py` | Isolated false-match islands in a flow field. | — |

## Shader generation and inspection

| tool | what it does |
|---|---|
| `gen_variational.py` | Generates the variational family: `gen_variational.py [S,E,Q,H iterations] [alpha] [sigma] [out.glsl] [sigma_flow] [S,E,Q,H medians] [base.glsl]` (a bare base name is looked up in `shaders/`). Switches, read from the environment, all off by default: `ZERO_SEED`, `GLOBAL_SEED`, `QZERO_MOIRE` (`QZERO_MOIRE_MIN`), `COHERENCE_GATE`, `COARSE_ENERGY` (`COARSE_ENERGY_WS`, `COARSE_ENERGY_WE`; `coarse_energy.py`), `ALIAS_PRIOR` and `ALIAS_CARRY` (`ALIAS_APERTURE`, on by default, and `ALIAS_TAU_CARRY`; `alias_carry.py`), `OUTLINE_ADOPT` (`outline_adopt.py`), `PRINT_LATTICE` (`print_lattice.py`), and `EDGE_PROP` (`EDGE_PROP_TAU`; refuted, kept as a switch). Without a switch the output is byte-identical to the form before it. The recipes of the committed files are the commands in `smoke.sh` steps 3 (`-variational`), 3c (the recommendation `-variational-propagated`: `ZERO_SEED=1 ... "0,0,8,4" 0.3 0.08 <out> 0 "0,0,2,0" bidirectional-interpolation-propagated.glsl`) and 3e (the player's default `-global-cage-energy-carry-adopt` and the `-adopt-lattice` candidate); `scale_shader.py` makes their 4K twins. |
| `gen_tridirectional.py` | Generates the experimental 3-frame shader from the base. Slot-keyed, not role-keyed — see its header for why that distinction cost a round of results. |
| `gen_quaddirectional.py` | Generates the 58-pass four-frame shader from the base (imports gen_tridirectional's machinery). Both `QUAD_MODE` arms -- exact cubic and least-squares quadratic -- come from the one file. Trap: same silent-fallback trap as tri: a shader that fails to load leaves libplacebo on its builtin mixer and the picture still looks fine. The `TRI_DIAG` marker test is not optional. Needs FOUR frames, so it falls back at one more frame per clip edge than tri -- interior frames are the comparison, edges are not. |
| `add_human_reading.py` | Appends the human-reading tail (`read_view`: painted or raw velocity, acceleration, jerk; the pooled and mode memories; the gradient tensor) to any interpolator, idempotently; the generators call it last. `read_alpha` makes the painting's opacity follow the field's magnitude: 0 (default) auto, full at the frame's running maximum; above 0 manual, full at that many px per frame; below 0 the flat painting of before. A rotating disc fades from a solid rim to a clear axis. |
| `flowvis.py` | Turns any interpolator into a flow visualiser by replacing only its final `hook()`, so what renders is exactly the flow that shader computes. |
| `trivis.py` | Four-panel view of the tridirectional fields: velocity, acceleration, correction in px, and the trust gate. Refuses to run on a 2-frame shader. |
| `accelcheck.py` | Calibrates the acceleration field against analytically known truth. Reports COVERAGE and conditional accuracy, because the field is legitimately sparse and a single average over the gaps is a category error. `FIELD=jerk` switches to the quad shader's TRI_DIAG=5 jerk field (same readback, one env var). **The truth is the DISCRETE difference, not the continuous derivative** (2026-09-01): a polynomial fit through N unit-spaced samples measures the (N−1)th finite difference — sin-attenuated on sinusoids, and for the even-order jerk anchored at the WINDOW CENTRE, which differs by host (`JERK_CENTRE`: −0.5 ffmpeg queue, +0.5 the NFrameDemo app). Comparing against continuous-at-slot-1 manufactured an oscillating ±32%-of-peak "error" whose zero-crossing was mistaken for a calibration — caught only when two hosts disagreed. See QUADDIRECTIONAL.md's CORRECTION section. |
| `manifolds.py` | Renders deterministic weird geometry with ANALYTIC per-pixel velocity: a spinning tilted torus, a tumbling Mobius band, a tesseract rotating in 4D, the Hopf fibration sliding along its fibres. Frames to a lossless file, the truth and the visible mask beside them. Ground truth for non-rigid 2D flow of rigid 3D and 4D motion, with occlusion. Since 2026-09-08 also `cube` and `cubet`: a textured cube rotating about a tilted axis (and translating), per-face affine flow, edges as aperture, self-occlusion; the first synthetic case where linear beats every shader (NFRAME-LIMITS.md). |
| `fieldcheck.py` | Scores a machine-read velocity frame (mode 4) against a `manifolds.py` truth: per-texel and pooled error, direction error, and the two neighbouring truth frames so a one-frame offset shows itself (at exact N:N the output sits ON the first frame of its straddle pair, so output n reports the FORWARD chord n -> n+1 -- measured on A5 at N:N, 2026-09-06, within 0.05 px on every frame; the two neighbouring truth frames are scored so a convention slip shows itself). |
| `loop_torus.py` | Renders a looping isometric torus whose velocity field is EXACTLY STATIONARY (it spins about its own symmetry axis: only the texture slides), three turns so the middle one is a steady loop, with the truth (the backward chord n-1 -> n, the forward chord n -> n+1 that the shaders report at N:N, their mean, the acceleration, the mask) and a zero-difference stationarity check. Options: the static shading fraction, frames per turn (80 = 19.6 px/frame at the rim, 160 = 9.8), the texture (m1 = the ladder's three sines; broad adds 84 and 170 px periods), a static textured backdrop (bg=tex, with truth/back.npy) and sensor noise (noise=sigma). The phase-locked test: every frame of the turn is a fresh reading of one field. |
| `loopfield.py` | Scores a turn of machine readings (mode 4, the exact read; `RV=rv7-x` for another folder, e.g. a reading with memory) against `loop_torus.py`'s truth as a DISTRIBUTION per 8-px cell: the hit fraction (how often the tracker is within 2 px), the single frame and the per-frame trend, the mean and its convergence, the median, the trimmed mean, the MODE (1-px histogram peak, mean-shifted; also over 3x3 cells), the oracle floor, and on a bg=tex loop the static backdrop's speckle; paints them with the shader's palette. The mean of a loop never converges on this content (the tracker reads aliases); the mode does. |
| `fieldpaint.py` | A module: paints a velocity field the way the shaders' `read_view 1` does (hue = direction, the shader's gates, over the picture at 0.35 luma), error maps, PNG out and frame decode through ffmpeg, and a cell field's upsampling. Used by `loopfield.py`. |
| `loop.sh` | The whole phase-locked test in one command: `loop_torus.py`, the exact read of the middle turn (read_view 4, `format=rgb48le` inside the graph), `loopfield.py`. `./loop.sh <name> [shade] [turn] [tex] [shader]`; about two minutes per 80-frame turn. |
| `rimprofile.py` | The silhouette-capture profile: a machine frame's reading along the truth by distance from the object's rim (bands 3-8 ... 96-131 px), on a `manifolds.py` scene. The aperture is the case: a static rim pulls the reading low within its coarse windows' reach. |
| `smallflow.py` | The small-flow floor: a machine frame's reading along the truth by \|truth\| band (0.25-3 px), per axis, on a `manifolds.py` scene; the zoom is the case. `BORDER=` leaves a frame-edge margin unscored. |
| `discaccel.py` | Scores a machine velocity or acceleration frame of the rotating disc against its analytic truth (tangential omega r / fps, centripetal omega^2 r / fps^2) by radius band: the reading along the truth, the angle, the fraction within 30 degrees. The frame-rate gate of "Lead B". |
| `middlebury.py` | Scores a machine velocity frame against a Middlebury ground-truth flow (.flo): average endpoint error, median, average angular error, the fraction within 1 px, and the zero field's floor. The external benchmark of "Lead C": the "other" set's eight sequences, fed as short videos. Its docstring scores the output frame that lands on frame11, on the reading that output n reports the chord n-1 -> n. NFRAME-LIMITS.md ("Two instrument facts first", measured on A5 at N:N, 2026-09-06) records the other convention: output n reports the FORWARD chord n -> n+1, under which the frame10 -> frame11 flow is read at the output frame on frame10. Which frame the recorded Lead C numbers used is an open question, not yet checked. |
| `tensorcheck.py` | Scores a machine gradient-tensor frame (read_view 9: divergence, curl, shear per frame) of a disc scene against its analytic divergence and curl by radius band. The two gates of "Lead E": the zoom (pure divergence) and the rotating disc (pure curl). |
| `watch.sh` | A genuine "watch this interpolated" render in one command: minutes of real footage through a shipped shader to 60 fps as a playable mp4 in the renders folder, named by the shader, never by the source. Passes the source in Windows form so paths with brackets survive the shell. Not a test. HDR sources (PQ/HLG) are tone-mapped to BT.709 SDR by libplacebo and the file tagged; without that a PQ source lands washed out in an untagged 8-bit file (2026-09-07). Output folder `HOTDROPS` (default: `hot-drops` beside the repository checkout); encoder `VENC` (default `h264_mf` under MSYS2, the encoder every render before 2026-10-01 used; `h264_videotoolbox` on macOS, tried on a short clip on 2026-10-01; `libx264` elsewhere, untried). |
| `fieldexport.py` | Turns a rendered field into `float32` data plus a JSON sidecar carrying units, scale and an audit. This is the handover format for anything downstream. Trap: **a 16-bit picture cannot tell you it overflowed.** A value beyond `ACCEL_DIAG_FS` comes back as exactly +/-FS and reads like a confident measurement — it cost this project a whole low-band calibration that reported "+4.000" against a true +1.917. The tool counts texels at the rail and says so loudly. Judge that count against LIVE texels, never the whole frame: a sparse field railed on 20% of its actual readings still rounds to 0.1% of the frame. |
| `rotcheck.py` | Calibrates the acceleration field against ROTATIONAL truth (`R2`/`R3`): per-texel vector comparison against `a(p) = alpha*J*(p-c) - omega^2*(p-c)`, reporting median vector error, magnitude ratio and angular error separately. Trap: a median against a scalar truth -- accelcheck's statistic -- is a CATEGORY ERROR on rotation, where truth varies per texel. Also: verify the truth against the exact discrete second difference before blaming the shader; that check is what proved the R2/R3 failure was real. |
| `tieprobe.sh` / `.py` | Perturbs every argmin cost by a few ULP to expose tie-breaking fragility. Needed because a bit-reproducible platform cannot otherwise measure this at all. |
| `mvkbench/run.sh` | macOS only. Twin-kernel microbenchmark: the same kernel logic as GLSL-through-MoltenVK and as native MSL, interleaved, to test "the translation layer is the bottleneck" directly instead of asserting it. The trap it encodes: comparing *systems* conflates kernel speed, dispatch overhead, clocks and thermals -- only twin kernels separate them. Not in smoke.sh (needs Metal + swiftc; answers a platform question, not a correctness one). |
| `gen_metal.py` | Translates an mpv-hook shader into per-pass standalone GLSL + `graph.json` for the native Metal port (METALPORT.md); `--compile` drives glslc + spirv-cross to MSL. Gen-family: output is generated material, regenerated after any shader edit, never hand-edited. Asserts the SAVE/STORAGE no-overlap property its shim depends on. Verified 68/68 quad passes to working Metal pipelines. EXTENDED 2026-09-08 for the whole family: `//!PARAM` blocks become live uniforms (so read_view/read_alpha/read_plate are host-settable and one graph serves the picture and every reading), `//!WHEN` is carried as `when_rpn` for the host to skip a pass on, the window (2-6 frames) and each bind's frame index are declared, and `gl_FragCoord` and `num_mix` are shimmed. All 23 shaders of the family at that date translated. The invariants are asserted by prep/verify_graphs.py, which lives beside the Metal app in that app's own tree; the tree is private and not in this repository, and its scripts find this repository through the `NFRAME` environment variable. |
| `gen_quintdirectional.py` | Generates the five-frame shader from a two-frame base (`[output.glsl [base.glsl]]`): everything the quad does plus slot 4, packing passes that keep the final pass under libplacebo's 16 binds, and the exact quartic at N:N for acceleration and jerk, degrading to the quad's cubic and the tri's quadratic where a link is untrusted or cut. The picture keeps the quad's cubic (QUINTDIRECTIONAL.md). |
| `gen_sextdirectional.py` | Generates the six-frame shader from a two-frame base (`[output.glsl [base.glsl]]`): the quint plus slot 5, and a weighted least-squares quartic whose residual (mode 6) measures the fit's own consistency. The final pass is the quint's under asserted substitutions, so the two cannot drift apart (SEXTDIRECTIONAL.md). |
| `gen_aperture.py` | Aperture-aware propagation: the first propagation pass votes by the structure tensor instead of scalar contrast (`PROP_TENSOR`). REFUTED on 2026-09-07; ships no shader. Kept as the record of the design point (NFRAME-LIMITS.md, "The aperture series"). |
| `scale_shader.py` | `scale_shader.py <in.glsl> <out.glsl> <2 \| S,E,Q,H>`: rescales a family shader for a larger frame by multiplying each pyramid level's divisor, so a level of the larger frame has the texel count the shader was tuned on (a factor of 2 keeps the same behaviour as a fraction of the screen). Makes the committed `-4k` twins. Refuses a shader with a pixel use it does not classify. `smoke.sh` steps 3b, 3d and 3e regenerate the twins and compare them byte for byte. |
| `foresight.py` | A module, imported by `gen_quaddirectional.py` (and so by the quint and sext): the foresight seed, the temporal seed mirrored in time -- a later pair's flow as one more coarse descent and 1/8 candidate. `SEED_FUT_LAMBDA` 0 (the candidate alone) is the shipped form. Every substitution is asserted to match once. |
| `coarse_energy.py` | A module: the coarse texture-energy channel as a text transform, `add(t, ws, we)`. It is `gen_variational.py`'s `COARSE_ENERGY=1`, and `probes/limb/energyvariant3.py` wraps it. |
| `alias_carry.py` | A module: `gen_variational.py`'s `ALIAS_PRIOR=1` (the frame's shift may break a local tie only if it is one of the tied answers) and `ALIAS_CARRY=1` (a semi-global min-sum carries a periodic pattern's ends into its tied interior; `ALIAS_APERTURE`, `ALIAS_TAU_CARRY`). |
| `outline_adopt.py` | A module: `gen_variational.py`'s `OUTLINE_ADOPT=1`. At the quarter level a fine periodic print whose interior locked one period away adopts its outline's motion. Needs `ALIAS_PRIOR=1` or `ALIAS_CARRY=1`. In the player's default from 2026-10-01. |
| `print_lattice.py` | A module: `gen_variational.py`'s `PRINT_LATTICE=1`. A fast fine print is re-scored at full resolution among the aliases its own lattice predicts. Needs `ALIAS_CARRY=1`. Builds the `-adopt-lattice` candidate. |
| `fielddiag.py` | `fielddiag.py [--legacy]`: the field acceptance through the picture path's TRI_DIAG diagnostic at full resolution, run on the private Metal demo's CLI (`QUADDEMO` must name it; output under `FIELDDIAG_OUT`, default `$NP_SCRATCH/fielddiag`). Cannot run without that app. |
| `smoke.sh` | 17 checks over 12 tools: `scenes.sh`, `clip.sh`, `gen_variational.py` and `scale_shader.py` (`-variational`, the recommendation, the player's default and the lattice candidate, with their 4K twins, regenerate byte-identical to the committed files), `flowvis.py`, a shader through Vulkan, `flowoutliers.py`, `prospect.py`, `bench.sh` with `analyze.py`, `visuals.sh`, `tieprobe.py`, `scenecheck.sh`. Exits non-zero on any failure. Run after building, after changing a tool, and on any new platform. |
| `linkcheck.py` | `./linkcheck.py [root]` (default: the directory above `tests/`): checks every relative link and `#anchor` in the tree's Markdown resolves inside that root, as the public copy (the contents of `scripts/`) sees it; anchors by GitHub's heading-slug rule. Prints each bad link with file and line and exits 1 if any. Run after editing any document. Trap: a link that climbs out of the tree works in the development repository and is broken in the copy, and a check run from the repository cannot see it. |

---

## Running any of this on macOS or Linux

Every tool at this level takes the build from `FFMPEG` and `FFPROBE` (default:
`ffmpeg` and `ffprobe` on `PATH`) and python from `PY`/`PYTHON` or `python3`.
On macOS, source `mvk-env.sh` first for any script that does not source it
itself (see its row above): MoltenVK's defaults are not deterministic. The
build from `../build-macos.sh` is `$HOME/np-build/ffmpeg/ffmpeg`, with numpy in
`$HOME/np-build/venv`. On Linux the build and its container are in `../linux/`
(`Dockerfile`, `build-linux.sh`); Mesa there is deterministic and needs no
switches. TESTING.md opens with the commands.

## Running any of this on Windows -- the shell matters

There are **two** unrelated bash shells on the Windows build machine and they
are not interchangeable:

- **Git Bash** (`C:\Program Files\Git\usr\bin\bash.exe`) -- `$HOME` is the
  Windows user profile (`/c/Users/<user>`). There is no ffmpeg here.
- **MSYS2** (`C:/msys64/usr/bin/bash.exe`) -- `$HOME` is `/home/<user>`
  (= `C:\msys64\home\<user>`). **The patched ffmpeg lives here**, at
  `$HOME/np-build/ffmpeg/ffmpeg.exe`, together with its build tree.

The tools at this level take the build from `FFMPEG`/`FFPROBE`
(`export FFMPEG=$HOME/np-build/ffmpeg/ffmpeg.exe FFPROBE=$HOME/np-build/ffmpeg/ffprobe.exe`)
and must be run through the MSYS2 bash:

```bash
C:/msys64/usr/bin/bash.exe scripts/tests/whatever.sh
```

The probes written 2026-09-08 to 09-10 (ablate, anchor, cost/timing.sh, jerk,
median, shear, snap, verbs) do not read `FFMPEG`: they call
`$FFDIR/ffmpeg.exe` with `/c/msys64/mingw64/bin` on `PATH`, and run only here
(probes/PROBES.md).

Two traps on top of that, both of which produce misleading failures:

1. **MSYS2 bash launched from elsewhere inherits the caller's PATH**, so the
   MSYS2 tools are not on it. ffmpeg then dies with
   `error while loading shared libraries: libplacebo-371.dll` even though the
   DLL sits right beside the exe. Put the DLL directories on `PATH` before
   running anything (the tools at this level do not do it for you):

   ```bash
   export PATH="/mingw64/bin:$HOME/np-build/ffmpeg:$PATH"
   ```

   Note the failure is a *DLL* message, which reads like a broken build. It is
   not -- it is a PATH problem, and the build is fine.

2. **Compiling** needs more than that: `make` and `gcc` come from MSYS2 and a
   plain invocation will not find them. Use a login shell with the environment
   named explicitly:

   ```bash
   MSYSTEM=MINGW64 CHERE_INVOKING=1 C:/msys64/usr/bin/bash.exe -lc 'cd $HOME/np-build/ffmpeg && make -j16 ffmpeg.exe'
   ```

   An incremental rebuild after touching one file is about a minute.

WSL is a *third* environment, with its own separate ffmpeg at
`~/build/ffmpeg/ffmpeg` (note: `build`, not `np-build`) and its own drive
mapping -- `/mnt/d/np-work` there is `/d/np-work` in both Windows shells. Do
not mix path styles between them. (2026-09-19: the WSL environment and its D:
drive no longer exist on the project's machines; this paragraph is kept for a
rebuild.)

## The failure shape this directory keeps producing

Three separate tools shipped the same bug, and it is worth naming because a
fourth will otherwise do it again.

**A path inside an ffmpeg filter argument must be relative, and must be
resolved by running from its directory.** `stats_file=`, `custom_shader_path=`
and `metadata=print:file=` are all filter *arguments*, not command arguments.
On Windows the drive-letter colon is ffmpeg's own option separator, so
`stats_file=D:/x.log` parses as an option named `D` and the error blames the
next filter in the chain. A POSIX path is no better: MSYS2 does not
path-convert inside filter strings.

**What makes it dangerous is the failure mode, not the fault.** The log is
simply never written. ffmpeg exits 0. The analysis step then finds no data and
prints an empty table, which reads as "no results" rather than "broken".
`screen.sh` printed a header and zero rows for every input on Windows and
looked like a tool reporting that nothing qualified.

So: **a tool that produces no output is a bug report, not an answer.** If a
summariser prints nothing, check for a missing log before believing the
absence of a finding. And `smoke.sh` exists to catch exactly this class —
extend it when adding a tool.

## Before adding a tool

1. Read this file and the docstrings of anything adjacent.
2. If an existing tool nearly fits, **extend it**. A new tool starts without
   the accumulated lessons — `prospect.py`'s scene-cut masking and relative
   thresholding, `realbench.sh`'s passthrough assertion — and will rediscover
   the need for each of them the hard way.
3. Add it to `smoke.sh` and to this table.

## Probes

`probes/` holds the one-off measurements the record quotes -- one directory per finding, the driver, its docstring and any pre-registered prediction -- indexed in [probes/PROBES.md](probes/PROBES.md). They read and write their data outside the tree (`NP_SCRATCH`) and derive the repo from their own location. Most find ffmpeg the way everything here does; the 2026-09-08 to 09-10 probes are MSYS2-only (see PROBES.md's conventions). Not run by `bench.sh`.
