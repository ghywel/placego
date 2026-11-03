# Retained 25-cell root proof as original-gate LRAT — GC2588

GPT, Intel, 3 November2026. **FROZEN, NOT RUN at publication.**
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
