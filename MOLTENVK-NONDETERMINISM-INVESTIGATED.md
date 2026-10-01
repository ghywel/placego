# MoltenVK nondeterminism, investigated

> **Status (2026-10-01).** Solved for measurement on MoltenVK 1.4.2. The two switches are set by default in
> `tests/mvk-env.sh`, which the main harnesses source (section 8). Verified at the bit level on the M5 only (section 7);
> the Intel Mac's RX 6600 at the ladder level (2026-09-30, section 6) and its UHD 630 by the pendulum's dropout count
> (section 5). No reduced test case has been written for MoltenVK's maintainers (section 10). Related records:
> [ENERGY-TRANSFER.md](ENERGY-TRANSFER.md), where the pendulum of section 4 was read, and
> [NFRAME-LIMITS.md](NFRAME-LIMITS.md), whose entry of 2026-09-19 gave an earlier reading of the wander (see the note
> after section 2). `np-scratch/` (section 9) is a private working folder, not part of this repository.

**Short answer: solved, with two of MoltenVK's own switches.** On macOS the same shader, the same binary and the
same input gave different pictures from one run to the next. The cause is not in this project's shaders or patch,
and not in Apple's GPUs or the Metal driver as such. It is two separate hazards inside MoltenVK's translation of
Vulkan to Metal, one on Apple GPUs and one on AMD and Intel GPUs. Each has a MoltenVK switch that removes it:

    MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS=0                    # the Apple GPU (measured on the M5)
    MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE=1    # the AMD RX 6600 and the Intel UHD 630

With both set, the M5's ladder repeats itself on 40 of 42 cases and is within 0.01 dB on all 42, where before it
agreed on 2 to 4 cases and drifted by up to 6 dB. At the bit level, the interpolators' gross wander is gone: none
in 120 renders, against most renders before. The cost is 1-2 percent of a run.

What remains is small and has a name. libplacebo's default blue-noise dither sometimes renders a whole run one or
two levels off (62-68 dB), and very rarely a single texel differs by one level (about 96 dB). Neither moves a ladder
score at the hundredth. With `dithering=ordered_fixed` as well, the recommendation and the player's High tier are
bit-exact: 32 renders of 32. The single texel was seen once in 48 renders, in the base interpolator.

The switches are set by default for every harness here (`tests/mvk-env.sh`). This document is the record of how
they were found, so that the numbers can be re-earned and the wrong turns are not taken twice.

## 1. The symptom

The project measures interpolation shaders against a ground-truth ladder of synthetic scenes (`tests/bench.sh`,
[tests/TESTING.md](tests/TESTING.md)). On Linux and Windows a ladder run is exactly reproducible. On macOS it was
not.

**2026-08-30, the Intel MacBook Pro** (macOS 15.7.9, MoltenVK 1.4.2). The same render twice, compared exactly with
`-f framemd5` rather than through a PSNR rounded to two decimals:

| path | frames differing out of 60 | magnitude |
|---|---|---|
| `fps=60`, no Vulkan at all | **0** | -- |
| stock `frame_mixer=linear` | 1 | negligible |
| a trivial one-pass custom hook | 1 | negligible |
| the interpolator | 9-14 | up to 39 dB |

The worst deviation grew with the distance of the GPU's memory from the CPU: the RX 6600 in a Thunderbolt enclosure
39.11 dB (14 of 60 frames), the internal Radeon Pro 560X 10.48 dB (1 of 60), the integrated UHD 630 1.80 dB (3 of
60).

**The amplifier** was found then: block matching picks an argmin over candidate offsets, and at a near-tie a
one-bit difference flips the chosen motion vector and the whole warp built on it. That part was ours. It was fixed
with a tie margin (`TIE_MARGIN`; `tests/tieprobe.sh`), which takes a perturbation of arithmetic size down to almost
nothing on a reproducible platform. But the source of the perturbation was not ours, and the tie margin cannot
absorb a perturbation that is not small.

**2026-09-19, the M5:** the ladder wandered in the propagated family (the shaders that carry flow across frames).
The same command scored L1 68.39, 68.67 and 69.84. The practice became "best of three runs" for every Mac number,
which costs three times the time and still leaves a spread.

**2026-09-30:** it wandered outside the propagated family too. The plain bidirectional flipped between two values
on one case, and moved by up to 0.3 dB on others.

## 2. What it was not

Each of these was tested, not assumed:

- **Not the flow cache.** With all twelve cache reads forced off, so every frame recomputes from scratch, the
  interpolator was just as nondeterministic (14 of 60 frames, 41.76 dB worst; 2026-08-30).
- **Not a missing barrier that validation can see.** 180 frames under `VK_LAYER_KHRONOS_validation` with
  synchronisation validation active reported zero `SYNC-HAZARD`. Validation checks API usage, not that the driver
  honours it, so this did not clear the driver.
- **Not persistence across frames.** The plain bidirectional, which keeps nothing between frames, also wandered on
  the RX 6600 (identical on 5 of 42 cases, up to 1.0 dB).
- **Not the shaders, by audit:** no shared memory and no barriers (every pass is a fragment pass); every in-pass
  read of a storage image is at the invocation's own coordinate; every cache is written before it is read; no
  float atomics.
- **Not GPU arithmetic as such:** the native Metal engine of this project's apps runs the same graphs and was
  exact to the hundredth from the start.
- **Not a property of the shaders' maths:** on Linux the same shaders, the same pins and the same ladder are
  identical run to run.

*2026-10-01: [NFRAME-LIMITS.md, "The cadence branch"](NFRAME-LIMITS.md#the-cadence-branch-the-prize-taken-inside-the-window-and-the-two-things-it-cannot-know-2026-09-19-afternoon)
(2026-09-19) placed the M5's wander in the propagated family's storage-cached flow. The cache-off test above
(2026-08-30, the Intel Mac) and the plain bidirectional's wander (section 1, 2026-09-30) argue against that, and
sections 5-6 name the two MoltenVK hazards that account for it.*

## 3. The Linux witness

On 2026-09-30 a third machine joined: a NAS with an Intel Arc A310, running the same build (ffmpeg ff2059a,
libplacebo c42968d, the same patches) in a Debian container on Mesa. Two ladder runs of the recommendation were
identical to the hundredth on all 42 cases. So the wander belonged to the macOS path, and the Arc became the place
to gate a shader in a single run.

The Intel Mac's RX 6600 through MoltenVK wandered more than the M5 (two runs agreed on 3 of 42 cases, up to 3.8
dB). The wander followed MoltenVK across GPU vendors. It was not a property of Apple's GPUs.

## 4. The clue: a pendulum

The energy-transfer work read a 120 px pendulum bob moving 14-18 px a frame. On the M5 the read speed dropped out
to 35-60 percent of the truth on a few frames per run, on DIFFERENT frames each run, always fast ones. On the Arc it
never did. Random in time, gross in size and gated by speed: the signature of a race, not of rounding. The dropout
count per run made a cheap, sensitive instrument, far faster than a ladder.

*2026-10-01: the pendulum is ENERGY-TRANSFER.md's investigation 1.4:
[Results: 1.4 in simulation, the pendulum's energy](ENERGY-TRANSFER.md#results-14-in-simulation-the-pendulums-energy-2026-09-30),
where the dropouts were first recorded.*

## 5. The sweep (pre-registered)

MoltenVK has its own environment switches. Before the sweep ran, two predictions were written down:

- **M1:** one synchronisation switch (synchronous submits, or the heap switch) would take the dropouts to zero on
  both GPUs.
- **M2:** fast math off would change nothing.

Dropouts per run, 4 runs per setting:

    setting                  M5           RX 6600
    default                  5 2 6 3      3 0 3 3
    synchronous submits      5 4 6 6      2 0 2 0
    heaps off / on           1 2 5 1 /    2 0 1 0 /
                             5 5 3 5      0 4 2 1
    fast math off            0 1 0 0      1 0 2 1
    argument buffers off     0 0 0 0      3 1 0 2

Both predictions MISSED, and the miss was the finding. Synchronous submits changed nothing, so this is not queue
synchronisation. On the M5, `MVK_CONFIG_USE_METAL_ARGUMENT_BUFFERS=0` removed the dropouts. Argument buffers are
how MoltenVK binds resources on Apple GPUs, which points at resource binding or residency. Fast math off reduced
them but did not end them.

More runs, 8 per setting:

    setting                               M5                  RX 6600
    default                               6 6 7 6 5 5 6 4     0 1 2 2 0 0 1 2
    fast math off                         1 2 1 0 0 0 0 1     0 1 0 1 1 1 4 0
    argument buffers off                  0 0 0 0 0 0 0 0     1 1 1 0 1 0 0 2

- **On the M5, argument buffers off gave zero dropouts in all 12 runs**, against a mean of 5.6 per run by default.
- **The RX 6600 was untouched by it.** A separate cause.

The RX 6600's own sweep, 8 runs per setting:

    default                                                  0 1 2 1 2 2 0 1
    MVK_CONFIG_PREFILL_METAL_COMMAND_BUFFERS=1               0 1 2 1 4 2 2 0
    MVK_CONFIG_MAX_ACTIVE_METAL_COMMAND_BUFFERS_PER_QUEUE=1  0 0 0 0 0 0 0 0
    MVK_CONFIG_USE_COMMAND_POOLING=0                         0 1 1 0 0 2 7 0
    MVK_CONFIG_SHOULD_MAXIMIZE_CONCURRENT_COMPILATION=0      1 1 0 0 2 1 2 3

**One active command buffer per queue ended the RX 6600's dropouts:** 0 in 8 runs against 10 in 8 by default. The
AMD path raced across command buffers in flight at once, and serialising them removed it. The Intel UHD 630, a
second non-Apple GPU, agreed: 1.1 dropouts per run by default, 0 in 8 with one command buffer.

## 6. The ladder, solved

Each ladder run twice, the recommendation (`bidirectional-interpolation-variational-propagated`), 42 cases:

    host      switches                                        identical r1/r2   max |r2 - r1|
    M5        default                                         2-4 of 42         3.1-6.1 dB
    M5        argument buffers off                            29 of 42          1.59
    M5        argument buffers off + one command buffer       40 of 42          0.01  (all 42 within 0.05)
    RX 6600   default                                         3 of 42           3.80
    RX 6600   one command buffer                              41 of 42          0.90  (one case)
    Arc       (Linux, Mesa; nothing to set)                   42 of 42          0

- **The M5 needed both switches.** Argument buffers off removed the gross failures. The second source, removed by
  one command buffer, is most plausibly the same race the AMD GPU shows on its own.
- **The cost is 1-2 percent of a ladder run** (M5 6:24 against 6:15; RX 6600 8:37 against 8:27).
- **Across platforms the numbers still differ a little:** M5 against the Arc, 24 of 42 cases within 0.05 dB and 37
  within 0.3. That is different compilers on different GPUs, each now self-consistent. Gate against the same host.

## 7. At the bit level (2026-10-01)

The ladder result is a PSNR to the hundredth. The original finding was at the bit level, and
[BUILDANDUSAGE.md](BUILDANDUSAGE.md#macos) named re-running it as the outstanding test. Done on the M5 (macOS
27.0.1, MoltenVK 1.4.2, ffmpeg ff2059a, libplacebo c42968d) with `tests/probes/mvk/repeatpairs.sh`. Each case and
path was rendered 8 times with MoltenVK's defaults and 8 times with the switches, interleaved, and each render
reduced to a signature (the md5 of its frames' md5s). Each odd render was then measured against the majority:
frames not bit-identical, and the worst PSNR between them. The paths are the original ones (stock linear, a
one-pass hook, the base interpolator) plus the recommendation (`rec`) and the Cadence player's High tier (`high`,
the default since 1.0.4).

Renders identical to the majority, out of 8; then what the others were:

| case | path | MoltenVK defaults | with the switches |
|---|---|---|---|
| L0_static | linear | 7; 1 whole-render (68 dB) | 7; 1 whole-render (68 dB) |
| | smoke | 7; 1 whole-render (66 dB) | 7; 1 whole-render (66 dB) |
| | base | 8 | 8 |
| | rec | 5; 1 whole-render, **1 gross (2 frames, 42 dB)**, 1 small | 7; 1 whole-render (68 dB) |
| | high | **3; 3 gross (all frames, 47 dB)**, 2 of a second state | 7; 1 whole-render (68 dB) |
| L7_textured_large | linear | 7; 1 whole-render (63 dB) | 8 |
| | smoke | 7; 1 whole-render (62 dB) | 7; 1 whole-render (62 dB) |
| | base | 5; 2 whole-render, **1 gross (2 frames, 26 dB)** | 6; 1 whole-render, 1 single texel (97 dB) |
| | rec | **1 -- eight different renders, gross (4-38 frames, 26-30 dB)** | 7; 1 whole-render (63 dB) |
| | high | **1 -- eight different renders, gross (34-60 frames, 24-27 dB)** | 5; 3 whole-render (63 dB) |
| M2_period40 | linear | 8 | 5; 3 whole-render (63 dB) |
| | smoke | 7; 1 whole-render (62 dB) | 7; 1 whole-render (62 dB) |
| | base | 5; **2 gross (all frames, 20 and 49 dB)**, 1 small | 5; 3 whole-render (63 dB) |
| | rec | **1 -- eight different renders, gross (10-60 frames, 30-34 dB)** | 7; 1 whole-render (63 dB) |
| | high | **1 -- eight different renders, gross (26-60 frames, 34 dB)** | 7; 1 whole-render (63 dB) |

- **The gross wander is gone.** With MoltenVK's defaults the recommendation and the High tier never repeated a
  render on moving content: eight runs, eight different pictures, each wrong on up to all 60 frames at 24-34 dB.
  That is the 2026-08-30 finding again, now on Apple silicon. With the switches, nothing in 120 renders came within
  sight of that.
- **Two small residuals remain, in both settings.**
  - **A whole-render variant:** every frame one or two levels off (62-68 dB, mostly in chroma). It has the SAME
    signature whether the switches are on or off, so it is a second fixed state, not noise. It comes in about one
    render in six, in stock `linear` and the one-pass hook as well. So it is not ours, and it is not the hazard the
    switches remove.
  - **A single texel,** one level off on one frame (96-97 dB), seen once in the base interpolator.

**The whole-render variant is libplacebo's blue-noise dither.** libplacebo dithers its 8-bit output, by default from
a blue-noise lookup texture. Stock linear on L0_static, with the switches, 40 renders per dither method
(`tests/probes/mvk/dithervariants.sh`):

| dithering | renders: majority / odd |
|---|---|
| `blue` (the default; a lookup texture) | 37 / 3 |
| `ordered_fixed` (computed, no texture) | 40 / 0 |
| `none` | 40 / 0 |

Zero in 40 for both texture-free methods, against about 1 in 13 with the texture, is about 0.2 percent by chance.
How the lookup texture comes to exist in two states is not isolated. Most plausibly its upload or generation
races its first use, which would be the same family of hazard as above, in libplacebo's path rather than ours.

With the switches AND `dithering=ordered_fixed`, the interpolators on the two moving cases:

| case | path | MoltenVK defaults | with the switches |
|---|---|---|---|
| L7_textured_large | base | 4; **4 gross (2 frames, 26 dB)** | 7; 1 single texel (96 dB) |
| | rec | **1 -- eight different renders, gross (7-23 frames, 25 dB)** | **8, bit-exact** |
| | high | **1 -- eight different renders, gross (24-40 frames, 24 dB)** | **8, bit-exact** |
| M2_period40 | base | 6; **2 gross (2 frames, 38 and 49 dB)** | **8, bit-exact** |
| | rec | **2; six others, gross (2-8 frames, 27-47 dB)** | **8, bit-exact** |
| | high | **1 -- eight different renders, gross (28-34 frames, 33-36 dB)** | **8, bit-exact** |

**With the switches and a texture-free dither, the recommendation and the High tier are bit-exact: 32 renders of
32.** The one exception in 48 is the single texel in the base interpolator, one level on one frame. The dither
cannot touch the gross wander: without the switches it is all still there.

## 8. What to do

- **On macOS, set both switches for any measurement.** `tests/mvk-env.sh` does it. `bench.sh` sources it, and so
  do `gate.sh`, `smoke.sh`, `realbench.sh` and the field tier; the newer probes carry the same two lines.
  `MVK_DETERMINISTIC=0` opts out, for a timing run or a sweep of the switches themselves. A value already in the
  environment wins.
- **Best of three is retired** wherever the switches are set. One run is a measurement again.
- **For a bit-exact comparison** (framemd5 against framemd5), also pass `dithering=ordered_fixed` to libplacebo.
  The blue-noise variant is below 0.01 dB on any PSNR, so the ladder does not need it.
- **Older probes that call ffmpeg directly** (about 35, from before 2026-09-30) do not source the file. Export the
  two variables, or source `tests/mvk-env.sh`, before trusting a hundredth from them on a Mac.
- **Gate a shader against the same host.** The M5, the RX 6600 and the Arc each repeat themselves now, but they do
  not agree with each other to the hundredth.

## 9. Method, so the numbers can be re-earned

- The ladder: `tests/bench.sh`, each run twice, compared case by case (TESTING.md, "The Linux witness on the Arc"
  and after).
- The pendulum dropout count: `tests/probes/energy/pendulumfit.py`, swept with `tests/probes/energy/mvksweep.sh`
  (which sets `MVK_DETERMINISTIC=0`, so its "default" row is MoltenVK's default).
- The bit level: `tests/probes/mvk/repeatpairs.sh <outdir> [case...]` (`RUNS`, `PATHS`, `DITHER`), and
  `tests/probes/mvk/dithervariants.sh <outdir> [case]` (`N`, `METHODS`). Logs of the 2026-10-01 runs are in
  np-scratch/mvk-repeat/.
- Unknown `MVK_CONFIG_*` names are ignored silently by MoltenVK. A switch that "does nothing" may be a typo. Check
  the spelling against MoltenVK's `MVKConfiguration` documentation before believing a null.

## 10. What this does not claim

- **That MoltenVK's internals are understood.** The switches name where each hazard lives (argument-buffer binding
  on Apple GPUs, concurrent command buffers on AMD and Intel), not the line of code. A reduced test case for
  MoltenVK's maintainers is the natural next step; it has not been written.
- **That the bit-level result holds on the RX 6600 or the UHD 630.** Section 7 is the M5 only; the Intel Mac was
  out of reach that day. Its ladder result (41 of 42) is from 2026-09-30.
- **That other MoltenVK versions behave the same.** Everything here is MoltenVK 1.4.2. Re-test after an update:
  the switches may become unnecessary, or stop being enough.
- **That the dither residual is libplacebo's fault rather than MoltenVK's.** It is in libplacebo's path, appears
  with or without the switches, and a texture-free dither removes it. Whose hazard it is, is open.
- **Anything about the native Metal apps.** Cadence and NFrameDemo run the same shader graphs on their own Metal
  engine, not through MoltenVK, and were exact before any of this.
