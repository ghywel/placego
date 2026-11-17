# Portal and kit update — GC2687

6 November 2026, owner-requested records update. Shared record read through `47d2c44a` / L1561. Local's SW-02 is still running at the owner's instruction. This update changes neither its frozen inputs nor its execution; both GPT schedules remain paused.

## Snapshot and status

The complete `known_find.py --new` refresh finished at **10:58:01.797290 UTC**, with portal snapshot **10:57:37Z**, kit main **`9d837cd5e5ac447cd868c20aebf49a1b4cfa866e`**, and **22 open kit PRs**. Since GPT's previous complete check at **5 November 21:48:45Z** (`9af60de9f51a2b110934006053cddb22d906cec5`), the index has **49 additions, four changes and two removals**. Those are index items, not submission counts.

The portal grew from **197 to 209 submissions**: **12 new entries**, one existing entry's badges changed, and none removed. Current totals are **208 Lean Verified**, **186 Human Verified**, and **147 Kit Contribution**. All entries still label their claim as partial. The remaining Lean Unverified entry is the old width-60 memory failure, `71f858`; this refresh supplies no new verdict on it. All 206 advertised Lean-source URLs have cached source files; this does not imply that every entry advertises a source URL.

The verifier remains **image 18**, Lean **4.35.0**, at kit **`5fb591588cfa869bfdc47946799b5ddd70a903d1`**, distinct from current kit main. All twelve new entries report successful kernel replay without new axioms. This update reads their sources and relevant kit/PR statements; it does **not** rerun Lean or Wolfram. GPT subagents supplied complementary source self-checks, not additional independent-worker carrying reads.

**No new entry establishes a prize conclusion.** Several titles say “discharge”, “unconditional”, or “bound” within a conditional framework; the conditions below matter.

## Important mathematical additions

**An exact anti-periodicity criterion is now in the kit.** For every Boolean sequence and positive `M`, eventual `M`-anti-periodicity, meaning `f(t+M) = !f(t)`, is equivalent to eventual `2M`-periodicity together with half density on **every residue class modulo M**. The theorem is `Rule30LeftAntiPeriod.evAntiPer_iff_evPer_two_mul_and_all_subseq_halfDensity`. This sharpens a one-way reduction into an equivalence; it does not establish the required progression densities for the center. [d0a19b](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261105-d0a19b), [landed source](https://github.com/WolframInstitute/Rule30PrizeKit/blob/9d837cd5e5ac447cd868c20aebf49a1b4cfa866e/lean/Ruliology/CellularAutomata/Rule30LeftAntiPeriod.lean).

**Period eight is organized into two remaining coupled questions.** The sixteen globally 4-anti-periodic binary sequences fall into two cyclic necklaces, `00001111` and `00101101`. The new reduction still assumes `CQ` for **both** necklaces; those are open. For an arbitrary 8-periodic column it also needs half density on all four stride-four residues. Thus this is a useful finite classification and conditional reduction, not an unconditional exclusion of period eight for the seed. [0a13ed](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-0a13ed), [PR189](https://github.com/WolframInstitute/Rule30PrizeKit/pull/189).

**Right-edge periods lift inward one bit at a time.** If the low-index collar `j < N` of the edge-map row returns after `P`, its next bit is either `P`-periodic or `P`-antiperiodic. The enlarged collar returns after `2P`; adding `d` bits gives a return after `2^d * P`. These are return times, not necessarily least periods. No rain-tail assumption is needed for these lemmas, but the initial collar-return hypothesis is retained. This packages the triangular map's known period mechanism; it does not give one period for the infinite row, wall capture, or Q01. [9760e1](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-9760e1), [PR193](https://github.com/WolframInstitute/Rule30PrizeKit/pull/193).

**A protected healing frontier is independent of right completions.** For actual whole-line Rule 30 evolutions `E,G` agreeing initially on every `x <= a`, the intrinsic frontiers `KFrom E a` and `KFrom G a` agree for all time. Boundary twins attain the fastest leftward causal line exactly while this frontier has recruited no further cell. This is useful for completion comparisons: the entire initial left half-line is fixed, not merely a finite prefix. It does not identify the actual disagreement edge with the protected frontier after positive recruitment, or prove a distribution or capture rate. [09b377](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-09b377), [PR198](https://github.com/WolframInstitute/Rule30PrizeKit/pull/198).

**Two exact reconstruction results strengthen the available tools.** Under a common driver, `Rule30DrivenLeft` now equates equality of a `D+1`-cell spatial slice with equality of a `D+1`-tick column-minus-one window. With white initial tails below `-M`, the first `M` column values determine the entire negative half-plane evolution. This is preservation and reconstruction of information, not forgetting. Separately, `Rule30LightCone` constructs the unique leftmost ancestor **block**, with the rest of the causal collar fixed, that produces any chosen target block: a finite `2^b`-possibility bijection. It does not determine an entire infinite configuration or bound the computational cost of the fixed seed. [5b95a1](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-5b95a1), [719e59](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-719e59).

**The new complexity bound is conditional and logarithmic in the input scale.** For a total binary-input one-tape machine computing `f`, exclusion of eventual period `2^k` gives an input in `[2^(k-1), 2^(k-1)+2^k)` requiring at least `k+1` steps, and possibly a different input there with rightward span at least `k+1`. Assuming Problem 1 gives these witnesses at every scale for the center. This is neither a uniform bound on all inputs nor the linear lower bound of Problem 3. Rightward span `k+1` means reaching zero-indexed cell `k`, not cell `k+1`. [8fafce](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-8fafce), [PR195](https://github.com/WolframInstitute/Rule30PrizeKit/pull/195).

## Complete new-entry register

“All three” means Lean Verified, Human Verified and Kit Contribution at the snapshot. “Lean only” does not assert a human review or integration.

| Entry | Status / PR | Source-scoped addition |
| --- | --- | --- |
| [b2dca8](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261105-b2dca8) | All three; PR187 closed, landed | Columns -9/-10 under a white driver and the assumed `(0,*,1)` skeleton. The `*` is free; this is not a literal periodic `001` column and does not discharge `C3s001`. |
| [d0a19b](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261105-d0a19b) | All three; PR188 closed, landed | Exact anti-periodicity / periodicity plus all-residue balance equivalence above. |
| [5b95a1](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-5b95a1) | Lean only; PR190 open | All-depth space/time reconstruction and single-free-phase determination under a common driver. |
| [0a13ed](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-0a13ed) | Lean only; PR189 open | Two-necklace classification; conditional coupled period-eight reduction. |
| [1f5267](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-1f5267) | Lean only; PR191 open | The anti-periodicity equivalence translated through the five already-equivalent density/energy forms; periodicity and every-residue balance remain hypotheses. No new center-energy estimate. |
| [db8dbc](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-db8dbc) | Lean only; PR192 open | Divisor-stride anti-period transport and a dyadic balance tower. The reverse implication uses only the top balance level; intermediate levels are consequences. |
| [9760e1](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-9760e1) | Lean only; PR193 open | Relative collar-return period/anti-period dichotomy and `2^d * P` lift. |
| [719e59](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-719e59) | Lean only; PR194 open | Constructive surjectivity completes the existing left-leaf injectivity to a finite block bijection. |
| [8fafce](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-8fafce) | Lean only; PR195 open | Conditional canonical-window time/right-span witnesses above. |
| [6f2266](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-6f2266) | Lean only; PR196 open | For `x(t+1)=a(t) XOR (b(t) OR x(t))`, `b` L-periodic and `x` L-antiperiodic from the same threshold imply `a(t+L)=a(t) XOR b(t)`. No coincidence hypothesis, but both period hypotheses remain. |
| [8e3d0b](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-8e3d0b) | Lean only; PR197 open | Explicit closing-law corollaries. Exponent `E+2^E+2` assumes a completed `1(10)^m11` run; existence of repeated closing runs is not proved. |
| [09b377](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261106-09b377) | Lean only; PR198 open | Healing-front envelopes, completion invariance, and exact zero-recruitment/fastest-line equivalence. |

Existing **[ef2406](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261105-ef2406)** gained Human Verified and Kit Contribution. Its new kit formulas reach columns -13/-14 under the assumed `w0001` fitting condition; the extra `no11` condition produces the stated white/black phase cells. This does not exclude the fitting condition.

Two relevant follow-ups were already present at the previous complete check, rather than new overnight: **[f1a386](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261105-f1a386)** formalizes permanent first-difference preservation and exact prefix injectivity of the right-edge map (all three badges, on main); **[7fe916](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261105-7fe916)** formalizes the multi-tick error-edge consequences of our six jump laws (Lean Verified and Human Verified; no Kit Contribution tag). Its jump-six/seven double stalls retain the white-parent guard. Both complete sources were read here. These are direct continuations of the wall/error-edge work, not fresh prize-level mechanisms.

## Integration and our submissions

Main changed in **three Lean modules plus the catalog**, with no change in `equivalents/` in this delta: `Rule30PeriodFourSkeleton`, `Rule30EtherThreeSkeleton`, `Rule30LeftAntiPeriod`. PRs **186, 187 and 188** are closed with null GitHub merge metadata, but each complete module at its exact PR head is **byte-identical to current main**. Accordingly, they are recorded as landed, not rejected. Heads: `bf6232c353d0f2fd054feb32c61c1239adcaefc1`, `d6c0e6d8144f90444bd0cdd872127bec486c3277`, `9c1e6ec5b9f0785eb75d3e3d88ce488ad858c651`, respectively.

Separate conversation, inline-comment and review-summary reads for all three closed PRs found only PR188's catalog-table repair discussion; its preserved-headline fix is present. Review-summary endpoints for all **22 open PRs** were also read, and all were empty. The twelve older still-open PRs have unchanged metadata, sources and cached discussions. New open PRs are **189–198**. PR189's requested reuse of the general PR188 theorem is present; PR193's requested catalog credit and removal of duplicate `iter_add` are present at the recorded head. Neither is yet recorded as integrated. No extra linked proof archive appeared in these discussions; this is not a new audit of every historical closed PR.

Our recent entries have unchanged badges since the preceding complete check:

| Entry | Lean Verified | Human Verified | Kit Contribution |
| --- | --- | --- | --- |
| [3cf160, synthesis](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-3cf160) | Yes | Not listed | Yes |
| [309041, aged left diagonals](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-309041) | Yes | Not listed | Yes |
| [458f3b, four left sides](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-458f3b) | Yes | Not listed | Yes |
| [9aa447, four fronts](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-9aa447) | Yes | Not listed | Yes |
| [c15ef5, right-wall locks](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261105-c15ef5) | Yes | Yes | Yes |
| [0c74ef, error edge](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261105-0c74ef) | Yes | Not listed | Yes |

## Evidence and next step

Record searched: current main's actual `lean/` and `equivalents/` sources/catalogs; the complete index delta; full sources of all twelve new entries plus f1a386/7fe916; ef2406's added theorems; exact added code and relevant antecedents at PR189–198; closed PR186–188 source comparisons and separate discussion channels; all current PR review summaries. This is a source/status update, not a literature novelty claim or fresh kernel replay.

| Snapshot file | SHA256 |
| --- | --- |
| stamp.json | `b69b4e4137906bcd613e8dd399fedccd4b26f5aa76c03df6e6207437486cf3a3` |
| checked.json | `599017c2f681beeceb11c59b8c43f539d72d38c6b128c002452ce2d58cc242bb` |
| portal.json | `9769389882e9f3208a2a1e37f30d22a82aef9eb7060fb7e856386c6381785de0` |
| prs.json | `4ab7b878ef56af5e3bf5930fde3f2c90fff72eb43e2884a3679866ff9794c846` |

Evidence outside git: shared-store `cited/gpt/gc2687-portal-kit-update-20261106.tar.gz`, **1,297,665 bytes**, SHA256 **`77837e1ec8681330fb9f742ce2b8cecf2ce837d4c141073a049f0c9b9007a535`**. It contains before/after snapshots, index output, source/diff pins, PR responses and source-review notes, with an individual-file manifest. Raw upload and byte-exact readback were verified.

**Next executable step:** at Local's next swarm synthesis, compare proposed results against this new-source register, especially all-residue balance, finite-block reconstruction and completion-invariant healing. Preserve the run's frozen source manifest and record any later comparison as a separate audit. L1561's swarm leads are received as self-checks, not carried or promoted by this update. GPT returns to owner-requested review; no new research task, build, swarm job or schedule is launched.
