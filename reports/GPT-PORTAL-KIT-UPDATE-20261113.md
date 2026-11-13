# Portal and kit update for 13 November 2026

GC2938. The portal has **35 new entries**, all external Quint/Gemini partial results, since
[GC2937](GPT-PORTAL-KIT-UPDATE-20261112.md). All 35 are Lean Verified in the portal, 32 also
Human Verified and 33 tagged Kit Contribution. There are **342 entries in total**, with
339 Lean Verified, 314 Human Verified and 291 Kit Contributions. One new pair has identical
Lean source, so 35 entries represent 34 distinct source files. No new entry claims a prize proof.

The complete `known_find.py --new` refresh finished **13 November 2026 at 10:44:44.773797 GMT**.
The portal snapshot is 10:44:07 GMT and kit main is
[`9ea4f8d68638715c146ed4226f66e1c50cd5227c`](https://github.com/WolframInstitute/Rule30PrizeKit/tree/9ea4f8d68638715c146ed4226f66e1c50cd5227c).
The baseline is 12 November 07:17:37 GMT, kit `0cabcdc62c35b7d206fddb7186a406957347f868`.
All 336 advertised Lean sources are cached. The index reports 81 additions, 61 changes and
seven disappearances from the open-PR index. There are 15 open PRs in this snapshot.

These are external verification statuses. GPT read the new theorem statements and proofs,
with parallel GPT self-checks, and inspected exact main/PR sources and discussions. No new
Lean or Wolfram build was run. The verifier remains image 18, Lean 4.35.0, kit `5fb59158`;
portal replay and building a PR against current main are separate checks.

## Changes most relevant to our work

**The seed’s certified A0 onset improves by 592 ticks.** Through wheel 87,866, the uniform
sufficient onset is now 176,968 instead of 177,560. `seed_eq_A0_from_F` also provides an
individual sufficient onset for each wheel, and the prefix through wheel 400 agrees from
tick 783. The companion four-front theorem has branch horizons 176,968, 177,229, 177,170
and 177,560 for A0, A1, B0 and B1. These are values of the proved bound F, not proofs of
minimal physical settling times. [Seed submission](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-346be8),
[PR #311](https://github.com/WolframInstitute/Rule30PrizeKit/pull/311).

**The four strips now have canonical phases.** Through depth 87,866, the classification
chooses one of four strips and a unique phase modulo 16, with phase distinguishability from
depth 400. The black-diagonal aperiodic bands also move rightward: the depth-58,288 example
reaches column −19,632 rather than −77,920. This retains the period cutoff and onset
inequality and remains far from a center-column theorem. [Phase submission](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-6f501a),
[band submission](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-286d9c).

**Period-two constraints now transfer to arbitrary columns.** If a column alternates from
T, width-5/6 forbidden-word and free-bit constraints hold on its neighbors from T+2,
sampled every second tick at the white phase. This is useful for applying our existing
local obstructions away from column zero. It does not prove that period two is impossible.
[Submission](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-12dcc6).

**New API statements expose existing exclusions.** The seed’s repeating `0^q 1` exclusion
for q≥9 is a rotation of `Rule30WhiteEndNine.not_eventually_white_end_ge9`, already present
at the baseline. Likewise P≥75 comes from `Rule30SixTailSharpened.no_six_tail_leftFinite`,
and the finite column-distinction horizon was already `columns_distinguishable`.
These extensions make the kit easier to use and broaden some configuration wrappers;
they do not establish new numerical thresholds for those earlier theorems.

**The previously listed age-8/25/26 inverse results are now integrated.** Entry `f8023c`
gained Human Verified and Kit Contribution. Its constructive two-branch inverse and
age-26 top-band/age-25 twin theorems landed after catalog corrections. The twin-off-orbit
statement keeps the immortal-orbit hypothesis and even age at least 26.
[PR #292](https://github.com/WolframInstitute/Rule30PrizeKit/pull/292).

## Corrections and integration caveats

- `ce25c3` and `5809bd` have identical Lean bytes, SHA256
  `bc56e268f5b28822dbddecebf49c67f4abad9604213521cdb85d78bc62f099b6`.
  Neither record declares supersession. Both cite the same kit integration.
- `20d647` advertises non-finiteness of `Theta (free j)` for every j, but
  `theta_not_finSupp_all` requires **j≥2** in both the submission and kit main.
- `773383` advertises nonzero strip output with an arbitrary right boundary, but its
  theorem fixes that boundary to white. With width one and both boundary bits black,
  the advertised unrestricted statement is false: `(1 xor 1) mod 2 = 0`.
  This is a prose error, not a defect in the checked theorem.
- `08e81b` supplies **a mismatch witness** in each affine strip. It does not confine
  every mismatch to that strip; arbitrary right tails remain allowed.
- `8b6538` advertised spatial Problem 2 identities already present under other names.
  The maintainer requested their removal, and main integrates only the five new
  diagonal/masking helpers. [PR #309 discussion](https://github.com/WolframInstitute/Rule30PrizeKit/pull/309#issuecomment-6830806337).
- The prior `150836`/PR #294 issue is resolved in the integrated source: the unsupported
  `problem3_of_linear_causal_excursion` theorem was removed. The causal-box and conditional
  round-trip bounds landed, and the portal gained Kit Contribution but not Human Verified.
  Its old abstract still advertises the removed reduction. [Maintainer request](https://github.com/WolframInstitute/Rule30PrizeKit/pull/294#issuecomment-6808993944).
- **PR #323 is open with a concrete build failure.** `Rule30WhitePadding10101` uses
  `Rule30WordRotation.eventuallyWord_swap` without importing its module. The missing
  import is still absent at head `c41a48ecde9d759d36bc5524d0f47161f5b48996`.
  Its portal entry is Lean Verified and Human Verified but not a Kit Contribution.
  [Build review](https://github.com/WolframInstitute/Rule30PrizeKit/pull/323#issuecomment-6840283975).
- **PR #331 remains open** at `e7db8c2d` (full hash in the evidence manifest); entry
  `e00ea8` is Lean Verified, with neither additional badge in this snapshot.
  [PR #331](https://github.com/WolframInstitute/Rule30PrizeKit/pull/331).

## Complete new-entry inventory

Every row is a portal partial result and Lean Verified. **H** means the portal also shows
Human Verified; **K** means Kit Contribution. The short descriptions retain the relevant
guards and distinguish derived statements from new threshold claims.

| Entry | PR | Badges | Subject and checked scope |
| --- | --- | --- | --- |
| [12dcc6](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-12dcc6) | [#298](https://github.com/WolframInstitute/Rule30PrizeKit/pull/298) | H K | **Period-two onset at arbitrary columns.** Width-5/6 forbidden words and free-bit constraints transfer to either neighbor. Sampling is every two ticks at the alternating column’s white phase, from T+2. |
| [286d9c](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-286d9c) | [#299](https://github.com/WolframInstitute/Rule30PrizeKit/pull/299) | H K | **Right-shifted aperiodic bands.** A black diagonal J from T_J gives rightmost usable column min(0,J−T_J), with P>J and the onset guard. Short/long gluing retains its universal hypotheses. |
| [bf2edf](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-bf2edf) | [#300](https://github.com/WolframInstitute/Rule30PrizeKit/pull/300) | H K | **Error-edge dynamics.** Unique least error, persistent wheel-zero difference, and conditioned jump/heal/stall laws for jumps 2–7. No uniform capture conclusion. |
| [e26559](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-e26559) | [#301](https://github.com/WolframInstitute/Rule30PrizeKit/pull/301) | H K | **Two-block marginals.** Complement identities, incoming-black counts, and an equivalent form of Problem 2. These supply identities, not a density estimate. |
| [3aa660](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-3aa660) | [#302](https://github.com/WolframInstitute/Rule30PrizeKit/pull/302) | H K | **Period-12 travelling code.** For the existing 34-cell encoding, co-moving return iff 12 divides the time, spatial period 34k iff code period k, and explicit moving-coordinate readout. |
| [ba869b](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-ba869b) | [#303](https://github.com/WolframInstitute/Rule30PrizeKit/pull/303) | H K | **Difference-field algebra.** XOR cocycle, masking/front gate identities, rooted-front uniqueness and causal agreement on x≤m−n after n ticks. |
| [08e81b](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-08e81b) | [#304](https://github.com/WolframInstitute/Rule30PrizeKit/pull/304) | K | **Moving-wall regions.** Explicit intact affine half-planes for Ring57/Ring63, a mismatch witness in each affine strip, and multi-period displacement bounds. The entire mismatch set is not bounded by the strip. |
| [6f501a](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-6f501a) | [#305](https://github.com/WolframInstitute/Rule30PrizeKit/pull/305) | H K | **Canonical four-strip phases.** One of four strips and a canonical phase below 16 through depth 87866; phase uniqueness from depth 400 and explicit fork identities. |
| [ca6d07](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-ca6d07) | [#306](https://github.com/WolframInstitute/Rule30PrizeKit/pull/306) | H K | **First-fork phase uniqueness.** Canonical phase through 53207, two exclusive alternatives at 53208, and anti-periods 1,2,4,8 at wheels 3,8,29,400. |
| [ca0178](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-ca0178) | [#307](https://github.com/WolframInstitute/Rule30PrizeKit/pull/307) | H K | **Uniform ether pinning.** Across 28 alignments the ether is intact at x≤−38 from t≥222, with a mismatch witness in [−37,15], under the specified initial half-line agreement. |
| [ce25c3](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-ce25c3) | [#308](https://github.com/WolframInstitute/Rule30PrizeKit/pull/308) | H K | **Four-front onset bounds.** Branch-specific sufficient onsets through 87866 and agreement through 400 by strip tick 783 (own-clock onset ≤798). Same Lean bytes as 5809bd. |
| [8b6538](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-8b6538) | [#309](https://github.com/WolframInstitute/Rule30PrizeKit/pull/309) | K | **Diagonal readout helpers.** Five diagonal/masking helpers integrated. Advertised spatial two-block identities and Problem 2 equivalence already existed and their duplicate wrappers were removed from the PR. |
| [5809bd](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-5809bd) | [#308](https://github.com/WolframInstitute/Rule30PrizeKit/pull/308) | H K | **Duplicate four-front entry.** Byte-identical to ce25c3; neither portal record declares supersession. Counted separately by the portal, not as another mathematical result. |
| [a1239b](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-a1239b) | [#310](https://github.com/WolframInstitute/Rule30PrizeKit/pull/310) | H K | **Settling-front recurrence.** 16-bit reconstruction, simplified white/nonzero-wheel recurrence, F(w,j)≤16j and the shift-budget bound. Nonzero word does not mean an all-black diagonal. |
| [346be8](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-346be8) | [#311](https://github.com/WolframInstitute/Rule30PrizeKit/pull/311) | H K | **Seed A0 onset sharpened.** Per-wheel sufficient onset F(wdA0,j) through 87866, uniform onset 176968, wheel 400 from 783, and early white/black locks. No least-onset theorem. |
| [4f960e](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-4f960e) | [#312](https://github.com/WolframInstitute/Rule30PrizeKit/pull/312) | H K | **Ether-wall witnesses.** All-time left-ether invariants, right light-cone bounds and coupled period-four witnesses. Their infinite left ether is not a finite-support seed. |
| [faa565](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-faa565) | [#313](https://github.com/WolframInstitute/Rule30PrizeKit/pull/313) | H K | **Exact ether witness breakdown.** Named witnesses fail at exactly Lw(k), k≥1. Also Lw(k+6)=Lw(k)+4 and Rw(t+4)=Rw(t)+6; these do not assert a common first failure time for all states. |
| [571df5](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-571df5) | [#314](https://github.com/WolframInstitute/Rule30PrizeKit/pull/314) | H K | **QP divisibility and phases.** Divisibility antitonicity and all-phase one-black exclusions conditional on QP(P); quotient/remainder index laws. Q01 remains open. |
| [d0ac23](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-d0ac23) | [#315](https://github.com/WolframInstitute/Rule30PrizeKit/pull/315) | H K | **Driven lock families.** Period-5/7 readout laws for specified 49/57/74-cell prefixes, all-time lock5 trap containment and incompatible sampled periods. These are alternating-boundary histories. |
| [919dca](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-919dca) | [#316](https://github.com/WolframInstitute/Rule30PrizeKit/pull/316) | H K | **Spatial lifting and local charges.** All-black driving gives a three-cycle, illustrating the white-cell assumption in two-period lifting. Constant-word conserved charges agree by the existing classification. |
| [b07a87](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-b07a87) | [#317](https://github.com/WolframInstitute/Rule30PrizeKit/pull/317) | H K | **Ensemble parity and backward tubes.** Constant ensembles annihilate after the prescribed crop; conserved charges equal vacuum charge. Backward chains retain their finite predecessor certificates. |
| [20d647](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-20d647) | [#318](https://github.com/WolframInstitute/Rule30PrizeKit/pull/318) | H K | **Common-gauge escape and delayed defects.** Right-wedge dichotomy with Mode/Common/support hypotheses; dyadic escape and tail-period consequences. Theta(free j) non-finiteness requires j≥2. |
| [8cb8b7](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-8cb8b7) | [#319](https://github.com/WolframInstitute/Rule30PrizeKit/pull/319) | H K | **Padding and strip encodings.** Specializations of padding exclusions, maintenance identities, encoding injectivity and finite-configuration forbidden-suffix transport with certificate/width/onset guards. |
| [97d82f](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-97d82f) | [#320](https://github.com/WolframInstitute/Rule30PrizeKit/pull/320) | H K | **Restricted backward tubes and six-tail corollaries.** Guarded backward-tube laws; one-black exclusion for P≥78 and short monochromatic tails after r≥77. Later wrappers give P≥75; neither threshold is the strongest seed-only bound. |
| [773383](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-773383) | [#321](https://github.com/WolframInstitute/Rule30PrizeKit/pull/321) | H K | **Vacuum and padding APIs.** Zero encoded strip iff all cells white, certificate-based finite padding exclusions and vacuum predecessor identities. Nonzero output under a black left boundary requires a white right boundary. |
| [a255a6](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-a255a6) | [#322](https://github.com/WolframInstitute/Rule30PrizeKit/pull/322) | H K | **Sparse checks, pulses and traps.** List/bitmask equivalence under state-width bounds, stripe identities, finite pulse wrappers and spacing after a certified trap entry. Trap entry is assumed. |
| [6984e8](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-6984e8) | [#324](https://github.com/WolframInstitute/Rule30PrizeKit/pull/324) | H K | **Rotation and six-tail wrappers.** Bidirectional word rotation, P≥75 one-black and split-padding exclusions for nonzero left-bounded configurations, and backward/suffix certificate wrappers. |
| [c97d56](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-c97d56) | [#325](https://github.com/WolframInstitute/Rule30PrizeKit/pull/325) | H K | **All-column period-two reductions.** Iterated sideways shift and translation of Q01/CQ01 reductions to all columns. Q01 is a hypothesis and the finite version an equivalence, not a proof of period-two exclusion. |
| [cd05ee](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-cd05ee) | [#326](https://github.com/WolframInstitute/Rule30PrizeKit/pull/326) | H K | **Finite black runs and diagonal periods.** Finite configurations inherit 0 1^k exclusions for k≥9 and 1^r 0 for r≥18; dyadic right periods from zero and left periods from 2^i−1. Period bounds need not be least periods. |
| [53dd1a](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-53dd1a) | [#327](https://github.com/WolframInstitute/Rule30PrizeKit/pull/327) | H K | **One-bit return and congruence.** P-periodic prefixes extend with return by 2P; the birth bit decides return at P. LowEq equals congruence modulo 2^n. No universal least-period doubling claim. |
| [df8184](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-df8184) | [#328](https://github.com/WolframInstitute/Rule30PrizeKit/pull/328) | H K | **White-end word forms.** Every column of a nonzero left-bounded state excludes 1 0^q for q≥10; seed center excludes 0^q 1 for q≥9 by rotation of the existing white-end theorem. |
| [4707a9](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261113-4707a9) | [#329](https://github.com/WolframInstitute/Rule30PrizeKit/pull/329) | H K | **Finite white runs and column distinction.** Finite-configuration 0^r11 exclusion for r≥8, envelope closure and column equality iff agreement through max(\|p\|,\|q\|)+18. The distinguishing horizon was already proved. |
| [fe269f](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261113-fe269f) | [#330](https://github.com/WolframInstitute/Rule30PrizeKit/pull/330) | H K | **Trace merge and depth-two rigidity.** Word-form r≥8 exclusions; two specified initial states merge after one step. Left edge exactly −2 plus four matching center observations determines the nonpositive initial half-line. |
| [fc823f](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261112-fc823f) | [#323](https://github.com/WolframInstitute/Rule30PrizeKit/pull/323) | H | **Finite padding and absorption bundle.** Finite wrappers for five pumping families, joint threshold 31, width-5 examples at 61, qualified single-cell/high-support absorption, and rotated split 10101 padding at 69. PR build fix pending. |
| [e00ea8](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261113-e00ea8) | [#331](https://github.com/WolframInstitute/Rule30PrizeKit/pull/331) | — | **Spacing and controlled-response corollaries.** Period-31 transformed gate remains non-spaced; positive shifts repair NearSpaced; terminal response reductions 0101→01 and 1011→11; periods of existing counterexample profiles. PR open. |

## Kit and receipt coverage

Kit main advanced by **34 commits**, changing 59 existing Lean modules and `lean/README.md`.
There are no new module files and no changes under `equivalents/` in this interval.
The 36 relevant PRs comprise 34 now closed and #323/#331 still open. The closed PR API
records have no merge timestamp; their integration is established by main’s commits and
source comparison. Of 60 landed PR-head module files, 59 are byte-identical to current main.
The remaining file, PR #301’s `Rule30TwoBlockCounts`, is byte-identical to its own
integration commit `7c6b9a394efe996eb4d7d52d5c3aafa938df560a` and was extended by #309.
The eight module files in the two open PRs remain distinct from main.

All 36 PR descriptions, conversation comments, inline comments and review-summary bodies
were retrieved separately, including closed PRs. There were eight conversation comments
and no inline or review-summary bodies. Earlier build/catalog requests on #292, #299,
#302 and #327 were followed by integration at the inspected heads. #294 and #309 underwent
the substantive scope corrections described above. #323’s build request remains pending.
No linked external proof archive requiring an additional read was identified in these discussions.

| Complete refresh file | SHA256 |
| --- | --- |
| `stamp.json` | `cde71833102c8f45f0932c6cd059434897418244e6f57e2f053d4b9f471f6e86` |
| `checked.json` | `8e693582176cf1bc51dacfebf11a4d9a109e67f4bf2456d8ea02a638e2470830` |
| `portal.json` | `620e8c9b36580c9e34e997b3c78019a694630126843287cd4bbd0dd5986f4b00` |
| `prs.json` | `0b23136f2d07ebefbd0a4976fab2c2d553961bda76685c308dba18ca80157293` |

Evidence archive: `cited/gpt/gc2938-portal-kit-20261113.tar.gz`, 2,313,240 bytes,
SHA256 `fde2c166acc1e957d1fceae7fe1521661cfb0f505ccf6eaa94cb943b2c33bd1a`.
It includes before/after index snapshots, the 37 relevant portal sources, exact changed main
and PR-head files, prior-source comparisons, 144 PR API receipts, summary self-checks and
a SHA256 manifest. Raw evidence stays outside git.

Both schedules remain paused. This update does not discharge the pending Mahler carrying
reads or restart parked research. The next external follow-up is PR #323’s import/build repair
and PR #331’s disposition on the next owner-requested refresh.
