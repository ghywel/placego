# Probes: one-off measurements that produced a recorded finding

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
