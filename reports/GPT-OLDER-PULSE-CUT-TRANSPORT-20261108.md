# Older-pulse information at the shared-row cut

GPT GC2737/GC2738, 8 November 2026. Owner requests continuation of the shared4→7 pull. The [previous guard block](GPT-SHARED-47-HISTORY-GUARDS-20261108.md#outcome-and-the-next-shared-row-coordinate--gc2734) supplies the checked finite implications and one-pulse countermodel. This block changes representation, retaining the whole ancestry; it does not retry the full target solve.

## Exact cut relation — PROOF-SKETCH pending carrying read

Use the whole finite seam row M at tick m=193, with cells numbered from1. The known right-to-left reconstruction uses v_t(k)=x^t_(k+t) and

```text
v_s(k) = v_(s+1)(k) XOR (v_s(k+1) OR v_s(k+2)), s=192,...,0.
```

On input seam cell j, k=j−193. Begin with v_193(k)=M_j and descend through s. For each still-live row, two previously read values suffice. At position k+s=0, require the actual alternating boundary at time s; at position1, require the prescribed head when there is one. Discard a row only after its boundary check. Keep the conjunction of every earlier check. Leading zeros above max(width(M),194) and the original root-width bound are retained.

After consuming cells above102, the pending rows are91..192: **204 bits** of pairs, plus acceptance of the checks already read. Input cells102..80, exactly23 bits, updates this to pairs for rows114..192: **158 bits**. This is a sufficient interface, not a minimal-state claim. Its initial204-bit state must come from that very row's high tail; an arbitrary state is not a physical completion.

A row event (time t, column p) is read when **j=193−t+p**. For the first local 25·3353 frame, whose source begins at physical tick108, this gives:

| Observation/check | Physical event | Seam input cell j |
|---|---|---:|
| Older A pulse | head at111 = black | 83 |
| Following white | head at113 = white | 81 |
| Last5 begins | head at115 = black | 79 |
| Historical white input | column8 at118 = white | 83 |
| Historical black input | column8 at121 = black | 80 |
| E begins | head at125 = black | 69 |
| End of the short3353 certificate | head at153 = black | 41 |

Thus the older pulse and white input are read on the same diagonal; the black input is read three diagonals later. But the heads that make the old finite implication valid are **not all checked inside the overlap**. In particular all the 5·3353 premise heads at115..153 are read at79..41, after the two historical inputs. This is a backward acceptance constraint: an observation can be emitted before a later check determines whether the scanned row belongs to the allowed history language. It is not propagation of an already forced unit through23 independent bits.

More explicitly, write M as low cells1..79, band80..102 and high cells103+. The tail initializes a definite pair state and earlier-check flag; the band deterministically emits the old pulse and the two old inputs; the lower cells finish all pending ancestry/head checks. Those three pieces are concatenated **once** for the same M. The future two input observations depend only on cells1..99 and1..102, respectively, but the **whole** future A^7E head trace still reads cells1..167. Therefore even the future target is not a predicate of the low79 cells and band alone. Retain the high cells103..167 as well.

The exact full target remains: width(M)≤553, q=M>>193<2^360, M=E_193(D^(−193)(q)), prescribed past heads through193, and the future heads through359 of that same M. The cut relation is another organization of these checks, not a reduction to204 free bits or to23 free cells. The earlier diagonal/T-function and ancestry identities are known and already carried; this cut/event specialization is the new hand step offered for review.

## Discriminating local strip pilot — frozen before launch, GC2738

The remaining local question is whether the old black-input implication already has a short strip explanation, or genuinely needs additional generated right-boundary history. Test widths **8,10,12**, physical horizon45, initial-black drive and the unchanged head word25·3353 at ticks3..45. Each odd row retains W inner cells and its two actual outer cells; the two-tick update computes all W next inner cells. At the next odd tick, the outer pair may be chosen afresh. This is a sound relaxation of physical rows, explicitly not an independently gluable full history. The first tick is also encoded from an actual initial prefix.

Exactly eight SAT queries, each at most2000 conflicts: at each width negate the white input at10 and black input at13; at width12 also remove heads3/5 for the white test and remove only head3 for the black test. **Prediction:** width12 already excludes both full-premise opposite bits and the weaker white opposite bit; the one-pulse-deleted black test is SAT. **Counterfactual:** a SAT strip on a full-premise opposite bit shows this width/model has lost necessary exterior compatibility; it is not a counterexample to the original cone theorem. UNKNOWN remains unclassified. No further width, conflict or horizon increase follows.

Every SAT strip replays every clause and cell with a separate scalar local update. Each original physical trajectory embeds in the relaxation; the retained genuine fixture and one-pulse countermodel control that embedding. Native RUP checking is required for every returned UNSAT proof, with an already verified positive and empty-proof negative control. Do not promote an UNSAT answer before its check. Separately replay the exact diagonal event/readout formula and complete finite ancestry on the genuine local fixture and countermodel at seam85; then on the original seed2135555 at seam159, including all159 actual past ticks. This tests the event schedule without transplanting a short row into the target's earlier ancestry.

**What it teaches:** a successful narrow-strip exclusion would give a smaller concrete mechanism for the pulse/input relation. A surviving relaxed strip identifies precisely why the generated boundary still matters. Either result complements the exact cut description; neither answers repeated4→7 realization.

**Record searched:** GC2708/2709 inverse scan, GC2719 input-word compatibility, GC2724/2734 original-CNF guards and countermodels; current record/kit/portal/open-PR index at complete2026-11-08T13:45:12.507522Z, kit48d8fbbc0d4a74ef5dd740cb76131704a6fc9167. Actual `Rule30ControlledResponse.diagonal/step/run_sound`, `Rule30Predecessors.T/back/lin_back/eq_back` and equivalents `TFunction.testBit_Phi/Phi_mod/mod_of_Phi_mod` read. Standard permutive preimage reconstruction is prior art; see Kopra's [rapid left expansivity paper](https://www.utupub.fi/bitstream/handle/10024/174540/1-s2.0-S0304397522007502-main.pdf?sequence=1). No new inverse or general automata theorem is claimed; this is a fixed finite test of a new guard representation.

**Resource freeze:** one serial Intel worker, no GPU/Wolfram/Lean. Main40CPU/80wall, up to eight native2CPU/6wall check slots plus two2CPU checker controls; stage aggregate65CPU, outer80CPU/180wall. Actual reaped process CPU plus supervisor/monitor CPU is accounted; exec wrappers introduce no hidden solver child. `run_capped.py --track-tree --max-procs6 --rss-mib8192 --swap-growth-mib4096 --launch-free-mib4096 --min-free-mib1024 --file-mib16 --disk-mib128`; nice10, one CPU thread. Pressure, thermal, monitor, memory, file, disk or output failure stops and preserves evidence; no retry or cap enlargement. Private plan hash and all source/input hashes are added before launch.

## Source/input freeze

Private stage-plan SHA256 `feb548b228d2d3b71b80af98542aa4387e35d7523498793407cdc46c08771daa`.

| Source/input | SHA256 |
|---|---|
| tests/probes/swarm/sw02/block3/older_pulse_strip.py | `92822af406b6a215dcc34a17a870e1345c3dd6588fb00aadba021499afb1fbe5` |
| tests/probes/swarm/sw02/block3/strip_proof_check.py | `87dbb21e49d9610924099420a9e5f8f49c4f69ee98739bc8f7e4819e2343856a` |
| tests/probes/swarm/sw02/block3/physical_47.py | `f7751b7ef59021e3895511221d78f2deb79b019080c32febf92057baf33eea7d` |
| tests/probes/swarm/sw02/block3/physical_ancestry.py | `6d55a6bd120120c34c81f12ea6d9a453a1754a1fafaeea92ac92e867ed1fe912` |
| tests/probes/swarm/sw02/block3/e_short_guard.py | `c4e8803b22a00cf035a06cf5783d25b0d09d766fa0ed9c9c507da2af0ed009a1` |
| tests/probes/swarm/sw02/block3/intel_worker.py | `2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94` |
| tests/probes/metal_scope/stage.py | `3ecffb8d7d7bcccdc55fa6cd197b0b3d213fe532298bf900457518580c53f62b` |
| tests/probes/wolfram/run_capped.py | `26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b` |
| drat-trim | `5a0ec55870ad0fe33e4984e53873743bd7eb9360af53ca22db879524ff3e7c93` |
| guard10.cnf | `5f97f9c5e95c1762f73cb84cd6a4b2bfacc16a5b4c66a8e920ef26acde5c2e42` |
| guard10.drat | `362ebdd44c6d87cad1a846afdf578604af7ee3cbb5c41c2d5f7e390d9ca85155` |
| gc2738-empty.drat | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

## First result and one boundary-history correction — GC2739

All eight fixed strip queries are SAT, including both full-premise opposites at width12. All clauses/scalar cells and genuine-history embeddings pass. Thus the prediction of narrow-strip exclusion is REFUTED; these are relaxed histories, not physical counterexamples. Native positive/empty-proof controls pass; there are no new UNSAT certificates. Exact ancestry/readout controls at local85 and full global159 pass.

Every retained countermodel violates the same omitted necessary equation at one or more even ticks. If the outer column W+1 is black at an even tick s, its next value must be the complement of column W there, regardless of the unseen next right cell. Existentially eliminating that unseen cell gives `(not center) or (next != left)`, exactly two clauses over **already present** variables. This is known local-rule projection, not a new Rule30 law. For W12 the retained white/black countermodels violate it at8/7 even ticks. The genuine fixture satisfies it.

Freeze exactly two follow-up queries, still W12/H45/2000conflicts, adding these44 clauses, no new tracked cell or time variable. This is one explicit generated-boundary-history correction, weaker than a full wider-strip model; it must not become an automatic sequence of width lifts. Prediction: both opposite-guard queries remain SAT, demonstrating that one such local consistency condition does not capture the required boundary history. Counterfactual: native-checked UNSAT yields a smaller sufficient strip explanation. All SAT results replay clauses, scalar cells and every new corner condition; the two old models must be rejected. Any UNSAT is checked against its augmented-strip CNF; it does not replace the previously certified original cone. No claim of physical lift. After this correction, no third strip refinement in this block. Return to the exact ancestry cut if both survive.

One6CPU/15wall worker, two2CPU/6wall native slots, aggregate15CPU/outer20CPU40wall; all original memory/tree/headroom/process/file/disk/thermal stops unchanged. First stage1.532196 worker/supervisor CPU, outer monitor accounting retained separately. This is a new fixed constraint test justified by the explicit violated local equations, not a larger retry.

Private follow-up plan SHA256 `c2621ad28ad566593d3d6fa977a0b193e1f10ba0ed27dbbd4b0fae2dbf8307cd`.

| Source/input | SHA256 |
|---|---|
| tests/probes/swarm/sw02/block3/older_pulse_corner.py | `b9c66c0aebd92c5951aa67129946d22d7b5e4531713001f2cab541be5ec6cdc1` |
| tests/probes/swarm/sw02/block3/older_pulse_strip.py | `92822af406b6a215dcc34a17a870e1345c3dd6588fb00aadba021499afb1fbe5` |
| tests/probes/swarm/sw02/block3/strip_proof_check.py | `87dbb21e49d9610924099420a9e5f8f49c4f69ee98739bc8f7e4819e2343856a` |
| tests/probes/swarm/sw02/block3/physical_47.py | `f7751b7ef59021e3895511221d78f2deb79b019080c32febf92057baf33eea7d` |
| tests/probes/swarm/sw02/block3/physical_ancestry.py | `6d55a6bd120120c34c81f12ea6d9a453a1754a1fafaeea92ac92e867ed1fe912` |
| tests/probes/swarm/sw02/block3/e_short_guard.py | `c4e8803b22a00cf035a06cf5783d25b0d09d766fa0ed9c9c507da2af0ed009a1` |
| tests/probes/swarm/sw02/block3/intel_worker.py | `2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94` |
| tests/probes/metal_scope/stage.py | `3ecffb8d7d7bcccdc55fa6cd197b0b3d213fe532298bf900457518580c53f62b` |
| tests/probes/wolfram/run_capped.py | `26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b` |
| drat-trim | `5a0ec55870ad0fe33e4984e53873743bd7eb9360af53ca22db879524ff3e7c93` |
| result.json | `a2ea8bb23e57251998154ce676335672600753b9be90416caf9469d9f32a8bde` |

## Change to an explicit nonlinear memory predicate — GC2740

Both corner-corrected W12 queries remain SAT and replay every new condition. The strip-filter route is parked: do not add more strip width/corner constraints without a new structural reason. The returned models only show that this relaxation is inadequate.

There is a direct algebraic transport statement. Put z_s(j)=x^s_(j−193+s), allowing the actual center at position0. The inverse recurrence telescopes:

```text
z_a(j) XOR z_b(j) = XOR_(s=a,...,b−1) (z_s(j+1) OR z_s(j+2)).
```

At j83 let P be the parity of the seven OR terms for s111..117. At j80 let Q be the parity of the eight terms for s113..120. Then P=head111 XOR column8(118), whereas Q=center113 XOR column8(121)=column8(121), since the actual center113 is white. All register values are reconstructed from the same M; P reads the register just before83, Q the one just before80. No new independently chosen state is allowed.

Keep common temporal premise S: head113 white and the complete5·3353 heads115..153; omit only head111. The certified weaker white guard gives column8(118)=0, so **P=head111**. The old original-cone black-input implication gives **P=1 implies Q=1** under S. This is an explicit one-way constraint on two nonlinear register predicates three scan cells apart. It is a hand corollary of checked cone implications, PROOF-SKETCH pending a carrying read, not a new original-CNF certificate. The retained good and one-pulse-deleted fixtures give (P,Q)=(1,1) and(0,0).

**One remaining finite question:** is (P,Q)=(0,1) physically possible under S? This distinguishes equality (a copied bit) from one-way information. Return to the unchanged45-tick/46-cell original physical cone, change exactly head3 from black to white and require column8(13)=black. One5000-conflict query, no other constraints or window/horizon growth. Prediction equality: UNSAT; counterfactual SAT supplies the missing corner and refutes equality. UNKNOWN leaves it open. Every SAT model replays original case clauses, all cone cells, independent scalar evolution, both parity identities and full finite ancestry at local seam85. This is not a witness for the earlier E/A^4 target ancestry. Native RUP check any UNSAT; the original two controls give00/11 and wrong-old-pulse rejects the new witness. No additional query in this block.

Main5CPU12wall, one2CPU native slot, aggregate10CPU/outer15CPU30wall; normal one-worker/tree/RSS8192/swap4096/launch4096/floor1024/process6/file16/stage128/thermal stops. This changes from a refuted free-input abstraction to an exact physical missing-corner question, not a larger retry.

Private plan SHA256 `7c0569cf5d94a3da126f33571aa7af1c2954f5671a802ed9342396fc2a884a6c`.

| Source/input | SHA256 |
|---|---|
| tests/probes/swarm/sw02/block3/older_pulse_parity.py | `d477ffc475f781fae0480f4a398bf475b2052007dcd0744c19ec676e6ea4463d` |
| tests/probes/swarm/sw02/block3/strip_proof_check.py | `87dbb21e49d9610924099420a9e5f8f49c4f69ee98739bc8f7e4819e2343856a` |
| tests/probes/swarm/sw02/block3/physical_47.py | `f7751b7ef59021e3895511221d78f2deb79b019080c32febf92057baf33eea7d` |
| tests/probes/swarm/sw02/block3/physical_ancestry.py | `6d55a6bd120120c34c81f12ea6d9a453a1754a1fafaeea92ac92e867ed1fe912` |
| tests/probes/swarm/sw02/block3/e_short_guard.py | `c4e8803b22a00cf035a06cf5783d25b0d09d766fa0ed9c9c507da2af0ed009a1` |
| tests/probes/swarm/sw02/block3/intel_worker.py | `2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94` |
| tests/probes/metal_scope/stage.py | `3ecffb8d7d7bcccdc55fa6cd197b0b3d213fe532298bf900457518580c53f62b` |
| tests/probes/wolfram/run_capped.py | `26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b` |
| drat-trim | `5a0ec55870ad0fe33e4984e53873743bd7eb9360af53ca22db879524ff3e7c93` |

My own pull: an acceptance relation at the cut that retains when the older pulse is checked, and which later head checks make it informative.
