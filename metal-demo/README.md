# metal-demo — the quaddirectional shader, native

A native Swift/Metal host for the quaddirectional interpolation shader:
no ffmpeg, no libplacebo, no Vulkan. The GLSL in `scripts/` stays the
single source of truth — `gen.sh` machine-translates it into per-pass
Metal compute shaders (GLSL → SPIR-V → MSL) and this package executes
the graph with the same window semantics the libplacebo patch defines.
The port reproduces the ladder and the field calibrations through the
project's own verification tools (METALPORT.md records every phase,
prediction against outcome).

What the demo shows is the point of the whole project: not just smooth
pictures but **the field** — the acceleration and jerk overlays are the
same 68 passes read out as a measurement, live.

## Prerequisites (once)

```
xcode-select --install                # Swift toolchain, free, no account
brew install shaderc spirv-cross      # the GLSL -> MSL road for gen.sh
```

## Run it — two doors, same room

**Click:** build a double-clickable app (ad-hoc signed; runs cleanly on
the machine that built it):

```
./make-app.sh
open QuadDemo.app
```

**Terminal:**

```
./gen.sh                              # regenerate after any shader edit
swift run -c release QuadDemoUI
```

The CLI host (acceptance harness, raw export, benchmarks) is the same
engine:

```
swift run -c release QuadDemo -- --help-ish   # see main.swift header
./accept.sh                                    # ladder vs the ffmpeg pipeline
./fieldaccept.sh                               # field calibrations
```

## In the app

- **Scene**: three synthetic motion laws from the test ladder's own
  envelopes — constant velocity, constant acceleration, oscillation
  (the one that sweeps acceleration *and* jerk through their cycles).
- **Show**: Picture / Acceleration field / Jerk field. The fields are
  the product; the picture is the harness.
- **View**: Interpolated / Hold (what 24p looks like) / A/B wipe.
- **Open Video…**: mp4/mov, decoded in hardware and handed to the GPU
  zero-copy via `CVMetalTextureCache` — the path unified memory makes
  nearly free. Note: HEVC muxed by ffmpeg defaults to the `hev1` tag,
  which AVFoundation refuses; remux with
  `ffmpeg -i in.mp4 -c copy -tag:v hvc1 out.mp4` (seconds, no
  re-encode). Matroska is not supported by AVFoundation at all.
- The HUD reports the honest render rate. On a base M2, 640×360 plays
  in real time; 1280×720 and native film sizes run at whatever the 68
  passes cost — the number is the truth, not a target.

## Distributing it

Anyone can build and run from source exactly as above — no signing, no
notarisation, no App Store. A *downloaded* prebuilt `.app` hits
Gatekeeper's unidentified-developer prompt (Apple's toll on binary
distribution, not a defect here); recipients either build from source
or use right-click → Open / System Settings → Open Anyway.
