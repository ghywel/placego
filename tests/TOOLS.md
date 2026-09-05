# The tools in this directory — read this before building another one

Twenty-five tools live here. Each exists because a specific measurement went
wrong once, and each one's docstring records the trap it was built to avoid.
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
| `analyze.py` | Summarises `bench.sh` logs. `--variants` for side-by-side. | Excludes the every-5th passthrough frames and the startup hold, which would inflate every column equally. |
| `visuals.sh` | Renders shader / truth / amplified difference for one case. | — |
| `realbench.sh` | Decimate-and-reconstruct on real footage. | Renders naturally (no `setpts`/`-r`) or the muxer re-times and duplicates. Asserts a passthrough check every run. |
| `realanalyze.py` | Summarises real-footage runs. | **PSNR rewards blur.** A linear blend can outrank a sharp but slightly-misplaced motion-compensated frame. Trust SSIM — and see `edgeerror.sh`. |
| `edgeerror.sh` / `.py` | Error AT EDGES separately from everywhere else. | **Whole-frame metrics systematically understate the defect.** Measured: whole-frame PSNR said both shaders beat linear by 2.5 dB on a segment where they were *worse than linear at edges*. If the effect you are chasing lives at edges, this is the instrument, not `realanalyze.py`. |
| `screen.sh` | Screens segments for genuine per-frame motion. | Animation on twos makes half the "reconstructed" frames duplicates, flattering every mode equally. Also a fast read on how hard a segment is: low median dB = lots of motion. |

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
| `gen_variational.py` | Generates the production `-variational` shader from the base. |
| `gen_tridirectional.py` | Generates the experimental 3-frame shader from the base. Slot-keyed, not role-keyed — see its header for why that distinction cost a round of results. |
| `gen_quaddirectional.py` | Generates the 58-pass four-frame shader from the base (imports gen_tridirectional's machinery). Both `QUAD_MODE` arms -- exact cubic and least-squares quadratic -- come from the one file. | Same silent-fallback trap as tri: a shader that fails to load leaves libplacebo on its builtin mixer and the picture still looks fine. The `TRI_DIAG` marker test is not optional. Needs FOUR frames, so it falls back at one more frame per clip edge than tri -- interior frames are the comparison, edges are not. |
| `flowvis.py` | Turns any interpolator into a flow visualiser by replacing only its final `hook()`, so what renders is exactly the flow that shader computes. |
| `trivis.py` | Four-panel view of the tridirectional fields: velocity, acceleration, correction in px, and the trust gate. Refuses to run on a 2-frame shader. |
| `accelcheck.py` | Calibrates the acceleration field against analytically known truth. Reports COVERAGE and conditional accuracy, because the field is legitimately sparse and a single average over the gaps is a category error. `FIELD=jerk` switches to the quad shader's TRI_DIAG=5 jerk field (same readback, one env var). **The truth is the DISCRETE difference, not the continuous derivative** (2026-09-01): a polynomial fit through N unit-spaced samples measures the (N−1)th finite difference — sin-attenuated on sinusoids, and for the even-order jerk anchored at the WINDOW CENTRE, which differs by host (`JERK_CENTRE`: −0.5 ffmpeg queue, +0.5 metal-demo). Comparing against continuous-at-slot-1 manufactured an oscillating ±32%-of-peak "error" whose zero-crossing was mistaken for a calibration — caught only when two hosts disagreed. See QUADDIRECTIONAL.md's CORRECTION section. |
| `manifolds.py` | Renders deterministic weird geometry with ANALYTIC per-pixel velocity: a spinning tilted torus, a tumbling Mobius band, a tesseract rotating in 4D, the Hopf fibration sliding along its fibres. Frames to a lossless file, the truth and the visible mask beside them. Ground truth for non-rigid 2D flow of rigid 3D and 4D motion, with occlusion. |
| `fieldcheck.py` | Scores a machine-read velocity frame (mode 4) against a `manifolds.py` truth: per-texel and pooled error, direction error, and the two neighbouring truth frames so a one-frame offset shows itself (at exact N:N the output is the END of its straddle interval, so output n reports the chord n-1 -> n). |
| `fieldexport.py` | Turns a rendered field into `float32` data plus a JSON sidecar carrying units, scale and an audit. This is the handover format for anything downstream. | **A 16-bit picture cannot tell you it overflowed.** A value beyond `ACCEL_DIAG_FS` comes back as exactly +/-FS and reads like a confident measurement — it cost this project a whole low-band calibration that reported "+4.000" against a true +1.917. The tool counts texels at the rail and says so loudly. Judge that count against LIVE texels, never the whole frame: a sparse field railed on 20% of its actual readings still rounds to 0.1% of the frame. || `rotcheck.py` | Calibrates the acceleration field against ROTATIONAL truth (`R2`/`R3`): per-texel vector comparison against `a(p) = alpha*J*(p-c) - omega^2*(p-c)`, reporting median vector error, magnitude ratio and angular error separately. | A median against a scalar truth -- accelcheck's statistic -- is a CATEGORY ERROR on rotation, where truth varies per texel. Also: verify the truth against the exact discrete second difference before blaming the shader; that check is what proved the R2/R3 failure was real. |

| `tieprobe.sh` / `.py` | Perturbs every argmin cost by a few ULP to expose tie-breaking fragility. Needed because a bit-reproducible platform cannot otherwise measure this at all. |
| `mvkbench/run.sh` | macOS only. Twin-kernel microbenchmark: the same kernel logic as GLSL-through-MoltenVK and as native MSL, interleaved, to test "the translation layer is the bottleneck" directly instead of asserting it. The trap it encodes: comparing *systems* conflates kernel speed, dispatch overhead, clocks and thermals -- only twin kernels separate them. Not in smoke.sh (needs Metal + swiftc; answers a platform question, not a correctness one). |
| `gen_metal.py` | Translates an mpv-hook shader into per-pass standalone GLSL + `graph.json` for the native Metal port (METALPORT.md); `--compile` drives glslc + spirv-cross to MSL. Gen-family: output is generated material, regenerated after any shader edit, never hand-edited. Asserts the SAVE/STORAGE no-overlap property its shim depends on. Verified 68/68 quad passes to working Metal pipelines. |
| `smoke.sh` | Exercises every tool here and reports pass/fail per tool. Run after building, after changing a tool, and on any new platform. |

---

## Running any of this on Windows -- the shell matters

There are **two** unrelated bash shells on this machine and they are not
interchangeable:

- **Git Bash** (`C:\Program Files\Git\usr\bin\bash.exe`) -- `$HOME` is
  `/c/Users/loki`. There is no ffmpeg here.
- **MSYS2** (`C:/msys64/usr/bin/bash.exe`) -- `$HOME` is `/home/loki`
  (= `C:\msys64\home\loki`). **The patched ffmpeg lives here**, at
  `$HOME/np-build/ffmpeg/ffmpeg.exe`, together with its build tree.

Every driver script in this directory says `$HOME/np-build/ffmpeg/ffmpeg.exe`,
so it must be run through the MSYS2 bash:

```bash
C:/msys64/usr/bin/bash.exe scripts/tests/whatever.sh
```

Two traps on top of that, both of which produce misleading failures:

1. **MSYS2 bash launched from elsewhere inherits the caller's PATH**, so the
   MSYS2 tools are not on it. ffmpeg then dies with
   `error while loading shared libraries: libplacebo-371.dll` even though the
   DLL sits right beside the exe. Every script here therefore starts with

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
not mix path styles between them.

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
