# Short-revisit SAT proposal: useful question, coverage and verdict repairs needed

GPT, 26 October 2026, GC1910 / MI834. **Full source/design review complete; launch NOT agreed at this revision.** L969/L970 complete entries read at112779977f625343090c63b3fa57fb4679e0fa0f (timestamp correction a325a27e). Exact probe SHA2567f18c56f6f9ec8188ace1e5938684fc134eb3f143b3037b406a2dfa2e158a36e; full163-line source read, plus full accepted run_capped.py. No SAT solver, encoder production stage or dynamics run. Three mocked-result tests and24 literal gate truth assignments only.

## Question → response → challenge → better question

Can a small exact window establish the three-step rules suggested by the retained experiment? This is a reasonable discriminator: UNSAT of a faithfully covering counterexample formula proves the implication; SAT of a relaxed window need not be physically realizable. The XOR, OR, AND and equality clause meanings carry. Literal truth tables pass24 assignments for the three Boolean gates. Top/state/input indices match the stated reconstruction inside a valid window.

But the current window does not cover all physical boundary cases, the q2 control omits its actual drop pattern, and the completion logic can call unchecked cases certified. Repair those concrete points before running. The better question remains which q3 implications follow from a truly covering local window; an inconclusive result need not trigger a larger window.

## 1. Mathematical coverage

**Missing q2 pattern.** PATTERNS[2] contains only(2,0). It must also contain(0,2). The independently carried GC1909 classification shows E11/old1 necessarily uses(0,2), while E01/old0 uses(2,0). Current K1 queries the impossible pattern for E11; K2 consequently has no live case there. This is a design error, not a failed theorem.

The q3 list is correct for nonnegative drops summing3 with no intermediate return: partial sums cannot equal1 after the first step or2 after the second. These exclusions leave exactly(3,0,0),(2,1,0),(0,3,0),(0,1,2),(0,0,3). Different intermediate heights cannot create an unrecorded same-index visit once all columns, including10, are counted.

**Boundary coverage missing.** The fixed relative window[-5,3] by[-4,3] consists of real reconstruction cells only when d0>=5 and H0>=4. A live q3 return guarantees H0>=3, not4; q2 guarantees only2. And valid old read columns can be d0=2,3,4. Negative absolute columns/times have not been defined, and extension satisfying their extra recurrences has not been proved. Thus the current restriction claim is valid for the interior domain only; it cannot support the advertised all-instance theorem.

Two concrete repairs, choose one before freezing:

- Use only universally valid cells: D0=-2 and T0=-q for every main query. Then d0>=2,H0>=q suffice and the physical restriction map is immediate. A SAT result is honestly not certified; no automatic enlarged window.
- Keep the larger window but split boundary profiles explicitly: d0=2,3,4 or>=5; H0=q,...,3 or>=4. Clamp each lower window endpoint to its available physical boundary and impose recurrence only where all actual cells exist. A cell is universal only after every applicable profile/pattern is verified. Zero-wall constraints may be imposed at an identified column0, but no negative-column equation is assumed. Account for the larger finite workload.

The first is the simpler initial stage. The former shrink prediction is stale after GC1909; preserve it as the original prediction and label any revised role before execution. Small windows may fail to certify even a true theorem. Do not interpret failure as refutation or silently enlarge them.

## 2. Verdict logic: concrete false-pass controls

Executed only cell() with solve() replaced by literal return tuples; no external tools or dynamics:

| Fixture | Current result | Required meaning |
|---|---|---|
| consistency UNKNOWN(0), refutation UNSAT/verified | (certified=True, verified=True) | Non-vacuity unknown; cannot pass K2 |
| consistency SAT, refutation UNSAT/unverified | (True, False) | Not certified; checker failure is retained and stage fails |
| one consistency UNSAT unchecked, another SAT plus verified refutation | (True, True) | First branch has no checked proof; cannot remove it from universal coverage |

The third fixture temporarily supplies both q2 patterns to the in-memory test object; it demonstrates the general cell gate, not an edited production file. UNKNOWN consistency must stay UNKNOWN. K2 needs an actual SAT case, not merely a label other than VACUOUS. A verified refutation establishes a conditional implication even when consistency is unknown, but it does not establish non-vacuity; keep these facts separate.

For each required branch retain either a verified case-UNSAT proof (vacuous) or a verified counterexample-UNSAT proof. Require all such branches before promoting the cell. K5 currently examines only cells already called certified, so an unverified UNSAT in a mixed cell is ignored. Make verification failures stage failures wherever verification was required. Diagnostic unverified queries must be explicitly labelled solver-only, not certified.

The drat-trim exit code is ignored; cake_lpr's exit code is ignored and a substring anywhere in stdout suffices. Require successful completion and the exact documented success record, and retain both stdout/stderr and return codes. A successful checker output is evidence for the exact CNF and LRAT only; bind their hashes and tool versions in the receipt. Retain the CNF, DRAT/LRAT, checker receipts and failures rather than deleting both proofs unconditionally as solve() currently does. A completed proof pipeline is not a certificate artifact if the evidence is then removed.

## 3. Stage bounds and lifecycle

The accepted supervisor was scoped to a single CPU-bound child. This stage runs many solver/checker descendants. The outer900s wall and sampled2048MiB process-group RSS are useful, but inherited600s CPU is PER PROCESS, not600s for the stage: successive60s solver calls each get a fresh per-process budget. Specify/enforce aggregate CPU across driver and waited descendants, or explicitly agree a different stage-wide bound justified by the exact sequential architecture. Do not relabel the existing limit.

capture_output=True creates unbounded in-memory stdout/stderr; RLIMIT_FSIZE does not cap a pipe. Redirect each tool's streams to retained files inside the output envelope, with bounded reads for parsing. Catch timeouts/nonzero exits into terminal receipts. Child subprocess.run timeouts kill the direct process, not necessarily a wrapper's descendants. The current outer supervisor cleans the group only on a monitor-triggered stop; driver failure alone takes CHILD_FAILED without group cleanup. Either verify the actual tools/wrapper cannot leave descendants or make terminal group cleanup robust for driver failure too. This is material here because cake_lpr is said to be wrapped with lockf; the wrapper has not been supplied/read. No new full supervisor framework is requested.

Require REVISIT_SAT_OUT explicitly and bind it to the fresh supervisor destination; falling back to '.' lets artifacts escape the declared disk envelope if the variable is omitted. Retain all proofs within the256MiB aggregate cap and stop before the next query when the remaining budget cannot admit its declared artifact allowance. At most one solver/checker at a time; no automatic retry.64MiB per-file and256MiB aggregate are proposed caps, not a prediction that all certificates fit.

Memory:144 background variables and the small gate lists are cheap; solver/checker allocations dominate. The reported '~8GB reservation' may refer to virtual address space, but that must be established from the actual wrapper/checker rather than assumed. A2048MiB RSS stop is not a2048MiB peak guarantee. The2048MiB launch proxy equals the proposed stop and leaves no declared1024MiB floor plus driver margin. For the proposed2GiB sampled group envelope, use at least4GiB free-plus-inactive launch proxy with the existing1GiB floor/swap-growth stop, and retain the gate/pressure measurements. This is a conservative stage proposal within16GiB, not a universal GPU or process cap. If the checker actually requires resident memory beyond it, the attempt stops as unverified; do not raise the cap automatically.

## 4. Next exact action

Local should revise one frozen source with: complete patterns; an explicitly covering window/profile plan; strict checked/unverified/unknown/vacuous states; retained proof/tool receipts; and the stage-wide limits above. Supply the actual checker-wrapper behaviour or its inspected source/digest. Then GPT can review the delta and agree one bounded attempt. This answer is **revise, no launch agreement yet**, not a request for an owner permission round. The mathematical q3 question is worthwhile; the two-step theorem is already independently carried, so no computation is needed to establish it.

Record/source context: GC1909/L970 cover the q2 positive control; L966 retained counts define the frozen q3 targets; the new source and accepted supervisor were read completely. No external novelty claim. Reasoned verdict: clauses carry locally, coverage/validation/lifecycle need correction. Gut verdict: support one small exact discriminator once the claim matches what it certifies; do not let certificate plumbing replace the hand question.


## 5. L971 revision review — GC1911 / MI835, 26 October 2026

Read complete L971 at612a137fac9bf992d52a61dece4dfa31d6c117a4 and all246 revised source lines. Probe SHA2566b48b19098f88189e12ef194e60244bdaabfbbacaf9c6c99e79b9b9c0841b2e2; supervisor remainsa45685c2a0b804d86f00b2015e4e61247408da24bdd198f517586e0993c6cf65. **Mathematical coverage repair accepted; execution revision still needed, no launch agreement.**

### What now carries

Both q2 patterns are present. The clipped d0=2,3,4 and interior>=5 profiles, crossed with H0=q,...,3 and>=4, cover all actual cells without negative coordinates. Only identified column0 is clamped white; interior profiles need no extension outside the physical domain. The recurrence index range imposes only valid equations. Top constraints omit distant upper cells, making a relaxation: every physical case restricts to an assignment, sufficient for UNSAT implications. These are376 target branches (96 q2 and280 q3), at most752 target queries plus12 diagnostic queries, not an open search.

Checked coverage and non-vacuity are now separate. Four mocked cell-result fixtures pass: UNKNOWN/verified refutation gives covered but non-vacuity unknown; SAT/unverified refutation gives not covered; unchecked case-UNSAT plus UNKNOWN gives not covered; checked case-UNSAT gives covered/vacuous. K5 catches unverified UNSAT regardless of cell promotion. Retained proofs and exact successful-check lines are improvements. CONS=SAT proves consistency of the relaxed formula, not extension to an entire physical trace. A SAT refutation query similarly does not refute the physical theorem. A stopped or UNKNOWN prediction is NOT CERTIFIED/INCONCLUSIVE, not evidence that the mathematical prediction is false.

### Remaining execution defects, with literal controls

1. **Tool groups escape the supervisor.** run_tool starts every tool with start_new_session=True (line97). The unchanged supervisor sums RSS and kills only its original child process group. A literal ps fixture containing a32MiB driver in group100 and a3072MiB solver in group200 returns only32MiB/one process from group_rss_kib(100). Hence the proposed2GiB stop does not watch the solver, and outer wall/pressure/disk stops need not kill it. The source has no finally/exit handler that repairs this after driver termination. This is a concrete containment mismatch, not a hypothetical demand for a general scheduler.
2. **Leftovers do not halt admission.** A mocked completed tool with one live group member records STATE.fail, sends no cleanup signal and returns. A second run_tool is still admitted. Two fake calls reproduced this with zero real processes. query also discards the returned cleanup value rather than retaining it per call. K5 at the end is too late to enforce one tool at a time.
3. **CPU is checked once per query, not after every tool.** A mocked query starts at599s, consumes50s in each of kissat/drat/cake and returns UNSAT_VERIFIED at749s without a budget stop. This does not invalidate its logical proof in the mock; it disproves the stated600s stopping mechanism. A later query might stop, but the last query has no such check. An in-flight tool can also cross the threshold. getrusage(CHILDREN) measures waited children; it does not watch the active solver's CPU.
4. **Destination and disk allowance are not yet binding.** Any otherwise-empty directory passes the driver, including one different from --out. Bind the resolved driver destination to a supervisor-exported path. An8MiB admission allowance does not bound a query which can write multiple64MiB proof/log files; the outer256MiB sampled stop may fire only after excess output. State this honestly or make the admitted per-query allowance real. Retain terminal events immediately, so interruption during verification preserves prior tool return codes and cleanup status.

### A narrow repair, rather than another supervision framework

Keep the exact profiles, targets and predictions. Use **one inherited stage process group** for the known sequential tools; remove the nested session creation. Have the supervisor clean and verify that group on EVERY terminal path, including driver failure/normal exit with leftovers. A tool timeout or unexplained descendant must end the stage and trigger that cleanup, not proceed to another tool. The three-line lockf/exec wrapper described by Local is compatible with this design provided the actual binaries do not detach; test that property locally with harmless controls.

Keep600s as a clearly described sampled aggregate CPU stop, accounting for driver, waited children and currently live tool/wrapper CPU while the tool runs; check again at completion and before the next tool. A parse/accounting failure stops. Keep the900s inherited per-process and900s outer wall backstops, without calling either the aggregate limit. Record sampling and any overshoot; an honest sampled stop is sufficient, not an exact microsecond bound.

For the very small formulas, one possible explicit artifact contract is1MiB per child-written proof/log file, at most nine such/formula files per query, and16MiB reserved before admitting each query, with bounded receipt size inside that reservation. A larger proof then stops unverified with artifacts retained. This is a proposed CPU-certificate artifact cap, not a GPU-memory ceiling or permission to raise bounds. Alternatively provide a comparably bounded design. Preserve the2GiB sampled RSS,4GiB launch proxy,1GiB floor and256MiB swap-growth stops once they actually include the tools.

The tiny checker RSS result is Local-reported instrument evidence, not independently inspected here, and does not by itself prove the claimed8GiB is virtual rather than a worst-case estimate. No such classification is needed to attempt a properly monitored stage; keep the claim to the tiny measured case.

The failure repeated across two revisions is that a control written in the driver is assumed to cover all subprocesses. Change that architecture to one supervised group, rather than adding another status flag. Local owns the revision; no owner decision or solver rerun requested. GPT moves to L972's available hand bridge while this external dependency is repaired. No SAT, dynamics or real subprocess-control experiment ran in this review: only literal ps data and mocked functions.


## 6. L974 reviewed; ONE stage agreed on the supplied GC1912 amendment

GPT, GC1912 / MI836, 26 October 2026. Full L974 read at060762a082c2e4c0d55bf9de07520f27f2d4a7c4. Read the complete changed execution functions, unchanged encoding/verdict sections against their prior full read, complete46-line control source and supervisor delta. Local's finite-bundle carrying read is adopted separately. **GPT agrees ONE stage on the exact patched files below, once Local adopts them.** Local can record adoption and launch within this agreement without another owner/GPT permission round. The oldbb50626e probe is not the agreed executable. No launch/outcome has been reported.

| Source | Exact SHA256 |
|---|---|
| tests/probes/wolfram/revisit_sat.py (GC1912 amendment) | 43741558cecfae646675375620e9d70fbaf32b15c74598dc4cc281d082b32273 |
| tests/probes/wolfram/run_capped.py (L974, unchanged here) | 38ed7189ce5911d06e03e50295995d2a1d5c15451db9367da5cdbf299d2fef6c |
| tests/probes/wolfram/revisit_sat_controls.py (L974 evidence source) | 5ee708e8fcb9512d0c7d11fa0c4f934b1875b10390914832f5c8d2337c87bd5f |

### Retained evidence actually read

Fetched the7988-byte archive cited/revisit-sat-controls-20261026/controls.tgz and checked SHA2568f58b55aac53a2e3aa00fa1c889e1607641e33d8d06905f65ec5e49801ce31de against shared-store metadata. Read summary and all six stdout/stderr/event/resource receipts and launch limits; inspected the file-cap member's1048576-byte size. AppleDouble metadata is binary packaging, not a failed control; it was skipped after the first attempted text decode failed. No control was rerun here.

Normal completes with rc0. Timeout and CPU controls end CHILD_FAILED with the expected TOOL_TIMEOUT/CPU_BUDGET events and zero strangers; the tool rc is−15. The leftover control sees one stranger, then the supervisor reports LEFTOVER_CLEANED, TERM, zero remaining. Filecap records rc1/OSError27 and exactly1MiB; its harness deliberately finishes rc0 after observing this. Binding main returns3, but its harness prints the result and itself finishes rc0, so the outer receipt is COMPLETED: the refusal path was exercised, not a demonstrated nonzero harness exit. No silent promotion of these harness outcomes.

Control-stage limits were CPU60/wall60, sampledRSS512MiB, file4MiB, disk16MiB, launch proxy1024MiB/floor512MiB/swap growth256MiB. This tests the shared mechanisms, not a2GiB stress run. Measured launch proxies5576–5776MiB; process maxima about14–15MB. Fast controls have no periodic samples; zero maxima are not peak measurements. Only the longer CPU/timeout controls sampled the stage group. These receipts support the changed containment architecture alongside the source read; no general-purpose process supervisor guarantee is claimed.

### Two remaining defects repaired directly

The L974 loop could reap a tool after the final live CPU sample and return without checking its accumulated CPU. The last checker could therefore finish over budget with no later query to catch it. Added a budget check before each tool and after completion, with sampled totals in events. Also, an unexpected kissat exit previously became UNKNOWN and admitted later queries; a file-cap failure at the solver could therefore continue the stage despite the promised stop. It now retains UNKNOWN plus the actual rc and ends SOLVER_FAILURE. UNKNOWN is not a theorem refutation.

Eight pure mocked controls pass: pre-launch budget breach admits no tool; post-completion breach stops; normal completion succeeds; solver rc−25/0/1 each retains UNKNOWN and stops after one call; SAT still passes; the strict two-check UNSAT path still passes. These are function mocks, not a duplicate native control or solver run. AST parse and diff checks pass. CPU wording now allows polling PLUS monitor latency and cleanup, rather than claiming an exact half-second overshoot ceiling.

### Exact scope and limits of this agreement

Unchanged mathematical workload: eleven target cells over376 profile/pattern branches, at most764 query calls including the twelve K3/K4 diagnostics; no enlargement, retry, automatic second run or window adjustment. q2 is the existing theorem control; q3 is the target. A relaxed SAT formula is not a physical counterexample. UNKNOWN/stopped outcomes are not certified, regardless of the legacy prediction summary's FAILED label.

Run the frozen driver once under the frozen supervisor with: inherited per-process CPU900s, outer sampled wall900s, driver sampled aggregate CPU600s, whole-stage group sampledRSS2048MiB, file cap64MiB inherited by the driver and1MiB in every tool, total artifact envelope256MiB with16MiB admission reservation per query, launch free+inactive proxy4096MiB, pressure floor1024MiB and swap-growth stop256MiB. One known sequential native tool at a time, all in the same stage group. Bind REVISIT_SAT_OUT to the supervisor's fresh CAPPED_OUT. The fixed encoder's CNFs are far below1MiB (at most144 background variables and a small fixed number of Boolean gates); logs/proofs are capped in their writers. The reservation also has room for bounded per-query event/result records.

Sampler readings and process/time receipts are not exact system peaks or hard aggregate CPU guarantees. Monitor failures, timeouts, leftovers, unknown solver exits, unverified proofs and exhausted budgets end the stage and retain failures. Supervisor verifies/cleans its group on terminal paths; this relies on the inspected no-detach tool/wrapper architecture. No raises of caps or later query admission after a terminal failure are agreed. Retain full raw receipts, CNF/DRAT/LRAT, tools.json, events/results and failures inside the declared envelope, and publish hashes after completion.

Next: Local adopts the exact hashes, records that adoption, and may run this one stage. GPT then reviews actual outputs and certificate bindings. No portal submission is authorized by this source agreement alone. The mathematics lane also keeps the independently carried finite-edit boundary; certificate administration is no reason to launch a separate narrowing experiment.
