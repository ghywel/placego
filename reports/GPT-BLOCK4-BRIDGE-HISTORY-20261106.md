# Block4 carrying read and surviving bridge histories

GPT GC2697, 6 November 2026. **Block4 passes the requested source/mathematics review.** Local's kit and portal proofs have identical bodies, and their statements are the kit's own Q01, Mortality and all-length BudgetAt. No proof change is requested. One abstract sentence now states logical equivalence without an unsupported practical-difficulty comparison. The GC2697 freeze below is retained as written before execution. GC2698 completes that pilot with two language corrections and two UNKNOWN SAT results; see the outcome below.

## Block4 verdict

The complete 254-line kit form and 249-line portal form were read, including the far-boundary extension Z_rec. Inside the frontier it uses the kit's Z_depth. At the first exterior depth the zero-memory scan's first output is (a OR b,b), which cancels both components of the recurrence; farther out all terms are white. Thus chart_interior covers every positive depth, including the moving far boundary.

The two parity cases of chart_wall use the terminal pair (1, NOT s) and penultimate (s,s). The wall is proved for tau>=1. The horizontal start is taken at tau=2, and zrow_chart shifts by two; there is no illicit use at tau=0. inX_start reads a terminal high bit after a successful update. fr_length and atDepth's white default imply finite support, with the safe bound2*length(fr0)+6. This bound is not the stronger quantitative mortality claim left out of the packet. Legal is used only to rule out an empty initial frontier.

The converse composes the existing mortality namespace equivalence, Q01_of_mortality and Q01_iff_staged. budget_iff_Q01 quantifies over every frontier length, with a budget allowed to depend on that length. It does not prove one uniform budget, Q01 itself, or a prize statement. The abstract's final sentence is repaired accordingly; proof files are unchanged.

**Evidence distinctions:** GPT carries the source and mathematics and compares the two proof bodies byte for byte. Local's actual Check JSON is read: verdict pass,58 replayed constants,9 headlines, importsStatements true, no new axioms/reasons, standard axioms only, verifier kit5fb591588cfa869bfdc47946799b5ddd70a903d1. This is Local's M5 compilation/replay receipt, not an independent Intel build or public Lean Verified/Human Verified status. Essay/notebook, exact-source release receipts and outward posting remain later work, on the owner's instruction.

| Cleared file | SHA256 |
|---|---|
| Rule30FrontierChart.lean | 4c90192e4166d7a381a80cec264a3b94959ca19e8d1c9af606c14a309b4949c1 |
| Rule30Submission.lean | 9a5e9e81cb1fc276c116951773f9f8b4572f80f77f9f4f6f3276970cd27566a4 |
| Local Check JSON | b8a19b13d9849464c04cc59f32b76b47ad59044d943d76659f7a0ccc65b45683 |
| Revised abstract | 14785a5445d51ddee4dbea93ae6d241769869c0553ea4042ceaf49a8ad7b526b |

The complete source index refreshed at19:01:36Z: kit9d837cd5e5ac447cd868c20aebf49a1b4cfa866e, portal19:01:22Z,30 open PRs,33 additions since the previous complete check. The mortality search has no indexed converse. Closed PR75 at f131449bf08949cbf0d815b678f6d6dc431524ad,76 at fa511089735aa73643560165f1cc2dceffa2420c,85 at571f545554c7f533066cde5a2c50cc98c4210fbc were separately read through current metadata, issue comments, review bodies and inline comments; they leave this converse unknown. Current landed SurvivalBridge, AlternatingTraceBridge and ZeroBoundary definitions and carrying statements were read. The three carrying kit modules at verifier pin 5fb59158 are byte-identical to their current-main versions, checked directly by git object reads. This is not a blanket carrying read of the 33 additions.

## Bridge question and frozen test

L1569 already supplies genuine finite bridge crossings, so the question is now repeated crossings and their history compatibility. Its archive is raw-body/digest verified: cited/local/block3-bridges-20261106.tar.gz,1,410,257 bytes, SHA256 ba78c5fa0d097eb77b607d0abbcd87f316855b18eafa7c201a1037d0086b6147. No new window lift or census is proposed.

First compare the supplied X automata at widths38,39,40,41 by exact finite-product BFS. Compare them with the factor language of A=25 and E=33535555 with4 or>=6 A blocks between E's. This tests equality, not just block-list inclusion or agreement through16 gaps. Compute exact unary transition orbits for E A^n E and Y's excursion separations, replacing the n<=400 cutoff. The conclusions concern the supplied finite DFAs; they retain Local's hash-collision/original-graph-completeness caveat. A DFA comparison is not a fresh replay of the original C subset construction.

Then solve exactly two fixed actual-history SAT queries: gaps A^2(A^n E)^3 A^2, n=4 and6. Physical observation ticks are1+2s; the alternating center is black at even ticks. All initial cells in the triangular backward light cone are free, and every subsequent cone cell obeys the actual Rule30 rule. A model specifies one finite right-half integer, with zeros beyond that cone. Check it by separate scalar-cell and bit-integer simulation. No finite right half, horizon or number of crossings is increased after seeing a result. Positive results are finite witnesses only. UNSAT without a checked certificate remains an uncertified solver outcome, never a forbidden-word theorem.

**Predictions written before execution:** (P1) the X automata at38..41 have equal all-length languages; (P2) their language equals the claimed simple grammar; a shortest separating word would refute this prediction; (P3) at least one fixed three-excursion pattern has a genuine finite-history witness. Counterfactuals: an automaton mismatch, a grammar separating word, or both SAT queries unknown/uncertified UNSAT. Any of those is retained without a wider retry. Controls: equivalent/inequivalent DFA toys; fixed initial R=19 whose literal trace must be SAT; a wrong first tick under the same fixed root must be UNSAT; every new SAT witness must pass both simulators and reject a deliberately wrong output bit.

**Source freeze:** bridge_history.py SHA256 fcbdda049d78dc1b053ba41ec802c7ee2ce9c948203e9cb4068b066b47f52cdc; generated serial plan SHA256 bfb3382cecd0c724a2bc22fe2b6b0fdca34095f76b28f5b40f17b8f5af382dd2. All five DFA inputs, wrapper, stage driver and cap supervisor are digest-bound in the plan. Intel pilot ceiling120 aggregate CPU seconds/300 wall; worker stop105 including stage accounting, individual one-process math worker100CPU/240wall, reserved15 for outer supervision; one mathematical process, one thread, nice10. Tree RSS8192MiB;4096MiB launch headroom,1024MiB running floor,4096MiB swap-growth stop;16MiB/file,128MiB artifacts, at most6 processes including wrappers/monitors. run_capped plus the existing CPU-only stage orchestrator provides tree/pressure/thermal/artifact limits and aggregate reaped/live worker accounting. No GPU, no dependent retry after control/pressure/thermal/monitor failure. Each SAT query also has a fixed60,000-conflict stop. Solver unknown is distinguished from a failed control.

**Record searched:** L1568–L1571 and complete current packets; GC2688 Appendix A/GC2690/GC2692/GC2696; record_find33535555 and column word; kit actual source/index, portal sources and open PRs, plus the closed discussions above. Relevant earlier prior art is the existing column-word tree and realization guards, not a new assertion that arbitrary finite target words are always realizable. The exact source-index refresh log SHA256 is04f7f3b75e0d89fb0ee065964fcec50bc7d969fd960722ac7e74599669f7e34a. Preparation observed load3.68/3.10/2.77 and about5.05GiB free+inactive; fresh unsandboxed monitor gates are required at launch.

My own pull: determine whether the bridge grammar permits a genuine repeated history, and locate the first compatibility obstruction if it does not; do not infer infinite finite-support survival from any finite witness.

## GC2698 outcome: excursion history matters

**COMPUTED on the supplied DFA files:** P1 and P2 are refuted as stated. Exact comparison finds that X at width38 has a larger language than at39. Widths39,40,41 have equal languages at every finite length. The block list and single-separation set are necessary conditions, not a complete renewal grammar.

Put A=25 and E=33535555. Two explicit counterwords are:

| Gap word | Length | W38 | W39–41 | Meaning |
|---|---:|---|---|---|
| 55 A^4 E A^4 3 |27 gaps| absent | absent | E A^4 E A^4 E is forbidden |
| 55 A^4 E A^6 3 |31 gaps| present | absent | E A^4 E A^6 E is forbidden from39 |

The literal words are `552525252533535555252525253` and `5525252525335355552525252525253`. Each is a factor of the corresponding displayed three-E concatenation (55 is the preceding E's suffix,3 the following E's prefix). Both are admitted by the proposed simple block grammar. Independently reading the input transition tables reproduces each accepting/rejecting state trace, without using the grammar builder or product search. Those traces and input digests are in the evidence packet. A post-hoc directional product audit also checks X39 is contained in X38 and every tested X language is contained in the simple grammar; together with the counterword this establishes strict inclusion, rather than only inequality. This audit of the same fixed inputs used 0.004431 CPU seconds.

This shows precisely where pairwise separation information loses history. For each individual E A^n E, the exact unary orbit gives n=4 or n>=6, with no upper cutoff. Nevertheless, a separation4 cannot be followed by4, or, from width39, by6. The periodic gap stream (A^4 E)^infinity fails after its second complete copy in these automata, whereas every finite prefix of (A^6 E)^infinity is accepted. This is a statement about the supplied finite automata, not a constructed infinite right half.

For Y at width60, exact unary orbits confirm the reported four separation sets for all n, replacing the earlier check through400. The pure2 orbit accepts lengths0..21 and no larger length. These results do not establish that pairwise Y separations chain independently.

**Conditional hand corollary, PROOF-SKETCH awaiting Local's read.** For an infinite coded X tail satisfying these DFA exclusions, let n_i be the number of A blocks between consecutive E's. Then n_i=4 or n_i>=6, and n_i=4 forces n_(i+1)>=7. An E-to-E interval lasts34+7n_i sampled steps:62 for a short interval, at least83 for its successor. Pair each short interval with its successor; pairs are disjoint. Every other interval lasts at least76. In a finite list of k intervals there can be at most one unpaired short final interval, so elapsed time is at least(145k-21)/2. Thus the asymptotic frequency of E starts is at most2/145 per sampled step, or1/145 per physical tick. This is an exact conditional clock bound, not a density fit, a realizability proof or a finite-support exclusion. The premises retain the original subset-hash/completeness caveat.

## Actual-history queries and controls

The equivalent/inequivalent DFA controls pass. The fixed-root R=19 history is SAT and replays exactly in both scalar-cell and bit-integer simulators. Reversing its required tick1 while keeping the initial row fixed is rejected. The new queries stop at their requested conflict budgets:

| Copies of A per excursion | Physical horizon | Root-width bound | Variables | Clauses | Outcome |
|---|---:|---:|---:|---:|---|
|4|429|430|92,665|736,379|UNKNOWN,60,000 conflicts|
|6|513|514|132,355|1,052,933|UNKNOWN,60,001 conflicts|

No new SAT witness was found, and no UNSAT certificate exists for either query. P3 remains unresolved. Both original-CNF digests and the fixed generator/input hashes are retained. A finite trace outside an eventual component's language could still occur transiently, so even the DFA exclusion does not discharge the corresponding finite-history SAT question. No query, width or resource bound was enlarged.

The stage completed rc0:38.686791 accounted CPU seconds, plus0.713 seconds of outer-supervisor CPU;38.29 seconds worker wall time, peak sampled tree RSS294.65MiB, minimum free+inactive headroom5,120MiB, swap growth0. No pressure, thermal or monitor stop. All control outputs, failures of predictions, unknown outcomes and direct counterword traces are preserved. The unstructured full-cone SAT route now waits for a reduced constraint or decomposition; simply adding conflicts or time is not the next step.

**Evidence:** shared-store `cited/gpt/gc2698-bridge-memory-20261106.tar.gz`, 13,505 bytes, SHA256 `eaa5ed50a11d41fffa5db27a8b632e0823ce108cf39b4b1443bfbfb69fa44011`. It contains the pilot receipts, exact DFA results, counterword traces, source/plan bindings and source-index refresh receipt, with host paths normalized and original raw digests retained. Full input DFAs are in Local's cited archive above; raw pilot/input files are also retained in durable outside-git storage. The main proof files remain unchanged at the cleared hashes.

**Next executable step:** construct the return automaton at complete E boundaries from the existing X DFA. Label transitions by exact ultimately periodic sets of possible n. This retains the state discarded by the one-separation table and can test which short/long histories reset that state. Reopen the full physical-history problem only after this supplies a smaller compatibility relation or a constructive witness route. Block4 is DONE; later packaging/posting and GPT schedules remain deferred.

## GC2699 scoped read of Local's newly arrived left-side note

L1572 arrived during closeout and is safely merged. Its complete report and three probe sources are read. The numerical observations retain their self-check status; no duplicate computation is run. The report now separates finite spreading/compression data from the unproved assertion that `Theta` has no finite-state transducer. Neither a finite disorder test nor a narrow interface settles that general question. The observed9–12-column trunk also remains an observation on the tested rows, not a uniform depth bound.

The reduction to CQ01 now retains Q01Gap and both unresolved language exclusions, valid target certificates and the periodic cases. A residual X/Y language exclusion by itself does not cover entry into the gate. Unrestricted Theta realization excludes bare trace-only contradictions, without closing every finite-support or history-compatible route. The001/011 finite-left-game negative is not automatically a period-two theorem.

Nested compact-subshift entropies converge to the entropy of the intersection. Equating that intersection with genuine right-half histories needs the separate coherent-lifting argument, and no finite table or fitted extrapolation proves a positive limit. Kit Cert.sound_bad is cited as a prior-art ancestor with its actual-seed/masked-Jen hypotheses; it is not asserted to be identical to the generic C(W) classification.

My own pull: the return state after an excursion. We now have an explicit case where the preceding short gap changes what can happen next; preserve that state instead of treating excursions as independent choices.
