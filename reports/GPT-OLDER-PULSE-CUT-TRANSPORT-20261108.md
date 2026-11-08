# Older-pulse information at the shared-row cut

GPT GC2737/GC2738, 8 November 2026. Owner requests continuation of the shared4→7 pull. The [previous guard block](GPT-SHARED-47-HISTORY-GUARDS-20261108.md#outcome-and-the-next-shared-row-coordinate--gc2734) supplies the checked finite implications and one-pulse countermodel. This block changes representation, retaining the whole ancestry; it does not retry the full target solve.


**Outcome GC2741:** the older pulse has an explicit nonlinear register predicate P at seam cell83; a second predicate Q is read at80. In the exact45-tick physical frame, the possible pairs are **00,01,11**, with10 excluded by the original guard certificate. The parity interpretation and physical rebase are PROOF-SKETCH pending Local's carrying read. Equality is refuted by a new full finite-history witness. Free-outer strip filters remain inadequate and are parked; the full4→7 target stays open.

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

## Outcome — GC2741

### The exact physical relation is implication, not equality

The final missing-corner query is **SAT** in303 conflicts. Root **54421244276371** satisfies every original45-tick cone clause with head3 changed to white, all other original heads retained, and column8(13)=black. Every cone cell, independent scalar evolution, both parity identities and the entire85-tick finite ancestry replay. The corresponding CNF is105631 bytes, SHA256 `cd685ccbb9d21bdee24a5fb493e17f537e5adb29e6ef68c3ce4db70ef48b5801`. It refutes the equality prediction. No new UNSAT proof is needed or claimed.

| Original-frame root | Older pulse at3 | White input at10 | Black input at13 | (P,Q) |
|---|---:|---:|---:|---|
| 52777231658405 | 0 | 0 | 0 | 00 |
| 54421244276371 | 0 | 0 | 1 | 01 |
| 57931849600863 | 1 | 0 | 1 | 11 |

The last root is the retained genuine seed2135555 history cut at74 and clipped to46 cells. All three are actual finite starts in the initial-black drive. They retain the same common S heads at5..45. Pair10 is excluded by the previously VERIFIED original-cone guard13 proof, not by any of the free-boundary strip tests. Thus the exact projection onto **(head3, column8(13)) under S is {00,01,11}**: finite-certificate exclusion plus independently replayed models for every remaining corner. This finite relation is checked. Interpreting it as the nonlinear P/Q constraint at the target's193-tick seam uses the new telescoping/phase specialization and remains PROOF-SKETCH for the second read.

The two P=0 examples have even the **same seven individual OR terms**, namely1111101, yet their Q values differ. Their eight Q terms are01110111 and01110101; only the term for source time11 changes. That term is the OR of source-row11 cells7/8, corresponding to physical time119 in the target's108-shifted frame. This identifies a concrete place to inspect next; it does not say that this pair alone controls every history, or that the two roots differ by one physical cell. Their band80..102 words differ (1688989 and6321393), so no same-band collision or band-independence claim is made.

### What the failed strip controls teach

The initial8 relaxed strips and the two corner-corrected strips all have replayed SAT countermodels. All initial8 violate the omitted necessary outer-column update. Adding its44 projected clauses rejects both retained W12 full-premise countermodels but still allows fresh countermodels to both guards. Hence neither free outer pairs nor that one necessary consistency condition retains enough history. These statements refute the corresponding sufficient-model predictions; they do not refute the original physical guard.

No third strip correction, wider window or full4→7 solve follows. This route reopens only on a genuinely smaller exact boundary-history relation or a specific structural obstruction that can be checked while retaining the actual incoming state. The whole-tail ancestry cut remains the independent representation.

### Carrying request and next executable step

Local: please carry only (1) event(t,p) at j=193−t+p and the204→158 pending-pair counts; (2) telescoping the inverse recurrence to the two P/Q parities; (3) the common-S use of the certified white/black guards, including P⇒Q rather than equality; and (4) the distinction between full local85/global159 ancestry controls and the unproved earlier E/A^4 history of a target193 witness. The finite truth-table models and old certificate can be replayed from cited evidence; no new computation is assigned.

Next executable step: derive the exact three-scan-step transfer of the pairs for rows111..120, keeping the **actual four incoming values of row121 at j83,82,81,80** from the full high-tail reconstruction. Inspect how the row119 cells7/8 OR term can differ between the00 and01 controls while their earlier seven OR terms agree. The20 pair bits and four incoming values are an interface to the full ancestry, not an autonomous state or freely chosen driver. This is a small symbolic relation to write and carry before any new solver run. Independent alternative: annotate the existing original-CNF guard13 proof with this parity meaning and extract its head-dependent part, without searching again.

### Resources, evidence and refreshed record

All three separately published stages complete under their frozen controls. Accounted CPU including each stage's outer supervisor is **2.751386seconds**; total outer wall3.35seconds. Maximum sampled tree RSS48300KiB, maximum child rusage38096896bytes, minimum launch/running sampled headroom5130MiB, zero observed swap growth, at most3 observed processes. The final subsecond stage has no meaningful live RSS sample; its child rusage25137152bytes is retained. No pressure/thermal/monitor stop, GPU, Wolfram, Lean build or target solve. A concurrent-main push rejection delayed the first stage; the merge and successful freeze push completed before launch. No research job ran after a failed publication.

Post-run comment correction: the strip script's flipped-head control was incorrectly called a sampling-phase test in one comment. The current comment now says flipped head; executable code is unchanged, and the executed source version/hash remains in the archive. No new phase-control claim is made.

Evidence: `cited/gpt/gc2741-older-pulse-20261108.tar.gz`,153761 bytes, SHA256 `7e34c8c5696706d0ac1b262100a1e0accf13d348886285c342375366073a461d`, verified TLS/raw-body upload and exact readback. All11 SAT models, exact case CNFs, scalar/ancestry/diagonal outputs, native positive/empty-proof controls, source versions, normalized plans and receipts retained; original raw receipt digests recorded before path normalization. Earlier certified guards remain at the GC2734/GC2724 evidence pointers.

Fresh complete index **2026-11-08T14:48:37.276191Z**, kit `12ddd22e48df1d27a45e914b34839c251f84a9bf`, portal14:48:30Z,15open PRs. New own S04 [R30-20261108-752db6](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261108-752db6) and Block8 [R30-20261108-c1d531](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261108-c1d531) are Lean Verified; both actual portal sources equal the approved bytes. PR226 head a0db7d983563 and PR227 head c5513688884a module files likewise match. Current kit's S02 module equals reviewed SHA256ed43f13d…, and Local L1589/L1590 posting/rebase/recheck/open-PR outcomes are fully read. Closed PR225's separate discussion and review-summary lists are empty. No changed outside statement affects this guard question. No new submission or schedule change by GPT.

My own pull: the actual incoming row121 word and the row119 cells7/8 term that distinguishes one-way memory from a copied bit.

## Local carrying read — L1592

*Local, 8 November 2026, 15:34 UTC. Requested in GC2741 (and GC2734's scoped carry). I read the outcome and carrying sections and the GC2734 outcome. I did not import or run GPT's scripts. My independent replay is [`local_carry_gc2741.py`](../tests/probes/swarm/sw02/block3/local_carry_gc2741.py), [output](../tests/probes/swarm/sw02/block3/local_carry_gc2741.out), with its prediction written in the file before the run; every prediction held.*

**Verdict: all four items CARRIED.** GC2734's translation and support step is carried as well.

1. **Event schedule and counts.** In diagonal coordinates v_t(k) = x^t_(k+t) the inverse recurrence is left-permutivity at cell (t+1, k+t+1). It is valid for every column k+t ≥ 0, column 1 reading the drive at column 0. A cell (t, p) is computed when seam cell j = 193 − t + p is consumed. By induction on the scan, its value depends only on seam cells j′ ≥ j (with the leading zeros). Before cell j the live rows are those with s ≥ 193 − j: rows 91..192 before cell 102 (102 rows, 204 pair bits) and rows 114..192 before cell 79 (79 rows, 158 bits). The scan state is these pairs plus the acceptance flag; it is a sufficient interface, not a minimal one, as GPT says. The table of seven events (83, 81, 79, 83, 80, 69, 41) is recomputed exactly.
2. **Telescoping.** With z_s(j) = x^s_(j−193+s), the recurrence gives z_s(j) ⊕ z_(s+1)(j) = z_s(j+1) ∨ z_s(j+2). XOR over s = a..b−1 telescopes. With a = 111, b = 118 at j = 83, the end terms are z_111(83) = head at 111 and z_118(83) = column 8 at 118, so P (seven OR terms) is head111 ⊕ col8(118). With a = 113, b = 121 at j = 80, the end terms are the center at 113 (white: odd tick of a drive black at even ticks) and column 8 at 121, so Q (eight OR terms) is col8(121). All OR terms are at columns ≥ 1 of live rows. P uses the pair state of rows 111..117 just before cell 83, and Q that of rows 113..120 just before cell 80, of the same M.
3. **Common S and P ⇒ Q.**
   - The guards are cone implications in the 45-tick/46-cell source frame. Physical tick 108 + τ has the same drive phase, because 108 is even, and the cone holds whatever lies beyond column 46.
   - S (head113 white, the 5·3353 heads 115..153) contains the weaker white guard's premise (heads 7..45 of the source). So col8(118) = 0 and P = head111.
   - P = 1 restores the full original premise, and the VERIFIED black guard gives col8(121) = 1, that is Q = 1.
   - Equality is refuted by root 54421244276371 at (0,1). The projection {00, 01, 11} follows from the certificate (10) and the three replayed roots.
   - The replay confirms each root's heads 5..45, the bits (0,0,0), (0,0,1), (1,0,1), both parity identities on all three histories, and the OR-term words. The P = 0 roots share 1111101, with Q words 01110111 and 01110101; they differ only at s = 11, the OR of source-row 11 cells 7 and 8 (physical 119). The fixture computed independently from seed 2135555 at tick 74 is 57931849600863.
4. **Scope.** The three roots are histories from their own source tick 0, physical 108. Their 85-tick ancestry (the inverse scan reproduces all 85 rows here) and GPT's global seam-159 control on seed 2135555 test the event schedule on real histories. Neither exhibits an earlier E/A^4 past for a seam-193 row. P ⇒ Q is a property that any target witness satisfying S at 113..153 would have. No witness is claimed, and the statement is correctly scoped.

**GC2734's scoped carry.**
- Shifting the weaker white guard by an even d = g − 7 ≥ 0, with g odd ≥ 7, keeps the drive phase. It gives col8(g + 3) = white when the heads at g..g + 38 follow 5·3353; with the E-start b = g + 10 that is col8(b − 7).
- At seam 193 the past column-8 values at 118 and 121 depend only on cells ≥ 83 and ≥ 80, which include the whole high tail. The future ones at 284 and 287 depend only on cells 1..99 and 1..102, by finite speed.
- The supports overlap on 83..99 for the white pair and on 80..102 for the black pair, 23 cells at most. That is not a 23-bit closure, for the reason GPT gives.

**Status.** The hand steps of GC2741 (items 1–4) and GC2734 (translation and support) are now PROVED, hand and two-party, on top of the VERIFIED machine guards. The full 4→7 question stays OPEN.
