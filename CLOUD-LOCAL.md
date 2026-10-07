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
| 2026-10-07 22:19 | Cloud | CHAT-LEDGER.md, CASUAL-LEDGER.md, CLOUD-LOCAL.md (rotated to .4, .1, .1); tests/probes/ledger_check.py, break_room_seed.py, idle_alarm.py; WORKING-TOGETHER.md | At the owner's request, all three ledgers are rotated. ledger_check.py now guards all three (archived chat headings, break-room headings and dated rows here), with synthetic controls and a counterfactual on copies (a fresh rotation passes, a re-import fails in all three); --branch counts archives of all three. The seed tool and the idle alarm read the newest archive first. Chat CL029. | (this commit) |
| 2026-10-07 22:20 | Local | draw-and-work: Q1 drawn again; claims ZR, exact width-free zero-run ratios at position j (scratch C, an extension of L224's rho_j count; the code goes into the outcome entry) | For j = 2 .. 16 and k = 1 .. 6: P(forced left half white at depths j+1 .. j+k | black at j) over right parts, exactly, from the light cone (valid once w >= 2(j+k)+2). Control: k = 0 gives L224's rho_j. Blind: within k <= 6, at least one step is free (ratio 1) for some j, as §8.52 found at finite w; the geometric mean per step over k = 1 .. 6 lies in 0.35 .. 0.65 for every j. Pushed before the run. | |
| 2026-10-07 22:21 | Cloud | CLOUD-LOCAL.md (repaired) | The rotation's first casualty, caught by the new check: Local's ZR claim (80a8cf0) appended to the pre-rotation file, and its merge of main (45ec8b4) re-imported about 1,530 archived rows here by union merge. Rebuilt from the rotated file plus the one genuinely new row (Local's, kept verbatim). ledger_check.py passes again. Chat CL030. | (this commit) |
| 2026-10-07 22:43 | Cloud | claims KA, tests/probes/lexicon/rule30_kick_angles.py (row 6.1, after the owner's "why 12?") | The kick classes read in the wheel's rotation angle: class 12 is angle 36/56, inside the wheel's white arc; the survivors 32, 42 and 52 are an unbroken run at angles 40, 42 and 44; and every forward kick in entry 26's settled table lands in the same window, angles 44 to 52 (seen by looking, not yet evidence). KA tests the landing window on the one-turn table and finds each one-turn class's exact death time (KA-C1 reproduces Local's 127 for class 12). Predictions in the header, pushed before the run. | Not a duplicate of KLK: KLK found 12's threshold; KA asks the order and the geometry. |
| 2026-10-07 22:28 | Local | review (asked by GPT, GC380 + GC381): tests/probes/lexicon/rule30_locked_extend_review.py (RV) | An independent coding of the one-column extension: whole rows as integers in the reverse bit order, the set of consistent exterior tuples carried forward, the horizon read off directly (no graph, ranks or endpoint argument). Predictions in the header, pushed before the run: decoding control (k = 0 never dies; reversed decoding dies within 56), a positive control one column in (column 12 exact, never dies), GC381 reproduced (15 and 16 transitions, phases 30 and 29 among the starts, phase 0 gives 2 and 3), and blind: column 14 exact shortens at least one horizon. ZR waits behind this review. | |
| 2026-10-07 22:32 | Local | RV outcome (rule30_locked_extend_review.py); chat L235 | RV-C0 PASS (decoding checked on all 56 phases; reversed bits die within 1), RV-C1 PASS (one column in, the known cycle is seen), RV-P1 HELD (15 and 16 transitions from phases 30 and 29 only; phase 0 gives 2 and 3: GC381 exactly), RV-P2 HELD (column 14 exact: 13 and 16; column 15 exact: 13 and 15; no change at column 16; monotone at every phase). 2.7 s. | |
| 2026-10-07 22:32 | Local | claims KT2: Cloud's strain part 2 (classes 32, 52, 42 at N = 560 and 336) with KK's encoding and kissat, at Cloud's offer in CL029; tests/probes/lexicon/rule30_kick_strain_kissat.py | Predictions in the header, pushed before the run: KT2-C1 (every SAT replays, every instance reaches the solver), KT2-C2 (a case SAT at 560 is SAT at 336), KT2-C3 (class 12 at 336, case (0, 2), UNSAT), KT2-P1 (32 and 52 survive at both N; Cloud's KT-P2), KT2-P2 (class 42 survives at 560; diverging from Cloud's KT-P3). Background, 3 kissat processes, 1,800 s cap per instance, resumable. | |
| 2026-10-07 22:35 | Local | ZR outcome (row Q1): tests/probes/lexicon/rule30_zero_runs.py with rule30_zero_runs.c | ZR-C0 PASS (L224's rho_j exactly, and L225's j = 3 count). ZR-P1 HELD (ten steps equal 1). ZR-P2 REFUTED: at 11 of 15 depths the white run after a black cell hits a step of exactly 0 within six cells (at j = 4, depth 5 is black for every right part); L225's own j = 3 count already showed it. The bounds hold for every configuration with its leftmost black cell at -j. 0.5 s. | |
| 2026-10-07 22:38 | Local | claims ZR2 (Q1, follow-up): the same count at J = 28 and R_real(d), the longest white run of forced cells from depth d over every configuration, against section 8.36's records | Predictions in rule30_zero_runs.py's header, pushed before the run: ZR2-C0 (J = 22 counts reproduced; rho_23 .. rho_26 exact), ZR2-C1 (R_real(d) <= R(d) wherever the run closes), ZR2-P1 (R_real(d) < R(d) at some d <= 20; confidence 0.7). About a minute, one core. GC382/GC383 review (asked by GPT) comes first. | |
| 2026-10-07 22:39 | Local | ZR2 outcome (rule30_zero_runs.py zr2) | ZR2-C0 PASS, ZR2-C1 PASS, ZR2-P1 HELD: R_real(d), the exact longest white run of forced cells from depth d over every configuration, is below the record at d = 6 and 9 .. 19 (4 against 17 at d = 13) and equal at 1 .. 5, 7, 8. Not new in kind: section 8.12 already showed one layer tames the free column 1, and its real-right-halves value from depth 17 is 9, which is ZR2's R_real(17) exactly. New: exactness over every configuration to d = 19. | |
| 2026-10-07 22:42 | Local | claims RV2: review of GC382, GC383 and GC384 (asked by GPT); tests/probes/lexicon/rule30_locked_core_review.py | The complete width-m graph built and trimmed directly (no lift), rows as integers in the reverse bit order, widths 12 to 15. Predictions in the header, pushed before the run: RV2-C0 (602 and 836 vertices, columns 2 .. 4 forced), RV2-C1 (direct core = GPT's lift, vertices and edges), RV2-C2 (both GC383 words on 56-step closed walks), RV2-C3 (stabilizes within 86 rounds; pairs 00/11 only, both; column 5 at 13 always 0), RV2-C4 (pairing at 14 and 15 by projection), RV2-P1 (column 5 unforced at 14 and 15; 0.6), RV2-P2 (the pairing is exact among r-round survivors for some r < 40; 0.5). | |
