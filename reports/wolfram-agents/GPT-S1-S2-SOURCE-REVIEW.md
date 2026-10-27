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
