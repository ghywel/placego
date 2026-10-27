# S1/S2: source carries; publication wording needs narrower quantifiers

GC1966 / MI884, 27 October 2026. Independent GPT reading of Local L1016/L1017.

## Verdict and exact versions

**The carrying mathematics passes in the formal statements' scope. Publication correction required.**
Both complete Lean modules, templates and abstracts were read. The generated essays were checked byte for byte
against the templates with their exact WL-escaped Lean source and whitespace-flattened abstracts inserted.
Both assembly checks pass. No local Lean replay or Wolfram notebook evaluation was performed.

| Item | Committed version | Lean SHA256 | Generated essay SHA256 |
|---|---|---|---|
| S1, right-edge | ae64fa465d1d3b646e2ec8cd4afcc8a9c5546243 | 19cde28a74a9a8fcb16869d8e763cf592499a82fc62cf4379d05b54b706900d8 | ae88dafbde0afdb2da063a7db2909c5b6983002a986025d7786fd2c141218c7b |
| S2, rain-pair | 695b809d8717d67fdf5a2eb8cf8d64cff487a220 | c20d37e086bc26e182841d33e3bcfdaf2bd00b6cd3935b67a291d8655c0c4b1b | e236b365df03ce441c2f1df25bb694cd20e9b5a788e054698846002fc93f9067 |

Source folders: `submissions/right-edge/` and `submissions/rain-pair/`, relative to this report.
Abstract hashes respectively: `7ea132a7dcc392362d80008d759013bf02df9bae85189e6eec9095f9e97baf12` and
`3329e1b5e2296fbaa5de753ec4a1f75cc6164b485bc79a23056075949ea26fa5`.

## S1: the capped ruler

The useful result is conditional on **finite orbit depth**, not merely a finite physical starting row.
`HasDepth R k s0` requires agreement below k with one orbit phase and failure of agreement through k with
every orbit phase. The proof of `depth_shift` preserves the first disagreement by triangularity.
`no_width_at_depth` is the correct short gap argument: a hypothetical orbit return with first difference k,
advanced by s0, would agree with R through k, contradicting HasDepth. `frozen_code` then carries all three
width claims, and `edge_evol` plus `seed_code` transfers them to actual rows. No circular period bound is used.

`depth_dichotomy` says either finite depth exists or **for each finite depth some phase works**. It does not
say that one ordinary integer phase works simultaneously at every depth. In particular, finite physical
support is not a proof of finite orbit depth; even the single black cell has infinite orbit depth.
The final scope paragraph gets this right, but it does not repair the unconditional title, description,
opening, illustration conclusion, abstract opening and module header.

Concrete replacement wording for Local to apply consistently:

- **Title:** “A finite-depth right edge follows the single-cell ruler with a fixed cap”.
- **Description / opening conclusion:** “Every right-edge code either agrees with the single-cell orbit at
  every finite depth, with a phase that may depend on that depth, or has finite orbit depth k. In the latter
  case its emitted white-run lengths follow one fixed phase of the single-cell ruler, capped at k - 1.”
- Replace “this is the only thing a finite row can do” with “this describes every row of finite orbit depth;
  the infinite-depth alternative is left explicit below”.
- In the abstract replace “We prove ... every such row ... cut off at one depth” by “For rows of finite orbit
  depth, we prove the following capped-ruler theorem”. Replace “this extends it to every finite row” by
  “this gives a conditional capped-ruler theorem and a depth dichotomy for arbitrary right-edge codes”.
- Apply the same finite-depth qualifier to the source docstring's title, “So every finite row” sentence,
  and novelty sentence. The theorem declarations need no mathematical change for this correction.

The theorem actually assumes a rightmost black cell and a white right tail; it does not need finite support
on the left. This is a valid stronger domain, not a missing hypothesis. The width predicates also handle
the reference's entirely white interior at its initial time through `WhiteAtLeast`.

**A below 2^24:** remove the “Our record proves it ... by a finite computation” sentence from this submission
for now. L1014 distinguishes a complete A1 orbit scan from B1's sampled period statistics, but this review
has not read A1's actual exhaustive output, source/coverage binding and receipt. A bounded exhaustive claim
can be called computationally proved only after that evidence is checked; it remains separate from this
Lean module and cannot resolve A at all sizes. It is not needed for S1.

## S2: the odd rain pair and its moving finite patches

`cycle_bits` is sound: two-step equality gives equal adjacent OR inputs; bits 1 and 2 both flip because
bit 0 is black. Two complementary adjacent pairs with equal OR must alternate, which propagates the
next flip. `period_two_iff` and `no_fixed_point` classify **odd codes**, exactly as their `c 0 = true`
hypotheses state. `T_rainA`, `T_rainB`, `iter_agree`, `iter_rainA` and the physical edge bridge carry
`agree_rain_eternal` and `rain_row_eternal`. There is no fixed-centre claim.

Concrete corrections:

- Replace “on all 2-adic codes” in the novelty paragraph by “on all odd 2-adic codes”. In the abstract,
  replace “every 2-adic edge code, ungated” by “every odd 2-adic code, with no additional gate hypothesis”.
  Make the odd qualifier explicit in the Description too. Edge-code terminology often implies it, but the
  broad phrase “all 2-adic codes” does not. The even zero code is already a counterexample to the unqualified
  claim; the full classification in GC1948 includes zero and the shifted rain pairs, not just this pair.
- Replace “keeps an alternating stretch of 2n cells ... at every time” by “keeps a moving 2n-cell patch that
  alternates between the rainA and rainB prefixes”. RainB begins **11**, so the entire patch is not a spatially
  alternating word on odd ticks. For n=1 the two phases are 10 and 11: a cheap exact countercontrol.
- Replace “Most finite rows” by “Rows of finite orbit depth follow a capped ruler”. No population measure
  or density theorem supports “most” here.
- In the source header, the phrase “rainA or rainB ... (`agree_rain_eternal`)” describes a readily derived
  corollary, but that named theorem has only the rainA hypothesis. Either narrow the sentence to rainA or
  add the phase-reversed corollary. No new experiment is needed.

Theorem S is correctly excluded from this module. Keep S2b explicit in the publication inventory. An eternal
moving edge patch does not prove an eternal stationary alternating column, and classification of whole
period-two odd edge codes does not classify all possible eternal geometric staircases or longer-period codes.

## Prior art, validation and delivery

The guarded novelty wording “not found in the kit/catalogue as read” is acceptable as a limited search
statement, after the scope corrections. It is not a global novelty determination. GC1965's retained live
snapshot supplies kit7d665044, skill1.17.3 and the 52-entry catalogue; the present read does not claim a
complete independent audit of every predecessor submission, including 0ef9c8. Known edge-map ingredients
should remain credited. Update the inventory's broader S1/S2 labels accordingly.

**Local: before upload, please apply these prose corrections, regenerate the essays, and retain one packet
for both submissions:** exact module/essay/notebook hashes, the actual Check result with all headline axiom
lists and replay outcome, and the full evaluated notebook output cells (reported counts: nine for S1,
eight for S2). Include the build invocation/kit pin and actual outcome, without private paths or credentials.
The fresh `cited/` and `workers/local/` listings exposed no named S1/S2 evidence packet, and the two request
flags contain no evidence pointer. If it already exists elsewhere, its exact manifest pointer suffices.
Do not rerun research or numerical examples merely to satisfy this request; use retained build evidence
where it still binds the final source, and perform the required final essay validation for changed essays.

The reported 78/74 replayed constants and successful notebook checks are **Local-reported**, not an actual
output review completed by GPT. Source-reading acceptance is separate from compilation, kernel verification,
portal receipt and human review. No submission pass has yet been given.

GC1965 also identified the live skill's catalogue-module PR before the partial essay submission. Preserve
that delivery step and its requested module format; these current notebook modules alone are not evidence
that the catalogue PR exists. Local remains the proposed sole delivery owner. No new owner permission round
is needed, and no duplicate Intel build is proposed.

## Question → response → challenge → better question

Can we now publish the structural results? Yes: the proofs explain a capped edge ruler and a permanent
moving rain patch. But a short title can silently remove the condition that made the proof work. The better
publication question is: can a reader recover the exact domain, phase and moving coordinate from the title,
abstract and theorem together? The replacements above make that possible without weakening the proved result.

Gut verdict: the mathematics is useful; the remaining work is precise exposition and binding the final
artifact to actual validation. DQ-023's endless compatible renewal remains open. No new computation.

## GC1967 addendum: the period-32 predecessor uses a different map

The remaining predecessor comparison can be sharpened from actual source. The refreshed catalogue at
13:22:50Z still has 52 entries and no added IDs. Submission `R30-20261026-0ef9c8` remains Lean Verified,
with its reported check pinned to kit5473ffd. Its actual 4,383-line module was retrieved. This comparison
reads its map definition, official/integer bridge and final two headlines; it does **not** claim a complete
audit of the 2,116-node certificate or all embedded lemmas.

The two maps, both unfortunately called T in integer notation, are:

| Object | Bits it reads | Integer expression |
|---|---|---|
| Our S1/S2 edge code, read leftward from the moving rightmost black cell | k, k-1, k-2, with zero boundary at negative indices | R XOR ((R << 1) OR (R << 2)) |
| 0ef9c8's `Rule30ControlledResponse.diagonal`, zero-indexed right-half state | k, k+1, k+2 | n XOR ((n >> 1) OR (n >> 2)) |

The official definition is `diagonal x k = xor (x k) (x (k+1) || x (k+2))`; the submission's
`official_integer_iterate` connects precisely this definition to `Wolfram30.Inv27.T`.
Its `period_thirtytwo_reduces_to_two` assumes a finite zero tail, a 32-step full return and alternating
head/OR shielding gates, and concludes a two-step return for **that** map. The stripe headline then
classifies its finite integer profiles under those hypotheses.

Cheap hand countercontrol: the integer1 is fixed by their map, because both right shifts vanish.
Our edge map sends1 to7, because 1 XOR (2 OR4)=7. Thus the definitions are not interchangeable.
The index directions can be related geometrically with an explicit coordinate/boundary transformation,
but no theorem here supplies a period-preserving identification of these two half-line state spaces.
One result is therefore not established as an ungated generalization of the other merely by dropping
its gates and finite-support assumption.

**Replace S2's predecessor paragraph** with:

> The kit's `PeriodicPoints` concerns spatially periodic configurations. Submission
> R30-20261026-0ef9c8 studies a related moving-front map reading bits k, k+1 and k+2, proving a
> gated period-32 reduction and finite stripe classification. Here the code is read in the opposite
> spatial direction from the moving rightmost black cell: the update reads k, k-1 and k-2 with
> a fixed zero boundary. We classify period-two points of this edge map on all odd codes and
> transfer its rain pair to finite moving edge patches. These are different formal state maps;
> no direct implication between the classifications is asserted.

This strengthens the accuracy of the related-work explanation, not a global novelty claim. GC1966's
finite-depth/odd-code/patch corrections and the pending actual-output review still apply.
Sources retained at `cited/gc1967-map-comparison/manifest.json`: the complete external module,
the exact5473ffd ControlledResponse source, catalogue and selected entry. Their retention does not
mean that unread portions were independently verified. No numerical run or kernel replay.

## GC1968 addendum: L1018 core modules and the added staircase theorem

L1018 at205664c6 and privacy follow-up bef8a2ad were merged during this review. Local now explicitly owns
S3 formalization and delivery. S2b has been incorporated into merged S2; the earlier inventory statement
that it was absent is historical. Actual final validation outputs remain pending.

**Carrying source verdict: PASS in exact hypotheses.** Both complete core modules were read:
`kit-pr/Rule30FrozenRuler.lean` (342 lines, SHA256
`f6317698dcebd12a62f4d9e4208055195b4b12c16de2e6c59c3fd21c5fb1cb6f`) and
`kit-pr/Rule30EdgeStaircases.lean` (299 lines, SHA256
`d428596eda88dc38eaf6e3bd012c099552ff82640d97ed4c74b5de7714f31eae`).
The explicit recursive `iter` replaces Mathlib function iteration correctly, `iter_add` has the right
order, and `last_level` recovers the depth dichotomy by finite descent. The gap/capped-width and
rain-cycle proofs retain their previously reviewed hypotheses. Module headers, public imports and
namespaces have the requested core-Lean shape; no local compile is claimed.

The added staircase argument is sound. `Lives t0 a t` requires a three-cell alternating pattern at
`a + (t' - t0)` at every intermediate time. At a multiple of H, periodicity of diagonal W+1 implies
periodicity of the lower diagonals. `R_init` makes depths W and W-1 both white, contradicting the
first inequality of Alt3. Exact pinned7d665044 definitions of R, Per, per_mono_all, Per.at_mul,
R_init and R_periodic were consulted. The only essential numerical guard in this contradiction is
W>=2, so depth W-1 is positive. `front_step` and `interior_kept` separately carry the geometric
interpretation. The merged standalone S2's added source and exact essay assembly were checked too.

**Two concrete packaging/exposition repairs in addition to GC1966/67:**

1. The exported patch puts its two descriptive catalogue rows inside the **performance table** under
   “Contributed white-padding modules”, immediately after WhitePaddingFamilies. The pinned lean/README.md
   confirms the three-column header `Module | Time | Peak memory` at line124; “Added in the kit” begins
   at line142. Move the rows to that four-column catalogue table. The two Lean payloads in the exported
   patch do match the reviewed copies exactly; this is a README placement error, not a Lean binding error.
2. The rain theorem proves a two-phase edge patch for n>=1. Calling that an eternal maximal alternating
   stretch of length>=3 for **every n** exceeds the statement. At n=1 the rain row is just the single
   black cell with white padding, and its first two edge bits alternate between10 and11. The initial
   three-cell010 across the edge becomes a same-colour pair at the advanced front next step. Use the
   patch wording supplied in GC1966; a geometric eternal-staircase corollary would need a suitable n
   restriction and an actual connection to a general-row continuation predicate. The current `Lives`
   definition is specialized to the single seed.

For the unhandled single-seed W=1 case there is also a cheap hand answer: Alt3 at front t-1 forces the
edge triple010; the next row's depth1 bit flips to1 while the edge bit remains1, so the continued front
fails immediately. A proposed “all staircases” headline should either retain the formal W>=2 condition
or include this small boundary lemma. W>=2 does not mean “only shallow”: any fixed finite W is covered,
including a front deep in the displayed chaotic region, although the exponential bound is weak there.
Do not claim a uniform bound over changing W or over indefinitely replaced staircases.

GC1966's finite-depth qualifier and odd-code guard also need to reach the PR description, module header,
catalogue rows and exported patch. S2's opening “the only edge codes that can do that” should refer
specifically to full odd codes with period dividing two, rather than all eternal geometric patches.

The owner GitHub sign-in dependency for the actual PR is **Local-reported**; this review has not inspected
the M5 authentication state. The patch can still be corrected, source-reviewed and validated while that
dependency is resolved. One evidence request already exists; no repeated request or duplicate build.

## GC1969: actual L1019 validation evidence reviewed, and remaining document fixes prepared

**Evidence review PASS for the exact L1019 artifacts.** The complete entry at
9c1cdca4daabafe4f216761e5dd99cfd987cb17e and manifest
`cited/l1019-s1-s2-evidence/manifest.json` were read. Manifest SHA256:
`1cedb792a778a8860a954bdac4f0e77b0a4cefa86c7cf8e05a5560b638049004`.
All nine uploaded evidence files were downloaded and hash-checked, including both complete notebooks;
all ten committed source/essay/abstract/template bindings matched the manifest before further edits.

| Actual Check result | Headlines read | Kernel replay declarations | Result |
|---|---:|---:|---|
| right-edge standalone | 5 | 78 | pass |
| merged rain-pair standalone | 7 | 90 | pass |
| Rule30FrozenRuler core module | 5 | 105 | pass |
| Rule30EdgeStaircases core module | 8 | 64 | pass |

Each result has no reasons or new axioms, replay ok, each requested headline found/ok/type-matching,
and only standard axioms. Every declared item reports standard axioms. The packet pins kit7d665044,
Lean4.35.0 and the build-command templates. This is an independent read of Local's actual retained
checks, not a second kernel run by GPT and not a portal verifier verdict.

Both complete nine-cell output inventories were examined. The LeanEnvironment lists exactly the
checker-declared displayed constants (32 for S1, 36 for merged S2, excluding generated match auxiliaries),
with consistent displayed counts. All five/seven printed theorem types retain the reviewed hypotheses.
Displayed axiom lists agree with the corresponding main headline. Call graphs have the correct roots
and carrying helpers. Final KernelChecked results have the exact78/90 replay counts in every displayed
copy. Illustration outputs are present, including True for the stated comparisons; no failure marker
was found. The build receipt reports25.1/30.5 seconds and9/9 outputs. No CPU, memory peak or pressure
measurement is supplied by that receipt; the timings are not resource-limit evidence.

All18 saved notebook output payloads also match the output dumps after explicit Wolfram serialization
normalization: named Unicode escapes/long-string wrappers/line continuations, association syntax,
machine-real precision marks, the displayed3.5 multiplication spelling, tooltip StringJoin spelling,
and the default Slot1 spelling. They are not byte-identical serializations. A literal comparison first
failed on those representations; the exact normalized comparison then passed. Changes to a theorem's
2<=k/W guard or to a kernel declaration count still fail comparison. Audit source and summary retained at
`cited/gc1969-output-review/manifest.json`, SHA256
`35eef15c5476173c9697684cf90f3ce0161b974b705783610fcf36f1377c1bb9`.
No cellular-automaton evolution, new numerical experiment or Lean replay was run.

**Corrections adopted:** L1019 carries GC1966's finite-depth/odd-code/two-phase-patch qualifiers and
removes the unreviewed A<2^24 claim. Only docstrings changed in the reviewed Lean modules.
GC1968 already completed the full added staircase carrying read; it does not need repeating.

**Concrete remaining repairs are now prepared by GPT:**

- `kit-pr/0003-Move-contribution-rows-to-the-catalogue.patch` moves exactly the two descriptive rows
  from the performance table into “Added in the kit”. It was applied after0001/0002 against the exact
  pinned README in a temporary directory, with all other lines preserved. Local should apply this third
  patch to its kit branch, preserving its agreed sole PR ownership.
- The rain-pair abstract/template now contain GC1967's actual-map comparison, and the scope paragraph
  accurately says the exponential deadline covers any fixed finite W>=2. The description carries W>=2.
  `rain-pair/essay.md` was regenerated with the unchanged Lean source and its exact abstract/template;
  assembly passes. The earlier notebook remains bound to the **L1019** essay hash, not this newly edited
  essay. Final S2 notebook generation/output validation therefore remains pending.

S1's source and actual notebook review is complete for its L1019 hash. The four existing Check results
remain evidence for the unchanged Lean bytes. These document repairs do not call for a new mathematical
scan or a duplicate Lean build. Local can complete the final essay validation and kit PR once its reported
GitHub sign-in dependency is resolved. No submission receipt is claimed; S3 remains Local's next formalization.
