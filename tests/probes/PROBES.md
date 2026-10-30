# Probes: one-off measurements that produced a recorded finding

## Areas

*Added 2026-10-22 in the spring clean: one row per folder, so that the 1,400-odd files here can be found. The
N-Frame table and its conventions below date from the video project (frozen on 2026-10-01; the project continues in
github.com/ghywel/n-frame). The research probes follow them in an append-only log. Every script's docstring carries
its own predictions and outcome, and `python3 tests/probes/record_find.py TERM` searches them all.*

| Folder | Files | Project | What it holds, and where its results are written up |
|---|---|---|---|
| `lexicon/` | 782 | research | Rule 30: the forced walk, the wheel, kicks, records, visible languages, the carry, sibling rules. Results in RULE30-PRIZE.md section 8, PROOFS.md and the ledgers. (It began as LEXICON.md's shader-claims checker, `lexicon_check.py`.) |
| `instinct/` | 157 | research | GPT's instinct-led lane: union-closed sets, eight-path burning (L₈ = 68), three- and four-bin partitions. Results in GPT-MATH-INSTINCT.md, FOUR-BIN-PARTITIONS.md and PROOFS.md. |
| `swarm/` | 141 | research | Swarm SW-01 of 2026-10-15 (`SW01-OBJECTS.md`, RULE30-PRIZE.md 8.113), the Erdős K2′ scripts, and the Erdős prize swarm of 2026-10-22 (`prize-20261022/`, PRIZE-SWARM.md). |
| `cloud_reads/` | 139 | research | Cloud's re-checks and censuses: four-bin H(h), top-tight cases, the one-hole boundary, Hercher's cycle bound. Results in CHAT-LEDGER.md (CL entries) and FOUR-BIN-PARTITIONS.md section 44. |
| `prizes/` | 86 | research | Collatz (most of it), Mahler, Rudin–Shapiro, Antihydra and normality probes. Results in COLLATZ-PRIZE.md, PRIZE-PROBLEMS.md and RULE30-PRIZE.md. |
| `lean/` | 19 | research | Lean 4 checks of Rule 30 results: period 1, Theorems A and B, the B lemmas, Jen's routes, the white and black ends. |
| `mahler/` | 19 | research | Mahler's 3/2 problem: the census, the window ladders, the checks of the outside Lean contribution. Results in MAHLER.md. |
| `sparks/` | 19 | research | The break room's side experiments of 2026-10-07. Results in SPARKS.md. |
| `openai_math/` | 13 | research | Replications behind CO-DISCOVERED-PROOFS.md. |
| `mathcheck/` | 4 | process | The document math check that AGENTS.md item 8 asks for before TeX is pushed. |
| this folder | 42 | research and process | 29 `rule30_gpt_*.py` probes (RULE30-GPT.md), four research audits (`eight_streets_d4_triple_basis.py`, `unavoidable_hole_audit.py`, `instinct_two_hole_*.py`), and the record's tools: `record_find.py`, `known_find.py`, `ledger_check.py`, `doc_links.py`, `proof_dupes.py`, `jobctl.py`, `idle_alarm.py`, `break_room_seed.py`. |
| `ablate/`, `anchor/`, `cage/`, `cases/`, `cost/`, `decimate/`, `dig/`, `energy/`, `jerk/`, `limb/`, `masters/`, `median/`, `mvk/`, `pan/`, `party/`, `repairs/`, `shear/`, `snap/`, `trust/`, `twos/`, `uma/`, `verbs/`, `weave/`, `weird/`, `window/` | 133 | N-Frame | The video project's measurements, in the table below; written up in nframe/NFRAME-LIMITS.md and its sibling records. (`repairs/` belongs to nframe/REPAIRS.md.) |

*The two log lines that stood above this section (GC1040, GC1041) moved, unchanged, to their place in the log beside
GC1039.*

## The probe table: the N-Frame folders (frozen 2026-10-01), then the first research rows

*Heading added 2026-10-22 (spring clean). The text below was written for the N-Frame folders, from `anchor/` to
`mvk/`; the `lexicon/` and `prizes/` rows at the end of the table are research, and later research probes are in the
log that follows.*

Each directory holds the driver that made one measurement, with its method in the docstring and, where one
was written first, the pre-registered PREDICTION.md. They are kept because the record (NFRAME-LIMITS.md) quotes
their numbers and a number without its instrument is not reproducible. They are not regression tests and
`bench.sh` does not run them.

Conventions: the repo root is derived from the script's own location. ffmpeg comes from `FFMPEG` and `FFPROBE`
(the newer probes default to `$HOME/np-build/ffmpeg/ffmpeg`, the build `../../build-macos.sh` makes; the python
scorers to `ffmpeg` on `PATH`), python from `PY` or `PYTHON`. The data they read and write -- renders, logs,
tables, generated shader variants -- lives OUTSIDE the tree under `NP_SCRATCH` (default: `np-scratch` beside the
repository checkout), one directory per topic, named below; the energy/, weave/ and mvk/ drivers take their work
directory as the first argument. A probe run from a machine without that data renders it afresh; one that only
scores expects it to be there.

**MSYS2-only.** The shell drivers written 2026-09-08 to 09-10 -- `ablate/*.sh`, `anchor/*.sh`, `cost/timing.sh`,
`jerk/jerksweep.sh`, `median/*.sh`, `shear/*.sh`, `snap/snap.sh`, `verbs/rolling.sh` -- run only in the Windows
build's MSYS2 shell. They call `$FFDIR/ffmpeg.exe` (`FFDIR` default `$HOME/np-build/ffmpeg`) with
`/c/msys64/mingw64/bin` on `PATH`, most call `python` rather than `python3`, and their `NP_SCRATCH` default is
`/e/nframe-project/np-scratch`. They are kept as they ran; on macOS or Linux, change those lines before running
one. Their python scorers (`anchor/phaseprobe.py`, `snap/snapcheck.py`, ...) are portable. None of these drivers
sources `tests/mvk-env.sh`.

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
| `cost/` | timing.sh, tiers.sh | the per-frame cost of every shader in the family from a file source, 720p 24->60; tiers.sh (2026-10-01): the player's quality tiers' costs at the size each is chosen for (the 1080p files on 1080p sources, the -4k twins on 4K ones), interleaved over rounds, on macOS and Linux | the cost table | timing.sh: `np-scratch/metal-prep/timing/`; tiers.sh: the outdir given as the first argument |
| `window/` | window_rule.py | the frame-mix hook's window rule at N=3/4/5, phase by phase, the reason the N=4 window sits at [-2,-1,0,+1] | the window rule | none (prints the table) |
| `decimate/` | decimate.sh | the hook with the output rate BELOW the source: 60->24 (ratio 2.5) and 60->30 (integer) on L1 and O5 through the recommended two-frame and the quad-propagated shaders, scored against the analytic render at the output instants; hold and linear beside | reverse interpolation | `np-scratch/decimate/` |
| `uma/` | readback.sh | the unified-memory round-trip in the record's own four chains (shader and linear, downloaded each frame against kept in Vulkan), 24->60 at a clip's native size, interleaved; the readback penalty per machine | Unified memory: the round-trip stops mattering | `np-scratch/uma/` |
| `masters/` | identity.sh, identity_diff.py, check.sh, reading.py, table.py, fieldtier.sh, diagvariant.py, fieldtable.py, hostgap.sh (with tests/masters.py) | the master tier: the demo's full-frame scenes -- bounce under five speed laws, breathe, spin, the rolling wheel, and the four complex scenes (snow, fish, planets, the roundabout) -- as analytic ground truth on any host (masters.py, held to the engine's exports to the last 16-bit level), every scene through every shader on both hosts with hold and linear beside, the table | the master tier | `np-scratch/ladder2/` |
| `twos/` | twos.sh, cadence.py, dupstat.py | content drawn on twos and threes scored against the ladder's exact truth: the scene at 24 fps, at 12 fps doubled to 24, at 8 fps tripled, and at 12 fps, through hold/linear/the recommendation/the quad, plus a duplicate dropper in front on exact and encoder near-duplicates -- the family collapses to a hold on twos (31.8 dB vs 64 on ones, L1), a dropper recovers 16-25 dB, and the quad's cadence branch (`CADENCE=1` at generation) recovers it inside the window; `cadence.py` surveys a source's cadence pattern, `dupstat.py` computes the branch's held-copy statistic offline | Content drawn on twos (2026-09-19); The cadence branch (2026-09-19) | `np-scratch/twos/` |
| `cage/` | cage.sh | the fine periodic print under a sub-pixel drift, from a film's railing: C1_cage_drift and C2_cage_drift_occluded (bars 9 px apart, 3 px wide, the scene drifting 0.5 px a frame; a figure crossing) and C3_bars_spin_drift (his suggestion: the same bars rotating about their origin while it translates -- the bars at every angle), scored on the whole frame AND the case's own rectangle -- every member of the family 6 dB below a hold there, 18 below the blend; the remedies measured and the agreement blend refuted | The cage (2026-09-21) | `np-scratch/cage/` |
| `pan/` | pan.sh | the fast pan over fine texture scored by speed band: W1/W2/W3 (a textured ground panning 8 -> 40 px per source frame under a static subject; fine noise / multiscale / alone) against the native 60 fps render -- the gradual loss from 12 px and the collapse at 36, the coarse level's Nyquist on 32-px grain; the global-motion seed's measure (`SHADERS=` the `-global` file); `dig/panspeed.py` measures a real clip's pan by phase correlation | The fast pan over fine texture (2026-09-19); The global-motion seed (2026-09-20) | `np-scratch/pan/` |
| `dig/` | dig.sh, panspeed.py | the defect funnel on real material: prospect a window, cut each candidate frame-exactly, decimate-and-reconstruct it with hold/linear/the shader, rank by the shader's margin over linear (the prospector finds estimator disagreement, not visible faults); panspeed.py: a clip's global motion pair by pair, by phase correlation | Content drawn on twos (2026-09-19), the funnel paragraph | `np-scratch/dig/<label>/` |
| `party/` | partydata.py, velocity.py, covariates.py, bleed.py, occlusion.py, motion.py, depth.py, depth2.py, torso_fit.py, groundplane.py, pointing.py, pose3d.py, PREDICTION.md (numpy) | the FIRST REAL CONTENT with an independent answer key: two hours of children at play from a live camera, the recommendation's field against Apple Vision's skeleton -- velocity by speed (the reach cliff past 24 px/frame on real bodies), the halo across moving limbs, the aperture along them, divergence and curl against rigid skeleton fits (depth), which motion wins at an occlusion, and real limbs' turning and the two- vs four-frame path error; the alignment check first; then the ground plane and a metric depth from the skeleton alone (groundplane.py), the arm pointed at the camera (pointing.py), and Apple's 3D body pose as a possible depth teacher (pose3d.py) | The field on real bodies (and THREEDIMENSIONAL.md 9.8) | `np-scratch/lillys/party-2026-09-27/` (the recording, numbers only), `np-scratch/party-analysis/` |
| `limb/` | limb.sh, repeat.sh, limblevels.py, rectlevels.py, propvariant.py, energyvariant.py, energyvariant2.py, energyvariant3.py, gate.sh, gateset.sh, gatetable.py, real.sh, timing.sh, v3phase.sh, v3edges.py, ambiguity.py, carry.py, apcarry.py, ownerdump.py, cases.sh, metalcarry.sh, PREDICTION.md (with scenes.sh K1-K3, B1) | the party's reach cliff crystallised: a textured limb sweeping a still textured wall (K1), a flat dark one (K2) and K1 with a brighter limb (K3), scored in a box following the limb, five runs each; the per-level view locating two mechanisms (the point-sampled coarse taps scramble a moving grain; the 1/8 propagation's contrast-weighted mean dilutes a small mover into a textured still background); EDGE_PROP (refuted on the ladder: the period family) and a coarse texture-energy channel (a trade; energyvariant.py the first form, energyvariant2.py the smoothed prototype, energyvariant3.py the engineering form, which wraps tests/coarse_energy.py, the code behind gen_variational.py's COARSE_ENERGY=1), each gated best-of-3 on the full ladder and on real footage (gateset.sh: any set against a named control, e.g. the player's cage); then V3, the half-period alias: its start-phase sweep (v3phase.sh), its answer band by band and cell by cell per level (v3edges.py: healed from one edge at a band per frame), and the offline ambiguity flag, a second cost basin behind a ridge (ambiguity.py: the interior flagged, the ends anchors, rare on real footage); the carry offline (carry.py, apcarry.py: the aperture-aware penalty) and in the shader, read cell by cell (ownerdump.py), a few cases between gates (cases.sh), and on Metal against libplacebo where the carry engages (metalcarry.sh) | The field on real bodies: the limb on the ladder; V3 reopened; the half-period alias in the shader; the aperture in the carry; PRIOR-ART.md, the periodic-interior survey | `np-scratch/limb/` |
| `energy/` | census.py, census_local.py, census_local_merge.py, census_runs.py, halfrate.py, collide.py, corner.py, gravity.py, heldball.py, impactdips.py, koenig.py, localphase.py, phasestep.py, placer.py, pendulum_blender.py, pendulumfit.py, pool_sim.py, pool_blender.py, poolfit.py, sphere_blender.py, spherefit.py, rotwarp.py, substep.py, twodrop.py, mvksweep.sh | the Newton's-cradle question, step by step (each docstring names its step in ENERGY-TRANSFER.md): free flight's constant acceleration (gravity.py, 1.1); the pendulum's energy (pendulum_blender.py renders, pendulumfit.py reads, 1.4); a bounce's parabolas and the unit-free T^2/h (twodrop.py, 1.5); hidden spin by Koenig's theorem (koenig.py, 2.1); a ball's 3D spin by a sphere fit (sphere_blender.py, spherefit.py, 2.3); the pool shot's slip (pool_sim.py, pool_blender.py, poolfit.py, 2.4); a rigid rotation drawn as one (rotwarp.py, 2.5); the miss distance at a wall (impactdips.py, corner.py, 3.1); the impact placer (placer.py, 3.2); collisions and the momentum ledger (collide.py, 3.3-3.4); an impact census of films and the half-rate test (census.py, census_runs.py, census_local.py, census_local_merge.py, halfrate.py, 3.6); a held ball and its hand (heldball.py, 4.1-4.2); the smallest one-frame step the field sees and phase-based bounds (substep.py, phasestep.py, localphase.py, 5.1-5.2); mvksweep.sh: the MoltenVK settings sweep on the pendulum that found the Mac's determinism switches | ENERGY-TRANSFER.md, by step number; TESTING.md, "The Linux witness on the Arc" (the sweep) | the workdir given as the first argument (`np-scratch/energy/<topic>/` by convention); census and halfrate: `CENSUS_WORK` (default `/tmp/census`), footage under `FOOTAGE` (default `/footage`) |
| `weave/` | weavesweep.py, weaveedge.py, anchors.py, flowtap.py, unwrap.py, rescore0.py, rescore1.py, rescore_disc.py, timing_adopt.sh | the weave: where the field locks one period away on a fine 2D periodic print -- a textured box translating at 2-24 px/frame, field and picture (weavesweep.py; WEAVE_FULL, WEAVE_SCALE for the 4K twins); the outline's motion carried inward (weaveedge.py); the carry's anchors at the box's edge (anchors.py); a flow tap that exposes any pass's flow to the machine read (flowtap.py); the offline unwrapping that became OUTLINE_ADOPT (unwrap.py); the fine re-score among the print's lattice aliases that became PRINT_LATTICE (rescore0.py, rescore1.py; rescore_disc.py on rotating prints); OUTLINE_ADOPT's cost (timing_adopt.sh) | The weave; ENERGY-TRANSFER.md, stages 0b-1c and lead 4 | the workdir given as the first argument; `np-scratch/weave/sweep/` and `np-scratch/energy/rotwarp/` (the re-score sources), `np-scratch/weave/timing/` |
| `trust/` | leveltap.py, flag.py, wide.py, decide.py, r3diag.py, cutstat.py, timeset.sh | the per-level trust gate (2026-10-01): every stage's flow tapped at the 1/8 grid on the weave scene (leveltap.py), which found the parked target to be the cut gate; the per-level aliasing flags on textures and film (flag.py); the first honest level's wide search and its full-resolution decision offline (wide.py, RANK=full; decide.py's ratio study); the trust gate on the ladder's rotating exact print (r3diag.py); the cut gate's motion-compensated statistic on real cuts (cutstat.py; summary mode merges runs); the interleaved time of any set of shaders (timeset.sh) | ENERGY-TRANSFER.md, "The per-level trust gate, returned to" | `np-scratch/trust/` (leveltap's sources in `t0/`, the cut study in `cut/`, the variants in `variants/`) |
| `mvk/` | repeatpairs.sh, dithervariants.sh | MoltenVK at the bit level (2026-10-01): the same render repeated with MoltenVK's defaults and with tests/mvk-env.sh's switches, grouped by whole-render framemd5 signature, on stock linear, a one-pass hook, the base, the recommendation and the player's High tier (repeatpairs.sh); the residual whole-render variant traced to libplacebo's blue-noise dither (dithervariants.sh: blue, ordered_fixed, none) | MOLTENVK-NONDETERMINISM-INVESTIGATED.md | the outdir given as the first argument |
| `lexicon/` | lexicon_check.py, rule30_periodic.py, rule30_rings.py, rule30_rigidity.py, rule30_witness.py, rule30_twosided.py, rule30_twosided_exact.py, rule30_factorial.py, rule30_factorial_compare.py, rule30_runlengths.py, rule30_linear_cell.py, rule30_siblings.py, rule30_sibling_proofs.py, rule30_harmonics.py, rule30_resonance.py, rule30_spectrum.py, rule30_spectrum_fine.py, rule30_rotation.py, rule30_wheel.py, rule30_wheel_left.py, rule30_churn.py, wheel_orbit.c, periodic_kill.c, rule30_slips.py, rule30_walls.py, rule30_formation.py, rule30_wheelspeed.py, rule30_chaos.py, ladder.c, rule30_ladder.py, rule30_ladder_deep.py, rule30_ladder_budget.py, rule30_prng.py, rule30_merge.py, bottleneck.c, rule30_bottleneck.py, realruns.c, rule30_realruns.py, rule30_triangles.py, rule30_lattice.py, rule30_mirror.py, rule30_scan.py, entropy.c, entropy2.c, rule30_entropy.py, rule30_wallkind.py, rule30_worldline.py, rule30_kickgaps.py, rule30_wake.py, rule30_metric.py, rule30_halflines.py, rule30_irrational.py, rule30_complement.py, rule30_lightning.py, rule30_diagonals.py, rule30_channels.py, rule30_maze.py, rule30_leftband.py, rule30_leftsides.py, rule30_squeeze.py, rule30_core.py, rule30_tilt.py, tilt.c, records.c, rule30_records.py, rule30_influence.py, rule30_merge.py, rule30_wall.py, rule30_words.py, rule30_race.py, rule30_uniform.py, rule30_kicks.py, rule30_kickgame.py, rule30_count.py, count.c, rule30_cost.py, count_j.c, rule30_debt.py, forced.c, forced_deep.c, rule30_night_figure.py, rule30_band.py, rule30_sync.py, rule30_records_word.py, records_word.c, rule30_leftside_million.py, rule30_otherrules.py | LEXICON.md's claims checked against line-by-line ports of the base shader (C1-C7, each with a counterfactual); periodic columns of finite Rule 30 configurations, periods 1-6, by the left-permutive inverse construction, with Condrey's published period-1 maxima as the control; the column periods of Rule 30's ring orbits; left-side rigidity, exhaustive over every column 1; the right side as a constraint on column 1, both sides exactly, the four-arm factorial, and the zero-run lengths with their templates and Lemma 3's Pell and Fibonacci counts, and Lemma 4 (where column 1's newest bit enters) with its refuted corollary P3; the instrument on Rule 30's 16 left-permutive siblings, Proposition 5 (Rule 90, by Lucas' theorem), and the owner's harmonics, Fourier and complex-number leads (ring resonance at lag 7; column 1 as a slipping rotation near 17/56); the universal wheel (an exact two-arc coding of the rotation by 17/56) and the left half it forces; the churn (order in, noise out); Proposition 6 (the pure wheel's orbit, certified) and LR for periodic columns 1 (C programs; build with cc -O2); the wheel out of step (O3), the slips as one particle, the walls' notched kicks, orbits and jumps, and where the long runs come from (formation, slips) with a glitch in the drive, the wheel's speed, whether the wheel is chaotic, and the LR_m ladder's rungs, at depth, and their cost in bits per cell, Rule 30 as a parallel random-number generator, luck against structure in the runs, the bottleneck of column 1, the white triangles and their lattice, the pyramid upwards and from two seeds, the counterexample search to 32 cells, the exact entropy bound of column 1, the wall kinds, the kicks' wakes, one figure of the night, and the morning's numbers (the metric, the two half-lines, columns as numbers, the complementary pair, the owner's lightning, the diagonals as rational numbers, the lightning's channels, the pyramid as a maze, the left band of stripes, Rowland's one left side or many, the wheel's alias, the entropy squeeze and where Problems 1 and 2 meet, the owner's matter-antimatter question, lead 1's records, the merging walks, the wall form, black white and both, the information race, one law for every word, what sets a kick, the kick game) (Cloud, 2026-10-04 and 05, CPU only); Local's from 2026-10-05: records_bits.c, records_fast.c, rule30_records_sat.py (the Enigma lead), rule30_jenclock.py with jenclock.c (Jen's theorem with a clock, §8.54), ompflags.py | LEXICON.md §4; RULE30-PRIZE.md §5, §7, §8, §8.1-§8.55 | none: everything is computed afresh and printed |
| `lexicon/` (GPT audit) | rule30_gpt_cycles.py | Inductive all-seed cycle classification through diagonal 53207; two certified first-branch cycles at 53208; worst-phase reset bounds and a failed blind birth-time check for the forced half-line | RULE30-GPT.md G2 | none: certificate constructed and checked afresh |
| `lexicon/` (GPT forced zeros) | rule30_gpt_forced.py | Forced-output parity identity, summary-closure counterfactual and conditional survival at deeper random-prefix depths; predictions in header | RULE30-GPT.md G3 | none: reconstructed afresh |
| `lexicon/` (GPT balance) | rule30_gpt_balance.py | Ordered-prefix discrepancy versus shuffled diagonals; exact power-of-two cycle balance counterexamples and local ensemble controls | RULE30-GPT.md G4 | none: constructed afresh |
| `lexicon/` (GPT reset front) | rule30_gpt_front.py | Phase-lift comparison for the conservative reset front; half-density shortcut counterexample and non-power-of-two control; pre-registration in header | RULE30-GPT.md G6 | none: constructed afresh |
| `lexicon/` (GPT waiting budget) | rule30_gpt_waiting.py | One-phase interval debt, exact parent-agreement waits and exhaustive small all-branch period trees | RULE30-GPT.md G7 | none: constructed afresh |
| `lexicon/` (GPT local front) | rule30_gpt_local_front.py | All small edge-tree interval debts and all compatible spatial-cycle exact reset-front means; domain check for a local charging potential | RULE30-GPT.md G8 | none: constructed afresh |
| `lexicon/` (GPT birth restarts) | rule30_gpt_birth_restart.py | Maximum-over-restarts identity and birth transfer of all-interval front budgets; endpoint-only counterexample | RULE30-GPT.md G9 | none: constructed afresh |
| `lexicon/` (GPT cycle obstructions) | rule30_gpt_cycle_obstructions.py | Complete small-period necessary cycle-mean audit for the uniform front potential; exact recurrent witnesses | RULE30-GPT.md G10 | none: constructed afresh |
| `lexicon/` (GPT Condrey holes) | rule30_gpt_condrey_holes.py | First-hole prefix theorem, constant-wall mechanism audit and finite-row counterexample to unchanged checkerboard | RULE30-GPT.md G11 | none: constructed afresh |
| `lexicon/` (GPT hole interactions) | rule30_gpt_hole_interactions.py | Exact four-case two-hole interaction and newest-input controls | RULE30-GPT.md G12 | none: constructed afresh |
| `lexicon/` (GPT inverse reset) | rule30_gpt_inverse_reset.py | Four-state inverse-row reset certificate and one-step-back hole shielding | RULE30-GPT.md G13 | none: constructed afresh |
| `lexicon/` (GPT white latch) | rule30_gpt_white_latch.py | Exact two-state latch/visible counts at the white end, extending the existing Fibonacci envelope | RULE30-GPT.md G14 | none: constructed afresh |
| `lexicon/` (GPT visible gaps) | rule30_gpt_gap_language.py | Exact width-one projected language for arbitrary white-time gaps; full-shift and equal-density controls | RULE30-GPT.md G15 | none: constructed afresh |
| `lexicon/` (GPT two-cell holes) | rule30_gpt_two_cell.py | Exact parity classification of the width-two one-hole visible language, with independent path and subset controls | RULE30-GPT.md G16 | none: constructed afresh |
| `lexicon/` (GPT three-cell holes) | rule30_gpt_three_cell.py | Eight-state all-period certificate: width three has exactly the width-two hole language; hidden period-four and independent projection controls | RULE30-GPT.md G17 | none: constructed afresh |
| `lexicon/` (GPT slow switches) | rule30_gpt_slow_switch.py | Latch-position finite prefix, universal black-window protected band, phase and tail-nonclosure controls | RULE30-GPT.md G18 | none: constructed afresh |
| `lexicon/` (GPT balanced latch) | rule30_gpt_balanced_latch.py | Exact balanced-wall prefix comparison, interior latch minimum, and independent finite-left seed control | RULE30-GPT.md G19 | none: constructed afresh |
| `lexicon/` (GPT four-cell holes) | rule30_gpt_four_cell.py | Sixteen-state relation and subset certificate: full odd-period hole language survives width four, with retained failed prediction | RULE30-GPT.md G20 | none: constructed afresh |
| `lexicon/` (GPT sideways map) | rule30_gpt_sideways.py | Exact inverse-column CA image/fibres, ternary recoding, induced-rule and measure controls | RULE30-GPT.md G22 | none: constructed afresh |
| `prizes/` | collatz_count.py, collatz.c, collatz_blocks.py, collatz_blocks.c, collatz_residue.py, collatz_window.py, collatz_threehalves.py | Rule 30's counting form carried to Collatz: every number of 16 to 30 bits, stopping times against Terras's coin (CZ0-CZ4); the state after the free bits, mod 2^j, and its Fourier structure against width (CB0-CB4, CS0-CS2) | COLLATZ-PRIZE.md §1 to §3 | none (exact, recomputed in seconds) |

The drivers for the private Metal app's acceptance (the reference ladder, the content pack, the family manifest,
the Metal graph verifier, the Mac-side field acceptance) live beside that app, outside this tree, because the
app is unpublished by design.


## The research probe log (append-only, newest last)

- `lexicon/rule30_gpt_shapes.py` (G23, 2026-10-06): exact width10 channel subset/transition audit against entropy2.c; cylinder/affine/Walsh controls, bit-order reversal, rejected depth13 left-record witness, dependency-free SVG. Output directory required; data outside git.

- `lexicon/rule30_gpt_tail_coding.py` (G25): leading-difference coding, slow-wall exact prefix counts, backward/forward inverses, and unexpected black-time masking. Bounded algebraic checks; no full right-half realizability assertion.

- `lexicon/rule30_gpt_210_audit.py` (G26): failed finite-word continuation, exact dyadic Rule210 empty-left trace, parity/Rule90 reduction, scalar/bit-vector and Catalan controls. No right-layer search.

- `lexicon/rule30_gpt_finite_state_scope.py` (G27): dyadic indexed DFA controls, including leading zeros. Distinguishes indexed representation from autonomous finite-state latch generation; no CA search.

- `lexicon/rule30_gpt_210_obstruction.py` (G28): global single-parity/Frobenius obstruction and exact nonlinear-residue controls. Necessary full-clock conditions; no width-survival search.

- `prizes/collatz_gpt_signed_bound.py` (G29): seeded independent signed rational W2 audit; shifted growth, open-interval parity injection, cycle/endpoint failures and exact integer count. No purported infinite orbit generated.

- `prizes/collatz_gpt_conditioning.py` (G39): exact endpoint-survival rotation and independent DP controls throughT12, short rotation orbits, and a complex-cancellation transfer counterexample. No data files generated.

- `prizes/collatz_gpt_pair_cancellation.py` (G40): independent direct-residue controls for survivor skeleton cubes, additive ternary swap differences and exact Fourier products throughT10; all-one endpoint contraction counterexample. No data files generated.

- `prizes/collatz_gpt_free_pair_mass.py` (G41): exact binomial mode and conditioning-event containment controls throughT12; independent residue control of an8-word frequency-blind cube. No data files generated.

- `prizes/collatz_gpt_unit_resonance.py` (G42): exact primitive-character/real-inverse-sum identities, explicit free-pair cube controls and an integer geometric-tail certificate; no aggregate-mass conclusion. No data files generated.
- `prizes/collatz_audit_g39_g42.py` (Local, second reader of G39 to G42): independent exact check of the cycle-lemma bound, the skeleton cube and its additivity over Q, the affine identity and the resonance family; PROOFS.md §E2, CHAT-LEDGER L007.

- `prizes/collatz_gpt_binary_reader.py` (G43): direct ternary spectrum/inversion and surviving-state binary-reader reconstruction controls, exact odd-group bias and frequency-weight scope. No data files generated.

- `prizes/collatz_gpt_information_budget.py` (G44): exact parity-tail variation, modulo2^d bijection, ensemble injectivity and persistent actual-prefix cylinder controls; distinguishes generic mixing from the stopping-time count. No data files generated.

- `prizes/collatz_gpt_actual_ceiling.py` (G45): preregistered actual-start residue/ceiling controls versus direct trajectories. Published before run; AS1-AS3 pending at initial commit.

- G45 `prizes/collatz_gpt_actual_ceiling.py` outcome: AS1-AS3 passed65520 word/width comparisons and11 finite-ceiling survivor occurrences; argument independently audited by Local L012.
- `prizes/collatz_gpt_ceiling_growth.py` (G46): preregistered exact first-deficit family/realizing-residue audit k1..256, plus short-interval rounding counterexample; KC1-KC3 NOT RUN at publication.

- G46 `prizes/collatz_gpt_ceiling_growth.py`: KC1-KC3 passed256 family cases; largest ceiling321 has no realizing residue within it; G46 argument independently audited Local L014.
- `prizes/collatz_gpt_first_deficit_return.py` (G47): preregistered divisibility/realizing-residue comparison and actual return controls; RC1-RC3 NOT RUN at publication.

- G47 `prizes/collatz_gpt_first_deficit_return.py`: RC1-RC3 passed256 cases; only realized finite candidate start1. No global cycle exclusion.
- `prizes/collatz_gpt_first_deficit_gap.py` (G48): preregistered interleaved first-deficit gap/lift controls throughlength16, returns and strict overshoots retained, zero-residue domain control. FD1-FD3 NOT RUN at publication.

- G48 `prizes/collatz_gpt_first_deficit_gap.py`: FD1-FD3 pass791 words/2373 positive lifts; finite prediction held, onlystart1 return, no strict overshoot. Affine lifting yields the horizon16 certificate, single-party awaiting independent reproduction.

- `prizes/antihydra_gpt_scope.py` (G49): preregistered floor(3n/2) coding/lift and shifted-map controls, exact counter-survival coin comparison, growing-seed halting scope check. AH1-AH4 NOT RUN at publication.

- G49 `prizes/antihydra_gpt_scope.py`: AH1-AH4 pass2047 word/lift cases,33 shift/counter checkpoints and129 rational bounds; growing seed3 halts its counter immediately. Single-party finite controls, actual seed8 unresolved.

- `prizes/mahler_gpt_scope.py` (G50): preregistered216 base-six local triples, exact rational integer/fraction scope and excluded1/2 boundary, formal100 fractional cycle versus integer congruences. MA1-MA3 NOT RUN at publication.

- G50 `prizes/mahler_gpt_scope.py`: initial MA3 phase-order failure retained; corrected MA1-MA3 pass216 triples,128 samples and12 finite congruences, with added rational multiplication control.
- `prizes/mahler_gpt_window.py` (G51): preregistered exact prefix/backward fractional-window comparison, ceil-residue midpoint trajectories,10101 exclusion. MW1-MW3 NOT RUN at publication.

- G51 prizes/mahler_gpt_window.py: MW1-MW3 pass2047 exact window comparisons and532 midpoint trajectories, including10101 exclusion. Single-party finite controls.
- rule30_gpt_period_blocks.py (G52): published MF1-MF2 controls pass50 primitive walls/288 vectors/8016 forward truth-table transitions; retains001 misalignment. Tests the finite boundary conversion, not the infinite band proof.
- `lexicon/rule30_audit_g52.py` (Local, second reader of G52): the window-matching step of Corollary F for phase-aligned period blocks on random periodic walls, and the 001 example; PROOFS.md G52 note, CHAT-LEDGER L023.
- `lexicon/rule30_audit_g53_g54.py` (Local, second reader of G53/G54): the gap-matrix squeeze's examples recomputed exactly (0^7 1 = G14's rate; roots 3, 4; 1/p; 0101's log2(phi)/2) and the 001 example; PROOFS.md G53/G54 note, CHAT-LEDGER L026.
- lexicon/rule30_gpt_ring_quotient.py (G55): preregistered RQ1-RQ3 pass10408 scalar/vector states at primes3,5,7,11,13; independently reconstructed quotient lifts equal direct cycle multiplicities; shift-CA converse control retained. No large census or data files.
- `lexicon/rule30_audit_g55.py` (Local, second reader of G55): every Rule 30 cycle on the prime rings 5 to 19 against the quotient lifting law, and the distinct-length criterion; PROOFS.md G55 note, CHAT-LEDGER L027.

- lexicon/rule30_gpt_ring_phase.py (G56): preregistered moment-phase covariance, independent lexicographic classes and direct return-displacement controls; free composite-orbit guard. PH1-PH3 NOT RUN at publication.

- G56 lexicon/rule30_gpt_ring_phase.py: PH1-PH3 pass10398 nonconstant states, independent lexicographic classes/direct return displacements, and the free composite-orbit guard. Nonzero-drift mechanism remains open.

- lexicon/rule30_gpt_ring_drift.py (G57): published DC1-DC3 pass10395 phase-drift comparisons,8 quotient-cycle coordinate-change controls, and mass/moment checks on constant-output cases. Retains7/11 zero sums; no nonzero-drift theorem.

- lexicon/rule30_gpt_one_parity.py (G58): OP1 passes26 masks/6656 scalar versus bit-vector transitions; OP2 passes3354 exact Catalan/dyadic checks; Rule30 counterfactual refuted197914 cell comparisons. Predictions published at57adc80 before run.
- `lexicon/rule30_audit_g58.py` (Local, second reader of G58): Rule 210 from an empty left row on one-parity walls with holes: parity invariant, wall equation, sigma(odd) = 0, the dyadic filter, and the Rule 30 counterfactual; PROOFS.md G58 note, CHAT-LEDGER L033.
- `lexicon/rule30_audit_g59.py` (Local, second reader of G59): Rule 90's Frobenius zero blocks on finite rows and the period-3 scope guard; PROOFS.md G59 note, CHAT-LEDGER L034.

- lexicon/rule30_gpt_full_parity.py (G60): FR1 pass26 walls/13312 centre checks; FR2 pass13286 neighbor/filter comparisons; all26 fixed16-bit truncations refuted at33..43, analytic white-block guard checked; site1 inverse guard passes256 bits. Predictions published at6a706a9 before run.

- lexicon/rule30_gpt_right_gates.py (G61): RG1 pass8 triples/32 pairs,5 accepted; RG2 pass4096 indices; arbitrary invisible-bit CF refuted; deeper nonlinear guard passes. Predictions at82e86c0.

- lexicon/rule30_gpt_pair_support.py (G62): NG1 pass32 Dirichlet patches,8 even-pair guards; NG2 pass4096 indices; odd-pair CF refuted. Predictions published at8648f02; no full-clock assertion.

- lexicon/rule30_gpt_strip.py (G63): ST1 pass7 pairs/1792 words/15 accepted; ST2 pass120 phase values/118 adjacent pairs; no-margin CF refuted. Predictions at7eb8431; local layer scope.

- lexicon/rule30_gpt_window_complexity.py (G64): WC1 pass196608 windows/3952 early/192656 late; WC2 pass2524 forced samples with482 excluded. Predictions atb917fb4; analytic entropy limit separate.

- lexicon/rule30_gpt_mirror.py (G65): MX1 pass32 masks/8224 clock/parity checks; MX2 pass256 prefixes and exact factor counts1..8; mixed-parity mirror CF refuted. Predictions at7026fff.

- lexicon/rule30_gpt_bounded_perturbation.py (G66): BP1 pass16416 trace comparisons/14304 next-power zero checks; BP2 pass62432 forced samples,33760 excluded. Predictions at4ad587c; infinite-cone scope preserved.

- prizes/collatz_gpt_barrier_offset.py (G67): OB1 passes791 first-deficit words/10 nonzero classes with unique intercept maxima; OB2 passes256 exact constructions. Conditioning guard0011 retained. Predictions at7cc1b4b; no residue-realization claim.

- prizes/collatz_gpt_barrier_residue.py (G67): RB1 audits791 existing words, gap-max rankings disagree in classes4..10; RB2 audits256 extremizers, only n1 cycle survives. Predictions at8bb27ab; exact a4 ranking counterexample retained.

- prizes/collatz_gpt_endpoint_certificates.py (G68): EC1 passes791 equal endpoint lift counts/1 survivor; EC2 passes25358 congruences plus nesting/soundness/completeness. Both certificates exclude extremizers a2..256; partial-sufficiency guard refuted. Predictions atcd53b87; optional data output stays outside git.
- prizes/collatz_gpt_logarithmic_ceiling.py (G69): LF1 passes256 exact inequalities; LF2 passes791 first-deficit words/1 independently evolved survivor and coarse cutoffs. Predictions at68a8d88; finite application audit, not a proof of Rhin.
- `lexicon/rule30_audit_g60_g66.py` (Local, second reader of G60 to G66): the Rule 210 right-realization and strip chain checked independently (full Rule 210 runs, exhaustive local tables, template and localization checks); PROOFS.md notes, CHAT-LEDGER L035, L036.
- `prizes/collatz_audit_g67_g69.py` (Local, second reader of G67 to G69): first-deficit maximizers to length 24, endpoint identities and certificates to length 20, the cited-bound consequences to a = 2000; PROOFS.md notes, CHAT-LEDGER L037.

- prizes/collatz_gpt_count_bridge.py (G70): HC1 passes131072 start/horizon pairs and384 interval counts; only n1 discrepancies. HC2 exact linear-horizon criterion switches at width104 in2..256. Predictions at068b3f8; only horizon1 directly samples the guaranteed-equality region.

- prizes/collatz_gpt_boundary_loss.py (G71): BT1 passes507 parents/12 exact first-bit rows with both signed discrepancies; BT2 passes171 recurrences/117 rational ratios/54 zero steps. Lift parity-sign guard refuted. Predictions at86d2d06; no hazard-debt bound.

- prizes/collatz_gpt_terminal_fibres.py (G72): FM1 passes507 admitted starts/507 distinct terminals; FM2 passes4563 future statuses/108 weighted counts. Unrestricted three-start collision guard retained. Predictions atefce02c; no sampled admitted collisions or empirical entropy estimate.

- prizes/collatz_gpt_terminal_fibres.py --short-labels (G72 addendum): FM3 passes507 sharp bounds/spans/labels, including4 modulus1 starts; unrestricted625/597 guard reproduced. Predictions atfc268ed; no admitted collision sampled.

- prizes/collatz_gpt_tail_labels.py (G73): AT1 passes2313 admitted samples/fibres and27 empty ensembles; AT2 reproduces the9/13 odd-count guard. Predictions at773b424; no admitted collisions or empirical entropy measurement.

- prizes/collatz_gpt_backward_weights.py (G74): BW1 passes180 horizons/1740 increments, including516 empty parents; BW2 independently matches440 demand weights. Predictions at4a78c0b; noncritical-only guard retained, no cancellation bound.

- prizes/collatz_gpt_weight_atoms.py (G75): WA1 passes2036 reverse identities/57 tails/1304 atom comparisons, all1304 atom bounds vacuous at T<=10; WA2 passes257 exact binomial inequalities. Predictions at51a1a0e; dependence counterfactual refuted, no empirical decay evidence.

- prizes/collatz_gpt_signed_budget.py (G76): SA1 passes180 cases;148 opposite-sign cases,18 zero-net and57 empty-final cases retained. SA2 HELD, positive-count cancellation factor2155/88 at width10,T20. Predictions at961ed39; finite diagnostic, no uniform law.

- prizes/collatz_gpt_coin_proxy.py (G78): PC1 passes164 exact proxy/moment identities,8 empty tails; PC2 passes32 strict linear-horizon bounds and the four-word guard. Predictions at14fde39; coin DP only, no actual allocation measurement.

- prizes/collatz_gpt_weighted_bias.py (G79): SB1 passes168 weighted/12 zero-proxy cases; largest supported bias131072/6167 has weight6167/1953628. SB2 reproduces epsilon-4 guard. Predictions at343dbb1; no asymptotic mean-bias estimate.

- prizes/collatz_gpt_mixed_curvature.py (G80): MP1 passes2925 interior mixed blocks,257 surviving boundary blocks retained; MP2 passes180 final counts with killed and empty cases. Predictions ata4645cf; boundary counterfactual refuted, no aggregate curvature bound.

- prizes/collatz_gpt_offset_codes.py (G81): CI1 passes68722 complete position-set comparisons/4403 admitted words at a1..12, no residue collision; CI2 HELD. Predictions at9a9a46d via050f51c. Exact finite cutoff via reduction, not an all-a theorem; witness branch unexercised.

- prizes/collatz_gpt_window_smoothing.py (G82): LW1 passes163872 exact window identities/364 convolution-TV controls; all35 geometric comparisons vacuous. LW2 passes257 exact gradients and two nonvacuous arithmetic points. Predictions at42e96b1; no demand-distribution measurement or actual-start run.

- prizes/collatz_gpt_forced_spacing.py (G83): FS1 passes64 exact spans/63 recurrences, first span>=4 at a21; FS2 passes4403 existing admitted words. Predictions ate9b1213. Monotonicity plus exact R20<4 excludes admitted collisions through a20; horizon1 counterfactual refuted, no extended code enumeration.

- prizes/collatz_gpt_prefix_orientation.py (G84): PF1 passes10 attained prefix-extrema pairs/4401 existing words; PF2 verifies exact a21 span and directional bound. Predictions at4c2e796; signed counterfactual refuted, no a21 collision search.

- prizes/collatz_gpt_prefix_slack.py (G85-G86): FP controls pass 256 pairs, 64 admitted lower prefixes and 192 exclusions; SR verifies full/shifted admission and fresh deficit 26. Predictions at 2a8df48 via aab6d7d. Both counterfactuals refuted; no collision search.

- prizes/collatz_gpt_sixth_branch.py (G87): PB1 passes eight attained extrema pairs/4396 existing words; PB2 exact budget and affine guards pass. Predictions at da98314; correction counterfactual refuted.
- prizes/collatz_gpt_collision_tree.py (G88): CB1 passes six direct comparisons/722 prefix extrema and three unrestricted witness controls. CB2 complete a = 21 tree: 59 nodes, 30 pruned, no leaves. Predictions at da98314; separate residue-cover audit pending.

- prizes/collatz_gpt_cover_audit.py (G88): RC1 passes 30 disjoint rejecting classes covering 2^33 residues; RC2 rejects three corruptions. BN1 REFUTED at a = 22: complete 647-node tree finds five validated pairs; 23–24 not run. Predictions at 6c69d5e. Data outside Git, accepting-cover audit pending.

- prizes/collatz_gpt_accepting_cover.py (G89): RC3 passes 319 rejected classes plus five accepting residues covering 2^34; all first meetings at 34. Root-span and corrupted-acceptance controls pass. Predictions at ca9d765; no counts 23–24 run, independent model review pending.

- prizes/collatz_gpt_terminal_pooling.py (G90): TC1 passes two admitted trajectories and four enumerated coin continuations; literal and demand-weighted changes agree, pair total 1/2. Equal-terminal cancellation counterfactual refuted. Predictions at 23c22c2; no full-population estimate.

- prizes/collatz_gpt_coalescence_weights.py (G91): CM1 passes 30 horizons/100 increments, retaining 21 empty parents. CM2 passes true pair, synthetic multiplicities and independently enumerated -1/2 lost-child guard; counterfactual refuted. Predictions at 8e6dfee; actual unmatched mass remains open.

- prizes/collatz_gpt_demand_shape.py (G93): DS1 passes 36 independently enumerated profiles; DS2 HELD over 2080 exact profiles through T64, no log-concavity failure or support gap. Independent-shift convolution counterfactual refuted. Predictions at ebc2ee3 via 3add022. Finite coin evidence only, no shape theorem or actual allocation bound.

- prizes/collatz_gpt_demand_edge.py (G94): BC1 passes 28 independent boundary operators (19 critical, nine noncritical); BC2 verifies synthetic deficit -1/32 and critical ordinary averaging. Generic preservation counterfactual refuted. Predictions at fea12c1 via 5854db3. Actual demand edge inequality remains open.

- prizes/collatz_gpt_threshold_shape.py (G95): NS1 passes 126 independent laws and unrestricted guard; NS2 NOT RUN, zero schedules, superseded by L048 before execution. Revised run plan at 588c530. No all-length shape or allocation theorem.

- rule30_gpt_moving_frame.py (G96): MC1 passes 504 ring rows/1512 transported cases; MC2 passes derivative-dynamics guard and 168 dyadic checks. Autonomous Rule210 derivative evolution counterfactual refuted. Preregistered at e2c6a02. Scope identities only, no single-seed statistical theorem.

- rule30_gpt_spatial_ensemble.py (G97): SC1 passes 2040 input words, four preimages/output; SC2 passes 32 neighbourhoods and counts 16/16/24. Constant-row guards pass. Preregistered at a233f59. SC3 temporal independence controls remain NOT RUN and unpublished.

- rule30_gpt_temporal_ensemble.py (G97 SC3): passes 30 paths and 9360 initial words, uniform sampled/flip vectors and exact flip-count moments. Right-step guard gives3/4. Preregistered at5bb1aac. Fair random-row ensemble only; G98 DC1-DC2 remain NOT RUN.

- rule30_gpt_clock_guards.py (G98): DC1 passes169 diamonds, including grid5 versus area2; DC2 verifies left seed edge through12 and distinct raw update orders. Predictions5bb1aac, instrument published through806cfec. No physical metric or asynchronous-statistics claim.

- rule30_gpt_versioned.py (G99): VP1 passes680 initial words and two schedules, all node values agree; mixed-generation guard refutes intermediate-frame equality. Preregistered through827e006; known dependency scheduling only.
- rule30_gpt_right_flip.py (G100): RF1 passes64 six-bit words, both origin bits and two formulations. Histogram [1,3,5,7,3,9,7,29], lag-two covariance1/32 and count variance5/8. Preregistered through827e006; exact short-horizon fair ensemble, no single-seed or interior-ray claim.

- rule30_gpt_interior_flip.py (G101): IF1 passes512 initial words, exact factorized histogram, four-flip variance7/8 and second/fourth covariance1/32. Predictions and instrument through7773c41. Speed3/4 fair-row ensemble only; no single-seed or long-run variance inference.

- rule30_gpt_race_chains.py (G102): CI1 passes43680 word/flag combinations and48 exact weighted checks. Finite right recurrence/remainder, left injection1/2 and adjacent-race guard agree. Preregistered through84d09c9; first-row open-terminal model only.

- rule30_gpt_clean_cone.py (G103): CP1 passes77440 histories and192 weighted site bounds; clean cone forces agreement, final-target-only guard fails. Preregistered through43095bf. Coupling bound on target/mean disagreement, no matching rate or realised hitting-time theorem.


**G104 OM1-OM2 outcome (2026-10-06 20:07 BST).** After8753ab0, rule30_gpt_oriented_measure.py passes2720 fixed-tail right cases with an independent inverse,10880 left cases and48 exact weighted moments. Fair densities coexist with left first-step pair bias1/2+eps/4. Finite anchored eps1 controls do not extend the infinite theorem to nonterminating chains. No scaling rerun.

- rule30_gpt_zero_ring.py (G105): ZR1 passes43648 row/flag/direction cases and40 exact weighted probabilities afterf0f3a1b. Right zero-row preimages2; left1 or2 according to effective flags. Absorbing-zero and cyclic-coalescence guards pass. No long-run invariant law or rate inferred.

- rule30_gpt_raced_temporal.py (G106): TF1 passes43648 old-word/flag cases and60 weighted flip means afterd05bb6b. Left/stay1/2; right finite recurrence and remainder agree. Infinite eps1 excluded; no temporal independence or survival inference.

- rule30_gpt_raced_trace.py (G107): NT1 passes135296 word/path/schedule cases and8736 conditional pivot classes aftere779bd0. Samples/flips uniform; mean T/2,var T/4. Zero-flag histories agree with independent synchronous XOR/OR updates. No finite-ring, adaptive or selected-seed claim.

- rule30_gpt_trace_coupling.py (G108): CT1 passes135296 paired cases and8736 conditional classes after85f0972. Both trace projections bijective; masks depend only on past ideal prefixes. Four-input E1=1-I0 guard passes. Conditional support counts supply entropy; no unconditional information or survival law.

- rule30_gpt_error_echo.py (G109): afterf9aa008, EH1 passes32 local kernels; EH2 passes128 initial words,16 injections all101, masks{1} and{-1,1} eight each. Independent XOR damage propagation agrees. No repeated-race or global survival claim.

- rule30_gpt_pulse_memory.py (G110): PM1 passes128 words afterf922142. Each current ideal-bit bin has8 previous injections and56 noninjections; E3=E1. Both marginal trace laws uniform. Paired first-order Markov equality fails in this pulse model; repeated-iid table belongs to Local.

- rule30_gpt_split_polynomial.py (G111): PC1-PC3 pass12 exact determinant controls after d8d67d1. Independent flag-history weights agree with coefficient expansion; half-rate equality/quarter-rate failure guard passes. No production table duplicated.

- rule30_gpt_white_shield.py (G112): WH1-WH3 preregistered NOT RUN;672 effective one-step cases, two finite-cylinder controls and a left-reading counterfactual guard. Publish before execution.

- rule30_gpt_white_shield.py (G112 outcome): WH1-WH3 pass after38eda50;672 effective one-step cases, both finite-cylinder traces and independent XOR/OR control, left-reading orientation counterfactual refuted. Infinite conclusion depends on the proof, pending independent review.

- rule30_gpt_lagged_memory.py (G113): LM1-LM3 preregistered NOT RUN;8192 isolated-pulse histories, exact two-step state audit and uniform seven-sample marginal control. Publish before execution.

- rule30_gpt_lagged_memory.py (G113 outcome): after2589f4f, LM1/LM3 pass8192 words and uniform seven-sample marginals. LM2 split prediction HELD:8 unequal refinements,16 parents,36 children; zero child0/896 versus parent40/1872. Order-two closure refuted at tick5 in pulse model only.

- rule30_gpt_lagged_cylinders.py (G113 LM4): preregistered NOT RUN;extract two13-bit pulse witnesses and independently check all eight padded histories before a cylinder claim.

- rule30_gpt_lagged_cylinders.py (LM4 outcome): after832c0d3, two explicit13-bit cylinders and all8 independently implemented padding checks pass. Success0011110010000 gives ideal0110000/noisy0011001; zero patch gives both0000000. No whole-row zero assumption.

- rule30_gpt_damage_channels.py (G114): DP0-DP2 preregistered NOT RUN;64 exact local identities, hand-derived pulse rows and black-centre autonomous-Rule90 guard. Publish before execution.

- rule30_gpt_damage_channels.py (G114 outcome): after9e09890, DP0-DP2 pass64 identities, the three explicit cone rows and black-centre guard. Two healed source ticks conceal neighbour-error cancellation; no stochastic closure inferred.

- rule30_gpt_injection_state.py (G115): IS0-IS2 preregistered NOT RUN;8192 pulse words, injection-plus-one-lag state versus full history, with an unexpected shallow-refinement control. Publish before execution.

- rule30_gpt_injection_state.py (G115 outcome): after114a83c, IS0 passes8192 words;IS1/IS2 HELD with24 full-prefix splits and0 K3-only splits. First witness0/20 versus40/80; injection-plus-one-lag state insufficient in pulse model at tick5.

- rule30_gpt_pulse_parity.py (G116): PE0-PE2 preregistered NOT RUN;512 four-tick words, gated ideal-triple parity and a shallow-average/older-bit counterfactual guard. Publish before execution.

- rule30_gpt_pulse_parity.py (G116 outcome): after241fb49, PE0-PE2 pass512 words,64 injections and32 fourth errors. Gated triple parity exact;last-two-sample conditional rate1/2 becomes deterministic with the older bit.

- rule30_gpt_hidden_tail.py (G117): FT0-FT2 preregistered NOT RUN;2048 five-tick pulse words, exact latent-tail kernel and no-fresh-noise conditional uncertainty guard. Publish before execution.

- rule30_gpt_hidden_tail.py (G117 outcome): after6c4792e, FT0-FT2 pass2048 histories,256 injections and152 fifth errors. Tail rate3/8 independent in each ideal prefix;conditional kernel histogram verifies entropy weighting. Two initial words share observed past but differ at E5, with no fresh noise.

- rule30_gpt_pulse_information.py (G118): JI0-JI2 preregistered NOT RUN;2048 pulse words,joint-count spectrum and closed entropy law with an injection-conditioning guard. Publish before execution.

- rule30_gpt_pulse_information.py (G118 outcome): after8ced884, JI0-JI2 pass2048 words and112 joint pairs;closed joint entropy6.465291187412 and MI5.534708812588 agree with counts. Injection-independence counterfactual refuted.

- rule30_gpt_information_growth.py (G119):GF0-GF2 preregistered NOT RUN;32 shared-fresh-pivot histories and8 iid-marginal cross-copy-reuse guards. Publish before execution.

- rule30_gpt_information_growth.py (G119 outcome):after439744b,GF0-GF2 pass32 shared-fresh-pivot histories and8 reused-bit guards. MI increment identity holds in the positive class;two-bit guard increment refutes marginal-iid-only extension.

- rule30_gpt_rare_information.py (G120):RB0-RB2 preregistered NOT RUN;64 observed-injection histories and32 hidden-event guards for the later information-loss budget. Publish before execution.

- rule30_gpt_rare_information.py (G120 outcome):after9f37d68,RB0-RB2 pass64 observed-injection and32 hidden-event histories;exact budget tight in positive control,hidden-event entropy0.271782221600 refutes rarity-only extension.

- rule30_gpt_second_image.py (G127): NS0-NS2 preregistered NOT RUN. Prefix lengths1..7; full finite precursor exhaustion, independent path-count certificate, and a period-doubling section guard. Publish before execution.

- rule30_gpt_second_image.py (G127 outcome): after81fb4fd,NS0/NS2 pass;NS1 HELD at n6. Target022000 has six full-shift precursor blocks,all containing100,with independent path count6. Binary constraints independently force22100. Strict deeper-image loss proved,not universal strictness.

- rule30_debt16_endpoint.py (GC321): RD16-E endpoint diagnostic on Local independent clocks; all controls PASS, blind all-terminal-h-zero REFUTED at291257 and634886. Finite only, shared child constructor.

- rule30_debt32.c (GC324): RD32 preregistered finite reference debt through2^20 on sixteen known histories; compile/smoke PASS, full run NOT RUN at registration. Caps and independent controls in header.

- rule30_debt32.c (GC325 outcome): afterce52a59, all controls PASS, full16-path frontier1048576; max reference debt60, endpoint h10, finite phase/birth91. P1 HELD; P2 REFUTED and retained.

- rule30_debt32.c --witness (GC326): bounded hard-witness trace; original controls reproduce, C3/C4/CF2/U PASS, P3 half-black REFUTED.
- rule30_cloud_allphase_debt.c (AP, Cloud, CL156): the exact slope-5/2 debt of every rotated copy of RD32's sixteen
  histories to 2^20 (32 clocks a walk). D_phi = D_0 at every phase; all-phase maximum 60, so GC940's denominator 92 is
  exact at this frontier and the allowance 91 unused. C1/C2 PASS, G HELD, P1 HELD, U REFUTED.
  Addendum CW (CL157): the coalescence window identity holds exactly; phase dependence lives only before coalescence.
- rule30_pulse_rebound.py (GC326): literal pulse/hole identity controls on522 rotations q4..32; scalar costs(q,3,1,q), q3 failure guard; no general ancestry claim.

- rule30_sparse_ancestry.py (GC336, SA1): preregistered inverse absorption/cycle diagnostic for ten two-pulse inclusion starts atq4,8;10 CPU-second cap; scalar/root/cycle/reconstruction controls. Syntax parses; NOT RUN. No larger frontier or general reachability claim.

- rule30_sparse_ancestry.py (GC337 outcome): SA1 ran once after8760e40, Intel CPU0.076s, ten starts NONROOTED, no cap; P1 REFUTED. Scalar/root/cycle controls pass; target reconstruction vacuity and separate positive q4 depth8 control recorded. No q16 extension.

- `lexicon/rule30_two_gap_ancestry.py` (TG1, GC351): preregistered tiny inverse diagnostic for GC350's four q8 two-zero-run sources and one fixed q16 source. 2 CPU seconds globally,25000 states per target; cap means UNDECIDED. Known positive reconstruction and cycle controls; NOT RUN. No forward census or q16 expansion.

- `openai_math/` (Cloud, 2026-10-07): one replication script per family imported into CO-DISCOVERED-PROOFS.md
  (om088, om049, om049b, om205, om189, om119, om186, om175, om175c, om235, om332, om003b), each with its
  predictions in the docstring, written before it ran, and the outcome below them; plus gc338_signed_kernel_check.py,
  Cloud's second reading of GPT's GC338. Standard library, except om235 (python-sat) and om189 (python-sat, with a
  `--sym` degree-split mode). The levels and the misses are in CO-DISCOVERED-PROOFS.md. No data.

- `idle_alarm.py` (Cloud, 2026-10-07): flags a worker whose recent CLOUD-LOCAL.md rows pass on drawn or offered work,
  idle for three rows, or go quiet; its control is a synthetic ledger. Cloud runs it on each visit (the
  shared-procedures rule). First run on the real ledger: Local's two pass rows of 19:07 and 19:52, both from before
  the draw-and-work rule; nothing since. No data.

- `record_find.py` (Cloud, 2026-10-09, at the owner's request after the SL repeat of G205): searches the whole
  record, ledgers included, for paragraphs matching every term, and prints each hit's file, line, heading, record IDs
  and a snippet, in the order a reader should trust the files. It is the search step of RECORD-MAP.md and of
  literature-before-leaps. Control: the query `wheel "forc(e|ed|ing)" "column ?s? ?2"` must put PERIOD-TWO.md row
  6.1 (naming G205) first; it does. No data.

- `known_find.py` (Local, 2026-10-28, L1078, at the owner's request after the degree law was re-derived): searches
  the kit's current main and the portal's listed submissions. It covers catalog rows, module headers, every
  declaration with its doc comment, and each submission's title, abstract, headlines and Lean source.
  `record_find.py` runs it after the record's search. `--new` reports additions and changes since this host's
  last complete check; full-source fingerprints catch changes inside existing modules (GC2039). Old key-only
  checkpoints establish a new content baseline explicitly. The cache lives outside git and refreshes every six hours; an unavailable index is
  reported as "novelty cannot be judged". Controls (`--selftest`):
  - the degree law must hit `AlgebraicDegree`, also through a normalized minus sign;
  - a stripe query must hit the portal, and `FrozenRuler` the kit's modules;
  - a nonsense term must hit nothing.

  All pass. No data in git.

- `lexicon/rule30_cloud_hole_entropy.py` (Cloud, 2026-10-09; Local's offer of 21:17): HE, the one-hole channel
  driven by iid fair right halves. For the walls 0 1^(p - 1), p = 5, 7, 9 and the control 11, it records the hole
  word over 400 holes, exactly (initial width T + 2), and measures late periodicity, block conditional entropies
  and the density of 1s. Predictions in the docstring, pushed before the run. No data.

- `lexicon/rule30_cloud_hole_truecount.py` (Cloud, 2026-10-09): TC, the TRUE one-hole language by SAT
  (python-sat, CaDiCaL). The light-cone triangle of the half-line with the wall is one formula, and hole prefixes are
  assumptions. A depth-first search over realisable prefixes gives exact |L_n|, the true minimal forbidden words,
  and a certified ceiling a_m^(1/m) from them (exact integers, Aho-Corasick). Predictions in the docstring, pushed
  before the run. No data.

- `lexicon/rule30_cloud_triangle_echo.py` (Cloud, 2026-10-09; CL102's queue): EC, the triangle-top echo C(d, s)
  under iid fair rows as exact rationals, by enumerating the finite window GC851's band allows (bit-sliced big
  integers). It checks the band (C = 1 outside it) and a direct simulation, and compares with CL095's measured
  C(d, d). Predictions in the docstring, pushed before the run. No data.

- `lexicon/rule30_cloud_hole_freepairs.py` (Cloud, 2026-10-09): FP, free pairs and free codes in the TRUE one-hole
  language, decided exactly up to TC's reached length from TC's complete set of minimal forbidden words (read
  from NP_SCRATCH_TC). A free pair would bound the entropy below as far as it holds. Predictions in the docstring,
  pushed before the run. No data.

- `lexicon/rule30_cloud_channel_truecount.py` (Cloud, 2026-10-09): TC2, TC at p = 2, the TRUE language of column 1
  next to 0101 (§8.20's channel). Exact counts, true minimal forbidden words, and a certified Collatz-Wielandt
  ceiling on their automaton's spectral radius, against §8.20's layer bound 0.1236. Predictions in the docstring,
  pushed before the run. No data.

- `lexicon/rule30_cloud_hole_freepairs_long.py` (Cloud, 2026-10-09): FP2, FP's free pairs on two to three times
  longer hole words by TC's exact SAT formula (1,024 ten-block words at p = 9 and 7, 64 at p = 5, random 15-block
  words at p = 9), every model replayed, plus a locality check on the realising right halves. Predictions in the
  docstring, pushed before the run. No data. Verdict gates repaired per GC900 and GC902 (per-loop counts; HELD only
  on complete SAT samples); `lexicon/rule30_cloud_hole_freepairs_long_selftest.py` tests them without a solver.

- `lexicon/rule30_cloud_zero_first_roots.py` (Cloud, 2026-10-10): ZF, the whole physical-root tree at fixed period q
  (the in-tree of (0, 0) under G199's map B, built by predecessors, which are entry 39's children), and which
  zero-first pairs (0, b) it contains; q = 1 .. 12 and 16. Predictions and outcomes in the docstring; CL126. No data.
  Its q = 16 tree is a third independent replay of Proposition 8 (entry 21), found to be a repeat after the run (CL128).

- `lexicon/rule30_cloud_sharp_entry.py` (Cloud, 2026-10-10): SE, a replay of GC913's eight backward pair formulas,
  and a look at which physical odd zero returns are one-parity (ZF's trees to q = 16, TM6b's q = 32 certificate).
  Finds the single cell's period-32 entry sharp (GC911's equality case). Predictions and outcome in the docstring;
  CL134. No data.

- `lexicon/rule30_cloud_sharp_lockstep.py` (Cloud, 2026-10-10): SL2, how long all sharp doubling entries share their
  profile weights (through k), and a closed form for the first profile that differs: its weight is q/4 plus the
  number of changes of f's half-word around its twisted cycle. Predictions and outcome in the docstring; CL143.

- `lexicon/rule30_cloud_white_end_replay.py` (Cloud, 2026-10-09): WR, a third independent replay of L498's computed
  step for the white end 1 0^q (width-8 stable sets, per-tick determinism for q = 10 .. 40, W^(n+4) = W^n from
  n = 22), with set-valued relations and no shared code. Predictions and outcome in the docstring; CL110. No data.

- `lexicon/rule30_cloud_word_census_replay.py` (Cloud, 2026-10-09): WR2, an independent replay of Local's WC census
  of the one-sided route on every Lyndon column word (width 8 on periods 7 .. 18, width 10 on 7 .. 14), against
  L499's list and counts. Predictions in the docstring, pushed before the run. No data.


- `lexicon/rule30_one_excursion.c`: EX1, one fixed q16 zero-return charge audit from reviewed pair(320,64); CPU, standard C,800000-edge/2-second caps. Preregistered GC358, NOT RUN. Binary and transcript outside Git.

- `lexicon/rule30_kick_review.py`: GC359 targeted entry26 timing review, m16 only; CPU Python, shared automaton plus independent local truth table. No wider sweep or data census replay.

- `prizes/collatz_gpt_segment_gap.py`: GC436 endpoint-segment inspection of seven reused GC432 cases; exact rational gap and independent component/breakpoint/H controls, translation and empty guards. PASS196 increments; blind single incompatible increment HELD at width7,t34, gap97/8192. Data outside Git.

- `prizes/collatz_gpt_single_gap_audit.py`: GC437 one fixed width7,T48,t34 oriented component audit; exact P,N and literal-H controls with independent individual-survivor prefixes PASS. Both signs HELD; zero-imbalance singleton causes centering gap, actual collision guard vacuous. Data outside Git.

- `prizes/collatz_gpt_cancellation_split.py`: GC438 two-stage signed cancellation budget, seven reused cases; literal-H and four empty-final positive-Q controls PASS196 increments. Blind temporal>within at width7 HELD; abs-before-telescoping counterfactual REFUTED all seven. Data outside Git.

- `prizes/collatz_gpt_temporal_pairs.py`: GC439 fixed width7,T48 canonical G80 pair partition;21 block sums/34 interior controls PASS. Majority-capture REFUTED (14.48%); mixed-necessity REFUTED at t28. Data outside Git.

- `prizes/collatz_gpt_equal_bit_allocation.py`: GC442 fixed width7,T48,t28 G222 matched/unmatched allocation; literal-H, modulo4 and synthetic multiplicity controls PASS. Blind one match HELD; residual-drop counterfactual REFUTED. Data outside Git.

- `prizes/collatz_gpt_count_match_compare.py`: GC445 two fixed width7,T48 increments comparing G223/G91/G220 bounds; exact and multiplicity/lost-child controls PASS. Blind G220 improvement REFUTED both times; extra count matches retained. Data outside Git.

- `lexicon/rule210_gpt_deviation_audit.py`: GC466 independent decimal-rule integer-vector certificate;9 states, life3, no irregular endpoint/return/cycle; shifted-background rejection PASS.
- `lexicon/rule210_gpt_base_certificate.py`: GC467 exact121-prefix base for L274; unique R, depth120 two survivors,256 scalar and3 tail controls PASS.

- `prizes/collatz_gpt_schedule_shape_guard.py`: GC468 terminal-generated no-NN words through14 folds;2581 unimodal laws, exact mass controls PASS; generic-N dip retained.

- `prizes/collatz_gpt_composite_shape_audit.py`: GC469 L276 independent two-branch instrument;1364 composite identities and496 unimodal inputs PASS; wrong order, missing premise, zero/plateau/terminal guards retained.

- `lexicon/rule210_gpt_left_base_audit.py`: GC470 L278 independent seven depth121 bases,56 depth6 exclusions and1792 scalar controls PASS; reflected-prefix counterfactual fails at depth3.

- `lexicon/rule210_gpt_first_pulse.py`: GC472 uniform first-deviation recurrence controls;64 flips,352 binomial comparisons and20 one-sample pulses PASS; odd first flip fails its clock, even branch retained.

- `lexicon/rule210_gpt_next_odd_gate.py`: GC473 exact reset/freeze relation;64 vector/gate and32 binomial controls PASS,32 pass/32 blocked,32 paired-choice erasures.

- `lexicon/rule210_gpt_next_even_gate.py`: GC474 affine next-even transient;128 vectors,64 binomial controls and64 gate survivors PASS;32 paired choices erased by clock.

- `lexicon/rule210_gpt_e3_initial_gate.py`: GC475 independent Local E3 audit;64 binomial initial gates and320 E3 choices PASS,192 blocked/128 survive; all8 SB-witness choices survive.

- `lexicon/rule210_gpt_gate_transport.py`: GC476 background transport/finite-run lemma;64 transport/bound and128 binomial controls PASS;20 positive-tau passing guards.

- `lexicon/rule210_gpt_abstract_pulse.py`: GC477 abstract-history guard;10880 settling cases,8 truth and32 actual causal controls PASS; permanent-pulse failure and initial boundary-indexing error retained.

- `lexicon/rule210_gpt_clearing_front.py`: GC478 candidate clearing-front hand proof controls;16 local identities,10880 abstract cases and40064 clearing witnesses PASS; omitted-clearing failure retained.

- `lexicon/rule210_gpt_transfer_scope.py`: GC479 exact16-patch transfer audit; Rule210 identities PASS,6 Rule30 mismatches, explicit U1 clearing failure; zero-row guard PASS. Unrestricted patches, not clock orbits.

- `lexicon/rule30_gpt_balance_local.py`: GC483 signed non-flipping triple weights and finite-cone biased-prefix guards;8 local identities,4 ring steps,60 finite-prefix samples PASS. No fixed-seed asymptotic claim.

- `lexicon/rule30_gpt_selected_potential.py`: GC484 fixed singleton-orbit exact-potential audit, radii0..3/phase2,4,8,256 ticks;12 inconsistencies,257 independent rows and1536 pair identities PASS. No eventual-onset or density claim.

- `lexicon/rule30_gpt_late_potential.py`: GC485 fixed later starts16/64/128 at end256, radii0..3/phase2,4,8;36 exact-potential contradictions;257 independent rows and36 zero-reward controls PASS. No arbitrary eventual-onset conclusion.

- `lexicon/rule30_gpt_dyadic_anf.py`: GC486 times1/2/4 Boolean composition scope audit;1656 truth reconstructions PASS, degrees30=2/3/7, linear controls and affine-left-input guards PASS; no fixed-seed time lower bound.

- `lexicon/rule30_gpt_kernel_prefix.py`: GC487 fixed depth4/32 positive-continuation certificate;31 Rule30 signatures,465 pair witnesses,528 independent rows PASS; Thue-Morse2 and finite zero-tail controls. Restricted DFAO state size, not time hardness.

- `lexicon/rule30_gpt_boundary_collision.py`: GC502 clamped-wall output counts n=1..7 and exact collision probabilities; 170 literal-rule comparisons PASS, uniform-output counterfactual refuted. Shortest extra missing word 00000; separate local proof in the record, pending reading. No asymptotic entropy inference.

- `lexicon/rule30_gpt_zero_cylinder.py`: GC503 first visible zero-run classification from five initial right sites under the clamped wall; 128 fixed patch/tail controls PASS in packed and literal updates, uniform-duration CF refuted. No stationary renewal or entropy claim.

- `lexicon/rule30_gpt_gap_pair.py`: GC504 visible-101 characterization and two canalized row transitions; 32 patch and 8 transition controls PASS in packed and literal implementations. Separate local proof excludes adjacent gap lengths (1,2). No longer word scan or entropy claim.

- `lexicon/rule30_gpt_front_selection.py`: GC505 exact single-flip front laws through two ticks on fair initial rows; 512 local patches checked in XOR/OR and literal updates. First +1 forces next -1; second healing probability 3/8. No long-run speed inference.

- `lexicon/rule30_gpt_front_markov.py`: GC506 position-only front-state audit; 8192 thirteen-site patches through three ticks PASS in independent rules. Shared current position has history-dependent next law, with a separate hand proof for two histories. No speed or universal finite-state claim.

- `lexicon/rule30_gpt_front_window.py`: GC507 exact damage derivative on 64 triples and 12 finite-pair one-tick controls, all PASS. Arbitrarily wide finite damage has a hand-proved maximal jump to a singleton; ambient fixed-window CF refuted. No iid single-flip reachability or speed claim.

- `lexicon/rule30_gpt_front_reset.py`: GC508 causal aftermath of 12 finite-pair singleton resets, all PASS in independent updates. Guaranteed floor(N/2) left advances and odd-N healing endpoint; no iid reachability, regeneration or speed theorem.

- `lexicon/rule30_gpt_front_exposure.py`: GC511 fixed three-tick audit on the existing 8192 patches. Independent rules, 800 pre-gap and 1312 post-gap fresh groups, and 24576 exposure-accounting prefixes PASS. Reused fairness CF refuted; supports GC509-GC510 pending hand review, no speed fit or longer horizon.

- `lexicon/rule30_gpt_white_certificate.py`: GC514 independent five-tick checks of GC513's resonant white-run endpoint. All 341 patches and 31 fixed-left/right-prefix groups PASS; cap 6 means survival through tick 5. No selected-orbit duration bound or longer horizon.

- `lexicon/rule30_gpt_msb_prefix.py`: GC528 transposes GC487's unchanged 528-bit sample into 32 canonical MSB-prefix profiles. Independent rows, 496 distinguishing suffixes, two Thue-Morse profiles, original 31 LSB signatures and binary concatenation controls PASS. Finite state-size certificate only; no sample expansion or nonautomaticity claim.

- `lexicon/rule30_cloud_visible_gaps.py` (Cloud, 2026-10-08, CL033): RV, an independent replay of GPT's GC500 to GC504
  (visible counts, the zero-latch formula, the 101 characterisation) in Cloud's own coding, and the wheel read as
  visible gaps: 4, 4, 4, 4, 2, 4; every even-class kick is a swap of the two gap-start states (column 3 at the gap
  start). `--transients` (RV2): between kicks column 1 keeps the gaps 2 and 4, and 3-gaps almost never occur.
  Predictions in the docstring, pushed before each run; `--wheel` is post-hoc. CPU, standard library. No data.

- `lexicon/rule30_cloud_review_gc483.py` and `lexicon/rule30_cloud_review_gc505.py` (Cloud, 2026-10-08, CL034 and
  CL035): independent replays, in Cloud's own coding, of the finite claims in GPT's GC483 to GC496 and GC505 to GC546
  (19 controls, all PASS), with Cloud's unexpected checks: admissible velocity words number 2^(n-4) (held); the
  singleton's white starts are resonant at the run-start ensemble rate 1/4, not 1/3 (the 1/3 prediction refuted; the
  1/4 one, preregistered on fresh times with `--late`, held). CPU, standard library. No data.

- `lexicon/rule30_cloud_rr_replay.py` (Cloud, 2026-10-08, CL036): RRX, an independent encoding (CaDiCaL, one phase
  per solve, a four-input XOR) of Local's realizable records R_real(d). It reproduces ZR2 (d = 3 .. 19) and L247
  (d = 21 .. 41) exactly, and finds the clock samples their UNSAT instances need: from time 4 to 7 onward, at
  every depth. python-sat. Predictions in the docstring, pushed before the run. No data.

- `lexicon/rule30_gpt_gc549_certificate.py`: GC549 checkpoints 18..20, reproducible fixed horizon-17 inverse polynomial certificate and independent time-column controls; no actual-right search.

- `lexicon/rule30_cloud_relaxed_records.py` (Cloud, 2026-10-08, CL041, at GPT's request): RRL, realizable records
  per phase in four models of column 1 (free; avoiding 11, 00000, 101001; avoiding every minimal forbidden word of
  the actual language up to length 10; the actual right half). Also the exact visible language to length 10,
  and (`--gap`) a gap witness with its shortest absent factor found by SAT. python-sat. Predictions in the
  docstring, pushed before each run. No data.

- `lexicon/rule30_gpt_entry_image.py`: GC549 checkpoint 28, exact two-step sixteen-state predecessor image; 32 independent literal controls and a shortest missing spatial tail, no visible-word census or SAT.

- `lexicon/rule30_cloud_wheel_drift.py` (Cloud, 2026-10-08, CL043, the owner's 17/56 question): RD, the
  wheel's long-run rotation by exact kick bookkeeping (integers only). Forward and backward kicks cancel to 0.2%;
  the rotation is 17/56 to within about 1e-5. Predictions in the docstring, pushed before the run. CPU, standard
  library. No data.

- `lexicon/rule30_cloud_review_g236.py` (Cloud, 2026-10-08, second reading of G236): brute-force replay of GPT's
  two-step entry-image certificate (formula, state set, subset steps, end-to-end exclusion of 11100011), whether
  its 0001 premise is needed, and the minimal missing prefixes of the walled two-step image. CPU, standard
  library. Predictions in the docstring, pushed before the run. No data.

- `lexicon/rule30_gpt_gap_continuation.py`: GC549 checkpoint 29, one conditional thirteen-symbol target from prefix 11100; complete shrinking-cone source extension and independent literal/paired updates. No language census, SAT or death-time run.

- `lexicon/rule30_gpt_three_gap_gate.py`: GC549 checkpoint 30, fixed fifteen-site cone for the canonical branch's next 3-gap; 1024 independent literal/paired controls, necessary 001 gate and retained reset failure.

- `lexicon/rule30_gpt_gap_cylinders.py`: GC549 checkpoint 31, four sound ternary source cylinders and 27 local controls; three exclude the following two-gap, residual 001000 remains unknown. No source census.

- `lexicon/rule30_cloud_wheel_balance.py` (Cloud, 2026-10-08, the owner's matter and antimatter question): RB, the
  kick balance of RD measured without its mod-28 sign convention. A visible charge (14x - 3 per cell) makes each
  true kick a change of level; early and late windows test whether the balance needs equilibrium. CPU, standard
  library. Predictions in the docstring, pushed before the run. No data.

- `lexicon/rule30_gpt_gap_reset.py`: GC549 checkpoint 32/G237, fifteen literal controls for the six-site prefix chain and four common-prefix checks; shared-variable cancellation closes the residual cylinder. No new census.

- `lexicon/rule30_gpt_gap_classification.py`: GC549 checkpoint 33/G238, three finite local controls for the two-branch hand exclusion; 64,64,32 literal assignments, no target census.

- `lexicon/rule30_cloud_gray_split.py` (Cloud, 2026-10-08, the owner's Gray-code question): RG, Rule 30 as the
  Gray-code rule (Rule 60) XOR an edge term, and the forced left half under the 0101 clock as an exact Pascal-in-time
  sum of edge events (checked against section 5's recursion by Lucas's theorem). CPU, standard library. Predictions
  in the docstring, pushed before the run. No data.

- `lexicon/rule30_cloud_window_flips.py` (Cloud, 2026-10-08, the owner's window descent): RW, bit flips in every fixed
  window of the single-cell pyramid (widths 3 .. 8, centre 97 columns) and in windows moving with the right edge,
  against the exact fair-coin null; checks the forward Gray split (flip = left neighbour XOR edge event). CPU,
  standard library. Predictions in the docstring, pushed before the run. No data.

- `lexicon/rule30_cloud_rr_phases.py` (Cloud, 2026-10-08, Local's L291 request): RRP, RR's deep realizable records at
  d = 49 .. 81 replayed in RRX's independent encoding and split by clock phase, with the suffix threshold of the
  clock at each first impossible length (bisection). python-sat. Predictions in the docstring, pushed before the
  run. No data.

**GPT GC549 checkpoint34 (2026-10-08).** `lexicon/rule30_gpt_band_deletion.py` reuses the 89 no-11 nine-symbol words and independent scalar/polynomial inverse values. Preregistered all-five-essential prediction refuted at depth13; four remaining zeros force the same code. Other single deletions leave 8,3,5,1 relaxed witnesses. No actual right-language census, depth extension or hand proof promotion.

- `lexicon/rule30_cloud_slant_flips.py` (Cloud, 2026-10-08, the owner's slanted descent): RS, flip counts in windows
  that descend the single-cell pyramid along rays of slope -1 .. 1 and along the left edge, each against the exact
  fair null of its frame (G97's left, stay and right-step flip identities). CPU, standard library. Predictions in
  the docstring, pushed before the run. No data.

- `lexicon/rule30_gpt_gluing_control.py` (GPT, GC549.38): two fixed actual-right fixtures joined to inverse left prefixes, whole-row decimal Rule 30 clock checks through 17, final-pivot and outside-cone mutations. All pass. Prediction ledger append failed before the run; recording failure retained, not described as successfully ledger-preregistered.

| `lexicon/` | rule30_gpt_old_lock_boundary.py | OLD1 m=16 old-lock boundary audit; one preregistered run, controls PASS, table-equality prediction refuted | RULE30-GPT GC587 | text outcome only; no data in git |
| `lexicon/` (Local, 2026-10-08 to 10-09) | rule30_all_s_left_depth.py, rule30_all_l_period10.py, rule30_all_l_slab.py, rule30_all_l_slab_sat.py, rule30_all_l_future.py, rule30_all_l_certs.py, rule30_all_s_future.py, rule30_edge_period_universal.py, rule30_critical_bridge_sat.py, rule30_records_real_sweep.py, rule30_records_real_certs.py, rule30_alternation_single_seed.py, rule30_diagonal_bias.py, rule30_diagonal_bias.c, rule30_diagonal_bias_direct.c, rule30_local_review_432.py, rule30_local_review_cylinders.py, rule30_local_review_g237.py, rule30_local_review_gc549.py, rule30_local_review_gc549_34.py, rule30_trace_widths.py, rule30_isolated_zero_strip.py, rule30_isolated_zero_wrap.py, rule30_isolated_zero_wide.py, rule30_trace_width2.py, rule30_trace_width2.c, rule30_isolated_zero_pairs.py, rule30_verified_certs.py, rule30_template_coupling.py, rule30_and_shadow.py, rule30_mahler_carry_dial.py, rule30_trace_word_certs.py, rule30_one_hole_widths.py | the all-S and all-L renewal line: the left-depth certificate J >= 6n - 3 (L372), the 155-cell all-L ring (AL, L380), the all-L slabs (ALS, ALX, ALF, ALC; DRAT-verified) and the all-S slab of thirteen columns (ASF, DRAT-verified); the left edge's prefix-period staircase (UB, L383); bounded critical all-L uniqueness at p = 310 (CX and CXE, 100 DRAT-verified UNSATs, L404); the realizable records R_real(d) to d = 97 (RR2, L399) and their DRAT certificates (RRC, L419 to L421); the single seed against the fair-row alternation null (L415); the exact light-speed diagonal correlation rho_k to k = 21, two independent kernels (DB, L418, L422); exact trace-language counts at widths 1 and 2 in the physical and G frames (TW, L427); an independent reimplementation of the black-end strip-graph certificate, q = 1 .. 16 (SG, L429); the wrap table completing GPT's uniform black-end argument for q >= 17 (WT, L431); wider strips for the open walls, and ring orbits with exact 0 1^q columns (SGW, L433); the width-2 trace counts to n = 17, giving h_top(Rule 30) <= 1.3189 bits (TWX, L436); any forced adjacent column pair in the failing black-end components: none (SGP, L437); today's certificates re-checked by the verified checker cake_lpr (VC, L443 on); GC831's periodic coupling gate for GC828's template (TC, L452); carry-limited Collatz and sparse-AND Rule 150, the owner's XOR-plus-AND question (AS, L454); the carry dial on Mahler's 3/2 map, the owner's third corner (MD, L458); cake_lpr-verified certificates for the forbidden G-trace words through length 11 (TWC, L465); literal replays for hand readings (local_review_*). Each header carries its predictions and OUTCOME | PERIOD-TWO.md §6 (Q1, Q6); RULE30-PRIZE.md §8.70; CONSTELLATION.md row 20; CHAT-LEDGER L372 to L426 | CNFs, DRAT proofs and checkpoints in `~/np-scratch-int/rule30-al`, `rule30-rr` and `rule30-db` (outside git); the rest compute afresh |
| `lexicon/` (index backlog, 2026-10-05 to 10-09, all three parties) | rule30_debt16.py, rule30_affine_wall_audit.py, rule30_all_s_period6.py, rule30_all_s_period6_rigidity.py, rule30_anchor_review.py, rule30_audit_g95_g96.py, rule30_audit_g97_g98.py, rule30_audit_g99_g100.py, rule30_aw.py, rule30_aw2.py, rule30_aw3.py, rule30_aw3b.c, rule30_aw4.c, rule30_aw5.py, rule30_aw5c.py, rule30_aw5d.c, rule30_bricks.c, rule30_checkerboard_defect_certificate.py, rule30_class12_gate_check.py, rule30_cloud_alternation.py, rule30_cloud_bricks.py, rule30_cloud_edge_triangles.py, rule30_cloud_equivalent_seeds.c, rule30_cloud_four_quadrants.py, rule30_cloud_fringe_uniqueness.py, rule30_cloud_front_spectrum.py, rule30_cloud_left_apex.py, rule30_cloud_left_boundary.py, rule30_cloud_review_gc549.py, rule30_cloud_right_front.py, rule30_cloud_rr3.py, rule30_cloud_shunted_column.py, rule30_cloud_triangle_ladders.py, rule30_cloud_turning_rings.py, rule30_cloud_word_bias.py, rule30_cloud_word_replication.py, rule30_damage_speed.py, rule30_dq3.py, rule30_dq3_review.py, rule30_dq3_root_clock_review.py, rule30_dyadic_companion.py, rule30_edge_deadline.py, rule30_edge_deadline2.py, rule30_fbr16.py, rule30_fbr16_review.py, rule30_finite_inverse_branch.py, rule30_frames.py, rule30_g188_returns.py, rule30_gate_completion_review.py, rule30_gpt_e14_identity.py, rule30_gpt_gate_application.py, rule30_gpt_gate_bridge.py, rule30_gpt_gate_completion.py, rule30_gpt_gate_core.py, rule30_gpt_gate_correlations.py, rule30_gpt_gate_cut.py, rule30_gpt_gate_exterior.py, rule30_gpt_gate_image.py, rule30_gpt_gate_paths.py, rule30_gpt_gate_prefix.py, rule30_gpt_gate_propagation.py, rule30_gpt_gate_wall_times.py, rule30_gpt_instant_splice.py, rule30_gpt_noise_vector.py, rule30_gpt_records_scope.py, rule30_gpt_toolkit_information.py, rule30_gpt_zero_block_precursors.py, rule30_halfcircle_repeat.py, rule30_hg4.py, rule30_hg4_review.py, rule30_hw32.c, rule30_hw32_forward_compensation.py, rule30_hw32_literal_audit.py, rule30_hw32_trigger_scope.py, rule30_hw32w.c, rule30_j1_deadline_audit.py, rule30_kick_alphabet_exact.py, rule30_kick_angles.py, rule30_kick_bite.py, rule30_kick_bite_drat.py, rule30_kick_bite_kissat.py, rule30_kick_bite_sat.py, rule30_kick_candles.py, rule30_kick_class42_560.py, rule30_kick_exact_review.py, rule30_kick_landing.py, rule30_kick_layers.py, rule30_kick_lock.py, rule30_kick_strain_32.py, rule30_kick_strain_448.py, rule30_kick_strain_kissat.py, rule30_kick_strain_long.py, rule30_kick_strain_units.py, rule30_ladder_local.py, rule30_leftside_horizon.py, rule30_leftspecial_guard.py, rule30_linear_complexity.py, rule30_locked_core.py, rule30_locked_core_lock.py, rule30_locked_core_review.py, rule30_locked_cycles.py, rule30_locked_domains.py, rule30_locked_extend.py, rule30_locked_extend_review.py, rule30_locked_horizon.py, rule30_locked_lift.py, rule30_locked_pair.py, rule30_locked_paths.py, rule30_locked_replacements.py, rule30_locked_small_pair.py, rule30_neutral_concat.py, rule30_noise_vector_review.py, rule30_pr191_c1.py, rule30_pr195_d0.py, rule30_pr196_d1.py, rule30_pr198_d2.py, rule30_race_memory.py, rule30_races.py, rule30_rc2.py, rule30_rc2_certificate_check.py, rule30_rc2_export.py, rule30_rd16_check.py, rule30_rd32_check.py, rule30_records_ckpt.py, rule30_records_real_sat.py, rule30_ring_census.py, rule30_rq3.py, rule30_rq3_review.py, rule30_rqo.py, rule30_rqo_review.py, rule30_rs16.py, rule30_rs32.c, rule30_selected_gate_audit.py, rule30_silence_onset.py, rule30_silent_sources.c, rule30_silent_sources.py, rule30_sturmian.py, rule30_three_gap_death.py, rule30_tm5.py, rule30_tm5b.py, rule30_tm6.c, rule30_tm6_backward.py, rule30_tm6b.c, rule30_triangle_census.py, rule30_triangle_law_audit.py, rule30_wheel_lock_iid.py, rule30_window.py, rule30_zero_runs.c, rule30_zero_runs.py | listed so every script has a row (Local's upkeep, 2026-10-09). Each header names its author or requester, its predictions and its OUTCOME; this row does not attribute or summarize them | as each header says (RULE30-PRIZE.md, RULE30-GPT.md, PROOFS.md, the chat ledgers) | as each header says |
| `lean/` (Local, 2026-10-09) | Rule30Period1.lean, RootedReturn.lean, BlackLock.lean, ParityMask.lean, P8Lock.lean, TheoremA.lean | the period-1 case of Problem 1 for the single seed (Condrey's theorem, PROOFS.md entry 37) machine-checked in Lean 4 against DeepMind's Rule30.lean; checking instructions in the file | PROOFS.md entry 37; CHAT-LEDGER L445 | none: it needs google-deepmind/formal-conjectures (b3f2641) and its Mathlib cache, outside the repository; RootedReturn.lean: L487's theorem that every rooted walk returns, at every period q, machine-checked in full (termination core, step injectivity, reset uniqueness and existence; no sorryAx); BlackLock.lean: G.GPT271's nine-step black lock, its persistence and the eight-step control (no sorryAx); ParityMask.lean: G.GPT269's ingredients (degree count, equal-or-complement differences, odd-length parity flip, unique predecessor, odd driver has no predecessor; no sorryAx); P8Lock.lean: the one-hole wall 0 1^7 closes at width 5, since after two macros x1 = 0 for ever (TB, L496; no sorryAx); TheoremA.lean: entry 5 (Jen's theorem with a clock) and its corollary, no two adjacent columns periodic for ever (no sorryAx, no choice) |

- `lexicon/rule30_cloud_event_coherence.py` (Cloud, 2026-10-08, the owner's edge-line observation on the Sieve): EC,
  three one-line local rules for Rule 30's edge events (never adjacent straight down or down-left; a row of events
  continues exactly over black cells), checked at every cell, and the continuation rates in five directions against
  random photons at the same rate. CPU, standard library. Predictions in the docstring, pushed before the run. No
  data.

- `lexicon/rule30_cloud_review_g248.py` (Cloud, 2026-10-08, the reading of GPT's G248 and GC582): replays the
  crossing-gap parity law on all 784 formal splices and the complete-gap law on every pair of consecutive RB locks
  (RB's seeds), with endpoint choices varied. CPU, standard library. Predictions in the docstring, pushed before the
  run. No data.

- `lexicon/rule30_cloud_review_old1.py` (Cloud, 2026-10-08, the reading of GPT's GC584 and GC588): an independent
  replay of OLD1, with its own window step and set propagation (no KL or OLD1 code), comparing the 54-, 55- and
  56-transition kick tables at m = 16. CPU, standard library. Predictions in the docstring, pushed before the run.
  No data.

- `lexicon/rule30_nl_certificate_audit.py` (GPT, 2026-10-08, GC613): checks supplied NL artifact hashes, byte-identical regenerated cones, six sparse-core witnesses with independent list updates, and both DRAT proofs with a separately built official checker. CPU, standard library and drat-trim. Predictions recorded before running; all checks PASS. Data and logs outside git.

| Exceptional return gate | `lexicon/rule30_exceptional_gate.py` | 32 exact six-tick cone extensions, independent list and packed updates, two farther-tail controls; hand-collapse addendum | RULE30-GPT.md GC619 | No data files |

| LL second-return short image | `lexicon/rule30_ll_short_image.py` | Exhaustive 4096-input finite cone; all second-return fifth bits one; independent updates and farther-tail controls | RULE30-GPT.md GC621 | No data files |

- `lexicon/rule30_gpt_mixed_left_cost.py`: one preregistered sixteen-word forced-left cost audit; independent decimal wall controls, no physical right-side realization or asymptotic claim.

- `lexicon/rule30_gpt_mixed_pivot_partner.py`: four third-letter pivot/partner comparisons using GC708 JSON on standard input; common-partner prediction refuted, SL/LS common-black partners identified (GC714).

- `lexicon/rule30_gpt_zero_tail_guard.py`: four stored-prefix zero-tail forward checks using GC708 JSON; Boolean/decimal agreement, partner/deeper-bit controls, no supplied right boundary (GC716).

- `lexicon/rule30_gpt_absolute_guard.py`: validates the two-integrator absolute-guard recurrence on GC716’s same four prefixes against independent decimal evolution; GC717.

- `lexicon/rule30_gpt_l_white_track.py`: GC768 disclosed static replay of GC767’s stored-ring arithmetic; independent list/mask reads, reversed stride and all-start eight-white obstruction. No CA evolution or data files.

- `lexicon/rule30_gpt_diagonal_memory.py`: GC773 independent decimal replay of CL078 rho1..3 on128 words, leading-bit complement/fairness controls, failed order-two diagonal memory guard.

| `lexicon/rule30_gpt_window_memory.py` | GPT GC780 | Registered 256-word width-two higher-order scope control: single-row independence at lag two, mixed third moment 1/8, fixed-column zero control. Ran after 222b76a2: WM0/WM1/WM3 PASS, WM2 REFUTED as required. |


- `lexicon/rule30_gpt_black_lock.py`: GC850 exact width-five black-wall masks, independent tuple-table and integer kernels, backward image checks, width-four and reset-free controls. All checks PASS; nine-step transient is certified, indefinite prefix 01 invariance is hand-proved.


- `lexicon/rule30_gpt_wheel_start.py`: GC852 exact width-four one-turn wheel start viability; backward and forward label traversals agree, white-phase inverse control passes, reversed words empty. Relaxed initial ambiguities 5,27,44 for columns 2,3,4; no actual full-half counterexample.


- `lexicon/rule30_gpt_reference_exit.py`: GC853 small reference first-exit projection; all 155 profiles have 121 free falling ticks. Per-bit existential check and corrected indexed phase identity pass. Initial +29 indexing failure retained; no successor enumeration or infinite-extension claim.


- GC854 addendum to `lexicon/rule30_gpt_reference_exit.py`: third-edge projection leaves exactly56 independent free ticks, fixes65; all local existential W,Q combinations and every removed-tick failure checked. No complete-word enumeration or infinite-tail claim.


- `lexicon/rule30_gpt_slab_encoding_audit.py`: GC855 literal SL clause audit passes; reproduces historical missing-unit checker failure (153 violated units) and mocked unknown-return parsing. No SAT executable invoked; peer source at02bf2a8f preserved.

- `lexicon/rule30_gpt_sharp_witness_audit.py`: GC915 independently verifies SE's fixed physical one-parity period 16 source, absorption 87867 at caps 16/32 and entry weights8; literal-cell controls pass. No full-tree or TM6b replay.

- `lexicon/rule30_gpt_recoalescence_fixture.py` (GPT, 2026-10-10): GC926, fixed period8/16 full-line clock continuation; period16 entry lag29 reproduces G6.3's driver429 measurement, refuting six-edge extrapolation. Initial control-origin failure retained; no census.

- `prizes/mahler_gpt_fixed_prefix.py`: GC931, two independent residue constructions and direct replay certify CL148 fixed23/24-bit cutoff below10^6; flipped-last-bit and coarse-height countercontrols pass. No start census.

- `lexicon/rule30_gpt_p8_prefix.py`: GC932, corrected zero-exterior p8 prefix witnesses; initial00000->01 prediction failed and retained. Registered32-start repair, literal and phase checks pass; no full language census or Lean run.

- `lexicon/rule30_gpt_carry_limit.py`: GC935, exact dyadic one-step carry-cap thresholds; two implementations and below-boundary controls pass. Registered65-addition cap miscounted/exceeded, retained; no SAT/horizon sweep.

- rule30_gpt_witness_suffix.py (GC949): fixed nine-edge q16 witness suffix; inherited clock, exhaustive literal children and interval-debt controls. Predictions published before run; no ancestry census or frontier extension.

- `lexicon/rule30_rrl_transducer.py`: GC971 exact finite-word inverse-column DFA image; finite membership, literal-image, truth-table and terminal controls PASS. No closed invariant or record bound.

- `lexicon/rule30_rrl_closure.py`: GC973 capped K10 C32 counter closure unfinished after 12 rounds; controls PASS, no cap. No invariant or record bound.

- `lexicon/rule30_rrl_boundary.py`: GC974 boundary-only widening obstruction; six endpoint-preserving relaxed 33-white constructions independently replayed. Full clock rejects them.

- `lexicon/rule30_rrl_factors.py`: GC975 sound length-3 internal-factor widening; controls PASS, abstract C32 overflow at round34. No physical witness or certificate. GC976 recovers depth5 zero trap: exact maximum3, widening pumps all lengths; independent source replay PASS.

- `lexicon/rule30_rrl_prefix_refine.py`: GC977 exact leading-zero-profile refinement repairs GC976 trap; controls PASS, abstract C32 overflow round35. No certificate or physical witness.

- `lexicon/rule30_rrl_history.py`: GC978 backward overflow ancestry recovers counter13 unsupported post-exit prefix; twenty inverse truth-table controls PASS. No physical witness.

- `lexicon/rule30_rrl_context.py`: GC979 seven-letter separator excludes GC978 loss with source containment; controls PASS, abstract C32 overflow round36. Fixed packet-length refinements parked.

- `lexicon/rule30_rrl_residual.py`: GC980 suffix-test quotient preserves source/test membership and GC978 separator; abstract C32 overflow round37. No certificate.

- `lexicon/rule30_rrl_learn.py`: GC981 two guided loss refinements verified; third attempt hits shared time cap. No certificate; short dead-prefix viability identified as next refinement.

- `lexicon/rule30_rrl_viable.py`: GC982 short dead-prefix viability blocks GC981 pumping with44 tests; controls PASS, C32 overflow round37. No invariant.

- `lexicon/rule30_rrl_origin.py`: GC983 exact white-first origin preserved through all black resets; nine-word input, controls PASS, abstract C32 overflow round38. No invariant.

- `lexicon/rule30_cloud_centre_sequences.py` (Cloud, 2026-10-10, the owner's question: can the centre column follow
  the primes, the Fibonacci numbers, pi?): CS, builds any target square by square (the left-permutive inverse) and
  finds the best prefix over every start of total width up to 18 for the primes, the Fibonacci positions and parity,
  01 and pi in binary. CPU, standard library. Predictions in the docstring, pushed before each run. No data.

- `lexicon/rule30_rrl_core_budget.py` — GC986: fullK18 admits at most one4422 core at all lengths; finite edge potential, literal controls; not a record bound.

- `lexicon/rule30_cloud_rreal_trend.py` (Cloud, 2026-10-10, row Q6, the uniform target's test): TR, the trend of the
  decided realizable records R_real(d) over d = 30 .. 114 (slope, block means, a shuffle counterfactual), and a deep
  test at L = 18 for sampled depths 121 .. 168 with RR's query (pysat CaDiCaL, capped, resumable). CPU. Predictions
  in the docstring, pushed before each run. Checkpoint outside git.
- `lexicon/rule30_cloud_train_block.py` (Cloud, 2026-10-10, row Q6, serving CUT): TG, the 2-gap train 1010.. (column 1 of
  period 4 beside the 0101 wall): membership of (10)^n to n = 200 in both phases (kissat, via relaxed_records_k), the
  finite right halves that sustain it (1001 beside the phase-0 clock, 3000 readings), the six-cell period-4 block that
  lasts 20,000 steps against chaos at site 7, and a failed search for a finite invariant window. CPU, seconds to a minute.
  Mode `joint` (2026-10-10 18:46, CL210): GPT's GC1039 replicated with own code (581 origins with a future, 2 with an
  entry past, common sites 1 .. 23; the wrong-x8 branch 4975 and 0; slab support two prefixes); JP4 REFUTED: with
  only the leading 0 relaxed, 5 survive and their common sites are exactly CL198's 19 pins.
- `lexicon/rule30_train_slab.py` (GPT, 2026-10-10, GC1017, Q6/CUT): literal local truth-table checks for three correlated implications forcing the two-gap train slab; exact phase-0 exterior gate and dropped-observation countercontrols. No SAT or record scan.
- `lexicon/rule30_train_return_gate.py` (GPT, 2026-10-10, GC1018, Q6/CUT): exact five-cell return gate at the reduced 0111 train boundary, a nine-cell nonclosure witness, and literal/packed/full-slab controls. No SAT or record scan.
- `lexicon/rule30_train_exit_delay.py` (GPT, 2026-10-10, GC1019): exact eight-tick train-exit delay, all 256 controlled exterior streams, eight actual cones, domain-table and fixed-seed reduction controls.

- `lexicon/rule30_train_p8_closure.py` (GPT, 2026-10-10, GC1020): finite premises for KIMI Q2 eternity by causal P8 feedback; 32-tick cone, eight band transitions, exact five-cell lock image and independent/countercontrols. No long run or SAT.

- `lexicon/rule30_train_escape_transport.py` (GPT, 2026-10-10, GC1021): bounded known-escape displacement diagnostic; original t16 exit, no shifted exit through100, two continuations and independent cone controls. No eternal-healing inference.

- `lexicon/rule30_train_hidden_returns.py` (GPT, 2026-10-10, GC1022): two recurrent five-cell paths with distinct outputs and impossible exterior updates; actual seven-ring output control, G282 restriction, and complete independent macro checks.

- `lexicon/rule30_train_boundary.py` — GC1023: short-factor train exit proof controls and finite startup entrance3 witness; no membership solver.

- `lexicon/rule30_train_carrier.py` — GC1025: 45 early mutation controls and independent replay of CL193; no solver.

| `lexicon/rule30_train_exit_packet.py` | GC1026/W283: exact seven-cell failed-gate packet;512 literal gates,22 image steps,65536 cone controls pass; independent review pending. |

| `lexicon/rule30_train_exit_target.py` | GC1028:39 exact nine-bit exit targets;512 literal cases and1024 full-slab controls pass. Prefix exclusion remains the missing inference. |

- `lexicon/rule30_cut_pair_domains.py`: GC1029 bounded pair-domain diagnostic; stalls on the verified 45-bit cut, controls pass.

- `lexicon/rule30_train_macro_pinning.py`: CL198 pinning diagnostic with proved macro premises; still unresolved, controls pass, stopped.
- `lexicon/rule30_cloud_junctions.py` (Cloud, 2026-10-10, row Q6, the anatomy of records): JN, the forced left half of
  piecewise-periodic visible words in the free model; does the longest white run stay bounded as the periodic pieces grow,
  so that white runs are made at the junctions? Pure words, one junction, two junctions (the L596 shape). CPU, seconds.

- `lexicon/rule30_two_constant_junction.py`: GC1031 free-model two-constant-piece diagnostic; independent controls, inconclusive and stopped.

- `lexicon/rule30_pinned_strip_future.py`: GC1034 fixed24 strip reset diagnostic; first output ambiguity at time96, literal controls pass; stopped.

- `lexicon/rule30_entrymemory_repair_check.py`: GC1035 independent packed replay of CL204 retained sets; merger at59, terminal190; no SAT calls.


- lexicon/rule30_cut45_pin_guard.py: GC1036 exact joint five-pin predicates; common19 pins plus suffix require sites16,20 black for final1. Peak2554 rows; literal controls PASS, transport prediction REFUTED; no actual membership or all-depth bound.


- lexicon/rule30_cut45_origin_past.py: GC1037 exact backward correlated past; entry plus common19 pins excludes joint black sites16,20. Peak261 rows;23 leading1 initial rows. Parent and nonvacuous forward/backward controls PASS; common-pin forcing inherited, no all-depth bound.

- lexicon/rule30_cut45_past_support.py: GC1038 prefix15 guard REFUTED by literal relaxed past with illegal exterior updates; width24 exclusion survives releasing pin23. Common18 suffice backwards; forward pins/all-depth unresolved.

- lexicon/rule30_cut45_joint_origin.py: GC1039 discharges common19 pins via two-sided width24 origins plus proved first7 support. Two correct-bit origins; wrong-bit join empty. Independent graph and actual-model controls PASS; all-depth OPEN.

- GC1040: rule30_cut45_origin_scan.py — two joint origins, one inverse tick; spatial reset prediction fails, clock selects a common21-bit parent prefix. Parametric plateau proof,252 literal controls and r0 counterexample; failed r1 countercontrol retained.
- GC1041: rule30_plateau_phase_guard.py — six-site black-phase age2 exclusion, correct-phase/age1/shortened-prefix positives; hand white-plateau halo and exact1-versus3 terminal-pair control. No SAT, visible cut or record bound.

- lexicon/rule30_exterior_repair.py: GC1042 exact four-row projection of one added updated column; 2728 literal pair controls and414 repairs PASS. Greedy iteration rejects the actual1001 train; halfwidth/all-depth OPEN.

- lexicon/rule30_black_wall_scope.py: GC1043 corrects WA3's phase interpretation and question D; true free R°(3)=4, finite black-phase endpoints odd. Literal, packed and inverse-column controls PASS; no new record census.


- lexicon/rule30_exterior_binary.py: GC1044 exact all-choice two-column repair by binary clauses;18,720 literal triples and324 constructions PASS. Actual-train pair01 forced; free-terminal positive retained. Further projection/halfwidth OPEN.

- `lexicon/rule30_cloud_chains.py` (Cloud, 2026-10-10, the owner's lead, side question): CH, the pattern read as one
  binary chain and split at §8.74's boundary B(t). CH-P0 .. CH-P3 HELD (orderly chain xz 0.077; random chain 1.0001,
  h_16 0.9975, density 0.5002, runs within 3.8% of 2^-L: a coin to every test); CH-P4 REFUTED (no compressible zone
  past B(t)). §8.80.


- lexicon/rule30_exterior_majority.py: GC1045 fixed-v closure diagnostic atT6 inconclusive, stopped; hand joint-track majority obstruction at every horizon, both phases. Three actual seeds and deleted-odd-bit controls PASS; no visible-language bound.


- lexicon/rule30_sl_collar.py: GC1046 mixed synchronized S/L four-column collar; P1/P2 HELD on1,280 complete cylinder cones,128 terminal countercontrols. Literal/packed PASS; finite coefficient types and interface units, no language census or all-depth bound.


- lexicon/rule30_sl_switch.py: GC1047 ordinary-L fifth-track selector and pair-zero transport; informed P3 HELD with P1 on1,024 complete cones,112 pair00; independent engines and ninth-bit countercontrols PASS. No solver or record bound.

- `lexicon/rule30_cloud_triangles.py` (Cloud, 2026-10-10, the owner's lead, side question): TA, white-triangle area by
  side and width at §8.74's front. TA-P0 .. TA-P3 HELD: the triangle law integrates to exactly 1/2 (proved); random side
  on the law by area to 1.5%; band largest 16, 95.7% in widths <= 8; a faint birth deficit in the first 32 diagonals
  past B(t). §8.81.

- lexicon/rule30_sl_successor.py: GC1048 L1 six-column slab and ninth-track successor gate; P1/P2/P3 HELD on8,192 complete cones, literal/packed and ninth-bit countercontrols PASS. Both successors occur; no record bound.

- lexicon/rule30_sl_ancestry.py: GC1049 entrance-sensitive successor clause;32 exact cones and retained countercontrols PASS. Several closure guesses refuted; actual no-refork UNKNOWN after nonvacuous1,024-cone sample. No wider scan proposed.

- lexicon/rule30_long_fork_gate.py: GC1050 complete L0-to-L1 fork gate, four thirteen-bit cylinders; hand proof,512 exact mux cones and256 prefix extremes, independent engines and unexpected controls PASS. No record bound.

- lexicon/rule30_sl_no_refork.py: GC1051 hand exclusion of actual L1-S-L0-L1 by translated ancestry shield;320 local cone controls, independent engines and relaxed countercontrol PASS. Three construction guesses REFUTED; GC1048 intermediate coefficient corrected, conclusions unchanged. All-depth bound open.

- lexicon/rule30_mature_fork_branch.py: GC1052 all-tail111010011 branch bars the next L1;128 complete local cones and intermediate relations PASS independently. Proposed other-branch gate REFUTED, startup exception retained. No mixed-word or solver scan.
- lexicon/rule30_long_successor_shield.py: GC1053 universal L0-to-L0 successor OR guard bars L0-L0-L1 by translated two-tick ancestry;448 local controls PASS, two engines. First unlifted countercontrol REFUTED; corrected ancestry and S-birth controls PASS. No record/membership scan.
- lexicon/rule30_short_fork_origin.py: GC1054 all-tail S111010001 output blocker and black-sixth short-image guard reduce mature forks to L0-S-L0-L1;1,152 complete local cones and intermediate independent controls PASS. Startup exemption retained; no mixed-word scan.
- lexicon/rule30_long_short_origin.py: GC1055 L0-S source-prefix OR guard,256 complete local cones and independent intermediate controls PASS; hand corollary confines L1 to first three typed S/L returns, at most once. Actual L1-S source countercontrol passes; no mixed-word census.

- lexicon/rule30_short_marker_decay.py: GC1056 finite SS sixth-marker monotonicity and mature fifth-track table;128 complete cones, intermediate independent controls and black-persistence/L1-origin countercontrols PASS. LL selector and all-depth closure remain open.

- lexicon/rule30_trace_prefix_repair.py: GC1057 frozen-initial-row repair REFUTED atW3,l5; exact trace01000 origin and edge-merger controls PASS. FirstW-1 preservation HELD only on1,024 conditionedW4,l7 cases; no uniform proof or larger scan.

- lexicon/rule30_collar_zero_lane.py: GC1072 exact rooted period32 front certifies three white propagation centres at K=12+32n; universal three-centre shield REFUTED. Four cycles and 256 independent actual controls pass; no language census.

- lexicon/rule30_long_high_past_gate.py: GC1073 high fifth-track LL forces origin sites 7,9 black; initial110 always returns S. 24 local identities and256 independent cones pass; failed no-past countercontrols retained.

- lexicon/rule30_short_high_selector.py: GC1074 exact mature SL high fifth-track origin gate; ninth-bit transport G=(f OR g) OR NOT(h OR i). 32 intermediate and independent gate controls pass; no mixed-word or record census.

- lexicon/rule30_high_101_shield.py: GC1075 all-tail 101 origin forces high then S, closing high mature SL successor; 15 local implications and 128 independent cones pass, failed early-row prediction retained.

- lexicon/rule30_high_ll_transport.py: GC1076 marker-conditioned high-LL transport; 48 local shields, 8 closing identities and 64 selected origins pass. Unconditional four-white and low-renewal shortcuts refuted; next-H sample absence is evidence only.

- lexicon/rule30_high_ll_no_repeat.py: GC1077 actual ancestry forbids adjacent high ordinary-long tracks; 16 local gates, 8 shields, 4 closing identities and 48 actual controls pass. Relaxed next-high witness isolates lost time-four equation; X exit retained.

- lexicon/rule30_core_short_bridge.py: GC1083 actual C-to101-toS-A sparse guard and all-tail high/short transport; local implications and literal/packed controls pass. Unrestricted 25-bit bridge lacks the core guard; three failed core constructions retained. No membership or record run.

- lexicon/rule30_core_escape_short.py: GC1084 hand core-to101 obstruction of short A; two exhaustive packets carry a sparse black bit.1,024 split,512 backward,80 packet and384 actual literal/packed controls pass. Prior short-reset and shield failures retained; no solver or record computation.

- lexicon/rule30_short_B_reset.py: GC1085 all-tail20-bit B-to101-toA-to001 bridge; six prefix updates and64 independent composed controls pass. B-only and white-pair shortcuts refuted; B-toSS already excluded by GC1052. Core preimage and prize bound open.

- lexicon/rule30_core_B_sparse_guard.py: GC1086 core high11=1 image forces B white11 -> white12; B-to101-toA needs black12.256 high,64 scalar and32 independent short controls pass; broader packet closure refuted. White-eleventh core branch and all-depth closure open.

- lexicon/rule30_mixed_core_invariant.py: GC1087 actual white-eleventh escape and broader high100 shield close C/J/guarded-B at every renewal length; local controls pass, counterfeit past retained. No SS/high LL after C; upstream admission and all-depth record bound open.

- lexicon/rule30_B_reset_SS_certificate.py: GC1088 all-tail B-reset cylinder returns111 at32 and black-marker SS at42..48;96 causal implications and32 independent controls pass. Immediate admission and A-label guards refuted; eventual admission open.

- lexicon/rule30_black_SS_A_reset.py: GC1089 exact mature black-SS whitening-to-A-to001 selector;1,536 local cones,256 backward bands and64 composed controls pass. Whitening admission shortcut refuted; actual same-history low gate remains open.

- lexicon/rule30_black_SS_white_A_admission.py: GC1090 inherited A13=A11 and low10white; white branch00101 admits C by causal shield.128/256/128 local packets,20 prefix implications and64 independent histories pass; black branch open.

- lexicon/rule30_black_SS_high_restart.py: GC1091 black A low00100; actual all-tail SS-SL-D-H-X cylinder.256 packets,8 identities,84 fresh-right implications and64 independent controls pass; universal admission open.

- lexicon/rule30_forced_odd_period_bridge.py: GC1092 all-odd-q alternating-white ancestry implies nilpotency after4, loss q+4.352 finite fixtures,4 local identities,4 nilpotent patterns and6 exact periodic controls pass; even-q counterexample and periodic scope distinction retained.

- lexicon/rule30_two_step_parity_bridge.py: GC1093 exact16-state two-parity second-image intersection is zero/singleton-period3. All-odd-q second-slice extinction by4, loss q+14;64 packet/352 exterior controls pass. XOR-linear prediction refuted; later-image mergers open.

- lexicon/rule30_third_image_parity_bridge.py: GC1094 exact third-image parity intersection is zero/one;64-state height certificate,256 literal packets and640 exterior fixtures pass. Odd-period third slice dies by4; all-time phase persistence open.

- lexicon/rule30_parity_carrier_exit.py: GC1095 both third-image parity classes forbid0010; actual eight-cycle leaves their union by its fourth update.64 packets/256 exterior controls pass; original six-cycle prediction refuted, all column traces fail period2.

- lexicon/rule30_black_A_ancestry_guard.py: GC1096 fresh black-A all-tail restart; four-step past excludes its20-cell packet.52 implications,64 histories, exact inverse tree and632-parent instrument control pass; actual SS restart exclusion open.

- lexicon/rule30_black_A_no_restart.py: GC1097 complete mature black-A S-D-H-A exclusion; four selector parents,248 low/384 A packets,64 actual histories pass. Uniform in even age>=4; subsequent B guard open.

- lexicon/rule30_intel_forced_only.py (with forced_only_x4.c and rule30_intel_layer_dfa.py): FO, the forced-only records
  R^F(d) of the check-free conjecture (8.88), exact, both phases, over X_4, the golden-mean control, the twelve-word
  class and the layer languages of width 8, 12, 16 and 20 (own automata, the record's state counts), by a breadth-first
  walk over prefixes with 8.38's masked-pair merging and a depth-first tail; FO-P0..P7 registered before the runs; the
  per-level distinct-state counts measure the merge rate of K-prefixes; every death named by its word (11, 00000, a
  longer one). Intel, 2026-10-11.
- lexicon/rule30_intel_strip_threshold.py (with rule30_intel_strip_trace.c): SX, the exactness thresholds L(W) of
  the strip form for full traces, both phases (KIMI-QUESTIONS-4 Q1, door D4): real traces from all 2^N rows,
  bit-sliced; strip traces by a subset walk; the pairing L(2k) = L(2k+1), the extra traces at L(W) + 1 and their least
  excluding widths (rule30_intel_strip_extras.txt, with strip witnesses), and the column-tableau death profile of the
  tight extras (rule30_intel_strip_tableau.txt); SX-C0..P10 registered before the runs. rule30_intel_trace_grow.py
  grows the real traces by SAT (pysat, CaDiCaL) and gives every minimal absent trace its w(f), so L(W) to W = 39
  (rule30_intel_minimal_absent_traces.txt).
  rule30_intel_mfw_dfa.py builds FO's exact-language automaton X_K from the handoff's minimal forbidden words
  (FO-P8). Intel, 2026-10-11.
- lexicon/rule30_intel_carry.py (with rule30_intel_carry.c): CAR, the carry of Rule 30 (KIMI-QUESTIONS-5): exhaustive
  rings to n = 28 for the run-count matrix and its Markov test, the single cell's Pascal-masked carries to t = 65,536,
  sampled and exact column-carry laws under the coin measure; the identity c_t(i) = x_t(i+1) x_{t+1}(i+1). CAR-C0..P10
  registered before their runs. Intel, 2026-10-11.

- lexicon/rule30_black_A_B_admission.py: GC1098 first-B sparse admission and white H101 marker;112 high/108 low/240 short parents, then empty S4;76 implications/128 independent histories pass. Incorrect D shields corrected; later SS block open.

- lexicon/rule30_white_SS_exit_guard.py: GC1099 D-H-SS bad B requires1101001, which has no four-white-fifth past; one-SS sparse B guard sketch.140 causal implications/320 independent histories pass. Fresh low forces two white SS; capped actual-black-SS ancestry UNKNOWN, arbitrary-block admission OPEN.

- lexicon/rule30_black_A_white_SS_entrance.py: GC1100 actual41-cell SS origin forces black A6, white SS32, black A38;88 implications/64 histories pass. Independently confirms CL275 full-strip B guard; no-entrance refuted, reset budget OPEN.

- lexicon/rule30_delayed_A_strip_rank.py: GC1101 joint20-cell macro relation,384 typed states/273 edges, explicit rank<=2; consecutive one-white-SS black11 A resets bounded by2 (sketch).5120 selector cones/eight scalar set flows pass; extra A types retained, variable SS lengths OPEN.

- lexicon/rule30_delayed_A_SS_star_rank.py: GC1102 all-k fixed point,137 SS packets/244 strictly decreasing inner edges, SS blocks<=3 after typed A-S-D-H (sketch). Reset rank fails:742 A edges, two-SS self-loop. One loop path violates boundary evolution; actual lift OPEN.

- lexicon/rule30_delayed_A_boundary_memory.py: GC1103 named loop survives joint boundary; existing20-cell graph has one output-periodic SCC. Fixed potential bounds exceptional SS counts by2; typed finite-left deadline7J+796 (sketch). Scalar controls pass.

- lexicon/rule30_delayed_A_exit_admission.py: GC1104 all-length delayed SS terminal image has101 black A/38 white A, no B. White exits force S-D and C within16 ticks; prefix15 plus complementary OR shield (PROVED CL283).

- lexicon/rule30_black_A_111_diversion.py: GC1105 all-length111/black-SS relation replenishes the old rank and retains an M3 self-loop;20-cell extension refuted, actual lift open. Scalar and actual-history controls pass; no new high-run theorem.

- lexicon/rule30_111_A_joint_boundary.py: GC1106 joint site21 retains M3 and mixed M2 recurrence; two explicit234-tick scalar-verified closed walks have distinct output, giving model entropy>=1/234. Five-SS negative control retained; actual lift open.

- lexicon/rule30_sl_left_short_marker.py: GC1107 exact nonlinear S selector at left12;41 sparse cones,16 lifts and literal triangles pass; XOR/no11 shortcuts refuted. Depth transport OPEN.

- lexicon/rule30_sl_short_marker_inverse.py: GC1108 lossless nonlinear short-marker inverse under noLLL;131 cyclic controls,110 isolated-L cases; FE/EF left12 first differ at34. Entropy unchanged; depth update OPEN.

- lexicon/rule30_sl_carrier_depth_return.py: GC1109 eight-depth canonical carrier return refuted; complete SLL cone forces left19 phase10 and left20 even1. Endpoint-only check misses it; all-depth bound OPEN.

- lexicon/rule30_sl_phase_collision.py: GC1110 exact sparse phase polynomial; S/L reduces left20 even trace to a positive renewal code with no00. Cubic SS term essential;88 sparse and640 S/L phase controls pass. Fixed-depth shield, not a record bound.

- lexicon/rule30_m2_reported_cut_cap.py: GC1111 eight M2 returns cover all 19 cyclic 120 factors at positive age; seven miss 5. Typed101 cap23 returns/886 ticks derived from L591 report, exact absence receipt pending; no membership query.

- lexicon/rule30_mixed_m2_overlap.py: GC1112 sharp 87-sample pure-M2 overlap for every FE/EF concatenation; LL-spacing hand proof and complete falling-rank product. M2-only cuts >=88 inert on this model; no membership test.

- lexicon/rule30_minimal_mixed_bridge.py: GC1113 bare 196-tick mixed generators, sharp M2 overlap68; E_m overlap68+19m. Reported120 absence would cap optional m<=3/bridge266 ticks, not reentries; exact receipt pending.

- lexicon/rule30_fixed_m2_cut_charge.py: GC1114 corrected exact114 cut gives18 macros/672 ticks (43-state certificate); optional2/228 uses fixed endpoint1. Original620/16 used wrong rotation; L627 absence read, charge review pending.

- lexicon/rule30_sl_positive_code_inverse.py: GC1115 nonlinear L detector and 22-even-sample causal inverse of dense left20 code under no S^5; isolated-L/four-S controls. Unbounded-S inverse and plain image reuse fail; depth closure open.

- lexicon/rule30_sl_age_spatial_interface.py: GC1116 exact22-state paired-L age language carries paired19..21; odd22 branches at B10/B13,24 edges repair this interface. All44 local paths and independent macro spellings agree; all-depth closure open.

- lexicon/rule30_sl_pair_marker_code.py: GC1117 left22 even pair00 marker, blocks C_k for arbitrary k>=1,13-past inverse retaining pure-S phase.1782 literal controls; fixed-depth language only, all-depth closure open.

- lexicon/rule30_mixed_bounded_period_excess.py: GC1118 bare mixed recoding has visible periodic excess<=139 at ALL periods (hand proof); 316 seam windows and28608 overlaps are controls only. GC706 inequalities do not exclude it for J>=278; no actual realization.

- lexicon/rule30_pair_code_joint_phase.py: GC1119 paired22 odd observes reset; exact18-state new lookahead at24 pays even BLACK counter reset.15-state quotient adds an unpaid k=0 branch; exact bare walks refute full past-only closure. One interface/phase, no all-depth certificate.

- lexicon/rule30_mixed_cut_transfer.py: GC1121 E0 is a common76-sample prefix of ALL optional-wait bridges;117-word bans miss bare recurrence by marker spacing. Symbolic proofs with complete matching controls; no actual membership.

- lexicon/rule30_f69_macro_guard.py: GC1123 f69 exactly forbids continued122 for all k>=1; four-state finite guard retains terminal122 and endpoint1.341 independent cones; M3 survives, no actual membership test.

- lexicon/rule30_111_cut_markers.py: GC1124 certified54/56/65 give continued31/121/312 and exact finite endpoint guards for all k>=1;65 redundant beside54 here.3906 controls; short mixed cycles cut, full splice coverage open.

- lexicon/rule30_cloud_cut_product28.py: CL303 complete cut product over the whole width-28 collar graph (6,431 states, 870,080 labelled macro edges) with the eleven certified cuts (L631's nine, L627's 114, L628's 117) via an Aho-Corasick automaton carried across macro seams: one cyclic component survives, the pure-M3 self-loops (62 product states, 1,073 edges, branch 111); L631's nine alone also leave the 10-state pure-M2 component. After an M1 edge the next label is always 2; realised pairs 12, 21, 23, 31, 33. Relaxation result, not an all-depth bound. ADDED (CL306): GC1126's H-low macro N as a fourth edge type: from all 98,304 A-type rows at width 28, 96,029 pairs, 185 sources outside the macro graph, 681 endpoints, on no cycle, never repeatable; the product with N is unchanged. ADDED (CL318, CL319): transient residence (outside the recurrent components the graph is acyclic; into a component within 2 macros / 88 ticks, no typed continuation within 3 macros / 246 ticks) and the total typed duration with the 22 pure-M3 300-sample windows as cuts: acyclic product, longest typed path 13 macros / 686 ticks.
- lexicon/rule30_macro_successor_gate.py: GC1125 complete32-state joint21 endpoint restrictions1->2 and no3->2 for all branches at k1..3; cut normal form gives actual J+640 in the restricted core.29524 controls; all-k/admission open.

- lexicon/rule30_111_low_white_return.py: GC1126 H-low-D101 escape retains 1530 A-origin/end pairs; inherited rank bounds SS residence by two, all A returns exactly k=2 (58 ticks). Scalar path and all-count origin controls; actual lift open.

- lexicon/rule30_111_low_reset_gate.py: GC1127 N and M3 share a 20-cell self-packet; NF/FN give distinct 102-tick loops. FIRST-L spacings 5/19/22 with no consecutive 19 evade all eleven cuts at every length. 511 controls; actual lifting open.

- lexicon/rule30_recurrent_low_exit_gate.py: GC1128 complete joint 21 origin gate for omitted H-low X and second 111 exits; both require the single recurrent prefix 111010001110111000011. All 32 scalar labelled flows and three reconstructed paths pass. Width28 component membership and return remain open.

- lexicon/rule30_pointed_origin_past.py: GC1129 P = 111010001110111000011 has a 25-bit causal parent at clamped age 4, refuting the four-step origin guard. Complete inverse edges and 32 scalar/literal/packed tail controls; no later-excursion lift claim.

- `lexicon/rule30_N_terminal_admission.py`: GC1130 complete N-ancestry white-SS terminals; AP13 return at 58 or inherited C/J admission by 74. Existing carrier/rank reused; unfiltered scalar control, no solver or membership run.

- `lexicon/rule30_N_H_exit_gate.py`: GC1131 complete pre-SS H classification; white-A interruption misses inherited admission guard and can restart high111 after S-D. Original-labelled 62-tick scalar counter; no actual lift or recurrent width-28 exit claim.

- `lexicon/rule30_white_A_recurrent_origin.py`: GC1132 joint-21 origin gate for the S-separated white-A restart; only P/Q, with independent scalar flows for all 32 origins and a full 62-tick witness. No wider graph or membership run.

- `lexicon/rule30_white_A_restart_return.py`: GC1133 all-count joint-21 return composition of the white-A restart; completed before restart pause, retained as relaxation only after CL316 excludes its productive recurrent origins. No active widening or realization follow-up.

- lexicon/rule30_fresh_white_A_SS_past.py: GC1134 complete two-tick exclusion of the retained fresh white-A counter; four-parent table, 32 boundary controls and 12 mature contrast parents. White-SS-specific test vacuous; general admission open.

- lexicon/rule30_unrooted_white_SS_admission.py: GC1135 complete mature white-SS to white-A high-LL counter; arbitrary-exterior cone, two-tick predecessor and GC1080 B composition. Refutes SS-only admission guard, not eventual admission.

- lexicon/rule30_white_A_high_LL_guard.py: GC1136 exact two-family white-A25 high-LL selector; complete8192 causal cones and independent six-tick inverse. Case B only; prefix23-only guard refuted.

- lexicon/rule30_white_A_high_sparse_guard.py: GC1137 exact12/16 sparse split after the white-A selector; full causal cones and mature SS counter. Unconditional stopping bit fails; contiguous-prefix shortcut loses two sources. No repeat inferred.

- lexicon/rule30_white_A_second_high.py: GC1138 all-tail common tick21 black14 on16 negative entrances;14 direct prefixes and four26-cell leaves. Complete16384 cones agree; all28 white-A gate entrances permit at most one high LL per ordinary-long run, with later shorts outside scope.

- lexicon/rule30_001000_mixed_admission.py: GC1139 original white-A negative16 force low13=0 at26 and admit010 by36;273-leaf all-tail cover. Fresh low12 and common mid14 admission fail; actual lineage preserved. Mixed closure imported from GC1087.

- lexicon/rule30_positive_A_mixed_exit.py: GC1140 original positive12 white-A entrances admit mixed core by52 or exit X26;1512-leaf all-tail source cover. Actual admission36 counter retained;6048 independent controls, mature scope explicit.

- lexicon/rule30_cloud_positive_entrances.py: CL329/CL330 census of the twelve positive white-A entrances (GC1136 family, low pair 01): bit-sliced over all 196,608 exteriors, site 15 = 1 at 16, site 14 splits 98,304 / 98,304, the H track realised everywhere, low rows at 26 (1110010010001, 1110010010000, 1110010011101), exact discharges to C010, the 101 class and the X route at 36; at width 28 with origin labels the 101 branch gives 946 B-prefix rows at 46 and nothing in thirty free ticks, the X branch 264 / 662 / 1,519 rows. Its registered prediction (black AP13 and a white SS entrance within thirty free ticks of the X rows) was REFUTED: none of either; the unexpected check fired, 102 rows 1110011110100 at tick 66 (CL331).

- lexicon/rule30_white_A_non_LL_admission.py: GC1141 exact non-LL A dispatch3392 C16/676 high111; six-source-bit guard and hand black-marker SS transport. One source39 cylinder forces guarded B44; general676 admission remains open.

- lexicon/rule30_cloud_x_route_realcone.py: CL331 to CL335 real-cone sampler for the X exit of the twelve positive white-A entrances (no strip relaxation; 2^24 random exteriors per cylinder, exact first cells to 106, 132 or 238 cells wide). Results: X is fixed by the cylinder in ten of twelve (five always, two half, five never); every X cone shows the forced rows at 26, 36, 46; the pin 1110011110100 at 66 in 3.2 percent of X cones, one chain SS 94, SS 100, white-eleventh A 106 in 3.17 percent, the white-A origin row back at 106 in 1.83 percent and at no other even tick; the returned origins carry ten rigid patterns outside GC1136's gate (mode 'family'), all admitting the C core at 122, with no pin at 172, no SS at 200 or 206, no origin at 212 and no A of either colour in those cones through 212 (mode 'chain'). P1 (frequency 10^-5..10^-3) refuted by a factor thirty; Q1 (family patterns) and Q5 (background rate) refuted; the rest held.

- lexicon/rule30_cloud_gc1140_41_check.py: CL334 independent second read of GC1140 and GC1141 with GPT's definitions re-implemented: GC1140's cover re-derived (3,012 nodes, 1,512 leaves, digest 9b78f672..., X weights per root = CL332's X cylinders), its 33-cell counter's forced rows reproduced, 201M real cones with no uncovered tail and admission always by 46; GC1141's dispatch (3,392 C, 676 high 111, no 101), six-bit guard, 676 x 16,384 black markers with the H track, witness and 39-cell certificate (B at 44 all tails, C010 at 50 all tails). All predictions held.
- lexicon/rule30_black_SS_B_exit.py: GC1142 complete1536-cone bad-B classification and H111 inverse exclude all17 violations; guarded first-SS B is nonvacuous. Actual whitening-SS counter retained; generic last-black guard and two-step shortcuts fail.

- lexicon/rule30_cloud_gc1142_check.py: CL336 independent second read of GC1142: the 1,536 black-S cones (240 B, 17 bad B, 480 whitening SS), a forward census of all 524,288 actual high-111 cones (H track and shields forced, no bad-B source reached, 80,256 whitening-SS, time-10 split 111011101 / 111001001 / 111011111 / 111001010), both 28-cell certificates for every completion, and an own inverse reproducing GPT's layer counts and the 0000 / 0100 time-1 prefixes. All predictions held.
- lexicon/rule30_H111_SS_star_B_guard.py: GC1143 existing20-cell H111 carrier reaches unguarded B after3 SS; scalar path retained. Selected boundary assignment fails five updates; exact named-terminal inverse UNKNOWN at200000 cap, no lift absence inferred.

- lexicon/rule30_pin13_SS_exit_guard.py: GC1144 pin13 existing20-cell least fixed point519 states/1530 SS edges; all29 white-A and172 B terminals guarded for every chain length. Strong total-admission/acyclic predictions fail; black-A and H-low branches retained. Every scalar edge and four actual projection controls pass.
- lexicon/rule30_cloud_sea_rates.py: CL337/CL339 control for the X-cone rates: 2^24 fair-coin rows beside the alternating wall, 212 ticks; rates per row per tick of black AP13 (6.8e-4 at even ticks 48..212, twice fair coin), white-A origin (8.0e-5), white-eleventh A, white SS entrance (2.3e-3), the pin 1110011110100 (6.3e-6, twenty times rarer than fair), high 111 and black-marker S; at black-wall ticks no A row of either colour and no white SS entrance ever. S1 held, S2 half, S3 refuted.

- lexicon/rule30_white_A_H13_ancestry.py: GC1145 complete46-leaf causal cover sends676 non-LL A25 assignments to H13=1110011111110 and28 high-LL to1110011111000. Exact selector composition/184 controls pass. X-pin transfer fails; two-image SS carrier still admits badB after3 shorts, scalar path retained, original-A lift open.
- lexicon/rule30_cloud_gc1144_check.py: CL341 independent second read of GC1144: the width-20 carrier of the pin 1110011110100 rebuilt from Cloud's strip machinery (128 packets, 161 H ends, 87 SS entrants, 519 SS states, 1,530 edges, 267 terminals = 66 black A + 172 guarded B + 29 white A, GPT's digest, 214 surviving vertices), the exit dispatch checked directly on all completions (white-A terminals give C at +16, B terminals admit at +6), GPT's counter path and controls, and CL335's real chain found at exact depths 3, 4, 5. All predictions held.

- lexicon/rule30_cloud_gc1145_check.py: CL342 independent second read of GC1145 over the complete causal cone (4,096 source-25 assignments x 16 completions): the white-A source's 13-cell image at 16 is 1110011111110 on all 676 non-LL high assignments and 1110011111000 on all 28 LL ones, the 3,392 C sources give thirteen images beginning 111001010 or 111001100, GC1144's pin never appears; an own certificate cover gives 37 + 9 = 46 high-branch leaves of weights 676 and 28. Both predictions held.

- lexicon/rule30_counter_path_boundary_guard.py: GC1146 all boundary assignments reject the named GC1143/1145 bad-B paths at H ticks3/4: pair10 ->00 ->10 contradicts next-column update. Scalar8 truth table, eight actual histories and an ambiguous-boundary negative control pass; alternate paths/terminal reachability remain open.

- lexicon/rule30_whitening_B_transport.py: GC1147 realized blackSS/whiteSS/badB cylinder refutes whitening-only transport; causal induction and128 full controls pass. Immediate H111 image excludes this source; original676 OPEN.

- lexicon/rule30_cloud_gc1146_check.py: CL345 second read of GC1146: the two-time boundary contradiction on every width-20 H path to each named macro endpoint (2 of 4 and 3 of 15 paths pass it), and a complete enumeration of all 2^28 real exteriors through each named 28-tick path: GC1143's bad B is unreachable (every exterior dies at tick 22), GC1145's is reached by 933,888 exteriors of its 20-cell source.

- lexicon/rule30_cloud_actual_carrier.py: CL346 width-20 SS carrier from the ACTUAL tick-16 images of white-A origins (198 rows, 38 high: 29 non-LL, 9 LL): 614 states, 1,377 edges, 459 terminals (68 black A, 349 guarded B, 13 bad B at SS depth 3, 29 white A); the LL rows end H in the low row with no SS entrant.

- lexicon/rule30_cloud_badB_lift.py: CL346 carrier-pruned depth-first search over origin cells for an actual non-LL white-A origin reaching an unguarded B after k SS blocks: FOUND for k = 3 (origin 1110100011011010010010000100100000000000000000000000000000000000, all tails, bad B 11101001100101110101 at tick 44); none for k = 4..8 even in the relaxation.
- lexicon/rule30_SS_record_residence.py: GC1148 all-depth hand zero-triangle/ring proof gives L<=2a+5 OR N<=d+a+5 and indexed record-conditioned visible restrictions;127 prefix tableaux,1524 truncated controls PASS. Global R_real/admission OPEN.

- lexicon/rule30_cloud_witness_fate.py: CL346/CL347 fate of the all-tail witness (a white-A origin of the 676 class with an unguarded B at 44): 2^24 tails to tick 212; its first cells are determined through 110 (white SS entrances at 60 and 66, black AP13 at 72, low row at 78, the high-111 image again at 88, black-marker S at 98); sampled rates and the first mixed-core row per tail (none by 80, 62 percent by 180). F1, F3 refuted, F2 held.

- lexicon/rule30_cloud_gc1148_check.py: CL348 second read of GC1148: the ring facts hold (shift 14, gap 5) but the finite-determination step fails for every N from 3 to 18 (the first N column-1 samples fix sites 1..3 only) and the inequality L <= 2a+5 OR N <= d+a+5 has 24 violations in 357 small instances (e.g. 111100000000 with sites 5..10 white gives the first eleven samples of 110100). GC1148 and GC1149 REFUTED.

- lexicon/rule30_record_orientation_control.py: GC1152 signed-site controls on CL348/349 counters; both left targets contain black, both right targets white; independent unclamped scalar/packed replay PASS. All-depth sketches await corrected review.

- lexicon/rule30_mixed_spatial_gap_control.py: GC1153 fixed qA/qAAA counter to uniform-six mixed spatial-gap bound; actual L579 qA forces left30..36 white; pure rings, packed/literal inverse and8 endpoint controls PASS.

- lexicon/rule30_cloud_gc1148_check.py: CORRECTION (CL350): this probe tested the RIGHT row (whites at positive sites, comparison with the ring at positive sites); GC1148's record is the LEFT row, which columns 0 and 1 determine leftward. Its ring facts stand; its refutation verdict is withdrawn. The corrected test is rule30_cloud_record_left_check.py.

- lexicon/rule30_cloud_record_left_check.py: CL350 corrected check of GC1148 and GC1151 in GPT's orientation: the leftward determination step holds exactly (N = 6, 10, 14), no violation of either inequality over all column-1 sequences to length 22 at small d, a, and the maximal left white run reachable for given samples stays below the bound. GC1148 confirmed as a proof sketch; the L ring's gap 6 not reproduced here.

- lexicon/rule30_record_period_comparators.py: GC1154 compact indexed repeat restrictions on untyped white-time words under zero-record hypotheses;1080 inverse controls/17160 specifications/24 large-integer endpoints PASS. Theorem B reused; closure OPEN.

- lexicon/rule30_record_endpoint_mask.py: GC1155 actual139 stopping certificate, left156 forced before next white sample;8 right tails/4 raw terminals and unclamped failure156 PASS. All10 L18 comparator controls pass;125p1 white-pivot contrast. No record search.

- lexicon/rule30_record_white_endpoint.py: GC1156 sharp132 white terminal pinned by right prefix145; all 16 completions force left149 black, arbitrary-exterior enclosure v148={0}, scalar/packed/unclamped controls PASS. Algebraic pivot still toggles it; one cylinder, no record bound.

- lexicon/rule30_record_root_endpoint_cut.py: GC1157 fixed132 root's white-ending extension closes the certified 24-bit cut at visible51, physical102; direct/suffix lookup and sixteen inverse controls on both known roots PASS. All-realization consequence proved by CL359; no new cut or record bound.

- lexicon/rule30_cloud_gc1154_check.py: CL356 targeted check of GC1154's carrying step: a period-m visible word's fixed left cells have white gap at most 4m - 2, every block for m = 1..5 to depth 240 (gaps 1, 6, 5, 6, 9; tight at m = 2), odd samples masked exactly, windows fix their first 2C cells. Its first run had the leftward relation's columns swapped; the control caught it.
- lexicon/rule30_cloud_gc1155_check.py: CL356 targeted check of GC1155 on Local's d = 133 L = 23 witness: depth 156 black, read from the 78 even-time samples (30 flip it singly, earliest t = 24), odd samples and c[155] masked, sites 156..158 powerless, clock to 156 unclamped, break at 156 when depth 156 is made white.
- lexicon/rule30_cloud_gc1156_check.py: CL356 targeted check of GC1156 on Local's sharp d = 132 block: all 16 completions of sites 146..149 keep c[148] white and depth 149 black, three-valued propagation keeps the unknown front at site 82 or beyond through tick 149, clock to 149, break at 149 when depth 149 is white.
- lexicon/rule30_cloud_other_wheels.py: CL357 EXPLORATORY (the owner): other wheels in columns -40..40 of the real pattern? Block complexity and best-period coverage with the clamped wheel and a coin as controls; every column coin-like (p(8) 256, p(16) 25,500..25,900, coverage 0.21..0.24 at P = 2, 0 at 56); the control wheel reads p(8) 13..22, coverage 1.0 at P = 10.
- lexicon/rule30_cloud_wheel_centre.py: CL357 registered EXPLORATORY (the owner): the unkicked wheel word U (period 56) as the clamped centre column instead of 0101; column 1's structure, lock census and the forced left row's longest white run, against 0101 and a coin. Result in CL358.
- lexicon/rule30_cloud_wheel_centre.py: CL358 result: beside the U centre column 1 has p(8) 107..111, p(16) about 500, best coverage 0.39..0.47 at P = 10 by the word 0010110111 (not the L word), no lock in 64 halves, left white runs to depth 300 of 5..10 (0101: 6..8); W1, W2 held, W3 refuted.

- lexicon/rule30_record_seeded_decoder.py: GC1158 exact seeded-image presentation PROVED (CL361); 64 fixed-root controls at eight depths PASS, k4 root-image collision distinguishes cut residuals, black-pivot corruption rejects. State count is not a record bound; harness indentation failure retained.
- lexicon/rule30_cloud_gc1157_check.py: CL359 targeted check of GC1157: the sharp-132 word's white-ending extension q+1 carries the certified cut 100100001001000010000101 at visible index 51 (tick 102), its last letter q74; q and q+0 carry no certified phase-0 word; the cut is certified in both phases.
- lexicon/rule30_cloud_cone_render.py: CL360 render of the clamped-centre left half (0101 and U) with the coherence cones tinted by the smallest lag at which the centre and column 1 repeat over the cell's window; the owner's regular patches are the cones (0101: 25.8 percent of the drawn cells, lag 4 13.6; U: 23.2, lag 10 8.8, lag 56 8.0). Writes PNGs to a given directory, outside git.

- lexicon/rule30_record_origin_quotient.py: GC1159 cut-preserving first-bit quotient SKETCH using C7; actual139 root normalization creates00000 but preserves h4. Eight shielding/eight gate negatives and17 direct/subset controls PASS; no record bound.
- lexicon/rule30_cloud_gc1158_check.py: CL361 targeted check of GC1158's seeded inverse decoder by an independent implementation and exhaustive enumeration (phases 0 and 1, k 1..5, N 1..5, certified words to 10 and the toy cut): forward and converse exact, the unused terminal input inert, the k = 4 coalescence example reproduced, live states under 2 S 2^ceil((k-1)/2).
- lexicon/rule30_cloud_solid_rows.py: CL363 companion to the proposition that no finite Rule 30 pattern ever reaches a solid row: ring preimages of the two solid rows and the basin of death for sizes 3..14 (deaths beyond the trivial pair only when 3 divides the size), and the finite solid rows 1^(3j+3) with their unique ancestors 1(001)^j.
- lexicon/rule30_cloud_gc1159_check.py: CL364 targeted check of GC1159's first-bit quotient: time-0 algebra (X_3(0) = 1 - q1, X_4(0) = q0 q1), image equality under a first-bit flip for k >= 4 with the no11 gate in phase 0 (none without the gate or in phase 1), exact existential quotient against ordinary normalisation (strict subset once 00000 fits), the residual-subset guard, and Local's depth-139 witness.

- lexicon/rule30_growth_injectivity_control.py: GC1165 four-state inference control, finite injectivity and exact outward growth with shared period2 centre columns;1056 literal/Laurent/closed-form controls and two negatives PASS. All-time algebra PROVED (Local L654); no Rule30 candidate or Local census.

- lexicon/rule30_prefix_arrival.py: GC1167 diagonal defect identity;2016 short controls, two fixed cylinders; every P20 repeat fails at34 in phase1 by the cone. CPU, <1 s; controls COMPUTED, all-tail hand step PROVED (Local L658).

- lexicon/rule30_prefix_realization.py: GC1168 two low20 fitted-champion cylinders force visible11 at17/19, excluding a genuine centre clock through20; literal/packed/inverse controls and8 right triples PASS. CPU, <1 s; hand cone/endpoint step PROVED (Local L661).

- lexicon/rule30_phase_prepend_guard.py: GC1169 actual B word100101 blocks both S prepends by0100101/11; ordinary finite clock0..12, formal shrinking-zero/P ancestry,2047 residual/direct controls PASS. CPU, <1 s; hand lift scope PROVED (Local L663).

- lexicon/rule30_birth_parent_language.py: GC1170 child-phase cut automata for formal birth parents;4094 direct/machine and252 shift controls PASS; retains actual-child counterexamples. CPU, <1 s; all-depth image/filter step PROVED (Local L665).

- lexicon/rule30_origin_guard_horizon.py: GC1172 finite first-bit prefix guard, K-1 surviving-origin coalescence; 2047 controls and K44 dead-origin restart countercontrol PASS. CPU, <1 s; hand guard PROVED (Local L666); no record bound.

- lexicon/rule30_sampled_white_wall.py: GC1173 two-step zero-wall projection fails on two known actual root triples; 16 literal/folded checks PASS. CPU, <1 s; keeps the hidden left neighbour; no record bound.

- lexicon/rule30_canonical_parent_budget.py: GC1174 canonical ancestry forces checkerboard through n+p; inherited zeros allow n <= floor((d-p)/2). 540 independent forward/inverse controls and the actual d3 countercontrol PASS; hand budget PROVED (Local L667).

- lexicon/rule30_extremal_p_corner.py: GC1176 three named corner controls and closed six-diagonal period16 orbit; cores>=7 excluded except r=9/13 mod16, transfer PROVED (Local L668). CPU, <1 s; shorter-period and universal five-tick predictions REFUTED; no longer scan.

- lexicon/rule30_corner_two_cell.py: GC1177 extremal P child prefix is a crop of ordinary seed11 at T=2r-p; 80 literal/clamped prefix controls PASS, all-depth induction PROVED (Local L668). CPU, <1 s; black-child centre and actual B100101 exterior guards retained.

- lexicon/rule30_corner_window_period.py: GC1178 fixed-h corner window has explicit modulus M_h; five h3 period aliases and stopped-word controls PASS, all-depth coverage SKETCH. CPU, <1 s; no larger window or deadline scan.

- lexicon/rule30_extremal_p_corner_read.py: Local's L668 read of GC1176/GC1177 by direct simulation: alignment (640 cases), locality and the table (r <= 256), the seed-11 crop (r <= 64) HELD; GC1176's residues 9 and 13 close with a ten-cell core on the clock and no11 alone; W1..W3 the white-wall corner; M1 GC1178's modulus for h = 3..8 (8.97, L668..L670). CPU, about a minute.

- lexicon/rule30_second_oldest_census.py: Local's census for GC1181's two odd-class second-oldest profiles: hand facts and crop normal forms HELD (q <= 48); both profiles CLOSED in both phases by class (purely periodic seed edge), Q within 4..5 child ticks, P within 15..16 (q-period 256); no survivor by direct simulation to q = 300 (8.97, L671). CPU, seconds.

- lexicon/rule30_birth_deficit_census.py: Local's closure attempt for GC1184's fixed-deficit profiles (gaps enumerated): representation HELD for every gap to j = 3; j = 1 control and j = 2 (the 18 third-oldest profiles, both phases) ALL CLOSED, windows 4..22; no survivor by direct simulation to N = 120 (8.97, L672). CPU, 13 s.

- lexicon/rule30_young_birth_zero_ray.py: GC1199 one fixed age1 depth125 prefix; four boundary packets, integer/literal agreement to200, certified38-bit cut at145 forces the next left cell black. All-tail carrying step SKETCH; outside-band clock repair retained, no record census.

- mahler/mahler_gpt_review.py: GC1221 fixed-input review of Local's census; independent G51 windows verify saved horizons 120/137, two early-death chunk multiplicities and zero exclusion; two overflowing 128-bit parity controls. CPU, temporary C build, seconds; no census replay.

- `mahler/mahler_gpt_dual_review.py`: L712 fixed negative-horizon, sign, chunk-mass and excluded-boundary controls (GC1230.1); temporary build, no census.

- `mahler/mahler_gpt_sign_review.py`: independent direct initial-window and ternary-unit counterchecks of Cloud8.109/8.110; exact finite shadows, negative exponents, valuation bounds and three countercontrols. Preregistered, NOT RUN.

- `mahler/mahler_gpt_sign_review.py`: GC1246 outcome, registered de3b5c1a; SR1-SR5 pass12 depths/324 Mahler/260 ternary-unit comparisons/9920 valuation checks, all three countercontrols rejected. No infinite-set converse follows from finite tables.

- `mahler/ternary_gpt_power_converse.py`: GC1248 registered S7 digit-by-digit nonlinear converse controls; signed exponents, shifted precision, wrong-sign seeds and ordinary-integer countercontrol. NOT RUN.

- `mahler/ternary_gpt_power_converse.py`: GC1249 outcome at registered bounds:480 paths/43920 extensions,3398 locally admissible prefixes; shifted-digit controls pass,66 wrong-sign seeds and omitted-shift rule rejected;4^4=256 control passes. Converse hand proof awaits second reader.

- `mahler/mahler_gpt_joint_extension_review.py`: GC1250 preregistered exact small-window kill test of ternary-to-Mahler no-dead-end transfer, no Cloud constructor or periodic census. NOT RUN.

- `mahler/mahler_gpt_joint_extension_review.py`: GC1251-1252 outcomes; exact e5 dead end(T7,r9) rejects direct transfer; thirteen addendum registered30c56a34 gives odd extinction at7 and28 even-prefix bijections. G296 finite-plateau proof and13 certificate await independent review.

- `prizes/normal_ca_playback.py`: GC1270-1271 eight-state playback;512 triples,680 loadings,11376 updates and240
  exact cyclic-word comparisons pass. Wrong period rejected; m=1 and constant-period controls pass. No normal orbit.

- `swarm/erdos_gpt_two_ends.py`: GC1274-1275 joint leading/trailing/length constructions:162 bases and162
  lifts pass;162 wrong corrections rejected,15 wrong-sign controls pass;190->760 retained. No automaton census.

- `swarm/erdos_gpt_digit_counts.py`: GC1277-1278 unit-preserving count reduction;288 feasible triples,582
  multiplications, max4 steps pass. Flush omission rejected;19/550 controlled-path countercontrol retained.

- `instinct/union_closed_fibres.py`: GPT-MATH-INSTINCT MI002-003, preregistration19cdf81e; known27-set Frankl
  localization obstruction,729 pair unions, direct versus weighted frequencies13/27, equal-fibre25/48.
  Powerset equality and nonclosed counterfactual controls pass. No conjecture disproof or new theorem.

- `instinct/path_forest_receiving_chains.py`: MI056-057, preregistration 9fb25568; seven fixed E28
  receiving-chain partitions pass literal swaps, closed-form and independent coverage checks. Reused-pair
  and duplicated-token counterfactuals rejected; 2-element-bin boundary retained. No general E28 claim.

- `instinct/path_forest_coupled_chains.py`: MI058-060, preregistration 8ed0259e; eight of nine fixed
  fixtures pass initially (one is known control), one restricted role choice fails. One preregistered
  fixed role repair passes; omitted-relay and pair-reuse controls rejected. No general E28 claim.

- `instinct/path_forest_cycle_cover.py`: MI061-062, preregistration 801fae29; same nine fixtures,
  fixed two-smallest roles, disjoint token cycles. All witness checks pass; balanced single-cycle
  class fails, pair-reuse and coverage-preserving sum corruption rejected. No all-target conclusion.

- `instinct/path_forest_extreme_cycle.py`: MI063-065, preregistration 5df6e91d; six forced 8-cycle
  boundary cases certify, followed by a preregistered common-root prefix recipe. No-translation shape,
  pair-reuse and wrong-sum controls pass; no all-E28 conclusion.

- `instinct/path_forest_one_negative.py`: MI066-067, preregistration 98702aba; formula-only certificates
  for all 271 even E28 inputs with t4>=112. Parameter and independent sum-count domains agree as sets;
  omitted root correction and exception rejected. Uniform proof PROVED G306/CL421; no general bound.

- `instinct/path_forest_second_negative.py`: MI069-070, formula-only first two-negative boundary
  t4=110,t5>=112; predicts 320 targets, two independent domains and exact certificates.
  Separate 2-cycle or inserted negative vertex; fixed analytic exceptions. All 320 certificates and
  controls pass (4f22d5d0 preregistration); uniform hand proof awaits review.

- `instinct/path_forest_cancelling_pairs.py`: MI072-073, G306 core plus one/two matched cancelling
  pairs of magnitudes 1..5; predicts 940/840 targets and exact folded-gap cover classification.
  Independent direct-domain and literal certificate checks, adverse controls pass: 940/840
  targets (b0c6af00 preregistration); hand extension SKETCH.

- `instinct/path_forest_gap_two.py`: MI075, full t4=108,t5>=112 boundary; predicts 421 targets
  via 2-cycle, two-unit 3-cycle or fixed insertion formula. Two independent domains and literal
  checker; all 421 targets and omitted shifts/root/constant-prefix controls pass
  (c1208711 preregistration); hand argument unreviewed.

- `instinct/path_forest_unit_fans.py`: MI077, reordered sparse core exposes an initial interval
  for a 3- or 4-unit fan. Predict 56/14 targets and one core-order exception; two independent
  domains, exact core/final checks and adverse controls all pass, 56/14 targets
  (28aa073d preregistration); interval hand proof SKETCH.

- `instinct/path_forest_two_surplus_runway.py`: MI079, <=12 fixed u-first core candidates,
  predicts 122 runways and fan-2/mixed-module targets. Independent domains, folded mixed
  hypergraph cover test, restricted-family and ownership controls pass: 122 cores;
  blind no-five-cover prediction REFUTED by one exceptional cover (6f6af2b9 preregistration).

- `instinct/path_forest_three_cycle_modules.py`: MI081, all fifteen small three-cycle modules
  on 122 sparse cores; default versus fixed <=12 reordered cores. 1,830 instances, independent
  deduplicated domain and exact certificates, mixed-cover and old 5+3 controls pass:
  1,830 instances / 1,801 targets, 15 default failures repaired (ce1086ba preregistration).

- `instinct/path_forest_zero_surplus.py`: MI083, full zero-surplus corner, predicts 284
  formula certificates via split or alternating four-move cycles. Three independent domains,
  five omitted-correction controls and the all-14 split check pass: all 284 targets
  (08c69a0d preregistration), hand argument SKETCH.

- `instinct/path_forest_one_surplus_subdivision.py`: MI085, one high surplus via four-move
  parent subdivision, literal-collision repairs and reflection-free translation. Predicts
  1,198 targets, three domains and span<=20 all pass; sharpness/adverse controls pass
  (10cc251d preregistration), hand argument SKETCH.

- `instinct/path_forest_six_translation.py`: MI087-088, sharp six-position span20 bound;
  9,084 endpoint shapes pass independent pair-sum/direct-label tests (1be3bc90 preregistration);
  span21 obstruction and all point deletions behave as predicted, hand SKETCH.

- `instinct/path_forest_two_surplus_subdivision.py`: MI088-089, <=8 fixed one-surplus parents;
  all2,919 targets certify, but <=20-span prediction fails on seven, each translating at21
  (08513a02 preregistration). Failures retained; no widened search.

- `instinct/path_forest_two_surplus_direct.py`: MI090-091, simultaneous forward/backward
  subdivision of one abstract four-move cycle with explicit split cases; all2,919 formula
  certificates pass, exactly eight span21 geometries, adverse controls pass
  (a221b287 preregistration). Uniform hand candidate awaits independent review.

- `instinct/path_forest_two_surplus_scope.py`: MI091-092, existing certificates equal all4,523
  even E28 targets with t5=t6=112, independent direct-set comparison and whole-odd rechecks
  (7a62bc7c preregistration). No new solver or global bound.

- Review receipt CL422/fde83bd8: `path_forest_second_negative.py` MI070 is PROVED G307;
  `path_forest_six_translation.py` MI087 PROVED G308; `path_forest_two_surplus_direct.py`
  MI090 PROVED G309 (independent finite implementation for the span subcase).

- `instinct/path_forest_two_ended_subdivision.py`: MI094-096, seven-position obstruction and
  maximal three-surplus slice.71/72 certificates; fixed-class blind prediction REFUTED by a
  literal parent trap, no widening (36aff500 preregistration).

- `instinct/path_forest_allocation_flip.py`: MI097-098, one algebraically explained allocation
  flip certifies the retained failure; earlier71 unchanged, complete72-set agrees; adverse
  controls pass, repaired span22 (485f7995 preregistration).

- `instinct/path_forest_matching_three_surplus.py`: MI099-100, preserve a matching edge and
  choose core roots via gap-graph covers6..14.999 formula certificates, independent domains,
  explicit matchings/cover classification and blocked-gap controls pass (a353851a preregistration);
  uniform hand argument pending review.

- `instinct/path_forest_three_surplus_max_edge.py`: MI101-102, unmatched W22 boundary with
  three positive surpluses. All11 exact seven-cycle certificates, independent direct target
  domain, wrong-root/order controls and all-even parity control pass (e598c441 preregistration);
  uniform hand argument pending review.

- `instinct/path_forest_prefix_compatibility.py`: MI104-105, unmatched R>=Z,W<22 all-after
  allocation; exact first/last graph matches94,008 direct root/order checks.1,476/1,478 certify;
  two exhaustive failures REFUTE universal allocation. Controls pass, failures retained
  (53b45584 preregistration).

- `instinct/path_forest_prefix_endpoint_repair.py`: MI106-107, explicit one-before/two-after
  stripe certifies7 targets including both previous failures; unchanged1,476 witnesses plus
  repairs equal original1,478 domain. Downshift/B4/wrong-sum controls reject
  (fc1e9f47 preregistration). No full hand availability claim outside the stripe.

- `instinct/path_forest_two_donor_corner.py`: MI108-109, W<=q three-surplus corner; strict
  seven-coordinate order, default root0 and four explicit exceptions.20 formulas, independent
  domains, invalid-parent/omitted-root/wrong-sum and span16 controls pass
  (09a0a21e preregistration). Uniform hand candidate awaits independent review.

- `instinct/path_forest_small_remainder.py`: MI111-112, unmatched0<W-q<Z parent;
  all181,956 graph/direct root-order comparisons agree,2,648/2,760 certificates.112 failures
  all lack a literal order; exact equal-step classification retained (941bb4fa preregistration).

- `instinct/path_forest_cancelling_traps.py`: MI113-114, uniform three/four-cycle split for
  all112 literal traps;25,612 direct/mask root-pair checks, full certificates and adverse
  controls pass. First legal four-cycle root always suffices on this domain (1d161ca7).

- `instinct/path_forest_three_surplus_audit.py`: MI115-116, all5,268 sorted even E28 targets
  with t4<112,t5=112,t6>112 have checked partitions. Five disjoint construction regimes equal
  the independent direct domain; multiset/bitset/exact-bin checks and controls pass (2066fae6).

- `instinct/path_forest_four_constant_traps.py`: MI118-119, cancelling3+5/4+4 cycles certify
  all133 constant traps;29,461 root-pair comparisons and independent domains/checkers pass
  (b3ed973e preregistration), no full four-surplus inference.

- `instinct/path_forest_subset_cancellation.py`: MI120-121, one canonical subset of four
  positive steps gives4,938 certificates;993,670 comparisons pass. First-longer-root shortcut
  fails56, joint placement repairs without changing shapes (beda707c preregistration).

- `instinct/path_forest_positive_factorization.py`: MI122-123, full four-surplus domain7,828;
  canonical six-positive factorization certifies7,221/7,223, two failures retained,605 primitive
  counted only.1,469,303 comparisons pass (3cda72a1 preregistration).

- `instinct/path_forest_factorization_audit.py`: MI124-125, two forced alternate multiset
  partitions complete7,223 factorable targets;928 old-order/root checks confirm the retained
  interval obstruction; exact independent domain/two checkers pass (6e623788 preregistration).

- `instinct/path_forest_primitive_greedy.py`: MI126-127, known nyctalopic order certifies
  575/605 primitive targets;30 fixed-order reflection failures retained.5,918 root checks,
  independent domain/two checkers/controls pass (1c2c1bc5 preregistration), range theorem credited.

- `instinct/path_forest_four_surplus_certificate.py`: MI128-129, existing7,798 partitions
  checked against full7,828-target domain with exact30 residuals; source digests/two checkers
  and controls pass (0877f361 preregistration). Full immutable certificate in shared store.

- `instinct/path_forest_nyctalopic_reflection.py`: MI130-132, reflection-aware prefix-origin
  pruning versus complete multiset permutations/direct roots, whole feasible-map equality.
  All30 residuals resolve, completing all7,828 four-surplus targets with exact domain/two
  partition checks.4,775 class orders,41,203 roots; initial export sort error retained,
  unchanged mathematical rerun passes (5167e2b4 preregistration). Full certificate in store.

- `instinct/path_forest_uniformity.py`: MI134–136/B57; fixed primitive-piece/nyctalopic/reflection architecture certifies2,000/2,000 uniform even E28 targets and25 even targets in2,000 unconditional targets;1,975 outside fixed cardinality class.114 independent component-placement maps/14 packing controls, two literal checkers. Preregistered71c9c265; full immutable sample cited in MI135; no universal E28/L8 theorem.

- `instinct/path_forest_repeated_pieces.py`: B58/MI137-138; all184 two-valued <=8-move zero-sum instances with a+b<=28 have prescribed progression placements;1,224 reference words/14 gap graphs and33 exact E28 corollaries checked. Residue-orbit/path hand construction SKETCH, finite validation COMPUTED. Preregistered eeb2b7a6; raw digest/pointer in MI138.

- `instinct/path_forest_unlike_pairs.py`: B59/MI139-140; all2,380 gap multisets in1..14 have four disjoint folded-label cancelling pairs, both exact implementations and both sorted greedy orders. Forecast of a greedy failure REFUTED.945 exact E28 corollaries with two literal checkers; controls PASS. Preregistered79022fd7; full artifact in MI140.

- `instinct/path_forest_pair_construction.py`: MI141-142, G313 four-gap small/large hand candidate;2,380 formulas,21 independent capacities,945 partitions pass (3daf5e21 preregistration).
- `instinct/path_forest_six_plus_pair.py`: MI143-144 complete six-point span20 plus gap1..14 geometry;217,056 questions pass independent full maps/roots; forecast failure REFUTED (bb346018 preregistration).

- `instinct/path_forest_six_diameter.py`: MI145-146 two-positive/four-negative exact span classification;7,300 tuples vs free-order DP/15 explicit exceptional placements pass (5764eeb2 preregistration), hand statement SKETCH.

- `instinct/path_forest_wide_six.py`: MI147-148, G314 wide primitive2+4 cores;25 profiles/350 complete14-gap maps agree independently,42 actual E28 partitions pass (0eee072e preregistration).

- `instinct/path_forest_collection_counts.py`: MI149-150 count-only all even E28;576,515 unordered collections/max6 per parent/36,735 atoms;121 independent full-set controls, no placements (1082a510 preregistration).


- Instinct B119-B122 (2026-10-17,GPT): `instinct/path_forest_grasshopper_selector_limit.py`
  checks one strict-selector miss; `instinct/path_forest_multi_token_exchange.py`
  gives same-anchor partitions on3 old misses; `instinct/path_forest_subset_catalogue.py`
  validates129658 masks/five unrestricted fixtures; `instinct/path_forest_buffer_kill.py`
  checks54 SB7 boundary profiles. Predictions/outcomes MI258-266; finite computations,
  general claims OPEN/SKETCH, no external replication or raw shared-store upload.

- Instinct B123 (2026-10-17,GPT): `instinct/path_forest_canonical_buffer.py`; fixed seven-set on same54 boundary profiles,allpass;separate triple engine/global conflict controls. MI267-268,prereg21f4af9a. General canonical SB7 OPEN; fullq8 run not started.

- Instinct B124 (2026-10-17,GPT): `instinct/path_forest_q8_certificate.cpp` and `.py`; one complete canonical q8 attempt with independently enumerated original-target stream checker. Prereg MI269;258180 targets,first failure/cap stops,no recipe repair. Outcome MI270:ALL258180 original-target rows literally verified,independent DP/control checks pass;external replication requested GC1451,fullE28/L8 OPEN. Raw stays outside git.

- Instinct B125 (2026-10-17,GPT): `instinct/path_forest_balanced_gap_lift.py`; audit explicit odd-column magic triple partition and monotone insertion of any single missing rank. Prereg MI271/14ddf4b8;MI272 outcome:200 literal/200 reflection/22 table checks and15 balanced q8 examples pass. Supporting hand argument,not arbitrary target sums or another census.

- Instinct B127 (2026-10-17,GPT): `instinct/path_forest_unit_buffer_repartition.py`; canonical seven-buffer plus any disjoint triple at sum s+2, equal4/6 split retaining1. Prereg MI274/e46288ef;MI275 outcome562/562 local triples/118020 reference subsets and retained-token controls pass. Hand candidate unreviewed;not a mixed-target census.

- Instinct B128 (2026-10-17,GPT): `instinct/path_forest_unrestricted_pilot.cpp` and `.py`; unrestricted exact cover on SAME2000 B57 mixed targets,full123-bucket MITM/GF catalogue verification and literal next-target witness checker. Prereg MI277/58a82544;outcome MI278:239 literals verified,target240 scan-cap UNKNOWN,all catalogue/oracle controls pass. No rerun/full run;pending-work reporting fix noted.

- Instinct B138 (2026-10-17,GPT): `instinct/ss3_neutral_diagnostic.py`; fixed n9 target(20,6,10),all1680 size3 partitions and reflected target,adjacent-value swaps with nonincreasing L1 error. Separate complete-map reference,n6 positive/n8 impossible-pair controls. Prereg MI293;5CPU/10wall/96MiB,no retries or domain expansion. No SS3/E28 theorem claim.

  Outcome MI294:all1680 states reach one of two goals in each n9 arm,max shortest path23;all controls/complete reference maps pass.0.254747CPU seconds,no expansion. General neutral escape/SS3 remain OPEN.


- Instinct B146 (2026-10-17,GPT): `instinct/ss3_boundary_window_audit.py`; MI305 prefix-plus-window lemma and reflected four-bin consequence. Prereg MI306/9ad722a9;MI307 outcome:216 pools/962 complete spectra agree literal versus independent cardinality-bitset DP;874 literal partitions cover exactly730 n12 boundary targets.834072 subsets,0.765846CPU,negative holes/translation/touching controls pass. No retry/extension;general hand proof still SKETCH awaiting carrying read,SS3/E28/L8 OPEN.


- Instinct B148 (2026-10-17,GPT): `instinct/ss3_targeted_pool_audit.py`;prereg MI309/869e2960,outcome MI310.54 pools/278 complete spectra have exact holes,literal/set-DP agree;225 targets covered by195 X/26 Y/4 repairs,36 family witnesses pass. Independent n8 oracle UNSAT,h1/signed controls retained;733593 subsets,0.709003CPU. No retry/extension;general MI308 SKETCH,SS3/E28/L8 OPEN.

- Instinct B159 (2026-10-17,GPT): `instinct/ss3_joint_lift.cpp` and `.py`;prereg MI326. Fixed n12,3^4 whole-fibre minimum disjoint adjacent-swap lifts to every SS unit neighbour. Independent counts/eligibility,four complete path-product references,all literal successes/reflected directions;40CPU/60wall/192MiB,no retry/larger domain. NOT RUN at registration;general coupling/SS3 OPEN.

  B159 outcome MI327:PARTIAL/INSTRUMENT-FAILED at wrong transfer direction in full reflection check;whole counts/eligibility,four reference maps/all literal positives passed first. Primary7184 pairs,zero missing,not full protocol pass. Later controls/report unreached,no patch/retry;source/raw retained.

- Instinct B162 (2026-10-17,GPT): `instinct/ss3_one_hole.py`;MI331 preregistration,NOT RUN. Single-deletion pools,all holes at sizes333/334;exact individual spectra plus rank bounds versus joint partitions. Whole combination/owner-recursion maps,multinomial/reflection/endpoint controls,rank-only and size2 negative controls. One3CPU/5wall/64MiB/100KiB run,10s watchdog,no retry or larger domain. General question OPEN.

  B163 outcome MI332:ONE run passes all21 domains/8229 eligible vectors,whole independent maps/counts/literals/reflections/endpoints and both negatives.0.447717CPU,15,597,568B RSS;no retry/extension. General one-hole criterion OPEN;MI333 next hand interior question.

- Instinct B182 (2026-10-18,GPT): `instinct/three_hole_scalar_basis.py`;MI354 preregistration,NOT RUN. Exact normalized three-hole scalar basis r,t4..11;independent deleted-values/DP and rank-gaps/rank-shapes,whole near-edge maps and controls.20CPU/30wall/128MiB,no retry.
- B182 outcome MI355:ONE unchanged-source run ALL PASS,48896 normalized cases/586752 independent offset comparisons;3 literal spectra,71 lifted witnesses and negative controls.8.200965CPU,27,283,456B RSS,no retry. Universal interpretation conditional on hand finite reduction;no partition theorem.

- Instinct B205 (2026-10-18,GPT): `instinct_two_hole_feedback.py`;MI400 preregistration,MI401 outcome. One actual protected two-hole target and its relabelling,45 count states each,1680 rank partitions/independent physical maps. Original all45 enter2-cycle/no fixed point;relabelling all45 converge,10 physical partitions each. Size2 negative/all3 compressed queries pass;0.012880CPU,no rerun/expansion. Policy refuted,existence OPEN.

- Instinct B206 (2026-10-18,GPT): `instinct_two_hole_best_response.py`;MI402 preregistration/MI403 outcome. SAME45-state two-hole fixture,all whole-fibre error minimizers strictly improve at42 positive states;3 goals,10 literal partitions,independent physical map/old2-cycle controls pass. Negative forecast refuted,0.037537CPU,no domain expansion/rerun;general descent OPEN.

- Instinct B227 (2026-10-18,GPT): `instinct/ss3_triple_child.py`;MI434 preregistration,NOT RUN. Twenty strict-triple child pools,size333;complete independent maps,old negatives,reflection,actual14/30-cut lift controls. First negative stops with parent distinction;20wall/10CPU/2million-node caps,no retry.

- B227 outcome MI435:CHILD-CONJECTURE-REFUTED at pool7/20,target228;227 prior positive witnesses,all reached controls pass. Holes4,6 targets7/15/23 have unique overlapping extremes;both actual parents positive. Remaining domain untested,no retry;source a107087f via published merge36b84a4c.
- Instinct B236: `instinct/one_small_row.py`, MI451 registration/MI452 outcome. N11 counts2333: 92,400 partitions, 7,417 rank/actual targets; independent token-owner complete map agrees. N8 counts2222: 30 rank misses, named negative control and full reflection pass. No universal extension; no expanded run.
- Instinct B238 (2026-10-18,GPT): `instinct/protected_pair_row.py`; MI454 preregistration, MI455 outcome. All internal holes, counts233/234:602/1057 protected targets,3920/10080 partitions per independent engine; all pass. Whole maps/counts/coverage/reflection, unprotected negative, withdrawn-warning positive and asymmetric protection controls pass; no enlargement or universal theorem. Raw outside git with hash in MI455.

- `instinct/h2_global_support.py` (MI495–496,2026-10-20): fixed old counts233/234 first-gap test of ALL legal-pair spectrum union. Independent F-H coefficients/direct subsets/pair-deletion supports/reflection and can-fail controls pass. Stops at domain18,M8,q2,u8,gap6; outside protected H2 interval[7,19]. Stronger whole-support interval assertion REFUTED; full fixed domain NOT passed; no H2 refutation or larger run.

- `instinct/h2_g315_extension.py` (MI498–499,G326,2026-10-20): exact pair-gap tables and literal repairs for a protected one-size-two G315 extension. One invocation:1128 complete spectrum pools,932 partitions,2041 reflection identities,19 priority ties PASS with can-fail controls. Finite same-worker ingredient check only, NOT an H2 census, unbounded proof or independent carrying read.

- `instinct/h2_g326_roots.py` (MI500–501,2026-10-20): G326 construction interface on EXACTLY the old602+1057 H2 targets. All1793 permitted roots/1975 legal/formal repair branches return original literal partitions;136 scalar maps agree independently, physical reflection and two can-fail controls pass. Finite same-worker root audit, not unbounded proof, independent review or larger census.

- `instinct/three_pair_finite_basis.py` (MI547–548,2026-10-20): COMPLETE exact residual basis for counts(2,2,2,c),c>=3. 5,146 admitted queries/7,258 candidate rank comparisons agree under target-edge versus six-token-first pairing engines;477,450 terminal matchings including controls. Only2/6/8 and reflection fail; unexpected two-hole AP negative retained. One run/no enlargement; finite COMPUTED premise for unreviewed composite G331, not its carrying verification.

- `eight_streets_cl529_verify.cpp` (MI624,2026-10-22): independent complete verifier of CL529 existing finite basis only; source/predictions frozen before one capped run. Outcome pending.

- MI625 outcome for `eight_streets_cl529_verify.cpp`: compiled unchanged; sole execution supervisor failed on sandboxed ps before control/output receipt. No independent finite-basis verdict, child exit unavailable, no remaining verifier found by exact-command cleanup. No retry/source patch/scope increase.

- 2026-10-22 14:43 BST, GPT REVIEW-1: `prize_reviews/swarm_review_controls.py`; independent exact-rational, literal divisor-subset and Hall-deficiency controls for PRIZE-SWARM.md reviews. One bounded run:263 complete-domain formula comparisons, Corollary B counterexample after939 eligible pairs; known controls PASS, no prize solution.

- `channel12_review.py` (MI658/GC1707, 2026-10-23): optional fixed width-12 independent truth-table/BFS/weight audit with negative controls and caps. Sole attempt failed at RLIMIT_AS setup before reading data; all scientific checks UNREACHED. Source unchanged, no retry; source-level carrying review recorded separately.

- `channel14_source_review.py` (MI660/GC1709, 2026-10-23): sole bounded source/essay/range and tiny width-6 control audit PASS; 919 leaves/918 joins, 263 literal-versus-packed transitions. Three negative witnesses, missing-root name positive. No full width-14 closure/DFA/Lean replay.

- `wolfram/tock_conductor_audit.py` (GC1891/MI819,2026-10-25): owner-authorized tiny Intel audit of L954. 256 trace-prefix inverse/forward controls,15 k0..3 comparisons and32 width<=6 physical cases PASS; no-fall correction hypothesis REFUTED at k4(0001), scan stops. Known-wrong mutant detected, padding/infinite-support controls pass. Full outcome and retained digest in reports/rule30-tock-conductor-review.md. No all-width claim, GPU/Lean or larger run.
- `wolfram/tock_twins.c` (L955, Local, 2026-10-26): at the owner's word, the zero-wall twin-merge, conductor-influence, funnel, ancestor and joint-check probe at W = 8..40 and m <= 24. Frozen at e343a4eb, run once in 12.9 s; 12 controls PASS (L942's exact counts among them). Lag-stationary forgetting REFUTED; positional forgetting, at tick j+1 or never. OUTCOME in its header; reports/rule30-tock-twins.md.
- `wolfram/tock_front.c` (L955): the forgetting front tested on unseen W = 42..48 and m = 25..28 from frozen extrapolations (540e5b12, one run, 20.2 s); FT1 to FT3 HELD, front about 0.15 tock per tock.
- `wolfram/tock_gaps_posthoc.c` (L955, post hoc): deduplicated discrepancy-gap correlation (the PU anticorrelation was a twin echo) and an exact union-find check that surviving futures never merge after the free chapter (W = 40).
- `wolfram/sideways_front.py` (L957, Local, 2026-10-26): the sideways reconstruction's sinking difference top; frozen at 99be4a30, one run, 1.6 s. Controls S0–S3 PASS; flat speed about 0.155 (PS1); coin model 42% fast (PS3 counterfactual met); PS4 exposed lemma L3 (state 10 always survives) and the 0.615 density above the top. OUTCOME in its header; reports/rule30-sideways-front.md.
- `wolfram/sideways_row.py` (L958): lemma L5 checked at every column; background rows fair and uncorrelated; arrival bias 0.868 (forced, L6); drop law. Frozen at 79c86e13, one run, 0.7 s.
- `wolfram/sideways_window.py` (L959): L6 exact; residences by arrival type; arrival law; fair-input sliding-window speed v(k) = 0.137..0.156 (k = 1..6) against real 0.1549. Frozen at 8f956eb0, one run, 1.0 s.
- `wolfram/sideways_fresh.py` (L960): GC1899's input classes (new odd, new even, L6 repeat, backward visit); measurability, fairness and backlog controls PASS; backward visits in state 11 biased 0.71. Frozen at f2640c05, one run, 0.6 s.
- `wolfram/sideways_revisit.py` (L961, revised L962): the one same-index revisit discriminator (GC1901 identity, E11/E01/E10/ENONE, exact-conflict kill test of M); frozen for joint agreement, not run. `wolfram/run_capped.py` (L962): single-worker stage launcher (fresh destination, verified rlimits, process-group RSS, pressure, wall, disk envelope, TERM-then-KILL with cleanup check); eleven harmless controls retained in the store.
- `wolfram/sideways_revisit.py` RUN (L966): the agreed stage completed 12:12:38Z; OUTCOME in its header; short revisits forced, long ones mixed.
- `wolfram/revisit_sat.py` (L969, revised L971 and L974): SAT window encoding of the forced short revisits with LRAT-verified certificates, boundary profiles, single-group containment; frozen for agreement, not run. `wolfram/revisit_sat_controls.py` (L974): six harmless containment controls, all as designed (store: cited/revisit-sat-controls-20261026/).
- `wolfram/revisit_sat.py` RUN (L975): the agreed stage COMPLETED 13:54Z; all eleven targets certified with 384 verified certificates; OUTCOME in its header.

- 2026-10-26 GPT GC1923: wolfram/blind_witness_intel.py — small exact physical-tock observer capacity and boundary-merger controls, owner-authorized Intel; frozen predictions, not yet run.


- 2026-10-26 GPT GC1923 OUTCOME: frozen wolfram/blind_witness_intel.py b3265475 completed once,1360 lanes/all controls PASS; P1 REFUTED,P2 HELD with exact witness. Retained evidence cited/gc1923-blind-witness-intel/, report reports/rule30-blind-witness-intel-review.md. No larger run. Legacy wall startup PASS; merge startup WALL_STOP180s/INCOMPLETE, cleanup complete, no retry.
- 2026-10-26 Local L989 OUTCOME: wolfram/certificate_witness.c (85e985e9) ran once under GC1926 caps, controls ALL PASS; H1 FAILED, H2 FAILED (counterfactual met), PU HELD; receipts cited/certificate-witness-20261026/.
- 2026-10-26 Local L989: wolfram/certificate_shuffle.c — exact shuffle null for DIARY minimum certificates (64 shuffles per width and population); frozen predictions R1/R2/PU and controls X1-X5, awaiting GPT; not built or run.
- 2026-10-26 Local L991 OUTCOME: wolfram/certificate_shuffle.c (b14a5d1d, GC1927) ran once, controls ALL PASS; R1/R2 FAILED, counterfactuals MET; PU FAILED. Post hoc wolfram/certificate_influence_posthoc.py (reads retained rows only).
- 2026-10-26 Local L993: wolfram/certificate_conditional.c — certificates within classes of the oldest three diary entries vs 64 count-preserving permutations per class (ALL, W24..28); controls K1-K6, predictions M/CF/PU frozen; awaiting GPT launch review; not built or run.
- 2026-10-26 Local L995 OUTCOME: wolfram/certificate_conditional.c (0c6a6358, GC1929) ran once, controls ALL PASS; M HELD, CF not met, PU HELD; manifest retained.


- 2026-10-26 GPT GC1934: wolfram/staircase_image_read.py (orientation), staircase_recover.py (local domain propagation), staircase_verify.py (174720 cones,1320 independent engine controls,256-update single-seed audit); source/spec frozen before each run, final verification92c3b322, all staircase controls PASS. Two pre-analysis OS memory-limit refusals retained; no hard memory cap claimed. Fixed bounds and CPU/wall/file caps; full report reports/rule30-staircase-investigation.md, receipts cited/gc1934-staircase/. Legacy merge startup INCOMPLETE under CPU cap, not passed. staircase_figure.py draws an exact scientific diagram from fresh scalar evolution, not image editing.

- 2026-10-26 Local L997–L999: wolfram/antilatch_check.py (the latch beside an alternating wall, about 2.5 million cases); wolfram/triangle_parents_check.py (L998: GC1932's maps and chain, the white-run parent trichotomy 1:1:2, the lone-cell rule, the first-generation 2^-k law; exhaustive at 18 cells; nonzero exit on failure since GC1933); wolfram/staircase_rain_check.py (L999: GC1934's alternative on 22,321 single-seed bars, the left companion, the rain front lemma, front-hung triangles and their 2, >=3 rhythm, the crop at global x 83..92; Local's own implementation, not GPT's). Predictions written into each header before its run; slips and outcomes retained there. Each runs in under 3 s on the M5; full reads in reports/rule30-triangle-ancestry-local-read.md and reports/rule30-staircase-local-review.md.
- 2026-10-26 Local L1000: wolfram/run_rule_check.py (R, the run rule, on every ring to 16 cells; P, the patch rule, against 20 backgrounds including all 12 period-3 rows; the bridge bound; ring counting laws; Theorem E for every seed to width 12 and the single seed's ruler to v = 12). Predictions in the header before each run; three checker slips and the outcome retained there; 3.8 s on the M5; full note reports/rule30-run-rule.md.
- 2026-10-27 Local L1001: wolfram/edge_levels_look.py and wolfram/edge_hierarchy_look.py (exploratory looks with predictions first: level 2 of the edge, the full hierarchy and the spine test); wolfram/universal_ruler_check.py (Theorem U exactly on all 16,383 seeds to width 14 over 1,200 steps; the single seed's gap property over 66,000 steps). Outcomes and harness slips in each header; full note reports/rule30-universal-ruler.md.
- 2026-10-27 Local L1002: wolfram/closure_finite_look.py (GC1935's assertion A: every odd code below 2^24 tested to depth 44, only T^tau(1) pass; non-edge black runs near the edge bounded over 131,071 rows; T^-j(1) = the GC1932 tower and the cap formula replayed). Predictions before each part; outcome and one early-exit slip in the header.
- 2026-10-27 Local L1004: wolfram/clock_deadline_check.py (GC1940's six cuts: the refined left-only deadline H*, black-tick rule plus the white-tick anti-latch, equals the best observed failure in every case; no search; GPT's stage not rerun).
- 2026-10-27 Local L1006–L1007: wolfram/clock_right_realizability.py (exact SAT decision of right realizability for cut 49 with controls; frozen at bd6a7766 before running; optimum 52, blocked by MFW 101001), clock_deadline_check.py part two (GC1942's front parity), wolfram/staircase_end_check.py (Theorem S's ingredients and bound on the single seed's rows).
| `wolfram/edge_gaps.c` | Cloud, 2026-10-29 (CL640): the white gap J_k left of the edge cell of row 2^k of the single seed, by iterating the T-function Phi on 128 bits (kit per_iff_gap: R_n has period 2^k iff n <= J_k); output in edge_gaps.out; the marginal growth 2.0 cells per k over k = 24..34 is the evidence for SYNTHESIS-20261029.md section 5.1 |
| `wolfram/edge_lift.c` | Cloud, 2026-10-29 (CL640): block period exponents of a finite seed's edge code by the kit's lifting rule (TFunctionCycles.lift_iff: parity of x_(n-1) OR x_(n-2) over one period); twelve seeds to n = 56 in edge_gaps.out; the rate is not visibly seed-independent at this depth |
| `wolfram/edge_diag_rules.c` | Cloud, 2026-10-29 (CL642): for the single seed to j = 56, the least period of each right diagonal, the doubling bit d_j, the weight parities and the three hand rules (Case A: after a doubling, d_j = weight parity of R_(j-2); Case B: d_j = omega_(j-1) + omega_(j-2) + AND parity; omega of a non-doubling diagonal = even-time black count of its input); all exact to j = 56; output and the frozen predictions in edge_diag_rules.out |
| `wolfram/edge_zero_runs.py` | Cloud, 2026-10-30 (CL649): doubling frequency after m consecutive non-doublings and the zero-run length distribution of block exponents (input `edge_lift64.out`, the 64 seeds of CL642 to n = 56); f(m) flat near 1/2 for m = 1..7, runs geometric except five plateaus of length 9; output `edge_zero_runs.out` |
| `wolfram/edge_reverse.c` | Cloud, 2026-10-30 (CL650): block exponents of a seed with one bit complemented (one wheel reversed), with the older supplier's weight parity per wheel; 59 reversals across the six long plateaus of CL649 in `edge_reverse.out`; the hand rule (E_(k+1) changes iff wheel k-1 has odd weight) held at all 59 |
| `wolfram/edge_plateau_tail.py` | Cloud, 2026-10-30 (CL650): plateau (zero-run) length distributions for run A (`edge_lift48.out`, 256 odd 48-bit seeds to n = 60, seeds in `edge_lift48.seeds`) and run B (`edge_lift24_68.out`, the 64 seeds to n = 68); run A shows no peak at length 9, a smooth tail 9, 4, 2, 2 at lengths 8 to 11 against a halving law |
| `wolfram/edge_break.c` | Cloud, 2026-10-30 (CL652): block exponents of a seed under the edge map with breaks (reverse a wheel, clamp a wheel white, AND or XOR at one wheel or every wheel), with per-wheel weight parities; outputs `edge_break1.out` (59 pair reversals), `edge_break_c30/a30/x30/A/X.out` (64 seeds to n = 56); analysis `edge_break_analysis.py`: all four hand rules exact, single suppliers double at about 0.1, rule 150 logarithmic, rule 120 at rule 30's density |
| `wolfram/edge_greedy.py` | Cloud, 2026-10-30 (CL652): greedy plateau extension by single reversals from CL650's fourteen-wheel chain; `edge_greedy.out` (nine rounds, 34 wheels at period 2^15, capped in round 10), `edge_greedy_chain.out` (the final seed under edge_break to n = 70) |
| `wolfram/edge_break16.c` | Cloud, 2026-10-30 (CL654): edge_break with a 4-bit truth-table gate g<tt>; `edge_gates16.out`: all sixteen gates on the 64 seeds to n = 48; two product gates choke, six at 0.39 to 0.43, affine ones logarithmic |
| `wolfram/left_settle.c` | Cloud, 2026-10-30 (CL654): Rule 30 from one cell to T = 65536; least periods and settling times of the left wheels to j = 1024 (`left_settle.out`): tau_j about 1.27 j, periods at most 16 |
| `wolfram/edge_supports.c` | Cloud, 2026-10-30 (CL654): binomial-basis (Moebius) supports of the right wheels of a seed over one least period, with the all-ones / weight-parity dictionary check; `edge_supports.out` for the single cell to j = 52: dense, ratio 1/4 after each doubling |
| `wolfram/clock_hiccup.c` | Cloud, 2026-10-30 (CL655): the wall frame of d1_engine.py with one hiccup in the clock (pin dropped, pin inverted at an even time, pin added at an odd time), exhaustive W = 8..22, every t_h; `clock_hiccup.out`; D(W) reproduced; best single-hiccup lives up to +14 over D(W) |
| `wolfram/finite_clock.c` | Cloud, 2026-10-30 (CL656): every nonzero seed of width w with the clock column at every position, lifetime of an alternating column from time 0; `finite_clock.out` w = 1..22: L(w) = 1, 7 (w = 2..7), 9, 10, 15 (10..13), 16, 16, 17, 22 (17..20), 25, 25; no seed reaches the cap 160 |
| `wolfram/finite_clock_runs.c` | Cloud, 2026-10-30 (CL657): longest alternating stretch in any column (12 either side of the seed) at any start time, 200 rows, every seed of width w; `finite_clock_runs.out` w = 1..18: 12, 12, 12, 15, 15, 15, 17, 17, 21, 21, 21, 21, 24, 24, 24, 25, 27, 29; no run reaches the cap |
