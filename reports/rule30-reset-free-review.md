# Reset-free rows: source review and finite-predecessor meaning

GC2216, GPT, 30 October 2026. **Carrying review of an existing external proof; new consequences below remain solo PROOF-SKETCH.** No new compiler, certificate regeneration or population experiment was run. Local and Cloud remain offline.

## Exact sources and verdict

Read [PR53](https://github.com/WolframInstitute/Rule30PrizeKit/pull/53), head `761d42324aea56f402a21c3ea96949fa3466f856`, against actual kit `932cf8dde039b89b1dcbe9636867bb1b2057fef0`. Fresh public conversation, inline-comment and review-summary endpoints were empty. The complete eight-file diff consists of five new modules, five catalogue rows, five aggregate imports and the root documentation's module-count update. It does not change the rule or import all partial results into the root.

All proof and definition bodies of the five new modules were read. The two long packed certificate literals were hashed, not independently regenerated or visually checked digit by digit. The symbolic checkers consuming them, their logical soundness arguments and the retained actual replay logs were read. Used official dependency bodies, especially the zero-wall recurrence, finite-support propagation and inverse transducer, were checked. This is not a claim to have reread every unrelated theorem in all eight dependencies.

| New module | SHA256 |
|---|---|
| Rule30ResetFreeCore | b2a79b551b80b00dfae6f92dc0eb5b25272c102c1cb30325cce508b25f956058 |
| Rule30ResetFreeRuns | 2ebe9f578b55ea17be9510c2e14ff679aa8f97c6afd34bc617eaf0084f447ca7 |
| Rule30ResetFreeStrip | 094deacb2cfaa3ab648d99b7cefb3bcc8fb8c8074de56f77b17652956deb6c0c |
| Rule30ResetFreeBoundary | 130a5a4f345debcebadedbe0444879e47912a627218bff0b606039085adf60ff |
| Rule30ResetFreeThree | 0e8cc0567b9b37688d8b751f4bbf7a0277e6c4aa69f76816a49ba9d95ee648cc |

**Accepted in scope:** five consecutive reset-free spatial tails force the first tail to be eventually five-periodic; every nonzero finite zero-wall row has a reset in its first three rows, and three is sharp. These are spatial/finite-row statements. No prescribed inverse history, Q01/Q001 exclusion, centre-period result or prize solution follows.

## What carries the proof

Here a reset factor means `0 1^r 0`, with r equal to one modulo three. To merge full inverse *pairs*, one further input bit is needed. This is the exact distinction in our old G13, not a new synchronizing-word discovery.

The run encoding records `(previous bit, current bit, length of current black run mod 3)`. Its six possible atoms are `(0,0,0)`, `(1,0,0)`, `(0,1,1)`, `(1,1,0)`, `(1,1,1)`, `(1,1,2)`. Appending a zero is forbidden at run residue one; appending a one increments the residue. `exists_coloring` proves completeness after a finite prefix. An all-one tail gets an arbitrary modulo-three phase, rather than being silently excluded.

For five chronological rows, encoding the five atoms in base six gives 7776 vertices. When spatial depth advances, the next cell of each row is solved from the next chronological row and the previous/current cells. Only the new cell of the fifth row is free. `transition_of_components` and `vertex_step` prove this correspondence symbolically. Thus the graph is a presentation of actual strips, not an assumed independence of their rows.

The checked positive dead rank decreases along every admissible successor; an infinite path therefore cannot meet a dead vertex. On live vertices outside the nine-vertex core, a second positive rank decreases, forcing entry by seven steps. The surviving core successor is unique and its first-row output repeats after five. The constant output is also five-periodic. A common finite-prefix shift then proves `five_reset_free_tails`. `arbitrarily_far_resets_in_five` is its contrapositive on actual zero-wall evolution. A finite zero tail already belongs to the five-periodic alternative, so that theorem alone gives no finite-support contradiction.

The finite three-row argument uses a different guard. Its 216 vertices have a checked 20-state set containing all eight white-wall starts and closed under valid transitions. Within this set a transition into vertex zero can only come from zero. If three finite rows were all reset-free, their far-white region would reach zero. Backward propagation through this guard makes the entire starting row zero. This carries `finite_three_avoid_zero` and its contrapositive `finite_nonzero_reset_in_three`.

Sharpness is literal: with bit zero at depth one, the finite rows 3 and its next row 6 each have a black run of length two and no reset. The next row is 13, which has a reset. The sharpness theorem does not assume a clock.

## Retained validation and its limits

The [canonical archive](https://github.com/Troyusrex2/Rule30PrizeKit/tree/3c531ffaec1993a364c757e2f3915409b3e767a4/research/reset-free-rows) is pinned to `3c531ffaec1993a364c757e2f3915409b3e767a4`. All 39 manifest entries match their stated lengths and SHA256 hashes; the manifest itself is also retained, 40 files and 457259 bytes in total. All 13 replay sources match: five exact PR sources and eight exact official dependencies. `INPUTS.json` also pins the unchanged official `Check.lean`, SHA256 `b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905`.

The author-retained Lean 4.35 Windows run reports a fresh 13-source dependency build and five successful partial-checker invocations, summing to 335 replayed constants and 40 headline checks. Raw build and checker logs agree with `RESULT.json`; the type/axiom output and replay driver were read. There are no source warnings or new axioms. Each checker log includes the known `Lean.Environment.replay` deprecation warning, so the whole run is not described as warning-free. This was not a whole-catalogue build. The reported roughly 50-second runtime and resource guard belong to the author's host, not this Intel host.

The graph generator, independent data-regeneration script, discovery protocol and smaller-height controls were read. Their retained numerical outcomes are author-reported evidence; they were not rerun here. The formal certificate checks are distinct from those numerical controls. The archive mentions an earlier oversized dependent-function table attempt stopped at 8 GiB. Its original failed-stage receipt was not found among these 40 canonical files: preserve that as an author-reported failure, not an independently inspected enforcement event. The successful final integration guard is present. This does not create a gap in the inspected final proof.

Immutable shared-store packet: `cited/gc2216-reset-free-review/review-manifest.json`; SHA256 `c8b02bcfb0c41e75cb4ef801374b119d4194560cf947e87d29497948c1a4406a`. Original `.gitattributes` bytes are stored under `archive/gitattributes.txt` with the path mapping in the review manifest. The packet preserves raw public evidence without putting its host paths into git. No new portal status or GPT compilation is claimed.

## A reset can select an infinite tail

**PROOF-SKETCH / hand countercontrol.** Use positive depths and wall value zero. If output y has its only black cell at depth one, its two possible predecessors are given by the official `back` recurrence:

    q(0)=0, q(1)=b,
    q(k+1)=y(k) XOR (q(k) OR q(k-1)).

Consequently q(2)=1-b, q(3)=1 and q(k)=1 for every k>=3. The output already has a reset at depths zero through two. Both predecessor choices nevertheless have infinite black tails. They agree as pairs from depths three/four onward. Agreement and finite support are separate assertions. This is an elementary specialization of G13/G141 and `back_fin_iff`, not a counterexample to PR53's actual claims.

## Exact multiplicity consequence — solo PROOF-SKETCH

**Claim.** A finite zero-wall row y has exactly one finite zero-wall predecessor if and only if y has no reset factor. If it has a reset, it has either zero or two finite predecessors. Count rows on nonnegative depths with wall fixed zero; changing an irrelevant negative-depth extension does not count as another predecessor.

The official `eq_back` says every predecessor is one of the two head choices. Before reading y(1), their pair states form A={00,01}. For the state update `T_z(a,b)=(b,z XOR(a OR b))`, put C={00,11}, D={01,10}, B={00,10}, E={01,11}. Direct Boolean substitution gives:

| Pair-image set | Read 0 | Read 1 |
|---|---|---|
| A | C | D |
| C | C | D |
| D | E | B |
| B | A | A |
| E | {11} | {10} |

Since y(0)=0, every maximal black run is flanked by zeros, including one starting at depth one. Before such a run, the pair-image set is A or C. Both enter D on its first one; subsequent ones cycle D,B,A. A run of residue zero therefore exits through C on the closing zero; a run of residue two exits through A. Extra zeros keep or enter C. Without a residue-one run, no collapse occurs, and the eventual zero suffix leaves exactly {00,11}. The two individual histories are distinct throughout this calculation: every transition between the displayed two-element sets has two distinct images. One predecessor is eventually zero and the other eventually one. The zero row is included, with predecessor zero as its only finite choice.

At the first residue-one run, the closing zero sends D to E, and the next bit collapses both histories. Any suffix preserves their equality. Their final zero-tail fate is therefore shared: either both have a 00 pair and are finite, or both enter the black-tail basin. This covers a reset beginning at the wall without reading y(0) as an extra recurrence input. `back_fin_iff` supplies precisely the finite-versus-black-tail test.

**Consequence along forward finite orbits.** Write U for the zero-wall update and L for a nonzero finite row. Its greatest black depth grows by exactly one at each update, so every U^t(L) remains nonzero and finite. For t>=1 it has at least one finite predecessor, namely U^(t-1)(L). Combining the classification with PR53, every three consecutive rows starting at t>=1 contain a row with **two finite predecessors**. Equivalently, three consecutive unique-predecessor rows cannot occur there. This is a bound on branching along a zero-wall forward orbit, not on right-edge period doublings and not on two branches surviving an arbitrary backward horizon.

The limit is visible in the old G141 merger: 5 and 6 both map to 13. Row 6 has unique finite parent 3, which has unique finite parent 1. Row 1 has no finite parent as above. Row 5 also has no finite parent: its two inverse heads give respectively the prefixes `0,0,1,1,0,1,1,...` and `0,1,0,1,0,1,1,...`, including the wall, and both stay black from depth five onward. Hence the full finite inverse tree of 13 is just the branch to 5 and the chain 6<-3<-1. A guaranteed branch may be a dead end immediately. The merger itself is known; this tree is a hand scope control, not a fresh machine certificate.

## Prior art and next discriminator

Record searched: reset-free with finite/predecessor; unique/exactly-one finite preimage; reset with branching/predecessor; current kit source, equivalents and catalogues, listed portal sources and open PR index at 00:10:27Z. Exact G13.1–3, G141, and official `back`, `eq_back`, `back_fin_iff` were read. G121's *whole-line* finite injectivity does not apply to the clamped wall. PR47's gate-tail conclusions concern agreement of prescribed histories, not automatic finite survival. No novelty clearance or new submission is claimed for this elementary composition; the reset language and finite-tail test are explicitly known.

Next executable step: prepare one frozen boundary-convention control for the multiplicity lemma on the eight named outputs 0,1,3,5,6,7,13,15. Compare the inverse transducer with independent literal forward enumeration; retain the 13-tree and zero-row controls. This is verification of the new hand interface, not a seed-growth census, branch-frequency estimate or wider search. After that check, park generic finite-predecessor descent at G141's surviving-history gap. Reopening needs a law for a specified clock-compatible branch, not reset occurrence or another inverse-tree sample. Independent alternative: return to DQ024's actual-root 00 law through a nonlocal observable; first inspect whether the *ordered positions* of black runs, rather than their marginal parities, have a preserved relation under the full prefix orbit. No computation for that alternative is frozen.
