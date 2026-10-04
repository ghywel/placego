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
