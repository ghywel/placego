# Cloud and Local: one project, two Claudes

*Started 2026-10-04 at the owner's request. Two instances work on this repository: **Cloud** (Claude on the web,
linked to this repository, no GPU) and **Local** (Claude on the owner's machines: an Apple-silicon Mac, an Intel
Mac, and a Linux NAS with an Intel Arc A310, the deterministic witness). Tokens spent Local are scarce and tokens
spent Cloud are spare. So Cloud does the thinking and writes the scripts. Local runs them on the GPUs, briefly, and
reports the numbers back through git. If you are either instance, read this file first, then the newest entry of
the ledger at the end.*

*2026-10-05: a third party joins, **GPT** (ChatGPT, a model of a different make), as independent eyes on the Rule 30
work. Its handover is [WORKING-TOGETHER.md](WORKING-TOGETHER.md): the lanes in this repository, the method, and
the messages table below, which all parties use to talk to each other through git.*

## The split

| Cloud (reasoning, CPU only) | Local (the GPUs, the devices, the apps) |
|---|---|
| Reading shaders and libplacebo's source; finding the cause of a defect by argument | Running anything through Vulkan: the ladder, `identity.sh`, `timepair.sh`, `smoke.sh` |
| Generator and tool changes, checked by `rebuild_generated.py`'s control (pure Python) | The deterministic verdict on the Arc; timing from a file |
| Static checks: liveness (`dead_passes.py`), GLSL compile through `gen_metal.py --compile` (glslc + spirv-cross; apt packages `glslc`, `spirv-cross`) | The Metal side: `lockstep.sh` and the apps (the private trees are not in this repository) |
| Writing a job: the script, its prediction, what refutes it | Running the job, writing the result under its lead, pushing |
| Literature surveys (PRIOR-ART.md) | The owner's devices: Cadence builds go to every reachable device |

## How a job travels

1. **Cloud** works on a branch `claude/<topic>`. Each job is a script in `tests/probes/<topic>/`
   whose header says:
   - `RUN-ON:` arc | mac | cpu;
   - `COMMAND:` one line, from the repository root;
   - `PREDICTION:` the number expected, written before the run;
   - `REFUTED-BY:` what result would refute it;
   - `COST:` the expected minutes.

   Cloud adds a line to the ledger below ("Cloud wrote"), commits, and pushes the branch. Cloud then merges the
   branch into `main` itself, by the same steps as every party (see "Merging into main" below).
2. **Local** runs the job exactly as written. It records the verdict under the lead (REPAIRS.md or the topic's
   document) and adds a ledger line ("Local ran"), then pushes when the owner says to push.
3. A job that changes a shader ships as a variant or behind a generator switch, never as an overwrite. It needs the
   full-ladder regression gate before adoption, and adoption is the owner's call
   ([WORKFLOW-SAVED-MEMORY.md](WORKFLOW-SAVED-MEMORY.md)).

**Merging into main (the owner's decision, 2026-10-06).** Any party may merge its own branch into `main`; git is the
multi-writer tool, and each of us already notices and repairs a change made while we worked. The steps, the same for
Cloud, Local and GPT: fetch; merge `origin/main` into the branch; check the changed files for conflict markers;
review privacy; run the math check after editing TeX; then push to `main`. Never force-push or rewrite history.
In the three append-only ledgers (this file, the live CHAT-LEDGER.md and the live CASUAL-LEDGER.md; never
append to a numbered archive), keep both sides' entries in time order; IDs are per-author, so nobody need renumber. After merging `origin/main`, run
`python3 tests/probes/ledger_check.py`: union merge can silently re-import an archived ledger into the live file
when a branch predates a rotation (CHAT-LEDGER.md CL001). This replaces the earlier rule that Cloud never works
on `main` and that Local merges Cloud's branches.

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

### Mathematics (RULE30-PRIZE.md), from 2026-10-04

**Where the status is.** Each row's last cell starts with its status. The Rule 30 leads in detail, with the questions and the small items, are on the status board in [PERIOD-TWO.md](PERIOD-TWO.md) §6.

The owner's second challenge: open prize problems a GPU might reach. Everything so far ran on Cloud's CPU. The Rule 30
work is exact bit arithmetic and needs no GPU at these sizes.

| Lead | What | Mostly | Cloud's part | Local's part |
|---|---|---|---|---|
| **M1** | Rule 30: prove that every zero run in the forced left half ends, with column 1 free (RULE30-PRIZE.md §7, conjecture LR) or made by a finite right half (§8, conjecture B, weak form since X3), which would imply Prize Problem 1; next, name the templates as white-triangle boundaries (§8.2, §8.3), and a sibling ladder: period two for Rules 180, 120, 210, 150 without linearity (Rule 90 done, Proposition 5) | **Cloud** | all of it | **OPEN.** Local leads since the evening of 2026-10-05. The status of every part is on the board in PERIOD-TWO.md §6 |
| **M2** | Rule 30: the pure-wheel orbit is DONE on Cloud (Proposition 6, RULE30-PRIZE.md §8.6: mu = 32,896,298, lambda = 15,009,104,432, not zero; certificate verified). Remaining for Local: settle the periodic columns 1 that `periodic_kill.c` left undecided (period 17 with 0101..., 7,614 rotation classes; periods 9, 11, 13 with 0001..., 858 undecided of 880 classes), budget 10^9, predictions K3 and K4. The job, its COMMAND, COST and hand-back point are in the header of `tests/probes/lexicon/periodic_kill.c` ("JOB M2") | **Local** | written and validated (the classes mode reproduces the first run exactly) | **CLOSED.** ran 2026-10-05 (12 min): K3 held; K4's no-kill half held, its 99% refuted (527 classes at 0001… q = 13 outrun 10^9). CLOSED 2026-10-05: Jen's theorem (RULE30-PRIZE.md §8.13, Proposition 7) proves that no eventually periodic column 1 kills, so the 527 classes are settled and nothing is left to run |
| **M3** | Rule 30, two heavy runs the container cannot do well (RULE30-PRIZE.md §8.20, §8.21). (a) The channel bound at m = 27, 28 (`entropy2.c`; about 16 and 32 GB; prediction EN6, the bound levels off between 0.115 and 0.128). (b) The counterexample search to 34 cells (`rule30_scan.py 34 10`; 17 billion right halves, 2 to 3 hours on 10 cores; prediction SC3, no candidate and the longest run still 17). Jobs, commands and hand-back points are in the headers of `rule30_entropy.py` (JOB M3a) and `rule30_scan.py` (JOB M3b). Both optional: neither is on the proof's critical path | **Local** | written; the programs validated on Cloud | **DONE (both).** M3a not possible here (the M5 has 16 GB); M3b ran 2026-10-05 (50 min): SC3 held, no candidate to W = 34, longest run still 17 (a) ran 2026-10-06 with the pool mapped on the NVMe: 0.1229 and 0.1222, EN6 held |
| **M4** | Rule 30, lead 1 of 2026-10-05: the exact record zero runs of the forced left half for 0101... at depths 69, 73, 77 (and 81 if the machine can be left two days), for the doubling law and the renormalisation (RULE30-PRIZE.md §7, §8.14; `records.c`, `rule30_records.py`). JOB M4 in the header of `rule30_records.py`: command, cost per core (about 8 h at 69, 32 h at 73, 128 h at 77, 21 days at 81, divided by the cores), predictions M4a and M4b written before any run, and the hand-back (commit rule30_records_local.txt, add a ledger row, push to main). On the critical path of lead 1 | **Local** | written; the engine validated on Cloud against every known record and the Python search; Cloud ran depths 1 to 61 and 65 (§8.36; M4c added before any Local run) | **DONE.** ran 2026-10-05 (69, 73, 77 by records.c; 81 by records_bits.c): M4a, M4b, M4c held; 85 run (R = 73, all three held); 89 running since 16:27 89 landed 2026-10-06 06:19 (R = 75, 14 h; all predictions held) |
| **G1** | Do error-free transformations (TwoSum, FMA TwoProd) survive each GPU's compiler? The prerequisite for any float-based proof on a GPU | **Local** | write the job and its prediction | **OPEN, not written.** run it on the Arc and the M5 (minutes) |

## Archives, and how to catch up

This file is archived like the chat when it grows long. Archives are numbered in the order they were written and
are never renamed, so a reference to a row ("Local's row of 2026-10-05 12:46") stays valid there.

| Archive | Messages | Ledger rows | Lines |
|---|---|---|---|
| [CLOUD-LOCAL.1.md](CLOUD-LOCAL.1.md) | 2026-10-05 23:44 to 2026-10-07 09:59 | 2026-10-04 13:27 to the evening of 2026-10-07 | about 1,710 |

**Rotation rule** (the owner, 2026-10-07: "the ledgers really need their rotate ... very large text documents are
cumbersome to parse and can even be slow to load in memory past a certain size"). When this file passes about 1,500
lines or about 300 KB, the party who notices rotates it at a quiet moment. Fetch first, then `git mv CLOUD-LOCAL.md
CLOUD-LOCAL.N.md` (the next number). Start a new file with the head above, this section with a new row, and empty
messages and ledger tables with their headers. Announce it in the new ledger and in the chat, and push at once.
`tests/probes/ledger_check.py` fails if an archived row reappears here.

## Messages between the parties

One row to ask another party for something, one row to answer it. Append only; the owner reads these too.
`To` is Local, Cloud, GPT or owner. `Answered` holds the date of the answering row, or is blank.

| Date | From | To | Message | Answered |
|---|---|---|---|---|

## Ledger

Times are the owner's local time (BST). "Arc" is the NAS's GPU, "M5" the Apple-silicon Mac.

| When | Who | Where | What | Commit |
|---|---|---|---|---|
| 2026-10-07 | GPT | Claims GC380 one-column extension of GC378 witnesses | Prediction: both displayed width12 cycles permit an exact column13 extension with free column14. Counterfactual: imposing only the next exact column eliminates both particular witnesses. | Fixed two published cycle fixtures; binary phase graph for column13, independent scalar full-strip replay and mutation. Unexpected check includes112-period extensions so a failed56 closure is not mistaken for nonexistence. No wider state census or departure SAT run. |
| 2026-10-07 | GPT | GC380 exterior-extension attempt fails usefully | Both selected GC378 skeletons have no column13 extension:56/112 closure absent, forward core empty after15/16 sink rounds. Independent bit-row edges PASS; prediction REFUTED, replay/mutation controls VOID. | Only two fixed skeletons eliminated; whole width12 core and column5 uniqueness unresolved. Source/review request recorded; next coupled boundary relation, no wider census this block. |
| 2026-10-07 | GPT | Recovery receipts L233 and L234 | Entry27 filed with control correction received; RK Local lane preserved. Reconstructed reduced-length prior art read with source qualification, trace-closure premise noted in chat. | No fresh Q2 theorem; GC380 two-fixture failure remains distinct from a whole-core result. Updated LENGTH1402 followed before recovery push. |
| 2026-10-07 22:41 | Local | draw-and-work: Q1 drawn again; claims ZR, exact width-free zero-run ratios at position j (scratch C, an extension of L224's rho_j count; the code goes into the outcome entry) | For j = 2 .. 16 and k = 1 .. 6: P(forced left half white at depths j+1 .. j+k | black at j) over right parts, exactly, from the light cone (valid once w >= 2(j+k)+2). Control: k = 0 gives L224's rho_j. Blind: within k <= 6, at least one step is free (ratio 1) for some j, as §8.52 found at finite w; the geometric mean per step over k = 1 .. 6 lies in 0.35 .. 0.65 for every j. Pushed before the run. | |
| 2026-10-07 22:19 | Cloud | CHAT-LEDGER.md, CASUAL-LEDGER.md, CLOUD-LOCAL.md (rotated to .4, .1, .1); tests/probes/ledger_check.py, break_room_seed.py, idle_alarm.py; WORKING-TOGETHER.md | At the owner's request, all three ledgers are rotated. ledger_check.py now guards all three (archived chat headings, break-room headings and dated rows here), with synthetic controls and a counterfactual on copies (a fresh rotation passes, a re-import fails in all three); --branch counts archives of all three. The seed tool and the idle alarm read the newest archive first. Chat CL029. | (this commit) |

| 2026-10-07 | GPT | Claims GC381 finite obstruction certificate | Predict GC380 sink ranks bound every fixed-skeleton extension to at most14 and15 transitions respectively; counterfactual: sink-round count has an off-by-one. | Fixed fixtures only. Reconstruct longest paths and independently replay exact cells1..13; unexpected check rotates starting phase, avoiding phase0-only conclusions. Main push remains approval-blocked; feature branch publication only. Rotation duplicates found after clean Git merge and removed with archived-entry guards. |

| 2026-10-07 | GPT | GC381 finite boundary certificate | Graph14/15 arcs; physical finite strip15/16 transitions after explicit terminal row. Scalar replay PASS; all-phase check exposes starts30/29 vs phase0 limits1/2. Naive physical off-by-one retained and corrected. | Two fixed fixtures only; alternate-path boundary invariant open. Rotation guard PASS after duplicate removal; main push remains approval-blocked. |
| 2026-10-07 22:19 | Cloud | CHAT-LEDGER.md, CASUAL-LEDGER.md, CLOUD-LOCAL.md (rotated to .4, .1, .1); tests/probes/ledger_check.py, break_room_seed.py, idle_alarm.py; WORKING-TOGETHER.md | At the owner's request, all three ledgers are rotated. ledger_check.py now guards all three (archived chat headings, break-room headings and dated rows here), with synthetic controls and a counterfactual on copies (a fresh rotation passes, a re-import fails in all three); --branch counts archives of all three. The seed tool and the idle alarm read the newest archive first. Chat CL029. | (this commit) |
| 2026-10-07 22:41 | Local | draw-and-work: Q1 drawn again; claims ZR, exact width-free zero-run ratios at position j (scratch C, an extension of L224's rho_j count; the code goes into the outcome entry) | For j = 2 .. 16 and k = 1 .. 6: P(forced left half white at depths j+1 .. j+k | black at j) over right parts, exactly, from the light cone (valid once w >= 2(j+k)+2). Control: k = 0 gives L224's rho_j. Blind: within k <= 6, at least one step is free (ratio 1) for some j, as §8.52 found at finite w; the geometric mean per step over k = 1 .. 6 lies in 0.35 .. 0.65 for every j. Pushed before the run. | |
| 2026-10-07 22:21 | Cloud | CLOUD-LOCAL.md (repaired) | The rotation's first casualty, caught by the new check: Local's ZR claim (80a8cf0) appended to the pre-rotation file, and its merge of main (45ec8b4) re-imported about 1,530 archived rows here by union merge. Rebuilt from the rotated file plus the one genuinely new row (Local's, kept verbatim). ledger_check.py passes again. Chat CL030. | (this commit) |

| 2026-10-07 | GPT | GC382 exact core-lift argument and fixed instrument | Bi-infinite projection proves trimming the binary lift of C12 equals the full C13 core, retaining alternative paths and bridges. Source NOT RUN; prediction column5 still ambiguous, counterfactual pinned. | Next fixed1204-candidate run, direct width5-vs-width4-lift control including edges, literal wider scalar checks. No wider census or Local run duplication. |

| 2026-10-07 | GPT | GC382 executed once, outcome queued | Width13 lift1204 candidates,836 retained,15 rounds; only columns2..4 pinned. Prediction HELD, counterfactual REFUTED. Direct width5 vertex/edge and retained scalar edge controls PASS. | Completed, do not rerun. Next batched push publishes outcome; then inspect projected alternatives rather than sweep widths. |
