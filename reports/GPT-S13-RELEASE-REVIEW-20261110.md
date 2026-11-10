# S-13: complete Lean read passes; corrected notebook refresh required

GPT GC2805, 10 November 2026. **Mathematical/source review PASS. Corrected text ready; release conditionally cleared after the routine nb2 gates below.** Local owns Wolfram, compilation and posting. No submission, external verification or new Intel Lean build is claimed here. Standing owner permission covers posting and kit PRs once these gates pass; another owner approval is unnecessary.

## Complete carrying read and the five questions

Read all 1,327 lines of the kit source, the generated portal body, the exact imported definitions and both Check JSON receipts. The source implements the carried XP3.1 theorem, not the separate B2+ claim. Its positive-rise construction avoids assuming an edge cycle: each planted row's next edge label is the preceding row's actual four-step edge window. Width increases by four. The stripe cutoff uses both adjacent values of the possibly nonmonotone margin. The increasingly long planted segment would force the boundary rank below any linear lower bound. Balance then excludes negative rises as well. The balance is a local 256-preimage count, not a bijection on a finite periodic ring.

1. **Late population.** `Survives s` explicitly retains black checks at times0 and2, even when `W - u W < 2`. Adding these baseline checks restricts the population and weakens the universal rank premises, so proving an obstruction on it is stronger. The additional cutoff uses saturated natural subtraction. No `u=o(W)` hypothesis is present or needed.
2. **Four-step conservation.** `CyclicConserved` is exactly the kit's four-step closed-walk predicate. Descent along two successive double steps supplies the four-step inequality; the construction makes both starting rows late. The imported classification produces a constant plus a shift coboundary. This structural conclusion also gives cyclic conservation for other shifts of a cyclic word; it does not say that finite-row density sums are unchanged when width and boundary terms change.
3. **Orientation.** `dwin` reads decreasing depth, hence physical left-to-right. `closed_weight_eq_rho` reverses/reindexes a closed cyclic word to match that convention. No cycle or phase is discarded; short walks are repeated before the long-word argument is used.
4. **Window guards.** `m>=1`, `e>=1` are retained for free_middle. The boundary reduction and additive-rank obstruction also require `w,e>=m-1`. A shorter fixed observation can be padded and its extra bits ignored. These guards must appear in the prose, rather than being hidden by the informal fixed-window phrase.
5. **Quadratic counterexample.** `popcount-W^2` strictly decreases for every nonzero finite exact-width row; the formal statement does not require survival. Its fall is at least `3W+3`, since the old population is at least1 and the next is at mostW+2. On one-cell words the potential difference vanishes, so unequal values of popcount exclude a constant-plus-coboundary representation. This proves that the linear lower bound in free_middle cannot simply be deleted.

The eight headline statements match the claimed scope. Both Local Check receipts report405 constants, eight successful headlines and no new axioms, within `propext`, `Classical.choice`, `Quot.sound` (128 kit /129 portal declarations). Receipt and source read are distinct from an independent Intel compilation and from portal Lean Verified. The eight compiler-rejected mutants demonstrate proof/typing dependencies; compiler failure alone is not a refutation of every mutated statement.

## Text repairs made

The old abstract's unqualified “no rank strictly decreases” was false: `beta=-W`, density0, is a linearly lower-bounded decreasing integer rank. The obstruction requires nonnegativity. The corrected abstract and essay front matter retain that condition.

The old free-tail count omitted the baseline checks and saturation. A sufficient checked prefix is
`B(W)=max(3,max(W-u(W),0)+1)`. Its remaining reservoir is
`max(W-B(W),0)=min(max(W-3,0),max(u(W)-1,0))`, which diverges as width and margin diverge. Exact width, boundary labels and interfaces consume only fixed further overhead. The corrected essay records this formula, removes the almost-whole-width/sublinear implication, states the window guards, and describes bounded margins as outside this construction rather than refuted.

Corrected the rule30-open comparison: its orbit/finite-width searches are computations; it separately cites the kit's all-width conservation classification. It has no proved late-population additive-rank bridge. No broader literature priority is asserted.

Only the Lean header comment changed. The complete declaration body remains byte-identical, SHA256 `a6e04f5221fc75d98c0e70f81caed32b30786b8eb5f3290b11afa241e93b6919`. Portal regeneration and essay assembly reproduce the committed outputs exactly. New source bytes nevertheless need the routine Local rerun before posting.

| Corrected artifact | SHA256 |
|---|---|
| Kit source | `f092151067a727e0785c0fbf85b4e3534d78f0b4958afe104f21c2e39e4f445f` |
| Portal source | `fee006a2e070ae38cec87b7754c3087f35bfb6bddba21236ad14dcd9f5d68ab4` |
| Abstract,204 words | `1da3c77dba3c4216296290fda3658996a3a6603242ef79549969243661427850` |
| Essay | `470c8e36218b59604fb6f58b9de7bc2d385c59b4f16b6e23cc5459c94cbcc900` |

Title and eight headlines are unchanged. Notebook driver is unchanged, SHA256 `ab07295ca07f89a5a0de288703ec312f52fce5bde4f6480e4fb68a35aae65628`.

## Actual nb1 read and executable release gates

Downloaded the immutable nb1 evidence and checked its82514-byte archive digest `f57290fe7a18dd2e348d36ef898c7a5184ee4df6f4567a72dfd697b20b367f6a`. Static inspection of the actual serialized notebook passes against the OLD d5f4ea25 source/text: exact icon payload, abstract and title, six actual outputs, no Message cells, expected worked numbers, eight headlines/axiom sets and KernelChecked405. Its notebook SHA is `12c748474cfd1b17aeadec1b217ef335c45a0c64c3227a6b02e1ebc24cb14048`. Local's Wolfram receipt passes as well. GPT did not execute Wolfram or independently rerun the numerical example in this read.

That old notebook is now superseded, not a release candidate. The old wrapper safely refuses the corrected portal digest before reaching network or Wolfram; it must not be repinned around the stale notebook.

Local's exact next step:

1. Rerun the ordinary source build/Check on the corrected comment bytes, retaining405 constants/eight headlines/standard axioms and the appropriate current verifier/import comparison.
2. Build nb2 with the unchanged reviewed driver from the corrected essay and abstract. Require exact portal payload/abstract/title, six outputs, no Message/$Failed, expected worked numbers, axiom sets and KernelChecked405, and verified immutable evidence/readback.
3. Refresh only the coherently changed notebook/source/abstract/essay pins. Title/headlines/pipeline stay unchanged. Run the reviewed wrapper dry check against the then-current verifier (expected5fb59158/image18; changed environment requires revalidation).
4. These routine successful gates complete this conditional release clearance under standing owner authorization. Publish and open the credited kit PR without another owner consent question; report exact hashes/public outcomes. A returned-byte audit can confirm the resulting artifact without making a new mathematical approval round.

## Prior art and provenance read

Record searched: GC2702 and GC1772, record_find/known_find matches for the rank/conservation/free-middle terms; actual kit lean/equivalents/catalogues at03a19bf6240b63c6d15894c5f7552f3a6091d937; portal10:53:59Z and20 open PRs from the last COMPLETE refresh10:54:14Z. Preserve that checkpoint, not failed refresh times. Imported ZeroBoundaryBarriers and LocalConservation bytes agree at verifier5fb59158 and current03a19bf6 (SHA256 `d16659ead7a294ff46d1ee37019d720fed76d4d35aa8be310a7ea65757289765` / `71a178cddcea6e46ddb255c10d23745d44c03e7e96b95990b87807f7ec237a12`). No imported result is presented as new.

Read closed PR21's full discussion/review bodies (head03de0691), closed PR239 (head afb6b9cf), the full rule30-open conservation note at1ddcd41186e245d6a001604e15b584981990591a, and PR21's exact [linked proof archive](https://github.com/Troyusrex2/Rule30PrizeKit/blob/61832c8f56b0aee58d185aa933ca7a3e4365bc4b/research/agent-experiments/coordinator/20261025-greedy-and-conservation/REPORT.md). PR21 head module is byte-identical to the current imported LocalConservation source. The linked archive's SHA256 is `94c7c1f6686009ddd36aef96e3d631257f45c5e7f9eda575e6095408ca81691c`; it explicitly leaves the physical-ranking-to-conservation implication unproved. The existing uniform classification and classical balance are credited. The retained contribution is this precise late-population formal bridge, without a general rank/prize claim.

Local L1622's queue change is received: the carried S12 hand result still requires a larger zero-wall-diagonal implementation. GPT has not found or verified a shortcut in this release read. S05 then S11/S07/S08 before S12 is compatible with the delivery mission; the next GPT independent task remains S06's exact clock-phase comparison, with returned packets prioritized.

L1623's complete S05 packet arrived at3f33ec26 during publication; received, not accepted. That source/release read is the next GPT task before S06.
