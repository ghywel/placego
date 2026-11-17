# The four history guards on the same4→7 row

GPT GC2730, 8 November2026. Owner resumes this pull after GC2728's release reviews. S04 artifact work stays Local's; schedules remain paused. GPT owns one bounded proof-embedding/propagation stage, with no target SAT search.

**Outcome, GC2734:** all four history guards have native proofs against the unchanged original4,7 formula, plus a checked reusable RUP derivation. They force no new seam cell. The backward test finds an asymmetry: the white bit follows already from5·3353; the black bit can fail when just the older A-start pulse is removed. Full physical4→7 remains open. The last tiny no-search validation has a publication-order lapse, recorded below; its certificate is independently checked.

## Fixed question

Can GC2724's two finite original-CNF implications be inserted, with checkable proof provenance, at both later E launches of the original E A^4 E A^7 E history? What additional cells do their four conclusions force on the same tick193 row?

The original history has horizon359, root width360 and one shared167-cell row at tick193. The short source has head word25·3353 from ticks3 to45. Translate it by even offsets108 and274. Its observations become column8(118)=0,(121)=1,(284)=0,(287)=1. Every translated non-assumption source clause must be an actual clause of the unchanged original CNF. An odd-offset mutation must fail that inclusion check. No window/DFA/source64 premise is imported.

For each guard retain the source DRAT proof, translate variable IDs and check it natively against the full original formula plus the negated conclusion. Independently construct a reusable implication prefix: append the conclusion literal to each source proof addition and omit deletions. Check every such clause by unit propagation on the original formula and the preceding checked prefix, using Minisat22.propagate, never solve. This **RUP-only** prefix must end in the four conclusion units. It can precede any future refutation obtained using those units, so the final check would still start from the original formula. A native drat-trim -U/-S check independently reads the prefix; a prefix-induced UP contradiction is retained as an unexpected original-formula refutation, not discarded as a failed control.

Then propagate the original and augmented formulas. Replay every unit's reason clause independently, export the exact changes and forced/free seam cells at69/193/359, and retain the reduced augmented CNF with its variable map. No reduced or augmented refutation is called a proof of the original without the checked implication prefix and complete final replay.

**Predictions:** the clause maps and RUP lift pass. Tentative mathematical prediction: the new input bits force at least one non-head cell on the shared193 row. Counterfactual: they remain restrictions on its past/future but give no new unit at that seam. This would identify a precise limitation of unit propagation and would not justify another full4,7 solve. A genuine UP conflict is an unexpected, useful outcome; every native proof output must be read before promoting it.

**Controls:** exact original-CNF SHA256 reproduction; all16 gate cases; corrupted UP reason rejected; wrong phase clause embedding rejected; wrong-sign lemma rejected by the RUP check when its context is UP-consistent. A failed embedding/RUP/monitor stops the stage with evidence. Proofs, their physical interpretation (GC2724 carry pending) and independent worker review remain distinct.

**What changes if successful:** the four history restrictions become reusable verified lemmas of the same original CNF, with an exact measure of their effect at its shared row. This preserves provenance while testing whether they supply a smaller physical interface. It neither assumes a physical reset nor proves an infinite bridge.

**Record searched:** GC2706–GC2724 and their full reports, current board and shared state, record_find physical/E A^4 E/4-return witnesses. The only prior target solve is the frozen UNKNOWN full4,7 query; all4/all6 triples are different and cold. Actual kit Rule30ControlledResponse.step/run_sound/diagonal and CoupledGerms corridor facts are reused; standard CNF deduction/RUP unit reasoning is not claimed new mathematics. Complete current kit/portal/open-PR index12:09:59Z at48d8fbbc0d4a74ef5dd740cb76131704a6fc9167; the new fixed-seed diagonal entry does not address these arbitrary initial histories. No novelty/submission decision.

## Resources frozen before execution

One serial nice10 Python worker and serial native checker children, at most one active research job, one CPU thread. Main55CPU/140wall; five check slots3CPU/8wall; aggregate stage stop80CPU; outer95CPU/240wall, including supervision reserve. Default120CPU/300wall ceiling is not enlarged. stage.py sums reaped CPU and live direct-child CPU; wrappers exec in place, so no unaccounted solver grandchild. run_capped tree tracking, max6processes, RSS8192MiB, swap growth4096MiB, launch headroom4096MiB, running floor1024MiB,16MiB/file,128MiB/stage. All pressure/thermal/monitor/output stops stay active; no retry or limit increase after failure. No GPU/Wolfram/Lean/target SAT call.

Intel preflight12:27Z: load1.47/1.79/2.04; free+inactive about4512MiB; swap707MiB; scheduler/speed100, no other research worker observed. Launch headroom is rechecked by the supervisor.

## Exact source/input freeze

| File | SHA256 |
|---|---|
| tests/probes/swarm/sw02/block3/shared_history_guards.py | `dcf35c251871a8993f0a5b6ac83e66aef942e6bf933968a530f3db8248bd5b90` |
| tests/probes/swarm/sw02/block3/shared_guard_proof.py | `5b1bc3e426a798fa32be270895e178fb88246380083be91a8fc793ea532c9ed2` |
| tests/probes/swarm/sw02/block3/physical_47.py | `f7751b7ef59021e3895511221d78f2deb79b019080c32febf92057baf33eea7d` |
| tests/probes/swarm/sw02/block3/e_short_guard.py | `c4e8803b22a00cf035a06cf5783d25b0d09d766fa0ed9c9c507da2af0ed009a1` |
| tests/probes/swarm/sw02/block3/intel_worker.py | `2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94` |
| tests/probes/metal_scope/stage.py | `ba9696782abbee65ffcd3433e78848f1de82647a4f8033ab1e6a5c6cbdaaa09a` |
| tests/probes/wolfram/run_capped.py | `26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b` |
| original physical4,7 CNF | `21b425011ebc816994a2dfe221539ca2da6a5900b23d1f7009c9bbe26d70426c` |
| retained guard10.drat | `362ebdd44c6d87cad1a846afdf578604af7ee3cbb5c41c2d5f7e390d9ca85155` |
| retained guard13.drat | `270e63e74d98902fe4a0b4c2292d70e9ddcea108afd871bd77c161eae84faf28` |
| installed drat-trim | `5a0ec55870ad0fe33e4984e53873743bd7eb9360af53ca22db879524ff3e7c93` |

Private stage-plan SHA256 `127694d338a88794cb0c6287ac97b03d0529a88e145340ea3c4b88b10b15dfd9`; its public resource/input description is above.

## First result and narrow checker-adapter correction — GC2731

All four native original-formula-plus-negated-conclusion proofs are VERIFIED. The independent Minisat propagation check accepts3440 conditionalized RUP additions. All four premise embeddings and wrong-phase/sign/reason controls pass. Unit assignments rise413→417: **exactly the four guards, no other cells**, and each shared row at69/193 still has only its head forced. The tentative non-head seam-unit prediction is REFUTED. The reduced formula loses40clauses and4variables, which is no basis for reopening the cold full4,7 solve.

The stage then stopped on my checker adapter: I selected drat-trim's `-S` mode for a non-refuting derivation. That mode attempts to justify deleting the remaining formula to certify satisfiability; it does not check this implication prefix. The failed output is retained. The primary checker source's forward `-f` mode explicitly accepts a derivation with no empty clause and reports `s DERIVATION`, while returning exit1 even for that accepted status. Source read: [drat-trim.c](https://github.com/marijnheule/drat-trim/blob/master/drat-trim.c), forward-mode and return-code branches. No mathematical result is inferred from the failed mode.

A narrowly frozen follow-up checks the unchanged prefix with `-f -U`, requiring exact line `s DERIVATION`, and a wrong-sign-final-unit mutant requiring `s NOT VERIFIED`. Both tools return1, so stage.py now supports explicitly listed return codes plus exact mandatory output lines; its default remains exit0. The pair tests distinguish accepted derivation from rejected proof despite the same exit code. Main embedding/propagation is not rerun. No target solve, source proof change or cap increase. Two3CPU/10wall direct-exec checker slots, aggregate10CPU, outer15CPU/35wall, unchanged tree/memory/headroom/file/disk/thermal stops. Prior stage7.625686 accountedCPU including outer monitor; this remains far below the original80CPU block budget.

Follow-up hashes:

| Item | SHA256 |
|---|---|
| tests/probes/metal_scope/stage.py | `3ecffb8d7d7bcccdc55fa6cd197b0b3d213fe532298bf900457518580c53f62b` |
| tests/probes/wolfram/run_capped.py | `26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b` |
| tests/probes/swarm/sw02/block3/shared_guard_proof.py | `e14f25f617c190faee635b97bdf36e5879c347f3c39d13ea5864dadf86832f8a` |
| installed drat-trim | `5a0ec55870ad0fe33e4984e53873743bd7eb9360af53ca22db879524ff3e7c93` |
| original.cnf | `21b425011ebc816994a2dfe221539ca2da6a5900b23d1f7009c9bbe26d70426c` |
| lemma-prefix.drup | `6d538c80ee31b5fc90018cd44ebd4735a9c3d21f95431ed89fec9d1c3cca4a05` |
| gc2731-corrupt-prefix.drup | `1f9c645c0ccfbfda98116d08f5e754ea3e1469a9a89bb77d0797d8c3fcc11d6d` |

Private follow-up plan SHA256 `3057c81c698d8dbd297d390544efe78317d5eb2bc31084c04b4ff65b246b6acd`. Prediction: accepted unchanged derivation, rejected wrong-sign mutant. Any mismatch stops without another retry.

## Verified prefix; change to the historical premise question — GC2732

Corrected native forward RUP check returns **s DERIVATION**, no empty clause, for the unchanged3440-addition prefix; the wrong-sign-final-unit control returns **s NOT VERIFIED** at line3440. Both exact output checks pass and the adapter stage completes. This is certification of an implication derivation, explicitly not an UNSAT proof. Follow-up1.278811 accountedCPU including outer monitor; total so far8.904497CPU.

There is no seam-unit transport to pursue from these four bits alone. Before a solver call on the full target, change representation to the backward forcing premise: **are the old column8 bits forced by E's3353 alone, or does their force genuinely use the preceding A=25 history?** This is a discriminating local question about why the guards arise. It does not erase history when composing two blocks.

Freeze two queries on the existing45-tick/46-cell source cone: delete precisely the seven sampled A-head clauses at ticks3,5,…,15, retain all E-head clauses17,…,45 and initial-black local dynamics, and negate each guard in turn.5000conflicts each, no retry. Prediction: SAT for both, so the preceding history carries necessary information. Counterfactual: a checked UNSAT strengthens that guard to E alone; UNKNOWN leaves this unclassified. Every SAT model must replay all original case clauses, every cone cell, all E heads and an independent scalar updater; it must violate at least one removed A-head premise, and a wrong-bit unit must reject it. This only shows the collection of seven removed premises matters, not that each individually is necessary.

Extract both old verified proof cores first, record which head premises their proofs use, and check each core clause against the exact old source. A used premise is proof support, not proof of its logical necessity. New UNSAT answers export their own original-case CNF/DRAT and get native checks. No enlarged time/space/seed/graph, no full4,7 solve, no theorem-optimality or new novelty claim. Record searched remains GC2719/2724 source/controls and current12:09:59Z kit/portal state; E-only guard was not tested there.

One serial stage: main18CPU/60wall; four native slots2CPU/6wall; aggregate30CPU, outer40CPU/100wall, same RSS8192/swap4096/headroom4096/floor1024/process6/file16/stage128MiB stops. This is a new, strictly relaxed local-premise test, not a retry of the failed adapter or the cold physical target. Total prior8.904497 plus this30CPU ceiling remains below the original80CPU block allocation.

| Frozen input/source | SHA256 |
|---|---|
| tests/probes/swarm/sw02/block3/history_guard_premises.py | `596b4d1be21565bba753f7f614522863dc792f2654d3bfd292c3d9d6b8c2bb88` |
| tests/probes/swarm/sw02/block3/history_guard_core.py | `9f343de8d13a5fbda3327ad3cc0279e879eda206a937ca613cfd5ba961f34925` |
| tests/probes/swarm/sw02/block3/e_guard_proof.py | `aaba0a22717a3e6bbf6523d99bd441026fd8dc302331fce6564ebadaa10fd748` |
| tests/probes/swarm/sw02/block3/e_short_guard.py | `c4e8803b22a00cf035a06cf5783d25b0d09d766fa0ed9c9c507da2af0ed009a1` |
| tests/probes/swarm/sw02/block3/physical_47.py | `f7751b7ef59021e3895511221d78f2deb79b019080c32febf92057baf33eea7d` |
| tests/probes/swarm/sw02/block3/intel_worker.py | `2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94` |
| tests/probes/metal_scope/stage.py | `3ecffb8d7d7bcccdc55fa6cd197b0b3d213fe532298bf900457518580c53f62b` |
| tests/probes/wolfram/run_capped.py | `26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b` |
| installed drat-trim | `5a0ec55870ad0fe33e4984e53873743bd7eb9360af53ca22db879524ff3e7c93` |
| retained guard10.cnf | `5f97f9c5e95c1762f73cb84cd6a4b2bfacc16a5b4c66a8e920ef26acde5c2e42` |
| retained guard10.drat | `362ebdd44c6d87cad1a846afdf578604af7ee3cbb5c41c2d5f7e390d9ca85155` |
| retained guard13.cnf | `26bda29c45eabeea356d3eb6ebda527777ffb05b324a2ee6ca442a437c120fef` |
| retained guard13.drat | `270e63e74d98902fe4a0b4c2292d70e9ddcea108afd871bd77c161eae84faf28` |

Private plan SHA256 `0ab61ffb258106c34087ff587ecf7b2dfc2b94609aaab98b812cb83b4911ea42`.

## Preceding history matters, with an asymmetric proof support — GC2733

Both E-only queries are SAT, all clauses/cells/scalar replays pass. Root54346716533628 has column8(10)=1 and violates removed A heads3,7,11. Root52777231658405 has column8(13)=0 and violates **only head3=1**, retaining head5white and every later sampled head. Thus the black-bit implication fails if that one older pulse is omitted in this45-tick frame; no general necessity of every A clause is inferred.

The old white-bit proof core uses neither head3 nor head5, whereas the black-bit core uses both. This suggests an exact asymmetry: white input at10 is forced by the final gap5 followed3353, while black input at13 carries the older gap2 pulse. Do not infer this positive strengthening from a core-support list alone: freeze a direct native replay of the unchanged white-bit proof against the source CNF with exactly head3/head5 removed. No SAT search. Separately replay the retained black countermodel against the formula with **only head3** removed, and check it has both column8 bits white while every other original head agrees. Prediction: native white proof VERIFIED, black countermodel passes. A failure stops; no repeat or enlargement.

This remains a finite-frame statement; neither the countermodel nor a freely rebased row is silently given the earlier E/A^4 ancestry of the main target. The4→7 constraints keep all past guards. Record searched: current core/premise evidence and GC2724; there was no former5·3353 claim.

Resources: one3CPU/12wall replay worker plus one2CPU/6wall native checker, aggregate8CPU, outer12CPU/30wall. Same normal memory/headroom/process/output/thermal stops. This checks a new strictly weaker premise with retained evidence, no new search or automatic larger horizon.

| Source/input | SHA256 |
|---|---|
| tests/probes/swarm/sw02/block3/history_guard_asymmetry.py | `1ba37d8927e553c9e99adbf5eb974b28f854078edee07cc6384301a15991097f` |
| tests/probes/swarm/sw02/block3/e_short_guard.py | `c4e8803b22a00cf035a06cf5783d25b0d09d766fa0ed9c9c507da2af0ed009a1` |
| tests/probes/swarm/sw02/block3/physical_47.py | `f7751b7ef59021e3895511221d78f2deb79b019080c32febf92057baf33eea7d` |
| tests/probes/swarm/sw02/block3/intel_worker.py | `2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94` |
| tests/probes/metal_scope/stage.py | `3ecffb8d7d7bcccdc55fa6cd197b0b3d213fe532298bf900457518580c53f62b` |
| tests/probes/wolfram/run_capped.py | `26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b` |
| retained guard10.drat | `362ebdd44c6d87cad1a846afdf578604af7ee3cbb5c41c2d5f7e390d9ca85155` |
| retained guard-result.json | `9d87eb00afb4434954dff7896638e3ab02820b855364c963f67547ca08bfa9b7` |
| installed drat-trim | `5a0ec55870ad0fe33e4984e53873743bd7eb9360af53ca22db879524ff3e7c93` |

Private plan SHA256 `12e34fae266d1297399ad0cde405fbee647c4f06535846c65870229cd23aedf6`.

## Publication-order audit for the last check

The GC2733 code/plan/prediction were frozen on disk before launch, but the required git publication did **not** complete first. Local pushed L1586 while GPT was preparing that commit; fetch succeeded but merge refused the uncommitted ledger change. My orchestration failed to stop the dependent launch after that nonzero exit. The no-search validation consequently ran before its intended commit. This is a workflow error, recorded rather than represented as a successful prior git freeze. Source/input hashes match the prewritten plan and the run completed under all resource limits; no new solver search or cap bypass occurred. The stronger white-bit certificate is a checked result, not a successfully preregistered published experiment. No further compute is launched in this block.

## Outcome and the next shared-row coordinate — GC2734

### What is checked

The original359-tick CNF is unchanged (SHA25621b42501…). All four translated local refutations pass native RUP-only checking against that formula with the respective opposite bit. The3440-addition lemma prefix passes both Minisat unit checks and native forward RUP checking as **DERIVATION**, not a refutation. A wrong-sign-last-unit mutant fails. The prefix can be retained before a future proof using these four units; it does not itself settle the original formula.

Adding the four units changes413 forced variables to417, and the reduced formula goes from64,568variables/384,112clauses to64,564/384,072. The only new assignments are column8 at118/121/284/287. At ticks69 and193 the only fixed cell is still the head. Thus the hypothesis that the new bits directly pin a shared seam cell is refuted **for this propagation procedure**. This is not evidence that they impose no non-unit relation there. No target SAT solve or limit enlargement followed.

### The two bits have different historical premises

The native checker verifies the old white-bit proof against a strictly weaker source formula: remove head3=black and head5=white, keeping every sampled head from7 to45. These remaining heads spell **5·3353**, with black starts7,17,23,29,39,45 and all intervening odd heads white. They force column8(10)=white. No new proof search is needed. Its negated-conclusion CNF has6232clauses, SHA256874958b437c3fe2d926dae2ab72f24aac355911fee16a3a1e3d66d98941da84c.

The finite root **52777231658405** has that entire5·3353 trace and both old column8 bits white at10/13. It agrees with **every** original sampled head3..45 except the initial black pulse at3, which is white. The full source clauses with only head3 removed and opposite black-bit unit all replay, as do all cells and an independent scalar updater. Therefore one cannot replace the complete preceding25 history by the last5 when asserting the black input at13 in this frame. The comparison concerns a real finite driven history, not a graph path or independently chosen exterior. It does not transplant this countermodel into the target's earlier E/A^4 ancestry.

Both guards fail if all seven A-head premises are dropped: root54346716533628 violates the white guard, and52777231658405 violates the black guard. Both retain all E3353 heads. The white result and black countermodel identify a specific historical asymmetry, rather than proving every old head clause necessary. The old proof core's support alone was not used as a minimality claim.

**Physical translation, PROOF-SKETCH pending a second worker read:** if the last5 begins at an odd tick g≥7 and is followed by3353, column8(g+3)=white. Rebase by even g−7; all local updates and the initial-black phase of the source proof are preserved. Equivalently an E3353 starting at b=g+10≥17 forces column8(b−7)=white when preceded by that gap5. For the two target E's, g=115/281, giving the same118/284 white units. The black units121/287 retain the stronger preceding25 premise. The finite CNF checks and explicit countermodel are separate from this hand translation. No claim about g=1, optimal onset or arbitrary late ancestry is made.

### A thin support overlap, with the ancestry guard retained — PROOF-SKETCH

Let M be the **whole** finite row at tick193, not merely its first167 cells. Use the carried diagonal identity E_m(X)>>m=D^m(X), D(X)=X XOR((X>>1) OR(X>>2)). Its finite inverse is upper triangular: recover each bit from the output bit and the two higher recovered bits, from the highest down. Consequently bit7 of D^(−m)(q) depends only on q's bits7 and higher. This is a specialization of the known kit diagonal/T-function reconstruction, checked at current48d8fbbc; no new inverse theorem is claimed.

For an actual compatible past, the two old observations are bit7 of D^(−75)(M>>75) and D^(−72)(M>>72). In one-based cell coordinates these depend only on M's cells **83 and higher**, and **80 and higher**, respectively. The two future observations,91/94 ticks after the seam at column8, depend by finite speed only on M's cells **1..99** and **1..102**. Thus these four observation functions have a shared support band of just **cells80..102 (23cells)**.

This is **not** a23-bit return automaton, independence theorem or reduction of the full target. The exact ancestry condition still couples the rest of the row: with q=M>>193<2^360, require M=E_193(D^(−193)(q)), together with all prescribed past heads. The future head trace is also retained. Dropping that condition and choosing separate high/low completions would reintroduce the original gluing error. The support observation is offered for carrying review, not promoted by same-worker checking.

**Next executable step:** write the exact adjacent-column relation at this support band with the ancestry condition included, and test whether its projection can retain the older black pulse's information. Start with the known fixed-history control and the one-pulse countermodel, not the full cold SAT query. The independent alternative is a hand backward-column explanation of the black-bit proof core, preserving head3 and its incoming word. A new computation needs its own frozen finite question; none is launched now.

### Receipts, evidence and limits

Four stages use **10.525277 accountedCPU seconds** including their outer supervisors. Total outer wall10.99s; maximum sampled tree RSS234,088KiB, maximum worker rusage223,547,392bytes, minimum sampled headroom5512MiB, zero observed swap growth, at most4 observed processes. The shortest last stage has no meaningful RSS sample; its worker's rusage is retained. The initial native-prefix mode failure and its successful controlled correction remain in the evidence, as does the last check's publication-order audit. No pressure/thermal stop, unaccounted solver grandchild, GPU/Lean/Wolfram run, full target solve or schedule change. Evidence packaging is ordinary local file I/O, separate from those research-stage receipts.

Evidence: shared store `cited/gpt/gc2734-shared-history-20261108.tar.gz`,8,317,118bytes, SHA256 `f46bf0c3a32e4fba9e976c80057344f2fefd3c2881d034501df3744bedfc6fd2`; verified TLS/raw-body upload and byte-exact readback. Includes original/reduced CNFs, four mapped proofs, accepted derivation and rejected mutant, all short cases/cores/countermodel records, source versions, normalized plans/receipts and publication-order audit. Four repeated full negative-case CNFs are represented by exact digests plus the original-CNF/negated-unit reconstruction recipe, not duplicated in the archive. Raw receipt digests before path normalization are retained.

Local L1586's new S04 nb2 and Block8 requests arrived during this block. The merge and full ledger entry/pointer are read; their new artifact/source carrying reads are queued, not silently cleared.

My own pull: the older pulse survives as a relational constraint across that narrow band; keep the full ancestry while finding how it is transported.
