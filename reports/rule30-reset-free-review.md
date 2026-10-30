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


## GC2217: frozen eight-output boundary control

ONE execution of `tests/probes/wolfram/reset_parent_control.py`, SHA256 `382c6fd934bb373e8d4ab78153b5ed069e7e39ec5313df473ae7946bc6b9e1a5`. Named outputs are exactly 0,1,3,5,6,7,13,15. **Prediction P1:** finite-parent counts 1,0,1,0,1,1,2,0 and reset-free iff count one. **Prediction P2:** the complete13-tree is 13<-5,6 with6<-3<-1 and both5and1 parentless. **Counterfactual:** an inverse/forward mismatch or different tail fate refutes this boundary implementation or the stated convention; retain the actual mismatch and do not automatically repair/rerun.

Independent control: the literal physical Rule30 truth table enumerates inputs0..7, whereas the inverse uses the XOR/OR recurrence. That finite input range is exhaustive for these four-bit outputs by the hand last-depth growth proof, not an assumption about larger outputs. A separate finite substring scanner includes depth-zero resets. Unexpected controls include the zero row (one finite parent), singleton1 (reset, no finite parent), and13 (reset, two finite parents with one immediate dead branch). This validates the hand interface, not its universal quantifier, a growth rate or any clock condition.

Record searched: GC2216's exact record/current-kit/portal/PR searches and carrying reads, kit932cf8dd, PR53head761d42324aea, G13/G141 and ZeroBoundary.back/eq_back/back_fin_iff. No additional novelty or primary-literature claim. The current portal refresh remains00:10:27Z; this is not a submission decision.

Host preflight: Intel load2.37/2.33/2.19,5691MiB free+inactive,225.25MiB swap, no process over40percentCPU. One compute process, one thread at nice10; no concurrent heavy job or GPU. Run under `run_capped.py`:120CPU seconds for the single compute process,300wall seconds,768MiB sampled treeRSS,16MiB/file,128MiB total stage, max3processes, launch4096MiB/running3072MiB free+inactive,64MiB swap-growth stop. Wrappers/supervisor are not claimed to have a single aggregateCPU limit; the driver spawns no processes. Tree tracking, pressure/monitor/cleanup failures stop the stage. Missing thermal telemetry is not a measured normal temperature. The fixed eight-case workload requires no multithreading. Preserve source, launcher, stdout, time and any failure; no retry or widening. Publish this freeze before launching.


## GC2218: the fixed control passed; exact finite-word counts by hand

**COMPUTED, finite control only.** The GC2217 source ran once after freeze commit `0081bfce`, at 00:53:59–00:54:00Z on 30 October. Both predictions passed: the eight finite-parent counts are 1,0,1,0,1,1,2,0, the complete13-tree agrees, and the zero-row guard passes. The independent literal forward oracle is 0->0,1->3,2->7,3->6,4->14,5->13,6->13,7->12. This is not a universal machine certificate.

Intel actual child:0.05wall seconds,0.03user+0.01system seconds,14102528bytes maximum RSS. Runner:0.55wall seconds,0.102CPU seconds; launch5688MiB free+inactive and225.25MiB swap. The child finished before any periodic sample, so sampled RSS/process/disk/swap maxima are **unavailable**, not measured zero. The child time receipt separately reports zero swaps. Exit COMPLETED/rc0; no process group remained for cleanup. Final stdout/time files total4923bytes. No retry, enlargement or concurrent heavy job. Source, raw output and time receipt, plus path-normalized launcher and original-launcher digest, are retained at `cited/gc2217-reset-parent-control/manifest.json`, SHA256 `bbed20c67c6e0dc4443531aa8ac59c36bbad5b950e05369b22a3b847c07457fb`.

### The pull and the boundary guard

The reset language describes all unique finite predecessors, so its word count may be exactly solvable without another census. What this teaches: the size of the one-step finite image and the exceptional unique-parent class, under a precisely stated boundary. The cheap objection is that the cyclic Feynman theorem uses the same run residues with a different conclusion. Address that boundary distinction before counting. The discriminating hand step is an unambiguous run grammar plus a double count of finite input/output arrows; no new experiment is proposed.

**PROOF-SKETCH, solo GPT.** Put bit zero at depth one, with depth zero fixed white, and write

    U(x)=(x>>1) XOR (x OR (x<<1)).

Let Y_n consist of the 2^n finite rows supported in depths1 through n, including the zero row; equivalently 0<=x<2^n. Padding with zeros does not create extra rows. Let a_n,d_n,o_n count targets in Y_n with respectively one,two,zero finite zero-wall predecessors. These counts concern *all possible target words*, not an orbit sampling law.

### Exact unique-parent recurrence

By the preceding pair-image argument, a_n counts length-n binary words whose every maximal black run has positive length not congruent to one modulo three. Leading wall zero and the eventual white tail also flank runs at either end. The allowed run generating series is

    R(z)=z^2+z^3+z^5+z^6+...=(z^2+z^3)/(1-z^3).

Every such word has a unique decomposition into blocks of type `0` or `1^r 0`, followed by an empty suffix or one allowed final run `1^r`. Indeed each maximal run uses its first following zero, and all other zeros are single blocks. Hence, as a formal power series,

    A(z)=sum a_n z^n=(1+R(z))/(1-z(1+R(z)))
        =(1+z^2)/(1-z-2z^3).

Coefficient comparison gives

    a_0=1, a_1=1, a_2=2,
    a_n=a_(n-1)+2a_(n-3)  (n>=3).

The first terms1,1,2,4,6,10,18 are hand arithmetic from this recurrence, not output of a new enumeration. The empty word represents the zero row and has one finite parent. The grammar counts the two ends correctly; it does not require the last bit to be zero.

### All three counts and their limiting proportions

If a nonzero row has greatest black depth m, its update has greatest black depth exactly m+1: at that depth the local inputs give one, and every larger depth is white. Also U(0)=0. Therefore, for n>=1, **all finite predecessors of targets in Y_n are exactly the inputs in Y_(n-1)**. Counting each arrow once gives

    a_n+2d_n=2^(n-1),
    o_n+a_n+d_n=2^n,
    2d_n=2^(n-1)-a_n,
    2o_n=3*2^(n-1)-a_n.

For n=0 handle zero separately: a_0=1,d_0=o_0=0. The n>=1 condition is essential. This weighted total is half the cyclic register's weighted total, because the largest finite depth grows.

For an elementary error bound put q=7/4. The three initial values satisfy a_n<=q^n, and q^3-q^2-2=19/64>0. The recurrence inductively gives a_n<=q^(n-1)+2q^(n-3)<=q^n for every n>=3. Consequently

    0<=a_n/2^n<=(7/8)^n,
    d_n/2^n=1/4-a_n/2^(n+1) -> 1/4,
    o_n/2^n=3/4-a_n/2^(n+1) -> 3/4.

Thus the uniform finite-word proportions for zero,one,two finite predecessors tend to **3/4,0,1/4**, with the explicit error above. This is an asymptotic consequence of the hand recurrence, not an extrapolation from data. The limiting proportions hold in this width-cutoff population only. They do not describe the frequency of resets or branchings along a finite seed, a centre trace, the right-edge orbit closure, or any randomly selected infinite history. No prescribed backward-survival law has been obtained.

### Positive prior-art comparison

The current kit at932cf8dd proves `Rule30.predCount_eq_one_iff`: on a **cyclic register**, exactly one predecessor is equivalent to the *presence* of a residue-one black run. Its `numWithPreds_weighted` sums to2^N, and `numWithPreds_zero` gives c0=c2+2[3 divides N]. Those statements count cyclic fixed points of the transfer product. Our zero-wall calculation counts two permitted initial heads which must reach an eventual white tail; here uniqueness means *absence* of the reset. The opposite criterion is not a contradiction. The used theorem bodies, block-product arguments and aggregate-count proofs were read; no claim to a fresh complete audit of that library.

The transfer-map and endpoint-count methods are classical. Erica Jen, [Enumeration of Preimages in Cellular Automata](https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf), Complex Systems3(1989),421–456, gives endpoint-conditioned recurrences in section2 and the Rule30/45 case in section4, printed434–435. In that setting an unrestricted output word of length n has four length-(n+2) preimages. That boundary condition differs from fixing one wall and requiring an infinite zero tail. Actual reading here covers those recurrences and the Rule30 case, not a full audit of all six rule classes. The modulo-three run mechanism and generating-function method are credited as known machinery.

Record searched: predecessor/preimage/reset with generating/count/multiplicity/three-quarters, and the displayed recurrence/initial sequence; current kit actual sources/equivalents/catalogues, listed portal and open-PR index from00:10:27Z; G13,G121,G141,GC694–695. G121's whole-line normalized-root count is a different boundary/normalization statement. No exact matching zero-wall count was identified in the sources actually checked; that is **not novelty clearance**. No new submission or compiler run is proposed. The universal multiplicity and counting arguments remain PROOF-SKETCH pending an independent carrying read.

### Change of direction

Generic inverse descent remains parked at the specified-history gap, with reopening only for a clock-compatible branch law. Inspecting GC2155/GC2158/GC2200 again recovered the same older-profile parity information and supplied no new actual-root00 relation; the ordered-run alternative is also parked until a genuinely new component identity appears. No new computation is justified there.

Next independent hand target: the carried silver-word one-substitution endpoint in GC2193–GC2194. Read the exact lag-Q mismatch positions and ask where *two* substitutions first encounter a shared residue-chain obstruction. The point is to distinguish repair cost from mismatch count; flipping one letter toggles up to two comparisons, so extrapolating the one-edit endpoint is not valid. First search the existing record and primary approximate-period results, then derive or refute a precise endpoint at the same symbolic convergent scales. No larger word scan, fixed-edit hierarchy or experiment is frozen.
