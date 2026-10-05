# Cloud and Local: one project, two Claudes

*Started 2026-10-04 at the owner's request. Two instances work on this repository: **Cloud** (Claude on the web,
linked to this repository, no GPU) and **Local** (Claude on the owner's machines: an Apple-silicon Mac, an Intel
Mac, and a Linux NAS with an Intel Arc A310, the deterministic witness). Tokens spent Local are scarce and tokens
spent Cloud are spare. So Cloud does the thinking and writes the scripts. Local runs them on the GPUs, briefly, and
reports the numbers back through git. If you are either instance, read this file first, then the newest entry of
the ledger at the end.*

## The split

| Cloud (reasoning, CPU only) | Local (the GPUs, the devices, the apps) |
|---|---|
| Reading shaders and libplacebo's source; finding the cause of a defect by argument | Running anything through Vulkan: the ladder, `identity.sh`, `timepair.sh`, `smoke.sh` |
| Generator and tool changes, checked by `rebuild_generated.py`'s control (pure Python) | The deterministic verdict on the Arc; timing from a file |
| Static checks: liveness (`dead_passes.py`), GLSL compile through `gen_metal.py --compile` (glslc + spirv-cross; apt packages `glslc`, `spirv-cross`) | The Metal side: `lockstep.sh` and the apps (the private trees are not in this repository) |
| Writing a job: the script, its prediction, what refutes it | Running the job, writing the result under its lead, pushing |
| Literature surveys (PRIOR-ART.md) | The owner's devices: Cadence builds go to every reachable device |

## How a job travels

1. **Cloud** works on a branch `claude/<topic>`, never on `main`. Each job is a script in `tests/probes/<topic>/`
   whose header says:
   - `RUN-ON:` arc | mac | cpu;
   - `COMMAND:` one line, from the repository root;
   - `PREDICTION:` the number expected, written before the run;
   - `REFUTED-BY:` what result would refute it;
   - `COST:` the expected minutes.

   Cloud adds a line to the ledger below ("Cloud wrote"), commits, and pushes the branch.
2. **Local** merges the branch into `main` and runs the job exactly as written. It records the verdict under the
   lead (REPAIRS.md or the topic's document) and adds a ledger line ("Local ran"), then pushes when the owner says
   to push.
3. A job that changes a shader ships as a variant or behind a generator switch, never as an overwrite. It needs the
   full-ladder regression gate before adoption, and adoption is the owner's call
   ([WORKFLOW-SAVED-MEMORY.md](WORKFLOW-SAVED-MEMORY.md)).

4. **Hand back.** Local hands the work back to Cloud at one of two defined points.
   - **Finished.** Every output named by the job's COMMAND exists and is complete. The verdict (each prediction HELD
     or REFUTED, with its numbers) is recorded where the job's header says. A ledger line "Local ran" is added, and
     `main` is pushed.
   - **Stopped early.** At once, on any result the job's header names as a stop (a refutation that changes the
     direction), or if the run passes three times its COST.

   Then the owner tells Cloud "Local ran <lead>". Cloud starts by fetching `main` and reading the ledger and the
   recorded verdict, never from memory, because a Cloud container does not keep its state between sessions.

## Rules for both

- **Generated shaders are never edited by hand.** Change the source or the generator. Then run
  `PY=python3 python3 tests/probes/repairs/rebuild_generated.py /tmp/out`: first the control, with every file
  `same` on unchanged sources, then the change.
- **The generators do not compile GLSL.** A well-formed rebuild can still fail to build: 14 files did in L3's first
  cut. Cloud: run `gen_metal.py --compile` on every changed file. Local: run `compile_all.sh`.
- **Every check has a control and a counterfactual.** Run a shader against itself (it must be identical). Run it
  against a shader known to differ (it must differ). Assert the commit under test: a job on the Arc once compared
  the old commit with itself because a checkout aborted silently (2026-10-04).
- **This repository is public.** Never write hostnames, usernames, addresses or personal names other than the
  owner's. `jellyfin-project/` is the owner's: never touch it.
- **Predictions are written before runs.** A known is a measurement with a date and conditions; anything else is an
  assumption, labelled as one.

## The open leads, by kind (2026-10-04)

From REPAIRS.md. L1-L4 are done.

| Lead | What | Mostly | Cloud's part | Local's part |
|---|---|---|---|---|
| **L7** | 177 dead passes (the B->A flow chain unread in two-frame shaders; 3 of Cadence High's passes) | **Cloud** | A prune step at the end of each generator and for the hand files, driven by `dead_passes.py`; control by rebuild; compile by glslc | Identity on the Arc, time from a file, lockstep, Cadence. **Awaiting the owner's go.** |
| **L8** | Not deterministic on L7_textured_large: the quad, and Cadence High on the first render of a job (the next renders agree) | **Cloud** (the cause) | Read the quad and the carry/cage path for a race or a read of storage before its first write (persistent textures on frame 1, uninitialised VRAM) and name the pass | A repro and a bisect on the Arc to confirm the named pass |
| **L9** | Generated headers cannot rebuild their files (base argument, `ZERO_SEED=1` missing) | **Cloud** (all of it) | Make every generator record its full command; `rebuild_generated.py` then needs no inference; control by rebuild | None beyond the merge |
| **L6** | `lum` computed, never used, in every reading tail | **Cloud** (all of it) | Drop it in `add_human_reading.py`; rebuild; only tails change | Lockstep (the Metal graphs hash the GLSL) |
| **L10** | Readback through the reading tail passes an fp16 stage (about 1/32 px floor) | **Both** | Trace the output format in libplacebo; write the probe (a known sub-pixel translation through read_view 4) | Run the probe (minutes) |
| **L5** | The cel-animation class still has `ZERO_SEED = 0` | **Local** | Write the variant files and the ladder job | The ladder on the Arc; the decision is the owner's |

### Mathematics (PRIZE-PROBLEMS.md), from 2026-10-04

The owner's second challenge: open prize problems a GPU might reach. Everything so far ran on Cloud's CPU. The Rule 30
work is exact bit arithmetic and needs no GPU at these sizes.

| Lead | What | Mostly | Cloud's part | Local's part |
|---|---|---|---|---|
| **M1** | Rule 30: prove that every zero run in the forced left half ends, with column 1 free (PRIZE-PROBLEMS.md §7, conjecture LR) or made by a finite right half (§8, conjecture B, weak form since X3), which would imply Prize Problem 1; next, name the templates as white-triangle boundaries (§8.2, §8.3), and a sibling ladder: period two for Rules 180, 120, 210, 150 without linearity (Rule 90 done, Proposition 5) | **Cloud** | all of it | none |
| **M2** | Rule 30: the pure-wheel orbit is DONE on Cloud (Proposition 6, PRIZE-PROBLEMS.md §8.6: mu = 32,896,298, lambda = 15,009,104,432, not zero; certificate verified). Remaining for Local: settle the periodic columns 1 that `periodic_kill.c` left undecided (period 17 with 0101..., 7,614 rotation classes; periods 9, 11, 13 with 0001..., 858 undecided of 880 classes), budget 10^9, predictions K3 and K4. The job, its COMMAND, COST and hand-back point are in the header of `tests/probes/lexicon/periodic_kill.c` ("JOB M2") | **Local** | written and validated (the classes mode reproduces the first run exactly) | ran 2026-10-05 (12 min): K3 held; K4's no-kill half held, its 99% refuted (527 classes at 0001… q = 13 outrun 10^9) |
| **G1** | Do error-free transformations (TwoSum, FMA TwoProd) survive each GPU's compiler? The prerequisite for any float-based proof on a GPU | **Local** | write the job and its prediction | run it on the Arc and the M5 (minutes) |

## Ledger

Times are the owner's local time (BST). "Arc" is the NAS's GPU, "M5" the Apple-silicon Mac.

| When | Who | Where | What | Commit |
|---|---|---|---|---|
| 2026-10-04 13:27 | Cloud | CPU | The base written out as equations; wrong comments repaired; REPAIRS.md and SHADERS.md with leads L1-L6 | 79e96c2 |
| 2026-10-04 14:54 | Local | - | Cloud's branch merged with the local work; branch deleted on the owner's word | 3c3d23e |
| 2026-10-04 15:02 | Local | M5 | The six `-cut` shaders regenerated; smoke | ef3cbec |
| 2026-10-04 16:31 | Local | M5 + Arc | L1: edge masks gone from the N-frame shaders; the six-frame slot-5 luma bug fixed (+0.66 dB) | 705c89a |
| 2026-10-04 16:40 | Local | M5 + Arc | L3: 490 dead contrast gates retired, byte-identical, free (the first cut broke 14 files; caught, never pushed) | 33e77ad |
| 2026-10-04 16:47 | Local | Arc | L4: the coarse search sets the flow's fraction (15.75 px for 16); the rounding variant is neutral on real clips, not shipped | 863d287 |
| 2026-10-04 17:38 | Local | M5 + Arc | L2 measured (the snap at 1.0: -0.99 dB mean, retire); leads L7-L10 written; smoke 18/18, lockstep PASS; pushed | e850bca |
| 2026-10-04 19:28 | Local | M5 + Arc | L2 done: the snap retired, generators fixed. 24 of 24 identity comparisons byte-identical on the Arc. Time from a file: base -6.3%, Cadence High -2.1%, Standard -1.5% | 696cd46 |
| 2026-10-04 19:36 | Local | M5 + Arc | L2 in the six cel-animation shaders; compile 6/6; identity 24/24 on the Arc | 33a63f5 |
| 2026-10-04 19:45 | Local | Arc | L8 step 1: Cadence High against itself on L7, three in a row: the first differs, the next two identical (a first-render effect) | 0c52d5d |
| 2026-10-04 19:40 | Local | - | This file | 0c52d5d |
| 2026-10-04 20:01 | Local | M5 + devices | L2 carried into Cadence: nine graphs regenerated, lockstep PASS (19:36-19:41), mac-tests 57/57, build 202610042001 on the Mac, the Intel Mac, the iPhone and the Apple TV (the iPad asleep) | (Cadence's tree) |
| 2026-10-04 20:33 | Local | - | Pushed to placego on the owner's word (e850bca..be6fd30), with 41 stray `._*` files removed and a `.gitignore`. His first Cloud task: a mathematical challenge on BIDIRECTIONAL-AS-MATHEMATICS.md | be6fd30 |
| 2026-10-04 21:15 | Cloud | CPU | LEXICON.md (checked by `lexicon_check.py`: 7 claims, 5 counterfactuals caught) and PRIZE-PROBLEMS.md (the prizes as of today, ranked; Rule 30 Problem 1 first). The Rule 30 periodic-column probe: Condrey's published period-1 maxima reproduced exactly to w = 8; no finite configuration has a periodic column of period 2-6 with right half up to 18 cells (27,262,976 cases, depth 256); the 7-periodic tails explained by the 7-ring's 4-cycles. BIDIRECTIONAL-AS-MATHEMATICS.md brought up to date with L2/L3. No Local job this round | (this commit) |
| 2026-10-04 21:39 | Cloud | CPU | Rung 2 first progress (PRIZE-PROBLEMS.md §7): the left half depends on column 1 only where the trace is 0 (checked 880 of 880); rotations of a periodic word are equivalent; conjecture LR (left-side rigidity) would imply Prize Problem 1. Evidence: exhaustive over every column 1 for all 26 primitive words of period 2-4, every zero run ends; the pre-registered bound 3d+12 refuted for two words. No Local job | (this commit) |
| 2026-10-04 21:45 | Cloud | CPU | Rigidity, deeper (14 free bits, periods 2-5): every zero run ends for all 50 primitive words (depths to 72); the 3d+12 bound refuted for 10 words; single-zero words the most rigid (longest runs 17-23), mostly-zero words the least (45-66) | (this commit) |
| 2026-10-04 22:22 | Cloud | CPU | The owner's two-sided idea (PRIZE-PROBLEMS.md §8): the right side constrains column 1 to 86 of 1,048,576 sequences at length 20; with both sides exact, zero runs stay near 20 (0101...) and 17 (0001...) to depth 192 and grow only slowly deeper (22 by depth 384), against about d with column 1 free. Column 1 is locally rigid, globally chaotic, not 2-automatic. Run to width 24 in progress | (this commit) |
| 2026-10-04 22:32 | Cloud | CPU | The four arms (the owner's design, PRIZE-PROBLEMS.md §8.1): right alone = neither (proved and measured); left alone close to coin flips; both reshapes the distribution, with quantised run lengths (exactly 12 or 14 for 0101...) and a short ceiling; F2 refuted. The owner's question answered: pseudorandom is enough, F4 held against the OS entropy source (3.43 SE at most over 152 comparisons) | (this commit) |
| 2026-10-04 22:58 | Cloud | CPU | X3 refuted (PRIZE-PROBLEMS.md §8): every right half to width 24, depth 384, gives zero runs of 24 (0101...) and 26 (0001...), so the depth-192 plateau was an artefact; B kept in its weak form, every run ends. The owner's question on 13 (§8.2): 13 is not special, the hole moves with the phase (13 for 0101..., 15 for 1010...) because long runs come from a few templates whose lengths step by 2; 13 the Fibonacci number counts what Lemma 3 lets the left side see over 10 steps (Pell and Fibonacci envelope proved, P1). Lemma 4 proved and checked (column 1's newest bit enters the left half once, as an XOR); its pre-registered corollary P3 refuted for all five words. Four earlier Cloud times in this ledger corrected to their commit times | (this commit) |
| 2026-10-04 23:33 | Cloud | CPU | Prior art surveyed (PRIOR-ART.md): period one closed by Condrey, period two open and worked on in public; our forced left half, the X3 fact and B's weak form were reached independently. The random-chaos step: the instrument on Rule 30's 16 left-permutive siblings (rung 1 now shown able to see a counterexample: Rule 60); S4 refuted, every two-sided zero-fixing sibling is witness-free; Proposition 5 (Rule 90, by Lucas' theorem) proved and checked. The owner's harmonics lead: H1/H2 refuted, the resonance is the 7-cell ring's 4-cycle (lag 7, period-4 words only; 15 fresh words, Q2 held 14 of 14, Q1 refuted). The owner's Fourier lead: the left half rings at sevenths (0101... weakly too); octaves in column 1 refuted; column 1 for 0101... has an unexplained line near 17/56 | (this commit) |
| 2026-10-04 23:44 | Cloud | CPU | The owner's complex-number lead (PRIZE-PROBLEMS.md §8.4): column 1 for 0101... is locally a coding of a circle rotation e^(2 pi i f t), f = 0.30365 (about 17/56), with the trace's half-turn (error 0.082 at 64 steps against an instrument floor of 0.049; R1 and R2 held, R3 refuted 4 of 8, the misses being the broadened second overtone). The first run was void: its controls caught two bugs (phase sign, a non-periodic planted control). One control (C1) missed its threshold by 0.009, recorded as a failure, with a calibration. 42 of 1,024 right halves lock column 1 exactly (28 to period 4, 14 to period 14); the other 982 are a wheel that slowly loses phase (81% agreement at lag 56, 39-40% at 55 and 57). Quaternions: not needed so far; one complex plane holds every line | (this commit) |
| 2026-10-04 23:56 | Cloud | CPU | The universal wheel (PRIZE-PROBLEMS.md §8.5): between slips, column 1 for 0101... is one universal word U (96.6% of stretches, Q3 held), an exact two-arc coding of the rotation t -> 17t mod 56 (five blocks 0001001101 and one 001101; 17/56 = [0; 3, 3, 2, 2]); 95% of slips are shifts in time (Q2 held); exact windows are rarer than predicted (8.4%, Q1 refuted); long zero runs sit next to slips, never inside exact stretches (Q4 refuted, 0 of 40); no sibling turns the wheel (S held). Under the pure wheel the forced left half is never eventually zero within 200,000 depths (W1 held), but its runs grow like log2 of the depth, 23 by 200,000 (W2 refuted); at depth 192 they are at most 10. Two control failures caught and fixed (C1 compared 21 cells against 8). New lead M2 for Local | (this commit) |
| 2026-10-05 00:25 | Cloud | CPU | The owner's question, 'does the left churn the wheel into noise?' (PRIZE-PROBLEMS.md §8.6): yes. Under the pure wheel the left half passes block entropy (0.9999 for blocks to 12), a flat spectrum and a 50% avalanche; order in, noise out (N1-N3 held). Proposition 6 (computed): the pure wheel's left half is never eventually zero; the pair orbit has tail 32,896,298 and cycle 15,009,104,432 (not zero), one certificate for all 28 phases by symmetry, verified independently (wheel_orbit.c, O1 and O2 held). The random-chaos step: LR holds for every decided periodic column 1 (0 kills in 417,010 words; 140,042 undecided, counted) (periodic_kill.c) | (this commit) |
| 2026-10-05 00:33 | Cloud | CPU | Cloud wrote job M2 for Local (`periodic_kill.c`, "JOB M2" in its header): the undecided periodic columns 1, one word per rotation class (7,712 classes for 0101... q = 17; 880 for 0001... q = 9, 11, 13), budget 10^9, predictions K3 and K4, under 40 minutes on 8 cores at worst. Validated: the classes mode reproduces the first run's counts exactly. The protocol gains step 4, the hand-back point | (this commit) |
| 2026-10-05 00:47 | Local | M5 (CPU, 10 cores) | Local ran M2 exactly as written (00:35:12-00:47:26). No KILL line. K3 HELD: 0101… q = 17, all 7,712 classes and 131,072 words decided, 0 kills, longest cycle 5,224,661. K4: no kills (held), decided share REFUTED: 3,753 of 10,604 words (35.4%), 331 of 858 classes; q = 9 and 11 fully decided, q = 13 leaves 6,851 words (527 classes) undecided within 10^9, longest cycle found 452,150,348. LR now holds for 550,201 decided periodic columns 1. Verdict in `periodic_kill.c` and PRIZE-PROBLEMS.md §8.6. Handed back: finished | (this commit) |
| 2026-10-05 01:06 | Cloud | CPU | Cloud took M2 back (main fetched, verdict read; 3 of 64 shards of K3 re-run on Cloud agree: 0 kills, longest cycle 5,224,661). The random-chaos step, O3: the wheel out of step (U at odd phases, which breaks Lemma 3) still cannot kill the left half (mu 276,594,382, lambda 363,832, columns of period 28); the verifier now factors lambda itself, after a composite was passed as a prime. Part 3 of the route, PRIZE-PROBLEMS.md §8.7: a slip is one particle (P2 held, 4 shapes cover 96.7% of 22,937 slips; the commonest 84%); P1 refuted as operationalised, P3 refuted, CF2 failed vacuously. The method is Hanson and Crutchfield's domain filter, reached independently | (this commit) |
