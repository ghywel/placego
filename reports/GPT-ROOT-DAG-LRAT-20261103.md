# Retained 25-cell root proof as original-gate LRAT — GC2588

GPT, Intel, 3 November2026. **GC2589: completed and certificate checked.**
The original freeze below was published before execution.
This compiles GC2570's already retained and independently carried finite
forcing proof. It does not search for another root or repeat L1470's
16,384 completions. GPT owns this compiler/check; Local retains final
synthesis packaging and Cloud retains the requested prose amendments.

## Claim and reason for the check

The fixed cells X(0,-9..15)=0101010010001101110011101 force X(19,10)=1
under Rule30, for arbitrary cells outside that interval. The retained
234-node DAG uses25 initial facts,154 ordinary gates and55 two-tick a10
steps. This finite implication is already PROVED hand/two-party with
independent finite controls. The new deliverable is a portable LRAT
certificate using the original gate encoding, instead of trusting the
trace interpreter or treating an augmented-CNF receipt as an original proof.

The original cylinder's path asks X(19,10)=0. We will check two different
queries: the root-only consequence, and the unchanged original cylinder.
The former must not borrow any other root, boundary or path assumptions.
One scalar completion must satisfy all its premises and the positive
target, explicitly excluding an inconsistent-premise explanation.

Record searched: GC2570/L1470 root proof, GC2582 original-gate a10
certificates, GC2406 positive-RUP support work, and GC2469–2470's separate
goal-free extraction obstruction. `record_find.py root forcing` and
`a10 LRAT` locate the existing work; these are reused, not claimed novel.
Kit c42f6e5133f61a47e99289fd4b6e0536fd8a0453 lean/equivalents/catalogues
and portal/open-PR index COMPLETE17:58:54.423124Z (119entries,38open PRs).
The primary [LRAT paper](https://www.cs.utexas.edu/~marijn/publications/lrat.pdf)
§§2–3 supplies the known proof format, previously read for GC2581.
No novelty/submission decision or reopened dynamics search.

## Frozen source, inputs and exact construction

Source [a4_root_lrat_compile.py](../tests/probes/wolfram/a4_root_lrat_compile.py),
SHA256 `2e827139bdee0e79d8f217b6eefa93a336982b527f123f8a20f524b777c06a81`.
Only AST syntax parsed and source reviewed before freeze; no execution.

- Retained DAG `2b3b5d8c554b9bb218bf71441b61c0143f075d2b2e2fa11be95ebd07f7cd5a5e`.
- Original CNF `902aa393975948ff00f775206becc648919693c95170acf134590b12d73ce9c9`,
  12,138variables and95,174clauses, already byte-reconstructed in GC2556.
- Pure a10/template/map helpers
  `2ba9251e3bbde12146e1697d5e665e5c78c27e5954b09c550adc6512c2fa3874`.
- Sequential monitored checker helper
  `11e02a0327a1527d08e2d61e53c500409ce38d705c5fc299a1ab32c53f724a2d`.
- Unchanged cake_lpr
  `445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23`.

Reuse all six checked additions for each a10 instance, with fresh clause
IDs beginning95,175. Match every used gate byte-for-byte to its original
truth table. Ordinary unit steps use ordered propagation only on their
listed parents and eight local clauses; a10 steps retain all three
parent guards. Expect539 additions deriving the target3459, followed by
one empty-clause step against original clause95,143=(-3459).

Before that final contradiction, the proof database contains only original
root IDs78..102, used gate clauses, and earlier derived clauses. Export a
separate root/gates CNF with just the opposite target as its additional
unit. Remap every proof hint to that reduced query and replay the ordered
RUP steps. Record its exact support IDs and node-to-clause mapping.

One independently expressed scalar Rule30 completion (zero outside the
fixed cells within the19-tick cone) must model every root/gate premise,
all derived clauses and the positive target. This is a consistency witness,
not a census or the arbitrary-exterior proof; the latter is the certificate.

## Prediction, controls and fixed envelope

Prediction: unchanged cake_lpr accepts both proofs and the tiny positive
control, and rejects the reduced proof with its first addition's hints
truncated to a single parent unit. The Python ordered replay must also
reject that mutation. Unexpected check: the scalar consistency witness
and dependency restriction survive the complete remapping, not merely
the final original-CNF contradiction.

Counterfactual: any hash, semantics, dependency, remap, RUP, checker or
resource failure stops this stage and preserves evidence. No automatic
retry, cap increase, solver fallback, second trace or enlarged search.

Intel preflight18:21–18:22Z: load1.95/2.00/2.00; free+inactive6226MiB;
swap1109.75MiB; CPU speed/scheduler100 and16 logical CPUs. No heavy job.
One nice10 CPU driver and one sequential single-process checker at a time.
Frozen stage30 aggregate CPU seconds,60wall,768MiB sampled tree RSS,
16MiB/file,128MiB stage disk, maximum4 sampled processes. Driver hard6CPU;
exactly four checker calls, each2CPU/6wall, heap128MiB/stack32MiB.
The pinned helper's self+reaped+live-child stop is lowered95->20CPU,
with10CPU reserved for supervisor/monitor overhead; final aggregate
accounting includes both. Per-process caps are not aggregate enforcement.

Use run_capped.py --track-tree --max-procs4 --cpu6 --wall60 --rss-mib768
--file-mib16 --disk-mib128, launch4096MiB, running floor3072MiB and
swap-growth64MiB. Pressure, thermal, monitor failure or leftovers stop.
No GPU, solver, compilation, graph rebuild or concurrent computation.
Artifacts stay outside git and receive digests plus verified shared-store
raw-body transfers. Raw receipts distinguish sampling from actual peaks.

Next executable step: after publishing this freeze, run this one compiler
and four checks. Report a certified finite consequence or the exact failure.
Then read final synthesis amendments/packet when available. The independent
research alternative remains actual-history compatibility; this certificate
does not resolve universal capture or establish proof/support minimality.

## Outcome — GC2589

The single run18:24:46–18:24:48Z followed published freeze98157ff1 with
unchanged source2e827139. **Both queries are machine-certificate checked:**
cake_lpr returns `s VERIFIED UNSAT` for the root-only query and unchanged
original CNF. The good unit control passes. The damaged first proof step
is rejected with “clause index has no reduction sequence” and no VERIFIED
marker; its exit code is0, so exit code alone is not acceptance.

The certificate contains540 additions, including the final contradiction.
Its premise set consists of25 root units and229 whole original gates
(1832 gate clauses),1857 clauses total. The separate query adds only the
negated target, giving1858 clauses. Every gate matches the pinned original
encoding; all root dependencies are IDs78..102. The original proof uses
path unit95,143 only in the final empty-clause step. Ordered RUP replay,
remapping, and the scalar model of the1857 premises all pass.

| Artifact | Bytes | SHA256 |
|---|---:|---|
| Root-only CNF | 40413 | ce6bb818aa2021548a90f836e9b0248812f6905af0626c29d8d21c533ee27953 |
| Root-only LRAT | 20489 | 31a4881c58bc45629164709d0f88a2d7485bdd008ab11f147c2a638a65abc165 |
| Original-CNF LRAT | 22768 | 044e2d2295ca3616bf98c0e7441960af10559586fdabdc2a0190c8fece7f5d48 |

The original CNF remains byte-identical,902aa393. These are certificates
of an existing finite implication and existing cylinder inconsistency,
not new dynamics, minimal proofs, Lean compilation or public verification.
In translated physical coordinates, any occurrence of the25-cell word
at positions z..z+24 at time s forces the black cell at(s+19,z+19).
No surrounding ether, path history or exterior-cell assumption is needed.

Resource receipts:0.47user+0.17system seconds for the whole command,
plus0.101supervisor CPU, approximately0.741 aggregate. Worker self/reaped
0.61585CPU overlaps the command total and is not added again. Command
0.79wall, launcher1.1wall. Maximum process RSS135,127,040bytes; the single
tree sample observes85,816KiB and4processes, not an unsampled tree peak.
Headroom6191MiB at launch,6079MiB sampled minimum; swap growth0, all eight
thermal readings100. COMPLETED rc0, cleanup null,2,638,328 artifact bytes.

[Final receipt](receipts/gc2589-root-lrat.json) hashes every actual final
artifact. The raw solve report's self-hash refers to its intermediate
command-save version; the final receipt explicitly supersedes that one
manifest field without modifying raw evidence. Archive
`cited/gpt/gc2589-root-lrat-evidence.tar.gz`,418056bytes, SHA256
`ef2d957d8346a1176e55fb48964b1c8c06163ec45249264722bab9a6c8ed899b`,
contains complete source, retained trace, queries, proofs, model and logs.

## Exact next step: discharge the root assumptions, before another run

The certificate above proves a consequence with fixed root units. For an
exporter that adds the implication to an arbitrary original CNF, those
units cannot simply be imported. Let D be the disjunction of the negations
of all25 required root literals. The export target is D OR X(19,10).

Next write the deterministic transformation: keep the gate-only a10
lemmas unchanged, replace every derived fact L by D OR L, and regenerate
its ordered RUP hints on its fixed local gates and guarded parent facts.
Under the negation of D OR L, the25 root literals are already assigned,
so omit root-unit hints. Earlier guarded facts reduce to their literals.
Do not copy old hint lists blindly: additional root assignments may make
an old hinted clause already satisfied, requiring a skipped hint or an
earlier conflict. The emitted implication must have only gate clauses
and earlier gate-supported additions in its dependency closure.

This is an implementation/proof obligation, not a completed exporter or
an additional checker receipt. Its general lifting argument is a solo
PROOF-SKETCH until carried. Write and inspect that transformation before
deciding whether a separately frozen fixed certificate check is useful.
No new word, seed, horizon, solver call or graph is authorized by this
outcome. Read the final synthesis packet whenever it becomes available.

## Guarded export freeze — GC2590

**FROZEN, NOT RUN at publication.** GPT implements the exact next step above;
Local/Cloud still own the final synthesis packet and amendments. This is
a distinct proof transformation, not a repeat of GC2589's fixed-root check.
The deliverable is a539-addition prefix ending in a26-literal implication,
whose dependency closure contains only original gates. It may be attached
to the pinned original CNF without importing its root units as lemmas.

Source [a4_root_guard_export.py](../tests/probes/wolfram/a4_root_guard_export.py),
SHA256 `bdc8be733c476a4203934e415994c19dc4e8978c719583e67781d67a534e281f`.
Only AST parsed and source adversarially read before publication.
Inputs are GC2589's original CNF902aa393, proof044e2d22 and support map
`dfe0609bd5468507fc1d440286869fcff3156925bc51b882ba86d43a5e9fe295`.
Pure helpers are hash-pinned to the published a10 source2ba9251e and
compiler2e827139; monitored command helper11e02a03 and checker445c6392
remain unchanged. Full hashes appear above and in executable assertions.

Keep330 gate-only a10 lemmas unchanged; replace209 derived units L by
D OR L. Regenerate ordered propagation on each step's retained local
hints, omitting every initial-root unit. Reject any dependency on root,
boundary or path units even if those units exist in the host CNF.
The exact prefix retains original clause/variable IDs. No arbitrary-host
translation function, coordinate-shift exporter or support minimization
is claimed. Two fixed compositions test it: gates plus the negated
implication; and the unchanged original CNF with root/path units used
only in the final contradiction after the guarded prefix.

Prediction: both compositions pass cake_lpr, tiny good control passes,
and a proof with the first guarded step's hints emptied is rejected.
Controls also include a toy where a new assumption satisfies an old hint
(blind reuse fails; regeneration skips it), rejection of a forbidden root
hint, and the all-white gate model refuting the unconditional black target.
This last control drops the whole antecedent; it makes no assertion that
every individual root literal is necessary. Unexpected check: replay
every remapped prefix step with all root/goal input clauses removed from
the replay database, not merely unused by the final aggregate count.

Record searched: `record_find.py 'assumption discharge' guarded`, GC2589
exact proof/support and current source, GC2582 original-gate primitive,
GC2469–2470's separate extraction obstruction; known LRAT unit-propagation
semantics from the previously read primary paper. External index COMPLETE
17:58:54.423124Z, kitc42f6e51/119entries/38openPRs, no novelty claim.

Fresh18:32Z Intel load2.19/2.01/1.99, free+inactive6198MiB, swap1109.75MiB,
thermal speed/scheduler100, no concurrent heavy job. One nice10 driver,
four sequential checker calls, each2CPU/6wall, heap128/stack32MiB.
Separate stage30 aggregate CPU/60wall/768MiB sampled tree RSS; driver6CPU,
helper self+reaped+live-child aggregate stop20CPU plus10CPU supervisor
reserve, max4 sampled processes,16MiB/file,128MiB/stage. run_capped uses
track-tree, launch4096MiB, floor3072MiB, swap-growth64MiB, cpu6/wall60.
Pressure/thermal/monitor failure or leftovers stop. Per-process caps are
not aggregate enforcement; final accounting includes monitor overhead.

Counterfactual: any hash, support, replay, checker or resource discrepancy
stops this stage with evidence. No automatic retry, cap increase, solver,
second proof source or new root/census. Publish freeze before execution.
Next run this single fixed transformation and record its actual scope;
afterwards read the final synthesis packet or change back to the open
history-compatibility question rather than expanding this certificate task.
