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
| [CLOUD-LOCAL.1.md](archive/ledgers/CLOUD-LOCAL.1.md) | 2026-10-05 23:44 to 2026-10-07 09:59 | 2026-10-04 13:27 to the evening of 2026-10-07 | about 1,710 |
| [CLOUD-LOCAL.2.md](archive/ledgers/CLOUD-LOCAL.2.md) | none | 2026-10-07 to 2026-10-08 22:25 BST (767 rows) | about 1,440 |
| [CLOUD-LOCAL.3.md](archive/ledgers/CLOUD-LOCAL.3.md) | 2026-10-08 22:28 to 2026-10-09 15:46 (21 messages) | 2026-10-08 22:25 to 2026-10-09 21:00 BST (558 rows) | about 1,472 |
| [CLOUD-LOCAL.4.md](archive/ledgers/CLOUD-LOCAL.4.md) | 2026-10-09 21:17 to 2026-10-09 21:17 (1 message) | 2026-10-09 21:00 to 2026-10-11 14:24 BST (804 rows) | about 1,748 |
| [CLOUD-LOCAL.5.md](archive/ledgers/CLOUD-LOCAL.5.md) | 2026-10-13 12:16 to 2026-10-15 14:58 (6 messages) | 2026-10-11 14:31 to 2026-10-22 12:23 BST (612 rows) | about 1,810 |

**Rotation rule** (the owner, 2026-10-07: "the ledgers really need their rotate ... very large text documents are
cumbersome to parse and can even be slow to load in memory past a certain size"). When this file passes about 1,500
lines or about 300 KB, the party who notices rotates it at a quiet moment. Fetch first, then `git mv CLOUD-LOCAL.md
CLOUD-LOCAL.N.md` (the next number). Start a new file with the head above, this section with a new row, and empty
messages and ledger tables with their headers. Announce it in the new ledger and in the chat, and push at once.
`tests/probes/ledger_check.py` fails if an archived row reappears here.

*(Since 2026-10-22, the spring clean: the archives live in [archive/ledgers/](archive/ledgers/), unchanged and with their numbers, so the root lists only live files. Rotate with `git mv CLOUD-LOCAL.md archive/ledgers/CLOUD-LOCAL.N.md`. `tests/probes/ledger_check.py` reads both places and notes any archive left at the root.)*

## Messages between the parties

One row to ask another party for something, one row to answer it. Append only; the owner reads these too.
`To` is Local, Cloud, GPT or owner. `Answered` holds the date of the answering row, or is blank.

| Date | From | To | Message | Answered |
|---|---|---|---|---|

## Ledger

Times are the owner's local time (BST). "Arc" is the NAS's GPU, "M5" the Apple-silicon Mac.

| When | Who | Where | What | Commit |
|---|---|---|---|---|
| 2026-10-22 13:24 BST | Cloud | Cloud | CLOUD-LOCAL.md rotated to archive/ledgers/CLOUD-LOCAL.5.md (1,812 lines, 268 KB, 612 rows, 6 messages) and CHAT-LEDGER.md to archive/ledgers/CHAT-LEDGER.16.md (8,871 lines, 600 KB, 292 entries), at the owner's word; announced in CL545. | (this commit) |

| 2026-10-22 13:32 BST | GPT | Intel | MI623/GC1671 CL546 handshake and independent CL495 carrying read | Quiet13min research ACTIVE, no poller; C11 exact three-deletion scalar gaps PROVED with original Cloud proof retained. No experiment/new review request or parent completion claim. Next bounded CL529 localization/finite-interface read, no automatic replay. Rotation/new summary home adopted; HTTPS authorization persists. |

| 2026-10-22 13:50 BST | GPT | Intel | MI624/GC1672 frozen independent CL529 verifier, NOT RUN | Exact old finite basis only; physical witnesses/complete-domain controls/caps frozen in source. One unchanged-source run planned, no larger census/CL530-531 adoption or new review request.13min ACTIVE. |

| 2026-10-22 13:54 BST | GPT | Intel | MI625/GC1673 sole CL529 verifier attempt incomplete | External supervisor denied ps before RSS/control receipt; child exit unavailable, exact-command cleanup found no remaining verifier. No pass/counterexample/retry/source patch. Seek existing Cloud receipt only;13min ACTIVE, no automatic wrapper repair or new review job. |

| 2026-10-22 14:10 BST | GPT | Intel | MI626/GC1674 strict top-tight arbitrary-h ALLR obstruction | Complete HAND witness h12/3336/63,44,44,122: bad actual triple forces both child44 bins through0, while parent partitions. Independent Cloud scope check requested, no formal promotion or h1/h2/one-hole refutation.13min ACTIVE, no CL529 retry. |

| 2026-10-22 14:27 BST | GPT | Intel | MI627/GC1675 deliberate selector incubation | Parent still OPEN; no concrete independent joint-selector step after arbitrary-h ALLR hand obstruction. Research heartbeat PAUSED/no poller; existing review request retained, no duplicate or CL529 retry. Reopen on mechanism-changing response/bridge or owner direction. |

| 2026-10-22 14:37 BST | GPT | Intel | MI628/GC1676 owner-directed prize-swarm lane change | Review all open PRIZE-SWARM.md claims, then pursue full low-prize solutions.13-minute heartbeat ACTIVE, no self-halt. Added prize won column, all No; independent review queue explicit. Eight-streets held, Cloud overnight stays paused. |

| 2026-10-22 14:43 BST | GPT | Intel | MI629/GC1677 all prize-swarm review verdicts | REVIEW-1 scoped PASS/GAP/QUALIFIED for every report. Actual e470 Corollary B counterexample, e710 canonical-Hall wording correction; all prize won No. Next full #708 host-Hall bridge, heartbeat ACTIVE/no self-halt. |
| 2026-10-22 14:40 BST | Cloud | Cloud | Room switch at the owner's word: the prize ladder (CL548) | Cloud works PRIZE-SWARM.md "The ladder continued" (\$100 tier upward); GPT works the twelve swarm problems (GC1676). Cloud heartbeat rearmed every 20 minutes, instinct method, no self-halt. | (this commit) |

| 2026-10-22 14:59 BST | GPT | Intel | MI631/GC1678 #1052 full-prize quantifier corrected | Finiteness is the $10 question; a sixth example only the separate 10-cent bounty. Fixed-component completion is PRIOR-ART, no new solution/experiment/review request. H708 remains open; 13-minute programme ACTIVE, no self-halt. |

| 2026-10-22 15:09 BST | GPT | Intel | MI632/GC1679 #661 multi-residue density guard | Complete HAND finite-field proof, no new novelty/proof number/review queue. Primewise split-prime filters cannot buy cheaper point density; actual norm support remains separate, no full prize or experiment. 13-minute programme ACTIVE, no self-halt. |

| 2026-10-22 15:10 BST | GPT | Intel | MI633/GC1680 supplemental CL550 SDP scope audit | MaxCut identity PASS; SCS primal value is not an upper certificate despite source label. No positive refuted; exact dual condition supplied, original source untouched. Cloud keeps #582, programme ACTIVE. |


| 2026-10-22 15:27 BST | GPT | Intel | MI634/GC1681 complete HAND #132 partial candidate | G342: all but one point cocircular, n >= 7, arbitrary extra point; saturation plus second/fourth moments. One scoped Cloud carrying read requested, no C13 premise or experiment. Full prize open, all prize won No; 13-minute programme ACTIVE. |


| 2026-10-22 15:34 BST | GPT | Intel | MI635/GC1682 direct odd-weird interface scope audit | Known repeated-prime extension and actual divisor blocks retained; primitive-abundant 2205 kills squarefree-largest-prime inference. No new odd example/universal theorem, experiment or review queue. G342 pending one carrying read; programme ACTIVE. |


| 2026-10-22 15:36 BST | GPT | Intel | MI636/GC1683 G342 carrying review adopted | Cloud CL552/71069ac0 checks full hand proof; G342 now PROVED/E2 in cocircular-plus-one n >= 7 family only. Full #132 OPEN, novelty unassessed, all prize won No. No rerun/duplicate review; programme ACTIVE. |


| 2026-10-22 15:47 BST | GPT | Intel | MI637/GC1684 #710 restricted prime-weight repair fails | Actual primorial right vertex overloads any multiplier-only kernel at T^2=o(log n). HAND scope guard, no Hall deficit/asymptotic theorem/experiment/new review queue. G342 remains carried; programme ACTIVE. |

| 2026-10-22 16:03 BST | GPT | Intel | MI638/GC1685 #711 short-direction CRT audit and trajectory | Coordinatewise uniform compression has a collision/log budget with actual period remainders; correlated/prime-support routes remain open. No full prize or experiment/review queue. Next #647 divisor forcing; Cloud CL554 read, #99 lane respected. 13-minute programme ACTIVE, no self-halt. |

| 2026-10-22 16:04 BST | GPT | Intel | MI639/GC1686 immediate CL555 scope warning | Generic perturbation/rescaling makes triangle-free infimum equal exact unrestricted minimum for every fixed n; attainment is the real #99 issue. No numerical replay or prize conclusion, Cloud keeps lane; GPT next #647, programme ACTIVE. |


| 2026-10-22 16:17 BST | GPT | Intel | MI640–641/GC1687 #647 uniformity checked; #634 exact boundary audit | No full #647 implication. Provisional equilateral rational 120-degree branch gives N>18 from two-c-edge premise; source missing-hypothesis/application and N15 interface remain to audit. No promotion/review queue/experiment/prize; 13-minute programme ACTIVE. |

| 2026-10-22 16:32 BST | GPT | Intel | MI642/GC1688 #634 complete HAND boundary candidate | G343 equilateral rational 120-degree branch N>18; one scoped carrying packet also audits literature-dependent N15 composition. No general classification/prize, experiment or table promotion. CL556 read, Cloud retains #99; 13-minute programme ACTIVE. |

| 2026-10-22 16:41 BST | GPT | Intel | MI643–644/GC1689 #552 cash-target attempt and CL557 scope read | No global Ramsey bound; f41=49 already in Boza June 2026 table, valid swarm witness retained. Exact regular polygons give triangle-free KKT points for all n>=4, not local-minimum certificates. Cloud retains #99; next #7 source/interface. G343 pending, programme ACTIVE. |

| 2026-10-22 16:56 BST | GPT | Intel | MI645–646/GC1690 #7 interface and new #32 source audit | #7 full lift unresolved. Radomskii v2 external proof excludes cash O(log X) subquestion; complete deduction/carrying lemma hand-audited, no gap found. Displayed o(log-squared) question open, all prize won No; no experiment/new review queue. G343 pending, programme ACTIVE. |

| 2026-10-22 16:58 BST | GPT | Intel | MI647/GC1691 adopts CL558 carrying read | G343 PROVED/E2 only equilateral rational 120-degree N>18; N15 remains literature-dependent, full #634 open. Source checks read not rerun; all prize won No, no duplicate review queue. Programme ACTIVE. |

| 2026-10-22 17:05 BST | GPT | Intel | MI648/GC1692 block complete, owner-requested pause | #32 repair budget gives no little-o/global reuse theorem. Owner explicitly asked pause after the block; saved heartbeat PAUSED, awaiting their continuance, no poller/background research. Cloud's lane unchanged; all prize won No. |

| 2026-10-22 20:55 BST | GPT | Intel | MI649/GC1693 owner-directed rStation check-in | Registered u/wcm_gpt; posted and byte-verified comment h0qwZbJJbAzqXRgU on Collatz post 35. Reviewed G74/G90/G91 meet source-retaining coupling; missing rare-selection estimate explicit. No new theorem/run/review queue; heartbeat remains PAUSED. |

| 2026-10-22 22:48 BST | Local | M5 | Rule 30 Prize for agents: the Mac is set up (HANDOVER-LOCAL steps 1-5) and submission 1 is built | Engine 15.0 in /Applications, CloudConnect done by the owner; Lean 4.35.0, kit at cc1e0e0, all 56 catalogue modules built; LeanLink 1.2.2 (Problem1 TypeForm Prop); Wolfram Local MCP installed for Claude Code (live after a restart); starter essay built clean twice. White-end module: checker pass on the M5 (207 constants, standard axioms, 4 headlines ok). essay.nb built, UseCache False, 207 s: LeanEnvironment, 3 axioms, KernelCheck Success, no messages. Nothing submitted; waiting for the owner. |

| 2026-10-22 22:50 BST | Local | M5 | Rule 30 Prize submission 1 SUBMITTED on the owner's yes | id R30-20261022-c27323, Problem 1, claim partial, 4 headlines; status Lean Unverified, verifier queued. Page: https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261022-c27323 (opens for the owner's Wolfram ID and the reviewers). Local follows the status. |

| 2026-10-22 22:55 BST | Local | M5 | Submission 1: automatic check timed out (error), maintainer rerun pending | R30-20261022-c27323 still Lean Unverified. Verifier: "did not finish within the four minutes a cloud task gives it, twice. A maintainer runs it again without that limit." Local is timing the essay cells for a possible trimmed resubmission (Cloud and owner to decide). |

| 2026-10-22 23:06 BST | Local | M5 | Submission 1 LEAN VERIFIED | R30-20261022-c27323: maintainer rerun passed 23:06 BST, kernel replay 207 constants, standard axioms, 4 headlines ok, kitCommit cc1e0e0. Next stage Human Verified (a person reads it). |

| 2026-10-22 23:14 BST | Local | M5 | Overnight arrangement: the owner gives standing consent for tonight's submissions | The owner (2026-10-22 23:12 BST): "with my express permission to submit every one". Local runs a 20-minute heartbeat overnight: for each submission Cloud announces, checker pass on the M5, essay build and read-back, byline and privacy check, then submit (5/hour, 20/day), record and flag. The per-item owner yes is waived for tonight by the owner's word; the other gates stand. |

| 2026-10-22 23:44 BST | Local | M5 | Submission 2a (words-A) SUBMITTED on the owner's standing consent | R30-20261022-5c4fbf, Problem 1, partial, headlines not_eventuallyWord_words and words_general. Gates: checker pass on the M5 (257 constants, standard axioms; build 70 s, check 57 s), essay.nb built UseCache False in 124 s, read back clean (LeanEnvironment, 3 axioms, KernelChecked, no messages, no $Failed), byline as set, nothing private. Status Lean Unverified, verifier queued. words-B held until this automatic check reports (CL575). |

| 2026-10-22 23:53 BST | Local | M5 | words-A automatic check timed out twice (error); maintainer rerun pending; words-B HELD per CL575 | R30-20261022-5c4fbf still Lean Unverified. Verifier log: each attempt ~3 min "evaluating the notebook" then ~1 min "building" before the 4-min cut; the M5 build was 124 s, so the verifier runs about 2x slower. Local flags Cloud for the words-B decision. |

| 2026-10-23 00:01 BST | Local | M5 | Submission 3 (diagonals) SUBMITTED on the owner's standing consent | R30-20261022-0616de, Problem 1, partial, 8 headlines (B1, B2, B3 on the kit's D). Gates: checker pass on the M5 (162 constants, standard axioms; build 26 s, check 6 s), essay.nb built UseCache False in 46 s, read back clean, byline as set, nothing private. Lean Unverified, verifier queued. |

| 2026-10-23 00:03 BST | Local | M5 | Submission 3 (diagonals) LEAN VERIFIED automatically | R30-20261022-0616de: first attempt passed at 00:02 BST (kernel replay, standard axioms, 8 headlines). The first automatic pass: the module is light (162 constants, hand proofs). |
| 2026-10-23 00:03 BST | Local | M5 | Submission 4 (theorem-a4) SUBMITTED on the owner's standing consent | R30-20261022-1d5070, Problem 1, partial, 6 headlines (center_A4_sharp and A4, A3, B3). Gates: checker pass on the M5 (106 constants, standard axioms; build 22 s, check 6 s), essay.nb built UseCache False in 25 s, read back clean, byline as set, nothing private. Lean Unverified, verifier queued. |

| 2026-10-23 00:09 BST | Local | M5 | Submission 4 (theorem-a4) LEAN VERIFIED automatically | R30-20261022-1d5070: first attempt passed at 00:04 BST (kernel replay, standard axioms, 6 headlines). |
| 2026-10-23 00:09 BST | Local | M5 | Submission 5 (corollary-f) SUBMITTED on the owner's standing consent | R30-20261022-91b0b0, Problem 1, partial, 6 headlines (corollary_F and its lemmas). Gates: checker pass on the M5 (189 constants, standard axioms; build 23 s, check 6 s), essay.nb built UseCache False in 26 s, read back clean, byline as set, nothing private. Lean Unverified, verifier queued. CL579: words-B goes as it is, next. |

| 2026-10-23 00:10 BST | Local | M5 | Submission 5 (corollary-f) LEAN VERIFIED automatically | R30-20261022-91b0b0: first attempt passed at 00:09 BST (kernel replay, standard axioms, 6 headlines). |
| 2026-10-23 00:10 BST | Local | M5 | Submission 2b (words-B) SUBMITTED on the owner's standing consent (CL579: as it is) | R30-20261022-70d23b, Problem 1, partial, 2 headlines. Gates: checker pass on the M5 (321 constants, standard axioms; build 65 s, check 48 s), essay.nb built UseCache False in 116 s, read back clean, byline as set, nothing private. Lean Unverified, queued; a maintainer rerun is expected, as for words-A. Five of five used this hour; the queue is empty. |

| 2026-10-23 00:18 BST | Local | M5 | words-B automatic check timed out twice (error), as expected; maintainer rerun pending | R30-20261022-70d23b still Lean Unverified. The other five unchanged (1, 3, 4, 5 Lean Verified; words-A awaiting its rerun). No new module from Cloud this tick. |

| 2026-10-23 00:44 BST | Local | M5 | words-A LEAN VERIFIED (maintainer rerun) | R30-20261022-5c4fbf: rerun passed at 00:44 BST, "Kernel replay passed; standard axioms only." words-B's rerun is in its last stage. |
| 2026-10-23 00:44 BST | Local | M5 | Submission 6 (rule-210) SUBMITTED on the owner's standing consent | R30-20261022-920c1b, Problem 1, partial, 6 headlines (not_Q01_210, parity_invariant, linear, ...). Gates: checker pass on the M5 (29 constants, standard axioms, the headline on propext and Quot.sound only; build 29 s, check 5 s), essay.nb built UseCache False in 29 s, read back clean, byline as set, nothing private. Lean Unverified, queued. |

| 2026-10-23 00:46 BST | Local | M5 | words-B LEAN VERIFIED (maintainer rerun) and rule-210 LEAN VERIFIED (automatic) | R30-20261022-70d23b rerun passed 00:44 BST; R30-20261022-920c1b first attempt passed 00:46 BST. All seven submissions are Lean Verified. Queue empty. |

| 2026-10-23 01:00 BST | Local | M5 | Submission 7 (sturmian, extended per CL582) SUBMITTED on the owner's standing consent | R30-20261023-e872a3, Problem 1, partial, 7 headlines (characteristic_excluded, characteristic_block_excluded, ...). Gates: checker pass on the M5 (266 constants, standard axioms; build 26 s, check 7 s), essay.nb built UseCache False in 28 s, read back clean, byline as set, nothing private. Lean Unverified, queued. The other seven unchanged, all Lean Verified. |

| 2026-10-23 01:02 BST | Local | M5 | Submission 7 (sturmian) LEAN VERIFIED automatically | R30-20261023-e872a3: first attempt passed at 01:02 BST. Eight of eight Lean Verified. Queue empty. |

| 2026-10-23 04:58 BST | Local | M5 | Overnight arrangement ended: the owner is awake (04:5x BST), Cloud paused (CL585); Local's 20-minute heartbeat stopped | Eight submissions, all Lean Verified, awaiting Human Verified. The per-item owner yes applies again from here unless the owner says otherwise. |

| 2026-10-23 05:11 BST | GPT | Intel | MI650/GC1694 response to CL582 | Complete HAND alternative: factor complexity n+1 plus mechanical telescoping gives Corollary F pairs with K1, unbounded gaps, every intercept; no continued fractions. Scoped carrying read requested; frozen submissions unchanged, CL586 reviews received not completed, heartbeat PAUSED. |

| 2026-10-23 05:21 BST | GPT | Intel | MI651/GC1695–1697 completes CL586's three second reads | All formal claims PASS; Corollary F essay needs the already-adopted growth hypothesis, Sturmian nesting starts at std1. Rule-210 clamp/phase carried. Frozen files unchanged, no replay/resubmission; report sent to Cloud, heartbeat PAUSED. |

| 2026-10-23 05:38 BST | GPT | Intel | GC1698 accepts CL587 and freezes job1 controls | Full PROOFS32 statement chain written; finite source/caps published before one bounded run. Then channel widths16/20 and Theorem E second read on arrival. GC1694 carrying read adopted; heartbeat PAUSED. |

| 2026-10-23 05:40 BST | GPT | Intel | MI652/GC1700 CL587 job1 complete | Exact PROOFS32 induction chain ready; bounded revised controls pass, original resource failure retained. GC1694 carrying read adopted from CL587. Continuing channel16/20; Theorem E review on arrival, heartbeat PAUSED. |
