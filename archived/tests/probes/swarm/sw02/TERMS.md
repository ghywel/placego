# SW-02 terms, aliases and gates

*Frozen with the design at Wave 0. Conventions for every agent. Section numbers are the design's.*

## 4. Terms

Every agent gets these definitions and one shared reference library, so that no agent re-derives a convention. The library is `ref.py`; its self-test prints the smallest cases (guards G1, G11).

- **Row, F, G.** A natural number Y is a finite row: bit i is the cell at depth i + 1 behind a white wall.
 F(Y) = (Y >> 1) xor (Y or (Y << 1)) is one step, and G = F∘F. F adds exactly one to the width of a nonzero Y
 (kit: `IntegerForm.testBit_F_succ_of_top`).
- **Q01.** Every natural reaches an even number under some iterate of G (`Rule30ZeroBoundary.Q01_iff_integer`). Open.
 It excludes period 2 for every finite configuration.
- **Survivors.** S_W(t) = #{0 ≤ Y < 2^W : bit₀(F^(2s)(Y)) = 1 for every 2s ≤ t}; t is a **physical tick**,
 inclusive. For W ≥ 1 and 0 ≤ t < W, S_W(t) = 2^(W − floor(t/2) − 1); in particular
 S_W(W−1) = 2^floor(W/2), the exact `count_constrained` checkpoint. S_0(t)=0 for t≥0; the kit's
 empty constraint interval is a different count. Beyond the proved range the table is finite computation, with a coin model only a heuristic. The table
 below is Local's retained observation, not an asymptotic law:

 | W | t = W − 2 | W | W + 2 | W + 4 | W + 6 | W + 8 | W + 10 | first t with 0 |
 |---|---|---|---|---|---|---|---|---|
 | 12 | 64 | 38 | 9 | 3 | 2 | 2 | 2 | 30 |
 | 14 | 128 | 57 | 26 | 15 | 14 | 7 | 7 | 32 |
 | 16 | 256 | 112 | 63 | 34 | 19 | 16 | 13 | 32 |
 | 18 | 512 | 251 | 147 | 72 | 43 | 33 | 22 | 32 |

- **Free bits, check bits, K, Theta.** The odd-time values of column −1 are free, and each row bit is then fixed:
 `Theta f` is the row of the free word f. K is the set of rows that stay odd for ever, a Cantor set on which G is the
 shift of the free bits (`two_step_shift`). Q01 says K contains no natural (`Q01_iff_Theta`).
- **Death time.** D(W)=max over 0≤Y<2^W of the first even physical tick with bit₀(F^t(Y))=0, allowing ∞ if
 one never dies. Width means **at most** W. D(52)=96 has the public exact theorem `death_time_52_exact`
 (R30-20261023-8e6bd3); D(56)=100 and D(60)=114 combine matching lower witnesses with Local's kernel-checked
 upper certificates (L816/L818), not a claim that every full certificate passed the portal. D(76)≥138 is a
 kernel-checked lower bound. No verified asymptotic law is asserted.
- **CQ01.** Weaker than Q01 and sufficient to exclude period 2 for finite configurations: no finite left half and
 finite right half are coupled to the alternating column (`Rule30PeriodTwoCoupled.CQ01`). For each **finite** R,
 CQ01 asserts ¬FinSupp(Psi R). **CQ01Empty** fixes R=∅. **Q01Gap** says that whenever the complement of a free
 word eventually has black gaps 3 or 5, its Theta row is not finite (`Rule30GateTrap.Q01Gap`). It suffices for
 trap-entering R, including ∅; no Q01Gap⇒all-CQ01 arrow is asserted.
- **Frames.** F here is the zero-boundary half-row map, not an unqualified whole-line evolution or the right-edge
 map T. Each transfer names its coordinates, boundary, padding and time units. Finite F-images can merge; that
 statement does not transfer to whole-line finite configurations.
- **Count** and **amplification.** One proposed route combines an upper count with a mechanism forcing many distinct
 survivors. A bound strictly below 1 proves an integer count is zero;
 a bound still allowing one, or a zero-density/almost-sure result, does not. Amplification is sufficient, not a
 necessary shape of every proof. A transfer must specify the input population, output width, survival horizon,
 distinctness and any fibre multiplicity. Read GC1882, CL637 **with GC1883/CL638 corrections** before inventing it again.
- **Fixed width and limits.** To prove Q01 it suffices to prove ∀W ∃t S_W(t)=0. Allowing W to grow with t can
 leave arbitrarily long survivors without one immortal natural. A compact limit of finite rows may have infinite
 support. Every compactness or density argument must preserve its claimed population.

## 4a. Aliases and name checks (Cloud, draft 3)

The record names one object several ways, and a search that misses the other names re-derives what the record holds
(one identity of §8.66 was re-derived as new in CL740). Every reader and every record skeptic searches under every name in its row. Statuses
are the record's, with their sources; the derivations behind the last two rows are in
the design review §3.

| Object | Names in the record | Frame | Status in the record |
|---|---|---|---|
| The edge of the ordered left side | error edge (CL740; `Rule30ErrorEdge`), band edge (atlas §9.1, §15), settling front and actual front (§21.6), damage front (§8.66; CL741), news front (§8.74; §19) | wall frame: wheel j at tick t is the cell x = j − t from the leftmost black cell (`Rule30FiniteDiagonals.Ld`) | never retreats, heals iff its parent is black (PROVED, kit); its long-run speed is close to the left damage front's: the seed's windows give 0.7588, nine random ring runs 0.7564 ± 0.0003, so λ_L = 0.2436 ± 0.0003 (MEASURED, CL742; Grassberger: 0.2428 ± 0.0003); that these are one constant is CONJECTURE (atlas §21.8, §21.9); the finite chains M(L, R, W) extrapolate to 0.7562 ± 0.0005 (CONJECTURE, GC2682) |
| A heal, a stall, a jump | the death of the edge's error, a wait, the edge's step; the forced stall after a jump of 2 (CL691/GC521, CL722) is `jump_two` | wall frame | p = q/(q + S) with S the share of heals onto a white parent and q the stall hazard (PROVED two-party, GC2682/CL743); the jump facts 2 to 7 (PROVED, kit) |
| The strip's walk | the one walk (§20), the forced front (`Rule30FourFronts.walk`), the settling recursion (§21) | strip time | wheel j of every left-finite configuration carries its strip from the forced tick F j, about 2 j (F 87,866 = 176,968 on A0) (PROVED, kit, whole-line, through wheel 87,866); the actual settling runs ahead of it at about 1.32 ticks a wheel through the coincidences (MEASURED, §21.6; its limit is open, B2) |
| The left sides | the universal strip and its forks (`Rule30UniversalLeftSide`), the four strips (`Rule30FourLeftSides`), the sixteen strips below 894,235 (tree16, §21.10) | wall frame | one shift aligns every left-finite configuration with its strip (PROVED through 87,866, kit); the sixteen are sixteen settings of fifteen switches, each thrown by one cell at a fork's child (COMPUTED, §21.10); the branch law (PROOF-SKETCH, 24 of 24) |
| The far edge and the wall | the far edge is the leftmost black cell and moves out one depth a tick (`zrow_edge`; `testBit_F_succ_of_top`); the wall is depth 0 of the zero-boundary frame, column 0, and in wheels it is wheel W + t at tick t for a row of width W | zero-boundary (§4) and wall frame together | causality runs from the far edge to the wall only; on the rows measured the two frames are joined by the chaotic region between the band edge and the wall, about W + 0.243 t cells wide (MEASURED; an immortal row is outside those populations; that it grows for ever is CONJECTURE) |

**Name checks on kit main `5ad29d6`** (two commits past GC2686's `9af60de9`: #186 `Rule30PeriodFourSkeleton`, #187
`Rule30EtherThreeSkeleton`; Cloud's clone, fetched 5 November 22:10 GMT): every theorem this document names is defined
there, with three notes. `IntegerForm` is a namespace inside `Rule30ZeroBoundary.lean`, not a module.
`death_time_52_exact` is a portal theorem (R30-20261023-8e6bd3, MAP row 12), not on kit main: cite the entry.
`white_shift` is defined in both `Rule30FourFrontsBase` and `Rule30LeftReset`: cite the module.

## 6. The gates


a source-matched theorem can reject a candidate in its exact class; observations and heuristics
cannot. Screeners must write the matching hypothesis and the failed step. An uncertain rejection goes to a skeptic.
Novelty, proof validity, usefulness and resource feasibility are separate judgments. Gates 4, 6, 8 and 9 are diagnostics.

| Gate | Exact check | Standing and scope |
|---|---|---|
| 1 Siblings | If the proposed proof uses only hypotheses also true for a counterexample rule, identify the unsupported Rule-30 step | `Rule30Realization.barrier`; applies to that hypothesis package, not every lemma or every prize |
| 2 Rankings | Match `RankCert` or the actual finite-abstraction/local-ranking theorem, including strict descent and target domain | Q01 stripe barriers exist. **Coupled B1 is already proved** by `Rule30PeriodTwoSideways.no_finite_abstract_ranking_coupled` using `alternates_long`; do not recreate it |
| 3 Two-sided witnesses | Periodic-left witnesses refute arguments omitting left finiteness; `JointCert` also allows both edge positions and fixed windows | `alt_coupled_left_periodic`, `no_joint_local_ranking`: latter descends at every centre flip over all finite configurations. Seed-reachable-only predicates require a separate match |
| 4 Single exceptional row | Show an upper bound below 1, a competing amplification, a descent, or another pointwise exclusion | Diagnostic, not an amplification requirement |
| 5 Onset | An eventual-periodicity proof must justify its time shift and keep finite support after the shift | `Rule30PeriodTwo.normalize`. Initial-time lemmas may be valid intermediate steps |
| 6 Random-word control | If using the observed coin law, show why the argument distinguishes its target from the control population | MEASURED similarity is not a theorem that all methods must exploit periodicity |
| 7 Conservation | Match four-step integer cyclic conserved densities, four-step mod-2 product scores, or homogeneous one-step group cocycles | All widths in `Rule30LocalConservation`, `Rule30ProductParity`, `Rule30GroupCocycle`. **Not** a ban on dissipative potentials, constrained-orbit invariants or noninvertible transport |
| 8 Local information | Name the allowed observations/certificates, then exhibit indistinguishable cases with different required conclusions if possible | No general theorem says every Problem 2/3 proof must reach an edge. BR-1 is a restricted-information question |
| 9 Entropy | Identify the missing pointwise statement when a measure/entropy estimate is used on one finite seed | Positive entropy alone neither proves nor forbids emptiness of a particular intersection |
| 10 Realisation | Arbitrary trace realisation uses an unrestricted half-row; check which finiteness/history hypothesis a proposed forbidden word uses | `column_realizable_unique`; it does not negate every forbidden-word statement on a physical restricted family |
| 11 Population | Name Q01, coupled finite configurations, fixed R, fair-input surrogate, actual finite-history front, or single seed | No silent transfer between them; state every projection or conditioning |
| 12 Time scale | Check any proposed universal deadline against verified D(W), including D(76)≥138 and additive constants | This finite checkpoint is **not** an asymptotic slope ≥1.8 |

An accepted intermediate lemma need not solve any prize. A conditional bridge is useful if its hypothesis is weaker,
more testable or more structural than the target, with that comparison explained.

