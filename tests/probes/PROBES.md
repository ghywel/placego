# Probes: one-off measurements that produced a recorded finding

Each directory holds the driver that made one measurement, with its method in the docstring and, where one
was written first, the pre-registered PREDICTION.md. They are kept because the record (NFRAME-LIMITS.md) quotes
their numbers and a number without its instrument is not reproducible. They are not regression tests and
`bench.sh` does not run them.

Conventions, the same as every tool in `tests/`: the repo root is derived from the script's own location; the
project ffmpeg build is found through `FFDIR` (default `$HOME/np-build/ffmpeg`) or `FFMPEG` on `PATH`; the data
they read and write -- renders, logs, tables, generated shader variants -- lives OUTSIDE the tree under
`NP_SCRATCH` (default `E:/nframe-project/np-scratch`), one directory per topic, named below. A probe run from
a machine without that data renders it afresh; one that only scores expects it to be there.

| probe | scripts | what it measured | recorded under (NFRAME-LIMITS.md) | data |
|---|---|---|---|---|
| `anchor/` | phaseprobe.py, probe.sh, picture_control.sh, eyes.sh, PREDICTION.md | the reading's measurement instant: a phase probe against the analytic derivative, before and after the held-anchor fix; the picture path as the control that must not move | The held anchor | `np-scratch/anchor/` |
| `jerk/` | jerksweep.sh | jerk against acceleration across four textured oscillations spanning jerk 8:1 -- flat 3-5:1, so truncation, not noise | Jerk is not noise-limited | `np-scratch/jerk/` |
| `snap/` | snapcheck.py, make_snap_variant.py, snap.sh, PREDICTION.md | the machine snap field scored against the analytic fourth derivative; the family's derivative ceiling | the snap and cost-table section | `np-scratch/metal-prep/snap/` |
| `median/` | ladder.sh, film.sh, outliers.sh, run2.sh, oracle.sh | the animation-pollution audit: the coarse vector medians removed from the recommendation and the full variational, on the ladder and on film; the real-content shader-selection oracle (+0.04 dB) | the pollution audit | `np-scratch/median/` |
| `ablate/` | ablate.sh, reseed.sh | the ablation ladder: the zero seed, the variational cascade and the medians each switched off against a control that reproduces the committed file | the ablation, and analyze.py's capped mean | `np-scratch/ablate/` |
| `cases/` | cluster.py | clusters the 60 proposed ladder cases from the survey into 43 mechanisms with vote counts | The synthetic pool | `np-scratch/cases/` |
| `shear/` | shear.sh, matched.sh | the gradient tensor's third component (a hyperbolic strain), then all three components on one matched construction | The gradient tensor's third component | `np-scratch/shear/` |
| `verbs/` | rolling.sh | a rolling wheel: rotation and translation locked, the small-flow floor read as a curve inside one rigid body | Verb-object pairs | `np-scratch/verbs/` |
| `weird/` | weird.py, levels.py | five non-constant fields (spiral, vortex, flag sweep, jelly, bird) read by the velocity and tensor views; the strain-rate ladder (LADDER=1, TEX=); the per-pyramid-level view that located the coarse-search wagon wheel | Weird geometry; The non-affine failure | `np-scratch/weird/` |
| `cost/` | timing.sh | the per-frame cost of every shader in the family from a file source, 720p 24->60 | the cost table | `np-scratch/metal-prep/timing/` |
| `window/` | window_rule.py | the frame-mix hook's window rule at N=3/4/5, phase by phase, the reason the N=4 window sits at [-2,-1,0,+1] | the window rule | `np-scratch/metal-prep/` |

The drivers for the private Metal app's acceptance (the reference ladder, the content pack, the family manifest,
the Metal graph verifier, the Mac-side field acceptance) live beside that app, outside this tree, because the
app is unpublished by design.
